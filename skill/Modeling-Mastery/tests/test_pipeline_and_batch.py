from __future__ import annotations

import json
from pathlib import Path

from modeling_mastery.batch import discover_inputs, run_batch
from modeling_mastery.config import Settings
from modeling_mastery.pipeline import run_pipeline


def test_offline_pipeline_creates_ir_vault_and_index(tmp_path: Path, demo_markdown: str, project_root: Path) -> None:
    paper = tmp_path / "paper.md"
    paper.write_text(demo_markdown, encoding="utf-8")
    workspace = tmp_path / "workspace"
    vault = tmp_path / "vault"
    report = run_pipeline(
        paper,
        workspace,
        vault_path=vault,
        settings=Settings(llm_provider="none", pdf_backend="markdown"),
        backend="markdown",
        provider="none",
        reproduce=False,
        project_root=project_root,
    )
    assert Path(report["paper_ir"]).exists()
    assert (workspace / "reports" / "pipeline_report.json").exists()
    assert (vault / ".modeling-mastery" / "index.json").exists()
    ir = json.loads(Path(report["paper_ir"]).read_text(encoding="utf-8"))
    assert len(ir["models"]) >= 2


def test_batch_resume_and_reports(tmp_path: Path, demo_markdown: str, project_root: Path) -> None:
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "a.md").write_text(demo_markdown, encoding="utf-8")
    (papers / "b.md").write_text("# B\n\n使用蒙特卡洛方法进行不确定性模拟。", encoding="utf-8")
    assert len(discover_inputs(papers)) == 2

    workspace_root = tmp_path / "batch-workspaces"
    vault = tmp_path / "vault"
    first = run_batch(
        papers,
        workspace_root,
        vault_path=vault,
        settings=Settings(llm_provider="none", pdf_backend="markdown"),
        backend="markdown",
        provider="none",
        project_root=project_root,
    )
    assert first["success_count"] == 2
    assert first["failure_count"] == 0

    second = run_batch(
        papers,
        workspace_root,
        vault_path=vault,
        settings=Settings(llm_provider="none", pdf_backend="markdown"),
        backend="markdown",
        provider="none",
        project_root=project_root,
        resume=True,
    )
    assert second["skip_count"] == 2
    assert (workspace_root / "batch_report.json").exists()
