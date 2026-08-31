from __future__ import annotations

from pathlib import Path

from modeling_mastery.codegen import reproduce_code
from modeling_mastery.llm import MockLLM
from modeling_mastery.schema_utils import SchemaStore


def test_mock_code_reproduction_produces_valid_recipes(tmp_path: Path, demo_ir: dict, project_root: Path) -> None:
    updated, report = reproduce_code(
        demo_ir,
        tmp_path / "code",
        llm=MockLLM(),
        max_targets=1,
        timeout=30,
        memory_mb=1024,
        run_tests=True,
        check_octave=False,
    )
    SchemaStore(project_root / "schemas").validate("paper", updated)
    assert len(updated["code_recipes"]) == 2
    python_recipe = next(item for item in updated["code_recipes"] if item["language"] == "python")
    assert python_recipe["validation_status"] == "tests_passed"
    assert Path(python_recipe["path"]).exists()
    assert report["targets"][0]["status"] == "tests_passed"
