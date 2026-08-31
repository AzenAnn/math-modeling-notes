from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from modeling_mastery.cli import app
from modeling_mastery.skill_installer import install_skills, install_skills_for_hosts


def test_skill_bundle_installs_eight_skills(tmp_path: Path, project_root: Path) -> None:
    result = install_skills(tmp_path / "skills", project_root=project_root)
    assert result["count"] == 8
    assert (tmp_path / "skills" / "modeling-mastery" / "SKILL.md").exists()
    assert (tmp_path / "skills" / "modeling-mastery" / "references" / "paper-workspace.md").exists()
    assert (tmp_path / "skills" / "paper-ingest" / "SKILL.md").exists()
    assert (tmp_path / "skills" / "model-retriever" / "SKILL.md").exists()


def test_packaged_skill_assets_are_usable(tmp_path: Path) -> None:
    empty_root = tmp_path / "empty-project"
    empty_root.mkdir()
    result = install_skills(tmp_path / "packaged-skills", project_root=empty_root)
    assert result["count"] == 8
    assert (tmp_path / "packaged-skills" / "modeling-mastery" / "SKILL.md").exists()
    assert (tmp_path / "packaged-skills" / "modeling-mastery" / "references" / "paper-workspace.md").exists()


def test_cli_help_lists_pipeline_and_batch() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "pipeline" in result.stdout
    assert "batch" in result.stdout
    assert "init-paper" in result.stdout


def test_skill_bundle_installs_for_codex_and_claude(tmp_path: Path, project_root: Path) -> None:
    result = install_skills_for_hosts(
        host="both",
        scope="project",
        base_dir=tmp_path,
        project_root=project_root,
    )
    assert result["count"] == 16
    assert (tmp_path / ".agents" / "skills" / "modeling-mastery" / "SKILL.md").exists()
    assert (tmp_path / ".claude" / "skills" / "modeling-mastery" / "SKILL.md").exists()


def test_cli_help_lists_skill_run() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "skill-run" in result.stdout
