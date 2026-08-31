from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from .io_utils import find_project_root

_HOST_ALIASES = {
    "codex": "codex",
    "openai": "codex",
    "openai-codex": "codex",
    "claude": "claude-code",
    "claude-code": "claude-code",
    "claudecode": "claude-code",
}


def _skill_sources(project_root: Path | None = None) -> tuple[Path, Path]:
    root = project_root or find_project_root()
    source_orchestrator = root / "SKILL.md"
    source_children = root / "skills"
    if source_orchestrator.exists() and source_children.exists():
        return source_orchestrator, source_children

    packaged = Path(__file__).resolve().parent / "assets" / "skills"
    source_orchestrator = packaged / "modeling-mastery" / "SKILL.md"
    source_children = packaged
    if not source_orchestrator.exists() or not source_children.exists():
        raise FileNotFoundError("Cannot find packaged Agent Skill assets.")
    return source_orchestrator, source_children


def install_skills(
    target: Path,
    *,
    project_root: Path | None = None,
    overwrite: bool = True,
) -> dict[str, Any]:
    """Install the orchestrator plus all child skills into an explicit skill directory."""
    source_orchestrator, source_children = _skill_sources(project_root)
    target = target.expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    installed: list[str] = []

    orchestrator_target = target / "modeling-mastery"
    if orchestrator_target.exists() and overwrite:
        shutil.rmtree(orchestrator_target)
    orchestrator_target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_orchestrator, orchestrator_target / "SKILL.md")
    workspace_reference = source_orchestrator.parent / "references" / "paper-workspace.md"
    if workspace_reference.exists():
        reference_target = orchestrator_target / "references"
        reference_target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(workspace_reference, reference_target / workspace_reference.name)
    installed.append(str(orchestrator_target))

    for source in sorted(source_children.iterdir()):
        if source.name == "modeling-mastery" or not source.is_dir() or not (source / "SKILL.md").exists():
            continue
        destination = target / source.name
        if destination.exists() and overwrite:
            shutil.rmtree(destination)
        if not destination.exists():
            shutil.copytree(source, destination)
        installed.append(str(destination))
    return {"target": str(target), "installed": installed, "count": len(installed)}


def resolve_host_skill_target(
    host: str,
    *,
    scope: str = "project",
    base_dir: Path | None = None,
) -> Path:
    """Resolve the official local skill location for Codex or Claude Code."""
    normalized = _HOST_ALIASES.get(host.strip().lower())
    if not normalized:
        raise ValueError(f"Unsupported skill host: {host}")
    normalized_scope = scope.strip().lower()
    if normalized_scope not in {"project", "user"}:
        raise ValueError("Skill scope must be 'project' or 'user'.")
    root = Path.home() if normalized_scope == "user" else (base_dir or Path.cwd()).expanduser().resolve()
    if normalized == "codex":
        return root / ".agents" / "skills"
    return root / ".claude" / "skills"


def install_skills_for_hosts(
    *,
    host: str = "both",
    scope: str = "project",
    base_dir: Path | None = None,
    project_root: Path | None = None,
    overwrite: bool = True,
) -> dict[str, Any]:
    """Install to Codex `.agents/skills`, Claude `.claude/skills`, or both."""
    requested_raw = [item.strip() for item in host.split(",") if item.strip()]
    if not requested_raw or any(item.lower() in {"both", "all"} for item in requested_raw):
        requested = ["codex", "claude-code"]
    else:
        requested = []
        for item in requested_raw:
            normalized = _HOST_ALIASES.get(item.lower())
            if not normalized:
                raise ValueError(f"Unsupported skill host: {item}")
            if normalized not in requested:
                requested.append(normalized)

    reports: dict[str, Any] = {}
    total = 0
    for item in requested:
        target = resolve_host_skill_target(item, scope=scope, base_dir=base_dir)
        report = install_skills(target, project_root=project_root, overwrite=overwrite)
        reports[item] = report
        total += int(report["count"])
    return {
        "hosts": requested,
        "scope": scope,
        "base_dir": str((base_dir or Path.cwd()).expanduser().resolve()) if scope == "project" else str(Path.home()),
        "reports": reports,
        "count": total,
    }
