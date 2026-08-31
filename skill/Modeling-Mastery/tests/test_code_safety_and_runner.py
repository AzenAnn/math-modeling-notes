from __future__ import annotations

import shutil
from pathlib import Path

from modeling_mastery.code_validation import validate_matlab_source, validate_python_source
from modeling_mastery.runner import run_python_tests


def test_python_static_validation_accepts_numeric_function() -> None:
    source = """# Source evidence: E-001\nimport math\n\ndef solve(x: float) -> float:\n    return math.sqrt(x)\n"""
    report = validate_python_source(source)
    assert report.safe
    assert report.syntax_ok
    assert report.functions == ["solve"]
    assert report.source_anchor_count == 1


def test_python_static_validation_blocks_system_access() -> None:
    source = "import os\n\ndef solve():\n    return os.system('echo unsafe')\n"
    report = validate_python_source(source)
    assert not report.safe
    assert any("Forbidden import" in error for error in report.errors)
    assert any(".system()" in error for error in report.errors)


def test_matlab_static_validation_blocks_shell() -> None:
    report = validate_matlab_source("function y=f(x)\ny=x;\nsystem('whoami');\nend\n")
    assert not report.safe
    assert any("system command" in error for error in report.errors)


def test_demo_python_recipe_runs(tmp_path: Path, project_root: Path) -> None:
    source = project_root / "examples" / "demo_code" / "topsis"
    recipe = tmp_path / "recipe"
    shutil.copytree(source, recipe)
    result = run_python_tests(recipe, timeout=30, memory_mb=2048)
    assert result.passed, result.stdout + result.stderr
