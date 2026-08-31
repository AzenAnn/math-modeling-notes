from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT
from modeling_mastery.codegen import reproduce_code
from modeling_mastery.config import Settings
from modeling_mastery.io_utils import read_json, write_json
from modeling_mastery.llm import create_llm
from modeling_mastery.schema_utils import SchemaStore


def main() -> None:
    parser = argparse.ArgumentParser(description="05 Code Reproducer: generate Python, MATLAB, and pytest assets.")
    parser.add_argument("input_ir", type=Path)
    parser.add_argument("--output", "-o", type=Path, required=True)
    parser.add_argument("--updated-ir", type=Path)
    parser.add_argument("--provider", choices=["mock", "openai-compatible", "anthropic", "codex", "claude-code", "local-agent"], default=None)
    parser.add_argument("--max-targets", type=int, default=8)
    parser.add_argument("--no-tests", action="store_true")
    parser.add_argument("--check-octave", action="store_true")
    args = parser.parse_args()
    settings = Settings.from_env()
    updated, report = reproduce_code(
        read_json(args.input_ir),
        args.output,
        llm=create_llm(settings, args.provider),
        max_targets=args.max_targets,
        timeout=settings.code_timeout,
        memory_mb=settings.code_memory_mb,
        run_tests=not args.no_tests,
        check_octave=args.check_octave,
    )
    SchemaStore(PROJECT_ROOT / "schemas").validate("paper", updated)
    updated_ir = args.updated_ir or args.output / "paper_ir.with_code.json"
    write_json(updated_ir, updated)
    write_json(args.output / "code_reproduction_report.json", report)
    print(json.dumps({"updated_ir": str(updated_ir.resolve()), "report": report}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
