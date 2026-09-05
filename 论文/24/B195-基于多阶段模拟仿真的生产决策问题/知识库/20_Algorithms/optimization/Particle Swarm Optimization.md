---
type: algorithm
id: algorithm-particleswarmoptimization-1f1996630f
canonical_name: Particle Swarm Optimization
aliases:
- 粒子群优化
- 粒子群算法
- PSO
category: optimization
source_papers:
- 基于多阶段模拟仿真的生产决策问题
provenance: HEURISTIC
confidence: 0.58
tags:
- mm/algorithm
- mm/algorithm/optimization
updated_at: '2026-09-04T18:08:23+00:00'
---

<!-- MM:BEGIN AUTO -->
# Particle Swarm Optimization

> [!abstract] 用途
> 利用个体最优和群体最优引导连续空间搜索

## 基本属性

- 分类：`optimization`
- 来源等级：`HEURISTIC`
- 置信度：58%
- 输入：objective function、bounds、swarm settings
- 输出：global best position、global best value、history

## 伪代码

```text
1. 初始化粒子位置与速度
2. 计算每个粒子的目标值
3. 更新个体最优与全局最优
4. 更新速度和位置并执行边界处理
5. 达到停止条件后返回全局最优
```

## 初始化与停止条件

- 初始化：论文未说明
- 停止条件：最大迭代数；全局最优长期无改进

## 参数

| 参数 | 值 | 范围 | 说明 | 来源 |
|---|---|---|---|---|
| `inertia_weight` | 论文未说明 | paper-specific | 惯性权重 | AI_INFERRED |
| `cognitive_coefficient` | 论文未说明 | paper-specific | 个体学习因子 | AI_INFERRED |
| `social_coefficient` | 论文未说明 | paper-specific | 社会学习因子 | AI_INFERRED |

## 复杂度

- 时间：`O(G·P·C_f)`
- 空间：`O(P·d)`
- 说明：无

## 随机性与复现

- 使用随机性：是
- 必须固定 seed：是
- 说明：固定 seed 并报告多次运行

## 实现要点

- 边界处理方式必须说明
- 记录收敛曲线

## 常见失败模式

- 群体过早聚集
- 速度爆炸
- 参数尺度与变量范围不匹配

## 来源论文

- [[基于多阶段模拟仿真的生产决策问题]]：证据 E-TEXT-P021-cae2a6c04d

## 当前论文证据

> [!quote] E-TEXT-P021-cae2a6c04d · p.21 · 基于多阶段模拟仿真的生产决策问题
> (3) 预期在这两个算法的基础上 , 使用最速粒子群算法得到一个更好的快速迭代方法 -
<!-- MM:END AUTO -->

## 我的补充

在这里补充你自己的理解、比赛经验、参数选择与踩坑记录。
