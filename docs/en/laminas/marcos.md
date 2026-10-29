---
source_blob: 6de4b58e03f1a2eec8fa825eb5e035c1f029e844
---

# View frames and scale

A **view frame** is a window onto the model placed on the sheet. It is the central item of the composer.

## Creating a frame

With the **Frame** tool, draw the rectangle on the sheet (two clicks or a drag), or use **Add frame** in the panel. In its properties you choose:

- **View**: the current camera, a **standard view** (plan, front, sides, isometric…) or any of your **saved scenes** — a "First floor plan" scene with its layers, section and style set up is your drawing, ready.
- **Scale 1:N**: the composer's sacred equation — *1:100 in a frame 200 mm high shows exactly 20 m of model*. Always, without approximations. Change the scale and the content is reframed exactly. The combo offers the usual scales and accepts any other.
- **Enlargement scales**: for small parts the combo also offers **2:1, 5:1 and 10:1**, and accepts them typed that way. The sheet labels them accordingly ("ESC. 10:1"), as does the `{escala}` field of the title block.
- **Frame size** in mm, by dragging or numerically; **Frame the model** centers the view on the whole model.
- The frame's **Printed border**: thickness and color, or none.

## Editing the view inside the frame

**Double-clicking** a frame enters view editing: the frame is highlighted and the mouse works **inside** it as in the modeler —drag to pan, middle button or `Ctrl`+drag to orbit, wheel to zoom— until `Enter`, `Esc` or a click outside. Each gesture is an undo step and the frame stays in editing even if you scroll the sheet. That manual framing belongs to the chosen view source: if you switch the frame to another scene or standard view, it is discarded and the frame starts from the scene's camera.

**Rotating the view**: `Shift`+drag rotates the drawing inside the frame around its center, snapping every 15°; or type the angle in the panel's **View rotation** (positive = clockwise, the same angle you give the north arrow). The frame and everything else stay still; what comes out of the camera rotates: the render, the hidden lines, the snapping, the anchored dimensions, the section marks and the DXF.

## Render styles

| Style | What it shows |
|---|---|
| **Model style** | The model as seen in the viewport: materials, textures, shading, shadows. |
| **Saved styles** | Any style from the library (Hidden line, Architectural, X-ray, your own…), per frame. **A new frame is born in Architectural**: white background, edges and profiles. |
| **Vector (hidden lines removed)** | The drawing a draftsman would ink: **hidden lines are removed by exact calculation**, as real vectors for the PDF and the DXF. |

Below the style, the **Paper background** checkbox renders on white without sky or ground, whatever the style's background: a frame in **X-ray** (to show the rebar) or in Default no longer brings the model's gray onto the sheet.

### Pens and poché of the Vector style { #plumas-y-poche-del-estilo-vector }

The Vector style classifies each stroke and draws it with its pen, like an office drawing:

| Class | Default pen | What it is |
|---|---|---|
| **Section cut** | 0.50 mm | Where the section plane passes through a solid. |
| **Profiles** | 0.35 mm | Silhouettes and outlines against the background (the usual profile weight). |
| **Edges** | 0.18 mm | All other edges, between two visible faces. |

Where the section cuts a **closed solid**, the frame fills the cut (the *poché*): **solid** or **hatched at 45°**, with color and hatch spacing to your liking; an open surface stays blank. Pens and fill are set in the panel's **Vector pens** section, which only appears with this style. The DXF export distributes the classes into the `VISTA`, `VISTA-PERFIL` and `VISTA-CORTE` layers for your CAD's pen table.

## View title

Tick **View title** in the frame's panel and choose the style:

- **Numbered, rule under**: a bubble with the view **number** on top and the **sheet** below, bold title, "ESC. 1:N" and a baseline running to the edge of the frame. With an optional subtitle ("N.P.T. +0.15").
- **Vertical bar**: a strip to the left of the frame with title, subtitle and scale rotated 90°, and the bubble at the foot — the habit of Brazilian drawings.
- **Simple line**: the usual centered line.

Title, subtitle, number and sheet accept dynamic fields: `{lamina}` reads the title block, `{escala}` the scale of that frame, `{escena}` the scene name. Alignment, position (below or above) and text size are in the same panel. Everything is edited live, without recomputing the view.

## Section marks { #marcas-de-seccion }

Tick **Section marks (A–A)** and the frame draws the trace of each section plane of the model that crosses its view: the dash-dot cutting line, the arrows toward the side the section looks at and the **plane's letter** in bubbles at both ends. That way the plan says where "Section A-A" runs. The letter is the plane's symbol ([Section planes](../modelado/secciones.md)); without a symbol, A, B, C… in order. A plane parallel to the view leaves no mark.

## Frame extras { #extras-del-marco }

- **Model annotations**: the dimensions and leader texts drawn in the modeler appear in the frame, with the text height you choose.
- **Alignments and chainages**: [routes](../terreno/rutas-perfil.md) drawn on the terrain are always drawn in the views (in cyan, with their nodes); with **Chainage marks** the plan frame adds the stationing marks (0+000, 0+020…) at the interval you set or an automatic one — the same one the sheet's terrain profile uses, so they match.
- **Coordinate grid**: the grid in model meters over the view (the habit of gridded drawings), at the spacing you choose.
- **Update view** re-renders the frame from the current model; **Update views** (sheet bar), all of them. With **Auto-render** on (status bar), frames update by themselves when the model changes — frames are not snapshots, they are live windows.

!!! tip "The recommended workflow"
    Prepare **scenes** in the modeler (plan with the right layers and section, front elevations) and in the composer just place them at scale. When the project changes, the sheets update by themselves.
