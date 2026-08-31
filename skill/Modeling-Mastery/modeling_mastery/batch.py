from __future__ import annotations

import traceback
from pathlib import Path
from typing import Any, Iterable

from .config import Settings
from .io_utils import safe_filename, sha256_file, utc_now_iso, write_json
from .pipeline import run_pipeline

SUPPORTED_INPUTS = {".pdf", ".md", ".markdown", ".txt"}


def discover_inputs(
    input_root: Path,
    *,
    recursive: bool = True,
    patterns: Iterable[str] | None = None,
) -> list[Path]:
    """Discover supported papers in a directory with deterministic ordering."""
    input_root = input_root.expanduser().resolve()
    if input_root.is_file():
        return [input_root] if input_root.suffix.lower() in SUPPORTED_INPUTS else []
    if not input_root.exists():
        raise FileNotFoundError(input_root)
    selected_patterns = list(patterns or ["*.pdf", "*.md", "*.markdown", "*.txt"])
    result: dict[Path, None] = {}
    for pattern in selected_patterns:
        iterator = input_root.rglob(pattern) if recursive else input_root.glob(pattern)
        for path in iterator:
            if path.is_file() and path.suffix.lower() in SUPPORTED_INPUTS:
                result[path.resolve()] = None
    return sorted(result, key=lambda path: path.as_posix().casefold())


def _workspace_name(path: Path) -> str:
    digest = sha256_file(path)[:10]
    return f"{safe_filename(path.stem, fallback='paper', max_length=70)}-{digest}"


def run_batch(
    input_root: Path,
    workspace_root: Path,
    *,
    vault_path: Path | None = None,
    settings: Settings | None = None,
    backend: str | None = None,
    provider: str | None = None,
    reproduce: bool = False,
    max_code_targets: int = 8,
    run_tests: bool = True,
    check_octave: bool = False,
    project_root: Path | None = None,
    recursive: bool = True,
    patterns: Iterable[str] | None = None,
    resume: bool = True,
    continue_on_error: bool = True,
) -> dict[str, Any]:
    """Run the seven-stage pipeline sequentially for a directory of papers.

    Sequential execution is intentional: MinerU/Docling and LLM calls can be memory-heavy,
    and parallel PDF jobs often make a laptop less reliable during contest preparation.
    """
    settings = settings or Settings.from_env()
    workspace_root = workspace_root.expanduser().resolve()
    workspace_root.mkdir(parents=True, exist_ok=True)
    inputs = discover_inputs(input_root, recursive=recursive, patterns=patterns)
    report: dict[str, Any] = {
        "schema_version": "1.0.0",
        "started_at": utc_now_iso(),
        "input_root": str(input_root.expanduser().resolve()),
        "workspace_root": str(workspace_root),
        "vault": str(vault_path.expanduser().resolve()) if vault_path else None,
        "input_count": len(inputs),
        "succeeded": [],
        "skipped": [],
        "failed": [],
    }
    report_path = workspace_root / "batch_report.json"

    for input_path in inputs:
        workspace = workspace_root / _workspace_name(input_path)
        final_ir = workspace / "ir" / "paper_ir.json"
        pipeline_report = workspace / "reports" / "pipeline_report.json"
        if resume and final_ir.exists() and pipeline_report.exists():
            report["skipped"].append(
                {
                    "input": str(input_path),
                    "workspace": str(workspace),
                    "reason": "Existing paper_ir.json and pipeline_report.json",
                }
            )
            write_json(report_path, report)
            continue
        try:
            item_report = run_pipeline(
                input_path,
                workspace,
                vault_path=vault_path,
                settings=settings,
                backend=backend,
                provider=provider,
                reproduce=reproduce,
                max_code_targets=max_code_targets,
                run_tests=run_tests,
                check_octave=check_octave,
                project_root=project_root,
            )
            report["succeeded"].append(
                {
                    "input": str(input_path),
                    "workspace": str(workspace),
                    "paper_ir": item_report.get("paper_ir"),
                    "warnings": item_report.get("warnings", []),
                }
            )
        except Exception as exc:  # deliberate per-file boundary
            report["failed"].append(
                {
                    "input": str(input_path),
                    "workspace": str(workspace),
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                    "traceback": traceback.format_exc(limit=12),
                }
            )
            if not continue_on_error:
                report["finished_at"] = utc_now_iso()
                write_json(report_path, report)
                raise
        write_json(report_path, report)

    report["finished_at"] = utc_now_iso()
    report["success_count"] = len(report["succeeded"])
    report["skip_count"] = len(report["skipped"])
    report["failure_count"] = len(report["failed"])
    write_json(report_path, report)
    return report
