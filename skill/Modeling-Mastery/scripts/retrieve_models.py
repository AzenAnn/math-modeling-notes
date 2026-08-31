from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT  # noqa: F401
from modeling_mastery.retriever import search_index


def main() -> None:
    parser = argparse.ArgumentParser(description="Retrieve models/algorithms/cases/code from a Modeling Vault.")
    parser.add_argument("vault", type=Path)
    parser.add_argument("query")
    parser.add_argument("--type", dest="note_type")
    parser.add_argument("--category")
    parser.add_argument("--task", action="append", default=[])
    parser.add_argument("--top-k", type=int, default=10)
    args = parser.parse_args()
    results = search_index(args.vault, args.query, note_type=args.note_type, category=args.category, tasks=args.task or None, top_k=args.top_k)
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
