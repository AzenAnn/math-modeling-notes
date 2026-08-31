from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


IGNORED_VAULT_DIRECTORIES = {
    ".git",
    ".modeling-mastery",
    ".obsidian",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "node_modules",
    "venv",
}


def ignore_vault_markdown(path: Path, vault_path: Path) -> bool:
    """Return True for environment/cache Markdown that is not a vault note."""
    relative = path.relative_to(vault_path)
    return any(part in IGNORED_VAULT_DIRECTORIES for part in relative.parts[:-1])


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    marker = text.find("\n---\n", 4)
    if marker < 0:
        return {}, text
    raw = text[4:marker]
    body = text[marker + 5 :]
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        # Template files can contain Jinja or other placeholders inside a
        # frontmatter-looking block. Treat the whole file as ordinary Markdown
        # instead of making an otherwise healthy vault unindexable.
        return {}, text
    if not isinstance(data, dict):
        data = {}
    return data, body


def dump_frontmatter(data: dict[str, Any]) -> str:
    payload = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=1000).strip()
    return f"---\n{payload}\n---\n"
