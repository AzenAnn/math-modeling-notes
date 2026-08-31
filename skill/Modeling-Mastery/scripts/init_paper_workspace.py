from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT  # noqa: F401

from modeling_mastery.paper_workspace import initialize_paper_workspace, workspace_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a canonical per-paper workspace.")
    parser.add_argument("library_root", type=Path)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    report = workspace_report(initialize_paper_workspace(args.library_root, args.title))
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
