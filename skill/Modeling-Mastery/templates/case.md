# {{ case.title }}：建模案例

- 来源论文：{{ paper_note | wikilink }}
- 领域：`{{ case.domain }}`
- 竞赛：{{ case.competition or "未识别" }}
- 年份：{{ case.year if case.year else "未识别" }}
- 题号：{{ case.problem_id or "未识别" }}
- 奖项：{{ case.award or "未识别" }}

## Problem Fingerprint

- 问题类型：{{ case.problem_fingerprint.problem_types | join("、") if case.problem_fingerprint.problem_types else "未标注" }}
- 数据类型：{{ case.problem_fingerprint.data_types | join("、") if case.problem_fingerprint.data_types else "未标注" }}
- 目标：{{ case.problem_fingerprint.targets | join("、") if case.problem_fingerprint.targets else "未标注" }}
- 约束：{{ case.problem_fingerprint.constraints | join("；") if case.problem_fingerprint.constraints else "未标注" }}
- 领域关键词：{{ case.problem_fingerprint.domain_keywords | join("、") if case.problem_fingerprint.domain_keywords else "未标注" }}

## 子问题—模型—算法映射

{% for item in case.subproblem_mapping %}
### {{ item.subproblem_id }}：{{ item.task }}

- 模型：{{ item.model_ids | code_join }}
- 算法：{{ item.algorithm_ids | code_join }}
- 数据流：{{ item.data_flow or "未说明" }}
- 选择理由：{{ item.rationale or "未说明" }}
- 证据：{{ item.evidence_ids | join(", ") if item.evidence_ids else "未锚定" }}
{% endfor %}

## 结果

{{ case.results | md_list }}

## 可迁移经验

{{ case.transferable_insights | md_list }}

## 创新点

{{ case.innovations | md_list }}

## 易踩坑

{{ case.pitfalls | md_list }}
