# Cross-Media Consistency Audit Report

> **Status**: PASSED（含已披露 OCR 警告）  
> **Date**: 2026-09-05  
> **Scope**: 16 篇论文的源 PDF、`manifest.json`、逐篇 `page_map.json`、`paper_ir.json`、`source_map.json`、`解读.md`、年度 `README.md` 与 `年度综述.md`  
> **Source-of-truth tier**: 原始扫描 PDF → 逐页 OCR `page_map.json` → Evidence `paper_ir.json`；本任务未复现论文代码，因此没有 `frozen_numbers.json`

## Pass Items

1. ✅ **论文覆盖一致**：源目录有 16 个 PDF，年度清单有 16 条记录，目标目录有 16 个 `编号-论文名` 文件夹；编号集合完全一致，无遗漏、无重复。
2. ✅ **页数一致**：源 PDF 页数、`manifest.json` 声明页数、16 份 `page_map.json` 和 16 份 `source_map.json` 均合计 807 页；逐篇比较没有页数差异。
3. ✅ **标题一致**：16 份 `解读.md` 的一级标题均与 `manifest.json` 的编号和题目一致；A178 因扫描首页缺标题而使用摘要推定名，已在清单和逐篇说明中同时披露。
4. ✅ **Evidence 数量一致**：每篇 `source_map.json.blocks` 与对应 `paper_ir.json.evidence` 数量相等，合计 1,099 条；不存在来源映射多写或漏写 Evidence 的情况。
5. ✅ **关键数值回溯通过**：抽查 11 篇的 25 个核心数值（含 A016/A178/A242 的碰撞、螺距和速度，B159/B196 利润，C038/C094 收益，D033 概率，E010/E061/E218 停车或效果指标）均能在对应完整 OCR 正文中找到同值文本。
6. ✅ **导航链接通过**：修复知识库首页文件名后，年度 README、年度综述和 16 份逐篇 README 的人工导航链接均解析到真实文件；没有剩余用户可见坏链。
7. ✅ **图像文件一致**：16 份 README 引用的 `assets/首页.png` 全部存在，且每个文件都由对应源 PDF 第 1 页生成；没有跨论文串图。
8. ✅ **解析器与置信度标注一致**：16 份 `paper_structure.json` 均记录 `pymupdf-ocr`；16 份 `translation_notes.md` 均声明 Tesseract `chi_sim+eng`、180 dpi 和公式/单位复核要求。
9. ✅ **年度横向比较口径一致**：A 题的结果差异和 E 题停车位差异均被表述为“模型/口径差异”，没有把不同约束下的数值直接平均或误当成同一实验结果。
10. ✅ **目录边界一致**：本次新增论文产物全部位于 `论文/24/`；仓库根目录未新增散落的 `00_Home`、`10_Models`、`parsed`、`ir` 或共享 Vault 目录。

## Divergences

无未解决的跨文件矛盾。

## Warnings / Unauditable Items

| # | 原因 | 影响 | 当前处理 | 后续复核 |
|---|---|---|---|---|
| 1 | 原始 PDF 全部为扫描件，公式 OCR 不可靠 | 公式、上下标、希腊字母、小数点、单位 | 每篇明确标为 medium 置信度；解读只校订方法主线和可读数字 | 正式引用/编码前回看源 PDF 页图 |
| 2 | A178 首页没有正式题目 | 文件夹名与论文题名无法逐字核对 | 使用摘要主题“板凳龙行进路径与速度控制优化”，在清单和说明中标注为推定 | 若取得原始封面，替换标题并全局重命名 |
| 3 | A053 摘要中的 Q4/Q5 单位被 OCR 破坏 | `12.5109`、`1.33` 的单位不可审计 | 解读保留数值但明确不直接引用单位 | 打开 A053 原 PDF 的结果页人工复核 |
| 4 | 本任务未运行论文附录代码 | 无法把论文数字与程序输出交叉验证 | 不声称代码复现；`code_reproducibility=0` | 需要复现时单独调用 code-reproducer/reviewer |
| 5 | Codex/Claude 本地语义后端单块 180 秒超时 | 自动 Paper IR 的模型字段偏保守 | 使用确定性 Evidence IR，并把人工校订模型/算法写入 `解读.md` 与 `补充笔记/` | 后端稳定后可重跑语义 IR，但不得覆盖人工补充 |

## Post-rerun Verification

在清除单篇语义后端试验对顶层状态报告的覆盖后，已重新执行 16/16 篇确定性分析与 16/16 篇蒸馏。终检仍为 807/807 页、空页 0、1,099 条 Evidence、16/16 份 Paper Schema 通过、全量产物失败项 0；此前的一致性结论没有变化。

## Verdict

- **Requested summary collection may be finalized**: yes
- **Blocking divergences**: 0
- **Warnings**: 5（均已在用户可见产物中披露）
- **Recommended next skill**: `completeness-auditor`
