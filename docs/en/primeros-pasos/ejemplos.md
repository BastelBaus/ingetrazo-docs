---
source_blob: 7e8cbd95eb7c5e9c2452f19b3139010183f90a58
---

# Examples to open

Four real documents, drawn with IngeTrazo for the remodeling of the Yanque town square, Chichas district (Arequipa, 2026), by Ing. Marco Sumari. All four come with their **A3 sheet ready** and, next to it, the PDF exported from it so you can compare.

**Download them:** all together in every release as [`IngeTrazo-ejemplos.zip`](https://github.com/ingelibre/ingetrazo/releases/latest/download/IngeTrazo-ejemplos.zip), or one by one from the [`examples/`](https://github.com/ingelibre/ingetrazo/tree/main/examples) folder of the repository (and from the *Ejemplos* section of [ingetrazo.com](https://ingetrazo.com/#ejemplos)). They need IngeTrazo 0.3.15 or later.

| File | What it is | What it teaches |
|---|---|---|
| `pileta-fuente-yanque.igz` (+ `.pdf`) | The central fountain of the square: octagonal pedestal, fluted shaft, two wavy-rimmed basins, sidewalk with a bullnose edge | Repeated components (22 instances), **shadows with the real sun**, section plane; sheet with front, 3D, plan and section at 1:40, reference photo and title block |
| `banca-pergola-yanque.igz` (+ `.pdf`) | Concrete bench with a timber pergola | Components, five saved **scenes**; sheet with four views, **23 dimensions** and 12 leader labels |
| `luminaria-solar-yanque.igz` (+ `.pdf`) | 4.5 m solar street-light pole: truncated-cone pedestal, buried footing with its 3/8" rebar, two floodlights with a panel | Modeling by recipes with the [AI](../ia.md), rebar detail, sheet with four views and a detail of the pedestal |
| `arco-yanque.igz` (+ `.pdf`) | "YANQUE" welcome arch following structural sheet E02: concrete, **all the rebar** (footings, columns, segmental arch, beam, tympanum), ashlar capitals, four ornamental lampposts, letters and sculpture | **X-ray** to see the rebar, section planes, "face the camera" images, textures; sheet D04 with front, side, plan and 3D at 1:50, details of the letters and sculpture (1:25) and of the capital (1:20), **levels**, **ground line** and leader labels |

## What to look at in each one

- **Open the document** (File ▸ Open, or double-click the `.igz`) and go through the **scenes** in the Scenes panel with a double-click: each one stores camera, layers and active section.
- **The sheet**: the *Sheet 1* tab in the status bar (or File ▸ Sheet composer). Select a frame and look at its panel: scale, style, caption. Double-click a frame to orbit inside it. **Export PDF…** and compare with the PDF that comes alongside.
- **The rebar of the arch and the street light**: Camera ▸ Style ▸ **X-ray**, or activate the document's section plane (Camera ▸ Section Cuts) and move it with the Move tool.
- **The groups**: everything has a name ("Acero columna C1 izq 10 Ø5/8"", "Farola ornamental blanca der adelante"…). Double-click to enter and edit; `Esc` exits.

!!! note "License"
    The documents (models, sheets and PDF) belong to Ing. Marco Sumari Tellez and are published under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/): use, modify and share them crediting the source. IngeTrazo's code remains under the GPL-3.0.
