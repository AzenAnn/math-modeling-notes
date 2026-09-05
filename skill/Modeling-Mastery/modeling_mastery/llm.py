from __future__ import annotations

import json
import os
import re
import shlex
import shutil
import subprocess
import tempfile
import urllib.error
import urllib.request
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .config import Settings
from .errors import LLMConfigurationError, LLMResponseError
from .structured_output import schema_for_codex, schema_for_purpose, validate_purpose_output


@dataclass(slots=True)
class LLMResult:
    data: dict[str, Any]
    raw_text: str
    provider: str
    model: str


class BaseLLM(ABC):
    provider: str
    model: str

    @abstractmethod
    def generate_json(
        self,
        *,
        system: str,
        user: str,
        purpose: str,
        max_tokens: int | None = None,
    ) -> LLMResult:
        raise NotImplementedError


def extract_json_object(text: str) -> dict[str, Any]:
    stripped = text.strip()
    fences = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", stripped, re.DOTALL | re.I)
    candidates = [*fences, stripped]
    decoder = json.JSONDecoder()
    for candidate in candidates:
        try:
            value = json.loads(candidate)
            if isinstance(value, dict):
                return value
        except json.JSONDecodeError:
            pass
        for index, char in enumerate(candidate):
            if char != "{":
                continue
            try:
                value, _ = decoder.raw_decode(candidate[index:])
                if isinstance(value, dict):
                    return value
            except json.JSONDecodeError:
                continue
    raise LLMResponseError("No valid JSON object was found in the LLM response.")




def _split_command(raw: str, default: str) -> list[str]:
    value = os.path.expandvars(os.path.expanduser((raw or default).strip()))
    if not value:
        value = default
    candidate = Path(value)
    if candidate.exists():
        return [str(candidate)]
    try:
        parts = shlex.split(value, posix=os.name != "nt")
    except ValueError as exc:
        raise LLMConfigurationError(f"Invalid local CLI command {value!r}: {exc}") from exc
    if not parts:
        raise LLMConfigurationError(f"Local CLI command is empty: {value!r}")
    if os.name == "nt":
        # ``shlex.quote`` uses POSIX single quotes.  With ``posix=False`` (needed
        # to preserve Windows backslashes), ``shlex.split`` retains those outer
        # quotes, so a valid command such as ``'C:\\...\\python.exe' script.py``
        # fails the existence check below.  Remove only matching wrapper quotes;
        # embedded quotes and the token content stay untouched.
        parts = [
            part[1:-1]
            if len(part) >= 2 and part[0] == part[-1] and part[0] in {"'", '"'}
            else part
            for part in parts
        ]
    return parts


def command_available(raw: str, default: str) -> bool:
    try:
        executable = _split_command(raw, default)[0]
    except LLMConfigurationError:
        return False
    path = Path(executable).expanduser()
    return path.exists() or shutil.which(executable) is not None


def _combined_prompt(system: str, user: str, purpose: str) -> str:
    return (
        f"Modeling-Mastery structured task: {purpose}\n\n"
        "Follow the SYSTEM instructions exactly. Return only the final JSON object required by the schema. "
        "Do not expose private chain-of-thought.\n\n"
        f"SYSTEM\n{system.strip()}\n\n"
        f"USER PAYLOAD\n{user.strip()}\n"
    )


def _run_local_cli(
    args: list[str],
    *,
    input_text: str,
    cwd: Path,
    timeout: int,
    provider: str,
) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment.setdefault("NO_COLOR", "1")
    try:
        completed = subprocess.run(
            args,
            input=input_text,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            cwd=str(cwd),
            env=environment,
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError as exc:
        raise LLMConfigurationError(
            f"{provider} CLI was not found. Configure its command path or install/login to the CLI first."
        ) from exc
    except subprocess.TimeoutExpired as exc:
        raise LLMResponseError(f"{provider} CLI timed out after {timeout} seconds.") from exc
    if completed.returncode != 0:
        stderr = completed.stderr.strip()
        stdout = completed.stdout.strip()
        detail = stderr or stdout or "no diagnostic output"
        raise LLMResponseError(
            f"{provider} CLI exited with status {completed.returncode}: {detail[-4000:]}"
        )
    return completed


class CodexCLILLM(BaseLLM):
    """Use the locally installed and already authenticated Codex CLI as the semantic engine."""

    provider = "codex"

    def __init__(self, settings: Settings):
        self.command = _split_command(settings.codex_command, "codex")
        if not command_available(settings.codex_command, "codex"):
            raise LLMConfigurationError(
                "Codex CLI is unavailable. Install/login to Codex or set MODELING_CODEX_COMMAND."
            )
        self.model = settings.codex_model or settings.llm_model or "cli-default"
        self.model_override = settings.codex_model or settings.llm_model
        self.sandbox = settings.codex_sandbox
        if self.sandbox not in {"read-only", "workspace-write", "danger-full-access"}:
            raise LLMConfigurationError(
                "MODELING_CODEX_SANDBOX must be read-only, workspace-write, or danger-full-access."
            )
        self.approval_policy = settings.codex_approval_policy
        if self.approval_policy not in {"untrusted", "on-request", "never"}:
            raise LLMConfigurationError(
                "MODELING_CODEX_APPROVAL_POLICY must be untrusted, on-request, or never."
            )
        self.extra_args = shlex.split(settings.codex_extra_args, posix=os.name != "nt") if settings.codex_extra_args else []
        self.cwd = (settings.local_agent_cwd or Path.cwd()).expanduser().resolve()
        self.timeout = settings.llm_timeout
        self.max_tokens = settings.llm_max_tokens

    def generate_json(
        self,
        *,
        system: str,
        user: str,
        purpose: str,
        max_tokens: int | None = None,
    ) -> LLMResult:
        del max_tokens  # Codex CLI uses the configured model/session limits.
        schema = schema_for_codex(purpose)
        prompt = _combined_prompt(system, user, purpose)
        with tempfile.TemporaryDirectory(prefix="modeling-mastery-codex-") as temporary:
            temporary_path = Path(temporary)
            schema_path = temporary_path / "output.schema.json"
            output_path = temporary_path / "final.json"
            schema_path.write_text(json.dumps(schema, ensure_ascii=False, indent=2), encoding="utf-8")
            args = [
                *self.command,
                "--ask-for-approval",
                self.approval_policy,
                "exec",
                "--sandbox",
                self.sandbox,
                "--skip-git-repo-check",
                "--cd",
                str(self.cwd),
                "--output-schema",
                str(schema_path),
                "--output-last-message",
                str(output_path),
            ]
            if self.model_override:
                args.extend(["--model", self.model_override])
            args.extend(self.extra_args)
            args.append("-")
            completed = _run_local_cli(
                args,
                input_text=prompt,
                cwd=self.cwd,
                timeout=self.timeout,
                provider="Codex",
            )
            raw_text = output_path.read_text(encoding="utf-8", errors="replace") if output_path.exists() else completed.stdout
        data = extract_json_object(raw_text or completed.stdout)
        validate_purpose_output(data, purpose)
        return LLMResult(data, raw_text, self.provider, self.model)


class ClaudeCodeCLILLM(BaseLLM):
    """Use the locally installed and already authenticated Claude Code CLI."""

    provider = "claude-code"

    def __init__(self, settings: Settings):
        self.command = _split_command(settings.claude_command, "claude")
        if not command_available(settings.claude_command, "claude"):
            raise LLMConfigurationError(
                "Claude Code CLI is unavailable. Install/login to Claude Code or set MODELING_CLAUDE_COMMAND."
            )
        self.model = settings.claude_model or settings.llm_model or "cli-default"
        self.model_override = settings.claude_model or settings.llm_model
        self.permission_mode = settings.claude_permission_mode
        allowed_modes = {"default", "manual", "acceptEdits", "plan", "auto", "dontAsk", "bypassPermissions"}
        if self.permission_mode not in allowed_modes:
            raise LLMConfigurationError(
                "MODELING_CLAUDE_PERMISSION_MODE is not a supported Claude Code permission mode."
            )
        self.max_turns = max(1, settings.claude_max_turns)
        self.max_budget_usd = max(0.0, settings.claude_max_budget_usd)
        self.bare = settings.claude_bare
        self.extra_args = shlex.split(settings.claude_extra_args, posix=os.name != "nt") if settings.claude_extra_args else []
        self.cwd = (settings.local_agent_cwd or Path.cwd()).expanduser().resolve()
        self.timeout = settings.llm_timeout
        self.max_tokens = settings.llm_max_tokens

    def generate_json(
        self,
        *,
        system: str,
        user: str,
        purpose: str,
        max_tokens: int | None = None,
    ) -> LLMResult:
        del max_tokens  # Claude Code print mode does not expose a direct max-output-tokens flag.
        schema = schema_for_purpose(purpose)
        # Claude Code currently rejects the draft 2020-12 meta-schema URI even
        # though it accepts the concrete object/array constraints we use.
        schema.pop("$schema", None)
        schema_text = json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
        args = [*self.command, "--print"]
        if self.bare:
            args.append("--bare")
        args.extend(
            [
                "--output-format",
                "json",
                "--json-schema",
                schema_text,
                "--permission-mode",
                self.permission_mode,
                "--tools",
                "",
                "--disallowedTools",
                "mcp__*",
                "--no-session-persistence",
                "--max-turns",
                str(self.max_turns),
                "--system-prompt",
                system,
            ]
        )
        if self.model_override:
            args.extend(["--model", self.model_override])
        if self.max_budget_usd > 0:
            args.extend(["--max-budget-usd", str(self.max_budget_usd)])
        args.extend(self.extra_args)
        completed = _run_local_cli(
            args,
            input_text=user,
            cwd=self.cwd,
            timeout=self.timeout,
            provider="Claude Code",
        )
        raw_text = completed.stdout.strip()
        outer = extract_json_object(raw_text)
        structured = outer.get("structured_output")
        if isinstance(structured, dict):
            data = structured
        elif isinstance(outer.get("result"), dict):
            data = outer["result"]
        elif isinstance(outer.get("result"), str):
            data = extract_json_object(outer["result"])
        else:
            data = outer
        validate_purpose_output(data, purpose)
        return LLMResult(data, raw_text, self.provider, self.model)


class LocalAgentLLM(BaseLLM):
    """Try local Codex and/or Claude Code according to the configured preference."""

    provider = "local-agent"

    def __init__(self, settings: Settings):
        aliases = {
            "codex": "codex",
            "openai-codex": "codex",
            "claude": "claude-code",
            "claudecode": "claude-code",
            "claude-code": "claude-code",
        }
        requested = [
            aliases.get(item.strip().lower(), item.strip().lower())
            for item in settings.local_agent_preference.split(",")
            if item.strip()
        ] or ["codex", "claude-code"]
        backends: list[BaseLLM] = []
        configuration_errors: list[str] = []
        for name in requested:
            try:
                if name == "codex":
                    backends.append(CodexCLILLM(settings))
                elif name == "claude-code":
                    backends.append(ClaudeCodeCLILLM(settings))
            except LLMConfigurationError as exc:
                configuration_errors.append(str(exc))
        if not backends:
            detail = "; ".join(configuration_errors) or "no recognized local agents were requested"
            raise LLMConfigurationError(f"No local agent CLI is ready: {detail}")
        self.backends = backends if settings.local_agent_fallback else backends[:1]
        self.model = " -> ".join(f"{item.provider}:{item.model}" for item in self.backends)
        self.max_tokens = settings.llm_max_tokens

    def generate_json(
        self,
        *,
        system: str,
        user: str,
        purpose: str,
        max_tokens: int | None = None,
    ) -> LLMResult:
        errors: list[str] = []
        for backend in self.backends:
            try:
                return backend.generate_json(
                    system=system,
                    user=user,
                    purpose=purpose,
                    max_tokens=max_tokens,
                )
            except (LLMConfigurationError, LLMResponseError) as exc:
                errors.append(f"{backend.provider}: {exc}")
        raise LLMResponseError("All configured local agent CLIs failed: " + " | ".join(errors))


class OpenAICompatibleLLM(BaseLLM):
    provider = "openai-compatible"

    def __init__(self, settings: Settings):
        if not settings.llm_api_key:
            raise LLMConfigurationError("MODELING_LLM_API_KEY is required.")
        if not settings.llm_model:
            raise LLMConfigurationError("MODELING_LLM_MODEL is required.")
        self.model = settings.llm_model
        self.api_key = settings.llm_api_key
        self.base_url = settings.llm_base_url.rstrip("/")
        self.timeout = settings.llm_timeout
        self.max_tokens = settings.llm_max_tokens
        self.temperature = settings.llm_temperature

    def generate_json(
        self,
        *,
        system: str,
        user: str,
        purpose: str,
        max_tokens: int | None = None,
    ) -> LLMResult:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": self.temperature,
            "max_tokens": max_tokens or self.max_tokens,
            "response_format": {"type": "json_object"},
        }
        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "User-Agent": "Modeling-Mastery/0.2.0",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise LLMResponseError(f"OpenAI-compatible HTTP {exc.code}: {detail[:2000]}") from exc
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise LLMResponseError(f"OpenAI-compatible request failed: {exc}") from exc
        try:
            content = body["choices"][0]["message"]["content"]
            if isinstance(content, list):
                content = "".join(str(part.get("text", "")) for part in content if isinstance(part, dict))
        except (KeyError, IndexError, TypeError) as exc:
            raise LLMResponseError(f"Unexpected OpenAI-compatible response: {body}") from exc
        return LLMResult(extract_json_object(str(content)), str(content), self.provider, self.model)


class AnthropicLLM(BaseLLM):
    provider = "anthropic"

    def __init__(self, settings: Settings):
        if not settings.llm_api_key:
            raise LLMConfigurationError("MODELING_LLM_API_KEY is required.")
        if not settings.llm_model:
            raise LLMConfigurationError("MODELING_LLM_MODEL is required.")
        self.model = settings.llm_model
        self.api_key = settings.llm_api_key
        self.base_url = settings.llm_base_url.rstrip("/") if settings.llm_base_url else "https://api.anthropic.com"
        if self.base_url.endswith("/v1"):
            self.base_url = self.base_url[:-3]
        self.timeout = settings.llm_timeout
        self.max_tokens = settings.llm_max_tokens
        self.temperature = settings.llm_temperature

    def generate_json(
        self,
        *,
        system: str,
        user: str,
        purpose: str,
        max_tokens: int | None = None,
    ) -> LLMResult:
        payload = {
            "model": self.model,
            "system": system,
            "messages": [{"role": "user", "content": user}],
            "temperature": self.temperature,
            "max_tokens": max_tokens or self.max_tokens,
        }
        request = urllib.request.Request(
            f"{self.base_url}/v1/messages",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
                "user-agent": "Modeling-Mastery/0.2.0",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise LLMResponseError(f"Anthropic HTTP {exc.code}: {detail[:2000]}") from exc
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise LLMResponseError(f"Anthropic request failed: {exc}") from exc
        try:
            content = "".join(block.get("text", "") for block in body["content"] if block.get("type") == "text")
        except (KeyError, TypeError) as exc:
            raise LLMResponseError(f"Unexpected Anthropic response: {body}") from exc
        return LLMResult(extract_json_object(content), content, self.provider, self.model)


class MockLLM(BaseLLM):
    provider = "mock"
    model = "deterministic-mock"

    def generate_json(
        self,
        *,
        system: str,
        user: str,
        purpose: str,
        max_tokens: int | None = None,
    ) -> LLMResult:
        if purpose == "evidence":
            data = {
                "chunk_id": "MOCK",
                "evidence": [],
                "candidate_models": [],
                "candidate_algorithms": [],
                "assumptions": [],
                "variables": [],
                "validation_clues": [],
                "warnings": ["Mock provider did not perform semantic extraction."],
            }
        elif purpose == "code":
            data = {
                "python_code": "def solve(data):\n    raise NotImplementedError('Mock provider')\n",
                "matlab_code": "function out = solve(data)\nerror('Mock provider');\nend\n",
                "pytest_code": "import pytest\nfrom implementation import solve\n\ndef test_mock():\n    with pytest.raises(NotImplementedError):\n        solve(None)\n",
                "metadata": {
                    "entrypoint": "solve",
                    "dependencies": [],
                    "input_contract": ["manual review required"],
                    "output_contract": ["manual review required"],
                    "assumptions": ["Mock implementation"],
                    "limitations": ["Not a real reproduction"],
                },
            }
        else:
            data = {}
        return LLMResult(data, json.dumps(data, ensure_ascii=False), self.provider, self.model)


def create_llm(settings: Settings, provider: str | None = None) -> BaseLLM | None:
    selected = (provider or settings.llm_provider or "none").strip().lower()
    if selected in {"none", "off", "disabled", "heuristic"}:
        return None
    if selected in {"openai", "openai-compatible", "compatible"}:
        return OpenAICompatibleLLM(settings)
    if selected == "anthropic":
        return AnthropicLLM(settings)
    if selected in {"codex", "codex-cli", "openai-codex"}:
        return CodexCLILLM(settings)
    if selected in {"claude", "claude-code", "claudecode", "claude-cli"}:
        return ClaudeCodeCLILLM(settings)
    if selected in {"local", "local-agent", "local-cli", "auto-local"}:
        return LocalAgentLLM(settings)
    if selected == "mock":
        return MockLLM()
    raise LLMConfigurationError(f"Unknown LLM provider: {selected}")
