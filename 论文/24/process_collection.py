from __future__ import annotations

import argparse
import json
import re
import sys
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable


COLLECTION_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = COLLECTION_ROOT.parent.parent
SKILL_ROOT = REPOSITORY_ROOT / "skill" / "Modeling-Mastery"
sys.path.insert(0, str(SKILL_ROOT))

from modeling_mastery.config import Settings  # noqa: E402
from modeling_mastery.dedup import scan_duplicates  # noqa: E402
from modeling_mastery.document import parse_document  # noqa: E402
from modeling_mastery.indexer import build_index  # noqa: E402
from modeling_mastery.io_utils import atomic_write_text, merge_unique, read_json, utc_now_iso, write_json  # noqa: E402
from modeling_mastery.ir_builder import build_paper_ir  # noqa: E402
from modeling_mastery.llm import create_llm  # noqa: E402
from modeling_mastery.normalizer import ReferenceCatalog, normalize_ir  # noqa: E402
from modeling_mastery.schema_utils import SchemaStore  # noqa: E402
from modeling_mastery.vault import write_obsidian_vault  # noqa: E402


def _manifest() -> dict[str, Any]:
    return json.loads((COLLECTION_ROOT / "manifest.json").read_text(encoding="utf-8"))


def _curated() -> dict[str, Any]:
    return json.loads((COLLECTION_ROOT / "curated_analysis.json").read_text(encoding="utf-8"))


def _safe_folder_name(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*]', "-", value)
    return re.sub(r"\s+", "", value).strip(". ")


def _paper_root(paper: dict[str, Any]) -> Path:
    return COLLECTION_ROOT / _safe_folder_name(f"{paper['code']}-{paper['title']}")


def _source_path(paper: dict[str, Any]) -> Path:
    return Path(_manifest()["source_directory"]) / paper["source_file"]


def _ensure_layout(paper: dict[str, Any]) -> Path:
    root = _paper_root(paper)
    for relative in [
        "assets",
        "workflow/parsed",
        "workflow/ir",
        "workflow/reports",
        "补充笔记/模型",
        "补充笔记/算法",
        "知识库",
    ]:
        (root / relative).mkdir(parents=True, exist_ok=True)
    return root


def _parse_one(paper: dict[str, Any]) -> dict[str, Any]:
    root = _ensure_layout(paper)
    parsed = root / "workflow" / "parsed"
    result = parse_document(
        _source_path(paper),
        parsed,
        backend="pymupdf-ocr",
        title_hint=paper["title"],
    )
    return {
        "code": paper["code"],
        "status": "parsed",
        "parser": result.parser,
        "warnings": result.warnings,
        "normalized_markdown": str(result.normalized_markdown),
    }


def _enforce_known_metadata(ir: dict[str, Any], paper: dict[str, Any]) -> dict[str, Any]:
    code = paper["code"]
    title = paper["title"]
    ir["paper_id"] = f"paper-2024-{code.lower()}"
    ir["bibliographic"].update(
        {
            "title": title,
            "year": 2024,
            "competition": "高教社杯全国大学生数学建模竞赛",
            "award": "优秀论文",
            "problem_id": code[0],
            "language": "zh-CN",
        }
    )
    ir["case"].update(
        {
            "id": f"case-2024-{code.lower()}",
            "title": title,
            "year": 2024,
            "competition": "高教社杯全国大学生数学建模竞赛",
            "award": "优秀论文",
            "problem_id": code[0],
        }
    )
    ir["source"]["parser"] = "pymupdf-ocr"
    ir["quality"]["review_required"] = True
    ir["quality"]["warnings"] = merge_unique(
        ir["quality"].get("warnings", []),
        [
            "源 PDF 为扫描件；全文由 Tesseract chi_sim+eng 以 180 dpi OCR。",
            "公式、上下标、变量、表格与精确数值必须回看源 PDF 页面复核。",
        ],
    )
    if paper.get("title_source", "").startswith("inferred"):
        ir["quality"]["warnings"] = merge_unique(
            ir["quality"]["warnings"],
            ["扫描件首页缺少正式标题；当前标题由摘要主题推定。"],
        )
    return ir


def _analyze_one(payload: tuple[dict[str, Any], str, int]) -> dict[str, Any]:
    paper, provider, chunk_chars = payload
    root = _ensure_layout(paper)
    parsed = root / "workflow" / "parsed"
    ir_dir = root / "workflow" / "ir"
    llm = create_llm(Settings.from_env(), provider)
    raw_ir, build_report = build_paper_ir(
        parsed / "normalized_paper.md",
        structure_path=parsed / "paper_structure.json",
        page_map_path=parsed / "page_map.json",
        output_dir=ir_dir,
        llm=llm,
        catalog=ReferenceCatalog(SKILL_ROOT / "references"),
        chunk_chars=chunk_chars,
    )
    raw_ir = _enforce_known_metadata(raw_ir, paper)
    write_json(ir_dir / "paper_ir.raw.json", raw_ir)
    normalized_ir, normalization_report = normalize_ir(
        raw_ir, ReferenceCatalog(SKILL_ROOT / "references")
    )
    normalized_ir = _enforce_known_metadata(normalized_ir, paper)
    SchemaStore(SKILL_ROOT / "schemas").validate("paper", normalized_ir)
    write_json(ir_dir / "paper_ir.json", normalized_ir)
    write_json(ir_dir / "normalization_report.json", normalization_report)
    return {
        "code": paper["code"],
        "status": "analyzed",
        "provider": build_report.get("provider", provider),
        "chunk_count": len(build_report.get("chunks", [])),
        "warnings": build_report.get("warnings", []),
        "evidence_count": len(normalized_ir.get("evidence", [])),
        "model_count": len(normalized_ir.get("models", [])),
        "algorithm_count": len(normalized_ir.get("algorithms", [])),
    }


def _value_list(values: list[Any] | None, fallback: str = "论文未明确给出") -> str:
    cleaned = [str(value).strip() for value in values or [] if str(value).strip()]
    return "；".join(cleaned) if cleaned else fallback


def _evidence_pointer(ir: dict[str, Any], ids: list[str] | None) -> str:
    lookup = {item.get("id"): item for item in ir.get("evidence", [])}
    pointers = []
    for evidence_id in ids or []:
        item = lookup.get(evidence_id, {})
        page = item.get("page")
        pointers.append(f"{evidence_id}（p.{page if page is not None else '?'}）")
    return "、".join(pointers) if pointers else "未锚定"


def _summary_markdown(ir: dict[str, Any], paper: dict[str, Any]) -> str:
    bibliographic = ir["bibliographic"]
    lines = [
        f"# {paper['code']}｜{paper['title']}",
        "",
        "> 本文解读由完整扫描 PDF 的逐页 OCR、Evidence IR、模型卡与算法卡汇总而成。公式、上下标、表格和精确数值请按页码回看源 PDF。",
        "",
        "## 一句话定位",
        "",
        str(ir.get("problem", {}).get("overall_objective") or bibliographic.get("abstract") or "围绕赛题建立可计算、可求解并可验证的数学模型。"),
        "",
        "## 摘要与研究主线",
        "",
        str(bibliographic.get("abstract") or "OCR 未能可靠分离摘要，请查看完整正文。"),
        "",
        "## 子问题拆解",
        "",
    ]
    for item in ir.get("problem", {}).get("subproblems", []):
        lines.extend(
            [
                f"### {item.get('id', '子问题')}",
                "",
                str(item.get("statement") or "论文未明确分段"),
                "",
                f"- 任务类型：{_value_list(item.get('task_types'), '未分类')}",
                f"- 输入：{_value_list(item.get('inputs'))}",
                f"- 输出：{_value_list(item.get('outputs'))}",
                f"- 约束：{_value_list(item.get('constraints'))}",
                "",
            ]
        )
    lines.extend(["## 建模链", "", "| 顺序 | 子问题 | 模型 | 求解算法 | 输入 → 输出 | 依据 |", "|---:|---|---|---|---|---|"])
    for step in ir.get("modeling_chain", []):
        lines.append(
            "| {order} | {sub} | `{model}` | {algorithms} | {input} → {output} | {evidence} |".format(
                order=step.get("order", ""),
                sub=str(step.get("subproblem_id") or "-").replace("|", "\\|"),
                model=str(step.get("model_id") or "-").replace("|", "\\|"),
                algorithms="、".join(step.get("algorithm_ids", [])) or "未指定",
                input=str(step.get("input") or "未明确").replace("|", "\\|"),
                output=str(step.get("output") or "未明确").replace("|", "\\|"),
                evidence=_evidence_pointer(ir, step.get("evidence_ids")),
            )
        )
    lines.extend(["", "## 核心模型", ""])
    for model in ir.get("models", []):
        lines.extend(
            [
                f"### {model.get('canonical_name', model.get('name', '未命名模型'))}",
                "",
                str(model.get("description") or model.get("role") or "论文未给出独立说明。"),
                "",
                f"- 角色：{model.get('role') or '未明确'}",
                f"- 输入：{_value_list(model.get('inputs'))}",
                f"- 输出：{_value_list(model.get('outputs'))}",
                f"- 假设：{_value_list(model.get('assumptions'))}",
                f"- 局限：{_value_list(model.get('limitations'))}",
                f"- 来源类型：`{model.get('provenance', 'unknown')}`；置信度：{model.get('confidence', 'unknown')}",
                f"- 证据：{_evidence_pointer(ir, model.get('evidence_ids'))}",
                "",
            ]
        )
    lines.extend(["## 求解算法", ""])
    for algorithm in ir.get("algorithms", []):
        parameters = algorithm.get("parameters", [])
        parameter_text = "；".join(
            f"{item.get('name', '?')}={item.get('value') if item.get('value') is not None else 'unknown'} ({item.get('provenance', 'unknown')})"
            for item in parameters
            if isinstance(item, dict)
        ) or "论文未明确给出"
        lines.extend(
            [
                f"### {algorithm.get('canonical_name', algorithm.get('name', '未命名算法'))}",
                "",
                str(algorithm.get("purpose") or "用于模型求解。"),
                "",
                f"- 初始化：{algorithm.get('initialization') or 'unknown'}",
                f"- 停止条件：{algorithm.get('stopping_criterion') or 'unknown'}",
                f"- 参数：{parameter_text}",
                f"- 复杂度：{algorithm.get('time_complexity') or 'unknown'} / {algorithm.get('space_complexity') or 'unknown'}",
                f"- 失败模式：{_value_list(algorithm.get('failure_modes'))}",
                f"- 证据：{_evidence_pointer(ir, algorithm.get('evidence_ids'))}",
                "",
            ]
        )
    validation = ir.get("validation", {})
    case = ir.get("case", {})
    lines.extend(
        [
            "## 结果与验证",
            "",
            f"- 验证方法：{_value_list(validation.get('methods'))}",
            f"- 指标：{_value_list(validation.get('metrics'))}",
            f"- 主要结果：{_value_list(validation.get('results') or case.get('results'))}",
            f"- 灵敏度分析：{_value_list(validation.get('sensitivity_analysis'))}",
            f"- 鲁棒性检查：{_value_list(validation.get('robustness_checks'))}",
            "",
            "## 可迁移经验",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in case.get("transferable_insights", []) or ["迁移到新赛题前重新核验数据、约束和评价指标。"])
    lines.extend(["", "## 创新、优点与局限", "", "### 创新点", ""])
    lines.extend(f"- {item}" for item in ir.get("innovations", []) or ["论文未明确声明创新点。"])
    lines.extend(["", "### 局限与风险", ""])
    lines.extend(f"- {item}" for item in ir.get("limitations", []) or ["论文未明确讨论局限；需结合假设、样本与求解精度复核。"])
    lines.extend(f"- 易踩坑：{item}" for item in case.get("pitfalls", []))
    lines.extend(["", "## 关键证据索引", "", "| ID | 页码 | 类型 | 原文摘录 |", "|---|---:|---|---|"])
    for item in ir.get("evidence", []):
        quote = str(item.get("quote") or "").replace("|", "\\|").replace("\n", " ")
        lines.append(f"| `{item.get('id')}` | {item.get('page') if item.get('page') is not None else '?'} | {item.get('kind', '-')} | {quote[:260]} |")
    quality = ir.get("quality", {})
    lines.extend(
        [
            "",
            "## 质量说明",
            "",
            f"- Evidence 数量：{len(ir.get('evidence', []))}",
            f"- 证据覆盖率：{float(quality.get('evidence_coverage', 0)):.1%}",
            f"- 结构完整度：{float(quality.get('completeness', 0)):.1%}",
            f"- 需要人工复核：{'是' if quality.get('review_required', True) else '否'}",
        ]
    )
    lines.extend(f"- 警告：{warning}" for warning in quality.get("warnings", []))
    return "\n".join(lines).rstrip() + "\n"


def _curated_summary_markdown(ir: dict[str, Any], paper: dict[str, Any], curated: dict[str, Any]) -> str:
    lines = [
        f"# {paper['code']}｜{paper['title']}",
        "",
        "> [!important] 解读口径",
        "> 本文解读建立在 807 页全量 OCR 中该论文的全部页面、确定性 Evidence IR、摘要页与模型评价页上。普通段落已人工校订；公式、上下标、表格数字和单位仍须按页码回看源 PDF。",
        "",
        "## 一句话定位",
        "",
        curated["positioning"],
        "",
        "## 逐问路线总览",
        "",
        "| 子问题 | 任务 | 核心方法 | 主要结果 | 原文页 |",
        "|---|---|---|---|---|",
    ]
    for item in curated["subproblems"]:
        pages = "、".join(f"p.{page}" for page in item.get("pages", [])) or "p.?"
        values = [item["id"], item["task"], item["method"], item["result"], pages]
        lines.append("| " + " | ".join(str(value).replace("|", "\\|").replace("\n", " ") for value in values) + " |")
    lines.extend(["", "## 模型与算法分工", "", "### 模型（描述数学关系）", ""])
    lines.extend(f"- {item}" for item in curated["models"])
    lines.extend(["", "### 算法（负责求解或估计）", ""])
    lines.extend(f"- {item}" for item in curated["algorithms"])
    lines.extend(["", "## 分问题精读", ""])
    for item in curated["subproblems"]:
        pages = "、".join(f"p.{page}" for page in item.get("pages", [])) or "p.?"
        lines.extend(
            [
                f"### {item['id']}｜{item['task']}",
                "",
                f"**怎么建模：** {item['method']}",
                "",
                f"**得到什么：** {item['result']}",
                "",
                f"**来源锚点：** {pages}；更细的原文证据见 `source_map.json` 与 `workflow/ir/paper_ir.json`。",
                "",
            ]
        )
    lines.extend(["## 值得学习的地方", ""])
    lines.extend(f"- {item}" for item in curated["strengths"])
    lines.extend(["", "## 局限与复核重点", ""])
    lines.extend(f"- {item}" for item in curated["limitations"])
    lines.extend(["", "## 可迁移经验", ""])
    lines.extend(f"- {item}" for item in curated["transferable"])
    quality = ir.get("quality", {})
    lines.extend(
        [
            "",
            "## 证据与质量状态",
            "",
            f"- 原始 PDF：{paper['pages']} 页扫描件。",
            f"- OCR 文本：逐页完成，空页数见 `translation_notes.md`。",
            f"- Evidence：{len(ir.get('evidence', []))} 条，均保留页码或可追溯文本。",
            f"- 自动 IR 证据覆盖率：{float(quality.get('evidence_coverage', 0)):.1%}；语义后端超时后采用确定性回退，模型含义由本解读人工校订。",
            "- 结论使用规则：普通方法描述可直接用于复习；精确参数、公式和小数结果在论文写作中引用前必须打开源 PDF 复核。",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def _curated_cards_markdown(paper: dict[str, Any], curated: dict[str, Any], kind: str) -> str:
    names = curated["models" if kind == "模型" else "algorithms"]
    lines = [f"# {paper['code']}｜{kind}总览", "", f"来源：[[论文/24/{_paper_root(paper).name}/解读|{paper['title']}]]", ""]
    for index, name in enumerate(names, start=1):
        lines.extend([f"## {index}. {name}", ""])
        related = [item for item in curated["subproblems"] if name.split("（", 1)[0][:4] in item["method"]]
        if related:
            lines.append("关联子问题：" + "、".join(item["id"] for item in related) + "。")
        else:
            lines.append("关联范围：见《解读》中的逐问路线总览。")
        lines.extend(["", "> 该卡由人工校订的年度论文解读生成；精确公式与参数请回看源 PDF。", ""])
    return "\n".join(lines).rstrip() + "\n"


def _source_map(ir: dict[str, Any], paper: dict[str, Any], page_map: dict[str, Any]) -> dict[str, Any]:
    blocks = []
    page_blocks: dict[int, list[str]] = {int(page["page"]): [] for page in page_map.get("pages", [])}
    for index, item in enumerate(ir.get("evidence", []), start=1):
        block_id = f"S{index:03d}"
        page = item.get("page")
        blocks.append(
            {
                "id": block_id,
                "evidence_id": item.get("id"),
                "page": page,
                "type": item.get("kind", "paragraph"),
                "order": index,
                "original_text": item.get("quote", ""),
                "translation": "",
                "bbox": [0, 0, 0, 0],
                "confidence": "medium",
                "refs": [],
                "insert_after": "",
            }
        )
        if isinstance(page, int) and page in page_blocks:
            page_blocks[page].append(block_id)
    glossary = []
    seen = set()
    for item in [*ir.get("models", []), *ir.get("algorithms", [])]:
        term = str(item.get("canonical_name") or "").strip()
        if term and term not in seen:
            seen.add(term)
            glossary.append({"term": term, "translation": term, "note": str(item.get("description") or item.get("purpose") or "")})
    return {
        "paper": {
            "title": paper["title"],
            "venue": "2024年高教社杯全国大学生数学建模竞赛优秀论文",
            "source_type": "pdf",
            "language": "zh-CN",
            "source_path": str(_source_path(paper)),
        },
        "blocks": blocks,
        "pages": [{"page": number, "block_ids": ids} for number, ids in sorted(page_blocks.items())],
        "figures": [],
        "glossary": glossary,
    }


def _notes_markdown(ir: dict[str, Any], paper: dict[str, Any], page_map: dict[str, Any]) -> str:
    empty_pages = [str(page["page"]) for page in page_map.get("pages", []) if not str(page.get("text") or "").strip()]
    error_pages = [str(page["page"]) for page in page_map.get("pages", []) if page.get("ocr_error")]
    title_note = "首页原文标题。"
    if paper.get("title_source", "").startswith("inferred"):
        title_note = "扫描件首页缺少正式标题；当前标题依据摘要研究目标推定。"
    return (
        f"# {paper['code']} 解析与置信度说明\n\n"
        f"- 来源：`{_source_path(paper)}`\n"
        f"- 页数：{paper['pages']}\n"
        f"- 标题依据：{title_note}\n"
        "- 来源语言：中文，因此未生成中英翻译对；`source_map.json` 的 `translation` 字段留空。\n"
        "- OCR：Tesseract `chi_sim+eng`，180 dpi；所有 OCR 证据默认 `medium` 置信度。\n"
        f"- 空文本页：{('、'.join(empty_pages) if empty_pages else '无')}\n"
        f"- OCR 报错页：{('、'.join(error_pages) if error_pages else '无')}\n"
        "- 重点复核：公式、矩阵、上下标、希腊字母、图表数字、小数点、单位和参考文献。\n"
        "- 图表策略：扫描页没有把页面背景误当成独立图表资产；图表请按页码回看源 PDF。\n\n"
        "## Pipeline 警告\n\n"
        + "\n".join(f"- {warning}" for warning in ir.get("quality", {}).get("warnings", []))
        + "\n"
    )


def _readme_markdown(ir: dict[str, Any], paper: dict[str, Any]) -> str:
    return f"""# {paper['code']}｜{paper['title']}

- 题组：{paper['code'][0]} 题
- 年份：2024
- 页数：{paper['pages']}
- 原文件：`{paper['source_file']}`
- 解析器：`pymupdf-ocr`（Tesseract `chi_sim+eng`）

## 快速入口

- [论文解读](解读.md)
- [来源映射](source_map.json)
- [OCR 与复核说明](translation_notes.md)
- [完整 OCR 正文](workflow/parsed/normalized_paper.md)
- [Paper IR](workflow/ir/paper_ir.json)
- [知识库首页](知识库/00_Home/Modeling-Mastery%20首页.md)
- [人工校订模型总览](补充笔记/模型/模型总览.md)
- [人工校订算法总览](补充笔记/算法/算法总览.md)
- [首页扫描图](assets/首页.png)

## 资产说明

`workflow/` 保存可复跑的解析和证据产物；`知识库/` 保存 Paper、Case、Model、Algorithm 卡片；`补充笔记/` 专供人工追加内容，自动流程不覆盖。
"""


def _render_cover(paper: dict[str, Any], target: Path) -> None:
    import fitz

    with fitz.open(_source_path(paper)) as document:
        pixmap = document[0].get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
        pixmap.save(target)


def _distill_one(paper: dict[str, Any]) -> dict[str, Any]:
    root = _ensure_layout(paper)
    ir_path = root / "workflow" / "ir" / "paper_ir.json"
    ir = read_json(ir_path)
    vault = root / "知识库"
    vault_report = write_obsidian_vault(
        ir,
        vault,
        project_root=SKILL_ROOT,
        obsidian_root=REPOSITORY_ROOT,
    )
    dedup_report = scan_duplicates(vault)
    index_report = build_index(vault)
    page_map = read_json(root / "workflow" / "parsed" / "page_map.json")
    curated = _curated()[paper["code"]]
    atomic_write_text(root / "解读.md", _curated_summary_markdown(ir, paper, curated))
    write_json(root / "source_map.json", _source_map(ir, paper, page_map))
    atomic_write_text(root / "translation_notes.md", _notes_markdown(ir, paper, page_map))
    atomic_write_text(root / "README.md", _readme_markdown(ir, paper))
    atomic_write_text(root / "补充笔记" / "模型" / "模型总览.md", _curated_cards_markdown(paper, curated, "模型"))
    atomic_write_text(root / "补充笔记" / "算法" / "算法总览.md", _curated_cards_markdown(paper, curated, "算法"))
    _render_cover(paper, root / "assets" / "首页.png")
    report = {
        "paper": paper,
        "finished_at": utc_now_iso(),
        "parser": "pymupdf-ocr",
        "semantic_provider": ir.get("_generation", {}).get("provider", "recorded in build_ir_report.json"),
        "counts": {
            "evidence": len(ir.get("evidence", [])),
            "models": len(ir.get("models", [])),
            "algorithms": len(ir.get("algorithms", [])),
            "vault_notes": len(vault_report.get("created_or_updated", [])),
        },
        "quality": ir.get("quality", {}),
        "vault": vault_report,
        "dedup": dedup_report,
        "index": index_report,
    }
    write_json(root / "workflow" / "reports" / "pipeline_report.json", report)
    return {"code": paper["code"], "status": "distilled", **report["counts"]}


def _run_parallel(
    papers: list[dict[str, Any]],
    worker: Callable[[Any], dict[str, Any]],
    *,
    workers: int,
    payload: Callable[[dict[str, Any]], Any] | None = None,
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    with ProcessPoolExecutor(max_workers=workers) as executor:
        future_map = {
            executor.submit(worker, payload(paper) if payload else paper): paper
            for paper in papers
        }
        for future in as_completed(future_map):
            paper = future_map[future]
            try:
                result = future.result()
            except Exception as exc:
                result = {
                    "code": paper["code"],
                    "status": "failed",
                    "error": f"{type(exc).__name__}: {exc}",
                    "traceback": traceback.format_exc(),
                }
            results.append(result)
            print(json.dumps(result, ensure_ascii=False), flush=True)
    return sorted(results, key=lambda item: item["code"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Process the complete 2024 excellent-paper collection.")
    parser.add_argument("stage", choices=["init", "parse", "analyze", "distill"])
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--provider", default="codex", choices=["codex", "claude-code", "local-agent", "none"])
    parser.add_argument("--chunk-chars", type=int, default=16000)
    parser.add_argument("--codes", nargs="*", help="Optional paper codes; default is all 16 papers.")
    args = parser.parse_args()
    manifest = _manifest()
    papers = [paper for paper in manifest["papers"] if not args.codes or paper["code"] in args.codes]
    if args.stage == "init":
        results = [{"code": paper["code"], "root": str(_ensure_layout(paper))} for paper in papers]
    elif args.stage == "parse":
        results = _run_parallel(papers, _parse_one, workers=max(1, args.workers))
    elif args.stage == "analyze":
        results = _run_parallel(
            papers,
            _analyze_one,
            workers=max(1, args.workers),
            payload=lambda paper: (paper, args.provider, args.chunk_chars),
        )
    else:
        results = _run_parallel(papers, _distill_one, workers=max(1, args.workers))
    write_json(COLLECTION_ROOT / f"_{args.stage}_report.json", {"generated_at": utc_now_iso(), "results": results})
    if any(result.get("status") == "failed" for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
