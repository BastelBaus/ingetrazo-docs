---
source_blob: dea27e7f254d72923a172eaaaea821c2745dfb17
---

# Import and export

## The native format: `.igz`

Open and documented. Without textures it is readable JSON; with textures it becomes a self-contained container (the images travel **inside**, with no paths from your machine). Sheet layouts, layers, scenes, sections, shadows, BIM and georeferencing are stored there too. Atomic saving: a power cut does not corrupt the file, and with the `.igz.bak` copy from [Preferences](preferencias.md) it even survives a full disk. An `.igz` from a newer version opens in an older one (anything unknown is ignored).

## Importing `.skp` — native

![A freshly opened `.skp`: the original geometry, materials and layers arrive intact.](images/importar.jpeg)


**File ▸ Import ▸ SKP (.skp)…**, or **double-click** the file, or drag it onto the window.

The importer is **in-house and open source** (the [OpenSKP](https://github.com/iamahsanmehmood/openskp) project, to which IngeTrazo contributes): it reads the `.skp` directly, **without converters or other installed programs**, across all its eras — from the old formats (2013–2020) to the current ones.

What comes in:

- Complete geometry, **groups and components** (instances stay shared: moving one lamppost does not drag the rest; nested components keep their hierarchy).
- **Materials and textures**, including colorized ones, translucency, per-side materials, positioned textures and "always face camera" billboards.
- **Layers/tags** with their visibility, **scenes** (camera + layers per scene), **linear dimensions** and **leader texts**.
- Verified with real project files: exact bounding box and 0.00 % area difference against the original model.

## CAD: DXF and DWG { #cad-dxf-y-dwg }

**File ▸ Import ▸ AutoCAD DXF (.dxf)…** or **AutoCAD DWG (.dwg)…** brings in a 2D or 3D CAD drawing:

- Each **layer** arrives as a tagged group; **curves** (arcs, circles, polylines) as a single entity selectable with one click; **blocks** as components with their instances; 3D faces as faces, merging coplanar ones. Text and dimensions are skipped.
- **The unit is suggested by measuring the drawing** (a DWG header often lies); the dialog lets you confirm it. Distant UTM coordinates are recentered automatically.
- DWG is converted with LibreDWG, which ships inside the Linux package (on Windows, for now, export to DXF from your CAD program).
- Double-clicking a `.dxf` or `.dwg` also opens it.

For the reverse direction, [export a sheet view as DXF](laminas/exportar.md#dxf-hacia-ingecad-autocad).

## Other formats

| Format | Import | Export | Notes |
|---|:-:|:-:|---|
| **COLLADA (.dae)** | ✔ | ✔ | The export includes the geolocation — Blender opens it with your site's sun for sun studies. |
| **OBJ** | ✔ | ✔ | With materials (MTL). On import you are asked for the unit. |
| **glTF / GLB** | ✔ | ✔ | Native import with textures and hierarchy; PBR export + geolocation — the format of web viewers and modern Blender. |
| **STL** | — | ✔ | Binary, for 3D printing. Watertight solids guaranteed. |
| **IFC 4** | — | ✔ | The BIM bridge. See [BIM and quantity takeoff](bim.md). |
| **DXF (R12)** | ✔ | ✔ | Comes in as a CAD drawing; goes out as the vector view of a sheet, with one layer per line class. |
| **DWG** | ✔ | — | Via LibreDWG (Linux). |
| **Image** | ✔ | ✔ | Comes in as a [reference image](modelado/imagenes-referencia.md) to trace; goes out as a high-resolution capture of the viewport. |
| **WebODM/ODM** | ✔ | — | The drone survey. See [Terrain](terreno/dron.md). |
| **Survey CSV** | ✔ | — | P,N,E,Z total-station points. See [Terrain](terreno/rutas-perfil.md). |
| **KML / GeoJSON** | ✔ | — | Georeferenced alignments and polygons. |
| **PDF** | — | ✔ | The sheets, as vectors. See [Export PDF](laminas/exportar.md). |

Every import is **one undo step**: `Ctrl+Z` removes it completely.
