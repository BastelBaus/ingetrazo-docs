---
source_blob: a1b3b7a75c31ccbef97c3e345547c8b208065f64
---

# Reference images

A scanned drawing, an aerial photo, a sketch: **File ▸ Import ▸ Image (PNG / JPG)…** places it in the model as a plane to **trace over**.

## Placing and adjusting

1. Import the image: it appears on the ground plane, on its own **Images** layer.
2. **Right-click ▸ Image size…** to give it its real dimensions in meters — the width of the drawing you scanned, the side of the plot.
3. **Move** (`M`), **Rotate** (`Q`) and **Scale** (`S`) treat it like any entity: take it to its place, rotate it, scale it using two known points.
4. **Right-click ▸ Lock** once it is in place: locked, it **does not accept clicks** (it is not selected or moved by accident) but it **still provides a working plane and snapping** on its edges — the tracing state.

## Tracing

- The drawing tools work **on the image**: Line, Rectangle and Arc land on its plane, with the usual inferences.
- The image is **reference only**: it does not enter the geometry, the takeoffs or the 3D exports; turn its layer off when you are done.
- It travels **inside the `.igz`**, like textures: the document stays self-contained.

!!! tip "Drawings in DWG/DXF"
    If the drawing is in CAD, do not trace it: **File ▸ Import ▸ AutoCAD DXF/DWG** brings it in as real lines by layer — see [Import and export](../importar-exportar.md#cad-dxf-y-dwg).
