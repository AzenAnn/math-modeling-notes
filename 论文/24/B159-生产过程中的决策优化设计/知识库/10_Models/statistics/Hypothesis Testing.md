---
type: model
id: model-hypothesistesting-cfe3d9969d
canonical_name: Hypothesis Testing
aliases:
- 假设检验
- 显著性检验
- statistical hypothesis test
category: statistics
tasks:
- hypothesis_testing
- inference
- comparison
source_papers:
- 生产过程中的决策优化设计
provenance: HEURISTIC
confidence: 0.58
tags:
- mm/model
- mm/model/statistics
- mm/task/hypothesis_testing
- mm/task/inference
- mm/task/comparison
updated_at: '2026-09-04T18:08:23+00:00'
---

<!-- MM:BEGIN AUTO -->
# Hypothesis Testing

> [!abstract] 一句话说明
> 由参考目录识别，需结合论文证据复核。

## 适用定位

- 分类：`statistics`
- 任务：hypothesis_testing、inference、comparison
- 在论文中的作用：在给定显著性水平下判断样本证据是否反对原假设
- 来源等级：`HEURISTIC`，置信度 58%

### 适合使用

- 需要比较群体或验证关系
- 有明确可检验假设

### 不适合或慎用

- 样本选择偏差严重
- 检验前提不满足且无稳健替代

## 输入与输出

### 输入

暂无可靠输入契约。

### 输出

暂无可靠输出契约。

## 数学表达

论文或抽取结果中没有可靠公式。

## 建模步骤

1. **定义原假设与备择假设**：定义原假设与备择假设  
   输入：-；输出：-；证据：E-TEXT-P001-1961bbddbc。
2. **选择与数据和假设匹配的检验统计量**：选择与数据和假设匹配的检验统计量  
   输入：-；输出：-；证据：E-TEXT-P001-1961bbddbc。
3. **检查独立性、分布和方差等前提**：检查独立性、分布和方差等前提  
   输入：-；输出：-；证据：E-TEXT-P001-1961bbddbc。
4. **计算统计量与 p 值或临界域**：计算统计量与 p 值或临界域  
   输入：-；输出：-；证据：E-TEXT-P001-1961bbddbc。
5. **报告效应量和置信区间**：报告效应量和置信区间  
   输入：-；输出：-；证据：E-TEXT-P001-1961bbddbc。

## 参数

| 参数 | 值 | 范围 | 说明 | 来源 |
|---|---|---|---|---|
| - | - | - | 暂无可靠参数 | - |

## 优缺点与替代

### 优点
- 统计推断框架清晰
- 可量化证据强度

### 局限
- p 值容易误读
- 多重比较和低检验功效会误导

### 可替代模型
- Bootstrap
- Permutation Test
- Bayesian Inference

### 常见组合
- Effect Size
- Confidence Interval
- Multiple Testing Correction

## 求解算法

论文未明确指定求解算法。

## 复杂度与验证

- 时间复杂度：`test-dependent`
- 空间复杂度：`O(n)`
- 说明：无
- 推荐验证：前提检验；效应量；检验功效；多重比较校正

## 来源论文

- [[生产过程中的决策优化设计]]：证据 E-TEXT-P001-1961bbddbc

## 当前论文证据

> [!quote] E-TEXT-P001-1961bbddbc · p.1 · 生产过程中的决策优化设计
> 用检测花销与假设检验效昂 ( 运用假设检验功效函数衡量 ) 之间相互制约的关系 , 建立决策函
<!-- MM:END AUTO -->

## 我的补充

在这里补充你自己的理解、比赛经验、参数选择与踩坑记录。
