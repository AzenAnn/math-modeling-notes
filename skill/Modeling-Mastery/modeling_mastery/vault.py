from __future__ import annotations

import copy
import logging
import shutil
from pathlib import Path
from typing import Any

from .constants import (
    AUTO_BEGIN,
    AUTO_END,
    INDEX_DB_FILE,
    INDEX_JSON_FILE,
    MANUAL_HEADING,
    REGISTRY_DIR,
    REGISTRY_FILE,
    VAULT_FOLDERS,
)
from .frontmatter import dump_frontmatter, split_frontmatter
from .io_utils import (
    atomic_write_text,
    merge_unique,
    read_json,
    relative_posix,
    safe_filename,
    utc_now_iso,
    write_json,
)
from .render import render_template
from .schema_utils import SchemaStore

LOGGER = logging.getLogger(__name__)

GENERATED_FRONTMATTER_KEYS = {
    "type", "id", "paper_id", "title", "canonical_name", "aliases", "category", "tasks",
    "authors", "year", "competition", "award", "problem_id", "source_papers", "models",
    "algorithms", "tags", "provenance", "confidence", "language", "target_id", "target_type",
    "entrypoint", "validation_status", "generated_at", "updated_at",
}


def _merge_cards(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    if not left:
        return copy.deepcopy(right)
    result = copy.deepcopy(left)
    for key, value in right.items():
        if isinstance(value, list):
            result[key] = merge_unique(result.get(key, []), value)
        elif isinstance(value, dict):
            result[key] = _merge_cards(result.get(key, {}) if isinstance(result.get(key), dict) else {}, value)
        elif key == "confidence":
            result[key] = max(float(result.get(key, 0.0)), float(value or 0.0))
        elif value not in (None, "", [], {}):
            result[key] = value
    return result


def _default_registry() -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "papers": {},
        "models": {},
        "algorithms": {},
        "cases": {},
        "codes": {},
        "updated_at": utc_now_iso(),
    }


def _load_registry(vault_path: Path) -> dict[str, Any]:
    path = vault_path / REGISTRY_DIR / REGISTRY_FILE
    if not path.exists():
        return _default_registry()
    try:
        data = read_json(path)
        return data if isinstance(data, dict) else _default_registry()
    except Exception as exc:
        LOGGER.warning("Registry could not be read; a new one will be created: %s", exc)
        return _default_registry()


def _manual_tail(existing_body: str) -> str:
    if AUTO_END in existing_body:
        tail = existing_body.split(AUTO_END, 1)[1].strip()
        if tail:
            return tail
    elif existing_body.strip():
        return f"{MANUAL_HEADING}\n\n> [!warning] 导入前已有内容\n\n{existing_body.strip()}\n"
    return f"{MANUAL_HEADING}\n\n在这里补充你自己的理解、比赛经验、参数选择与踩坑记录。\n"


def _write_generated_note(path: Path, frontmatter: dict[str, Any], generated_body: str) -> None:
    existing_frontmatter: dict[str, Any] = {}
    existing_body = ""
    if path.exists():
        existing_frontmatter, existing_body = split_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
    preserved = {key: value for key, value in existing_frontmatter.items() if key not in GENERATED_FRONTMATTER_KEYS}
    merged_frontmatter = {**preserved, **frontmatter}
    manual = _manual_tail(existing_body)
    content = (
        dump_frontmatter(merged_frontmatter)
        + "\n"
        + AUTO_BEGIN
        + "\n"
        + generated_body.strip()
        + "\n"
        + AUTO_END
        + "\n\n"
        + manual.strip()
        + "\n"
    )
    atomic_write_text(path, content)


def _evidence_context(ir: dict[str, Any], ids: list[str]) -> list[dict[str, Any]]:
    lookup = {item["id"]: item for item in ir.get("evidence", [])}
    return [lookup[value] for value in ids if value in lookup]


def _obsidian_link_path(target: Path, vault_path: Path, obsidian_root: Path | None) -> str:
    base = obsidian_root or vault_path
    try:
        return target.resolve().relative_to(base.resolve()).as_posix()
    except ValueError as exc:
        raise ValueError(f"Vault path must be inside the Obsidian root: {vault_path} not in {base}") from exc


def _copy_figures(
    ir: dict[str, Any],
    vault_path: Path,
    obsidian_root: Path | None = None,
) -> list[dict[str, Any]]:
    structure_raw = ir.get("source", {}).get("structure_json", "")
    if not structure_raw:
        return []
    structure_path = Path(structure_raw)
    source_figures = structure_path.parent / "figures"
    if not source_figures.exists():
        return []
    target_dir = vault_path / VAULT_FOLDERS["assets"] / ir["paper_id"] / "figures"
    target_dir.mkdir(parents=True, exist_ok=True)
    copied: list[dict[str, Any]] = []
    manifest_path = source_figures / "manifest.json"
    manifest = read_json(manifest_path).get("figures", []) if manifest_path.exists() else []
    for source in source_figures.iterdir():
        if not source.is_file() or source.name == "manifest.json":
            continue
        target = target_dir / source.name
        shutil.copy2(source, target)
        metadata = next((item for item in manifest if item.get("path") == source.name), {})
        copied.append(
            {
                **metadata,
                "path": relative_posix(target, vault_path),
                "embed": f"![[{_obsidian_link_path(target, vault_path, obsidian_root)}]]",
            }
        )
    return copied


def _copy_code_asset(
    recipe: dict[str, Any],
    ir: dict[str, Any],
    vault_path: Path,
    obsidian_root: Path | None = None,
) -> tuple[str, str]:
    source_raw = recipe.get("path", "")
    source = Path(source_raw) if source_raw else None
    if not source or not source.exists():
        return "", ""
    target_dir = vault_path / VAULT_FOLDERS["assets"] / ir["paper_id"] / "code" / safe_filename(recipe["target_name"])
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / source.name
    shutil.copy2(source, target)
    return _obsidian_link_path(target, vault_path, obsidian_root), source.read_text(encoding="utf-8", errors="replace")


def initialize_vault(vault_path: Path) -> None:
    vault_path.mkdir(parents=True, exist_ok=True)
    for folder in VAULT_FOLDERS.values():
        (vault_path / folder).mkdir(parents=True, exist_ok=True)
    (vault_path / REGISTRY_DIR).mkdir(parents=True, exist_ok=True)


def write_obsidian_vault(
    ir: dict[str, Any],
    vault_path: Path,
    *,
    project_root: Path | None = None,
    obsidian_root: Path | None = None,
) -> dict[str, Any]:
    SchemaStore().validate("paper", ir)
    vault_path = vault_path.expanduser().resolve()
    obsidian_root = obsidian_root.expanduser().resolve() if obsidian_root else None
    if obsidian_root:
        _obsidian_link_path(vault_path, vault_path, obsidian_root)
    initialize_vault(vault_path)
    registry = _load_registry(vault_path)
    report: dict[str, Any] = {
        "vault": str(vault_path),
        "obsidian_root": str(obsidian_root or vault_path),
        "created_or_updated": [],
        "warnings": [],
    }
    paper = ir["bibliographic"]
    paper_title = paper["title"]
    paper_source = {"paper_id": ir["paper_id"], "title": paper_title, "evidence_ids": []}
    figures = _copy_figures(ir, vault_path, obsidian_root)

    registry["papers"][ir["paper_id"]] = {"ir": ir, "updated_at": utc_now_iso()}
    model_entries: list[dict[str, Any]] = []
    for model in ir.get("models", []):
        current = registry["models"].get(model["id"], {"card": {}, "sources": []})
        current["card"] = _merge_cards(current.get("card", {}), model)
        current["sources"] = merge_unique(current.get("sources", []), [{**paper_source, "evidence_ids": model.get("evidence_ids", [])}])
        registry["models"][model["id"]] = current
        model_entries.append(current)

    algorithm_entries: list[dict[str, Any]] = []
    for algorithm in ir.get("algorithms", []):
        current = registry["algorithms"].get(algorithm["id"], {"card": {}, "sources": []})
        current["card"] = _merge_cards(current.get("card", {}), algorithm)
        current["sources"] = merge_unique(current.get("sources", []), [{**paper_source, "evidence_ids": algorithm.get("evidence_ids", [])}])
        registry["algorithms"][algorithm["id"]] = current
        algorithm_entries.append(current)

    registry["cases"][ir["case"]["id"]] = {"card": ir["case"], "paper_id": ir["paper_id"], "updated_at": utc_now_iso()}

    paper_name = safe_filename(paper_title)
    paper_path = vault_path / VAULT_FOLDERS["papers"] / f"{paper_name}.md"
    paper_frontmatter = {
        "type": "paper",
        "id": ir["paper_id"],
        "paper_id": ir["paper_id"],
        "title": paper_title,
        "authors": paper.get("authors", []),
        "year": paper.get("year"),
        "competition": paper.get("competition", ""),
        "award": paper.get("award", ""),
        "problem_id": paper.get("problem_id", ""),
        "models": [model["canonical_name"] for model in ir.get("models", [])],
        "algorithms": [algorithm["canonical_name"] for algorithm in ir.get("algorithms", [])],
        "tags": merge_unique(["mm/paper"], [f"mm/competition/{paper.get('competition')}" ] if paper.get("competition") else []),
        "updated_at": utc_now_iso(),
    }
    paper_body = render_template(
        "paper.md",
        {
            "ir": ir,
            "paper": paper,
            "models": ir.get("models", []),
            "algorithms": ir.get("algorithms", []),
            "figures": figures,
            "evidence": ir.get("evidence", []),
        },
        project_root / "templates" if project_root else None,
    )
    _write_generated_note(paper_path, paper_frontmatter, paper_body)
    report["created_or_updated"].append(relative_posix(paper_path, vault_path))

    case = ir["case"]
    case_path = vault_path / VAULT_FOLDERS["cases"] / f"{safe_filename(case['title'])}-案例.md"
    case_frontmatter = {
        "type": "case",
        "id": case["id"],
        "title": case["title"],
        "paper_id": ir["paper_id"],
        "competition": case.get("competition", ""),
        "year": case.get("year"),
        "problem_id": case.get("problem_id", ""),
        "models": [model["canonical_name"] for model in ir.get("models", [])],
        "algorithms": [algorithm["canonical_name"] for algorithm in ir.get("algorithms", [])],
        "tags": ["mm/case", f"mm/domain/{safe_filename(case.get('domain', 'unknown')).replace(' ', '-')}"],
        "updated_at": utc_now_iso(),
    }
    _write_generated_note(
        case_path,
        case_frontmatter,
        render_template("case.md", {"case": case, "ir": ir, "paper_note": paper_name}, project_root / "templates" if project_root else None),
    )
    report["created_or_updated"].append(relative_posix(case_path, vault_path))

    for entry in model_entries:
        model = entry["card"]
        category = safe_filename(model.get("category", "other"))
        model_path = vault_path / VAULT_FOLDERS["models"] / category / f"{safe_filename(model['canonical_name'])}.md"
        model_frontmatter = {
            "type": "model",
            "id": model["id"],
            "canonical_name": model["canonical_name"],
            "aliases": model.get("aliases", []),
            "category": model.get("category", "other"),
            "tasks": model.get("task_types", []),
            "source_papers": [source["title"] for source in entry.get("sources", [])],
            "provenance": model.get("provenance"),
            "confidence": model.get("confidence"),
            "tags": ["mm/model", f"mm/model/{model.get('category', 'other')}", *[f"mm/task/{task}" for task in model.get("task_types", [])]],
            "updated_at": utc_now_iso(),
        }
        model_body = render_template(
            "model.md",
            {
                "model": model,
                "sources": entry.get("sources", []),
                "evidence": _evidence_context(ir, model.get("evidence_ids", [])),
                "known_model_names": {item["card"]["canonical_name"] for item in model_entries},
            },
            project_root / "templates" if project_root else None,
        )
        _write_generated_note(model_path, model_frontmatter, model_body)
        report["created_or_updated"].append(relative_posix(model_path, vault_path))

    for entry in algorithm_entries:
        algorithm = entry["card"]
        category = safe_filename(algorithm.get("category", "other"))
        algorithm_path = vault_path / VAULT_FOLDERS["algorithms"] / category / f"{safe_filename(algorithm['canonical_name'])}.md"
        algorithm_frontmatter = {
            "type": "algorithm",
            "id": algorithm["id"],
            "canonical_name": algorithm["canonical_name"],
            "aliases": algorithm.get("aliases", []),
            "category": algorithm.get("category", "other"),
            "source_papers": [source["title"] for source in entry.get("sources", [])],
            "provenance": algorithm.get("provenance"),
            "confidence": algorithm.get("confidence"),
            "tags": ["mm/algorithm", f"mm/algorithm/{algorithm.get('category', 'other')}"],
            "updated_at": utc_now_iso(),
        }
        algorithm_body = render_template(
            "algorithm.md",
            {
                "algorithm": algorithm,
                "sources": entry.get("sources", []),
                "evidence": _evidence_context(ir, algorithm.get("evidence_ids", [])),
            },
            project_root / "templates" if project_root else None,
        )
        _write_generated_note(algorithm_path, algorithm_frontmatter, algorithm_body)
        report["created_or_updated"].append(relative_posix(algorithm_path, vault_path))

    for recipe in ir.get("code_recipes", []):
        code_path, source_code = _copy_code_asset(recipe, ir, vault_path, obsidian_root)
        recipe_copy = copy.deepcopy(recipe)
        recipe_copy["vault_code_path"] = code_path
        registry["codes"][recipe["id"]] = {"card": recipe_copy, "paper_id": ir["paper_id"], "updated_at": utc_now_iso()}
        language = safe_filename(recipe.get("language", "unknown"))
        note_name = f"{safe_filename(recipe['target_name'])}-{language}"
        note_path = vault_path / VAULT_FOLDERS["code"] / language / f"{note_name}.md"
        code_frontmatter = {
            "type": "code",
            "id": recipe["id"],
            "target_id": recipe["target_id"],
            "target_type": recipe.get("target_type"),
            "title": note_name,
            "language": recipe["language"],
            "entrypoint": recipe["entrypoint"],
            "validation_status": recipe["validation_status"],
            "paper_id": ir["paper_id"],
            "tags": ["mm/code", f"mm/code/{language}"],
            "updated_at": utc_now_iso(),
        }
        code_body = render_template(
            "code.md",
            {"recipe": recipe_copy, "source_code": source_code, "ir": ir},
            project_root / "templates" if project_root else None,
        )
        _write_generated_note(note_path, code_frontmatter, code_body)
        report["created_or_updated"].append(relative_posix(note_path, vault_path))

    registry["updated_at"] = utc_now_iso()
    write_json(vault_path / REGISTRY_DIR / REGISTRY_FILE, registry)
    home_path = vault_path / VAULT_FOLDERS["home"] / "Modeling-Mastery 首页.md"
    home_frontmatter = {"type": "moc", "title": "Modeling-Mastery 首页", "tags": ["mm/moc"], "updated_at": utc_now_iso()}
    home_body = render_template(
        "home.md",
        {
            "registry": registry,
            "index_json": f"{REGISTRY_DIR}/{INDEX_JSON_FILE}",
            "index_db": f"{REGISTRY_DIR}/{INDEX_DB_FILE}",
        },
        project_root / "templates" if project_root else None,
    )
    _write_generated_note(home_path, home_frontmatter, home_body)
    report["created_or_updated"].append(relative_posix(home_path, vault_path))
    write_json(vault_path / REGISTRY_DIR / "last_write_report.json", report)
    return report
