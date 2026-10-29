---
source_blob: 829da49dcedb9cdfe832f720fb5436acfa4cbbaa
---

# Your first model

Let's put up a small 6 × 4 m house with exact dimensions. It is the essential walkthrough: draw, extrude, cut openings and save.

## 1. The floor plan

1. Activate **Rectangle** (`R`).
2. Click the origin, move the mouse and **type** `6,4` and Enter. You have the exact 6 × 4 m floor plan.

!!! tip "Inferences guide you"
    While you draw you will see colored points and lines: endpoints, midpoints, axes, parallels and perpendiculars. These are the **inferences** — let them snap you and your lines will land exactly, effortlessly.

## 2. Raising the walls

1. Activate **Push / Pull** (`P`).
2. Click the rectangle's face, move up, type `2.7` and Enter. The box is 2.70 m high.

## 3. Cutting the door and the window

1. With **Rectangle**, draw the door opening on the façade (for example `0.9,2.1`).
2. **Push / Pull** that rectangle inward until the inference marks the opposite face of the wall: the opening is cut through.
3. Repeat with the window.

## 4. The roof

1. Draw a **Line** (`L`) through the midpoint of the top face, from side to side.
2. With **Move** (`M`) select that line, move it up, type the ridge height (for example `1.2`) and Enter. You have a gable roof.

## 5. Paint and measure

- **Paint** (`B`) opens the materials: pick a color or texture and click each face. With `Alt` you pick up the material of an existing face (eyedropper).
- **Dimension** (`D`): click two points and pull the dimension out — it stays anchored to the model.

## 6. Save

`Ctrl+S` saves the document as **`.igz`**, IngeTrazo's native, open format. If the model has textures, they travel **inside** the file: you can take it to another PC and it opens complete. The document also stores **the camera** you left it with: when you open it you see what you were seeing (and **File ▸ New** goes back to the default view). A large `.igz` shows a **progress bar** while it loads; the last ten are under **File ▸ Open Recent**.

!!! note "Real solids"
    IngeTrazo guarantees that operations leave **watertight** (closed) solids. If an operation would break the volume, the engine rejects it instead of corrupting the model — that is what makes the BIM takeoff and 3D printing reliable.

## What next?

- All the drawing tools, in detail: **[Drawing tools](../modelado/dibujo.md)**.
- Tag the little house and get its quantities: **[BIM and quantity takeoff](../bim.md)**.
- Put real terrain underneath it: **[Project location](../terreno/ubicacion.md)**.
