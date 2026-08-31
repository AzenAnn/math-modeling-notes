from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from modeling_mastery.cli import app
from modeling_mastery.constants import AUTO_END
from modeling_mastery.paper_workspace import initialize_paper_workspace


def test_initialize_paper_workspace_is_idempotent_and_preserves_manual_content(tmp_path: Path) -> None:
    layout = initialize_paper_workspace(tmp_path, "多情形下无人机烟幕遮蔽策略的建模与优化研究")

    assert layout.paper_root == tmp_path.resolve() / "论文" / "多情形下无人机烟幕遮蔽策略的建模与优化研究"
    for path in [
        layout.workflow / "parsed",
        layout.workflow / "ir",
        layout.workflow / "code",
        layout.workflow / "reports",
        layout.knowledge_vault / "00_Home",
        layout.knowledge_vault / "10_Models",
        layout.knowledge_vault / "_assets",
        layout.supplements / "模型",
        layout.supplements / "算法",
        layout.assets,
    ]:
        assert path.is_dir()

    readme = layout.paper_root / "README.md"
    content = readme.read_text(encoding="utf-8").replace(
        "在这里记录本论文工作区的人工维护说明。",
        "人工备注：优先核对遮蔽判据。",
    )
    readme.write_text(content, encoding="utf-8")

    initialize_paper_workspace(tmp_path, "多情形下无人机烟幕遮蔽策略的建模与优化研究")
    rewritten = readme.read_text(encoding="utf-8")
    assert "人工备注：优先核对遮蔽判据。" in rewritten
    assert rewritten.count(AUTO_END) == 1
    assert (tmp_path / "论文" / "README.md").exists()


def test_cli_pipeline_library_root_uses_per_paper_layout(
    tmp_path: Path,
    demo_markdown: str,
) -> None:
    source = tmp_path / "source.md"
    source.write_text(demo_markdown, encoding="utf-8")
    library = tmp_path / "笔记库"
    title = "应急设施评价示例"

    result = CliRunner().invoke(
        app,
        [
            "pipeline",
            str(source),
            "--library-root",
            str(library),
            "--paper-title",
            title,
            "--backend",
            "markdown",
            "--provider",
            "none",
        ],
    )

    assert result.exit_code == 0, result.stdout
    paper_root = library / "论文" / title
    assert (paper_root / "workflow" / "ir" / "paper_ir.json").exists()
    assert (paper_root / "知识库" / ".modeling-mastery" / "index.json").exists()
    assert not (library / "10_Models").exists()


def test_initializer_does_not_rewrite_unmanaged_paper_readme(tmp_path: Path) -> None:
    paper_root = tmp_path / "论文" / "已有论文"
    paper_root.mkdir(parents=True)
    readme = paper_root / "README.md"
    readme.write_text("# 已有人工说明\n\n保持原样。\n", encoding="utf-8")

    initialize_paper_workspace(tmp_path, "已有论文")

    assert readme.read_text(encoding="utf-8") == "# 已有人工说明\n\n保持原样。\n"
