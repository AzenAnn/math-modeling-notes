from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def atomic_write_text(path: Path, text: str, encoding: str = "utf-8") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding=encoding, newline="\n") as handle:
            handle.write(text)
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: Any, *, indent: int = 2) -> None:
    atomic_write_text(path, json.dumps(data, ensure_ascii=False, indent=indent) + "\n")


def read_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def write_yaml(path: Path, data: Any) -> None:
    text = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=1000)
    atomic_write_text(path, text)


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", text)).strip()


def canonical_key(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    return "".join(ch for ch in value if ch.isalnum())


def safe_filename(value: str, *, fallback: str = "untitled", max_length: int = 100) -> str:
    value = unicodedata.normalize("NFKC", value).strip()
    value = re.sub(r"[\\/:*?\"<>|\x00-\x1f]", "-", value)
    value = re.sub(r"\s+", " ", value)
    value = value.strip(" .-")
    if not value:
        value = fallback
    return value[:max_length].rstrip(" .-") or fallback


def slug_id(value: str, *, prefix: str = "") -> str:
    key = canonical_key(value)
    readable = re.sub(r"[^a-z0-9]+", "-", key).strip("-")[:36]
    digest = sha256_text(value)[:10]
    core = f"{readable}-{digest}" if readable else digest
    return f"{prefix}{core}"


def merge_unique(*iterables: Iterable[Any]) -> list[Any]:
    result: list[Any] = []
    seen: set[str] = set()
    for iterable in iterables:
        for item in iterable:
            marker = json.dumps(item, ensure_ascii=False, sort_keys=True, default=str)
            if marker not in seen:
                seen.add(marker)
                result.append(item)
    return result


def find_project_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in [current, *current.parents]:
        if (candidate / "pyproject.toml").exists() and (candidate / "schemas").exists():
            return candidate
    return Path(__file__).resolve().parent.parent


def asset_dir(kind: str, project_root: Path | None = None) -> Path:
    root = project_root or find_project_root()
    source_path = root / kind
    if source_path.exists():
        return source_path
    packaged = Path(__file__).resolve().parent / "assets" / kind
    if packaged.exists():
        return packaged
    raise FileNotFoundError(f"Cannot find asset directory: {kind}")


def relative_posix(path: Path, base: Path) -> str:
    try:
        return path.resolve().relative_to(base.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()
