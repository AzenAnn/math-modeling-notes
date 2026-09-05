from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console
from rich.table import Table

from .batch import run_batch
from .code_validation import validate_file
from .codegen import reproduce_code
from .config import Settings
from .dedup import scan_duplicates
from .doctor import doctor_report
from .document import parse_document
from .indexer import build_index
from .io_utils import find_project_root, read_json, write_json
from .ir_builder import build_paper_ir
from .llm import create_llm
from .logging_utils import configure_logging
from .normalizer import normalize_ir
from .paper_workspace import initialize_paper_workspace, workspace_report
from .pipeline import run_pipeline
from .retriever import search_index
from .runner import run_python_file, run_python_tests
from .schema_utils import SchemaStore
from .skill_installer import install_skills, install_skills_for_hosts
from .vault import write_obsidian_vault

app = typer.Typer(
    name="modeling-mastery",
    help="Evidence-grounded mathematical modeling paper-to-Obsidian pipeline.",
    no_args_is_help=True,
)
console = Console()


def _echo(data: object) -> None:
    console.print_json(json.dumps(data, ensure_ascii=False, default=str))


def _resolve_pipeline_layout(
    *,
    library_root: Path | None,
    paper_title: str | None,
    workspace: Path | None,
    vault: Path | None,
    legacy_workspace: Path,
) -> tuple[Path, Path | None, Path | None, dict[str, str] | None]:
    if library_root is None:
        return workspace or legacy_workspace, vault, None, None
    if not paper_title or not paper_title.strip():
        raise typer.BadParameter("--paper-title is required with --library-root")
    if workspace is not None or vault is not None:
        raise typer.BadParameter("Do not combine --library-root with --workspace or --vault")
    layout = initialize_paper_workspace(library_root, paper_title)
    return (
        layout.workflow,
        layout.knowledge_vault,
        layout.library_root,
        layout.as_dict(),
    )


@app.command("doctor")
def doctor(verbose: bool = typer.Option(False, "--verbose", "-v")) -> None:
    """检查解析器、LLM、Vault 和运行环境。"""
    configure_logging(verbose)
    _echo(doctor_report())


@app.command("ingest")
def ingest(
    input_path: Annotated[Path, typer.Argument(exists=True, readable=True)],
    output: Annotated[Path, typer.Option("--output", "-o")] = Path("workspaces/ingest/parsed"),
    backend: str = typer.Option("auto", "--backend"),
    mineru_backend: str = typer.Option("pipeline", "--mineru-backend"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """01 Paper Ingest。"""
    configure_logging(verbose)
    _echo(parse_document(input_path, output, backend=backend, mineru_backend=mineru_backend).as_dict())


@app.command("analyze")
def analyze(
    normalized_markdown: Annotated[Path, typer.Argument(exists=True, readable=True)],
    structure: Annotated[Optional[Path], typer.Option("--structure")] = None,
    page_map: Annotated[Optional[Path], typer.Option("--page-map")] = None,
    output: Annotated[Path, typer.Option("--output", "-o")] = Path("workspaces/analyze/ir/paper_ir.raw.json"),
    provider: Annotated[Optional[str], typer.Option("--provider")] = None,
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """02–04 证据、模型和算法抽取。"""
    configure_logging(verbose)
    settings = Settings.from_env()
    llm = create_llm(settings, provider)
    ir, report = build_paper_ir(
        normalized_markdown,
        structure_path=structure,
        page_map_path=page_map,
        output_dir=output.parent,
        llm=llm,
    )
    write_json(output, ir)
    _echo({"output": str(output.resolve()), "report": report})


@app.command("normalize")
def normalize_command(
    ir_path: Annotated[Path, typer.Argument(exists=True, readable=True)],
    output: Annotated[Path, typer.Option("--output", "-o")] = Path("paper_ir.json"),
) -> None:
    """规范化模型/算法 canonical name 并合并同义项。"""
    ir, report = normalize_ir(read_json(ir_path))
    SchemaStore().validate("paper", ir)
    write_json(output, ir)
    write_json(output.with_suffix(".normalization-report.json"), report)
    _echo({"output": str(output.resolve()), "report": report})


@app.command("reproduce")
def reproduce_command(
    ir_path: Annotated[Path, typer.Argument(exists=True, readable=True)],
    output: Annotated[Path, typer.Option("--output", "-o")] = Path("workspaces/reproduce/code"),
    updated_ir: Annotated[Path, typer.Option("--updated-ir")] = Path("workspaces/reproduce/paper_ir.with_code.json"),
    provider: Annotated[Optional[str], typer.Option("--provider")] = None,
    max_targets: int = typer.Option(8, "--max-targets", min=1),
    run_tests: bool = typer.Option(True, "--run-tests/--no-run-tests"),
    check_octave: bool = typer.Option(False, "--check-octave/--no-check-octave"),
) -> None:
    """05 Code Reproducer。"""
    settings = Settings.from_env()
    ir, report = reproduce_code(
        read_json(ir_path),
        output,
        llm=create_llm(settings, provider),
        max_targets=max_targets,
        timeout=settings.code_timeout,
        memory_mb=settings.code_memory_mb,
        run_tests=run_tests,
        check_octave=check_octave,
    )
    SchemaStore().validate("paper", ir)
    write_json(updated_ir, ir)
    write_json(output / "code_reproduction_report.json", report)
    _echo({"updated_ir": str(updated_ir.resolve()), "report": report})


@app.command("distill")
def distill(
    ir_path: Annotated[Path, typer.Argument(exists=True, readable=True)],
    vault: Annotated[Optional[Path], typer.Option("--vault")] = None,
    library_root: Annotated[Optional[Path], typer.Option("--library-root")] = None,
) -> None:
    """06–07 知识蒸馏并写入 Obsidian。"""
    if (vault is None) == (library_root is None):
        raise typer.BadParameter("Supply exactly one of --library-root or --vault")
    ir = read_json(ir_path)
    obsidian_root: Path | None = None
    layout_data: dict[str, str] | None = None
    if library_root is not None:
        layout = initialize_paper_workspace(library_root, ir["bibliographic"]["title"])
        vault = layout.knowledge_vault
        obsidian_root = layout.library_root
        layout_data = layout.as_dict()
    assert vault is not None
    report = write_obsidian_vault(
        ir,
        vault,
        project_root=find_project_root(),
        obsidian_root=obsidian_root,
    )
    report["index"] = build_index(vault)
    if layout_data:
        report["paper_workspace"] = layout_data
    _echo(report)


@app.command("init-paper")
def init_paper_command(
    library_root: Annotated[Path, typer.Argument(file_okay=False)],
    title: Annotated[str, typer.Option("--title")],
) -> None:
    """初始化“论文/<论文题目>”标准解读工作区。"""
    _echo(workspace_report(initialize_paper_workspace(library_root, title)))


@app.command("deduplicate")
def deduplicate(
    vault: Annotated[Path, typer.Argument(exists=True, file_okay=False)],
    threshold: float = typer.Option(0.93, "--threshold", min=0.0, max=1.0),
) -> None:
    """生成精确/模糊重复候选报告，不自动删除用户笔记。"""
    _echo(scan_duplicates(vault, fuzzy_threshold=threshold))


@app.command("index")
def index_command(vault: Annotated[Path, typer.Argument(exists=True, file_okay=False)]) -> None:
    """构建 JSON + SQLite FTS5 本地索引。"""
    _echo(build_index(vault))


@app.command("retrieve")
def retrieve(
    vault: Annotated[Path, typer.Argument(exists=True, file_okay=False)],
    query: Annotated[str, typer.Argument()],
    note_type: Annotated[Optional[str], typer.Option("--type")] = None,
    category: Annotated[Optional[str], typer.Option("--category")] = None,
    task: Annotated[Optional[list[str]], typer.Option("--task")] = None,
    top_k: int = typer.Option(10, "--top-k", min=1, max=100),
) -> None:
    """按问题描述反向检索模型、算法、案例或代码。"""
    results = search_index(vault, query, note_type=note_type, category=category, tasks=task, top_k=top_k)
    table = Table(title=f"Modeling-Mastery Retrieval: {query}")
    table.add_column("Score", justify="right")
    table.add_column("Type")
    table.add_column("Title")
    table.add_column("Path")
    table.add_column("Why")
    for result in results:
        table.add_row(f"{result['score']:.3f}", result["type"], result["title"], result["path"], "；".join(result["reasons"]))
    console.print(table)


@app.command("validate-code")
def validate_code_command(path: Annotated[Path, typer.Argument(exists=True, readable=True)]) -> None:
    """静态检查单个 Python/MATLAB 文件。"""
    _echo(validate_file(path).as_dict())


@app.command("run-code")
def run_code_command(
    path: Annotated[Path, typer.Argument(exists=True, readable=True)],
    timeout: int = typer.Option(30, "--timeout", min=1),
    memory_mb: int = typer.Option(2048, "--memory-mb", min=128),
) -> None:
    """运行通过检查的 Python 文件或 recipe pytest。"""
    if path.is_dir():
        result = run_python_tests(path, timeout=timeout, memory_mb=memory_mb)
    else:
        report = validate_file(path)
        if not report.safe:
            raise typer.BadParameter("Code failed static safety validation: " + "; ".join(report.errors))
        result = run_python_file(path, timeout=timeout, memory_mb=memory_mb)
    _echo(result.as_dict())


@app.command("install-skills")
def install_skills_command(
    target: Annotated[Optional[Path], typer.Option("--target")] = None,
    host: str = typer.Option("both", "--host", help="codex | claude | both"),
    scope: str = typer.Option("project", "--scope", help="project | user"),
    base_dir: Path = typer.Option(Path("."), "--base-dir"),
    overwrite: bool = typer.Option(True, "--overwrite/--no-overwrite"),
) -> None:
    """安装到 Codex `.agents/skills`、Claude `.claude/skills` 或显式目录。"""
    if target is not None:
        _echo(install_skills(target, project_root=find_project_root(), overwrite=overwrite))
        return
    try:
        report = install_skills_for_hosts(
            host=host,
            scope=scope,
            base_dir=base_dir,
            project_root=find_project_root(),
            overwrite=overwrite,
        )
    except ValueError as exc:
        raise typer.BadParameter(str(exc)) from exc
    _echo(report)


@app.command("batch")
def batch_command(
    input_root: Annotated[Path, typer.Argument(exists=True, readable=True)],
    workspace_root: Annotated[Path, typer.Option("--workspace-root")],
    vault: Annotated[Optional[Path], typer.Option("--vault")] = None,
    backend: str = typer.Option("auto", "--backend"),
    provider: Annotated[Optional[str], typer.Option("--provider")] = None,
    reproduce_code_flag: bool = typer.Option(False, "--reproduce-code/--no-reproduce-code"),
    max_code_targets: int = typer.Option(8, "--max-code-targets", min=1),
    run_tests: bool = typer.Option(True, "--run-tests/--no-run-tests"),
    check_octave: bool = typer.Option(False, "--check-octave/--no-check-octave"),
    recursive: bool = typer.Option(True, "--recursive/--no-recursive"),
    resume: bool = typer.Option(True, "--resume/--no-resume"),
    continue_on_error: bool = typer.Option(True, "--continue-on-error/--fail-fast"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """批量处理一个目录中的 PDF/Markdown，并增量写入同一 Vault。"""
    configure_logging(verbose)
    _echo(
        run_batch(
            input_root,
            workspace_root,
            vault_path=vault,
            settings=Settings.from_env(),
            backend=backend,
            provider=provider,
            reproduce=reproduce_code_flag,
            max_code_targets=max_code_targets,
            run_tests=run_tests,
            check_octave=check_octave,
            project_root=find_project_root(),
            recursive=recursive,
            resume=resume,
            continue_on_error=continue_on_error,
        )
    )


@app.command("skill-run")
def skill_run_command(
    input_path: Annotated[Path, typer.Argument(exists=True, readable=True)],
    workspace: Annotated[Optional[Path], typer.Option("--workspace")] = None,
    vault: Annotated[Optional[Path], typer.Option("--vault")] = None,
    library_root: Annotated[Optional[Path], typer.Option("--library-root")] = None,
    paper_title: Annotated[Optional[str], typer.Option("--paper-title")] = None,
    agent: str = typer.Option("auto", "--agent", help="auto | codex | claude"),
    backend: str = typer.Option("auto", "--backend"),
    reproduce_code_flag: bool = typer.Option(False, "--reproduce-code/--no-reproduce-code"),
    max_code_targets: int = typer.Option(8, "--max-code-targets", min=1),
    run_tests: bool = typer.Option(True, "--run-tests/--no-run-tests"),
    check_octave: bool = typer.Option(False, "--check-octave/--no-check-octave"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """使用本机已登录的 Codex CLI 或 Claude Code CLI 运行完整 Skill 流水线。"""
    aliases = {
        "auto": "local-agent",
        "local": "local-agent",
        "local-agent": "local-agent",
        "codex": "codex",
        "codex-cli": "codex",
        "claude": "claude-code",
        "claude-code": "claude-code",
        "claudecode": "claude-code",
    }
    selected = aliases.get(agent.strip().lower())
    if not selected:
        raise typer.BadParameter("--agent must be auto, codex, or claude")
    workspace, vault, obsidian_root, layout_data = _resolve_pipeline_layout(
        library_root=library_root,
        paper_title=paper_title,
        workspace=workspace,
        vault=vault,
        legacy_workspace=Path("workspaces/skill-run"),
    )
    configure_logging(verbose)
    report = run_pipeline(
        input_path,
        workspace,
        vault_path=vault,
        settings=Settings.from_env(),
        backend=backend,
        provider=selected,
        reproduce=reproduce_code_flag,
        max_code_targets=max_code_targets,
        run_tests=run_tests,
        check_octave=check_octave,
        project_root=find_project_root(),
        obsidian_root=obsidian_root,
        paper_title_hint=paper_title,
    )
    report["skill_host"] = selected
    if layout_data:
        report["paper_workspace"] = layout_data
    _echo(report)


@app.command("pipeline")
def pipeline_command(
    input_path: Annotated[Path, typer.Argument(exists=True, readable=True)],
    workspace: Annotated[Optional[Path], typer.Option("--workspace")] = None,
    vault: Annotated[Optional[Path], typer.Option("--vault")] = None,
    library_root: Annotated[Optional[Path], typer.Option("--library-root")] = None,
    paper_title: Annotated[Optional[str], typer.Option("--paper-title")] = None,
    backend: str = typer.Option("auto", "--backend"),
    provider: Annotated[Optional[str], typer.Option("--provider")] = None,
    reproduce_code_flag: bool = typer.Option(False, "--reproduce-code/--no-reproduce-code"),
    max_code_targets: int = typer.Option(8, "--max-code-targets", min=1),
    run_tests: bool = typer.Option(True, "--run-tests/--no-run-tests"),
    check_octave: bool = typer.Option(False, "--check-octave/--no-check-octave"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """运行完整七阶段流水线。"""
    workspace, vault, obsidian_root, layout_data = _resolve_pipeline_layout(
        library_root=library_root,
        paper_title=paper_title,
        workspace=workspace,
        vault=vault,
        legacy_workspace=Path("workspaces/run"),
    )
    configure_logging(verbose)
    report = run_pipeline(
        input_path,
        workspace,
        vault_path=vault,
        settings=Settings.from_env(),
        backend=backend,
        provider=provider,
        reproduce=reproduce_code_flag,
        max_code_targets=max_code_targets,
        run_tests=run_tests,
        check_octave=check_octave,
        project_root=find_project_root(),
        obsidian_root=obsidian_root,
        paper_title_hint=paper_title,
    )
    if layout_data:
        report["paper_workspace"] = layout_data
    _echo(report)


if __name__ == "__main__":
    app()
