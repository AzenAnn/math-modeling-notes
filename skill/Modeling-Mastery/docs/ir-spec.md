# Paper IR 规范

## 1. 为什么需要 IR

直接让不同 Prompt 分别生成 Paper Note、模型卡和代码，会出现模型名称、变量含义、参数来源互相矛盾的问题。Modeling-Mastery 先生成并校验 `paper_ir.json`，所有下游资产只读取这一份中间表示。

主 Schema：`schemas/paper.schema.json`。

## 2. 顶层结构

```json
{
  "schema_version": "1.0.0",
  "paper_id": "paper-...",
  "source": {},
  "bibliographic": {},
  "problem": {},
  "evidence": [],
  "assumptions": [],
  "variables": [],
  "data": {},
  "modeling_chain": [],
  "models": [],
  "algorithms": [],
  "validation": {},
  "limitations": [],
  "innovations": [],
  "case": {},
  "code_recipes": [],
  "quality": {}
}
```

## 3. Provenance

每个关键事实使用以下来源等级之一：

| 值 | 含义 | 例子 |
|---|---|---|
| `PAPER_EXPLICIT` | 论文直接写出 | “种群规模为 100” |
| `PAPER_DERIVED` | 可从论文公式/描述直接推导 | 由循环结构推导复杂度 |
| `AI_INFERRED` | 为补齐实现而推测 | 论文未写停止阈值，AI 给出默认值 |
| `EXTERNAL_REFERENCE` | 来自内置模型百科或外部教材 | TOPSIS 通用流程 |
| `HEURISTIC` | 规则匹配产生 | 通过关键词检测到模型名 |

严禁把 `AI_INFERRED` 或 `EXTERNAL_REFERENCE` 写成论文原始事实。

## 4. Evidence

一条 Evidence 至少包含：

```json
{
  "id": "E-TEXT-P002-ab12cd34ef",
  "kind": "text",
  "page": 2,
  "section": "2 模型建立",
  "locator": "page:2",
  "quote": "采用熵权法计算指标权重……",
  "provenance": "PAPER_EXPLICIT",
  "confidence": 0.92
}
```

Evidence ID 由类型、页码和内容哈希稳定生成。页码无法确认时为 `null`；不得根据章节顺序猜页码。

## 5. 模型与算法分离

- 模型卡描述数学关系、输入输出、假设、公式、适用场景和验证方法。
- 算法卡描述求解步骤、参数、初始化、停止条件、复杂度、随机性和失败模式。
- `modeling_chain` 将子问题、模型和算法连接起来。

## 6. Code Recipe

Code Recipe 不直接嵌入大段代码，而是保存：

- 目标模型/算法。
- Python/MATLAB 文件路径与入口。
- 依赖、输入输出契约。
- Source Anchors。
- 静态检查与测试结果。
- 限制和生成器信息。

## 7. 质量字段

`quality` 中的分数用于门禁而不是“论文水平评分”：

- `evidence_coverage`：被证据支撑的核心资产比例。
- `completeness`：IR 必需字段的可用程度。
- `code_reproducibility`：通过静态检查或测试的 recipe 比例。
- `warnings`：解析、抽取、参数或代码风险。
- `review_required`：默认必须人工复核。
