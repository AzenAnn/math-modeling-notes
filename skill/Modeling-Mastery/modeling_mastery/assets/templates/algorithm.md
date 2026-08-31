# {{ algorithm.canonical_name }}

> [!abstract] 用途
> {{ algorithm.purpose }}

## 基本属性

- 分类：`{{ algorithm.category }}`
- 来源等级：`{{ algorithm.provenance }}`
- 置信度：{{ "%.0f%%" | format(algorithm.confidence * 100) }}
- 输入：{{ algorithm.inputs | join("、") if algorithm.inputs else "未明确" }}
- 输出：{{ algorithm.outputs | join("、") if algorithm.outputs else "未明确" }}

## 伪代码

```text
{% for step in algorithm.pseudocode %}
{{ loop.index }}. {{ step }}
{% endfor %}
```

## 初始化与停止条件

- 初始化：{{ algorithm.initialization or "论文未说明" }}
- 停止条件：{{ algorithm.stopping_criteria | join("；") if algorithm.stopping_criteria else "论文未说明" }}

## 参数

| 参数 | 值 | 范围 | 说明 | 来源 |
|---|---|---|---|---|
{% for parameter in algorithm.parameters %}
| `{{ parameter.name }}` | {{ parameter.value if parameter.value is not none else "论文未说明" }} | {{ parameter.range or "-" }} | {{ parameter.description or "-" }} | {{ parameter.provenance }} |
{% else %}
| - | - | - | 暂无可靠参数 | - |
{% endfor %}

## 复杂度

- 时间：`{{ algorithm.complexity.time }}`
- 空间：`{{ algorithm.complexity.space }}`
- 说明：{{ algorithm.complexity.notes or "无" }}

## 随机性与复现

- 使用随机性：{{ "是" if algorithm.randomness.uses_randomness else "否" }}
- 必须固定 seed：{{ "是" if algorithm.randomness.seed_required else "否" }}
- 说明：{{ algorithm.randomness.notes or "无" }}

## 实现要点

{{ algorithm.implementation_notes | md_list }}

## 常见失败模式

{{ algorithm.failure_modes | md_list }}

## 来源论文

{% for source in sources %}
- {{ source.title | wikilink }}：证据 {{ source.evidence_ids | join(", ") if source.evidence_ids else "未锚定" }}
{% endfor %}

## 当前论文证据

{% for item in evidence %}
> [!quote] {{ item.id }} · p.{{ item.page if item.page else "?" }} · {{ item.section or "未标章节" }}
> {{ item.quote }}
{% else %}
暂无当前论文证据。
{% endfor %}
