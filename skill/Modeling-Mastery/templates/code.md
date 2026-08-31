# {{ recipe.target_name }} · {{ recipe.language }}

> [!warning] 运行边界
> 这是自动复现代码。先核对 `source_anchors`、`AI_INFERRED` 参数与验证状态，再在隔离环境中使用。

## 元数据

| 字段 | 内容 |
|---|---|
| Target | `{{ recipe.target_id }}` |
| 类型 | `{{ recipe.target_type }}` |
| 语言 | `{{ recipe.language }}` |
| 入口 | `{{ recipe.entrypoint }}` |
| 变体 | `{{ recipe.variant }}` |
| 验证状态 | `{{ recipe.validation_status }}` |
| 生成器 | `{{ recipe.generated_by }}` |
| 代码文件 | `{{ recipe.vault_code_path or recipe.path }}` |

## 输入契约

{{ recipe.input_contract | md_list }}

## 输出契约

{{ recipe.output_contract | md_list }}

## 依赖

{{ recipe.dependencies | md_list }}

## 证据锚点

{% for anchor in recipe.source_anchors %}
- `{{ anchor.evidence_id }}`：{{ anchor.relationship }}；来源 `{{ anchor.provenance }}`
{% endfor %}

## AI 补全假设

{{ recipe.assumptions | md_list }}

## 测试结果

| 名称 | 类型 | 状态 | 说明 |
|---|---|---|---|
{% for test in recipe.tests %}
| {{ test.name }} | {{ test.kind }} | `{{ test.status }}` | {{ test.details | replace("|", "\\|") | replace("\n", " ") }} |
{% endfor %}

## 代码

{% if source_code %}
```{{ "python" if recipe.language == "python" else "matlab" }}
{{ source_code.rstrip() }}
```
{% else %}
代码文件不存在或尚未复制，请查看原始路径：`{{ recipe.path }}`。
{% endif %}

## 局限

{{ recipe.limitations | md_list }}
