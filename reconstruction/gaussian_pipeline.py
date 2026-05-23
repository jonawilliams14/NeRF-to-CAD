from __future__ import annotations

from pathlib import Path

from coffee_nerf_cad.commands import run_command


def run_gaussian_pipeline(source: Path, output: Path, dry_run: bool = False) -> None:
    args = ["python", "train.py", "-s", str(source), "-m", str(output)]
    run_command(args, dry_run=dry_run)
