from __future__ import annotations

import importlib.util
import os
import shutil
import sys
from pathlib import Path
from typing import Any

from .config import Settings
from .llm import command_available


def doctor_report(settings: Settings | None = None) -> dict[str, Any]:
    settings = settings or Settings.from_env()
    modules = {
        "jinja2": importlib.util.find_spec("jinja2") is not None,
        "jsonschema": importlib.util.find_spec("jsonschema") is not None,
        "yaml": importlib.util.find_spec("yaml") is not None,
        "fitz": importlib.util.find_spec("fitz") is not None,
        "docling": importlib.util.find_spec("docling") is not None,
        "pytest": importlib.util.find_spec("pytest") is not None,
    }
    codex_ready = command_available(settings.codex_command, "codex")
    claude_ready = command_available(settings.claude_command, "claude")
    commands = {
        "mineru": shutil.which("mineru"),
        "docling": shutil.which("docling"),
        "octave": shutil.which("octave") or shutil.which("octave-cli"),
        "codex": settings.codex_command if codex_ready else None,
        "claude": settings.claude_command if claude_ready else None,
    }
    selected = settings.llm_provider
    if selected in {"none", "mock", "off", "disabled", "heuristic"}:
        llm_ready = True
    elif selected in {"openai", "openai-compatible", "compatible", "anthropic"}:
        llm_ready = bool(settings.llm_api_key and settings.llm_model)
    elif selected in {"codex", "codex-cli", "openai-codex"}:
        llm_ready = codex_ready
    elif selected in {"claude", "claude-code", "claudecode", "claude-cli"}:
        llm_ready = claude_ready
    elif selected in {"local", "local-agent", "local-cli", "auto-local"}:
        llm_ready = codex_ready or claude_ready
    else:
        llm_ready = False
    vault = settings.vault_path
    return {
        "python": {"version": sys.version, "compatible": sys.version_info >= (3, 11)},
        "modules": modules,
        "commands": commands,
        "llm": {
            "provider": settings.llm_provider,
            "model": settings.llm_model,
            "base_url": settings.llm_base_url,
            "api_key_present": bool(settings.llm_api_key),
            "ready": llm_ready,
            "local_agents": {
                "codex": {
                    "command": settings.codex_command,
                    "available": codex_ready,
                    "model": settings.codex_model or settings.llm_model or "cli-default",
                    "sandbox": settings.codex_sandbox,
                    "approval_policy": settings.codex_approval_policy,
                },
                "claude_code": {
                    "command": settings.claude_command,
                    "available": claude_ready,
                    "model": settings.claude_model or settings.llm_model or "cli-default",
                    "permission_mode": settings.claude_permission_mode,
                    "bare": settings.claude_bare,
                },
                "preference": settings.local_agent_preference,
                "fallback": settings.local_agent_fallback,
            },
        },
        "pdf_backend": settings.pdf_backend,
        "mineru_backend": settings.mineru_backend,
        "vault": {
            "path": str(vault) if vault else "",
            "exists": bool(vault and vault.exists()),
            "writable": bool(vault and vault.exists() and os.access(vault, os.W_OK)),
        },
        "cwd": str(Path.cwd()),
    }
