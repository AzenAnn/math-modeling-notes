from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT
from modeling_mastery.skill_installer import install_skills, install_skills_for_hosts


def main() -> None:
    parser = argparse.ArgumentParser(description="Install Modeling-Mastery Agent Skills for Codex and/or Claude Code.")
    parser.add_argument("--target", type=Path, help="Explicit skill directory; overrides --host/--scope.")
    parser.add_argument("--host", default="both", help="codex | claude | both | comma-separated")
    parser.add_argument("--scope", choices=["project", "user"], default="project")
    parser.add_argument("--base-dir", type=Path, default=Path("."), help="Project root for project-scoped installs.")
    parser.add_argument("--no-overwrite", action="store_true")
    args = parser.parse_args()
    if args.target:
        result = install_skills(args.target, project_root=PROJECT_ROOT, overwrite=not args.no_overwrite)
    else:
        result = install_skills_for_hosts(
            host=args.host,
            scope=args.scope,
            base_dir=args.base_dir,
            project_root=PROJECT_ROOT,
            overwrite=not args.no_overwrite,
        )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
