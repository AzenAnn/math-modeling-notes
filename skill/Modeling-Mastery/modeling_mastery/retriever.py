from __future__ import annotations

import math
from collections import Counter
from pathlib import Path
from typing import Any

from .constants import INDEX_JSON_FILE, REGISTRY_DIR
from .indexer import build_index, tokenize
from .io_utils import read_json, read_yaml


def _infer_fingerprint(query: str, references_dir: Path | None = None) -> dict[str, list[str]]:
    from .io_utils import asset_dir

    directory = references_dir or asset_dir("references")
    mapping_path = directory / "taxonomy" / "problem-types.yaml"
    result = {"categories": [], "tasks": [], "keywords": []}
    if not mapping_path.exists():
        return result
    raw = read_yaml(mapping_path) or []
    lowered = query.casefold()
    for item in raw:
        if not isinstance(item, dict):
            continue
        keywords = [str(value) for value in item.get("keywords", [])]
        if any(keyword.casefold() in lowered for keyword in keywords):
            result["categories"].extend(str(value) for value in item.get("categories", []))
            result["tasks"].extend(str(value) for value in item.get("tasks", []))
            result["keywords"].extend(keywords)
    for key in result:
        result[key] = list(dict.fromkeys(result[key]))
    return result


def search_index(
    vault_path: Path,
    query: str,
    *,
    note_type: str | None = None,
    category: str | None = None,
    tasks: list[str] | None = None,
    top_k: int = 10,
) -> list[dict[str, Any]]:
    vault_path = vault_path.expanduser().resolve()
    index_path = vault_path / REGISTRY_DIR / INDEX_JSON_FILE
    if not index_path.exists():
        build_index(vault_path)
    payload = read_json(index_path)
    notes = payload.get("notes", [])
    filtered = [
        note
        for note in notes
        if (not note_type or note.get("type") == note_type)
        and (not category or note.get("category") == category)
        and (not tasks or set(tasks) & set(note.get("tasks", [])))
    ]
    if not filtered:
        return []
    query_tokens = tokenize(query)
    query_counts = Counter(query_tokens)
    document_frequency: Counter[str] = Counter()
    for note in filtered:
        document_frequency.update(note.get("token_counts", {}).keys())
    n_docs = len(filtered)
    fingerprint = _infer_fingerprint(query)
    results: list[dict[str, Any]] = []
    for note in filtered:
        counts = note.get("token_counts", {})
        length = max(1, int(note.get("length", 1)))
        lexical = 0.0
        matched_tokens: list[str] = []
        for token, query_tf in query_counts.items():
            tf = float(counts.get(token, 0)) / length
            if tf <= 0:
                continue
            idf = math.log((n_docs + 1) / (document_frequency[token] + 1)) + 1.0
            lexical += (1 + math.log(query_tf)) * tf * idf
            matched_tokens.append(token)
        title_lower = note.get("title", "").casefold()
        phrase_bonus = 1.5 if query.casefold() in title_lower else 0.0
        category_bonus = 0.6 if note.get("category") in fingerprint["categories"] else 0.0
        task_hits = set(note.get("tasks", [])) & set(fingerprint["tasks"])
        task_bonus = 0.4 * len(task_hits)
        alias_bonus = 0.7 if any(query.casefold() in alias.casefold() or alias.casefold() in query.casefold() for alias in note.get("aliases", [])) else 0.0
        score = lexical * 100 + phrase_bonus + category_bonus + task_bonus + alias_bonus
        if score <= 0 and not fingerprint["categories"] and not fingerprint["tasks"]:
            continue
        reasons: list[str] = []
        if matched_tokens:
            reasons.append("关键词命中: " + ", ".join(matched_tokens[:8]))
        if category_bonus:
            reasons.append(f"问题类型匹配: {note.get('category')}")
        if task_hits:
            reasons.append("任务匹配: " + ", ".join(sorted(task_hits)))
        if alias_bonus:
            reasons.append("名称/别名匹配")
        results.append(
            {
                "id": note.get("id"),
                "path": note.get("path"),
                "type": note.get("type"),
                "title": note.get("title"),
                "category": note.get("category"),
                "tasks": note.get("tasks", []),
                "source_papers": note.get("source_papers", []),
                "score": round(score, 6),
                "reasons": reasons,
            }
        )
    results.sort(key=lambda item: (-item["score"], item["title"]))
    return results[:top_k]
