from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT  # noqa: F401
from modeling_mastery.dedup import scan_duplicates


def main() -> None:
    parser = argparse.ArgumentParser(description="Find exact and fuzzy duplicate Obsidian notes.")
    parser.add_argument("vault", type=Path)
    parser.add_argument("--threshold", type=float, default=0.93)
    args = parser.parse_args()
    print(json.dumps(scan_duplicates(args.vault, fuzzy_threshold=args.threshold), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
