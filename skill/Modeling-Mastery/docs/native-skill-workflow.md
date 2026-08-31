# Codex / Claude Code 原生 Skill 工作流

Modeling-Mastery 同时支持两种“本地 Agent”使用方式：

1. 在普通终端中调用 `modeling-mastery skill-run`，由 Python 进程启动本机 Codex / Claude Code 的非交互式结构化任务。
2. 把 `SKILL.md` 安装到 Codex 或 Claude Code，在交互式 Agent 中直接调用完整工作流。

两种方式共用相同的七阶段 Pipeline、Schema、模板和确定性脚本。

## 1. 安装项目级 Skills

在准备存放数模论文和工作区的项目根目录执行：

```bash
modeling-mastery install-skills --host both --scope project
```

得到：

```text
<project>/
├── .agents/skills/       # Codex
│   ├── modeling-mastery/
│   ├── paper-ingest/
│   ├── paper-analyze/
│   ├── model-extractor/
│   ├── algorithm-extractor/
│   ├── code-reproducer/
│   ├── vault-writer/
│   └── model-retriever/
└── .claude/skills/       # Claude Code
    └── ...同上
```

只安装一个宿主：

```bash
modeling-mastery install-skills --host codex --scope project
modeling-mastery install-skills --host claude --scope project
```

## 2. 安装用户级 Skills

```bash
modeling-mastery install-skills --host both --scope user
```

目标位置：

```text
~/.agents/skills/   # Codex
~/.claude/skills/   # Claude Code
```

用户级安装适合在任意数模目录中使用；项目级安装适合团队共享和版本控制。

## 3. 在 Codex 中调用

启动 Codex 后，可以显式提及 Skill：

```text
$modeling-mastery 分析 ./papers/2025-A.pdf，workspace 放到 ./workspaces/2025-A，
Vault 写入 D:/Obsidian/Mathematical-Modeling，并复现 Python 与 MATLAB 代码。
```

单篇论文推荐直接指定上层笔记库和正式题目，由 Skill 自动使用 `论文/<论文题目>/workflow` 与 `论文/<论文题目>/知识库`：

```text
$modeling-mastery 分析 ./papers/2025-A.pdf，笔记库根目录是 D:/Obsidian/Mathematical-Modeling，
论文题目是“论文正式题目”，并复现 Python 与 MATLAB 代码。
```

也可以只调用某个阶段：

```text
$paper-ingest ./papers/2025-A.pdf
$model-retriever 多指标综合评价，要求客观赋权、排序和敏感性分析
```

## 4. 在 Claude Code 中调用

```text
/modeling-mastery 分析 ./papers/2025-A.pdf，workspace 放到 ./workspaces/2025-A，
Vault 写入 D:/Obsidian/Mathematical-Modeling，并复现 Python 与 MATLAB 代码。
```

分阶段调用：

```text
/paper-ingest ./papers/2025-A.pdf
/model-retriever 多指标综合评价，要求客观赋权、排序和敏感性分析
```

## 5. Skill 如何使用本地 Agent 接口

总 Skill 首先运行：

```bash
modeling-mastery doctor
```

然后根据用户要求选择：

```bash
modeling-mastery skill-run <paper> \
  --agent auto \
  --library-root <上层笔记库> \
  --paper-title "<论文题目>" \
  --reproduce-code
```

`--agent` 可选：

```text
auto    按 codex,claude-code 顺序尝试并回退
codex   只调用本机 Codex CLI
claude  只调用本机 Claude Code CLI
```

本地 Agent 只处理三类结构化语义任务：

```text
Evidence Extraction
Paper IR Synthesis
Code Reproduction
```

PDF 解析、页码映射、IR 规范化、Schema 校验、代码安全检查、测试、Vault 写入、去重和索引仍由 Python 脚本完成。

## 6. 为什么不让 Agent 直接随意修改 Vault

直接让交互式 Agent 边读论文边创建几十个 Markdown 文件，会导致：

- 同一模型产生多个名字不同的重复卡片；
- 每张笔记对论文的理解互相矛盾；
- 页码和公式引用缺乏统一 Evidence ID；
- Agent 中途失败后难以断点恢复；
- 用户手写内容容易被覆盖。

因此 Skill 必须坚持：

```text
论文 → Evidence → Paper IR → Schema Validation → Notes
```

而不是：

```text
论文 → Agent 随机创建笔记
```

## 7. 不使用环境变量的调用方式

```bash
modeling-mastery skill-run paper.pdf --agent codex \
  --workspace workspaces/paper

modeling-mastery skill-run paper.pdf --agent claude \
  --workspace workspaces/paper
```

要把普通 `pipeline` 命令固定到本地 Agent：

```bash
export MODELING_LLM_PROVIDER=local-agent
modeling-mastery pipeline paper.pdf --workspace workspaces/paper
```

## 8. 诊断

```bash
modeling-mastery doctor
```

重点检查：

```json
{
  "commands": {
    "codex": "codex",
    "claude": "claude"
  },
  "llm": {
    "provider": "local-agent",
    "ready": true,
    "local_agents": {}
  }
}
```

`available: true` 只说明命令可找到，不等于账号一定已登录。真实认证错误会在首次任务中明确返回。

## 9. 常见问题

### 找不到 Codex

```bash
export MODELING_CODEX_COMMAND=/absolute/path/to/codex
```

### 找不到 Claude Code

```bash
export MODELING_CLAUDE_COMMAND=/absolute/path/to/claude
```

### 当前目录不是 Git 仓库

Codex Provider 默认加入 `--skip-git-repo-check`，无需额外处理。

### Claude Code 加载了项目插件或 Hook

默认使用 `--bare` 并禁用工具。确认：

```bash
export MODELING_CLAUDE_BARE=true
```

### 单次任务超时

```bash
export MODELING_LLM_TIMEOUT=900
```

### 不希望自动回退

```bash
export MODELING_LOCAL_AGENT_FALLBACK=false
```
