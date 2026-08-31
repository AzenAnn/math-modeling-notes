from __future__ import annotations

from modeling_mastery.render import render_template


def test_model_io_items_render_on_separate_lines(demo_ir: dict, project_root) -> None:
    model = next(item for item in demo_ir["models"] if item["canonical_name"] == "TOPSIS")
    rendered = render_template(
        "model.md",
        {"model": model, "sources": [], "evidence": []},
        project_root / "templates",
    )
    assert "shape=`n×m`\n- **weights**" in rendered
    assert "shape=`n`\n- **ranking**" in rendered


def test_model_combinations_link_only_known_model_cards(demo_ir: dict, project_root) -> None:
    model = dict(next(item for item in demo_ir["models"] if item["canonical_name"] == "TOPSIS"))
    model["combinations"] = ["Entropy Weight Method", "先正向化再评价"]
    rendered = render_template(
        "model.md",
        {
            "model": model,
            "sources": [],
            "evidence": [],
            "known_model_names": {"TOPSIS", "Entropy Weight Method"},
        },
        project_root / "templates",
    )
    assert "- [[Entropy Weight Method]]" in rendered
    assert "- 先正向化再评价" in rendered
    assert "[[先正向化再评价]]" not in rendered


def test_case_model_and_algorithm_lines_do_not_merge(demo_ir: dict, project_root) -> None:
    rendered = render_template(
        "case.md",
        {
            "case": demo_ir["case"],
            "paper_note": demo_ir["bibliographic"]["title"],
        },
        project_root / "templates",
    )
    assert "\n- 算法：" in rendered
    assert "\n- 数据流：" in rendered
