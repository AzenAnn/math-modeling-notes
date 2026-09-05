from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from .codegen import reproduce_code
from .config import Settings
from .document import parse_document
from .indexer import build_index
from .io_utils import read_json, utc_now_iso, write_json
from .ir_builder import build_paper_ir
from .llm import create_llm
from .normalizer import ReferenceCatalog, normalize_ir
from .schema_utils import SchemaStore
from .vault import write_obsidian_vault

LOGGER = logging.getLogger(__name__)


def run_pipeline(
    input_path: Path,
    workspace: Path,
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
    obsidian_root: Path | None = None,
    paper_title_hint: str | None = None,
) -> dict[str, Any]:
    settings = settings or Settings.from_env()
    workspace = workspace.expanduser().resolve()
    parsed_dir = workspace / "parsed"
    ir_dir = workspace / "ir"
    code_dir = workspace / "code"
    reports_dir = workspace / "reports"
    for directory in [parsed_dir, ir_dir, code_dir, reports_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    report: dict[str, Any] = {
        "started_at": utc_now_iso(),
        "input": str(input_path.expanduser().resolve()),
        "workspace": str(workspace),
        "stages": {},
        "warnings": [],
    }

    parse_result = parse_document(
        input_path,
        parsed_dir,
        backend=backend or settings.pdf_backend,
        mineru_backend=settings.mineru_backend,
        title_hint=paper_title_hint,
    )
    report["stages"]["01_paper_ingest"] = parse_result.as_dict()
    report["warnings"].extend(parse_result.warnings)

    llm = create_llm(settings, provider)
    raw_ir, build_report = build_paper_ir(
        parse_result.normalized_markdown,
        structure_path=parse_result.structure_json,
        page_map_path=parse_result.page_map_json,
        output_dir=ir_dir,
        llm=llm,
        catalog=ReferenceCatalog(project_root / "references" if project_root else None),
    )
    report["stages"]["02_04_analysis"] = build_report

    normalized_ir, normalization_report = normalize_ir(
        raw_ir,
        ReferenceCatalog(project_root / "references" if project_root else None),
    )
    SchemaStore(project_root / "schemas" if project_root else None).validate("paper", normalized_ir)
    write_json(ir_dir / "normalization_report.json", normalization_report)
    report["stages"]["normalization"] = normalization_report

    final_ir = normalized_ir
    if reproduce:
        final_ir, code_report = reproduce_code(
            final_ir,
            code_dir,
            llm=llm,
            max_targets=max_code_targets,
            timeout=settings.code_timeout,
            memory_mb=settings.code_memory_mb,
            run_tests=run_tests,
            check_octave=check_octave,
        )
        SchemaStore(project_root / "schemas" if project_root else None).validate("paper", final_ir)
        write_json(code_dir / "code_reproduction_report.json", code_report)
        report["stages"]["05_code_reproducer"] = code_report
    else:
        report["stages"]["05_code_reproducer"] = {"skipped": True}

    final_ir_path = ir_dir / "paper_ir.json"
    write_json(final_ir_path, final_ir)
    report["paper_ir"] = str(final_ir_path)

    selected_vault = vault_path or settings.vault_path
    if selected_vault:
        vault_report = write_obsidian_vault(
            final_ir,
            selected_vault,
            project_root=project_root,
            obsidian_root=obsidian_root,
        )
        report["stages"]["06_07_vault"] = vault_report
        index_report = build_index(selected_vault)
        report["stages"]["index"] = index_report
    else:
        report["stages"]["06_07_vault"] = {"skipped": True, "reason": "No vault path supplied"}

    report["finished_at"] = utc_now_iso()
    write_json(reports_dir / "pipeline_report.json", report)
    return report


def rerun_vault_from_ir(
    ir_path: Path,
    vault_path: Path,
    *,
    project_root: Path | None = None,
    obsidian_root: Path | None = None,
) -> dict[str, Any]:
    ir = read_json(ir_path)
    report = write_obsidian_vault(
        ir,
        vault_path,
        project_root=project_root,
        obsidian_root=obsidian_root,
    )
    report["index"] = build_index(vault_path)
    return report
