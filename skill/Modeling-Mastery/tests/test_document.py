from __future__ import annotations

import json
from pathlib import Path

import pytest

from modeling_mastery.document import (
    _merge_markdown_pages_with_geometry,
    _normalize_ocr_text,
    parse_document,
)
from modeling_mastery.ir_builder import build_paper_ir


def test_markdown_ingest_creates_contract_files(tmp_path: Path) -> None:
    source = tmp_path / "paper.md"
    source.write_text("# Demo\n\nTOPSIS ranks alternatives.\n", encoding="utf-8")
    result = parse_document(source, tmp_path / "out", backend="markdown")
    assert result.parser == "markdown"
    assert result.normalized_markdown.exists()
    assert result.structure_json.exists()
    assert result.page_map_json.exists()
    structure = json.loads(result.structure_json.read_text(encoding="utf-8"))
    assert structure["document"]["page_count"] == 1
    assert structure["sections"][0]["title"] == "Demo"


def test_pymupdf_pdf_ingest(tmp_path: Path) -> None:
    fitz = pytest.importorskip("fitz")
    pdf = tmp_path / "paper.pdf"
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "TOPSIS and Dijkstra modeling paper")
    document.save(pdf)
    document.close()

    result = parse_document(pdf, tmp_path / "parsed", backend="pymupdf")
    assert result.parser == "pymupdf"
    page_map = json.loads(result.page_map_json.read_text(encoding="utf-8"))
    assert page_map["pages"][0]["page"] == 1
    assert "TOPSIS" in page_map["pages"][0]["text"]
    assert "MM_PAGE: 1" in result.normalized_markdown.read_text(encoding="utf-8")

    ir, _ = build_paper_ir(
        result.normalized_markdown,
        structure_path=result.structure_json,
        page_map_path=result.page_map_json,
        output_dir=tmp_path / "ir",
        llm=None,
    )
    assert ir["bibliographic"]["title"] == "TOPSIS and Dijkstra modeling paper"


def test_markdown_page_markers_build_true_page_map(tmp_path: Path) -> None:
    source = tmp_path / "paper.md"
    source.write_text(
        "<!-- MM_PAGE: 1 -->\n# 第一页\n正文一\n"
        "<!-- MM_PAGE: 2 -->\n## 第二页\n正文二\n"
        "<!-- MM_PAGE: 3 -->\n## 第三页\n正文三\n",
        encoding="utf-8",
    )
    result = parse_document(source, tmp_path / "out", backend="markdown")
    page_map = json.loads(result.page_map_json.read_text(encoding="utf-8"))
    structure = json.loads(result.structure_json.read_text(encoding="utf-8"))
    assert [page["page"] for page in page_map["pages"]] == [1, 2, 3]
    assert structure["document"]["page_count"] == 3
    assert [section["page"] for section in structure["sections"]] == [1, 2, 3]
    assert structure["sections"][1]["parent_section"] == "第一页"
    assert structure["sections"][2]["parent_section"] == "第一页"


def test_page_marked_ocr_text_keeps_pdf_geometry() -> None:
    markdown = (
        "<!-- MM_PAGE: 1 -->\n第一页 OCR\n"
        "<!-- MM_PAGE: 2 -->\n第二页 OCR\n"
    )
    geometry = [
        {"page": 1, "width": 595.0, "height": 842.0, "text": ""},
        {"page": 2, "width": 612.0, "height": 792.0, "text": ""},
    ]

    pages = _merge_markdown_pages_with_geometry(markdown, geometry)

    assert [page["text"] for page in pages] == ["第一页 OCR", "第二页 OCR"]
    assert [(page["width"], page["height"]) for page in pages] == [
        (595.0, 842.0),
        (612.0, 792.0),
    ]


def test_normalize_ocr_text_removes_artificial_cjk_spacing() -> None:
    source = "基 于 几 何 模 型\n\nresult1.xlsx, 表 1 。"
    assert _normalize_ocr_text(source) == "基于几何模型\n\nresult1.xlsx, 表 1。"


def test_title_hint_is_added_as_heading(tmp_path: Path) -> None:
    source = tmp_path / "paper.md"
    source.write_text("摘要正文", encoding="utf-8")
    result = parse_document(source, tmp_path / "out", backend="markdown", title_hint="正式题目")
    normalized = result.normalized_markdown.read_text(encoding="utf-8")
    structure = json.loads(result.structure_json.read_text(encoding="utf-8"))
    assert "# 正式题目" in normalized
    assert structure["sections"][0]["title"] == "正式题目"
