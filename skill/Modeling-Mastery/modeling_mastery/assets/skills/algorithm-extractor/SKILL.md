---
name: algorithm-extractor
description: 从数模论文中抽取求解算法、初始化、参数、停止条件、复杂度、随机性、伪代码与失败模式；用户要求算法实现细节、复现参数或算法卡时使用。
license: MIT
metadata:
  version: 0.2.0
---

# 04 Algorithm Miner

参数：`$ARGUMENTS`

算法对象必须满足 `schemas/algorithm.schema.json`，至少回答：

- 算法解决哪个模型或子问题
- 输入与输出
- 初始化
- 逐步伪代码
- 参数及其 provenance
- 停止条件
- 时间/空间复杂度；论文未说明时写 `unknown`
- 是否使用随机数、是否暴露 seed
- 约束处理和不可行解修复
- 常见失败模式

参数表中，论文没有明确值时使用：

```json
{"value": null, "provenance": "AI_INFERRED"}
```

不要用“常见设置”冒充论文设置。外部推荐值只能标记 `EXTERNAL_REFERENCE`。
