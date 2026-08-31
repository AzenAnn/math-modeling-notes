from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from .errors import SchemaValidationError
from .io_utils import asset_dir


class SchemaStore:
    def __init__(self, schemas_dir: Path | None = None):
        self.schemas_dir = schemas_dir or asset_dir("schemas")
        self._schemas: dict[str, dict[str, Any]] = {}
        self._registry = Registry()
        self._load_all()

    def _load_all(self) -> None:
        resources: list[tuple[str, Resource[Any]]] = []
        for path in sorted(self.schemas_dir.glob("*.schema.json")):
            schema = json.loads(path.read_text(encoding="utf-8"))
            self._schemas[path.name] = schema
            schema_id = schema.get("$id")
            if schema_id:
                resources.append((schema_id, Resource.from_contents(schema)))
        self._registry = self._registry.with_resources(resources)

    def get(self, name: str) -> dict[str, Any]:
        normalized = name if name.endswith(".schema.json") else f"{name}.schema.json"
        if normalized not in self._schemas:
            raise KeyError(f"Unknown schema: {name}")
        return self._schemas[normalized]

    def errors(self, name: str, instance: Any) -> list[str]:
        schema = self.get(name)
        validator = Draft202012Validator(schema, registry=self._registry)
        result: list[str] = []
        for error in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path)):
            path = "/".join(str(part) for part in error.absolute_path) or "$"
            result.append(f"{path}: {error.message}")
        return result

    def validate(self, name: str, instance: Any) -> None:
        errors = self.errors(name, instance)
        if errors:
            raise SchemaValidationError(name, errors)
