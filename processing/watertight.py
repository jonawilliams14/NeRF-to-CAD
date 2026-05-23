from __future__ import annotations

from pathlib import Path

import click

from coffee_nerf_cad.mesh import clean_mesh, export_mesh, load_mesh, mesh_report


@click.command()
@click.option("--input", "input_path", type=click.Path(path_type=Path), required=True)
@click.option("--output", type=click.Path(path_type=Path), required=True)
def watertight(input_path: Path, output: Path) -> None:
    mesh = clean_mesh(load_mesh(input_path))
    mesh.fill_holes()
    export_mesh(mesh, output)
    click.echo(mesh_report(mesh))


if __name__ == "__main__":
    watertight()
