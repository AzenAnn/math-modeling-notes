from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT  # noqa: F401
from modeling_mastery.code_validation import validate_file
from modeling_mastery.runner import run_python_file, run_python_tests


def main() -> None:
    parser = argparse.ArgumentParser(description="Run validated Python code with timeout/resource limits.")
    parser.add_argument("path", type=Path, help="Python file or recipe directory containing python/ and tests/.")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--memory-mb", type=int, default=2048)
    args = parser.parse_args()
    if args.path.is_dir():
        result = run_python_tests(args.path, timeout=args.timeout, memory_mb=args.memory_mb)
    else:
        report = validate_file(args.path)
        if not report.safe:
            print(json.dumps({"validation": report.as_dict(), "executed": False}, ensure_ascii=False, indent=2))
            raise SystemExit(2)
        result = run_python_file(args.path, timeout=args.timeout, memory_mb=args.memory_mb)
    print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2))
    raise SystemExit(0 if result.passed else 3)


if __name__ == "__main__":
    main()
