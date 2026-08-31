---
name: vault-writer
description: 把 Paper IR 蒸馏为 Obsidian Paper、Case、Model、Algorithm、Code Notes，写入 YAML、Wikilink、Tag、资产、注册表和索引；用户要求保存到 Obsidian 或批量建数模知识库时使用。
license: MIT
metadata:
  version: 0.2.0
---

# 06 Knowledge Distiller + 07 Obsidian Writer

参数：`$ARGUMENTS`

## 执行

```bash
python scripts/write_obsidian.py <paper_ir.json> --library-root <上层笔记库>
```

默认写入 `<上层笔记库>/论文/<IR 中的论文题目>/知识库`，并初始化同级 `workflow/`、`补充笔记/` 与 `assets/`。不得把 `00_Home`、`10_Models` 等目录直接写到上层笔记库根目录。

只有用户明确要求多篇论文共用一个 Vault 时，才使用兼容模式：

```bash
python scripts/write_obsidian.py <paper_ir.json> --vault <shared-vault-path>
```

## 笔记类型

- Paper：论文整体、问题拆分、建模链、证据目录
- Case：Problem Fingerprint 和子问题—模型—算法映射
- Model：适用条件、数学表达、流程、优缺点、来源论文
- Algorithm：伪代码、参数、复杂度、随机性、失败模式
- Code：代码、输入输出契约、证据、测试与局限

## 幂等与用户内容保护

自动区间使用：

```text
<!-- MM:BEGIN AUTO -->
...
<!-- MM:END AUTO -->
```

只替换自动区间；`## 我的补充` 及用户自定义 frontmatter 字段必须保留。

写入后运行：

```bash
python scripts/deduplicate.py <vault>
python scripts/build_index.py <vault>
```

不自动删除模糊重复笔记；生成候选报告供人工确认。

如果 `知识库` 位于更上层的 Obsidian Vault 中，资产 Wikilink 必须从上层根目录开始，迁移或重写后需检查失效链接。
