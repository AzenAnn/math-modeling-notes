from __future__ import annotations

from typing import Any

from modeling_mastery.structured_output import schema_for_codex


def _assert_codex_strict_objects(node: Any) -> None:
    if isinstance(node, dict):
        node_type = node.get("type")
        if node_type == "object" or (isinstance(node_type, list) and "object" in node_type):
            properties = node.get("properties")
            assert isinstance(properties, dict) and properties
            assert node.get("additionalProperties") is False
            assert set(node.get("required", [])) == set(properties)
        for value in node.values():
            _assert_codex_strict_objects(value)
    elif isinstance(node, list):
        for value in node:
            _assert_codex_strict_objects(value)


def test_codex_evidence_schema_uses_strict_nested_objects() -> None:
    _assert_codex_strict_objects(schema_for_codex("evidence"))


def test_codex_synthesis_schema_uses_strict_nested_objects() -> None:
    _assert_codex_strict_objects(schema_for_codex("synthesis"))
