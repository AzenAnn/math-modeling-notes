from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT  # noqa: F401
from modeling_mastery.document import parse_document


def main() -> None:
    parser = argparse.ArgumentParser(description="01 Paper Ingest: PDF/Markdown to normalized Markdown, structure, page map, and figures.")
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--backend", choices=["auto", "mineru", "docling", "pymupdf", "markdown"], default="auto")
    parser.add_argument("--mineru-backend", default="pipeline")
    parser.add_argument("--timeout", type=int, default=3600)
    args = parser.parse_args()
    result = parse_document(args.input, args.output, backend=args.backend, mineru_backend=args.mineru_backend, parser_timeout=args.timeout)
    print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
