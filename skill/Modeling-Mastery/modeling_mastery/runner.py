from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class RunResult:
    command: list[str]
    returncode: int | None
    stdout: str
    stderr: str
    duration_seconds: float
    timed_out: bool
    skipped: bool = False
    reason: str = ""

    @property
    def passed(self) -> bool:
        return not self.skipped and not self.timed_out and self.returncode == 0

    def as_dict(self) -> dict[str, Any]:
        return {
            "command": self.command,
            "returncode": self.returncode,
            "stdout": self.stdout,
            "stderr": self.stderr,
            "duration_seconds": round(self.duration_seconds, 4),
            "timed_out": self.timed_out,
            "skipped": self.skipped,
            "reason": self.reason,
            "passed": self.passed,
        }


def _resource_limiter(cpu_seconds: int, memory_mb: int):
    def apply_limits() -> None:
        try:
            import resource

            resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds + 1))
            memory = memory_mb * 1024 * 1024
            resource.setrlimit(resource.RLIMIT_AS, (memory, memory))
            resource.setrlimit(resource.RLIMIT_FSIZE, (64 * 1024 * 1024, 64 * 1024 * 1024))
            resource.setrlimit(resource.RLIMIT_NPROC, (32, 32))
        except (ImportError, ValueError, OSError):
            pass

    return apply_limits


def _safe_environment(extra: dict[str, str] | None = None) -> dict[str, str]:
    keep = [
        "PATH",
        "SYSTEMROOT",
        "WINDIR",
        "COMSPEC",
        "PATHEXT",
        "LANG",
        "LC_ALL",
        "TMP",
        "TEMP",
    ]
    environment = {name: os.environ[name] for name in keep if name in os.environ}
    environment.update(
        {
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONNOUSERSITE": "1",
            "PYTHONHASHSEED": "0",
        }
    )
    if extra:
        environment.update(extra)
    return environment


def run_command(
    command: list[str],
    *,
    cwd: Path,
    timeout: int = 30,
    memory_mb: int = 2048,
    env: dict[str, str] | None = None,
) -> RunResult:
    started = time.monotonic()
    preexec = _resource_limiter(timeout, memory_mb) if os.name == "posix" else None
    with tempfile.TemporaryDirectory(prefix="modeling-mastery-home-") as home:
        environment = _safe_environment(env)
        environment["HOME"] = home
        try:
            completed = subprocess.run(
                command,
                cwd=str(cwd),
                env=environment,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False,
                preexec_fn=preexec,
            )
            return RunResult(
                command=command,
                returncode=completed.returncode,
                stdout=completed.stdout[-20000:],
                stderr=completed.stderr[-20000:],
                duration_seconds=time.monotonic() - started,
                timed_out=False,
            )
        except subprocess.TimeoutExpired as exc:
            stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            stderr = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
            return RunResult(
                command=command,
                returncode=None,
                stdout=stdout[-20000:],
                stderr=stderr[-20000:],
                duration_seconds=time.monotonic() - started,
                timed_out=True,
                reason=f"Timed out after {timeout}s",
            )


def run_python_tests(recipe_dir: Path, *, timeout: int = 30, memory_mb: int = 2048) -> RunResult:
    python_dir = recipe_dir / "python"
    tests_dir = recipe_dir / "tests"
    if not python_dir.exists() or not tests_dir.exists():
        return RunResult([], None, "", "", 0.0, False, skipped=True, reason="Missing python/ or tests/ directory")
    python_path = str(python_dir.resolve())
    existing = os.environ.get("PYTHONPATH", "")
    if existing:
        python_path = os.pathsep.join([python_path, existing])
    return run_command(
        [sys.executable, "-B", "-m", "pytest", "-q", str(tests_dir.resolve())],
        cwd=recipe_dir,
        timeout=timeout,
        memory_mb=memory_mb,
        env={"PYTHONPATH": python_path},
    )


def run_python_file(path: Path, *, timeout: int = 30, memory_mb: int = 2048) -> RunResult:
    return run_command(
        [sys.executable, "-B", str(path.resolve())],
        cwd=path.parent,
        timeout=timeout,
        memory_mb=memory_mb,
    )


def run_octave_check(matlab_file: Path, *, timeout: int = 30, memory_mb: int = 2048) -> RunResult:
    octave = shutil.which("octave") or shutil.which("octave-cli")
    if not octave:
        return RunResult([], None, "", "", 0.0, False, skipped=True, reason="Octave is not installed")
    escaped = str(matlab_file.parent.resolve()).replace("'", "''")
    command = [octave, "--quiet", "--eval", f"addpath('{escaped}'); which('{matlab_file.stem}');"]
    return run_command(command, cwd=matlab_file.parent, timeout=timeout, memory_mb=memory_mb)
