# Verification Matrix

本文件记录 `Modeling-Mastery 0.2.0` 在交付构建环境中的实际验证范围。它用于区分“已运行验证”和“仅实现接口但当前环境不可用”的能力。

## 已验证

- Python：3.13.5；项目声明支持 Python 3.11+。
- 自动化测试：`pytest -q`，32 项通过。
- 语法编译：`python -m compileall -q modeling_mastery scripts tests` 通过。
- Markdown Ingest：页标记、多页 page map、章节层级、公式结构化抽取通过。
- PDF Ingest：使用 PyMuPDF 对真实生成的两页 PDF 跑通端到端流程。
- Evidence：文本、页码、章节与公式 `EQ-*` 锚点通过 Schema 校验。
- Model / Algorithm Miner：离线规则识别熵权法、TOPSIS 与 Dijkstra。
- Knowledge Distiller / Vault Writer：生成 Paper、Case、Model、Algorithm 笔记，幂等写入通过。
- Index / Retriever：生成 JSON 索引和 SQLite FTS5 数据库，模型反向检索通过。
- Code Reproducer：使用确定性 Mock LLM 生成 Python、MATLAB 与 pytest；Python 静态检查与 pytest 通过。
- Wheel：离线构建并在独立目录验证 CLI 与打包资产可读取。

- 本地 Agent CLI：使用模拟的 `codex` / `claude` 可执行程序验证命令参数、stdin、结构化输出、JSON Schema 校验、Codex→Claude 回退以及完整 Markdown 流水线。
- Skill 安装：验证 Codex 项目级 `.agents/skills/` 与 Claude Code 项目级 `.claude/skills/` 的双宿主安装。

## 当前环境未验证

- MinerU 实际运行：当前构建环境没有安装 `mineru` CLI。
- Docling 实际运行：当前构建环境没有安装 `docling`。
- 真实 OpenAI-compatible / Anthropic API：未提供 API Key，因此没有发起外部请求。
- 真实本地 Codex / Claude Code 登录态调用：构建容器未安装且未登录这两个 CLI；已通过模拟 CLI 验证协议，但需在目标机器执行一次真实验收。
- MATLAB / GNU Octave 运行：当前环境没有安装 Octave；仅完成 MATLAB 静态检查路径。
- 对扫描版、复杂双栏、超长公式和复杂表格的质量：依赖实际 MinerU/Docling 环境与论文样本，应在目标机器上补充验收。

## 推荐的目标机器验收

```bash
python -m modeling_mastery doctor
pytest -q

modeling-mastery pipeline path/to/paper.pdf \
  --workspace ./workspaces/acceptance \
  --vault /path/to/Mathematical-Modeling \
  --backend auto \
  --reproduce-code
```

检查：

- `parsed/parse_manifest.json`
- `ir/paper_ir.json`
- `ir/normalization_report.json`
- `code/code_reproduction_report.json`
- `reports/pipeline_report.json`
- Vault 中 `.modeling-mastery/index.json` 与 `modeling_index.sqlite3`
