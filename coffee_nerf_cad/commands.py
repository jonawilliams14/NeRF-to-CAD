from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def require_executable(name: str) -> str:
    executable = shutil.which(name)
    if executable is None:
        raise RuntimeError(f"Required executable not found on PATH: {name}")
    return executable


def run_command(args: list[str], dry_run: bool = False) -> None:
    print(" ".join(args))
    if not dry_run:
        subprocess.run(args, check=True)


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
