from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@pytest.fixture()
def project_root() -> Path:
    return ROOT


@pytest.fixture()
def demo_ir() -> dict:
    return json.loads((ROOT / "examples" / "demo_paper" / "paper_ir.json").read_text(encoding="utf-8"))


@pytest.fixture()
def demo_markdown() -> str:
    return (ROOT / "examples" / "demo_paper" / "normalized_paper.md").read_text(encoding="utf-8")
