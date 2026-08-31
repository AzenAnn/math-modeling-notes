from __future__ import annotations

import json
import re
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Any

from .constants import INDEX_DB_FILE, INDEX_JSON_FILE, REGISTRY_DIR
from .frontmatter import ignore_vault_markdown, split_frontmatter
from .io_utils import normalize_space, utc_now_iso, write_json

CJK = re.compile(r"[\u3400-\u9fff]")
ALNUM_WORD = re.compile(r"[a-zA-Z0-9_+.-]+")


def tokenize(text: str) -> list[str]:
    normalized = normalize_space(text).casefold()
    tokens = ALNUM_WORD.findall(normalized)
    cjk_chars = [char for char in normalized if CJK.match(char)]
    tokens.extend(cjk_chars)
    tokens.extend("".join(cjk_chars[index : index + 2]) for index in range(max(0, len(cjk_chars) - 1)))
    return [token for token in tokens if token.strip()]


def _plain_markdown(body: str) -> str:
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    body = re.sub(r"!?(?:\[([^\]]*)\])\([^\)]*\)", r"\1", body)
    body = re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", body)
    body = re.sub(r"[#>*_`~-]", " ", body)
    return normalize_space(body)


def build_index(vault_path: Path) -> dict[str, Any]:
    vault_path = vault_path.expanduser().resolve()
    registry_dir = vault_path / REGISTRY_DIR
    registry_dir.mkdir(parents=True, exist_ok=True)
    entries: list[dict[str, Any]] = []
    for path in sorted(vault_path.rglob("*.md")):
        if ignore_vault_markdown(path, vault_path):
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        metadata, body = split_frontmatter(raw)
        title_match = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
        title = str(metadata.get("canonical_name") or metadata.get("title") or (title_match.group(1) if title_match else path.stem))
        aliases = [str(value) for value in metadata.get("aliases", []) or []]
        tags = [str(value) for value in metadata.get("tags", []) or []]
        tasks = [str(value) for value in metadata.get("tasks", []) or []]
        text = _plain_markdown(body)
        token_counts = Counter(tokenize(" ".join([title, *aliases, *tags, *tasks, text])))
        entries.append(
            {
                "id": str(metadata.get("id") or path.relative_to(vault_path).as_posix()),
                "path": path.relative_to(vault_path).as_posix(),
                "type": str(metadata.get("type") or "note"),
                "title": title,
                "canonical_name": str(metadata.get("canonical_name") or ""),
                "aliases": aliases,
                "category": str(metadata.get("category") or ""),
                "tasks": tasks,
                "tags": tags,
                "source_papers": [str(value) for value in metadata.get("source_papers", []) or []],
                "content": text,
                "token_counts": dict(token_counts),
                "length": sum(token_counts.values()),
            }
        )

    payload = {"schema_version": "1.0.0", "generated_at": utc_now_iso(), "vault": str(vault_path), "notes": entries}
    write_json(registry_dir / INDEX_JSON_FILE, payload)

    database_path = registry_dir / INDEX_DB_FILE
    if database_path.exists():
        database_path.unlink()
    connection = sqlite3.connect(database_path)
    try:
        connection.execute(
            "CREATE TABLE note_metadata (id TEXT PRIMARY KEY, path TEXT, type TEXT, title TEXT, category TEXT, metadata_json TEXT)"
        )
        fts_enabled = True
        try:
            connection.execute(
                "CREATE VIRTUAL TABLE note_fts USING fts5(id UNINDEXED, title, aliases, tags, tasks, content, tokenize='unicode61')"
            )
        except sqlite3.OperationalError:
            fts_enabled = False
            connection.execute(
                "CREATE TABLE note_fts (id TEXT, title TEXT, aliases TEXT, tags TEXT, tasks TEXT, content TEXT)"
            )
        for entry in entries:
            connection.execute(
                "INSERT INTO note_metadata VALUES (?, ?, ?, ?, ?, ?)",
                (entry["id"], entry["path"], entry["type"], entry["title"], entry["category"], json.dumps(entry, ensure_ascii=False)),
            )
            connection.execute(
                "INSERT INTO note_fts VALUES (?, ?, ?, ?, ?, ?)",
                (entry["id"], entry["title"], " ".join(entry["aliases"]), " ".join(entry["tags"]), " ".join(entry["tasks"]), entry["content"]),
            )
        connection.commit()
    finally:
        connection.close()
    return {"vault": str(vault_path), "note_count": len(entries), "index_json": str(registry_dir / INDEX_JSON_FILE), "index_db": str(database_path), "fts5": fts_enabled}
