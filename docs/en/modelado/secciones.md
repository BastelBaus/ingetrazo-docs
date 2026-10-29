---
source_blob: 9d77106f65aaf70e43b3ffe3d57222c9b189d272
---

# Section planes

A **section plane** cuts the model so you can look inside — the plan of a house at window height, the cut through the axis of a fountain, the rebar inside a column. It works like this: you place the plane, the model is clipped live, and the sheets draw the cut with its fill.

## Placing a plane

1. **Tools ▸ Section Plane** (also on the toolbar).
2. Move the cursor over the model: the plane **aligns itself** with the face underneath (or with the ground).
3. To set the orientation without depending on the face: the **arrow keys** lock the axis — `↑` cuts horizontally (Z plane), `→` vertically along X, `←` vertically along Y, `↓` goes back to the face — and `Shift` freezes the current inference. The plane always faces the camera: placed in front of the model, what gets hidden is what is on your side.
4. **Click** to place it. You are asked for a **name** and a **symbol** (the letter that will appear on the sheets: A, B…). You can keep the ones it suggests: the symbol is the **next free letter**, so cuts come out A, B, C… and the sheet mark reads "A … A", as technical drawing requires. If you never change them, tick **"Don't ask again"**: planes will be born with the default name and symbol ([Preferences ▸ General](../preferencias.md#general) turns the dialog back on). Once the plane is placed, the tool **finishes** and returns to Select.

To change them later, right-click the section plane ▸ **Name and symbol…**.

The newly placed plane is **active** and cuts immediately.

## Working with sections

- **Only one active plane per context.** Placing another one activates it and deactivates the previous one. **Double-clicking** a plane toggles whether it is active.
- **Move and rotate** the plane with the Move (`M`) and Rotate (`Q`) tools: grab it by its frame. This is how you "walk" a cut through the model.
- **Right-click** the plane: **Reverse** (cuts toward the other side), **Active Cut**, **Align View** (the camera goes perpendicular to the plane — the framing of a section drawing).
- **`Del`** deletes it; `Ctrl+Z` brings it back.
- The frame of a plane perpendicular to an axis is drawn **in that axis's color** (red, green or blue; oblique ones, gray), so you can see at a glance where each one cuts.
- **Camera ▸ Section Planes** shows or hides the planes' frames; **Camera ▸ Section Cuts** turns the clipping on or off without deleting anything.
- The edges where the plane passes through a solid are drawn **thick**, and the style can fill the cut (**Section Fill**, with its color, in the [style editor](estilos-sombras.md)).
- The drawing and selection tools **do not reach what the cut hides**: you snap to and select only what is visible.

## Sections, scenes and sheets

- Each **scene** remembers which plane was active and whether cuts were shown: a "Plan" scene with the horizontal cut at 1.20 m is your architectural floor plan, and another "Section A-A" your section.
- In the **sheet composer**, a frame showing that scene draws the cut: in the **Vector** style, the cut edges get their thick pen and the cut solid is filled with **poché** (solid or hatched) — see [View frames](../laminas/marcos.md#plumas-y-poche-del-estilo-vector).
- **Section marks**: a plan frame can draw the trace of each section plane that crosses it, with its arrows and the plane's letter in bubbles — so the plan says where "Section A-A" runs ([annotation on sheets](../laminas/marcos.md#marcas-de-seccion)).
- Planes are saved in the `.igz` and restored with the document.

!!! tip "Seeing the rebar"
    To check reinforcement or services inside the concrete, combine a section plane with **Camera ▸ Style ▸ X-ray**: the cut shows the exact position and X-ray the rest of the reinforcement through the faces. The arch and street-light [examples](../primeros-pasos/ejemplos.md) are designed for exactly that.
