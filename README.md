# 数学建模笔记仓库

这是一个由三名队员共同维护的数学建模知识库，用于整理和共享：

- 算法笔记与实现
- 数学建模方法与模型
- Python、MATLAB 等可复用代码
- 数学建模比赛的题目、数据、结果和论文
- 论文、书籍和其他参考资料

## 目录结构

```text
数学建模仓库/
├─ 算法/
├─ 模型/
├─ 代码/
│  ├─ Python/
│  └─ MATLAB/
├─ 比赛/
├─ 资料/
└─ 论文/
   └─ <论文题目>/
```

## 笔记索引

- [多情形下无人机烟幕遮蔽策略的建模与优化研究](论文/多情形下无人机烟幕遮蔽策略的建模与优化研究/README.md)

## 首次上传到 GitHub

当前文件夹还没有初始化为 Git 仓库时，只需执行一次下列操作。请将 `<GitHub 仓库地址>` 替换为实际地址。

```bash
git init
git branch -M main
git remote add origin <GitHub 仓库地址>
git add -A
git commit -m "docs: 初始化数学建模仓库"
git push -u origin main
```

## 提交当前的所有更新

完成笔记或代码修改后，依次执行：

```bash
# 1. 查看当前变更
git status

# 2. 将新增、修改和删除的文件全部加入本次提交
git add -A

# 3. 创建本地提交，将引号中的内容改为本次更新说明
git commit -m "docs: 更新遗传算法笔记"

# 4. 整合队友已经推送的更新
git pull --rebase origin main

# 5. 推送到 GitHub
git push origin main
```

`git add -A` 会包含当前仓库中的所有新增、修改和删除操作。

## 拉取远端仓库的最新内容

开始编辑前，建议先查看状态：

```bash
git status
```

如果没有尚未提交的修改，执行：

```bash
git pull --rebase origin main
```

如果已经有本地修改，建议先按上一节创建本地提交，再执行拉取命令。

## 协作约定

- 每次开始工作前先拉取远端最新内容。
- 一次提交尽量只处理一类内容。
- 提交说明要简洁、明确，例如 `docs: 补充 ARIMA 模型笔记`。
- 推送前再执行一次 `git status`，避免误传临时文件。
- 尽量不要同时修改同一篇笔记，以减少合并冲突。
