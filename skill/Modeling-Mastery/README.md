# Modeling-Mastery

**面向数学建模竞赛的论文知识蒸馏、模型检索与代码复用 Pipeline。**

它把一篇数模论文从 PDF 编译为可核验、可执行、可检索的知识资产：

```text
数模论文 PDF
  → Paper Ingest（MinerU / Docling / PyMuPDF）
  → Evidence Extractor（页码 / Section / Eq / Fig 锚点）
  → Model Miner（问题 → 假设 → 变量 → 模型 → 求解）
  → Algorithm Miner（算法 / 参数 / 复杂度 / 伪代码）
  → Code Reproducer（Python + MATLAB + tests）
  → Knowledge Distiller（模型卡 / 算法卡 / 代码卡 / 案例卡）
  → Obsidian Writer（YAML / Wikilink / Tag / 去重 / 索引）
  → Modeling Vault
```

## 设计原则

1. **证据优先**：论文结论必须指向页码、章节、公式、图表或原文片段。
2. **来源分级**：严格区分 `PAPER_EXPLICIT`、`PAPER_DERIVED`、`AI_INFERRED`、`EXTERNAL_REFERENCE` 与 `HEURISTIC`。
3. **IR 优先**：先生成统一 `paper_ir.json`，再渲染所有笔记和代码资产。
4. **一篇论文，多张知识卡**：Paper、Case、Model、Algorithm、Code Recipe 分开存储并互相链接。
5. **幂等与去重**：同一论文重复运行不会无限生成副本；同义模型归一到 canonical name。
6. **代码先审后跑**：生成代码先做 AST/语法/危险调用检查，再进入受限子进程测试。
7. **赛前建库、赛时反查**：SQLite FTS5 + 结构化元数据共同完成模型检索。
8. **一篇一目录**：单篇解读默认收拢到 `论文/<论文题目>/`，自动流程、知识库与人工补充互不混放。

## 快速开始

### 1. 安装核心依赖

```bash
cd Modeling-Mastery
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[pdf]"
```

高质量 PDF 解析可选安装：

```bash
# Docling
python -m pip install -e ".[docling]"

# MinerU（请按 MinerU 官方环境要求安装）
uv pip install -U "mineru[all]"
```

### 2. 配置语义引擎

#### 方案 A：直接使用本机 Codex / Claude Code（推荐）

这一模式复用你已经登录的本地 CLI，不需要再给 Modeling-Mastery 填一份 API Key。先检查：

```bash
codex --version
claude --version
modeling-mastery doctor
```

自动优先使用 Codex，失败时回退到 Claude Code：

```bash
export MODELING_LLM_PROVIDER=local-agent
export MODELING_LOCAL_AGENT_PREFERENCE=codex,claude-code
```

只使用 Codex：

```bash
export MODELING_LLM_PROVIDER=codex
export MODELING_CODEX_COMMAND=codex
# 可选；留空时沿用 Codex 当前配置
export MODELING_CODEX_MODEL=
```

只使用 Claude Code：

```bash
export MODELING_LLM_PROVIDER=claude-code
export MODELING_CLAUDE_COMMAND=claude
# 可选；留空时沿用 Claude Code 当前配置
export MODELING_CLAUDE_MODEL=
```

也可以不设置环境变量，直接运行：

```bash
modeling-mastery skill-run paper.pdf \
  --agent codex \
  --library-root "D:/Obsidian/Mathematical-Modeling" \
  --paper-title "论文正式题目" \
  --reproduce-code
```

将 `--agent codex` 改成 `--agent claude` 即可使用 Claude Code；`--agent auto` 会按 `MODELING_LOCAL_AGENT_PREFERENCE` 自动选择和回退。

本地 CLI 调用使用 JSON Schema 约束输出。Codex 默认采用 `read-only + never approval`；Claude Code 默认采用 `--bare`、`plan` 权限模式并禁用内置和 MCP 工具。它们只负责对已经传入的论文文本做结构化语义分析，确定性文件写入仍由 Modeling-Mastery 完成。

#### 方案 B：API Provider

OpenAI-compatible：

```bash
export MODELING_LLM_PROVIDER=openai-compatible
export MODELING_LLM_BASE_URL=https://api.openai.com/v1
export MODELING_LLM_API_KEY=...
export MODELING_LLM_MODEL=...
```

Anthropic：

```bash
export MODELING_LLM_PROVIDER=anthropic
export MODELING_LLM_BASE_URL=https://api.anthropic.com
export MODELING_LLM_API_KEY=...
export MODELING_LLM_MODEL=...
```

`mock` 用于测试；`none` 只构建启发式骨架。完整变量见 [`.env.example`](.env.example) 与 [`docs/llm-providers.md`](docs/llm-providers.md)。

### 3. 一条命令完成论文到 Vault

```bash
modeling-mastery pipeline paper.pdf \
  --library-root "D:/Obsidian/Mathematical-Modeling" \
  --paper-title "论文正式题目" \
  --backend auto \
  --reproduce-code
```

输出大致如下：

```text
Mathematical-Modeling/
└── 论文/
    └── 论文正式题目/
        ├── README.md
        ├── assets/
        ├── workflow/
        │   ├── parsed/
        │   ├── ir/
        │   ├── code/
        │   └── reports/
        ├── 补充笔记/
        │   ├── 模型/
        │   └── 算法/
        └── 知识库/
            ├── 00_Home/
            ├── 10_Models/
            ├── 20_Algorithms/
            ├── 30_Code-Recipes/
            ├── 40_Competition-Cases/
            ├── 50_Papers/
            ├── _assets/
            └── .modeling-mastery/
```

这一路径会先由 `modeling-mastery init-paper <library-root> --title "<论文题目>"` 初始化。只有批量汇总或用户明确要求共享知识库时，才继续使用独立的 `--workspace` 与 `--vault`。详见 [`docs/paper-workspace.md`](docs/paper-workspace.md)。

### 4. 批量把论文目录蒸馏到同一 Vault

```bash
modeling-mastery batch ./papers \
  --workspace-root ./workspaces/batch-001 \
  --vault "D:/Obsidian/Mathematical-Modeling" \
  --backend auto
```

批处理默认串行、单篇失败隔离、持续写入 `batch_report.json`，并通过 `--resume` 跳过已经生成 `paper_ir.json` 与 `pipeline_report.json` 的论文。详见 [`docs/batch-ingestion.md`](docs/batch-ingestion.md)。

### 5. 分阶段运行

```bash
# 01 Paper Ingest
python scripts/parse_pdf.py paper.pdf -o workspaces/demo/parsed --backend auto

# 02–04 Evidence / Model / Algorithm
python scripts/build_ir.py \
  workspaces/demo/parsed/normalized_paper.md \
  --structure workspaces/demo/parsed/paper_structure.json \
  --output workspaces/demo/ir/paper_ir.raw.json

# 规范化模型名与来源
python scripts/normalize_model.py \
  workspaces/demo/ir/paper_ir.raw.json \
  -o workspaces/demo/ir/paper_ir.json

# 05 Code Reproducer
python scripts/reproduce_code.py \
  workspaces/demo/ir/paper_ir.json \
  --output workspaces/demo/code

# 06–07 Knowledge Distiller + Obsidian Writer
python scripts/write_obsidian.py \
  workspaces/demo/ir/paper_ir.json \
  --library-root "D:/Obsidian/Mathematical-Modeling" \
  --code-root workspaces/demo/code

# 去重、索引与检索
python scripts/deduplicate.py "D:/Obsidian/Mathematical-Modeling"
python scripts/build_index.py "D:/Obsidian/Mathematical-Modeling"
python scripts/retrieve_models.py "D:/Obsidian/Mathematical-Modeling" \
  "多指标综合评价，需要客观赋权和排序" --type model --top-k 5
```

## Agent Skill 工作流

项目中的 `SKILL.md` 是总编排 Skill，`skills/*/SKILL.md` 是七个子 Skill。可以一次安装到 Codex 和 Claude Code 的项目级目录：

```bash
modeling-mastery install-skills --host both --scope project
# 等价脚本：
python scripts/install_skills.py --host both --scope project
```

生成位置：

```text
Codex       .agents/skills/
Claude Code .claude/skills/
```

安装为用户级全局 Skill：

```bash
modeling-mastery install-skills --host both --scope user
```

在 Codex 中显式调用：

```text
$modeling-mastery paper.pdf --library-root D:/Obsidian/Mathematical-Modeling --paper-title "论文正式题目"
$model-retriever 多指标评价 客观赋权 排序
```

在 Claude Code 中显式调用：

```text
/modeling-mastery paper.pdf --library-root D:/Obsidian/Mathematical-Modeling --paper-title "论文正式题目"
/model-retriever 多指标评价 客观赋权 排序
```

Skill 会编排确定性脚本，并可通过 `modeling-mastery skill-run --agent codex|claude|auto` 把语义阶段交给本机已登录的 Codex 或 Claude Code。无需在 Skill 文件中保存 API Key。

完整说明见 [`docs/native-skill-workflow.md`](docs/native-skill-workflow.md)。

## Parser 回退策略

`--backend auto` 按顺序尝试：

1. MinerU CLI：`mineru -p <input> -o <output>`；可通过 `MODELING_MINERU_BACKEND=pipeline` 指定 CPU 友好的 pipeline 后端。
2. Docling Python API：`DocumentConverter().convert(...).document.export_to_markdown()`。
3. PyMuPDF：快速文本、页码和内嵌图片兜底。

无论正文由哪个后端产生，项目都会尽量用 PyMuPDF 再建立页级文本映射与图片 manifest，供证据锚定使用。

## 安全边界

- LLM 生成代码属于**不可信代码**。项目会检查危险导入、系统命令、动态执行、网络库和文件破坏操作，并使用超时与资源限制运行，但这不是完整的操作系统级沙箱。
- 比赛正式环境中，建议在 Docker、WSL 临时发行版或专用虚拟机中复现代码。
- 自动抽取结果必须查看 `quality.warnings`、`AI_INFERRED` 字段和代码验证报告，不能把模型输出当作论文原文。

## 项目结构

```text
Modeling-Mastery/
├── SKILL.md
├── skills/
├── schemas/
├── templates/
├── references/
├── scripts/
├── modeling_mastery/
├── tests/
├── examples/
└── docs/
```

## 测试

```bash
pytest
```

当前随项目交付的自动化测试覆盖 JSON Schema、多页与公式证据锚定、模型归一化、代码静态检查、Vault 幂等写入、索引检索、批量断点恢复和离线流水线。实际构建环境的验证边界见 [`docs/verification.md`](docs/verification.md)。

## 文档导航

- [`docs/architecture.md`](docs/architecture.md)：七阶段架构、阶段契约与可替换点。
- [`docs/ir-spec.md`](docs/ir-spec.md)：Paper IR、Evidence 与 Provenance 规范。
- [`docs/obsidian-vault.md`](docs/obsidian-vault.md)：Vault 目录、幂等写入、Registry 和索引。
- [`docs/paper-workspace.md`](docs/paper-workspace.md)：`论文/<论文题目>/` 默认整理机制、路径边界与验收规则。
- [`docs/llm-providers.md`](docs/llm-providers.md)：本地 Codex、Claude Code、API、Mock 与离线模式。
- [`docs/native-skill-workflow.md`](docs/native-skill-workflow.md)：Codex / Claude Code Skill 安装和本地 CLI 工作流。
- [`docs/security.md`](docs/security.md)：生成代码的威胁模型和执行边界。
- [`docs/batch-ingestion.md`](docs/batch-ingestion.md)：批量建库与断点恢复。
- [`docs/verification.md`](docs/verification.md)：已验证能力、未验证外部集成与目标机器验收命令。
- [`examples/README.md`](examples/README.md)：有效 IR 和 TOPSIS 代码示例。

## 第三方组件

本项目不复制 MinerU、Docling 或 Obsidian 的代码，只通过可选依赖或 CLI/API 调用它们。请分别遵守各自许可证与环境要求。详见 `docs/third_party.md`。
