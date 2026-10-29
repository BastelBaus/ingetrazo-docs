---
source_blob: 6f05af3c9838a55fc6d539afd9e8803ad17849b2
---

# Routes, profile and survey points

## The Route tool

**`Y`** activates Route (GeoPath): it draws georeferenced alignments — the centerline of a road, a canal, a property line.

- Click by click on the map, the 3D terrain or your drone survey.
- The live label shows the **length, elevation and grade (%)** of each segment.
- Routes live in their own subsystem: they do not mix with the model's geometry.

## Longitudinal profile

With a route selected, the **profile panel** shows the longitudinal profile instantly, sampled from the best surface available (your drone flight if there is one; otherwise, the DEM):

- **Chainages** on the horizontal axis, elevations on the vertical.
- Export to **CSV** (for your spreadsheet or geometric design) and to **PNG**.
- **On the sheets**: the composer's **Profile** tool draws the profile on the sheet with horizontal and vertical scale, exaggeration, chainages and elevations; and plan frames show the alignment with its **chainages** (0+000, 0+020…), with the same interval as the profile, so they match. See [View frames](../laminas/marcos.md#extras-del-marco).
- **Tools ▸ Terrain profile of selection** extracts the profile of any selected polyline; right-clicking a route lets you choose whether its surface is flat, draped over the relief or just the line, and **Convert Path to Geometry** turns it into model edges.

## Total-station / GPS points

File ▸ Import ▸ **Survey points (CSV)**: the classic `P,N,E,Z,description` in UTM.

- Specify the **zone and hemisphere** when importing (if the project has no datum yet, the first point anchors it).
- The points appear as markers with their number and description, and the drawing tools **snap to them with exact precision** — you draw the property line by joining your real points.

## KML and GeoJSON

Import alignments and polygons from Google Earth or QGIS: they arrive georeferenced at their correct position (elements without their own altitude are placed on the project's reference plane).
