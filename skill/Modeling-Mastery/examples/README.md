# Examples

- `demo_paper/source_paper.md`：带 3 个页码标记的输入论文。
- `demo_paper/` 的其余文件：Paper Ingest、结构化证据和离线启发式生成的有效 `paper_ir.json`。
- `demo_code/topsis/`：可直接运行的 Python 与 MATLAB TOPSIS 代码；Python 附带 pytest。

验证示例 IR：

```bash
python scripts/validate_ir.py examples/demo_paper/paper_ir.json
```

运行示例代码测试：

```bash
PYTHONPATH=examples/demo_code/topsis/python \
python -m pytest examples/demo_code/topsis/tests
```

从示例论文创建临时 Vault：

```bash
modeling-mastery pipeline examples/demo_paper/source_paper.md \
  --workspace ./workspaces/example \
  --vault ./examples/generated_vault \
  --provider none
```
