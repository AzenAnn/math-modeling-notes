# Contributing

1. 使用 Python 3.11+。
2. 新增字段时同步修改 `schemas/`、示例 IR、模板与测试。
3. 任何从论文抽取的事实都必须携带 `evidence_ids` 或明确标为 `AI_INFERRED`。
4. 生成代码不得绕过 `validate_code.py`；不可信代码应在容器或虚拟机中执行。
5. 模型名称必须经过 canonicalization，避免创建同义重复笔记。
6. 提交前运行 `pytest` 与 `ruff check modeling_mastery scripts tests`。
