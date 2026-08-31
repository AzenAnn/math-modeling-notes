from __future__ import annotations

import json
import shlex
import sys
from pathlib import Path

import pytest

from modeling_mastery.config import Settings
from modeling_mastery.errors import LLMResponseError
from modeling_mastery.llm import ClaudeCodeCLILLM, CodexCLILLM, LocalAgentLLM, create_llm
from modeling_mastery.pipeline import run_pipeline


def _command_for(script: Path) -> str:
    return f"{shlex.quote(sys.executable)} {shlex.quote(str(script))}"


def _evidence_payload() -> dict:
    return {
        "chunk_id": "TEST",
        "evidence": [],
        "candidate_models": [],
        "candidate_algorithms": [],
        "assumptions": [],
        "variables": [],
        "validation_clues": [],
        "warnings": [],
    }


def _synthesis_payload() -> dict:
    return {
        "bibliographic": {
            "title": "本地 Agent 测试论文",
            "authors": [],
            "year": 2026,
            "competition": "",
            "award": "",
            "problem_id": "",
            "abstract": "",
            "keywords": [],
            "language": "zh-CN",
        },
        "problem": {"background": "", "overall_objective": "测试", "subproblems": []},
        "assumptions": [],
        "variables": [],
        "data": {},
        "modeling_chain": [],
        "models": [],
        "algorithms": [],
        "validation": {},
        "limitations": [],
        "innovations": [],
        "case": {},
        "quality": {"warnings": [], "review_required": True},
    }


def _write_fake_codex(path: Path, *, fail: bool = False, invalid: bool = False) -> None:
    evidence = json.dumps(_evidence_payload(), ensure_ascii=False)
    synthesis = json.dumps(_synthesis_payload(), ensure_ascii=False)
    path.write_text(
        f"""from __future__ import annotations
import json
import pathlib
import sys

args = sys.argv[1:]
prompt = sys.stdin.read()
pathlib.Path(__file__).with_suffix('.args.json').write_text(json.dumps(args), encoding='utf-8')
if {str(fail)}:
    print('simulated codex failure', file=sys.stderr)
    raise SystemExit(7)
try:
    output = args[args.index('--output-last-message') + 1]
except (ValueError, IndexError):
    print('missing output path', file=sys.stderr)
    raise SystemExit(8)
if {str(invalid)}:
    payload = {{'not': 'the required evidence shape'}}
elif 'structured task: synthesis' in prompt:
    payload = json.loads({synthesis!r})
else:
    payload = json.loads({evidence!r})
pathlib.Path(output).write_text(json.dumps(payload, ensure_ascii=False), encoding='utf-8')
print(json.dumps(payload, ensure_ascii=False))
""",
        encoding="utf-8",
    )


def _write_fake_claude(path: Path, *, invalid: bool = False) -> None:
    evidence = json.dumps(_evidence_payload(), ensure_ascii=False)
    path.write_text(
        f"""from __future__ import annotations
import json
import pathlib
import sys

args = sys.argv[1:]
_ = sys.stdin.read()
pathlib.Path(__file__).with_suffix('.args.json').write_text(json.dumps(args), encoding='utf-8')
payload = {{'wrong': True}} if {str(invalid)} else json.loads({evidence!r})
print(json.dumps({{'type': 'result', 'structured_output': payload}}, ensure_ascii=False))
""",
        encoding="utf-8",
    )


def test_codex_cli_provider_uses_structured_output_and_safe_flags(tmp_path: Path) -> None:
    script = tmp_path / "fake_codex.py"
    _write_fake_codex(script)
    llm = CodexCLILLM(
        Settings(
            llm_provider="codex",
            codex_command=_command_for(script),
            local_agent_cwd=tmp_path,
            llm_timeout=10,
        )
    )
    result = llm.generate_json(system="system", user="user", purpose="evidence")
    assert result.data["chunk_id"] == "TEST"
    args = json.loads(script.with_suffix(".args.json").read_text(encoding="utf-8"))
    assert "exec" in args
    assert "--output-schema" in args
    assert args[args.index("--sandbox") + 1] == "read-only"
    assert args[args.index("--ask-for-approval") + 1] == "never"
    assert args.index("--ask-for-approval") < args.index("exec")
    assert args[-1] == "-"


def test_claude_code_provider_reads_structured_output_wrapper(tmp_path: Path) -> None:
    script = tmp_path / "fake_claude.py"
    _write_fake_claude(script)
    llm = ClaudeCodeCLILLM(
        Settings(
            llm_provider="claude-code",
            claude_command=_command_for(script),
            local_agent_cwd=tmp_path,
            llm_timeout=10,
        )
    )
    result = llm.generate_json(system="system", user="user", purpose="evidence")
    assert result.data["chunk_id"] == "TEST"
    args = json.loads(script.with_suffix(".args.json").read_text(encoding="utf-8"))
    assert "--print" in args
    assert "--json-schema" in args
    assert "--bare" in args
    assert args[args.index("--tools") + 1] == ""
    assert args[args.index("--permission-mode") + 1] == "plan"


def test_local_agent_falls_back_from_codex_to_claude(tmp_path: Path) -> None:
    codex = tmp_path / "bad_codex.py"
    claude = tmp_path / "good_claude.py"
    _write_fake_codex(codex, fail=True)
    _write_fake_claude(claude)
    llm = LocalAgentLLM(
        Settings(
            llm_provider="local-agent",
            codex_command=_command_for(codex),
            claude_command=_command_for(claude),
            local_agent_cwd=tmp_path,
            local_agent_preference="codex,claude-code",
            local_agent_fallback=True,
            llm_timeout=10,
        )
    )
    result = llm.generate_json(system="system", user="user", purpose="evidence")
    assert result.provider == "claude-code"


def test_local_cli_rejects_schema_invalid_output(tmp_path: Path) -> None:
    script = tmp_path / "invalid_codex.py"
    _write_fake_codex(script, invalid=True)
    llm = CodexCLILLM(
        Settings(codex_command=_command_for(script), local_agent_cwd=tmp_path, llm_timeout=10)
    )
    with pytest.raises(LLMResponseError):
        llm.generate_json(system="system", user="user", purpose="evidence")


def test_create_llm_recognizes_local_provider_aliases(tmp_path: Path) -> None:
    codex = tmp_path / "codex.py"
    claude = tmp_path / "claude.py"
    _write_fake_codex(codex)
    _write_fake_claude(claude)
    settings = Settings(
        codex_command=_command_for(codex),
        claude_command=_command_for(claude),
        local_agent_cwd=tmp_path,
    )
    assert isinstance(create_llm(settings, "codex"), CodexCLILLM)
    assert isinstance(create_llm(settings, "claude"), ClaudeCodeCLILLM)
    assert isinstance(create_llm(settings, "local-agent"), LocalAgentLLM)


def test_fake_codex_can_drive_full_markdown_pipeline(
    tmp_path: Path, demo_markdown: str, project_root: Path
) -> None:
    script = tmp_path / "pipeline_codex.py"
    _write_fake_codex(script)
    paper = tmp_path / "paper.md"
    paper.write_text(demo_markdown, encoding="utf-8")
    settings = Settings(
        llm_provider="codex",
        pdf_backend="markdown",
        codex_command=_command_for(script),
        local_agent_cwd=tmp_path,
        llm_timeout=20,
    )
    report = run_pipeline(
        paper,
        tmp_path / "workspace",
        settings=settings,
        backend="markdown",
        provider="codex",
        reproduce=False,
        project_root=project_root,
    )
    assert Path(report["paper_ir"]).exists()
    assert report["stages"]["02_04_analysis"]["provider"] == "codex"
