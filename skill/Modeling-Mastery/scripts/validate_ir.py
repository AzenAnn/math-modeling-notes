from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT
from modeling_mastery.io_utils import read_json
from modeling_mastery.schema_utils import SchemaStore


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a Modeling-Mastery Paper IR.")
    parser.add_argument("ir", type=Path)
    args = parser.parse_args()
    errors = SchemaStore(PROJECT_ROOT / "schemas").errors("paper", read_json(args.ir))
    print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if not errors else 2)


if __name__ == "__main__":
    main()
