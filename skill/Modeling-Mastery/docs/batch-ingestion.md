# 批量建库

## 1. 基本命令

```bash
modeling-mastery batch ./papers \
  --workspace-root ./workspaces/batch-001 \
  --vault "D:/Obsidian/Mathematical-Modeling" \
  --backend auto
```

等价脚本：

```bash
python scripts/batch_pipeline.py ./papers \
  --workspace-root ./workspaces/batch-001 \
  --vault "D:/Obsidian/Mathematical-Modeling"
```

## 2. 断点恢复

默认启用 `--resume`。当某论文 workspace 已包含：

```text
ir/paper_ir.json
reports/pipeline_report.json
```

该论文会被跳过。使用 `--no-resume` 强制重跑。

## 3. 失败隔离

默认 `--continue-on-error`：某篇 PDF 失败不阻断整个目录，错误、异常类型与 traceback 写入 `batch_report.json`。使用 `--fail-fast` 在第一处错误停止。

## 4. 批量代码复现

```bash
modeling-mastery batch ./papers \
  --workspace-root ./workspaces/batch-code \
  --vault ./vault \
  --reproduce-code \
  --max-code-targets 4
```

代码生成和测试成本显著高于论文分析。建议先批量生成 IR 和知识卡，再对最有价值的模型单独执行 `reproduce`。

## 5. 建库策略

- 第一轮：每类题选 5–10 篇高质量获奖论文，验证 taxonomy。
- 第二轮：按模型缺口补充，而不是无差别堆论文。
- 每批结束后运行 `deduplicate` 和 `retrieve` 做质量抽检。
- 对 `AI_INFERRED` 数量过多、Evidence Coverage 过低的论文设置人工复核标签。
