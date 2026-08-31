# 单篇论文工作区整理规范

## 1. 目标

每篇论文的自动产物、人工解读、补充笔记和局部知识库必须收拢在一个以论文正式题目命名的目录中。上层笔记库只承担论文索引和其他主题笔记，不直接承载某篇论文生成的 `00_Home`、`10_Models` 等目录。

规范路径为：

```text
<library-root>/论文/<论文题目>/
```

论文题目需先经过文件名安全化，Windows 禁止字符会替换为连字符。不得用比赛提交编号、PDF 文件哈希或临时 workspace 名代替已经可以确认的正式题目。

## 2. 目录职责

```text
<论文题目>/
├── README.md
├── 解读.md
├── paper.md
├── translation_notes.md
├── source_map.json
├── assets/
├── workflow/
│   ├── parsed/
│   ├── ir/
│   ├── code/
│   └── reports/
├── 补充笔记/
│   ├── 模型/
│   └── 算法/
└── 知识库/
    ├── 00_Home/
    ├── 10_Models/
    ├── 20_Algorithms/
    ├── 30_Code-Recipes/
    ├── 40_Competition-Cases/
    ├── 50_Papers/
    ├── 60_Data-Processing/
    ├── 70_Visualization/
    ├── 80_Writing/
    ├── 90_Inbox/
    ├── _assets/
    └── .modeling-mastery/
```

- `workflow/` 只放可再生成的中间结果、代码和报告。
- `知识库/` 只放由 Paper IR 幂等生成的标准卡片、注册表和检索索引。
- `补充笔记/` 放人工判断、竞赛经验和不适合自动覆盖的模型/算法总结。
- `assets/` 放解读文档直接使用、但不属于自动 Vault `_assets` 的论文级素材。
- `解读.md`、`paper.md`、`translation_notes.md`、`source_map.json` 按任务需要创建，不要求制造空文件。

## 3. 推荐命令

先初始化目录：

```bash
modeling-mastery init-paper <library-root> --title "<论文题目>"
```

一次运行完整流程：

```bash
modeling-mastery skill-run <paper.pdf> \
  --agent auto \
  --library-root <library-root> \
  --paper-title "<论文题目>"
```

`pipeline` 命令也接受同样的 `--library-root` 与 `--paper-title`。这两个命令在工作区模式下不接受额外的 `--workspace` 或 `--vault`，以免再次把产物拆散。

已有 IR 重新蒸馏：

```bash
modeling-mastery distill <paper_ir.json> --library-root <library-root>
```

该命令直接使用 IR 中的正式题目创建或更新论文工作区。

## 4. 兼容的共享 Vault 模式

当用户明确要求多篇论文汇总到同一知识库时，可继续使用：

```bash
modeling-mastery pipeline <paper.pdf> --workspace <workspace> --vault <shared-vault>
```

共享模式是显式例外，不是单篇解读的默认布局。不要同时提供 `--library-root` 与 `--workspace`/`--vault`。

## 5. 幂等和链接规则

1. `README.md`、Paper/Model/Algorithm/Code 卡片中的自动区由 `<!-- MM:BEGIN AUTO -->` 与 `<!-- MM:END AUTO -->` 标记。
2. 重跑可以替换自动区，不得覆盖标记外的人工内容和用户 frontmatter。
3. `论文/README.md` 自动维护论文工作区索引；已有人工内容保留。
4. 如果 `知识库` 是上层 Obsidian Vault 的子目录，图片和代码资产链接使用从上层根目录开始的路径，例如：

```text
![[论文/<论文题目>/知识库/_assets/<paper_id>/figures/<图片>]]
```

5. 迁移已有产物后，必须重建 `知识库/.modeling-mastery/index.json` 和 SQLite 索引，并检查旧绝对路径、旧相对路径与失效 Wikilink。

## 6. 完成验收

至少确认：

- 论文题目目录存在，且 `workflow/`、`知识库/`、`补充笔记/` 职责分离。
- `paper_ir.json` 位于 `workflow/ir/` 并通过 Schema 校验。
- `知识库/.modeling-mastery/registry.json`、`index.json` 和索引数据库存在。
- 去重扫描已运行，模糊重复仅报告、不自动删除。
- 上层根目录没有本次新建的 `00_Home`、`10_Models`、`workspaces`、`parsed`、`ir` 等散落目录。
- 所有 Markdown 链接、Wikilink、图片嵌入和记录的源路径均可解析。
- 再运行一次不会生成重复论文目录，也不会丢失人工补充。
