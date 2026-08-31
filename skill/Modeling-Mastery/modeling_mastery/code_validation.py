from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

FORBIDDEN_IMPORT_ROOTS = {
    "os",
    "subprocess",
    "socket",
    "requests",
    "urllib",
    "http",
    "ftplib",
    "shutil",
    "pickle",
    "marshal",
    "ctypes",
    "multiprocessing",
    "threading",
    "asyncio",
    "resource",
    "signal",
    "webbrowser",
}
FORBIDDEN_CALLS = {
    "eval",
    "exec",
    "compile",
    "__import__",
    "open",
    "input",
    "breakpoint",
    "globals",
    "locals",
    "vars",
}
FORBIDDEN_ATTRIBUTES = {
    "system",
    "popen",
    "spawn",
    "fork",
    "remove",
    "unlink",
    "rmdir",
    "rmtree",
    "chmod",
    "chown",
    "kill",
    "killpg",
    "connect",
    "request",
    "urlopen",
}
MATLAB_FORBIDDEN_PATTERNS = {
    r"(?i)\bsystem\s*\(": "system command",
    r"(?i)\bunix\s*\(": "unix command",
    r"(?i)\bdos\s*\(": "DOS command",
    r"(?i)\bwebread\s*\(": "network access",
    r"(?i)\bwebwrite\s*\(": "network access",
    r"(?i)\burlread\s*\(": "network access",
    r"(?i)\burlwrite\s*\(": "network access",
    r"(?m)^\s*!": "shell escape",
}


@dataclass(slots=True)
class ValidationReport:
    language: str
    safe: bool
    syntax_ok: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)
    functions: list[str] = field(default_factory=list)
    source_anchor_count: int = 0

    def as_dict(self) -> dict[str, Any]:
        return {
            "language": self.language,
            "safe": self.safe,
            "syntax_ok": self.syntax_ok,
            "errors": self.errors,
            "warnings": self.warnings,
            "imports": self.imports,
            "functions": self.functions,
            "source_anchor_count": self.source_anchor_count,
        }


class _SafetyVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.imports: list[str] = []
        self.functions: list[str] = []

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            root = alias.name.split(".")[0]
            self.imports.append(alias.name)
            if root in FORBIDDEN_IMPORT_ROOTS:
                self.errors.append(f"Forbidden import at line {node.lineno}: {alias.name}")
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        module = node.module or ""
        root = module.split(".")[0]
        self.imports.append(module)
        if root in FORBIDDEN_IMPORT_ROOTS:
            self.errors.append(f"Forbidden import at line {node.lineno}: {module}")
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Name) and node.func.id in FORBIDDEN_CALLS:
            self.errors.append(f"Forbidden call at line {node.lineno}: {node.func.id}()")
        elif isinstance(node.func, ast.Attribute) and node.func.attr in FORBIDDEN_ATTRIBUTES:
            self.errors.append(f"Forbidden attribute call at line {node.lineno}: .{node.func.attr}()")
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if node.attr.startswith("__") and node.attr.endswith("__"):
            self.errors.append(f"Dunder attribute access at line {node.lineno}: {node.attr}")
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.functions.append(node.name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.errors.append(f"Async function is not allowed in generated recipe at line {node.lineno}")
        self.generic_visit(node)


SAFE_TOP_LEVEL_NODES = (
    ast.Import,
    ast.ImportFrom,
    ast.FunctionDef,
    ast.ClassDef,
    ast.Assign,
    ast.AnnAssign,
    ast.Expr,
    ast.If,
)


def validate_python_source(source: str) -> ValidationReport:
    report = ValidationReport(language="python", safe=False, syntax_ok=False)
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        report.errors.append(f"SyntaxError line {exc.lineno}: {exc.msg}")
        return report
    report.syntax_ok = True
    visitor = _SafetyVisitor()
    visitor.visit(tree)
    report.errors.extend(visitor.errors)
    report.warnings.extend(visitor.warnings)
    report.imports = visitor.imports
    report.functions = visitor.functions
    for node in tree.body:
        if not isinstance(node, SAFE_TOP_LEVEL_NODES):
            report.warnings.append(f"Unexpected top-level node: {type(node).__name__}")
        if isinstance(node, ast.Expr) and not isinstance(node.value, ast.Constant):
            report.warnings.append(f"Top-level expression at line {getattr(node, 'lineno', '?')}")
    report.source_anchor_count = len(re.findall(r"(?i)(?:source evidence|evidence id|AI_INFERRED|PAPER_EXPLICIT)", source))
    if report.source_anchor_count == 0:
        report.warnings.append("No provenance/evidence comment was found in the generated code.")
    if not report.functions:
        report.warnings.append("No function definition was found.")
    report.safe = report.syntax_ok and not report.errors
    return report


def validate_matlab_source(source: str) -> ValidationReport:
    errors: list[str] = []
    for pattern, label in MATLAB_FORBIDDEN_PATTERNS.items():
        if re.search(pattern, source):
            errors.append(f"Forbidden MATLAB operation: {label}")
    functions = re.findall(r"(?im)^\s*function\s+(?:\[[^\]]+\]|\w+)?\s*=*\s*(\w+)", source)
    if not functions:
        functions = re.findall(r"(?im)^\s*function\s+(\w+)\s*\(", source)
    source_anchor_count = len(re.findall(r"(?i)(?:source evidence|evidence id|AI_INFERRED|PAPER_EXPLICIT)", source))
    warnings: list[str] = []
    if source_anchor_count == 0:
        warnings.append("No provenance/evidence comment was found in the MATLAB code.")
    if not functions:
        warnings.append("No MATLAB function declaration was detected.")
    syntax_ok = source.count("function") <= source.count("end") + 1
    if not syntax_ok:
        errors.append("Possible unbalanced function/end blocks.")
    return ValidationReport(
        language="matlab",
        safe=syntax_ok and not errors,
        syntax_ok=syntax_ok,
        errors=errors,
        warnings=warnings,
        imports=[],
        functions=functions,
        source_anchor_count=source_anchor_count,
    )


def validate_file(path: Path) -> ValidationReport:
    source = path.read_text(encoding="utf-8", errors="replace")
    suffix = path.suffix.lower()
    if suffix == ".py":
        return validate_python_source(source)
    if suffix == ".m":
        return validate_matlab_source(source)
    return ValidationReport(
        language=suffix.lstrip(".") or "unknown",
        safe=False,
        syntax_ok=False,
        errors=[f"Unsupported source type: {suffix}"],
    )
