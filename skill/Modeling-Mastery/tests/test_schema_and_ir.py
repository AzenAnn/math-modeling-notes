from __future__ import annotations

from pathlib import Path

from modeling_mastery.document import parse_document
from modeling_mastery.ir_builder import build_paper_ir
from modeling_mastery.normalizer import ReferenceCatalog
from modeling_mastery.schema_utils import SchemaStore


def test_demo_ir_validates(demo_ir: dict) -> None:
    SchemaStore().validate("paper", demo_ir)


def test_reference_cards_validate(project_root: Path) -> None:
    catalog = ReferenceCatalog(project_root / "references")
    store = SchemaStore(project_root / "schemas")
    assert len(catalog.entries) >= 10
    for entry in catalog.entries:
        if entry.kind == "model":
            store.validate("model", catalog.make_model_card(entry))
        elif entry.kind == "algorithm":
            store.validate("algorithm", catalog.make_algorithm_card(entry))


def test_heuristic_ir_detects_models_and_algorithm(tmp_path: Path, demo_markdown: str, project_root: Path) -> None:
    source = tmp_path / "paper.md"
    source.write_text(demo_markdown, encoding="utf-8")
    parsed = parse_document(source, tmp_path / "parsed", backend="markdown")
    ir, report = build_paper_ir(
        parsed.normalized_markdown,
        structure_path=parsed.structure_json,
        page_map_path=parsed.page_map_json,
        output_dir=tmp_path / "ir",
        llm=None,
        catalog=ReferenceCatalog(project_root / "references"),
    )
    SchemaStore(project_root / "schemas").validate("paper", ir)
    model_names = {item["canonical_name"] for item in ir["models"]}
    algorithm_names = {item["canonical_name"] for item in ir["algorithms"]}
    assert {"Entropy Weight Method", "TOPSIS"} <= model_names
    assert "Dijkstra Algorithm" in algorithm_names
    assert len(ir["evidence"]) >= 3
    assert report["provider"] == "none"


def test_structural_equation_evidence_keeps_page_and_section(
    tmp_path: Path, project_root: Path
) -> None:
    source = tmp_path / "paper.md"
    source.write_text(
        "<!-- MM_PAGE: 1 -->\n# Demo\nIntro.\n"
        "<!-- MM_PAGE: 2 -->\n## TOPSIS 模型\n"
        "使用 TOPSIS，并计算相对贴近度。\n"
        "$$C_i=\\frac{D_i^-}{D_i^+ + D_i^-}.$$\n",
        encoding="utf-8",
    )
    parsed = parse_document(source, tmp_path / "parsed", backend="markdown")
    ir, _ = build_paper_ir(
        parsed.normalized_markdown,
        structure_path=parsed.structure_json,
        page_map_path=parsed.page_map_json,
        output_dir=tmp_path / "ir",
        llm=None,
        catalog=ReferenceCatalog(project_root / "references"),
    )
    equations = [item for item in ir["evidence"] if item["kind"] == "equation"]
    assert len(equations) == 1
    assert equations[0]["page"] == 2
    assert equations[0]["section"] == "TOPSIS 模型"
    assert equations[0]["locator"] == "EQ-001"
