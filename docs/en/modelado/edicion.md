---
source_blob: 3a67fc1b1568329f63aa9aa235a94108a598f5c0
---

# Editing the geometry

## Push / Pull

**`P`** (or `U`) — the tool that turns drawings into volumes. Click a face, move, type the distance and press Enter.

![Push/Pull in action: the hut gains volume and the VCB (bottom right) receives the exact distance.](../images/modelado.jpeg)


- On a face of a solid: it **thickens or thins** it.
- On a drawing inside a face: it **cuts an opening** when it reaches the opposite face.
- The face's material **travels with the shape**: pushing a painted face gives a painted volume.
- On a **copy of a component** from outside, the push edits the definition: every copy gets the same push (right-click ▸ **Make Unique** first, if you only want to change that one).
- IngeTrazo checks every push: if the operation would leave a broken solid, it **rejects** it with a warning — it never corrupts the model.

## Selecting

**Space** activates Select.

| Gesture | What it does |
|---|---|
| Click | Selects what you touch. Double-click on a face takes the face and its edges; triple-click, everything connected. |
| Drag left → right | **Window**: only what lies fully inside the box. |
| Drag right → left | **Crossing**: everything the box touches. |
| `Shift` + click | **Toggles**: what was selected leaves, what was not joins. This is how you remove an edge or a face from a large selection. |
| `Ctrl` + click | Always **adds**. |
| `Shift` + `Ctrl` + click | Always **removes**. |
| Click on empty space | Clears the selection; with a modifier, leaves it as it is. |
| `Esc` | Deselects everything. |

The selection box uses the same modifiers, and also picks up groups, components and guides.

## Move, Rotate, Scale, Flip

| Tool | Shortcut | Notes |
|---|---|---|
| **Move** | `M` | Select and drag; type the distance (or `X;Y;Z` for a three-axis displacement). Moves points, edges, faces, groups or mixed selections. The arrow keys lock an axis; `Ctrl` moves a **copy**. It snaps to the three axes from any view (X, Y and Z, in their colors) and against faces of other objects. |
| **Rotate** | `Q` | A protractor: the disc is colored by the plane it infers from the hover; the **arrow keys** or `Shift` lock the plane; click the pivot, click the reference, drag the angle or type it. Ticks every 15° with snapping. `Ctrl` rotates a **copy**; dragging from the center defines a folding axis. Accepts slopes like `3:12`. |
| **Scale** | `S` | A yellow box with handles: **corner** = uniform scale, **edge** = two axes, **face** = one axis. The anchor is the opposite side; with `Ctrl` you scale from the **center**; `Shift` forces uniform. In the VCB: a factor (`2`), per-axis factors (`1;2;1`), an absolute size with unit (`3m`, `2'`) or a **negative factor to mirror**. You can retype after releasing. It works on loose geometry, groups, components and images at once. |
| **Flip** | — | Tools ▸ Flip: three translucent red, green and blue planes over the selection; clicking one mirrors it across that plane. `Ctrl` flips a **copy**. Also in the context menu. |

## Eraser, measuring and checking

| Tool | Shortcut | Notes |
|---|---|---|
| **Eraser** | `E` | Click or drag over edges. Erasing an edge dissolves the faces that depended on it. **`Shift` + Eraser hides** the stroke instead of erasing it. |
| **Tape Measure** | `T` | Measures between two points and creates construction **guides**: from an edge, a parallel guide; from an **axis** (click the red, green or blue axis, also with an empty document), a guide parallel to the axis at the distance you type; from a **named point** (endpoint, center, intersection, origin), a **guide point with its dashed segment** back to the starting point. |
| **Protractor** | `Shift+H` | Measures angles and creates angular guides. |
| **Delete Guides** | — | Edit ▸ Delete Guides, once they have done their job. |

## Divide

Right-click a line or an arc ▸ **Divide…** and the number of segments:

- A **line** is split into N equal pieces, with a vertex at each cut ready to snap to.
- An **arc or circle** is measured along its chain and becomes **N independent arcs**, each selectable on its own: a circle divided in four is four quarters.
- The faces bordering the edge receive the new vertices without breaking.
- With several edges selected, they are all divided; a single `Ctrl+Z` undoes it.

## Hiding edges { #ocultar-aristas }

To make a surface made of several faces look continuous without erasing anything:

- Select the edges and **Edit ▸ Hide Edges** (or right-click ▸ Hide Edges), or run the Eraser with `Shift`.
- **Edit ▸ Unhide All Edges** brings them back (all of them in the context you are in: outside a group, the loose ones; inside, the group's).
- A hidden edge cannot be clicked until it is shown; sheets and exports respect it. With **View ▸ Hidden Geometry** (or **Hidden Objects**) on, hidden things are drawn as ghosts and **can be clicked and selected** like anything else; when you turn the view off, they leave the selection.

## Groups and components

- **Make Group** (`Ctrl+G`): the selection becomes a group — isolated geometry that does not "stick" to the rest. **Double-click** to enter and edit it; `Esc` or click outside to leave. While you edit, the rest of the model is **dimmed** (Camera ▸ Rest of model while editing).
- **Explode** (`Ctrl+Shift+G`) dissolves it one level. **Merge Groups** fuses several into one.
- **Make Component…** (`G`): the selection becomes a named **definition** and a first instance. Copying it (`Ctrl+C`/`Ctrl+V`, or Move with `Ctrl`) creates instances that **share the definition**: you edit one and they all change ([details](organizacion.md#componentes-editas-uno-cambian-todos)). Moving an instance does not duplicate geometry.
- **Make Unique** (right-click) detaches a copy so you can edit it alone.
- Copy and paste works between documents; pasting shows a **solid preview** following the cursor, with colors and textures, and stamps only once.

## Undo

`Ctrl+Z` / `Ctrl+Shift+Z` (or `Ctrl+Y`). **Every** operation goes through the history — you can always go back, even full imports and whatever the [AI](../ia.md) draws. The history keeps **200 steps** by default; change it in [Preferences ▸ General](../preferencias.md#general) (0 = unlimited).
