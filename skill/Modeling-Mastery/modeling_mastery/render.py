from __future__ import annotations

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, Undefined

from .io_utils import asset_dir, safe_filename


def _wikilink(value: Any) -> str:
    text = str(value or "").strip()
    return f"[[{text}]]" if text else ""


def _md_list(values: Any, empty: str = "暂无") -> str:
    items = [str(value).strip() for value in (values or []) if str(value).strip()]
    return "\n".join(f"- {item}" for item in items) if items else empty


def _code_join(values: Any, empty: str = "未标注") -> str:
    items = [str(value).strip() for value in (values or []) if str(value).strip()]
    return "、".join(f"`{item}`" for item in items) if items else empty


def create_environment(templates_dir: Path | None = None) -> Environment:
    directory = templates_dir or asset_dir("templates")
    environment = Environment(
        loader=FileSystemLoader(str(directory)),
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
        undefined=Undefined,
    )
    environment.filters["wikilink"] = _wikilink
    environment.filters["md_list"] = _md_list
    environment.filters["code_join"] = _code_join
    environment.filters["filename"] = safe_filename
    return environment


def render_template(name: str, context: dict[str, Any], templates_dir: Path | None = None) -> str:
    environment = create_environment(templates_dir)
    return environment.get_template(name).render(**context).strip() + "\n"
