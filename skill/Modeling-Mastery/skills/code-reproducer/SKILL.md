---
name: code-reproducer
description: 根据带 Evidence ID 的模型/算法卡生成 Python、MATLAB 和 pytest，实现论文算法并做静态安全检查、超时测试与复现报告；用户明确要求代码实现或比赛代码模板时使用。
license: MIT
metadata:
  version: 0.2.0
---

# 05 Code Reproducer

参数：`$ARGUMENTS`

## 执行

```bash
python scripts/reproduce_code.py <paper_ir.json> \
  --output <workspace>/code \
  --updated-ir <workspace>/ir/paper_ir.with_code.json
```

## 生成要求

每个目标目录至少包含：

```text
<target>/
├── python/implementation.py
├── matlab/implementation.m
├── tests/test_implementation.py
├── code.json
├── validation.json
└── README.md
```

代码必须：

- 以函数为入口；不读写任意文件，不联网，不执行系统命令。
- 注释包含 `Source evidence: E-...`。
- 随机算法暴露 seed。
- 将未给出的论文细节变成参数，并写入 assumptions/limitations。
- pytest 包含正常、边界和数值/性质检查。

## 安全门禁

```bash
python scripts/validate_code.py <implementation.py>
python scripts/run_code.py <target-directory>
```

静态检查失败时不执行。即使测试通过，也要把代码状态视为“已通过当前样例”，而不是“完全复现论文”。
