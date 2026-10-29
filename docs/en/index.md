---
source_blob: 845633de4cd292d33bdd63fa2009475a3bc2e3b5
---

# IngeTrazo Manual

Welcome to the user manual of **IngeTrazo**, the free 3D modeler for civil engineering and architecture: sketch as you would by hand, tag for BIM, place your project on the real terrain and get your drawings out as PDF — all in a single program, offline and open source.

!!! tip "New to IngeTrazo?"
    Start with **[Installation](primeros-pasos/instalacion.md)** and continue with **[Your first model](primeros-pasos/primer-modelo.md)**: in fifteen minutes you put up a small house with exact dimensions.

## What you will find

<div class="grid cards" markdown>

-   :material-rocket-launch: **Getting started**

    ---

    Install the program on Windows or Linux, get to know the interface and build your first model with real dimensions.

    [:octicons-arrow-right-24: Get started](primeros-pasos/instalacion.md)

-   :material-pencil-ruler: **Modeling**

    ---

    The drawing and editing tools: push/pull, follow me, scale, groups and components, materials, layers, scenes, sections, styles and shadows.

    [:octicons-arrow-right-24: Model](modelado/dibujo.md)

-   :material-tag-outline: **BIM and quantity takeoff**

    ---

    Tag walls, slabs and columns; get live quantities and export IFC 4 for your cost estimate.

    [:octicons-arrow-right-24: Tag](bim.md)

-   :material-terrain: **Terrain**

    ---

    Satellite map, 3D terrain, your drone survey and the total-station points — in UTM WGS84.

    [:octicons-arrow-right-24: Georeference](terreno/ubicacion.md)

-   :material-file-document-outline: **Sheet layout**

    ---

    From model to drawing: views at exact scale with exact hidden lines, dimensions anchored to the model, levels, chains, callouts, title block with templates and vector PDF.

    [:octicons-arrow-right-24: Lay out](laminas/index.md)

-   :material-swap-horizontal: **Import and export**

    ---

    Open your `.skp` files (all versions, no converters), DXF and DWG; export IFC, STL, OBJ, glTF and DXF.

    [:octicons-arrow-right-24: Exchange](importar-exportar.md)

-   :material-robot-outline: **Modeling with AI**

    ---

    The AI Assistant inside the app, or Claude driving IngeTrazo over MCP: describe, attach a photo, and the AI writes the recipe the engine runs.

    [:octicons-arrow-right-24: Model with AI](ia.md)

-   :material-folder-open-outline: **Examples to open**

    ---

    Four real documents from the Yanque town square, three with their A3 sheet and PDF: the fastest way to see what the program can do.

    [:octicons-arrow-right-24: Open the examples](primeros-pasos/ejemplos.md)

</div>

## The idea behind IngeTrazo

The name is the thesis: ***trazar*, sketching as in real life**. You draw lines and rectangles, push a face and you have a solid — no rigid families or layers of CAD complexity between your idea and the model. When you need semantics, you add them *on top*: you tag the geometry as a wall or a column and the program gives you the quantities and the IFC.

The complete workflow that IngeTrazo covers together with its sibling [IngePresupuestos](https://ingepresupuestos.com):

```
Terrain (drone, GPS, satellite) → Sketch on top → BIM tagging → IFC → Cost estimate
                                        ↓
                              Sheets → PDF (drawings)
```

## Help and community

- The project lives on [GitHub](https://github.com/ingelibre/ingetrazo): open an *issue* with your sample file if something does not work.
- Direct contact: [ing.sumari@gmail.com](mailto:ing.sumari@gmail.com).
