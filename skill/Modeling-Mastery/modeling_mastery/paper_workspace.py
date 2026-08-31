from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .constants import AUTO_BEGIN, AUTO_END, REGISTRY_DIR, VAULT_FOLDERS
from .io_utils import atomic_write_text, relative_posix, safe_filename

PAPER_LIBRARY_DIR = "论文"
KNOWLEDGE_VAULT_DIR = "知识库"
WORKFLOW_DIR = "workflow"
SUPPLEMENT_DIR = "补充笔记"


@dataclass(frozen=True)
class PaperWorkspace:
    library_root: Path
    paper_library: Path
    paper_root: Path
    workflow: Path
    knowledge_vault: Path
    supplements: Path
    assets: Path

    def as_dict(self) -> dict[str, str]:
        return {
            "library_root": str(self.library_root),
            "paper_library": str(self.paper_library),
            "paper_root": str(self.paper_root),
            "workflow": str(self.workflow),
            "knowledge_vault": str(self.knowledge_vault),
            "supplements": str(self.supplements),
            "assets": str(self.assets),
        }


def _replace_or_append_auto_block(
    path: Path,
    generated: str,
    *,
    default_manual: str,
    append_if_unmanaged: bool = False,
) -> None:
    block = f"{AUTO_BEGIN}\n{generated.strip()}\n{AUTO_END}"
    if not path.exists():
        atomic_write_text(path, f"{block}\n\n{default_manual.strip()}\n")
        return

    current = path.read_text(encoding="utf-8", errors="replace")
    if AUTO_BEGIN in current and AUTO_END in current:
        prefix, remainder = current.split(AUTO_BEGIN, 1)
        _, suffix = remainder.split(AUTO_END, 1)
        updated = f"{prefix.rstrip()}\n\n{block}{suffix}"
    elif not append_if_unmanaged:
        return
    else:
        updated = f"{current.rstrip()}\n\n{block}\n"
    atomic_write_text(path, updated.lstrip("\n"))


def _paper_readme(title: str) -> str:
    return f"""# {title}

本目录是一篇论文的独立解读工作区。自动流程与人工笔记按职责分开，避免在上层笔记库散落文件。

## 固定目录

- `workflow/`：解析正文、页码映射、Paper IR、代码与运行报告。
- `知识库/`：由 Paper IR 幂等生成的 Paper、Case、Model、Algorithm、Code 卡片与索引。
- `补充笔记/模型/`：人工补充或二次整理的模型笔记。
- `补充笔记/算法/`：人工补充或二次整理的算法笔记。
- `assets/`：不属于自动知识库的论文级素材。

不要把 `00_Home`、`10_Models` 等知识库目录直接写到上层仓库根目录。"""


def _library_index(paper_library: Path) -> str:
    paper_names = sorted(
        path.name
        for path in paper_library.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )
    lines = ["# 论文", "", "每篇论文使用一个同名独立工作区："]
    if paper_names:
        lines.extend(["", *[f"- [[论文/{name}/README|{name}]]" for name in paper_names]])
    else:
        lines.extend(["", "暂无论文工作区。"])
    return "\n".join(lines)


def initialize_paper_workspace(library_root: Path, paper_title: str) -> PaperWorkspace:
    """Create the canonical per-paper layout without overwriting manual content."""
    title = paper_title.strip()
    if not title:
        raise ValueError("paper_title must not be empty")

    library_root = library_root.expanduser().resolve()
    paper_library = library_root / PAPER_LIBRARY_DIR
    paper_root = paper_library / safe_filename(title, fallback="未命名论文")
    workflow = paper_root / WORKFLOW_DIR
    knowledge_vault = paper_root / KNOWLEDGE_VAULT_DIR
    supplements = paper_root / SUPPLEMENT_DIR
    assets = paper_root / "assets"

    directories = [
        paper_library,
        paper_root,
        workflow / "parsed",
        workflow / "ir",
        workflow / "code",
        workflow / "reports",
        knowledge_vault / REGISTRY_DIR,
        supplements / "模型",
        supplements / "算法",
        assets,
    ]
    directories.extend(knowledge_vault / folder for folder in VAULT_FOLDERS.values())
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

    _replace_or_append_auto_block(
        paper_root / "README.md",
        _paper_readme(title),
        default_manual="## 人工补充\n\n在这里记录本论文工作区的人工维护说明。",
    )
    _replace_or_append_auto_block(
        paper_library / "README.md",
        _library_index(paper_library),
        default_manual="## 人工补充\n\n在这里维护论文库的人工分类与阅读计划。",
        append_if_unmanaged=True,
    )

    return PaperWorkspace(
        library_root=library_root,
        paper_library=paper_library,
        paper_root=paper_root,
        workflow=workflow,
        knowledge_vault=knowledge_vault,
        supplements=supplements,
        assets=assets,
    )


def workspace_report(layout: PaperWorkspace) -> dict[str, Any]:
    data: dict[str, Any] = layout.as_dict()
    data["relative_paper_root"] = relative_posix(layout.paper_root, layout.library_root)
    data["layout_version"] = "1.0"
    return data
