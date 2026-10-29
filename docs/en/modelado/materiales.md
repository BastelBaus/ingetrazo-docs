---
source_blob: 66d4a93acc4fde36c40c828fe2c1c73ef5f75f1a
---

# Materials, textures and components

## Paint

**`B`** opens the Paint tool and the **Materials** panel in the tray:

- Pick a **color** or a **texture** and click faces (or whole groups).
- **Painting a group or component from outside** paints the whole object with the usual rule: a face's own material takes precedence over the container's, so **only faces with the default material** wear the group's (on both sides); when you explode it, they keep it. Two copies of the same component can have different colors, the container's material travels in the `.igz`, and it is respected when importing a `.skp`.
- **Eyedropper**: holding `Alt`, a click *picks up* the material under the cursor instead of painting it (on a default face of a painted group, it picks the group's) and makes it the **active material** in the panel.
- **+ Color…** and **+ Texture…** create your own materials (with an optional name); you can bring in any PNG/JPG image as a texture.

### What comes with the program

- **427 textures** ready to use (wood, stone, brick, floors, metals, vegetation…), each with its **real size** in meters: a 30 cm tile measures 30 cm in your model.
- **213 RAL Classic colors**, with their name and code.
- **Named materials**: a material has an identity, not just a color. **In model** lists the ones you already use; right-clicking one lets you **edit and restamp** every face that carries it at once. The name travels to OBJ, and [Model Info](../extensiones.md) measures the m² per material.

## Textures

- The projection is **compatible with the `.skp` format**: planar per face, and the textures of an imported `.skp` arrive with their exact pins.
- **The texture mapping travels with the geometry**: moving, rotating, scaling or pasting a textured face does not shift its texture.
- Textures **travel inside the `.igz` document**: the file is self-contained, you take it to another PC and it opens complete.
- **Translucent** materials (glass) and **cut-out** textures (meshes, lattices, leaves) display correctly in the viewport and cast shadows according to their pattern.

## Faces

- Each face has a **front and a back** (the back is drawn grayish blue). **Reverse Faces** (right-click) flips them — it matters for texturing and for exporting.
- **Soft edges**: curved surfaces (cylinders, extruded arcs) display as continuous; their control edges are "soft" and do not clutter the drawing. The ones you want to hide without erasing: [hide edges](edicion.md#ocultar-aristas).

## Components and scale figures

The **Components** panel in the tray places ready-made models:

- **With the program** come 8 models (doors, windows, furniture) and **6 scale figures** — 1.75 m people who always face the camera, to give scale to any view. They go by their first names; **Sumari** is the house figure.
- **More components…** (also under **Help ▸ Get more models and textures…**) opens the **online library of 1,510 models** —furniture, doors, windows, trees, vehicles, people— with thumbnail, category and **real size in cm**. Browsing costs kilobytes: only the model you click is downloaded, and it is kept for next time. Each one carries its license and author (CC0, CC-BY or Free Art).
- A placed model is a **component**: it is placed with one click, Move (`M`) adjusts it, and its copies share the definition.
- Each model arrives **as its file describes it**: vertical axis, declared size, textures and smoothing groups in place.

!!! tip "Clearing the texture cache"
    Images coming from imported `.skp` files are stored in a program cache (never next to your files). File ▸ Import ▸ Clear imported texture cache… empties it if you need the space.
