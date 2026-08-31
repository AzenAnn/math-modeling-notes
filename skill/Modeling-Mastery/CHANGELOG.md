# Changelog

## 0.2.0 — 2026-08-26

- 新增本地 Codex CLI 结构化推理后端，复用当前机器的 Codex 登录态，无需单独填写 API Key。
- 新增本地 Claude Code CLI 结构化推理后端，复用当前机器的 Claude Code 登录态。
- 新增 `local-agent` 自动选择与 Codex → Claude Code 回退机制。
- 新增 `modeling-mastery skill-run`，可直接把七阶段流水线作为本地 Agent Skill 工作流运行。
- 支持同时安装到 Codex `.agents/skills/` 与 Claude Code `.claude/skills/`。
- 为 Evidence、Paper IR 与 Code Reproducer 增加按任务划分的 JSON Schema 输出校验。
- 增加本地 CLI 协议、回退、Schema 拒绝、完整流水线和双宿主安装测试。
- 补充本地 Agent 配置、原生 Skill 工作流、安全边界与故障排查文档。

## 0.1.0 — 2026-08-26

- 实现七阶段论文知识蒸馏流水线。
- 支持 MinerU、Docling、PyMuPDF 三级 PDF 解析回退。
- 实现证据锚点、统一 Paper IR、模型/算法规范化与来源标记。
- 实现 Python + MATLAB 代码复现接口、静态安全检查、超时运行与测试。
- 实现 Obsidian 幂等写入、YAML、Wikilink、注册表、去重与 SQLite FTS5 索引。
- 提供七个 Agent Skill、JSON Schema、Jinja 模板、示例和 24 项自动化测试。
- 支持目录级批量建库、断点跳过与单篇失败隔离。
- 增加 Markdown 多页映射、章节层级以及公式/图/表的确定性证据锚点。
- 提供可安装 wheel、Skill 安装器和验证矩阵。
