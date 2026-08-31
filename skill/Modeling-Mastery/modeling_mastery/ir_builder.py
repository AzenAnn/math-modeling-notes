from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any

from .constants import SCHEMA_VERSION
from .evidence import (
    chunk_markdown,
    heuristic_evidence,
    repair_evidence_anchors,
    stable_evidence_id,
)
from .io_utils import (
    merge_unique,
    normalize_space,
    read_json,
    sha256_file,
    sha256_text,
    slug_id,
    utc_now_iso,
    write_json,
)
from .llm import BaseLLM
from .normalizer import (
    ALGORITHM_CATEGORIES,
    MODEL_CATEGORIES,
    ReferenceCatalog,
    normalize_category,
)
from .prompts import EVIDENCE_SYSTEM, SYNTHESIS_SYSTEM
from .schema_utils import SchemaStore

LOGGER = logging.getLogger(__name__)


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    return [value]


def _strings(value: Any) -> list[str]:
    return [str(item).strip() for item in _as_list(value) if str(item).strip()]


def _provenance(value: Any, default: str = "AI_INFERRED") -> str:
    allowed = {"PAPER_EXPLICIT", "PAPER_DERIVED", "AI_INFERRED", "EXTERNAL_REFERENCE", "HEURISTIC"}
    raw = str(value or default).strip().upper()
    return raw if raw in allowed else default


def _confidence(value: Any, default: float = 0.5) -> float:
    try:
        return max(0.0, min(1.0, float(value)))
    except (TypeError, ValueError):
        return default


def _visible_markdown(markdown: str) -> str:
    """Remove parser metadata comments before bibliographic fallbacks."""
    return re.sub(r"<!--.*?-->", "\n", markdown, flags=re.S)


def _title_from_markdown(markdown: str) -> str:
    visible = _visible_markdown(markdown)
    heading = re.search(r"^#\s+(.+?)\s*$", visible, re.MULTILINE)
    if heading:
        return heading.group(1).strip()
    for line in visible.splitlines():
        stripped = line.strip().strip("#").strip()
        if stripped and not stripped.startswith(("$$", "\\[", "\\begin{")):
            return stripped[:160]
    return "未命名数学建模论文"


def _abstract_from_markdown(markdown: str) -> str:
    visible = _visible_markdown(markdown)
    match = re.search(r"(?:^|\n)#{0,4}\s*(?:摘要|Abstract)\s*[:：]?\s*\n?(.{30,1600}?)(?=\n#{1,4}\s|\Z)", visible, re.I | re.S)
    if match:
        return normalize_space(match.group(1))[:1200]
    paragraphs = [normalize_space(part) for part in re.split(r"\n\s*\n", visible) if len(normalize_space(part)) > 60]
    return paragraphs[0][:800] if paragraphs else ""


def _find_reference_quote(markdown: str, names: list[str]) -> tuple[str, int | None, str]:
    lowered = markdown.casefold()
    candidates: list[tuple[float, int, str, int, int]] = []
    for name in sorted(set(names), key=len, reverse=True):
        needle = name.casefold().strip()
        if not needle:
            continue
        cursor = 0
        while True:
            position = lowered.find(needle, cursor)
            if position < 0:
                break
            end_position = position + len(needle)
            line_start = markdown.rfind("\n", 0, position) + 1
            line_end = markdown.find("\n", end_position)
            line_end = len(markdown) if line_end < 0 else line_end
            line = markdown[line_start:line_end].strip()
            quote_start_candidates = [markdown.rfind(mark, 0, position) for mark in ["。", "！", "？", "\n", ". ", "；", ";"]]
            quote_start = max(quote_start_candidates) + 1
            quote_end_candidates: list[int] = []
            for marker in ["。", "！", "？", "\n", ". ", "；", ";"]:
                found = markdown.find(marker, end_position)
                if found >= 0:
                    quote_end_candidates.append(found + len(marker))
            quote_end = min(quote_end_candidates) if quote_end_candidates else min(len(markdown), end_position + 240)
            quote = normalize_space(markdown[quote_start:quote_end])
            is_heading = bool(re.match(r"^#{1,6}\s", line))
            is_comment = line.startswith("<!--")
            context_extra = max(0, len(quote) - len(name))
            verb_bonus = 2.0 if re.search(r"(?:采用|使用|构建|建立|计算|求解|排序|used?|using|apply|rank|calculate)", quote, re.I) else 0.0
            score = (0.0 if is_heading else 4.0) + (0.0 if is_comment else 2.0) + min(2.0, context_extra / 30.0) + verb_bonus
            if len(quote) < max(10, len(name) + 4):
                score -= 3.0
            candidates.append((score, position, quote, quote_start, quote_end))
            cursor = position + max(1, len(needle))
    if not candidates:
        return "", None, ""
    _, position, quote, _, _ = max(candidates, key=lambda item: (item[0], -item[1]))
    section = ""
    for heading in re.finditer(r"^(#{1,6})\s+(.+?)\s*$", markdown, re.MULTILINE):
        if heading.end() <= position:
            section = heading.group(2).strip()
        elif heading.start() > position:
            break
    page = None
    for marker in re.finditer(r"<!--\s*MM_PAGE:\s*(\d+)\s*-->", markdown):
        if marker.end() <= position:
            page = int(marker.group(1))
        elif marker.start() > position:
            break
    return quote, page, section


def _deduplicate_evidence(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    for item in items:
        evidence_id = str(item.get("id") or "")
        if evidence_id and evidence_id not in seen:
            result.append(item)
            seen.add(evidence_id)
    return result


def _location_from_char(markdown: str, char_start: Any) -> tuple[int | None, str]:
    try:
        position = int(char_start)
    except (TypeError, ValueError):
        return None, ""
    if position < 0:
        return None, ""
    page: int | None = None
    for marker in re.finditer(r"<!--\s*MM_PAGE:\s*(\d+)\s*-->", markdown):
        if marker.end() <= position:
            page = int(marker.group(1))
        elif marker.start() > position:
            break
    section = ""
    for heading in re.finditer(r"^(#{1,6})\s+(.+?)\s*$", markdown, re.MULTILINE):
        if heading.end() <= position:
            section = heading.group(2).strip()
        elif heading.start() > position:
            break
    return page, section


def _coerce_structure_location(item: dict[str, Any], markdown: str) -> tuple[int | None, str]:
    raw_page = item.get("page")
    try:
        page = int(raw_page) if raw_page is not None else None
    except (TypeError, ValueError):
        page = None
    section = str(item.get("section") or "")
    fallback_page, fallback_section = _location_from_char(markdown, item.get("char_start"))
    return page or fallback_page, section or fallback_section


def _structure_evidence(structure: dict[str, Any], markdown: str) -> list[dict[str, Any]]:
    evidence: list[dict[str, Any]] = []
    for equation in structure.get("equations", []) or []:
        if not isinstance(equation, dict):
            continue
        latex = normalize_space(str(equation.get("latex") or ""))
        if not latex:
            continue
        page, section = _coerce_structure_location(equation, markdown)
        evidence.append(
            {
                "id": stable_evidence_id("equation", latex, page),
                "kind": "equation",
                "page": page,
                "section": section,
                "label": str(equation.get("label") or equation.get("id") or ""),
                "locator": str(equation.get("id") or f"char:{equation.get('char_start')}-{equation.get('char_end')}"),
                "quote": latex,
                "char_start": equation.get("char_start"),
                "char_end": equation.get("char_end"),
                "content_hash": str(equation.get("content_hash") or sha256_text(latex)),
                "provenance": "PAPER_EXPLICIT",
                "confidence": 0.98,
            }
        )
    for source_key, kind in [("figure_mentions", "figure"), ("table_mentions", "table")]:
        for mention in structure.get(source_key, []) or []:
            if not isinstance(mention, dict):
                continue
            quote = normalize_space(str(mention.get("context") or mention.get("label") or ""))
            if not quote:
                continue
            page, section = _coerce_structure_location(mention, markdown)
            evidence.append(
                {
                    "id": stable_evidence_id(kind, quote, page),
                    "kind": kind,
                    "page": page,
                    "section": section,
                    "label": str(mention.get("label") or mention.get("id") or ""),
                    "locator": str(mention.get("id") or f"char:{mention.get('char_start')}-{mention.get('char_end')}"),
                    "quote": quote,
                    "char_start": mention.get("char_start"),
                    "char_end": mention.get("char_end"),
                    "content_hash": sha256_text(quote),
                    "provenance": "PAPER_EXPLICIT",
                    "confidence": 0.95,
                }
            )
    return _deduplicate_evidence(evidence)


def _heuristic_ir(
    markdown: str,
    structure: dict[str, Any],
    normalized_path: Path,
    catalog: ReferenceCatalog,
) -> dict[str, Any]:
    source_meta = structure.get("source", {})
    title = _title_from_markdown(markdown)
    evidence = _deduplicate_evidence([*heuristic_evidence(markdown), *_structure_evidence(structure, markdown)])
    models: list[dict[str, Any]] = []
    algorithms: list[dict[str, Any]] = []

    for entry in catalog.detect(markdown, "model"):
        quote, page, section = _find_reference_quote(markdown, [entry.canonical_name, *entry.aliases])
        evidence_ids: list[str] = []
        if quote:
            evidence_id = stable_evidence_id("text", quote, page)
            evidence.append(
                {
                    "id": evidence_id,
                    "kind": "text",
                    "page": page,
                    "section": section,
                    "label": "model",
                    "locator": f"page:{page}" if page else "heuristic-name-match",
                    "quote": quote,
                    "char_start": None,
                    "char_end": None,
                    "content_hash": sha256_text(quote),
                    "provenance": "PAPER_EXPLICIT",
                    "confidence": 0.82,
                }
            )
            evidence_ids.append(evidence_id)
        card = catalog.make_model_card(entry, evidence_ids)
        card["provenance"] = "HEURISTIC"
        card["confidence"] = 0.58
        card["role"] = card.get("role") or "论文中检测到该模型名称，具体作用需复核"
        models.append(card)

    for entry in catalog.detect(markdown, "algorithm"):
        quote, page, section = _find_reference_quote(markdown, [entry.canonical_name, *entry.aliases])
        evidence_ids = []
        if quote:
            evidence_id = stable_evidence_id("text", quote, page)
            evidence.append(
                {
                    "id": evidence_id,
                    "kind": "text",
                    "page": page,
                    "section": section,
                    "label": "algorithm",
                    "locator": f"page:{page}" if page else "heuristic-name-match",
                    "quote": quote,
                    "char_start": None,
                    "char_end": None,
                    "content_hash": sha256_text(quote),
                    "provenance": "PAPER_EXPLICIT",
                    "confidence": 0.82,
                }
            )
            evidence_ids.append(evidence_id)
        card = catalog.make_algorithm_card(entry, evidence_ids)
        card["provenance"] = "HEURISTIC"
        card["confidence"] = 0.58
        algorithms.append(card)

    evidence = repair_evidence_anchors(_deduplicate_evidence(evidence), markdown=markdown)
    assumptions = []
    for index, item in enumerate([item for item in evidence if item.get("label") == "assumption"], start=1):
        assumptions.append(
            {
                "id": f"A-{index:03d}",
                "statement": item["quote"],
                "rationale": "由关键词规则抽取，需人工核对假设边界。",
                "impact": "",
                "evidence_ids": [item["id"]],
                "provenance": "HEURISTIC",
            }
        )

    source_hash = str(source_meta.get("sha256") or sha256_file(normalized_path))
    paper_id = slug_id(f"{title}-{source_hash[:16]}", prefix="paper-")
    model_ids = [model["id"] for model in models]
    algorithm_ids = [algorithm["id"] for algorithm in algorithms]
    subproblem = {
        "id": "Q1",
        "statement": "离线启发式模式未可靠拆分子问题，请人工或使用 LLM 补全。",
        "task_types": merge_unique(*(model.get("task_types", []) for model in models)) or ["unknown"],
        "inputs": [],
        "outputs": [],
        "constraints": [],
        "evidence_ids": [],
    }
    modeling_chain = [
        {
            "order": index,
            "subproblem_id": "Q1",
            "model_id": model["id"],
            "algorithm_ids": algorithm_ids,
            "input": "论文数据",
            "output": "模型结果",
            "rationale": "启发式检测到模型名称，建模链需人工核对。",
            "evidence_ids": model.get("evidence_ids", []),
        }
        for index, model in enumerate(models, start=1)
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "paper_id": paper_id,
        "source": {
            "path": str(source_meta.get("path") or normalized_path),
            "sha256": source_hash,
            "parser": str(source_meta.get("parser") or "markdown"),
            "parsed_at": str(source_meta.get("parsed_at") or utc_now_iso()),
            "normalized_markdown": str(normalized_path),
            "structure_json": "",
        },
        "bibliographic": {
            "title": title,
            "authors": [],
            "year": None,
            "competition": "",
            "award": "",
            "problem_id": "",
            "abstract": _abstract_from_markdown(markdown),
            "keywords": merge_unique([model["canonical_name"] for model in models], [algorithm["canonical_name"] for algorithm in algorithms]),
            "language": "zh-CN",
        },
        "problem": {
            "background": normalize_space(markdown)[:800],
            "overall_objective": "启发式模式未可靠抽取总体目标。",
            "subproblems": [subproblem],
        },
        "evidence": evidence,
        "assumptions": assumptions,
        "variables": [],
        "data": {
            "sources": [],
            "fields": [],
            "data_types": [],
            "preprocessing": [],
            "missing_value_strategy": "",
            "outlier_strategy": "",
            "evidence_ids": [],
        },
        "modeling_chain": modeling_chain,
        "models": models,
        "algorithms": algorithms,
        "validation": {
            "methods": [],
            "metrics": [],
            "results": [],
            "sensitivity_analysis": [],
            "robustness_checks": [],
            "evidence_ids": [],
        },
        "limitations": ["当前结果由离线启发式规则生成，不能替代语义分析和人工复核。"],
        "innovations": [],
        "case": {
            "id": slug_id(title, prefix="case-"),
            "title": title,
            "domain": "unknown",
            "competition": "",
            "year": None,
            "award": "",
            "problem_id": "",
            "problem_fingerprint": {
                "problem_types": subproblem["task_types"],
                "data_types": [],
                "targets": [],
                "constraints": [],
                "domain_keywords": [],
            },
            "subproblem_mapping": [
                {
                    "subproblem_id": "Q1",
                    "task": subproblem["statement"],
                    "model_ids": model_ids,
                    "algorithm_ids": algorithm_ids,
                    "data_flow": "",
                    "rationale": "启发式占位映射",
                    "evidence_ids": [],
                }
            ],
            "results": [],
            "transferable_insights": ["使用 LLM 模式或人工补全问题拆分、模型作用和算法参数。"],
            "pitfalls": ["仅根据名称命中可能产生误判。"],
            "innovations": [],
            "evidence_ids": [],
        },
        "code_recipes": [],
        "quality": {
            "evidence_coverage": 0.25 if evidence else 0.0,
            "completeness": 0.25,
            "code_reproducibility": 0.0,
            "warnings": ["LLM disabled: generated a heuristic IR skeleton."],
            "review_required": True,
        },
    }


def _coerce_io_fields(value: Any) -> list[dict[str, Any]]:
    fields: list[dict[str, Any]] = []
    for item in _as_list(value):
        if isinstance(item, dict):
            name = str(item.get("name") or item.get("symbol") or "input")
            fields.append(
                {
                    "name": name,
                    "description": str(item.get("description") or item.get("meaning") or name),
                    "shape": str(item.get("shape") or ""),
                    "unit": str(item.get("unit") or ""),
                    "required": bool(item.get("required", True)),
                }
            )
        elif str(item).strip():
            text = str(item).strip()
            fields.append({"name": text, "description": text, "shape": "", "unit": "", "required": True})
    return fields


def _coerce_parameters(value: Any) -> list[dict[str, Any]]:
    parameters: list[dict[str, Any]] = []
    for item in _as_list(value):
        if not isinstance(item, dict):
            continue
        parameters.append(
            {
                "name": str(item.get("name") or "parameter"),
                "value": item.get("value"),
                "description": str(item.get("description") or ""),
                "range": str(item.get("range") or ""),
                "evidence_ids": _strings(item.get("evidence_ids")),
                "provenance": _provenance(item.get("provenance")),
            }
        )
    return parameters


def _coerce_workflow(value: Any, evidence_ids: list[str]) -> list[dict[str, Any]]:
    workflow: list[dict[str, Any]] = []
    for index, item in enumerate(_as_list(value), start=1):
        if isinstance(item, dict):
            workflow.append(
                {
                    "order": int(item.get("order") or index),
                    "name": str(item.get("name") or item.get("title") or f"步骤 {index}"),
                    "description": str(item.get("description") or item.get("detail") or item.get("name") or ""),
                    "inputs": _strings(item.get("inputs")),
                    "outputs": _strings(item.get("outputs")),
                    "evidence_ids": _strings(item.get("evidence_ids")) or evidence_ids,
                }
            )
        elif str(item).strip():
            text = str(item).strip()
            workflow.append(
                {"order": index, "name": text[:80], "description": text, "inputs": [], "outputs": [], "evidence_ids": evidence_ids}
            )
    if not workflow:
        workflow = [{"order": 1, "name": "论文未给出完整流程", "description": "需要人工补全。", "inputs": [], "outputs": [], "evidence_ids": evidence_ids}]
    return workflow


def _coerce_equations(value: Any) -> list[dict[str, Any]]:
    equations: list[dict[str, Any]] = []
    for item in _as_list(value):
        if isinstance(item, dict):
            latex = str(item.get("latex") or item.get("equation") or "").strip()
            if not latex:
                continue
            equations.append(
                {
                    "label": str(item.get("label") or ""),
                    "latex": latex,
                    "explanation": str(item.get("explanation") or "论文公式，需结合上下文解释。"),
                    "variables": _strings(item.get("variables")),
                    "evidence_ids": _strings(item.get("evidence_ids")),
                    "provenance": _provenance(item.get("provenance"), "PAPER_DERIVED"),
                }
            )
        elif str(item).strip():
            equations.append(
                {
                    "label": "",
                    "latex": str(item).strip(),
                    "explanation": "论文公式，需结合上下文解释。",
                    "variables": [],
                    "evidence_ids": [],
                    "provenance": "PAPER_DERIVED",
                }
            )
    return equations


def _match_evidence_quotes(raw: dict[str, Any], evidence: list[dict[str, Any]]) -> list[str]:
    ids = _strings(raw.get("evidence_ids"))
    if ids:
        valid = {item["id"] for item in evidence}
        return [value for value in ids if value in valid]
    quote_map = {normalize_space(item.get("quote", "")): item["id"] for item in evidence}
    result: list[str] = []
    for quote in _strings(raw.get("evidence_quotes")):
        normalized = normalize_space(quote)
        if normalized in quote_map:
            result.append(quote_map[normalized])
            continue
        best_id = ""
        best_score = 0.0
        for known, evidence_id in quote_map.items():
            if normalized and (normalized in known or known in normalized):
                score = min(len(normalized), len(known)) / max(len(normalized), len(known))
                if score > best_score:
                    best_score, best_id = score, evidence_id
        if best_id:
            result.append(best_id)
    return merge_unique(result)


def _coerce_model(raw: dict[str, Any], evidence: list[dict[str, Any]], index: int) -> dict[str, Any]:
    name = str(raw.get("canonical_name") or raw.get("name") or raw.get("display_name") or f"Model {index}").strip()
    evidence_ids = _match_evidence_quotes(raw, evidence)
    complexity_raw = raw.get("complexity") if isinstance(raw.get("complexity"), dict) else {}
    return {
        "id": str(raw.get("id") or slug_id(name, prefix="model-")),
        "canonical_name": name,
        "display_name": str(raw.get("display_name") or name),
        "aliases": _strings(raw.get("aliases")),
        "category": normalize_category(str(raw.get("category") or "other"), MODEL_CATEGORIES),
        "task_types": _strings(raw.get("task_types")),
        "role": str(raw.get("role") or ""),
        "description": str(raw.get("description") or "论文使用了该模型，但描述需要人工补全。"),
        "assumptions": _strings(raw.get("assumptions")),
        "inputs": _coerce_io_fields(raw.get("inputs")),
        "outputs": _coerce_io_fields(raw.get("outputs")),
        "equations": _coerce_equations(raw.get("equations")),
        "workflow": _coerce_workflow(raw.get("workflow"), evidence_ids),
        "parameters": _coerce_parameters(raw.get("parameters")),
        "solver_algorithm_ids": _strings(raw.get("solver_algorithm_ids")),
        "strengths": _strings(raw.get("strengths")),
        "weaknesses": _strings(raw.get("weaknesses")),
        "use_when": _strings(raw.get("use_when")),
        "avoid_when": _strings(raw.get("avoid_when")),
        "alternatives": _strings(raw.get("alternatives")),
        "combinations": _strings(raw.get("combinations")),
        "complexity": {
            "time": str(complexity_raw.get("time") or "unknown"),
            "space": str(complexity_raw.get("space") or "unknown"),
            "notes": str(complexity_raw.get("notes") or ""),
        },
        "validation_methods": _strings(raw.get("validation_methods")),
        "evidence_ids": evidence_ids,
        "provenance": _provenance(raw.get("provenance"), "PAPER_DERIVED"),
        "confidence": _confidence(raw.get("confidence"), 0.65),
    }


def _coerce_algorithm(raw: dict[str, Any], evidence: list[dict[str, Any]], index: int) -> dict[str, Any]:
    name = str(raw.get("canonical_name") or raw.get("name") or raw.get("display_name") or f"Algorithm {index}").strip()
    evidence_ids = _match_evidence_quotes(raw, evidence)
    complexity_raw = raw.get("complexity") if isinstance(raw.get("complexity"), dict) else {}
    if not complexity_raw:
        complexity_raw = {"time": raw.get("time_complexity"), "space": raw.get("space_complexity")}
    randomness_raw = raw.get("randomness") if isinstance(raw.get("randomness"), dict) else {}
    return {
        "id": str(raw.get("id") or slug_id(name, prefix="algorithm-")),
        "canonical_name": name,
        "display_name": str(raw.get("display_name") or name),
        "aliases": _strings(raw.get("aliases")),
        "category": normalize_category(str(raw.get("category") or "other"), ALGORITHM_CATEGORIES),
        "purpose": str(raw.get("purpose") or "论文使用该算法进行求解。"),
        "inputs": _strings(raw.get("inputs")),
        "outputs": _strings(raw.get("outputs")),
        "pseudocode": _strings(raw.get("pseudocode")) or ["论文未给出可复现伪代码，需人工补全。"],
        "parameters": _coerce_parameters(raw.get("parameters")),
        "initialization": str(raw.get("initialization") or ""),
        "stopping_criteria": _strings(raw.get("stopping_criteria")),
        "complexity": {
            "time": str(complexity_raw.get("time") or "unknown"),
            "space": str(complexity_raw.get("space") or "unknown"),
            "notes": str(complexity_raw.get("notes") or ""),
        },
        "randomness": {
            "uses_randomness": bool(randomness_raw.get("uses_randomness", False)),
            "seed_required": bool(randomness_raw.get("seed_required", False)),
            "notes": str(randomness_raw.get("notes") or ""),
        },
        "implementation_notes": _strings(raw.get("implementation_notes")),
        "failure_modes": _strings(raw.get("failure_modes")),
        "evidence_ids": evidence_ids,
        "provenance": _provenance(raw.get("provenance"), "PAPER_DERIVED"),
        "confidence": _confidence(raw.get("confidence"), 0.65),
    }


def _coerce_assumptions(value: Any, evidence: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for index, item in enumerate(_as_list(value), start=1):
        if isinstance(item, dict):
            evidence_ids = _match_evidence_quotes(item, evidence)
            result.append(
                {
                    "id": str(item.get("id") or f"A-{index:03d}"),
                    "statement": str(item.get("statement") or item.get("assumption") or ""),
                    "rationale": str(item.get("rationale") or "论文未详细说明。"),
                    "impact": str(item.get("impact") or ""),
                    "evidence_ids": evidence_ids,
                    "provenance": _provenance(item.get("provenance"), "PAPER_EXPLICIT"),
                }
            )
        elif str(item).strip():
            result.append(
                {"id": f"A-{index:03d}", "statement": str(item), "rationale": "", "impact": "", "evidence_ids": [], "provenance": "AI_INFERRED"}
            )
    return [item for item in result if item["statement"]]


def _coerce_variables(value: Any, evidence: list[dict[str, Any]]) -> list[dict[str, Any]]:
    allowed = {"scalar", "vector", "matrix", "tensor", "set", "categorical", "unknown"}
    result: list[dict[str, Any]] = []
    for item in _as_list(value):
        if not isinstance(item, dict):
            continue
        data_type = str(item.get("data_type") or "unknown").lower()
        result.append(
            {
                "symbol": str(item.get("symbol") or item.get("name") or "?"),
                "meaning": str(item.get("meaning") or item.get("description") or ""),
                "unit": str(item.get("unit") or ""),
                "domain": str(item.get("domain") or ""),
                "data_type": data_type if data_type in allowed else "unknown",
                "evidence_ids": _match_evidence_quotes(item, evidence),
                "provenance": _provenance(item.get("provenance"), "PAPER_EXPLICIT"),
            }
        )
    return result


def _coerce_subproblems(value: Any) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for index, item in enumerate(_as_list(value), start=1):
        if isinstance(item, dict):
            result.append(
                {
                    "id": str(item.get("id") or f"Q{index}"),
                    "statement": str(item.get("statement") or item.get("task") or f"子问题 {index}"),
                    "task_types": _strings(item.get("task_types")) or ["unknown"],
                    "inputs": _strings(item.get("inputs")),
                    "outputs": _strings(item.get("outputs")),
                    "constraints": _strings(item.get("constraints")),
                    "evidence_ids": _strings(item.get("evidence_ids")),
                }
            )
        elif str(item).strip():
            result.append({"id": f"Q{index}", "statement": str(item), "task_types": ["unknown"], "inputs": [], "outputs": [], "constraints": [], "evidence_ids": []})
    return result or [{"id": "Q1", "statement": "论文问题需进一步拆分。", "task_types": ["unknown"], "inputs": [], "outputs": [], "constraints": [], "evidence_ids": []}]


def _coerce_synthesis(
    raw: dict[str, Any],
    *,
    evidence: list[dict[str, Any]],
    structure: dict[str, Any],
    normalized_path: Path,
    markdown: str,
    fallback_candidates: dict[str, list[dict[str, Any]]],
    provider_name: str,
) -> dict[str, Any]:
    source_meta = structure.get("source", {})
    bibliographic_raw = raw.get("bibliographic") if isinstance(raw.get("bibliographic"), dict) else {}
    title = str(bibliographic_raw.get("title") or _title_from_markdown(markdown))
    year_raw = bibliographic_raw.get("year")
    try:
        year = int(year_raw) if year_raw not in (None, "") else None
    except (TypeError, ValueError):
        year = None
    source_hash = str(source_meta.get("sha256") or sha256_file(normalized_path))
    paper_id = slug_id(f"{title}-{source_hash[:16]}", prefix="paper-")

    model_raw = _as_list(raw.get("models")) or fallback_candidates.get("models", [])
    algorithm_raw = _as_list(raw.get("algorithms")) or fallback_candidates.get("algorithms", [])
    models = [_coerce_model(item, evidence, index) for index, item in enumerate(model_raw, start=1) if isinstance(item, dict)]
    algorithms = [_coerce_algorithm(item, evidence, index) for index, item in enumerate(algorithm_raw, start=1) if isinstance(item, dict)]

    problem_raw = raw.get("problem") if isinstance(raw.get("problem"), dict) else {}
    subproblems = _coerce_subproblems(problem_raw.get("subproblems"))
    valid_model_ids = {model["id"] for model in models}
    valid_algorithm_ids = {algorithm["id"] for algorithm in algorithms}

    modeling_chain: list[dict[str, Any]] = []
    for index, item in enumerate(_as_list(raw.get("modeling_chain")), start=1):
        if not isinstance(item, dict):
            continue
        model_id = str(item.get("model_id") or "")
        if model_id not in valid_model_ids and models:
            name_match = next((model["id"] for model in models if model["canonical_name"] == model_id), models[0]["id"])
            model_id = name_match
        modeling_chain.append(
            {
                "order": int(item.get("order") or index),
                "subproblem_id": str(item.get("subproblem_id") or subproblems[0]["id"]),
                "model_id": model_id,
                "algorithm_ids": [value for value in _strings(item.get("algorithm_ids")) if value in valid_algorithm_ids],
                "input": str(item.get("input") or ""),
                "output": str(item.get("output") or ""),
                "rationale": str(item.get("rationale") or ""),
                "evidence_ids": [value for value in _strings(item.get("evidence_ids")) if value in {e["id"] for e in evidence}],
            }
        )
    if not modeling_chain:
        modeling_chain = [
            {
                "order": index,
                "subproblem_id": subproblems[min(index - 1, len(subproblems) - 1)]["id"],
                "model_id": model["id"],
                "algorithm_ids": model.get("solver_algorithm_ids", []),
                "input": "",
                "output": "",
                "rationale": model.get("role", ""),
                "evidence_ids": model.get("evidence_ids", []),
            }
            for index, model in enumerate(models, start=1)
        ]

    data_raw = raw.get("data") if isinstance(raw.get("data"), dict) else {}
    validation_raw = raw.get("validation") if isinstance(raw.get("validation"), dict) else {}
    case_raw = raw.get("case") if isinstance(raw.get("case"), dict) else {}
    fingerprint_raw = case_raw.get("problem_fingerprint") if isinstance(case_raw.get("problem_fingerprint"), dict) else {}
    mapping_raw = _as_list(case_raw.get("subproblem_mapping"))
    mappings: list[dict[str, Any]] = []
    for index, item in enumerate(mapping_raw, start=1):
        if not isinstance(item, dict):
            continue
        mappings.append(
            {
                "subproblem_id": str(item.get("subproblem_id") or subproblems[min(index - 1, len(subproblems) - 1)]["id"]),
                "task": str(item.get("task") or subproblems[min(index - 1, len(subproblems) - 1)]["statement"]),
                "model_ids": [value for value in _strings(item.get("model_ids")) if value in valid_model_ids],
                "algorithm_ids": [value for value in _strings(item.get("algorithm_ids")) if value in valid_algorithm_ids],
                "data_flow": str(item.get("data_flow") or ""),
                "rationale": str(item.get("rationale") or ""),
                "evidence_ids": [value for value in _strings(item.get("evidence_ids")) if value in {e["id"] for e in evidence}],
            }
        )
    if not mappings:
        mappings = [
            {
                "subproblem_id": item["id"],
                "task": item["statement"],
                "model_ids": [step["model_id"] for step in modeling_chain if step["subproblem_id"] == item["id"]],
                "algorithm_ids": merge_unique(*(step["algorithm_ids"] for step in modeling_chain if step["subproblem_id"] == item["id"])),
                "data_flow": "",
                "rationale": "由建模链自动生成。",
                "evidence_ids": merge_unique(*(step["evidence_ids"] for step in modeling_chain if step["subproblem_id"] == item["id"])),
            }
            for item in subproblems
        ]

    quality_raw = raw.get("quality") if isinstance(raw.get("quality"), dict) else {}
    referenced_ids = set()
    for collection in [models, algorithms]:
        for item in collection:
            referenced_ids.update(item.get("evidence_ids", []))
    evidence_coverage = len(referenced_ids) / len(evidence) if evidence else 0.0
    completeness = min(1.0, 0.15 + 0.15 * bool(models) + 0.15 * bool(algorithms) + 0.15 * bool(subproblems) + 0.1 * bool(raw.get("assumptions")) + 0.1 * bool(raw.get("variables")) + 0.1 * bool(validation_raw) + 0.1 * bool(mappings))
    warnings = _strings(quality_raw.get("warnings"))
    if not evidence:
        warnings.append("No evidence anchors were extracted.")
    if any(item.get("provenance") == "AI_INFERRED" for item in [*models, *algorithms]):
        warnings.append("Some model/algorithm fields are AI_INFERRED and require review.")

    return {
        "schema_version": SCHEMA_VERSION,
        "paper_id": paper_id,
        "source": {
            "path": str(source_meta.get("path") or normalized_path),
            "sha256": source_hash,
            "parser": str(source_meta.get("parser") or "markdown"),
            "parsed_at": str(source_meta.get("parsed_at") or utc_now_iso()),
            "normalized_markdown": str(normalized_path),
            "structure_json": "",
        },
        "bibliographic": {
            "title": title,
            "authors": _strings(bibliographic_raw.get("authors")),
            "year": year,
            "competition": str(bibliographic_raw.get("competition") or ""),
            "award": str(bibliographic_raw.get("award") or ""),
            "problem_id": str(bibliographic_raw.get("problem_id") or ""),
            "abstract": str(bibliographic_raw.get("abstract") or _abstract_from_markdown(markdown)),
            "keywords": _strings(bibliographic_raw.get("keywords")),
            "language": str(bibliographic_raw.get("language") or "zh-CN"),
        },
        "problem": {
            "background": str(problem_raw.get("background") or normalize_space(markdown)[:800]),
            "overall_objective": str(problem_raw.get("overall_objective") or ""),
            "subproblems": subproblems,
        },
        "evidence": evidence,
        "assumptions": _coerce_assumptions(raw.get("assumptions"), evidence),
        "variables": _coerce_variables(raw.get("variables"), evidence),
        "data": {
            "sources": _strings(data_raw.get("sources")),
            "fields": _strings(data_raw.get("fields")),
            "data_types": _strings(data_raw.get("data_types")),
            "preprocessing": _strings(data_raw.get("preprocessing")),
            "missing_value_strategy": str(data_raw.get("missing_value_strategy") or ""),
            "outlier_strategy": str(data_raw.get("outlier_strategy") or ""),
            "evidence_ids": _strings(data_raw.get("evidence_ids")),
        },
        "modeling_chain": modeling_chain,
        "models": models,
        "algorithms": algorithms,
        "validation": {
            "methods": _strings(validation_raw.get("methods")),
            "metrics": _strings(validation_raw.get("metrics")),
            "results": _strings(validation_raw.get("results")),
            "sensitivity_analysis": _strings(validation_raw.get("sensitivity_analysis")),
            "robustness_checks": _strings(validation_raw.get("robustness_checks")),
            "evidence_ids": _strings(validation_raw.get("evidence_ids")),
        },
        "limitations": _strings(raw.get("limitations")),
        "innovations": _strings(raw.get("innovations")),
        "case": {
            "id": str(case_raw.get("id") or slug_id(title, prefix="case-")),
            "title": str(case_raw.get("title") or title),
            "domain": str(case_raw.get("domain") or "unknown"),
            "competition": str(case_raw.get("competition") or bibliographic_raw.get("competition") or ""),
            "year": year,
            "award": str(case_raw.get("award") or bibliographic_raw.get("award") or ""),
            "problem_id": str(case_raw.get("problem_id") or bibliographic_raw.get("problem_id") or ""),
            "problem_fingerprint": {
                "problem_types": _strings(fingerprint_raw.get("problem_types")) or merge_unique(*(item["task_types"] for item in subproblems)),
                "data_types": _strings(fingerprint_raw.get("data_types")) or _strings(data_raw.get("data_types")),
                "targets": _strings(fingerprint_raw.get("targets")),
                "constraints": _strings(fingerprint_raw.get("constraints")),
                "domain_keywords": _strings(fingerprint_raw.get("domain_keywords")),
            },
            "subproblem_mapping": mappings,
            "results": _strings(case_raw.get("results")),
            "transferable_insights": _strings(case_raw.get("transferable_insights")) or ["结合相似赛题时需重新检查数据、约束和评价指标。"],
            "pitfalls": _strings(case_raw.get("pitfalls")),
            "innovations": _strings(case_raw.get("innovations")),
            "evidence_ids": _strings(case_raw.get("evidence_ids")),
        },
        "code_recipes": [],
        "quality": {
            "evidence_coverage": _confidence(quality_raw.get("evidence_coverage"), evidence_coverage),
            "completeness": _confidence(quality_raw.get("completeness"), completeness),
            "code_reproducibility": 0.0,
            "warnings": merge_unique(warnings),
            "review_required": bool(quality_raw.get("review_required", True)),
        },
        "_generation": {"provider": provider_name},
    }


def _strip_internal_fields(ir: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in ir.items() if not key.startswith("_")}


def build_paper_ir(
    normalized_path: Path,
    *,
    structure_path: Path | None = None,
    page_map_path: Path | None = None,
    output_dir: Path | None = None,
    llm: BaseLLM | None = None,
    catalog: ReferenceCatalog | None = None,
    chunk_chars: int = 16000,
) -> tuple[dict[str, Any], dict[str, Any]]:
    normalized_path = normalized_path.expanduser().resolve()
    markdown = normalized_path.read_text(encoding="utf-8", errors="replace")
    structure = read_json(structure_path) if structure_path and structure_path.exists() else {
        "source": {
            "path": str(normalized_path),
            "sha256": sha256_file(normalized_path),
            "parser": "markdown",
            "parsed_at": utc_now_iso(),
        }
    }
    catalog = catalog or ReferenceCatalog()
    diagnostics: dict[str, Any] = {"chunks": [], "provider": llm.provider if llm else "none", "warnings": []}

    if llm is None:
        ir = _heuristic_ir(markdown, structure, normalized_path, catalog)
    else:
        chunks = chunk_markdown(markdown, max_chars=chunk_chars)
        bundles: list[dict[str, Any]] = []
        fallback_models: list[dict[str, Any]] = []
        fallback_algorithms: list[dict[str, Any]] = []
        raw_evidence: list[dict[str, Any]] = _structure_evidence(structure, markdown)
        for chunk in chunks:
            user = json.dumps(
                {
                    "chunk": {
                        "chunk_id": chunk.chunk_id,
                        "section_hint": chunk.section,
                        "page_hint": chunk.page_hint,
                        "char_start": chunk.char_start,
                        "char_end": chunk.char_end,
                        "text": chunk.text,
                    }
                },
                ensure_ascii=False,
            )
            try:
                response = llm.generate_json(system=EVIDENCE_SYSTEM, user=user, purpose="evidence", max_tokens=7000)
                bundle = response.data
                bundle["chunk_id"] = chunk.chunk_id
            except Exception as exc:
                LOGGER.warning("Evidence extraction failed for %s: %s", chunk.chunk_id, exc)
                bundle = {
                    "chunk_id": chunk.chunk_id,
                    "evidence": heuristic_evidence(chunk.text),
                    "candidate_models": [],
                    "candidate_algorithms": [],
                    "assumptions": [],
                    "variables": [],
                    "validation_clues": [],
                    "warnings": [f"LLM extraction failed: {exc}"],
                }
                diagnostics["warnings"].append(f"{chunk.chunk_id}: {exc}")
            bundles.append(bundle)
            raw_evidence.extend(item for item in _as_list(bundle.get("evidence")) if isinstance(item, dict))
            fallback_models.extend(item for item in _as_list(bundle.get("candidate_models")) if isinstance(item, dict))
            fallback_algorithms.extend(item for item in _as_list(bundle.get("candidate_algorithms")) if isinstance(item, dict))
            diagnostics["chunks"].append({"chunk_id": chunk.chunk_id, "evidence_count": len(_as_list(bundle.get("evidence"))), "warning_count": len(_as_list(bundle.get("warnings")))})

        evidence = repair_evidence_anchors(_deduplicate_evidence(raw_evidence), page_map_path=page_map_path, markdown=markdown)
        diagnostics["structural_evidence_count"] = len(_structure_evidence(structure, markdown))
        compact_bundles = []
        for bundle in bundles:
            compact_bundles.append(
                {
                    "chunk_id": bundle.get("chunk_id"),
                    "candidate_models": bundle.get("candidate_models", []),
                    "candidate_algorithms": bundle.get("candidate_algorithms", []),
                    "assumptions": bundle.get("assumptions", []),
                    "variables": bundle.get("variables", []),
                    "validation_clues": bundle.get("validation_clues", []),
                }
            )
        synthesis_payload = {
            "document_hint": {
                "title_guess": _title_from_markdown(markdown),
                "opening_text": markdown[:8000],
                "source": structure.get("source", {}),
            },
            "evidence": evidence,
            "chunk_findings": compact_bundles,
        }
        try:
            synthesis = llm.generate_json(
                system=SYNTHESIS_SYSTEM,
                user=json.dumps(synthesis_payload, ensure_ascii=False),
                purpose="synthesis",
                max_tokens=llm.max_tokens if hasattr(llm, "max_tokens") else None,
            ).data
        except Exception as exc:
            LOGGER.warning("Synthesis failed; falling back to heuristic IR: %s", exc)
            diagnostics["warnings"].append(f"Synthesis failed: {exc}")
            ir = _heuristic_ir(markdown, structure, normalized_path, catalog)
            ir["evidence"] = merge_unique(ir["evidence"], evidence)
        else:
            ir = _coerce_synthesis(
                synthesis,
                evidence=evidence,
                structure=structure,
                normalized_path=normalized_path,
                markdown=markdown,
                fallback_candidates={"models": fallback_models, "algorithms": fallback_algorithms},
                provider_name=f"{llm.provider}:{llm.model}",
            )

        if output_dir:
            output_dir.mkdir(parents=True, exist_ok=True)
            write_json(output_dir / "evidence_chunks.json", {"chunks": bundles, "diagnostics": diagnostics})

    ir["source"]["normalized_markdown"] = str(normalized_path)
    ir["source"]["structure_json"] = str(structure_path.resolve()) if structure_path else ""
    ir = _strip_internal_fields(ir)
    errors = SchemaStore().errors("paper", ir)
    if errors:
        ir["quality"]["warnings"] = merge_unique(ir["quality"].get("warnings", []), [f"Schema check: {message}" for message in errors[:20]])
        diagnostics["schema_errors"] = errors
        # A schema-invalid IR is not silently accepted: persist diagnostics and raise through validate below.
    SchemaStore().validate("paper", ir)
    if output_dir:
        write_json(output_dir / "paper_ir.raw.json", ir)
        write_json(output_dir / "build_ir_report.json", diagnostics)
    return ir, diagnostics
