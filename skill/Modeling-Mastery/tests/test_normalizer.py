from __future__ import annotations

import copy

from modeling_mastery.normalizer import ReferenceCatalog, normalize_ir
from modeling_mastery.schema_utils import SchemaStore


def test_aliases_merge_into_canonical_model(demo_ir: dict, project_root) -> None:
    ir = copy.deepcopy(demo_ir)
    topsis = next(item for item in ir["models"] if item["canonical_name"] == "TOPSIS")
    duplicate = copy.deepcopy(topsis)
    duplicate["id"] = "model-alias"
    duplicate["canonical_name"] = "优劣解距离法"
    duplicate["display_name"] = "优劣解距离法"
    duplicate["strengths"] = ["别名来源补充"]
    ir["models"].append(duplicate)
    ir["modeling_chain"].append(
        {
            "order": len(ir["modeling_chain"]) + 1,
            "subproblem_id": "Q1",
            "model_id": "model-alias",
            "algorithm_ids": [],
            "input": "matrix",
            "output": "ranking",
            "rationale": "alias test",
            "evidence_ids": duplicate["evidence_ids"],
        }
    )

    normalized, report = normalize_ir(ir, ReferenceCatalog(project_root / "references"))
    SchemaStore(project_root / "schemas").validate("paper", normalized)
    assert [item["canonical_name"] for item in normalized["models"]].count("TOPSIS") == 1
    merged = next(item for item in normalized["models"] if item["canonical_name"] == "TOPSIS")
    assert "别名来源补充" in merged["strengths"]
    assert any(item["kind"] == "model" and item["name"] == "TOPSIS" for item in report["merged"])
    assert normalized["modeling_chain"][-1]["model_id"] == merged["id"]
