from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def local_tool_paths() -> list[Path]:
    return [
        Path(sys.executable).parent,
        Path.cwd() / "tools" / "colmap" / "bin",
    ]


def require_executable(name: str) -> str:
    executable = shutil.which(name)
    if executable is None and not name.lower().endswith(".exe"):
        executable = shutil.which(f"{name}.exe")
    for tool_path in local_tool_paths():
        if executable is not None:
            break
        candidates = [tool_path / name]
        if not name.lower().endswith(".exe"):
            candidates.append(tool_path / f"{name}.exe")
        for candidate in candidates:
            if candidate.exists():
                executable = str(candidate)
                break
    if executable is None:
        raise RuntimeError(f"Required executable not found on PATH: {name}")
    return executable


def run_command(args: list[str], dry_run: bool = False) -> None:
    print(" ".join(args))
    if not dry_run:
        env = os.environ.copy()
        tool_path = os.pathsep.join(str(path) for path in local_tool_paths())
        env["PATH"] = tool_path + os.pathsep + env.get("PATH", "")
        subprocess.run(args, check=True, env=env)


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
