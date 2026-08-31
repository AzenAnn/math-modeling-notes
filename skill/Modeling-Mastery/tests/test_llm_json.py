from __future__ import annotations

import pytest

from modeling_mastery.errors import LLMResponseError
from modeling_mastery.llm import extract_json_object


def test_extract_json_from_fence_and_surrounding_text() -> None:
    assert extract_json_object("before```json\n{\"a\": 1}\n```after") == {"a": 1}
    assert extract_json_object("analysis text {\"b\": [1, 2]} trailing") == {"b": [1, 2]}


def test_extract_json_rejects_non_object() -> None:
    with pytest.raises(LLMResponseError):
        extract_json_object("[1, 2, 3]")
