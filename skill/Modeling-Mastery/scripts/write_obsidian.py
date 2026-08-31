from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT

from modeling_mastery.indexer import build_index
from modeling_mastery.io_utils import read_json
from modeling_mastery.paper_workspace import initialize_paper_workspace
from modeling_mastery.vault import write_obsidian_vault


def main() -> None:
    parser = argparse.ArgumentParser(description="06-07 Knowledge Distiller + Obsidian Writer.")
    parser.add_argument("input_ir", type=Path)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--vault", type=Path)
    target.add_argument("--library-root", type=Path)
    parser.add_argument("--project-root", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--no-index", action="store_true")
    args = parser.parse_args()
    ir = read_json(args.input_ir)
    if args.library_root:
        layout = initialize_paper_workspace(args.library_root, ir["bibliographic"]["title"])
        vault = layout.knowledge_vault
        obsidian_root = layout.library_root
    else:
        vault = args.vault
        obsidian_root = None
    report = write_obsidian_vault(
        ir,
        vault,
        project_root=args.project_root,
        obsidian_root=obsidian_root,
    )
    if not args.no_index:
        report["index"] = build_index(vault)
    if args.library_root:
        report["paper_workspace"] = layout.as_dict()
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
