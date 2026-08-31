from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT
from modeling_mastery.io_utils import read_json, write_json
from modeling_mastery.normalizer import ReferenceCatalog, normalize_ir
from modeling_mastery.schema_utils import SchemaStore


def main() -> None:
    parser = argparse.ArgumentParser(description="Canonicalize model/algorithm names and merge aliases.")
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    normalized, report = normalize_ir(read_json(args.input), ReferenceCatalog(PROJECT_ROOT / "references"))
    SchemaStore(PROJECT_ROOT / "schemas").validate("paper", normalized)
    write_json(args.output, normalized)
    report_path = args.report or args.output.with_suffix(".normalization-report.json")
    write_json(report_path, report)
    print(json.dumps({"output": str(args.output.resolve()), "report": str(report_path.resolve())}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
