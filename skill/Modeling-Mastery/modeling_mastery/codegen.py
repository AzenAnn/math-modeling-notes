from __future__ import annotations

import copy
import json
import logging
import re
from pathlib import Path
from typing import Any

from .code_validation import validate_matlab_source, validate_python_source
from .io_utils import merge_unique, safe_filename, slug_id, utc_now_iso, write_json
from .llm import BaseLLM
from .prompts import CODEGEN_SYSTEM
from .runner import run_octave_check, run_python_tests
from .schema_utils import SchemaStore

LOGGER = logging.getLogger(__name__)


def _strip_code_fence(value: str) -> str:
    value = value.strip()
    match = re.fullmatch(r"```(?:python|matlab|octave|py|m)?\s*(.*?)\s*```", value, re.S | re.I)
    return match.group(1).strip() + "\n" if match else value.rstrip() + "\n"


def _target_context(ir: dict[str, Any], target: dict[str, Any], target_type: str) -> dict[str, Any]:
    evidence_map = {item["id"]: item for item in ir.get("evidence", [])}
    evidence = [evidence_map[value] for value in target.get("evidence_ids", []) if value in evidence_map]
    if target_type == "model":
        algorithm_ids = target.get("solver_algorithm_ids", [])
        related_algorithms = [item for item in ir.get("algorithms", []) if item.get("id") in algorithm_ids]
    else:
        related_algorithms = []
    return {
        "paper": {
            "paper_id": ir.get("paper_id"),
            "title": ir.get("bibliographic", {}).get("title"),
        },
        "target_type": target_type,
        "target": target,
        "related_algorithms": related_algorithms,
        "evidence": evidence,
        "required_provenance_comment": [item["id"] for item in evidence],
    }


def reproduce_code(
    ir: dict[str, Any],
    output_dir: Path,
    *,
    llm: BaseLLM | None,
    max_targets: int = 8,
    timeout: int = 30,
    memory_mb: int = 2048,
    run_tests: bool = True,
    check_octave: bool = False,
) -> tuple[dict[str, Any], dict[str, Any]]:
    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    updated = copy.deepcopy(ir)
    report: dict[str, Any] = {"targets": [], "warnings": []}
    if llm is None:
        report["warnings"].append("No LLM provider configured; code reproduction skipped.")
        return updated, report

    targets: list[tuple[str, dict[str, Any]]] = [
        *(('model', item) for item in updated.get("models", [])),
        *(('algorithm', item) for item in updated.get("algorithms", [])),
    ][:max_targets]
    recipes: list[dict[str, Any]] = []
    for target_type, target in targets:
        target_name = str(target.get("canonical_name") or target.get("display_name") or "target")
        target_id = str(target.get("id") or slug_id(target_name, prefix=f"{target_type}-"))
        directory_name = safe_filename(target_name, fallback=target_id, max_length=70)
        recipe_dir = output_dir / directory_name
        python_dir = recipe_dir / "python"
        matlab_dir = recipe_dir / "matlab"
        tests_dir = recipe_dir / "tests"
        for directory in [python_dir, matlab_dir, tests_dir]:
            directory.mkdir(parents=True, exist_ok=True)

        context = _target_context(updated, target, target_type)
        try:
            response = llm.generate_json(
                system=CODEGEN_SYSTEM,
                user=json.dumps(context, ensure_ascii=False),
                purpose="code",
                max_tokens=12000,
            ).data
        except Exception as exc:
            LOGGER.warning("Code reproduction failed for %s: %s", target_name, exc)
            report["targets"].append({"target_id": target_id, "target_name": target_name, "status": "generation_failed", "error": str(exc)})
            continue

        python_code = _strip_code_fence(str(response.get("python_code") or ""))
        matlab_code = _strip_code_fence(str(response.get("matlab_code") or ""))
        pytest_code = _strip_code_fence(str(response.get("pytest_code") or ""))
        metadata = response.get("metadata") if isinstance(response.get("metadata"), dict) else {}
        python_file = python_dir / "implementation.py"
        matlab_file = matlab_dir / "implementation.m"
        test_file = tests_dir / "test_implementation.py"
        python_file.write_text(python_code, encoding="utf-8")
        matlab_file.write_text(matlab_code, encoding="utf-8")
        test_file.write_text(pytest_code, encoding="utf-8")

        python_validation = validate_python_source(python_code)
        test_validation = validate_python_source(pytest_code)
        matlab_validation = validate_matlab_source(matlab_code)
        static_passed = python_validation.safe and test_validation.safe and matlab_validation.safe
        test_result = None
        if run_tests and python_validation.safe and test_validation.safe:
            test_result = run_python_tests(recipe_dir, timeout=timeout, memory_mb=memory_mb)
        octave_result = run_octave_check(matlab_file, timeout=timeout, memory_mb=memory_mb) if check_octave and matlab_validation.safe else None
        tests_passed = bool(test_result and test_result.passed)
        validation_status = "tests_passed" if tests_passed else ("static_passed" if static_passed else "failed")

        evidence_ids = target.get("evidence_ids", [])
        anchors = [
            {
                "evidence_id": evidence_id,
                "relationship": f"Supports {target_type} reproduction",
                "provenance": target.get("provenance", "PAPER_DERIVED"),
            }
            for evidence_id in evidence_ids
        ]
        if not anchors:
            anchors = [{"evidence_id": "UNRESOLVED", "relationship": "No paper evidence anchor available", "provenance": "AI_INFERRED"}]

        python_recipe = {
            "id": slug_id(f"{target_id}-python", prefix="code-"),
            "target_id": target_id,
            "target_name": target_name,
            "target_type": target_type,
            "language": "python",
            "variant": "paper_reproduction",
            "path": str(python_file),
            "entrypoint": str(metadata.get("entrypoint") or (python_validation.functions[0] if python_validation.functions else "solve")),
            "dependencies": [str(value) for value in metadata.get("dependencies", [])],
            "input_contract": [str(value) for value in metadata.get("input_contract", [])],
            "output_contract": [str(value) for value in metadata.get("output_contract", [])],
            "source_anchors": anchors,
            "assumptions": [str(value) for value in metadata.get("assumptions", [])],
            "tests": [
                {"name": "static safety", "kind": "syntax", "status": "passed" if python_validation.safe else "failed", "details": "; ".join(python_validation.errors + python_validation.warnings)},
                {"name": "pytest", "kind": "unit", "status": "passed" if tests_passed else ("skipped" if not test_result or test_result.skipped else "failed"), "details": "" if not test_result else (test_result.stdout + "\n" + test_result.stderr)[-4000:]},
            ],
            "validation_status": validation_status,
            "limitations": [str(value) for value in metadata.get("limitations", [])],
            "generated_by": f"{llm.provider}:{llm.model}",
            "created_at": utc_now_iso(),
        }
        matlab_recipe = {
            "id": slug_id(f"{target_id}-matlab", prefix="code-"),
            "target_id": target_id,
            "target_name": target_name,
            "target_type": target_type,
            "language": "matlab",
            "variant": "paper_reproduction",
            "path": str(matlab_file),
            "entrypoint": str(metadata.get("entrypoint") or (matlab_validation.functions[0] if matlab_validation.functions else "solve")),
            "dependencies": [],
            "input_contract": [str(value) for value in metadata.get("input_contract", [])],
            "output_contract": [str(value) for value in metadata.get("output_contract", [])],
            "source_anchors": anchors,
            "assumptions": [str(value) for value in metadata.get("assumptions", [])],
            "tests": [
                {"name": "static safety", "kind": "syntax", "status": "passed" if matlab_validation.safe else "failed", "details": "; ".join(matlab_validation.errors + matlab_validation.warnings)},
                {"name": "Octave load", "kind": "smoke", "status": "passed" if octave_result and octave_result.passed else ("skipped" if not octave_result or octave_result.skipped else "failed"), "details": "" if not octave_result else (octave_result.stdout + "\n" + octave_result.stderr)[-4000:]},
            ],
            "validation_status": "static_passed" if matlab_validation.safe else "failed",
            "limitations": merge_unique([str(value) for value in metadata.get("limitations", [])], [] if octave_result and octave_result.passed else ["MATLAB/Octave runtime behavior was not fully verified."]),
            "generated_by": f"{llm.provider}:{llm.model}",
            "created_at": utc_now_iso(),
        }
        SchemaStore().validate("code", python_recipe)
        SchemaStore().validate("code", matlab_recipe)
        recipes.extend([python_recipe, matlab_recipe])
        validation_payload = {
            "target_id": target_id,
            "python": python_validation.as_dict(),
            "python_tests": test_result.as_dict() if test_result else None,
            "matlab": matlab_validation.as_dict(),
            "octave": octave_result.as_dict() if octave_result else None,
            "validation_status": validation_status,
        }
        write_json(recipe_dir / "validation.json", validation_payload)
        write_json(recipe_dir / "code.json", {"python": python_recipe, "matlab": matlab_recipe})
        (recipe_dir / "README.md").write_text(
            f"# {target_name} 代码复现\n\n"
            f"- Target: `{target_id}`\n"
            f"- Python status: `{python_recipe['validation_status']}`\n"
            f"- MATLAB status: `{matlab_recipe['validation_status']}`\n"
            f"- 证据：{', '.join(evidence_ids) if evidence_ids else 'UNRESOLVED'}\n\n"
            "运行前请阅读 `validation.json`，并在隔离环境中复核 AI_INFERRED 参数。\n",
            encoding="utf-8",
        )
        report["targets"].append({"target_id": target_id, "target_name": target_name, "status": validation_status, "directory": str(recipe_dir)})

    updated["code_recipes"] = merge_unique(updated.get("code_recipes", []), recipes)
    passed_count = sum(1 for recipe in recipes if recipe.get("validation_status") in {"static_passed", "tests_passed"})
    updated["quality"]["code_reproducibility"] = passed_count / len(recipes) if recipes else 0.0
    updated["quality"]["review_required"] = True
    return updated, report
