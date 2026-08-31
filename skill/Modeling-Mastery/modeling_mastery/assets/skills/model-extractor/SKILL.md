---
name: model-extractor
description: 从数模论文证据中拆解问题、假设、变量、数据、模型方程、建模流程与模型选择理由，并归一化模型名称；用户问论文用了什么模型、模型怎么建立或如何形成模型卡时使用。
license: MIT
metadata:
  version: 0.2.0
---

# 03 Model Miner

参数：`$ARGUMENTS`

## 模型抽取顺序

```text
问题与子问题
→ 数据与约束
→ 假设
→ 变量与单位
→ 数学关系/目标/约束
→ 模型输入输出
→ 建模步骤
→ 选择理由
→ 验证方式
```

模型对象必须满足 `schemas/model.schema.json`。

不要把遗传算法、Dijkstra、粒子群等求解过程错误地当作模型；它们属于 Algorithm Card。可以把“车辆路径问题”“最短路径模型”“整数规划模型”作为 Model Card，再链接求解算法。

## 规范化

```bash
python scripts/normalize_model.py <paper_ir.raw.json> -o <paper_ir.json>
```

创建新模型前搜索 `references/` 和现有 Vault：

- 精确 canonical name
- aliases
- 中文/英文缩写
- 模糊重复候选

论文只出现名称、没有过程时，模型卡应降低 confidence，并写明缺失内容。
