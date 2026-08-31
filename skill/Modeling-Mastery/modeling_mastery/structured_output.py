from __future__ import annotations

import copy
from typing import Any

from jsonschema import Draft202012Validator

from .errors import LLMResponseError

PROVENANCE_VALUES = [
    "PAPER_EXPLICIT",
    "PAPER_DERIVED",
    "AI_INFERRED",
    "EXTERNAL_REFERENCE",
    "HEURISTIC",
]

JSON_VALUE_SCHEMA: dict[str, Any] = {
    "type": ["string", "number", "integer", "boolean", "object", "array", "null"]
}

PARAMETER_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "value": JSON_VALUE_SCHEMA,
        "unit": {"type": "string"},
        "description": {"type": "string"},
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
    },
    "required": ["name", "value", "provenance"],
    "additionalProperties": True,
}

EVIDENCE_ITEM_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "kind": {
            "type": "string",
            "enum": ["text", "section", "equation", "figure", "table", "code", "metadata"],
        },
        "page": {"type": ["integer", "null"]},
        "section": {"type": "string"},
        "label": {"type": "string"},
        "locator": {"type": "string"},
        "quote": {"type": "string"},
        "char_start": {"type": ["integer", "null"]},
        "char_end": {"type": ["integer", "null"]},
        "content_hash": {"type": "string"},
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
    },
    "required": [
        "id",
        "kind",
        "page",
        "section",
        "label",
        "locator",
        "quote",
        "char_start",
        "char_end",
        "content_hash",
        "provenance",
        "confidence",
    ],
    "additionalProperties": False,
}

CANDIDATE_MODEL_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "category": {"type": "string"},
        "role": {"type": "string"},
        "description": {"type": "string"},
        "equations": {"type": "array", "items": {"type": "string"}},
        "workflow": {"type": "array", "items": {"type": "string"}},
        "parameters": {"type": "array", "items": PARAMETER_SCHEMA},
        "evidence_quotes": {"type": "array", "items": {"type": "string"}},
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
    },
    "required": [
        "name",
        "category",
        "role",
        "description",
        "equations",
        "workflow",
        "parameters",
        "evidence_quotes",
    ],
    "additionalProperties": True,
}

CANDIDATE_ALGORITHM_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "category": {"type": "string"},
        "purpose": {"type": "string"},
        "pseudocode": {"type": "array", "items": {"type": "string"}},
        "parameters": {"type": "array", "items": PARAMETER_SCHEMA},
        "time_complexity": {"type": "string"},
        "space_complexity": {"type": "string"},
        "evidence_quotes": {"type": "array", "items": {"type": "string"}},
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
    },
    "required": [
        "name",
        "category",
        "purpose",
        "pseudocode",
        "parameters",
        "time_complexity",
        "space_complexity",
        "evidence_quotes",
    ],
    "additionalProperties": True,
}

EVIDENCE_OUTPUT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "chunk_id": {"type": "string"},
        "evidence": {"type": "array", "items": EVIDENCE_ITEM_SCHEMA},
        "candidate_models": {"type": "array", "items": CANDIDATE_MODEL_SCHEMA},
        "candidate_algorithms": {"type": "array", "items": CANDIDATE_ALGORITHM_SCHEMA},
        "assumptions": {"type": "array", "items": {"type": "object", "additionalProperties": True}},
        "variables": {"type": "array", "items": {"type": "object", "additionalProperties": True}},
        "validation_clues": {"type": "array", "items": {"type": "string"}},
        "warnings": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "chunk_id",
        "evidence",
        "candidate_models",
        "candidate_algorithms",
        "assumptions",
        "variables",
        "validation_clues",
        "warnings",
    ],
    "additionalProperties": False,
}

SYNTHESIS_OUTPUT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "bibliographic": {"type": "object", "additionalProperties": True},
        "problem": {"type": "object", "additionalProperties": True},
        "assumptions": {"type": "array", "items": {"type": "object", "additionalProperties": True}},
        "variables": {"type": "array", "items": {"type": "object", "additionalProperties": True}},
        "data": {"type": "object", "additionalProperties": True},
        "modeling_chain": {"type": "array", "items": {"type": "object", "additionalProperties": True}},
        "models": {"type": "array", "items": {"type": "object", "additionalProperties": True}},
        "algorithms": {"type": "array", "items": {"type": "object", "additionalProperties": True}},
        "validation": {"type": "object", "additionalProperties": True},
        "limitations": {"type": "array", "items": {"type": "string"}},
        "innovations": {"type": "array", "items": {"type": "string"}},
        "case": {"type": "object", "additionalProperties": True},
        "quality": {"type": "object", "additionalProperties": True},
    },
    "required": [
        "bibliographic",
        "problem",
        "assumptions",
        "variables",
        "data",
        "modeling_chain",
        "models",
        "algorithms",
        "validation",
        "limitations",
        "innovations",
        "case",
        "quality",
    ],
    "additionalProperties": False,
}

CODE_OUTPUT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "python_code": {"type": "string"},
        "matlab_code": {"type": "string"},
        "pytest_code": {"type": "string"},
        "metadata": {
            "type": "object",
            "properties": {
                "entrypoint": {"type": "string"},
                "dependencies": {"type": "array", "items": {"type": "string"}},
                "input_contract": {"type": "array", "items": {"type": "string"}},
                "output_contract": {"type": "array", "items": {"type": "string"}},
                "assumptions": {"type": "array", "items": {"type": "string"}},
                "limitations": {"type": "array", "items": {"type": "string"}},
            },
            "required": [
                "entrypoint",
                "dependencies",
                "input_contract",
                "output_contract",
                "assumptions",
                "limitations",
            ],
            "additionalProperties": False,
        },
    },
    "required": ["python_code", "matlab_code", "pytest_code", "metadata"],
    "additionalProperties": False,
}

GENERIC_OBJECT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": True,
}

_PURPOSE_SCHEMAS: dict[str, dict[str, Any]] = {
    "evidence": EVIDENCE_OUTPUT_SCHEMA,
    "synthesis": SYNTHESIS_OUTPUT_SCHEMA,
    "code": CODE_OUTPUT_SCHEMA,
}


def _strict_object(properties: dict[str, Any]) -> dict[str, Any]:
    """Build an object accepted by Codex Structured Outputs strict mode."""
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties),
        "additionalProperties": False,
    }


_STRING_LIST: dict[str, Any] = {"type": "array", "items": {"type": "string"}}
_NULLABLE_PARAMETER_VALUE: dict[str, Any] = {
    "type": ["string", "number", "integer", "boolean", "null"]
}

_STRICT_PARAMETER = _strict_object(
    {
        "name": {"type": "string"},
        "value": _NULLABLE_PARAMETER_VALUE,
        "unit": {"type": "string"},
        "description": {"type": "string"},
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
    }
)

_STRICT_ASSUMPTION = _strict_object(
    {
        "id": {"type": "string"},
        "statement": {"type": "string"},
        "rationale": {"type": "string"},
        "impact": {"type": "string"},
        "evidence_ids": _STRING_LIST,
        "evidence_quotes": _STRING_LIST,
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
    }
)

_STRICT_VARIABLE = _strict_object(
    {
        "symbol": {"type": "string"},
        "meaning": {"type": "string"},
        "unit": {"type": "string"},
        "domain": {"type": "string"},
        "data_type": {
            "type": "string",
            "enum": ["scalar", "vector", "matrix", "tensor", "set", "categorical", "unknown"],
        },
        "evidence_ids": _STRING_LIST,
        "evidence_quotes": _STRING_LIST,
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
    }
)

_STRICT_CANDIDATE_MODEL = _strict_object(
    {
        "name": {"type": "string"},
        "category": {"type": "string"},
        "role": {"type": "string"},
        "description": {"type": "string"},
        "equations": _STRING_LIST,
        "workflow": _STRING_LIST,
        "parameters": {"type": "array", "items": _STRICT_PARAMETER},
        "evidence_quotes": _STRING_LIST,
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
    }
)

_STRICT_CANDIDATE_ALGORITHM = _strict_object(
    {
        "name": {"type": "string"},
        "category": {"type": "string"},
        "purpose": {"type": "string"},
        "pseudocode": _STRING_LIST,
        "parameters": {"type": "array", "items": _STRICT_PARAMETER},
        "time_complexity": {"type": "string"},
        "space_complexity": {"type": "string"},
        "evidence_quotes": _STRING_LIST,
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
    }
)

_CODEX_EVIDENCE_OUTPUT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    **_strict_object(
        {
            "chunk_id": {"type": "string"},
            "evidence": {"type": "array", "items": EVIDENCE_ITEM_SCHEMA},
            "candidate_models": {"type": "array", "items": _STRICT_CANDIDATE_MODEL},
            "candidate_algorithms": {"type": "array", "items": _STRICT_CANDIDATE_ALGORITHM},
            "assumptions": {"type": "array", "items": _STRICT_ASSUMPTION},
            "variables": {"type": "array", "items": _STRICT_VARIABLE},
            "validation_clues": _STRING_LIST,
            "warnings": _STRING_LIST,
        }
    ),
}

_STRICT_BIBLIOGRAPHIC = _strict_object(
    {
        "title": {"type": "string"},
        "authors": _STRING_LIST,
        "year": {"type": ["integer", "null"]},
        "competition": {"type": "string"},
        "award": {"type": "string"},
        "problem_id": {"type": "string"},
        "abstract": {"type": "string"},
        "keywords": _STRING_LIST,
        "language": {"type": "string"},
    }
)

_STRICT_SUBPROBLEM = _strict_object(
    {
        "id": {"type": "string"},
        "statement": {"type": "string"},
        "task_types": _STRING_LIST,
        "inputs": _STRING_LIST,
        "outputs": _STRING_LIST,
        "constraints": _STRING_LIST,
        "evidence_ids": _STRING_LIST,
    }
)

_STRICT_PROBLEM = _strict_object(
    {
        "background": {"type": "string"},
        "overall_objective": {"type": "string"},
        "subproblems": {"type": "array", "items": _STRICT_SUBPROBLEM},
    }
)

_STRICT_DATA = _strict_object(
    {
        "sources": _STRING_LIST,
        "fields": _STRING_LIST,
        "data_types": _STRING_LIST,
        "preprocessing": _STRING_LIST,
        "missing_value_strategy": {"type": "string"},
        "outlier_strategy": {"type": "string"},
        "evidence_ids": _STRING_LIST,
    }
)

_STRICT_MODELING_STEP = _strict_object(
    {
        "order": {"type": "integer", "minimum": 1},
        "subproblem_id": {"type": "string"},
        "model_id": {"type": "string"},
        "algorithm_ids": _STRING_LIST,
        "input": {"type": "string"},
        "output": {"type": "string"},
        "rationale": {"type": "string"},
        "evidence_ids": _STRING_LIST,
    }
)

_STRICT_MODEL = _strict_object(
    {
        "id": {"type": "string"},
        "canonical_name": {"type": "string"},
        "category": {"type": "string"},
        "task_types": _STRING_LIST,
        "role": {"type": "string"},
        "description": {"type": "string"},
        "assumptions": _STRING_LIST,
        "inputs": _STRING_LIST,
        "outputs": _STRING_LIST,
        "equations": _STRING_LIST,
        "workflow": _STRING_LIST,
        "parameters": {"type": "array", "items": _STRICT_PARAMETER},
        "solver_algorithm_ids": _STRING_LIST,
        "strengths": _STRING_LIST,
        "weaknesses": _STRING_LIST,
        "use_when": _STRING_LIST,
        "avoid_when": _STRING_LIST,
        "alternatives": _STRING_LIST,
        "combinations": _STRING_LIST,
        "validation_methods": _STRING_LIST,
        "evidence_ids": _STRING_LIST,
        "evidence_quotes": _STRING_LIST,
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
    }
)

_STRICT_ALGORITHM = _strict_object(
    {
        "id": {"type": "string"},
        "canonical_name": {"type": "string"},
        "category": {"type": "string"},
        "purpose": {"type": "string"},
        "inputs": _STRING_LIST,
        "outputs": _STRING_LIST,
        "pseudocode": _STRING_LIST,
        "parameters": {"type": "array", "items": _STRICT_PARAMETER},
        "initialization": {"type": "string"},
        "stopping_criteria": _STRING_LIST,
        "time_complexity": {"type": "string"},
        "space_complexity": {"type": "string"},
        "implementation_notes": _STRING_LIST,
        "failure_modes": _STRING_LIST,
        "evidence_ids": _STRING_LIST,
        "evidence_quotes": _STRING_LIST,
        "provenance": {"type": "string", "enum": PROVENANCE_VALUES},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
    }
)

_STRICT_VALIDATION = _strict_object(
    {
        "methods": _STRING_LIST,
        "metrics": _STRING_LIST,
        "results": _STRING_LIST,
        "sensitivity_analysis": _STRING_LIST,
        "robustness_checks": _STRING_LIST,
        "evidence_ids": _STRING_LIST,
    }
)

_STRICT_PROBLEM_FINGERPRINT = _strict_object(
    {
        "problem_types": _STRING_LIST,
        "data_types": _STRING_LIST,
        "targets": _STRING_LIST,
        "constraints": _STRING_LIST,
        "domain_keywords": _STRING_LIST,
    }
)

_STRICT_SUBPROBLEM_MAPPING = _strict_object(
    {
        "subproblem_id": {"type": "string"},
        "task": {"type": "string"},
        "model_ids": _STRING_LIST,
        "algorithm_ids": _STRING_LIST,
        "data_flow": {"type": "string"},
        "rationale": {"type": "string"},
        "evidence_ids": _STRING_LIST,
    }
)

_STRICT_CASE = _strict_object(
    {
        "id": {"type": "string"},
        "title": {"type": "string"},
        "domain": {"type": "string"},
        "competition": {"type": "string"},
        "year": {"type": ["integer", "null"]},
        "award": {"type": "string"},
        "problem_id": {"type": "string"},
        "problem_fingerprint": _STRICT_PROBLEM_FINGERPRINT,
        "subproblem_mapping": {"type": "array", "items": _STRICT_SUBPROBLEM_MAPPING},
        "results": _STRING_LIST,
        "transferable_insights": _STRING_LIST,
        "pitfalls": _STRING_LIST,
        "innovations": _STRING_LIST,
        "evidence_ids": _STRING_LIST,
    }
)

_STRICT_QUALITY = _strict_object(
    {
        "evidence_coverage": {"type": "number", "minimum": 0, "maximum": 1},
        "completeness": {"type": "number", "minimum": 0, "maximum": 1},
        "code_reproducibility": {"type": "number", "minimum": 0, "maximum": 1},
        "warnings": _STRING_LIST,
        "review_required": {"type": "boolean"},
    }
)

_CODEX_SYNTHESIS_OUTPUT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    **_strict_object(
        {
            "bibliographic": _STRICT_BIBLIOGRAPHIC,
            "problem": _STRICT_PROBLEM,
            "assumptions": {"type": "array", "items": _STRICT_ASSUMPTION},
            "variables": {"type": "array", "items": _STRICT_VARIABLE},
            "data": _STRICT_DATA,
            "modeling_chain": {"type": "array", "items": _STRICT_MODELING_STEP},
            "models": {"type": "array", "items": _STRICT_MODEL},
            "algorithms": {"type": "array", "items": _STRICT_ALGORITHM},
            "validation": _STRICT_VALIDATION,
            "limitations": _STRING_LIST,
            "innovations": _STRING_LIST,
            "case": _STRICT_CASE,
            "quality": _STRICT_QUALITY,
        }
    ),
}

_CODEX_PURPOSE_SCHEMAS: dict[str, dict[str, Any]] = {
    "evidence": _CODEX_EVIDENCE_OUTPUT_SCHEMA,
    "synthesis": _CODEX_SYNTHESIS_OUTPUT_SCHEMA,
    "code": CODE_OUTPUT_SCHEMA,
}


def schema_for_purpose(purpose: str) -> dict[str, Any]:
    """Return a detached JSON Schema suitable for Codex/Claude structured output."""
    return copy.deepcopy(_PURPOSE_SCHEMAS.get(purpose, GENERIC_OBJECT_SCHEMA))


def schema_for_codex(purpose: str) -> dict[str, Any]:
    """Return a detached schema that satisfies Codex strict-object requirements."""
    fallback = _strict_object({"result": {"type": "string"}})
    return copy.deepcopy(_CODEX_PURPOSE_SCHEMAS.get(purpose, fallback))


def validate_purpose_output(data: dict[str, Any], purpose: str) -> None:
    validator = Draft202012Validator(schema_for_purpose(purpose))
    errors = sorted(validator.iter_errors(data), key=lambda item: list(item.absolute_path))
    if not errors:
        return
    messages: list[str] = []
    for error in errors[:12]:
        path = ".".join(str(part) for part in error.absolute_path) or "$"
        messages.append(f"{path}: {error.message}")
    raise LLMResponseError(
        f"Local agent returned JSON that does not match the {purpose!r} schema: " + "; ".join(messages)
    )
