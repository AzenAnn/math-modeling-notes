# Modeling-Mastery 首页

> [!tip] 使用方式
> 赛前通过论文持续建库；赛时先把题目转成 Problem Fingerprint，再检索模型、算法、案例和代码卡。

## 知识库统计

- 论文：{{ registry.papers | length }}
- 模型：{{ registry.models | length }}
- 算法：{{ registry.algorithms | length }}
- 案例：{{ registry.cases | length }}
- 代码配方：{{ registry.codes | length }}
- 最近更新：{{ registry.updated_at }}

## 模型

{% for model_id, entry in registry.models.items() %}
- {{ entry.card.canonical_name | wikilink }}：`{{ entry.card.category }}`，来源论文 {{ entry.sources | length }} 篇
{% else %}
暂无模型。
{% endfor %}

## 算法

{% for algorithm_id, entry in registry.algorithms.items() %}
- {{ entry.card.canonical_name | wikilink }}：`{{ entry.card.category }}`，来源论文 {{ entry.sources | length }} 篇
{% else %}
暂无算法。
{% endfor %}

## 论文

{% for paper_id, entry in registry.papers.items() %}
- {{ entry.ir.bibliographic.title | wikilink }}
{% else %}
暂无论文。
{% endfor %}

## 本地索引

- JSON：`{{ index_json }}`
- SQLite：`{{ index_db }}`

运行：

```bash
python scripts/build_index.py <vault>
python scripts/retrieve_models.py <vault> "多指标综合评价 客观赋权 排序" --type model
```
