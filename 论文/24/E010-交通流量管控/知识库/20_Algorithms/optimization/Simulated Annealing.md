---
type: algorithm
id: algorithm-simulatedannealing-8fb5c5797e
canonical_name: Simulated Annealing
aliases:
- 模拟退火
- SA
category: optimization
source_papers:
- 交通流量管控
provenance: HEURISTIC
confidence: 0.58
tags:
- mm/algorithm
- mm/algorithm/optimization
updated_at: '2026-09-04T18:08:24+00:00'
---

<!-- MM:BEGIN AUTO -->
# Simulated Annealing

> [!abstract] 用途
> 允许以一定概率接受劣解，从而跳出局部最优

## 基本属性

- 分类：`optimization`
- 来源等级：`HEURISTIC`
- 置信度：58%
- 输入：objective function、initial solution、neighborhood、cooling schedule
- 输出：best solution、best objective、history

## 伪代码

```text
1. 生成初始解并设定初始温度
2. 在邻域中生成候选解
3. 更优则接受，较差则按 Metropolis 概率接受
4. 按降温策略更新温度
5. 达到停止条件后返回历史最优解
```

## 初始化与停止条件

- 初始化：生成一个可行初始解
- 停止条件：温度低于阈值；达到最大迭代数；长期无改进

## 参数

| 参数 | 值 | 范围 | 说明 | 来源 |
|---|---|---|---|---|
| `initial_temperature` | 论文未说明 | paper-specific | 初始温度 | AI_INFERRED |
| `cooling_rate` | 论文未说明 | (0,1) | 降温系数 | AI_INFERRED |

## 复杂度

- 时间：`O(K·C_f)`
- 空间：`O(d)`
- 说明：K 为候选解评估次数

## 随机性与复现

- 使用随机性：是
- 必须固定 seed：是
- 说明：多次运行检查稳定性

## 实现要点

- 邻域设计决定搜索能力
- 温度尺度要与目标差值匹配

## 常见失败模式

- 降温过快
- 初始温度过低
- 邻域无法覆盖可行域

## 来源论文

- [[交通流量管控]]：证据 E-TEXT-P030-9037dbea85

## 当前论文证据

> [!quote] E-TEXT-P030-9037dbea85 · p.30 · 准备 ANOVA 测试的数据
> group_label = 「Monday-Friday「 if day < 5 else 「Saturday if day == 5 else "Sun-
<!-- MM:END AUTO -->

## 我的补充

在这里补充你自己的理解、比赛经验、参数选择与踩坑记录。
