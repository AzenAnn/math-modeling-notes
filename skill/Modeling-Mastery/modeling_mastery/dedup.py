from __future__ import annotations

from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from .frontmatter import ignore_vault_markdown, split_frontmatter
from .io_utils import canonical_key, write_json


def scan_duplicates(vault_path: Path, *, fuzzy_threshold: float = 0.93) -> dict[str, Any]:
    vault_path = vault_path.expanduser().resolve()
    records: list[dict[str, Any]] = []
    for path in vault_path.rglob("*.md"):
        if ignore_vault_markdown(path, vault_path):
            continue
        metadata, body = split_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        note_type = str(metadata.get("type") or "unknown")
        name = str(metadata.get("canonical_name") or metadata.get("title") or path.stem)
        if note_type not in {"model", "algorithm", "code", "case", "paper"}:
            continue
        records.append(
            {
                "path": path.relative_to(vault_path).as_posix(),
                "type": note_type,
                "name": name,
                "key": canonical_key(name),
                "aliases": metadata.get("aliases", []),
            }
        )
    exact_groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for record in records:
        exact_groups.setdefault((record["type"], record["key"]), []).append(record)
    exact = [group for group in exact_groups.values() if len(group) > 1]
    fuzzy: list[dict[str, Any]] = []
    for index, left in enumerate(records):
        for right in records[index + 1 :]:
            if left["type"] != right["type"] or left["key"] == right["key"]:
                continue
            score = SequenceMatcher(None, left["key"], right["key"]).ratio()
            alias_keys = {canonical_key(alias) for alias in [*left.get("aliases", []), *right.get("aliases", [])]}
            alias_hit = left["key"] in alias_keys or right["key"] in alias_keys
            if score >= fuzzy_threshold or alias_hit:
                fuzzy.append({"left": left, "right": right, "score": round(score, 4), "alias_hit": alias_hit})
    report = {
        "vault": str(vault_path),
        "note_count": len(records),
        "exact_duplicate_groups": exact,
        "fuzzy_candidates": fuzzy,
        "advice": "Modeling-Mastery writes canonical notes idempotently. Review fuzzy candidates manually before merging user-authored content.",
    }
    report_path = vault_path / ".modeling-mastery" / "dedup_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(report_path, report)
    return report
