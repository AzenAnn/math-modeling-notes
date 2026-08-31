from __future__ import annotations

import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from .io_utils import normalize_space, read_json, sha256_text

PAGE_MARKER = re.compile(r"<!--\s*MM_PAGE:\s*(\d+)\s*-->")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


@dataclass(slots=True)
class TextChunk:
    chunk_id: str
    text: str
    char_start: int
    char_end: int
    section: str
    page_hint: int | None

    def as_dict(self) -> dict[str, Any]:
        return {
            "chunk_id": self.chunk_id,
            "text": self.text,
            "char_start": self.char_start,
            "char_end": self.char_end,
            "section": self.section,
            "page_hint": self.page_hint,
        }


def _section_at(markdown: str, position: int) -> str:
    section = ""
    for match in HEADING.finditer(markdown):
        if match.end() <= position:
            section = match.group(2).strip()
            continue
        if match.start() > position:
            break
    return section


def _page_at(markdown: str, position: int) -> int | None:
    page: int | None = None
    for match in PAGE_MARKER.finditer(markdown, 0, position + 1):
        page = int(match.group(1))
    return page


def chunk_markdown(markdown: str, *, max_chars: int = 16000, overlap_chars: int = 800) -> list[TextChunk]:
    if max_chars < 2000:
        raise ValueError("max_chars must be at least 2000")
    paragraphs = list(re.finditer(r"(?:^|\n\s*\n)(.+?)(?=\n\s*\n|\Z)", markdown, re.DOTALL))
    if not paragraphs:
        paragraphs = [re.match(r"(?s).*", markdown)]  # type: ignore[list-item]
    chunks: list[TextChunk] = []
    cursor = 0
    index = 1
    while cursor < len(markdown):
        target_end = min(len(markdown), cursor + max_chars)
        if target_end < len(markdown):
            boundary = markdown.rfind("\n\n", cursor + max_chars // 2, target_end)
            if boundary > cursor:
                target_end = boundary
        text = markdown[cursor:target_end].strip()
        if text:
            chunks.append(
                TextChunk(
                    chunk_id=f"CHUNK-{index:03d}",
                    text=text,
                    char_start=cursor,
                    char_end=target_end,
                    section=_section_at(markdown, cursor),
                    page_hint=_page_at(markdown, cursor),
                )
            )
            index += 1
        if target_end >= len(markdown):
            break
        cursor = max(cursor + 1, target_end - overlap_chars)
    return chunks


def stable_evidence_id(kind: str, quote: str, page: int | None = None) -> str:
    location = f"P{page:03d}" if page else "PX"
    return f"E-{kind.upper()}-{location}-{sha256_text(normalize_space(quote))[:10]}"


def _sentence_candidates(text: str, min_length: int = 12) -> list[str]:
    pieces = re.split(r"(?<=[。！？.!?;；])\s*|\n+", text)
    return [normalize_space(piece) for piece in pieces if len(normalize_space(piece)) >= min_length]


def _sentence_context(markdown: str, start: int, end: int, *, max_length: int = 420) -> tuple[str, int, int]:
    left_boundaries = [markdown.rfind(mark, 0, start) for mark in ["。", "！", "？", "\n", ". ", ";", "；"]]
    context_start = max(left_boundaries) + 1
    right_candidates = []
    for marker in ["。", "！", "？", "\n", ". ", ";", "；"]:
        found = markdown.find(marker, end)
        if found >= 0:
            right_candidates.append(found + len(marker))
    context_end = min(right_candidates) if right_candidates else min(len(markdown), end + max_length)
    if context_end - context_start > max_length:
        context_start = max(context_start, start - max_length // 2)
        context_end = min(context_end, end + max_length // 2)
    return normalize_space(markdown[context_start:context_end]), context_start, context_end


def heuristic_evidence(markdown: str) -> list[dict[str, Any]]:
    patterns: list[tuple[str, re.Pattern[str]]] = [
        ("assumption", re.compile(r"(?:假设|assum(?:e|ption))[^。！？\n]{6,180}", re.I)),
        ("model", re.compile(r"(?:采用|建立|构建|使用|引入|based on|using)[^。！？\n]{0,70}(?:模型|算法|法|model|algorithm)[^。！？\n]{0,120}", re.I)),
        ("validation", re.compile(r"(?:灵敏度|敏感性|鲁棒性|误差|检验|validation|sensitivity|robustness)[^。！？\n]{0,160}", re.I)),
    ]
    evidence: list[dict[str, Any]] = []
    for semantic_kind, pattern in patterns:
        for match in pattern.finditer(markdown):
            quote, quote_start, quote_end = _sentence_context(markdown, match.start(), match.end())
            if len(quote) < 12 or quote.startswith(("<!--", "# ", "## ", "### ")):
                continue
            page = _page_at(markdown, match.start())
            evidence.append(
                {
                    "id": stable_evidence_id("text", quote, page),
                    "kind": "text",
                    "page": page,
                    "section": _section_at(markdown, match.start()),
                    "label": semantic_kind,
                    "locator": f"char:{quote_start}-{quote_end}",
                    "quote": quote,
                    "char_start": quote_start,
                    "char_end": quote_end,
                    "content_hash": sha256_text(quote),
                    "provenance": "HEURISTIC",
                    "confidence": 0.55,
                }
            )
    unique: dict[str, dict[str, Any]] = {item["id"]: item for item in evidence}
    return list(unique.values())


def _best_page_for_quote(quote: str, pages: list[dict[str, Any]]) -> tuple[int | None, float]:
    normalized_quote = normalize_space(quote)
    if not normalized_quote:
        return None, 0.0
    for page in pages:
        page_text = page.get("normalized_text") or normalize_space(page.get("text", ""))
        if normalized_quote in page_text:
            return int(page["page"]), 1.0
    # Fuzzy matching against sentence windows avoids comparing an entire page to one sentence.
    best_page: int | None = None
    best_score = 0.0
    for page in pages:
        for sentence in _sentence_candidates(page.get("text", "")):
            score = SequenceMatcher(None, normalized_quote, sentence).ratio()
            if score > best_score:
                best_score = score
                best_page = int(page["page"])
    return (best_page, best_score) if best_score >= 0.72 else (None, best_score)


def repair_evidence_anchors(
    evidence: list[dict[str, Any]],
    *,
    page_map_path: Path | None = None,
    markdown: str | None = None,
) -> list[dict[str, Any]]:
    pages: list[dict[str, Any]] = []
    if page_map_path and page_map_path.exists():
        pages = read_json(page_map_path).get("pages", [])
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    for raw in evidence:
        item = dict(raw)
        quote = normalize_space(str(item.get("quote", "")))
        item["quote"] = quote
        page = item.get("page")
        anchor_score = 1.0 if page else 0.0
        if not page and pages:
            page, anchor_score = _best_page_for_quote(quote, pages)
            item["page"] = page
        if markdown and item.get("char_start") is None and quote:
            compact_markdown = normalize_space(markdown)
            compact_position = compact_markdown.find(quote)
            if compact_position >= 0:
                item["locator"] = item.get("locator") or f"normalized-char:{compact_position}"
        item.setdefault("kind", "text")
        item.setdefault("section", "")
        item.setdefault("label", "")
        item.setdefault("locator", f"page:{page}" if page else "unresolved")
        item.setdefault("char_start", None)
        item.setdefault("char_end", None)
        item.setdefault("content_hash", sha256_text(quote))
        item.setdefault("provenance", "PAPER_EXPLICIT")
        original_confidence = float(item.get("confidence", 0.5))
        item["confidence"] = max(0.0, min(1.0, original_confidence * (0.8 + 0.2 * anchor_score)))
        item["id"] = stable_evidence_id(str(item["kind"]), quote, page)
        if item["id"] not in seen:
            result.append(item)
            seen.add(item["id"])
    return result


def evidence_lookup(evidence: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(item.get("id")): item for item in evidence if item.get("id")}
