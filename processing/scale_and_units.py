from __future__ import annotations

from pathlib import Path

import click

from coffee_nerf_cad.mesh import export_mesh, load_mesh


@click.command()
@click.option("--input", "input_path", type=click.Path(path_type=Path), required=True)
@click.option("--output", type=click.Path(path_type=Path), required=True)
@click.option("--scale", type=float, required=True)
@click.option("--unit", default="mm", show_default=True)
def scale_and_units(input_path: Path, output: Path, scale: float, unit: str) -> None:
    mesh = load_mesh(input_path)
    mesh.apply_scale(scale)
    mesh.metadata["units"] = unit
    export_mesh(mesh, output)


if __name__ == "__main__":
    scale_and_units()
