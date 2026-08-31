from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT  # noqa: F401
from modeling_mastery.code_validation import validate_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Static validation for generated Python/MATLAB code.")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    report = validate_file(args.path)
    print(json.dumps(report.as_dict(), ensure_ascii=False, indent=2))
    raise SystemExit(0 if report.safe else 2)


if __name__ == "__main__":
    main()
