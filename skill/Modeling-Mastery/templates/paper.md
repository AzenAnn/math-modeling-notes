# {{ paper.title }}

> [!summary] 论文摘要
> {{ paper.abstract or "论文未提供可可靠抽取的摘要。" }}

## 基本信息

| 字段 | 内容 |
|---|---|
| 作者 | {{ paper.authors | join("、") if paper.authors else "未识别" }} |
| 年份 | {{ paper.year if paper.year else "未识别" }} |
| 竞赛 | {{ paper.competition or "未识别" }} |
| 奖项 | {{ paper.award or "未识别" }} |
| 题号 | {{ paper.problem_id or "未识别" }} |
| IR | `{{ ir.paper_id }}` |
| 解析器 | `{{ ir.source.parser }}` |

## 问题重述与拆分

**总体目标：** {{ ir.problem.overall_objective or "需要人工补全" }}

{% for subproblem in ir.problem.subproblems %}
### {{ subproblem.id }}

{{ subproblem.statement }}

- 任务类型：{{ subproblem.task_types | join("、") }}
- 输入：{{ subproblem.inputs | join("、") if subproblem.inputs else "未明确" }}
- 输出：{{ subproblem.outputs | join("、") if subproblem.outputs else "未明确" }}
- 约束：{{ subproblem.constraints | join("；") if subproblem.constraints else "未明确" }}
{% endfor %}

## 建模链

{% for step in ir.modeling_chain %}
{{ step.order }}. **{{ step.subproblem_id }} → {{ step.model_id }}**：{{ step.rationale or "论文未详细说明选择理由" }}  
   输入：{{ step.input or "未明确" }}；输出：{{ step.output or "未明确" }}；算法：{{ step.algorithm_ids | join("、") if step.algorithm_ids else "未指定" }}。
{% else %}
暂无可确认的建模链。
{% endfor %}

## 模型卡

{% for model in models %}
- {{ model.canonical_name | wikilink }}：{{ model.role or model.description }} `{{ model.provenance }}`
{% else %}
- 暂无可靠模型识别结果。
{% endfor %}

## 算法卡

{% for algorithm in algorithms %}
- {{ algorithm.canonical_name | wikilink }}：{{ algorithm.purpose }} `{{ algorithm.provenance }}`
{% else %}
- 暂无可靠算法识别结果。
{% endfor %}

## 假设

{% for item in ir.assumptions %}
- **{{ item.id }}** {{ item.statement }}  
  理由：{{ item.rationale or "未说明" }}；来源：`{{ item.provenance }}`；证据：{{ item.evidence_ids | join(", ") if item.evidence_ids else "无" }}。
{% else %}
暂无可靠抽取的假设。
{% endfor %}

## 变量与符号

| 符号 | 含义 | 单位 | 类型 | 来源 |
|---|---|---|---|---|
{% for variable in ir.variables %}
| `{{ variable.symbol }}` | {{ variable.meaning }} | {{ variable.unit or "-" }} | {{ variable.data_type }} | {{ variable.provenance }} |
{% else %}
| - | 暂无可靠变量表 | - | - | - |
{% endfor %}

## 数据处理

- 数据来源：{{ ir.data.sources | join("；") if ir.data.sources else "未识别" }}
- 字段：{{ ir.data.fields | join("、") if ir.data.fields else "未识别" }}
- 预处理：{{ ir.data.preprocessing | join("；") if ir.data.preprocessing else "未识别" }}
- 缺失值：{{ ir.data.missing_value_strategy or "未识别" }}
- 异常值：{{ ir.data.outlier_strategy or "未识别" }}

## 验证与结果

- 方法：{{ ir.validation.methods | join("；") if ir.validation.methods else "未识别" }}
- 指标：{{ ir.validation.metrics | join("、") if ir.validation.metrics else "未识别" }}
- 结果：{{ ir.validation.results | join("；") if ir.validation.results else "未识别" }}
- 灵敏度分析：{{ ir.validation.sensitivity_analysis | join("；") if ir.validation.sensitivity_analysis else "未识别" }}
- 鲁棒性检查：{{ ir.validation.robustness_checks | join("；") if ir.validation.robustness_checks else "未识别" }}

## 创新与局限

### 创新

{{ ir.innovations | md_list }}

### 局限

{{ ir.limitations | md_list }}

## 图片资产

{% for figure in figures %}
### {{ figure.id or loop.index }}

{{ figure.embed }}

- 页码：{{ figure.page if figure.page else "未知" }}
- 来源：{{ figure.source or "parser" }}
{% else %}
未提取到可嵌入的图片资产。
{% endfor %}

## 证据目录

| Evidence ID | 页码 | 类型 | Section | 原文 |
|---|---:|---|---|---|
{% for item in evidence %}
| `{{ item.id }}` | {{ item.page if item.page else "?" }} | {{ item.kind }} | {{ item.section or "-" }} | {{ item.quote | replace("|", "\\|") }} |
{% else %}
| - | - | - | - | 暂无证据锚点 |
{% endfor %}

## 质量门禁

- 证据覆盖率：{{ "%.1f%%" | format(ir.quality.evidence_coverage * 100) }}
- 完整度：{{ "%.1f%%" | format(ir.quality.completeness * 100) }}
- 代码可复现度：{{ "%.1f%%" | format(ir.quality.code_reproducibility * 100) }}
- 必须人工复核：{{ "是" if ir.quality.review_required else "否" }}

{% for warning in ir.quality.warnings %}
> [!warning] {{ warning }}
{% endfor %}
