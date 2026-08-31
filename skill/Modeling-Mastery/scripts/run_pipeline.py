from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT

from modeling_mastery.config import Settings
from modeling_mastery.paper_workspace import initialize_paper_workspace
from modeling_mastery.pipeline import run_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the complete Modeling-Mastery pipeline.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--vault", type=Path)
    parser.add_argument("--library-root", type=Path)
    parser.add_argument("--paper-title")
    parser.add_argument("--backend", choices=["auto", "mineru", "docling", "pymupdf"], default="auto")
    parser.add_argument("--provider", choices=["none", "mock", "openai-compatible", "anthropic", "codex", "claude-code", "local-agent"], default=None)
    parser.add_argument("--reproduce-code", action="store_true")
    parser.add_argument("--max-code-targets", type=int, default=8)
    parser.add_argument("--no-tests", action="store_true")
    parser.add_argument("--check-octave", action="store_true")
    args = parser.parse_args()
    if args.library_root:
        if not args.paper_title:
            parser.error("--paper-title is required with --library-root")
        if args.workspace or args.vault:
            parser.error("do not combine --library-root with --workspace or --vault")
        layout = initialize_paper_workspace(args.library_root, args.paper_title)
        workspace = layout.workflow
        vault = layout.knowledge_vault
        obsidian_root = layout.library_root
    else:
        workspace = args.workspace or Path("workspaces/run")
        vault = args.vault
        obsidian_root = None
    report = run_pipeline(
        args.input,
        workspace,
        vault_path=vault,
        settings=Settings.from_env(),
        backend=args.backend,
        provider=args.provider,
        reproduce=args.reproduce_code,
        max_code_targets=args.max_code_targets,
        run_tests=not args.no_tests,
        check_octave=args.check_octave,
        project_root=PROJECT_ROOT,
        obsidian_root=obsidian_root,
    )
    if args.library_root:
        report["paper_workspace"] = layout.as_dict()
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
