---
source_blob: 5b0447a99a21e2e454f2c87bcf84b30ff3ae6cb6
---

# The interface

The IngeTrazo window has four areas:

- **3D viewport** (the center): this is where you live. Everything is drawn and edited directly on the model.
- **Toolbars**: drawing, editing, camera and annotation, plus the **Styles**, **Shadows** and **Dimension style** drop-downs. Each button shows its keyboard shortcut on hover. You can drag them wherever you like and the program remembers the layout.
- **Side tray** (right): Entity info, Layers, Scenes, Materials, Components, BIM, Terrain and Survey points. It folds panel by panel and can be resized.
- **Status bar** (bottom): on the left the **Model | Sheet 1 | Sheet 2… | +** tabs —like the Model/Layout tabs in AutoCAD— to go from the model to each sheet and back with one click (`+` creates a new sheet); in the middle the messages of the active tool; on the right the tool, the coordinates, the **VCB** (measurements box) and — if the project is georeferenced — the live UTM coordinate readout.

![The full window: viewport with a model in progress and the side tray with Layers, Scenes and Materials.](../images/principal.jpeg)


## Navigating the model

| Action | How |
|---|---|
| **Orbit** | Middle mouse button (drag), or the Orbit tool (`O`) with the left button |
| **Pan** | `Shift` + middle button, or the Pan tool (`H`) |
| **Zoom** | Mouse wheel (two fingers on the touchpad); `Z` for drag zoom; Zoom Window to frame a region |
| **Frame everything** | Zoom Extents (`F2`, or on the camera toolbar) |
| **Standard views** | Camera menu ▸ Standard Views: top, front, side, isometric… |
| **Perspective / parallel** | `Shift+P` toggles the projection |
| **Clean screen** | `Ctrl+0` hides toolbars and panels; press again to bring them back |

!!! tip "The VCB: exact measurements from the keyboard"
    While you draw, **type the number and press Enter** — there is no need to click in any field. A 3.50 m line: activate Line, click the start point, set the direction, type `3.50` and Enter. It works in almost every tool: distances, radii, angles, numbers of sides, scale factors. It accepts meters, centimeters, inches and feet ([details](../modelado/dibujo.md#medidas-por-teclado-metros-centimetros-pulgadas-pies)).

## Dark mode

The interface always uses a dark theme, designed so the viewport and the panels do not clash. How the **model** looks (background, sky, edges, shadows) is up to you through the [styles](../modelado/estilos-sombras.md).

## Language and preferences

Window ▸ Language switches between Spanish, English and Brazilian Portuguese (applies after a restart). **Window ▸ Preferences…** gathers the rest: auto-save, backup copy, mouse wheel, anti-aliasing, undo steps, the **document units**, suggested units on import and the AI Assistant — see [Preferences](../preferencias.md). This manual uses the English names.
