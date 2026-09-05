---
type: algorithm
id: algorithm-geneticalgorithm-82b827f16c
canonical_name: Genetic Algorithm
aliases:
- 遗传算法
- GA
category: optimization
source_papers:
- 基于差分遗传算法的农作物种植策略优化
provenance: HEURISTIC
confidence: 0.58
tags:
- mm/algorithm
- mm/algorithm/optimization
updated_at: '2026-09-04T18:08:23+00:00'
---

<!-- MM:BEGIN AUTO -->
# Genetic Algorithm

> [!abstract] 用途
> 通过选择、交叉和变异在复杂搜索空间中寻找近似最优解

## 基本属性

- 分类：`optimization`
- 来源等级：`HEURISTIC`
- 置信度：58%
- 输入：fitness function、encoding、constraints、population settings
- 输出：best solution、best fitness、convergence history

## 伪代码

```text
1. 初始化种群并修复不可行个体
2. 计算适应度
3. 根据选择策略生成父代
4. 执行交叉与变异
5. 进行精英保留与约束处理
6. 达到停止条件后输出最优个体
```

## 初始化与停止条件

- 初始化：按编码和约束生成初始可行种群
- 停止条件：最大迭代数；连续若干代最优值无改进

## 参数

| 参数 | 值 | 范围 | 说明 | 来源 |
|---|---|---|---|---|
| `population_size` | 论文未说明 | paper-specific | 种群规模 | AI_INFERRED |
| `crossover_rate` | 论文未说明 | [0,1] | 交叉概率 | AI_INFERRED |
| `mutation_rate` | 论文未说明 | [0,1] | 变异概率 | AI_INFERRED |

## 复杂度

- 时间：`O(G·P·C_f)`
- 空间：`O(P·d)`
- 说明：G 迭代数，P 种群规模，C_f 适应度计算代价

## 随机性与复现

- 使用随机性：是
- 必须固定 seed：是
- 说明：固定 seed 并多次独立运行

## 实现要点

- 约束处理必须明确
- 保存收敛曲线
- 多次运行报告均值和方差

## 常见失败模式

- 早熟收敛
- 编码不合理
- 适应度尺度失衡
- 参数未报告

## 来源论文

- [[基于差分遗传算法的农作物种植策略优化]]：证据 E-TEXT-P001-881d0487b4

## 当前论文证据

> [!quote] E-TEXT-P001-881d0487b4 · p.1 · 基于差分遗传算法的农作物种植策略优化
> 采用基于差分进化的改进速传算法 (DEGA3 , 对渤销和 309%6 降价出售两种情境进行
<!-- MM:END AUTO -->

## 我的补充

在这里补充你自己的理解、比赛经验、参数选择与踩坑记录。
