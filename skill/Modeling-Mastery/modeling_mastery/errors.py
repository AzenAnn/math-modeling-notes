from __future__ import annotations


class ModelingMasteryError(RuntimeError):
    """Base exception."""


class ParserUnavailableError(ModelingMasteryError):
    """Requested parser is not installed or discoverable."""


class DocumentParseError(ModelingMasteryError):
    """All selected document parsers failed."""


class LLMConfigurationError(ModelingMasteryError):
    """LLM provider configuration is incomplete."""


class LLMResponseError(ModelingMasteryError):
    """LLM response is invalid or cannot be decoded."""


class SchemaValidationError(ModelingMasteryError):
    """JSON instance failed schema validation."""

    def __init__(self, schema_name: str, errors: list[str]):
        super().__init__(f"{schema_name} validation failed: " + "; ".join(errors[:10]))
        self.schema_name = schema_name
        self.errors = errors


class UnsafeGeneratedCodeError(ModelingMasteryError):
    """Generated code failed static safety checks."""
