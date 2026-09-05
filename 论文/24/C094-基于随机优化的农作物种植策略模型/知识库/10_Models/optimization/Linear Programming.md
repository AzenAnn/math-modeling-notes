---
type: model
id: model-linearprogramming-5c5372fcf9
canonical_name: Linear Programming
aliases:
- 线性规划
- LP
category: optimization
tasks:
- allocation
- scheduling
- minimization
- maximization
source_papers:
- 基于随机优化的农作物种植策略模型
provenance: HEURISTIC
confidence: 0.58
tags:
- mm/model
- mm/model/optimization
- mm/task/allocation
- mm/task/scheduling
- mm/task/minimization
- mm/task/maximization
updated_at: '2026-09-04T18:08:23+00:00'
---

<!-- MM:BEGIN AUTO -->
# Linear Programming

> [!abstract] 一句话说明
> 由参考目录识别，需结合论文证据复核。

## 适用定位

- 分类：`optimization`
- 任务：allocation、scheduling、minimization、maximization
- 在论文中的作用：在线性目标和线性约束下求最优决策变量
- 来源等级：`HEURISTIC`，置信度 58%

### 适合使用

- 目标和约束可线性表达
- 决策变量连续

### 不适合或慎用

- 明显非线性关系无法合理线性化

## 输入与输出

### 输入

- **objective_coefficients**：目标函数系数；shape=`n`
- **constraint_matrix**：约束系数矩阵；shape=`m×n`

### 输出

- **decision_variables**：最优决策变量；shape=`n`
- **objective_value**：最优目标值；shape=`scalar`

## 数学表达

论文或抽取结果中没有可靠公式。

## 建模步骤

1. **定义决策变量及单位**：定义决策变量及单位  
   输入：-；输出：-；证据：E-TEXT-P022-1fb065b390。
2. **写出目标函数**：写出目标函数  
   输入：-；输出：-；证据：E-TEXT-P022-1fb065b390。
3. **将业务规则转换为线性约束**：将业务规则转换为线性约束  
   输入：-；输出：-；证据：E-TEXT-P022-1fb065b390。
4. **检查可行域与变量边界**：检查可行域与变量边界  
   输入：-；输出：-；证据：E-TEXT-P022-1fb065b390。
5. **调用求解器并解释影子价格或松弛量**：调用求解器并解释影子价格或松弛量  
   输入：-；输出：-；证据：E-TEXT-P022-1fb065b390。

## 参数

| 参数 | 值 | 范围 | 说明 | 来源 |
|---|---|---|---|---|
| - | - | - | 暂无可靠参数 | - |

## 优缺点与替代

### 优点
- 可获得全局最优
- 求解器成熟
- 解释性较强

### 局限
- 要求线性
- 整数决策需扩展为 MILP
- 对参数误差可能敏感

### 可替代模型
- Integer Programming
- Nonlinear Programming

### 常见组合
- Sensitivity Analysis
- Scenario Analysis

## 求解算法

论文未明确指定求解算法。

## 复杂度与验证

- 时间复杂度：`problem-dependent`
- 空间复杂度：`O(mn)`
- 说明：单纯形法最坏指数级，内点法有多项式界
- 推荐验证：可行性检查；对偶/松弛分析；参数敏感性

## 来源论文

- [[基于随机优化的农作物种植策略模型]]：证据 E-TEXT-P022-1fb065b390

## 当前论文证据

> [!quote] E-TEXT-P022-1fb065b390 · p.22 · 基于随机优化的农作物种植策略模型
> 灾霁求等多种回素 , 构建了线性规划和随机优化模型、 通过求解器和责心算法两种方法 , 能够在有限土
<!-- MM:END AUTO -->

## 我的补充

在这里补充你自己的理解、比赛经验、参数选择与踩坑记录。
