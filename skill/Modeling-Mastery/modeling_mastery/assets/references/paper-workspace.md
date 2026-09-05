# 单篇论文工作区整理规范

## 路径契约

单篇论文的唯一项目根目录是：

```text
<library-root>/论文/<论文正式题目>/
```

先从封面、标题页、用户输入或有效 Paper IR 确定正式题目，再初始化目录。不得在已经能够识别题目时使用 `A196`、哈希值或临时 workspace 名称代替。

固定职责：

- `workflow/parsed/`：规范化正文、页码映射、结构 JSON 和解析图片。
- `workflow/ir/`：证据包、原始 IR、规范化 IR 和报告。
- `workflow/code/`、`workflow/reports/`：复现代码与流水线报告。
- `知识库/`：Paper、Case、Model、Algorithm、Code 卡片、Vault 资产、注册表与索引。
- `补充笔记/模型/`、`补充笔记/算法/`：人工二次整理，自动流程不得覆盖。
- `assets/`：不属于自动 Vault 的论文级素材。
- `解读.md`、`paper.md`、`translation_notes.md`、`source_map.json`：按实际任务创建，不制造空占位文件。

## 命令

```bash
python scripts/init_paper_workspace.py <library-root> --title "<论文题目>"

python -m modeling_mastery skill-run <paper.pdf> \
  --agent auto \
  --library-root <library-root> \
  --paper-title "<论文题目>"

python scripts/write_obsidian.py <paper_ir.json> --library-root <library-root>
```

`--library-root` 模式自动使用 `论文/<论文题目>/workflow` 与 `论文/<论文题目>/知识库`，不得再组合 `--workspace` 或 `--vault`。只有用户明确要求多篇论文写入同一共享 Vault 时，才使用兼容的独立 `--workspace` + `--vault` 模式。

## 幂等与链接

1. 自动内容由 `<!-- MM:BEGIN AUTO -->` 与 `<!-- MM:END AUTO -->` 包围；重跑保留标记外人工内容和用户 frontmatter。
2. `论文/README.md` 维护论文目录索引，更新时保留人工内容。
3. 嵌套知识库的图片与代码路径必须相对上层 Obsidian 根目录。例如：

```text
![[论文/<论文题目>/知识库/_assets/<paper_id>/figures/<图片>]]
```

4. 移动既有产物后重建 Registry/JSON/SQLite 索引，扫描旧绝对路径、旧相对路径与失效 Wikilink。

## 验收

- `paper_ir.json` 位于 `workflow/ir/` 且通过 Schema 校验。
- `知识库/.modeling-mastery/registry.json`、`index.json` 与索引数据库存在。
- 去重扫描已运行；模糊重复只报告，不自动删除。
- 上层根目录没有本次新增的 `00_Home`、`10_Models`、`workspaces`、`parsed` 或 `ir` 等散落目录。
- Markdown 链接、Wikilink、图片嵌入和记录的源路径均可解析。
- 第二次运行不会产生重复论文目录，也不会丢失人工补充。
