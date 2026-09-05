---
type: model
id: model-montecarlosimulation-748bbc93bd
canonical_name: Monte Carlo Simulation
aliases:
- 蒙特卡洛模拟
- Monte Carlo Method
- 随机模拟
category: simulation
tasks:
- uncertainty_propagation
- scenario_analysis
- probability_estimation
source_papers:
- 基于蚁群算法与遗传算法优化的蒙特卡洛模拟在生产决策优化中的应用研究
provenance: HEURISTIC
confidence: 0.58
tags:
- mm/model
- mm/model/simulation
- mm/task/uncertainty_propagation
- mm/task/scenario_analysis
- mm/task/probability_estimation
updated_at: '2026-09-04T18:08:23+00:00'
---

<!-- MM:BEGIN AUTO -->
# Monte Carlo Simulation

> [!abstract] 一句话说明
> 由参考目录识别，需结合论文证据复核。

## 适用定位

- 分类：`simulation`
- 任务：uncertainty_propagation、scenario_analysis、probability_estimation
- 在论文中的作用：通过重复随机采样近似复杂系统的分布、概率或期望
- 来源等级：`HEURISTIC`，置信度 58%

### 适合使用

- 解析求解困难
- 输入具有不确定性
- 关注风险或概率

### 不适合或慎用

- 随机输入分布完全无法合理设定
- 单次仿真极其昂贵且无代理模型

## 输入与输出

### 输入

暂无可靠输入契约。

### 输出

暂无可靠输出契约。

## 数学表达

论文或抽取结果中没有可靠公式。

## 建模步骤

1. **定义随机输入和联合分布**：定义随机输入和联合分布  
   输入：-；输出：-；证据：E-TEXT-P001-e329849700。
2. **明确输出指标与事件**：明确输出指标与事件  
   输入：-；输出：-；证据：E-TEXT-P001-e329849700。
3. **固定随机种子并生成样本**：固定随机种子并生成样本  
   输入：-；输出：-；证据：E-TEXT-P001-e329849700。
4. **对每个样本运行模型**：对每个样本运行模型  
   输入：-；输出：-；证据：E-TEXT-P001-e329849700。
5. **统计均值、方差、分位数和置信区间**：统计均值、方差、分位数和置信区间  
   输入：-；输出：-；证据：E-TEXT-P001-e329849700。
6. **检查样本量收敛与分布假设敏感性**：检查样本量收敛与分布假设敏感性  
   输入：-；输出：-；证据：E-TEXT-P001-e329849700。

## 参数

| 参数 | 值 | 范围 | 说明 | 来源 |
|---|---|---|---|---|
| - | - | - | 暂无可靠参数 | - |

## 优缺点与替代

### 优点
- 适用复杂非线性系统
- 实现灵活
- 易并行

### 局限
- 收敛速度通常为 O(N^-1/2)
- 结果依赖分布假设
- 计算量可能大

### 可替代模型
- Latin Hypercube Sampling
- Quasi-Monte Carlo
- Bootstrap

### 常见组合
- Sensitivity Analysis
- Surrogate Model

## 求解算法

论文未明确指定求解算法。

## 复杂度与验证

- 时间复杂度：`O(N·C_f)`
- 空间复杂度：`O(N) or streaming O(1)`
- 说明：N 为样本数
- 推荐验证：重复 seed；样本量收敛；置信区间；分布敏感性

## 来源论文

- [[基于蚁群算法与遗传算法优化的蒙特卡洛模拟在生产决策优化中的应用研究]]：证据 E-TEXT-P001-e329849700

## 当前论文证据

> [!quote] E-TEXT-P001-e329849700 · p.1 · 基于蚁群算法与遗传算法优化的蒙特卡洛模拟在生产决策优化中的应用研究
> 提高求解效率和解的质量 , 我们引入了蚁群算法对蒙特卡洛模拟进行优化 , 通过信息
<!-- MM:END AUTO -->

## 我的补充

在这里补充你自己的理解、比赛经验、参数选择与踩坑记录。
