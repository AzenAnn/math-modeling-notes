from __future__ import annotations

import argparse
import json
from pathlib import Path

from _bootstrap import PROJECT_ROOT
from modeling_mastery.config import Settings
from modeling_mastery.io_utils import write_json
from modeling_mastery.ir_builder import build_paper_ir
from modeling_mastery.llm import create_llm
from modeling_mastery.normalizer import ReferenceCatalog


def main() -> None:
    parser = argparse.ArgumentParser(description="02-04 Evidence Extractor + Model Miner + Algorithm Miner.")
    parser.add_argument("normalized_markdown", type=Path)
    parser.add_argument("--structure", type=Path)
    parser.add_argument("--page-map", type=Path)
    parser.add_argument("--output", "-o", type=Path, required=True)
    parser.add_argument("--provider", choices=["none", "mock", "openai-compatible", "anthropic", "codex", "claude-code", "local-agent"], default=None)
    parser.add_argument("--chunk-chars", type=int, default=16000)
    args = parser.parse_args()
    llm = create_llm(Settings.from_env(), args.provider)
    ir, report = build_paper_ir(
        args.normalized_markdown,
        structure_path=args.structure,
        page_map_path=args.page_map,
        output_dir=args.output.parent,
        llm=llm,
        catalog=ReferenceCatalog(PROJECT_ROOT / "references"),
        chunk_chars=args.chunk_chars,
    )
    write_json(args.output, ir)
    print(json.dumps({"output": str(args.output.resolve()), "report": report}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
