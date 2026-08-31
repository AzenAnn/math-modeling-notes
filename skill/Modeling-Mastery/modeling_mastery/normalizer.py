from __future__ import annotations

import copy
import logging
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from .io_utils import asset_dir, canonical_key, merge_unique, read_yaml, slug_id

LOGGER = logging.getLogger(__name__)

MODEL_CATEGORIES = {
    "evaluation", "optimization", "prediction", "statistics", "graph", "simulation",
    "mechanism", "clustering", "machine_learning", "game_theory", "data_processing", "other",
}
ALGORITHM_CATEGORIES = {
    "optimization", "graph", "numerical", "statistics", "machine_learning", "simulation",
    "search", "data_processing", "other",
}

CATEGORY_ALIASES = {
    "评价": "evaluation",
    "综合评价": "evaluation",
    "优化": "optimization",
    "预测": "prediction",
    "统计": "statistics",
    "图论": "graph",
    "网络": "graph",
    "仿真": "simulation",
    "模拟": "simulation",
    "机理": "mechanism",
    "聚类": "clustering",
    "机器学习": "machine_learning",
    "博弈": "game_theory",
    "数据处理": "data_processing",
    "数值": "numerical",
    "搜索": "search",
}


@dataclass(slots=True)
class ReferenceEntry:
    kind: str
    canonical_name: str
    aliases: list[str]
    data: dict[str, Any]
    path: Path


class ReferenceCatalog:
    def __init__(self, references_dir: Path | None = None):
        self.references_dir = references_dir or asset_dir("references")
        self.entries: list[ReferenceEntry] = []
        self._by_key: dict[tuple[str, str], ReferenceEntry] = {}
        self._load()

    def _load(self) -> None:
        for path in sorted(self.references_dir.rglob("*.yaml")):
            raw = read_yaml(path)
            items = raw if isinstance(raw, list) else [raw]
            for item in items:
                if not isinstance(item, dict) or not item.get("canonical_name"):
                    continue
                kind = str(item.get("kind", "model"))
                entry = ReferenceEntry(
                    kind=kind,
                    canonical_name=str(item["canonical_name"]),
                    aliases=[str(value) for value in item.get("aliases", [])],
                    data=item,
                    path=path,
                )
                self.entries.append(entry)
                for name in [entry.canonical_name, *entry.aliases]:
                    key = canonical_key(name)
                    if key:
                        self._by_key[(kind, key)] = entry

    def match(self, name: str, kind: str, *, fuzzy_threshold: float = 0.90) -> ReferenceEntry | None:
        key = canonical_key(name)
        if not key:
            return None
        exact = self._by_key.get((kind, key))
        if exact:
            return exact
        best: tuple[float, ReferenceEntry] | None = None
        for (entry_kind, candidate_key), entry in self._by_key.items():
            if entry_kind != kind:
                continue
            score = SequenceMatcher(None, key, candidate_key).ratio()
            if best is None or score > best[0]:
                best = (score, entry)
        return best[1] if best and best[0] >= fuzzy_threshold else None

    def detect(self, text: str, kind: str) -> list[ReferenceEntry]:
        lowered = text.casefold()
        detected: list[ReferenceEntry] = []
        seen: set[str] = set()
        for entry in self.entries:
            if entry.kind != kind:
                continue
            names = sorted([entry.canonical_name, *entry.aliases], key=len, reverse=True)
            found = False
            for name in names:
                normalized = name.casefold().strip()
                if len(canonical_key(normalized)) < 2:
                    continue
                if re.search(r"[a-z0-9]", normalized):
                    pattern = r"(?<![a-z0-9])" + re.escape(normalized) + r"(?![a-z0-9])"
                    found = bool(re.search(pattern, lowered, re.I))
                else:
                    found = normalized in lowered
                if found:
                    break
            key = canonical_key(entry.canonical_name)
            if found and key not in seen:
                detected.append(entry)
                seen.add(key)
        return detected

    def make_model_card(self, entry: ReferenceEntry, evidence_ids: list[str] | None = None) -> dict[str, Any]:
        data = entry.data
        workflow = data.get("workflow") or [
            {"order": 1, "name": "按参考资料配置模型", "description": "论文中的具体过程需人工核对。", "inputs": [], "outputs": [], "evidence_ids": evidence_ids or []}
        ]
        if workflow and isinstance(workflow[0], str):
            workflow = [
                {"order": index, "name": value, "description": value, "inputs": [], "outputs": [], "evidence_ids": evidence_ids or []}
                for index, value in enumerate(workflow, start=1)
            ]
        return {
            "id": slug_id(entry.canonical_name, prefix="model-"),
            "canonical_name": entry.canonical_name,
            "display_name": data.get("display_name", entry.canonical_name),
            "aliases": entry.aliases,
            "category": normalize_category(str(data.get("category", "other")), MODEL_CATEGORIES),
            "task_types": list(data.get("task_types", [])),
            "role": str(data.get("role", "")),
            "description": str(data.get("description", "由参考目录识别，需结合论文证据复核。")),
            "assumptions": list(data.get("assumptions", [])),
            "inputs": list(data.get("inputs", [])),
            "outputs": list(data.get("outputs", [])),
            "equations": list(data.get("equations", [])),
            "workflow": workflow,
            "parameters": list(data.get("parameters", [])),
            "solver_algorithm_ids": list(data.get("solver_algorithm_ids", [])),
            "strengths": list(data.get("strengths", [])),
            "weaknesses": list(data.get("weaknesses", [])),
            "use_when": list(data.get("use_when", [])),
            "avoid_when": list(data.get("avoid_when", [])),
            "alternatives": list(data.get("alternatives", [])),
            "combinations": list(data.get("combinations", [])),
            "complexity": data.get("complexity", {"time": "unknown", "space": "unknown", "notes": ""}),
            "validation_methods": list(data.get("validation_methods", [])),
            "evidence_ids": evidence_ids or [],
            "provenance": "EXTERNAL_REFERENCE",
            "confidence": 0.45,
        }

    def make_algorithm_card(self, entry: ReferenceEntry, evidence_ids: list[str] | None = None) -> dict[str, Any]:
        data = entry.data
        return {
            "id": slug_id(entry.canonical_name, prefix="algorithm-"),
            "canonical_name": entry.canonical_name,
            "display_name": data.get("display_name", entry.canonical_name),
            "aliases": entry.aliases,
            "category": normalize_category(str(data.get("category", "other")), ALGORITHM_CATEGORIES),
            "purpose": str(data.get("purpose", "由参考目录识别，需结合论文证据复核。")),
            "inputs": list(data.get("inputs", [])),
            "outputs": list(data.get("outputs", [])),
            "pseudocode": list(data.get("pseudocode", ["核对论文中的具体实现步骤"])),
            "parameters": list(data.get("parameters", [])),
            "initialization": str(data.get("initialization", "")),
            "stopping_criteria": list(data.get("stopping_criteria", [])),
            "complexity": data.get("complexity", {"time": "unknown", "space": "unknown", "notes": ""}),
            "randomness": data.get("randomness", {"uses_randomness": False, "seed_required": False, "notes": ""}),
            "implementation_notes": list(data.get("implementation_notes", [])),
            "failure_modes": list(data.get("failure_modes", [])),
            "evidence_ids": evidence_ids or [],
            "provenance": "EXTERNAL_REFERENCE",
            "confidence": 0.45,
        }


def normalize_category(value: str, allowed: set[str]) -> str:
    raw = value.strip().lower().replace("-", "_").replace(" ", "_")
    if raw in allowed:
        return raw
    for alias, canonical in CATEGORY_ALIASES.items():
        if alias in value and canonical in allowed:
            return canonical
    return "other"


def _merge_dict_cards(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(left)
    list_fields = {
        "aliases", "task_types", "assumptions", "inputs", "outputs", "equations", "workflow",
        "parameters", "solver_algorithm_ids", "strengths", "weaknesses", "use_when", "avoid_when",
        "alternatives", "combinations", "validation_methods", "evidence_ids", "pseudocode",
        "stopping_criteria", "implementation_notes", "failure_modes",
    }
    for key, value in right.items():
        if key in list_fields:
            result[key] = merge_unique(result.get(key, []), value or [])
        elif not result.get(key) and value not in (None, "", [], {}):
            result[key] = copy.deepcopy(value)
        elif key == "confidence":
            result[key] = max(float(result.get(key, 0)), float(value or 0))
    return result


def normalize_ir(ir: dict[str, Any], catalog: ReferenceCatalog | None = None) -> tuple[dict[str, Any], dict[str, Any]]:
    catalog = catalog or ReferenceCatalog()
    result = copy.deepcopy(ir)
    report: dict[str, Any] = {"models": [], "algorithms": [], "merged": []}
    model_id_map: dict[str, str] = {}
    normalized_models: dict[str, dict[str, Any]] = {}
    for model in result.get("models", []):
        original_name = str(model.get("canonical_name") or model.get("display_name") or "Unnamed Model")
        entry = catalog.match(original_name, "model")
        canonical = entry.canonical_name if entry else original_name.strip()
        model["canonical_name"] = canonical
        model["display_name"] = model.get("display_name") or canonical
        model["aliases"] = merge_unique(model.get("aliases", []), entry.aliases if entry else [], [original_name] if original_name != canonical else [])
        model["category"] = normalize_category(str(model.get("category", entry.data.get("category", "other") if entry else "other")), MODEL_CATEGORIES)
        old_id = str(model.get("id") or slug_id(original_name, prefix="model-"))
        new_id = slug_id(canonical, prefix="model-")
        model["id"] = new_id
        model_id_map[old_id] = new_id
        key = canonical_key(canonical)
        if key in normalized_models:
            normalized_models[key] = _merge_dict_cards(normalized_models[key], model)
            report["merged"].append({"kind": "model", "name": canonical})
        else:
            normalized_models[key] = model
        report["models"].append({"from": original_name, "to": canonical, "id": new_id, "matched_reference": bool(entry)})
    result["models"] = list(normalized_models.values())

    algorithm_id_map: dict[str, str] = {}
    normalized_algorithms: dict[str, dict[str, Any]] = {}
    for algorithm in result.get("algorithms", []):
        original_name = str(algorithm.get("canonical_name") or algorithm.get("display_name") or "Unnamed Algorithm")
        entry = catalog.match(original_name, "algorithm")
        canonical = entry.canonical_name if entry else original_name.strip()
        algorithm["canonical_name"] = canonical
        algorithm["display_name"] = algorithm.get("display_name") or canonical
        algorithm["aliases"] = merge_unique(algorithm.get("aliases", []), entry.aliases if entry else [], [original_name] if original_name != canonical else [])
        algorithm["category"] = normalize_category(str(algorithm.get("category", entry.data.get("category", "other") if entry else "other")), ALGORITHM_CATEGORIES)
        old_id = str(algorithm.get("id") or slug_id(original_name, prefix="algorithm-"))
        new_id = slug_id(canonical, prefix="algorithm-")
        algorithm["id"] = new_id
        algorithm_id_map[old_id] = new_id
        key = canonical_key(canonical)
        if key in normalized_algorithms:
            normalized_algorithms[key] = _merge_dict_cards(normalized_algorithms[key], algorithm)
            report["merged"].append({"kind": "algorithm", "name": canonical})
        else:
            normalized_algorithms[key] = algorithm
        report["algorithms"].append({"from": original_name, "to": canonical, "id": new_id, "matched_reference": bool(entry)})
    result["algorithms"] = list(normalized_algorithms.values())

    for model in result.get("models", []):
        model["solver_algorithm_ids"] = [algorithm_id_map.get(value, value) for value in model.get("solver_algorithm_ids", [])]
    for step in result.get("modeling_chain", []):
        step["model_id"] = model_id_map.get(str(step.get("model_id", "")), str(step.get("model_id", "")))
        step["algorithm_ids"] = [algorithm_id_map.get(value, value) for value in step.get("algorithm_ids", [])]
    case = result.get("case", {})
    for mapping in case.get("subproblem_mapping", []):
        mapping["model_ids"] = [model_id_map.get(value, value) for value in mapping.get("model_ids", [])]
        mapping["algorithm_ids"] = [algorithm_id_map.get(value, value) for value in mapping.get("algorithm_ids", [])]
    for recipe in result.get("code_recipes", []):
        target = str(recipe.get("target_id", ""))
        recipe["target_id"] = model_id_map.get(target, algorithm_id_map.get(target, target))
    return result, report
