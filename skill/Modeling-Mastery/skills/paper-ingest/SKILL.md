---
name: paper-ingest
description: 数模论文摄取阶段。把 PDF 转为 normalized_paper.md、paper_structure.json、page_map.json 和 figures/；需要 MinerU/Docling/PyMuPDF 回退、抽取公式表格图片或建立页码映射时使用。
license: MIT
metadata:
  version: 0.2.0
---

# 01 Paper Ingest

参数：`$ARGUMENTS`

## 输入

- PDF 路径
- 输出目录
- backend：`auto|mineru|docling|pymupdf`

## 执行

```bash
python scripts/parse_pdf.py "<paper.pdf>" -o "<workspace>/parsed" --backend auto --mineru-backend pipeline
```

`auto` 顺序：MinerU → Docling → PyMuPDF。不得因为 MinerU 不可用就停止整个流程。

## 输出契约

```text
parsed/
├── normalized_paper.md
├── paper_structure.json
├── page_map.json
├── parse_manifest.json
└── figures/
    └── manifest.json
```

## 检查

- `parse_manifest.json.parser` 必须说明实际后端。
- `page_map.json` 的页数应与 PDF 大体一致。
- 公式、表格或图片缺失时写入 warnings，不得伪造。
- 扫描版 PDF 使用 PyMuPDF 得到空文本时，应建议安装 MinerU/Docling OCR 后端并重跑。
