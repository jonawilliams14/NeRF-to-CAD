from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def export_mesh_wrapper_step(mesh: Any, output: Path, name: str) -> None:
    """Write an experimental STEP wrapper documenting mesh triangles.

    This is not parametric CAD. It is a conservative placeholder for Mode A
    until an OpenCascade-backed triangulated-shell writer is wired in.
    """
    output.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "ISO-10303-21;",
        "HEADER;",
        "FILE_DESCRIPTION(('coffee-nerf-cad experimental mesh wrapper'),'2;1');",
        f"FILE_NAME('{name}','{timestamp}',('coffee-nerf-cad'),('coffee-nerf-cad'),'','','');",
        "FILE_SCHEMA(('CONFIG_CONTROL_DESIGN'));",
        "ENDSEC;",
        "DATA;",
        f"/* mesh_vertices={len(mesh.vertices)} mesh_faces={len(mesh.faces)} */",
        "/* This file records mesh-derived geometry metadata only. */",
        "/* Use STL or 3MF as the authoritative printable artifact. */",
        "ENDSEC;",
        "END-ISO-10303-21;",
    ]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
