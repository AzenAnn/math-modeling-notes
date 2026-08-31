from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT  # noqa: F401
from modeling_mastery.indexer import build_index


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Obsidian JSON + SQLite FTS5 index.")
    parser.add_argument("vault", type=Path)
    args = parser.parse_args()
    print(json.dumps(build_index(args.vault), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
