# coffee-nerf-cad

Local-first reconstruction pipeline for turning multi-view phone photos, video frames, known camera poses, or turntable captures into printable mesh outputs.

Primary targets are watertight STL and unit-aware 3MF. STEP export is included as an experimental workflow because mesh-derived STEP is approximate and not true parametric CAD.

## Pipeline

```text
Input images/video
-> COLMAP pose estimation
-> Nerfstudio reconstruction
-> Gaussian/TSDF/marching-cubes mesh extraction
-> Open3D/Trimesh cleanup
-> STL / 3MF / experimental STEP export
-> CAD Explorer inspection
```

## MVP Status

This repo starts as a practical scaffold:

- CLI wrappers for COLMAP, Nerfstudio training, mesh export, cleanup, validation, and export.
- Reproducible configs in `configs/`.
- Lightweight Trimesh-based sample generator for STL, 3MF, and experimental STEP wrapper output.
- Placeholders for the `earthtojake/text-to-cad` harness integration.

Heavy reconstruction tools are expected to be installed locally. The project does not vendor Nerfstudio, COLMAP, Gaussian Splatting, FreeCAD, or OpenCascade.

## Quick Start

```powershell
python -m venv .venv
. .venv/Scripts/Activate.ps1
python -m pip install -U pip
python -m pip install -e .[mesh,cad]
python -m coffee_nerf_cad.cli example
```

The example command writes a simple printable cube to:

- `outputs/meshes/example_cube.obj`
- `outputs/stl/example_cube.stl`
- `outputs/3mf/example_cube.3mf`
- `outputs/step/example_cube.step`

## Reconstruction Workflow

1. Add source images to `input/images/` or videos to `input/videos/`.
2. Estimate poses:

   ```powershell
   python -m coffee_nerf_cad.cli colmap --images input/images --output outputs/colmap
   ```

3. Train Nerfstudio:

   ```powershell
   python -m coffee_nerf_cad.cli train --data outputs/colmap --output outputs/nerfstudio
   ```

4. Extract mesh:

   ```powershell
   python -m coffee_nerf_cad.cli extract --config outputs/nerfstudio/config.yml --output outputs/meshes/reconstruction.ply
   ```

5. Clean and export:

   ```powershell
   python -m coffee_nerf_cad.cli clean --input outputs/meshes/reconstruction.ply --output outputs/meshes/reconstruction_clean.glb
   python -m coffee_nerf_cad.cli export --input outputs/meshes/reconstruction_clean.glb --name reconstruction
   ```

## text-to-cad Harness

Add the harness as a submodule or local checkout:

```powershell
git submodule add https://github.com/earthtojake/text-to-cad text-to-cad
```

Use source-controlled generation commands and stable geometry references such as `@cad[...]` for review. Do not hand-edit derived STL, 3MF, STEP, GLB, or render outputs.

## STEP Export Modes

- Mode A: mesh wrapper STEP. Stores triangulated geometry in an approximate STEP-like exchange file when OpenCascade is unavailable.
- Mode B: experimental BREP approximation. Intended for future FreeCAD/OpenCascade workflows and feature recognition research.

## Roadmap

- MVP 1: input images -> Nerfstudio -> mesh -> STL.
- MVP 2: cleanup, watertight repair, 3MF export.
- MVP 3: CAD Explorer renders, topology sidecars, `@cad[...]` references.
- MVP 4: experimental STEP through OpenCascade or FreeCAD.
- MVP 5: local viewer or web UI.

## Engineering Notes

NeRF and Gaussian reconstructions are mesh-first. They are useful for printing and inspection, but they are not true editable CAD solids. Treat STEP output as lossy until a dedicated mesh-to-BREP reconstruction path exists.
