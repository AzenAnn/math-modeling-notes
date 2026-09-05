from __future__ import annotations

import json
import logging
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import DocumentParseError, ParserUnavailableError
from .io_utils import (
    atomic_write_text,
    normalize_space,
    safe_filename,
    sha256_bytes,
    sha256_file,
    sha256_text,
    utc_now_iso,
    write_json,
)

LOGGER = logging.getLogger(__name__)
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff"}
_CJK = r"\u3400-\u4dbf\u4e00-\u9fff"


@dataclass(slots=True)
class ParseResult:
    parser: str
    normalized_markdown: Path
    structure_json: Path
    page_map_json: Path
    figures_dir: Path
    manifest_json: Path
    warnings: list[str]

    def as_dict(self) -> dict[str, Any]:
        return {
            "parser": self.parser,
            "normalized_markdown": str(self.normalized_markdown),
            "structure_json": str(self.structure_json),
            "page_map_json": str(self.page_map_json),
            "figures_dir": str(self.figures_dir),
            "manifest_json": str(self.manifest_json),
            "warnings": self.warnings,
        }


def _require_pymupdf() -> Any:
    try:
        import fitz  # type: ignore

        return fitz
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise ParserUnavailableError("PyMuPDF is not installed. Install modeling-mastery[pdf].") from exc


def _location_at(markdown: str, position: int) -> tuple[int | None, str]:
    page: int | None = None
    for marker in re.finditer(r"<!--\s*MM_PAGE:\s*(\d+)\s*-->", markdown):
        if marker.end() <= position:
            page = int(marker.group(1))
        elif marker.start() > position:
            break
    section = ""
    for heading in re.finditer(r"^(#{1,6})\s+(.+?)\s*$", markdown, re.MULTILINE):
        if heading.end() <= position:
            section = heading.group(2).strip()
        elif heading.start() > position:
            break
    return page, section


def _pages_from_markdown(text: str) -> list[dict[str, Any]]:
    markers = list(re.finditer(r"<!--\s*MM_PAGE:\s*(\d+)\s*-->", text))
    pages: list[dict[str, Any]] = []
    if markers:
        for index, marker in enumerate(markers):
            start = marker.end()
            end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
            page_text = text[start:end].strip()
            pages.append(
                {
                    "page": int(marker.group(1)),
                    "width": None,
                    "height": None,
                    "text": page_text,
                    "normalized_text": normalize_space(page_text),
                    "content_hash": sha256_text(normalize_space(page_text)),
                    "char_count": len(page_text),
                }
            )
        return pages
    return [
        {
            "page": 1,
            "width": None,
            "height": None,
            "text": text,
            "normalized_text": normalize_space(text),
            "content_hash": sha256_text(normalize_space(text)),
            "char_count": len(text),
        }
    ]


def _configure_tessdata() -> None:
    """Help PyMuPDF/Tesseract find the bundled language data on Windows."""
    if os.getenv("TESSDATA_PREFIX"):
        return
    candidates = [
        Path(r"C:\Program Files\Tesseract-OCR\tessdata"),
        Path(r"C:\Program Files (x86)\Tesseract-OCR\tessdata"),
    ]
    for candidate in candidates:
        if candidate.exists():
            os.environ["TESSDATA_PREFIX"] = str(candidate)
            return


def _normalize_ocr_text(text: str) -> str:
    """Remove Tesseract's artificial spacing while preserving paragraphs."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(rf"(?<=[{_CJK}])[ \t]+(?=[{_CJK}，。！？；：、）】》])", "", text)
    text = re.sub(rf"(?<=[（【《])[ \t]+(?=[{_CJK}])", "", text)
    text = re.sub(r"[ \t]+([，。！？；：、）】》])", r"\1", text)
    text = re.sub(r"([（【《])[ \t]+", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


def _ocr_page_text(page: Any, *, language: str = "chi_sim+eng", dpi: int = 180) -> str:
    executable = shutil.which("tesseract")
    if not executable:
        raise ParserUnavailableError("Tesseract CLI was not found in PATH.")
    _configure_tessdata()
    scale = dpi / 72.0
    fitz = _require_pymupdf()
    pixmap = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    completed = subprocess.run(
        [executable, "stdin", "stdout", "-l", language, "--psm", "3"],
        input=pixmap.tobytes("png"),
        capture_output=True,
        timeout=180,
        check=False,
    )
    if completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace")
        raise DocumentParseError(f"Tesseract failed with exit code {completed.returncode}: {stderr[-1000:]}")
    return _normalize_ocr_text(completed.stdout.decode("utf-8", errors="replace"))


def _extract_page_map(
    pdf_path: Path,
    *,
    force_ocr: bool = False,
    ocr_language: str = "chi_sim+eng",
    ocr_dpi: int = 180,
) -> list[dict[str, Any]]:
    fitz = _require_pymupdf()
    pages: list[dict[str, Any]] = []
    with fitz.open(pdf_path) as document:
        for index, page in enumerate(document, start=1):
            text = page.get_text("text", sort=True) or ""
            ocr_used = force_ocr
            ocr_error = ""
            if force_ocr:
                try:
                    text = _ocr_page_text(page, language=ocr_language, dpi=ocr_dpi)
                except Exception as exc:
                    text = ""
                    ocr_error = f"{type(exc).__name__}: {exc}"
            pages.append(
                {
                    "page": index,
                    "width": float(page.rect.width),
                    "height": float(page.rect.height),
                    "text": text,
                    "normalized_text": normalize_space(text),
                    "content_hash": sha256_text(normalize_space(text)),
                    "char_count": len(text),
                    "ocr_used": ocr_used,
                    "ocr_language": ocr_language if ocr_used else "",
                    "confidence": "medium" if ocr_used and text else ("low" if ocr_used else "high"),
                    "ocr_error": ocr_error,
                }
            )
    return pages


def _extract_embedded_images(pdf_path: Path, figures_dir: Path) -> list[dict[str, Any]]:
    fitz = _require_pymupdf()
    figures_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, Any]] = []
    seen_xrefs: set[int] = set()
    with fitz.open(pdf_path) as document:
        for page_index, page in enumerate(document, start=1):
            image_number = 0
            for image in page.get_images(full=True):
                xref = int(image[0])
                if xref in seen_xrefs:
                    continue
                seen_xrefs.add(xref)
                try:
                    extracted = document.extract_image(xref)
                except Exception as exc:  # pragma: no cover - malformed PDF dependent
                    LOGGER.debug("Image xref %s extraction failed: %s", xref, exc)
                    continue
                data = extracted.get("image", b"")
                if not data:
                    continue
                image_number += 1
                extension = extracted.get("ext", "png").lower()
                filename = f"page_{page_index:03d}_img_{image_number:03d}.{extension}"
                target = figures_dir / filename
                target.write_bytes(data)
                manifest.append(
                    {
                        "id": f"FIG-P{page_index:03d}-{image_number:03d}",
                        "page": page_index,
                        "path": target.name,
                        "xref": xref,
                        "width": extracted.get("width"),
                        "height": extracted.get("height"),
                        "sha256": sha256_bytes(data),
                        "source": "pymupdf-embedded-image",
                    }
                )
    return manifest


def _copy_backend_images(markdown_path: Path, figures_dir: Path, markdown: str) -> tuple[str, list[dict[str, Any]]]:
    figures_dir.mkdir(parents=True, exist_ok=True)
    image_pattern = re.compile(r"(!\[[^\]]*\]\()([^\)]+)(\))")
    additions: list[dict[str, Any]] = []
    replacements: dict[str, str] = {}
    for match in image_pattern.finditer(markdown):
        raw_path = match.group(2).strip().strip("<>")
        if re.match(r"^[a-z]+://", raw_path, re.I) or raw_path.startswith("data:"):
            continue
        source = (markdown_path.parent / raw_path).resolve()
        if not source.exists() or source.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        stem = safe_filename(source.stem, fallback="figure", max_length=70)
        destination = figures_dir / f"backend_{len(additions) + 1:03d}_{stem}{source.suffix.lower()}"
        shutil.copy2(source, destination)
        new_path = f"figures/{destination.name}"
        replacements[raw_path] = new_path
        additions.append(
            {
                "id": f"FIG-BACKEND-{len(additions) + 1:03d}",
                "page": None,
                "path": destination.name,
                "sha256": sha256_file(destination),
                "source": "parser-backend",
            }
        )
    for old, new in replacements.items():
        markdown = markdown.replace(f"]({old})", f"]({new})")
    return markdown, additions


def _parse_with_mineru(input_path: Path, scratch: Path, mineru_backend: str, timeout: int) -> tuple[str, dict[str, Any], Path]:
    executable = shutil.which("mineru")
    if not executable:
        raise ParserUnavailableError("MinerU CLI was not found in PATH.")
    output = scratch / "mineru_output"
    output.mkdir(parents=True, exist_ok=True)
    command = [executable, "-p", str(input_path), "-o", str(output)]
    if mineru_backend:
        command.extend(["-b", mineru_backend])
    LOGGER.info("Running MinerU: %s", " ".join(command))
    completed = subprocess.run(command, text=True, capture_output=True, timeout=timeout, check=False)
    if completed.returncode != 0:
        raise DocumentParseError(
            f"MinerU failed with exit code {completed.returncode}: {completed.stderr[-2000:]}"
        )
    markdown_candidates = sorted(output.rglob("*.md"), key=lambda path: path.stat().st_size, reverse=True)
    if not markdown_candidates:
        raise DocumentParseError("MinerU completed but produced no Markdown file.")
    selected = markdown_candidates[0]
    markdown = selected.read_text(encoding="utf-8", errors="replace")
    json_candidates = sorted(output.rglob("*.json"), key=lambda path: path.stat().st_size, reverse=True)
    backend_structure: dict[str, Any] = {}
    if json_candidates:
        try:
            backend_structure = json.loads(json_candidates[0].read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            backend_structure = {"raw_json_path": str(json_candidates[0])}
    return markdown, backend_structure, selected


def _parse_with_docling(input_path: Path) -> tuple[str, dict[str, Any], Path]:
    try:
        from docling.document_converter import DocumentConverter  # type: ignore
    except ImportError as exc:
        raise ParserUnavailableError("Docling is not installed. Install modeling-mastery[docling].") from exc
    converter = DocumentConverter()
    result = converter.convert(str(input_path))
    page_numbers = sorted(int(page_no) for page_no in (result.document.pages or {}))
    if page_numbers:
        parts: list[str] = []
        for page_no in page_numbers:
            parts.append(f"<!-- MM_PAGE: {page_no} -->")
            parts.append(result.document.export_to_markdown(page_no=page_no).strip())
            parts.append("")
        markdown = "\n".join(parts).strip() + "\n"
    else:
        markdown = result.document.export_to_markdown()
    try:
        structure = result.document.export_to_dict()
    except AttributeError:
        structure = json.loads(result.document.export_to_json())
    return markdown, structure, input_path


def _merge_markdown_pages_with_geometry(
    markdown: str, pages: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Use page-marked OCR text while retaining PDF page dimensions."""
    if not re.search(r"<!--\s*MM_PAGE:\s*\d+\s*-->", markdown):
        return pages
    geometry = {int(page["page"]): page for page in pages if page.get("page") is not None}
    merged = _pages_from_markdown(markdown)
    for page in merged:
        source = geometry.get(int(page["page"]), {})
        page["width"] = source.get("width")
        page["height"] = source.get("height")
    return merged


def _parse_with_pymupdf(input_path: Path, pages: list[dict[str, Any]]) -> tuple[str, dict[str, Any], Path]:
    if not any(normalize_space(str(page.get("text") or "")) for page in pages):
        raise DocumentParseError("PyMuPDF found no usable text layer; OCR is required.")
    parts = ["<!-- generated-by: Modeling-Mastery/PyMuPDF -->", ""]
    for page in pages:
        parts.append(f"<!-- MM_PAGE: {page['page']} -->")
        parts.append(page["text"].rstrip())
        parts.append("")
    return "\n".join(parts).strip() + "\n", {"pages": pages}, input_path


def _parse_with_pymupdf_ocr(input_path: Path) -> tuple[str, dict[str, Any], Path, list[dict[str, Any]]]:
    pages = _extract_page_map(input_path, force_ocr=True)
    if not any(normalize_space(str(page.get("text") or "")) for page in pages):
        errors = [str(page.get("ocr_error")) for page in pages if page.get("ocr_error")]
        detail = errors[0] if errors else "OCR produced no text"
        raise DocumentParseError(detail)
    parts = ["<!-- generated-by: Modeling-Mastery/PyMuPDF-Tesseract-OCR -->", ""]
    for page in pages:
        parts.append(f"<!-- MM_PAGE: {page['page']} -->")
        parts.append(str(page.get("text") or "").rstrip())
        parts.append("")
    return "\n".join(parts).strip() + "\n", {"pages": pages}, input_path, pages


def _extract_sections(markdown: str) -> list[dict[str, Any]]:
    sections: list[dict[str, Any]] = []
    pattern = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
    matches = list(pattern.finditer(markdown))
    hierarchy: list[tuple[int, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        level = len(match.group(1))
        title = match.group(2).strip()
        while hierarchy and hierarchy[-1][0] >= level:
            hierarchy.pop()
        parent_section = hierarchy[-1][1] if hierarchy else ""
        page, _ = _location_at(markdown, match.start())
        sections.append(
            {
                "id": f"SEC-{index + 1:03d}",
                "level": level,
                "title": title,
                "page": page,
                "parent_section": parent_section,
                "char_start": match.start(),
                "char_end": end,
                "content_hash": sha256_text(normalize_space(markdown[match.start() : end])),
            }
        )
        hierarchy.append((level, title))
    return sections


def _extract_equations(markdown: str) -> list[dict[str, Any]]:
    patterns = [
        re.compile(r"\$\$(.+?)\$\$", re.DOTALL),
        re.compile(r"\\\[(.+?)\\\]", re.DOTALL),
        re.compile(r"\\begin\{(?:equation\*?|align\*?|gather\*?)\}(.+?)\\end\{(?:equation\*?|align\*?|gather\*?)\}", re.DOTALL),
    ]
    equations: list[dict[str, Any]] = []
    seen: set[tuple[int, int]] = set()
    for pattern in patterns:
        for match in pattern.finditer(markdown):
            span = match.span()
            if span in seen:
                continue
            seen.add(span)
            latex = match.group(1).strip()
            label_match = re.search(r"\\label\{([^}]+)\}", latex)
            page, section = _location_at(markdown, match.start())
            equations.append(
                {
                    "id": f"EQ-{len(equations) + 1:03d}",
                    "label": label_match.group(1) if label_match else "",
                    "latex": latex,
                    "page": page,
                    "section": section,
                    "char_start": match.start(),
                    "char_end": match.end(),
                    "content_hash": sha256_text(normalize_space(latex)),
                }
            )
    equations.sort(key=lambda item: item["char_start"])
    for index, equation in enumerate(equations, start=1):
        equation["id"] = f"EQ-{index:03d}"
    return equations


def _extract_mentions(markdown: str, kind: str, pattern: re.Pattern[str]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for index, match in enumerate(pattern.finditer(markdown), start=1):
        page, section = _location_at(markdown, match.start())
        line_start = markdown.rfind("\n", 0, match.start()) + 1
        line_end = markdown.find("\n", match.end())
        line_end = len(markdown) if line_end < 0 else line_end
        result.append(
            {
                "id": f"{kind.upper()}-{index:03d}",
                "label": match.group(0),
                "context": normalize_space(markdown[line_start:line_end]),
                "page": page,
                "section": section,
                "char_start": match.start(),
                "char_end": match.end(),
            }
        )
    return result


def parse_document(
    input_path: Path,
    output_dir: Path,
    *,
    backend: str = "auto",
    mineru_backend: str = "pipeline",
    parser_timeout: int = 3600,
    title_hint: str | None = None,
) -> ParseResult:
    input_path = input_path.expanduser().resolve()
    output_dir = output_dir.expanduser().resolve()
    if not input_path.exists():
        raise FileNotFoundError(input_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    figures_dir = output_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    warnings: list[str] = []

    suffix = input_path.suffix.lower()
    pages: list[dict[str, Any]] = []
    if suffix == ".pdf":
        try:
            pages = _extract_page_map(input_path)
        except Exception as exc:
            warnings.append(f"Page map extraction failed: {exc}")
    elif suffix in {".md", ".markdown", ".txt"}:
        text = input_path.read_text(encoding="utf-8", errors="replace")
        pages = _pages_from_markdown(text)
    else:
        raise DocumentParseError(f"Unsupported input format: {suffix}")

    markdown = ""
    backend_structure: dict[str, Any] = {}
    selected_source = input_path
    parser_used = "unknown"
    attempts = [backend] if backend != "auto" else ["mineru", "docling", "pymupdf", "pymupdf-ocr"]
    if suffix != ".pdf":
        attempts = ["markdown"]

    with tempfile.TemporaryDirectory(prefix="modeling-mastery-parse-") as temporary:
        scratch = Path(temporary)
        errors: list[str] = []
        for candidate in attempts:
            try:
                if candidate == "mineru":
                    markdown, backend_structure, selected_source = _parse_with_mineru(
                        input_path, scratch, mineru_backend, parser_timeout
                    )
                    parser_used = "mineru"
                elif candidate == "docling":
                    markdown, backend_structure, selected_source = _parse_with_docling(input_path)
                    parser_used = "docling"
                elif candidate == "pymupdf":
                    markdown, backend_structure, selected_source = _parse_with_pymupdf(input_path, pages)
                    parser_used = "pymupdf"
                elif candidate == "pymupdf-ocr":
                    markdown, backend_structure, selected_source, pages = _parse_with_pymupdf_ocr(input_path)
                    parser_used = "pymupdf-ocr"
                    failed_pages = [page["page"] for page in pages if page.get("ocr_error") or not page.get("text")]
                    warnings.append(
                        "Scanned PDF processed with Tesseract OCR (chi_sim+eng, 180 dpi); "
                        "formulae, symbols, and numeric values require source-image verification."
                    )
                    if failed_pages:
                        warnings.append(f"OCR failed or returned empty text on pages: {failed_pages}")
                elif candidate == "markdown":
                    markdown = input_path.read_text(encoding="utf-8", errors="replace")
                    backend_structure = {"pages": pages}
                    parser_used = "markdown"
                    selected_source = input_path
                else:
                    raise DocumentParseError(f"Unknown parser backend: {candidate}")
                break
            except Exception as exc:
                errors.append(f"{candidate}: {type(exc).__name__}: {exc}")
                if backend != "auto":
                    raise
                LOGGER.warning("Parser %s unavailable/failed; trying fallback: %s", candidate, exc)
        if not markdown:
            raise DocumentParseError("All parsers failed: " + " | ".join(errors))
        warnings.extend(errors)

        pages = _merge_markdown_pages_with_geometry(markdown, pages)

        if parser_used == "mineru":
            markdown, backend_images = _copy_backend_images(selected_source, figures_dir, markdown)
        else:
            backend_images = []

    normalized_path = output_dir / "normalized_paper.md"
    header = (
        f"<!-- Modeling-Mastery normalized document | parser={parser_used} | "
        f"source_sha256={sha256_file(input_path)} -->\n\n"
    )
    title_preamble = f"# {title_hint.strip()}\n\n" if title_hint and title_hint.strip() else ""
    atomic_write_text(normalized_path, header + title_preamble + markdown.strip() + "\n")

    embedded_images: list[dict[str, Any]] = []
    if suffix == ".pdf" and parser_used != "pymupdf-ocr":
        try:
            embedded_images = _extract_embedded_images(input_path, figures_dir)
        except Exception as exc:
            warnings.append(f"Embedded image extraction failed: {exc}")
    elif suffix == ".pdf" and parser_used == "pymupdf-ocr":
        warnings.append(
            "Full-page scan images were not copied into figures/ as figure crops; "
            "use the source PDF to verify OCR-sensitive equations, tables, and diagrams."
        )

    image_by_hash: dict[str, dict[str, Any]] = {}
    for image in [*backend_images, *embedded_images]:
        marker = image.get("sha256") or image.get("path")
        image_by_hash[str(marker)] = image
    figures = list(image_by_hash.values())
    for index, figure in enumerate(figures, start=1):
        figure["id"] = f"FIG-{index:03d}"

    page_map_path = output_dir / "page_map.json"
    write_json(
        page_map_path,
        {
            "source": str(input_path),
            "source_sha256": sha256_file(input_path),
            "generated_at": utc_now_iso(),
            "pages": pages,
        },
    )

    normalized_text = normalized_path.read_text(encoding="utf-8")
    structure = {
        "schema_version": "1.0.0",
        "source": {
            "path": str(input_path),
            "sha256": sha256_file(input_path),
            "parser": parser_used,
            "parsed_at": utc_now_iso(),
        },
        "document": {
            "page_count": len(pages),
            "char_count": len(normalized_text),
            "content_hash": sha256_text(normalize_space(normalized_text)),
        },
        "sections": _extract_sections(normalized_text),
        "equations": _extract_equations(normalized_text),
        "figure_mentions": _extract_mentions(
            normalized_text,
            "figure",
            re.compile(r"(?:图\s*\d+(?:[-.]\d+)?|Fig(?:ure)?\.?\s*\d+(?:[-.]\d+)?)", re.I),
        ),
        "table_mentions": _extract_mentions(
            normalized_text,
            "table",
            re.compile(r"(?:表\s*\d+(?:[-.]\d+)?|Table\s*\d+(?:[-.]\d+)?)", re.I),
        ),
        "figures": figures,
        "backend_structure": backend_structure,
        "warnings": warnings,
    }
    structure_path = output_dir / "paper_structure.json"
    write_json(structure_path, structure)

    figures_manifest_path = figures_dir / "manifest.json"
    write_json(figures_manifest_path, {"source": str(input_path), "figures": figures})

    manifest_path = output_dir / "parse_manifest.json"
    result = ParseResult(
        parser=parser_used,
        normalized_markdown=normalized_path,
        structure_json=structure_path,
        page_map_json=page_map_path,
        figures_dir=figures_dir,
        manifest_json=manifest_path,
        warnings=warnings,
    )
    write_json(manifest_path, result.as_dict())
    return result
