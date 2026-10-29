---
source_blob: f458d957dfcc37817abad501af3ba2f62f3e716c
---

# Layers, scenes and organization

## Layers

The **Layers** panel in the tray organizes the model's visibility (the list grows up to 12 rows and from there on scrolls by itself, just like the Components list):

- **+ Layer** creates one; each entity's selector (or the Entity info panel) assigns it.
- The **eye** shows/hides everything that lives on the layer — furniture, references, services.
- When importing a `.skp`, its layers/tags arrive with their original visibility.
- Deleting a layer does not erase its geometry: it moves to the default layer.

!!! note "Layers = visibility, not isolation"
    Layers control what is seen; geometry on different layers **does touch** if it shares space. To isolate geometry, use **groups**.

## Scenes

The **Scenes** panel stores named views:

- **+ Scene** captures the current camera **and** which layers are hidden.
- **Double-clicking** a scene restores it.
- Scenes are saved in the `.igz`, come in with imported `.skp` files, and are the **view sources** of the [sheet composer](../laminas/marcos.md): a well-prepared "Plan" scene is your floor plan drawing.

## Entity info

The **Info** panel shows and edits the essentials of the selection: length of an edge, area of a face, layer, material, and the BIM metadata if it has any.

## Scenes: what they remember

Besides the camera and the layers, each scene stores the active **style**, the active **section plane** and whether cuts are shown, and the **sun time** of the shadows. `F2` renames the scene (or layer) selected in its list; **Update** recaptures it from the current view.

## Visual style, sections and shadows

- **Styles** (Default, Architectural, Hidden line, X-ray… and your own), **shadows with the real sun** and the clean screen have their own page: [Styles, shadows and display](estilos-sombras.md).
- **Section planes** cut the model so you can look inside: [Section planes](secciones.md).
- A scanned drawing or a photo to trace: [Reference images](imagenes-referencia.md).
- **Face culling**: back faces are painted grayish blue so you can spot flipped faces at a glance.
- File ▸ Export ▸ **Image** saves a high-resolution capture of the viewport.

## Components: edit one, they all change { #componentes-editas-uno-cambian-todos }

Copies of a component (Ctrl+C / Ctrl+V, or Move with Ctrl) share a single definition:

- **Double-click any copy** to open it for editing. Draw, push, erase inside; when you leave (Esc or click outside), the change goes to **all** copies. The whole edit is undone in a single Ctrl+Z step.
- **Push / Pull on a copy from outside** also edits the definition: the other copies get the same push.
- **To change a single copy**, right-click ▸ **Make Unique** before editing it: that copy is detached and the others keep sharing the definition.
- Looking inside a component and leaving without touching anything changes nothing.
- **Make Component…** (`G`) turns the selection into a named definition; **Merge Groups** fuses several groups into one; **Explode** (`Ctrl+Shift+G`) dissolves one level.
- Components imported from `.skp` with **subgroups** keep their hierarchy: they move and copy as a single object and the file does not bloat. Editing inside one of them breaks it up in that document (the usual behavior when editing a nested component).
