# Obsidian Vault 设计

单篇论文默认把这里描述的 Vault 放在 `<上层笔记库>/论文/<论文题目>/知识库/`，而不是直接放在上层笔记库根目录。完整整理规则见 [`paper-workspace.md`](paper-workspace.md)。多篇论文明确要求共享建库时，才把该结构作为独立共享 Vault 使用。

## 1. 目录

```text
00_Home/                  MOC 与入口
10_Models/<category>/     模型卡
20_Algorithms/<category>/ 算法卡
30_Code-Recipes/<lang>/   代码卡
40_Competition-Cases/     赛题案例卡
50_Papers/                论文总览
60_Data-Processing/       预留
70_Visualization/         预留
80_Writing/               预留
90_Inbox/                 人工待整理
_assets/<paper_id>/        图片和代码副本
.modeling-mastery/         registry、index、报告
```

## 2. 自动区与人工区

每个笔记采用：

```markdown
<!-- MM:BEGIN AUTO -->
自动生成区
<!-- MM:END AUTO -->

## 我的补充
人工内容
```

重复导入时只更新自动区。自动区之后的人工内容与非系统 Frontmatter 字段会保留。

## 3. canonical 合并

模型文件名由 `canonical_name` 决定。别名例如“优劣解距离法”“逼近理想解排序法”会归一到 `TOPSIS.md`。新论文再次使用 TOPSIS 时，Registry 会累加来源论文和证据，而不是创建重复文件。

## 4. Registry

`.modeling-mastery/registry.json` 保存：

- 每篇论文的完整 IR。
- 合并后的 Model / Algorithm Card。
- 资产来源与 Evidence IDs。
- Case 和 Code Recipe。

Registry 是增量写入的状态文件；建议纳入 Git，但不要手工大规模编辑。

## 5. 索引

`build_index` 产生：

- `index.json`：便于调试与自定义检索。
- `modeling_index.sqlite3`：FTS5 可用时建立全文索引，否则回退普通表。

当前检索先做 type/category/task 过滤，再结合中文字符/二元片段与英文 token 计算词项分数，并加上问题指纹、别名和标题命中奖励。

## 6. 推荐 Obsidian 插件

项目本身不强依赖插件。可选：

- Dataview：按 YAML 生成模型矩阵。
- Templater：手工新建扩展笔记。
- Git：版本控制 Vault。
- Omnisearch：交互式全文搜索。

这些插件不是流水线运行条件。
