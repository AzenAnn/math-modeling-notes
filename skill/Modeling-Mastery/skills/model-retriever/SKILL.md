---
name: model-retriever
description: 将赛题或自然语言问题转成 Problem Fingerprint，从 Obsidian 数模库检索候选模型、算法、案例与代码，并解释匹配原因；比赛选题、选模或复用代码时使用。
license: MIT
metadata:
  version: 0.2.0
---

# Model Retriever

参数：`$ARGUMENTS`

## 赛题指纹

先提取：

- problem_types
- data_types
- targets
- constraints
- domain_keywords
- 是否需要解释性、实时性、全局最优或不确定性分析

再执行结构化过滤 + 词法检索：

```bash
python scripts/retrieve_models.py <vault> "<problem description>" --type model --top-k 10
python scripts/retrieve_models.py <vault> "<problem description>" --type case --top-k 10
python scripts/retrieve_models.py <vault> "<problem description>" --type code --top-k 10
```

## 输出候选方案

不要只返回一个模型。至少比较：

- 推荐模型栈
- 与问题指纹的匹配点
- 数据与假设前提
- 现有来源论文数量
- 可复用代码及验证状态
- 主要风险
- 一个简单 baseline

检索结果只是候选，不代表赛题一定应使用该模型；必须重新检查目标、约束、数据规模和验证方案。
