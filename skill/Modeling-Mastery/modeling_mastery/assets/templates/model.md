# {{ model.canonical_name }}

> [!abstract] 一句话说明
> {{ model.description }}

## 适用定位

- 分类：`{{ model.category }}`
- 任务：{{ model.task_types | join("、") if model.task_types else "未标注" }}
- 在论文中的作用：{{ model.role or "未说明" }}
- 来源等级：`{{ model.provenance }}`，置信度 {{ "%.0f%%" | format(model.confidence * 100) }}

### 适合使用

{{ model.use_when | md_list }}

### 不适合或慎用

{{ model.avoid_when | md_list }}

## 输入与输出

### 输入

{% for item in model.inputs %}
- **{{ item.name }}**：{{ item.description }}{{ "；shape=`" ~ item.shape ~ "`" if item.shape else "" }}{{ "；单位=" ~ item.unit if item.unit else "" }}
{% else %}
暂无可靠输入契约。
{% endfor %}

### 输出

{% for item in model.outputs %}
- **{{ item.name }}**：{{ item.description }}{{ "；shape=`" ~ item.shape ~ "`" if item.shape else "" }}{{ "；单位=" ~ item.unit if item.unit else "" }}
{% else %}
暂无可靠输出契约。
{% endfor %}

## 数学表达

{% for equation in model.equations %}
### {{ equation.label or ("公式 " ~ loop.index) }}

$$
{{ equation.latex }}
$$

{{ equation.explanation }}  
来源：`{{ equation.provenance }}`；证据：{{ equation.evidence_ids | join(", ") if equation.evidence_ids else "未锚定" }}。
{% else %}
论文或抽取结果中没有可靠公式。
{% endfor %}

## 建模步骤

{% for step in model.workflow %}
{{ step.order }}. **{{ step.name }}**：{{ step.description }}  
   输入：{{ step.inputs | join("、") if step.inputs else "-" }}；输出：{{ step.outputs | join("、") if step.outputs else "-" }}；证据：{{ step.evidence_ids | join(", ") if step.evidence_ids else "未锚定" }}。
{% endfor %}

## 参数

| 参数 | 值 | 范围 | 说明 | 来源 |
|---|---|---|---|---|
{% for parameter in model.parameters %}
| `{{ parameter.name }}` | {{ parameter.value if parameter.value is not none else "论文未说明" }} | {{ parameter.range or "-" }} | {{ parameter.description or "-" }} | {{ parameter.provenance }} |
{% else %}
| - | - | - | 暂无可靠参数 | - |
{% endfor %}

## 优缺点与替代

### 优点
{{ model.strengths | md_list }}

### 局限
{{ model.weaknesses | md_list }}

### 可替代模型
{{ model.alternatives | md_list }}

### 常见组合
{% for name in model.combinations %}
{% if name in known_model_names %}
- {{ name | wikilink }}
{% else %}
- {{ name }}
{% endif %}
{% else %}
暂无。
{% endfor %}

## 求解算法

{% for algorithm_id in model.solver_algorithm_ids %}
- `{{ algorithm_id }}`
{% else %}
论文未明确指定求解算法。
{% endfor %}

## 复杂度与验证

- 时间复杂度：`{{ model.complexity.time }}`
- 空间复杂度：`{{ model.complexity.space }}`
- 说明：{{ model.complexity.notes or "无" }}
- 推荐验证：{{ model.validation_methods | join("；") if model.validation_methods else "需按任务设计" }}

## 来源论文

{% for source in sources %}
- {{ source.title | wikilink }}：证据 {{ source.evidence_ids | join(", ") if source.evidence_ids else "未锚定" }}
{% endfor %}

## 当前论文证据

{% for item in evidence %}
> [!quote] {{ item.id }} · p.{{ item.page if item.page else "?" }} · {{ item.section or "未标章节" }}
> {{ item.quote }}
{% else %}
暂无当前论文证据；仅可作为参考知识，不能声称来自该论文。
{% endfor %}
