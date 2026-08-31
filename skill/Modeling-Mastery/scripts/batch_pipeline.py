from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import bootstrap

bootstrap()

from modeling_mastery.batch import run_batch  # noqa: E402
from modeling_mastery.config import Settings  # noqa: E402
from modeling_mastery.io_utils import find_project_root  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch-run Modeling-Mastery over a folder of papers.")
    parser.add_argument("input_root", type=Path)
    parser.add_argument("--workspace-root", type=Path, required=True)
    parser.add_argument("--vault", type=Path)
    parser.add_argument("--backend", default=None)
    parser.add_argument("--provider", default=None)
    parser.add_argument("--reproduce-code", action="store_true")
    parser.add_argument("--max-code-targets", type=int, default=8)
    parser.add_argument("--no-tests", action="store_true")
    parser.add_argument("--check-octave", action="store_true")
    parser.add_argument("--no-recursive", action="store_true")
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--fail-fast", action="store_true")
    args = parser.parse_args()

    report = run_batch(
        args.input_root,
        args.workspace_root,
        vault_path=args.vault,
        settings=Settings.from_env(),
        backend=args.backend,
        provider=args.provider,
        reproduce=args.reproduce_code,
        max_code_targets=args.max_code_targets,
        run_tests=not args.no_tests,
        check_octave=args.check_octave,
        project_root=find_project_root(),
        recursive=not args.no_recursive,
        resume=not args.no_resume,
        continue_on_error=not args.fail_fast,
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
