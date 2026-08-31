---
name: paper-analyze
description: 数模论文证据分析阶段。逐块抽取页码、章节、公式、图表、假设、变量、参数、验证与结果证据，并建立可追溯 Evidence ID；用户要求精读、核验或防止论文总结幻觉时使用。
license: MIT
metadata:
  version: 0.2.0
---

# 02 Evidence Extractor

参数：`$ARGUMENTS`

## 输入

- `normalized_paper.md`
- `paper_structure.json`
- `page_map.json`

## 执行

```bash
python scripts/build_ir.py \
  <normalized_paper.md> \
  --structure <paper_structure.json> \
  --page-map <page_map.json> \
  --output <workspace>/ir/paper_ir.raw.json
```

本脚本同时产生 `evidence_chunks.json`。本 Skill 只关注证据质量：

- quote 必须是原文或公式。
- page 不确定则 `null`。
- Equation、Figure、Table 要保留 label 或 locator。
- 同一原文不重复创建多个 Evidence ID。
- 任何不能回到原文的说明标记 `AI_INFERRED`。

## 失败处理

某个 chunk 的 LLM 调用失败时，保留其他 chunk，并在该块使用 HEURISTIC 结果；最终报告必须说明哪些块失败。
