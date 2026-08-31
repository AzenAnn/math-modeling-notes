# Modeling-Mastery 架构说明

## 1. 总体目标

Modeling-Mastery 不是普通的论文摘要器，而是一条“论文知识编译流水线”。所有下游产物都由统一的 `paper_ir.json` 生成，以保证 Paper Note、模型卡、算法卡、代码卡与案例卡使用同一套事实和证据。

```text
PDF / Markdown
  │
  ├─ 01 Paper Ingest
  │      ├─ normalized_paper.md
  │      ├─ paper_structure.json
  │      ├─ page_map.json
  │      └─ figures/
  │
  ├─ 02 Evidence Extractor
  │      └─ Evidence ID + page/section/equation/figure anchors
  │
  ├─ 03 Model Miner
  │      └─ problem → assumptions → variables → models → modeling chain
  │
  ├─ 04 Algorithm Miner
  │      └─ algorithms → parameters → complexity → pseudocode
  │
  ├─ 05 Code Reproducer
  │      └─ Python + MATLAB + tests + validation.json
  │
  ├─ 06 Knowledge Distiller
  │      └─ Paper / Case / Model / Algorithm / Code cards
  │
  └─ 07 Obsidian Writer
         └─ YAML + Wikilink + tags + registry + search index
```

## 2. 分层

### 2.1 接口层

- `modeling_mastery/cli.py`：统一 CLI。
- `scripts/*.py`：可被 Agent Skill、Shell 或 CI 直接调用的薄封装。
- `SKILL.md` 与 `skills/*/SKILL.md`：Agent 编排契约。

### 2.2 领域层

- `document.py`：PDF/Markdown 规范化。
- `evidence.py`：证据分块、稳定 ID、锚点修复。
- `ir_builder.py`：启发式或 LLM 驱动的 Paper IR 构建。
- `normalizer.py`：canonical name、同义词、卡片合并。
- `codegen.py`：代码复现与 recipe 生成。
- `vault.py`：Obsidian 知识蒸馏与幂等写入。
- `indexer.py` / `retriever.py`：本地索引与赛时反查。

### 2.3 基础设施层

- `llm.py`：OpenAI-compatible、Anthropic、Mock、None Provider。
- `schema_utils.py`：JSON Schema 2020-12 校验。
- `runner.py`：受限子进程、超时、资源限制。
- `code_validation.py`：Python AST / MATLAB 危险调用扫描。
- `io_utils.py`：原子写入、哈希、资源定位。

## 3. 阶段契约

| 阶段 | 输入 | 必需输出 | 失败策略 |
|---|---|---|---|
| 01 | PDF/Markdown | normalized Markdown、structure、page map、figures | `auto` 依次回退；保留 warnings |
| 02 | normalized Markdown | evidence records | 页码不确定时留空，不猜测 |
| 03 | evidence + paper text | model cards、modeling chain | LLM 失败时保留启发式骨架 |
| 04 | evidence + paper text | algorithm cards | 未给参数标为 unknown/AI_INFERRED |
| 05 | IR | Python、MATLAB、tests、validation | 静态检查失败则禁止执行 |
| 06 | validated IR | knowledge cards | 只从 IR 渲染，不独立总结 |
| 07 | cards + existing Vault | Markdown、registry、index | 自动区覆盖，人工区保留 |

## 4. Parser 回退

`backend=auto`：

1. `mineru`：适合复杂版式、公式、表格和图片；通过 CLI 调用。
2. `docling`：通过 Python API 导出 Markdown 和结构化对象。
3. `pymupdf`：快速文本与内嵌图片兜底。

PDF 无论由哪个正文解析器处理，只要 PyMuPDF 可用，都会尽量额外建立逐页文本映射，供 Evidence Extractor 修复页码。

## 5. LLM 与确定性逻辑的边界

LLM 负责：

- 语义拆解子问题。
- 识别模型角色与建模链。
- 将论文描述转换为伪代码和候选代码。

确定性代码负责：

- 文件解析编排与回退。
- Stable ID、Schema、canonicalization。
- 文件写入、去重、索引、代码静态检查和测试执行。

这保证了更换模型、API 或提示词时，知识库结构和文件布局仍保持稳定。

## 6. 批量执行

`modeling-mastery batch` 默认串行处理。原因是 MinerU、Docling 与代码测试可能占用大量内存，比赛前在笔记本上并发处理容易降低稳定性。每篇论文拥有由“文件名 + SHA-256 前缀”构成的独立 workspace，并持续写入 `batch_report.json`；进程中断后可通过 `--resume` 跳过已经生成 IR 和报告的条目。

## 7. 可替换点

- 解析器：实现与 `parse_document` 相同的输出契约。
- LLM：继承 `BaseLLM` 并返回 JSON object。
- 检索器：可将 JSON/FTS5 替换为向量库，但应保留 YAML 元数据过滤。
- Vault：可增加 Obsidian MCP Adapter；当前默认直接写本地文件，便于离线和版本控制。
