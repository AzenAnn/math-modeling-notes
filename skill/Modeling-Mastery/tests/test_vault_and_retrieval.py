from __future__ import annotations

import copy
import json
from pathlib import Path

from modeling_mastery.constants import AUTO_END
from modeling_mastery.dedup import scan_duplicates
from modeling_mastery.indexer import build_index
from modeling_mastery.retriever import search_index
from modeling_mastery.vault import write_obsidian_vault


def test_vault_write_is_idempotent_and_preserves_manual_content(tmp_path: Path, demo_ir: dict, project_root: Path) -> None:
    vault = tmp_path / "vault"
    first = write_obsidian_vault(demo_ir, vault, project_root=project_root)
    topsis_note = vault / "10_Models" / "evaluation" / "TOPSIS.md"
    assert topsis_note.exists()
    content = topsis_note.read_text(encoding="utf-8")
    assert AUTO_END in content
    content = content.replace(
        "在这里补充你自己的理解、比赛经验、参数选择与踩坑记录。",
        "我的人工经验：先检查成本型指标正向化。",
    )
    topsis_note.write_text(content, encoding="utf-8")

    second = write_obsidian_vault(demo_ir, vault, project_root=project_root)
    rewritten = topsis_note.read_text(encoding="utf-8")
    assert "我的人工经验：先检查成本型指标正向化。" in rewritten
    assert rewritten.count(AUTO_END) == 1
    assert len(first["created_or_updated"]) == len(second["created_or_updated"])

    registry = json.loads((vault / ".modeling-mastery" / "registry.json").read_text(encoding="utf-8"))
    assert len(registry["models"]) == 2
    assert len(registry["algorithms"]) == 1


def test_index_and_problem_retrieval(tmp_path: Path, demo_ir: dict, project_root: Path) -> None:
    vault = tmp_path / "vault"
    write_obsidian_vault(demo_ir, vault, project_root=project_root)
    ignored_template = vault / ".venv" / "Lib" / "template.md"
    ignored_template.parent.mkdir(parents=True)
    ignored_template.write_text("---\n{{ card_data }}\n---\n# dependency template\n", encoding="utf-8")
    user_template = vault / "templates" / "card.md"
    user_template.parent.mkdir(parents=True)
    user_template.write_text("---\n{{ card_data }}\n---\n# user template\n", encoding="utf-8")
    index_report = build_index(vault)
    assert index_report["note_count"] >= 6
    index_payload = json.loads((vault / ".modeling-mastery" / "index.json").read_text(encoding="utf-8"))
    indexed_paths = {item["path"] for item in index_payload["notes"]}
    assert ".venv/Lib/template.md" not in indexed_paths
    assert "templates/card.md" in indexed_paths
    results = search_index(vault, "多指标综合评价，需要客观赋权并对方案排序", note_type="model", top_k=5)
    titles = {item["title"] for item in results}
    assert "TOPSIS" in titles
    assert "Entropy Weight Method" in titles
    assert any(item["reasons"] for item in results)

    dedup = scan_duplicates(vault)
    assert dedup["exact_duplicate_groups"] == []


def test_nested_vault_assets_link_from_parent_obsidian_root(
    tmp_path: Path,
    demo_ir: dict,
    project_root: Path,
) -> None:
    ir = copy.deepcopy(demo_ir)
    parsed = tmp_path / "parsed"
    figures = parsed / "figures"
    figures.mkdir(parents=True)
    (parsed / "paper_structure.json").write_text("{}\n", encoding="utf-8")
    (figures / "figure-1.png").write_bytes(b"not-a-real-png")
    (figures / "manifest.json").write_text(
        json.dumps({"figures": [{"path": "figure-1.png", "id": "FIG-1", "page": 1}]}),
        encoding="utf-8",
    )
    ir["source"]["structure_json"] = str(parsed / "paper_structure.json")

    obsidian_root = tmp_path / "library"
    vault = obsidian_root / "论文" / "示例论文" / "知识库"
    write_obsidian_vault(
        ir,
        vault,
        project_root=project_root,
        obsidian_root=obsidian_root,
    )

    paper_note = vault / "50_Papers" / f"{ir['bibliographic']['title']}.md"
    content = paper_note.read_text(encoding="utf-8")
    expected = f"![[论文/示例论文/知识库/_assets/{ir['paper_id']}/figures/figure-1.png]]"
    assert expected in content
