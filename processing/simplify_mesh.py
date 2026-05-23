from __future__ import annotations

from pathlib import Path

import click

from coffee_nerf_cad.mesh import export_mesh, load_mesh


@click.command()
@click.option("--input", "input_path", type=click.Path(path_type=Path), required=True)
@click.option("--output", type=click.Path(path_type=Path), required=True)
@click.option("--faces", type=int, required=True)
def simplify(input_path: Path, output: Path, faces: int) -> None:
    mesh = load_mesh(input_path)
    simplified = mesh.simplify_quadric_decimation(face_count=faces)
    export_mesh(simplified, output)


if __name__ == "__main__":
    simplify()
