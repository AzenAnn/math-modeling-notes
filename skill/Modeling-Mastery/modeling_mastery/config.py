from __future__ import annotations

import os
from dataclasses import dataclass, replace
from pathlib import Path


def _int_env(name: str, default: int) -> int:
    raw = os.getenv(name)
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _bool_env(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None or not raw.strip():
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on", "y"}


def _float_env(name: str, default: float) -> float:
    raw = os.getenv(name)
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


@dataclass(frozen=True, slots=True)
class Settings:
    llm_provider: str = "none"
    llm_model: str = ""
    llm_api_key: str = ""
    llm_base_url: str = "https://api.openai.com/v1"
    llm_timeout: int = 180
    llm_max_tokens: int = 12000
    llm_temperature: float = 0.0
    pdf_backend: str = "auto"
    mineru_backend: str = "pipeline"
    vault_path: Path | None = None
    code_timeout: int = 30
    code_memory_mb: int = 2048
    local_agent_cwd: Path | None = None
    local_agent_preference: str = "codex,claude-code"
    local_agent_fallback: bool = True
    codex_command: str = "codex"
    codex_model: str = ""
    codex_sandbox: str = "read-only"
    codex_approval_policy: str = "never"
    codex_extra_args: str = ""
    claude_command: str = "claude"
    claude_model: str = ""
    claude_permission_mode: str = "plan"
    claude_max_turns: int = 1
    claude_max_budget_usd: float = 0.0
    claude_bare: bool = True
    claude_extra_args: str = ""

    @classmethod
    def from_env(cls) -> "Settings":
        vault_raw = os.getenv("MODELING_VAULT_PATH", "").strip()
        local_cwd_raw = os.getenv("MODELING_LOCAL_AGENT_CWD", "").strip()
        return cls(
            llm_provider=os.getenv("MODELING_LLM_PROVIDER", "none").strip().lower(),
            llm_model=os.getenv("MODELING_LLM_MODEL", "").strip(),
            llm_api_key=os.getenv("MODELING_LLM_API_KEY", "").strip(),
            llm_base_url=os.getenv("MODELING_LLM_BASE_URL", "https://api.openai.com/v1").strip(),
            llm_timeout=_int_env("MODELING_LLM_TIMEOUT", 180),
            llm_max_tokens=_int_env("MODELING_LLM_MAX_TOKENS", 12000),
            llm_temperature=_float_env("MODELING_LLM_TEMPERATURE", 0.0),
            pdf_backend=os.getenv("MODELING_PDF_BACKEND", "auto").strip().lower(),
            mineru_backend=os.getenv("MODELING_MINERU_BACKEND", "pipeline").strip(),
            vault_path=Path(vault_raw).expanduser() if vault_raw else None,
            code_timeout=_int_env("MODELING_CODE_TIMEOUT", 30),
            code_memory_mb=_int_env("MODELING_CODE_MEMORY_MB", 2048),
            local_agent_cwd=Path(local_cwd_raw).expanduser() if local_cwd_raw else None,
            local_agent_preference=os.getenv("MODELING_LOCAL_AGENT_PREFERENCE", "codex,claude-code").strip(),
            local_agent_fallback=_bool_env("MODELING_LOCAL_AGENT_FALLBACK", True),
            codex_command=os.getenv("MODELING_CODEX_COMMAND", "codex").strip() or "codex",
            codex_model=os.getenv("MODELING_CODEX_MODEL", "").strip(),
            codex_sandbox=os.getenv("MODELING_CODEX_SANDBOX", "read-only").strip() or "read-only",
            codex_approval_policy=os.getenv("MODELING_CODEX_APPROVAL_POLICY", "never").strip() or "never",
            codex_extra_args=os.getenv("MODELING_CODEX_EXTRA_ARGS", "").strip(),
            claude_command=os.getenv("MODELING_CLAUDE_COMMAND", "claude").strip() or "claude",
            claude_model=os.getenv("MODELING_CLAUDE_MODEL", "").strip(),
            claude_permission_mode=os.getenv("MODELING_CLAUDE_PERMISSION_MODE", "plan").strip() or "plan",
            claude_max_turns=_int_env("MODELING_CLAUDE_MAX_TURNS", 1),
            claude_max_budget_usd=_float_env("MODELING_CLAUDE_MAX_BUDGET_USD", 0.0),
            claude_bare=_bool_env("MODELING_CLAUDE_BARE", True),
            claude_extra_args=os.getenv("MODELING_CLAUDE_EXTRA_ARGS", "").strip(),
        )

    def with_overrides(self, **kwargs: object) -> "Settings":
        return replace(self, **{k: v for k, v in kwargs.items() if v is not None})
