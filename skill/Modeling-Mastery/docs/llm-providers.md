# LLM 与本地 Agent Provider 配置

Modeling-Mastery 的语义阶段统一通过 `BaseLLM.generate_json()` 工作。Provider 可以是 HTTP API，也可以是已经安装并登录的本地 Codex CLI / Claude Code CLI。

## 1. local-agent：自动选择本地 CLI

```bash
export MODELING_LLM_PROVIDER=local-agent
export MODELING_LOCAL_AGENT_PREFERENCE=codex,claude-code
export MODELING_LOCAL_AGENT_FALLBACK=true
```

运行时先尝试 Codex。某次调用失败时，若 `MODELING_LOCAL_AGENT_FALLBACK=true`，会尝试 Claude Code。该回退按每一次 Evidence、Synthesis 或 Code 任务执行，不会把失败输出静默当成成功。

```bash
modeling-mastery doctor
modeling-mastery skill-run paper.pdf \
  --agent auto \
  --workspace workspaces/paper-001 \
  --vault /path/to/Mathematical-Modeling
```

`local-agent` 不读取 `MODELING_LLM_API_KEY`。它复用 CLI 自己保存的登录状态。

## 2. Codex CLI Provider

确认本机可运行：

```bash
codex --version
```

配置：

```bash
export MODELING_LLM_PROVIDER=codex
export MODELING_CODEX_COMMAND=codex
export MODELING_CODEX_MODEL=
export MODELING_CODEX_SANDBOX=read-only
export MODELING_CODEX_APPROVAL_POLICY=never
export MODELING_CODEX_EXTRA_ARGS=
```

也可直接运行：

```bash
modeling-mastery skill-run paper.pdf --agent codex \
  --workspace workspaces/paper-001
```

内部使用非交互式 `codex exec`：

```text
codex exec
  --sandbox read-only
  --ask-for-approval never
  --skip-git-repo-check
  --output-schema <temporary-schema.json>
  --output-last-message <temporary-result.json>
  -
```

论文文本通过标准输入传入。Codex 的最终输出由 JSON Schema 约束并再次由本地 `jsonschema` 校验。默认 `read-only` 已足够，因为 Agent 不负责直接修改 Vault；写入由 Python 确定性程序完成。

自定义安装命令示例：

```bash
export MODELING_CODEX_COMMAND="/opt/homebrew/bin/codex"
# 或者
export MODELING_CODEX_COMMAND="npx @openai/codex"
```

命令包含空格时会按照当前操作系统的命令行规则拆分。不要把不可信参数放入 `MODELING_CODEX_EXTRA_ARGS`。

## 3. Claude Code CLI Provider

确认本机可运行：

```bash
claude --version
```

配置：

```bash
export MODELING_LLM_PROVIDER=claude-code
export MODELING_CLAUDE_COMMAND=claude
export MODELING_CLAUDE_MODEL=
export MODELING_CLAUDE_PERMISSION_MODE=plan
export MODELING_CLAUDE_MAX_TURNS=1
export MODELING_CLAUDE_MAX_BUDGET_USD=0
export MODELING_CLAUDE_BARE=true
export MODELING_CLAUDE_EXTRA_ARGS=
```

也可直接运行：

```bash
modeling-mastery skill-run paper.pdf --agent claude \
  --workspace workspaces/paper-001
```

内部使用 Claude Code print mode：

```text
claude --print
  --bare
  --output-format json
  --json-schema <schema-json>
  --permission-mode plan
  --tools ""
  --disallowedTools "mcp__*"
  --no-session-persistence
  --max-turns 1
```

论文文本通过标准输入传入。结构化结果从 Claude Code 返回对象的 `structured_output` 字段读取，然后再次本地校验。默认禁用工具与 MCP，避免项目级 hook、插件或工具改变纯分析任务的行为。

需要限制单次费用时：

```bash
export MODELING_CLAUDE_MAX_BUDGET_USD=2.0
```

设为 `0` 表示不主动传入预算参数。

## 4. 指定本地 CLI 工作目录

```bash
export MODELING_LOCAL_AGENT_CWD=/path/to/Modeling-Mastery
```

未指定时使用启动 `modeling-mastery` 命令的当前目录。语义分析文本已经通过标准输入传入，正常情况下无需让 Agent 读取论文文件。

## 5. OpenAI-compatible API

适用于兼容 `/chat/completions` JSON 输出的服务：

```bash
export MODELING_LLM_PROVIDER=openai-compatible
export MODELING_LLM_BASE_URL=https://api.example.com/v1
export MODELING_LLM_API_KEY=...
export MODELING_LLM_MODEL=...
```

## 6. Anthropic API

```bash
export MODELING_LLM_PROVIDER=anthropic
export MODELING_LLM_BASE_URL=https://api.anthropic.com
export MODELING_LLM_API_KEY=...
export MODELING_LLM_MODEL=...
```

## 7. mock 与 none

### mock

用于测试 Code Reproducer 和流水线，不产生真实论文分析：

```bash
export MODELING_LLM_PROVIDER=mock
```

### none

完全离线，只使用参考目录和关键词规则：

```bash
export MODELING_LLM_PROVIDER=none
```

它能检查工程链路和识别部分常见模型名，但不能替代语义级拆解。

## 8. 通用参数

```bash
export MODELING_LLM_TIMEOUT=600
export MODELING_LLM_MAX_TOKENS=12000
export MODELING_LLM_TEMPERATURE=0
export MODELING_CODE_TIMEOUT=30
export MODELING_CODE_MEMORY_MB=2048
export MODELING_VAULT_PATH=/path/to/vault
```

本地 CLI 的长论文综合阶段通常比 API 请求耗时更久，建议将 `MODELING_LLM_TIMEOUT` 设置为 300–900 秒。

## 9. 安全与可复现性

- 本地 CLI 登录凭据由 Codex / Claude Code 自己管理，Modeling-Mastery 不读取其认证文件。
- 不要把真实 API Key、Codex 认证文件或 Claude Code 会话数据提交到 Git。
- JSON Schema 只能约束输出形状，不能保证论文理解正确。仍需检查 Evidence ID、`quality.warnings` 和 `AI_INFERRED`。
- 生成代码依然属于不可信代码。静态检查与资源限制不等于完整 OS 沙箱。
- `danger-full-access`、`bypassPermissions` 等模式不应作为默认值；只有在外部隔离容器内才考虑使用。

## 10. 自定义 Provider

继承 `modeling_mastery.llm.BaseLLM`，实现 `generate_json` 并返回 `LLMResult`。Evidence、Synthesis 和 Code 阶段都要求 JSON object。新的 Provider 应调用：

```python
from modeling_mastery.structured_output import validate_purpose_output

validate_purpose_output(data, purpose)
```

以保持与本地 CLI 相同的输出门禁。
