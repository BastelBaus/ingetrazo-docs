---
source_blob: 2e8095d9d437fb2aea3eabb994f398aa7d9d4c9c
---

# BIM and quantity takeoff

IngeTrazo's BIM is not a cage of families: **you model freely and tag**. The tag is metadata on the selected geometry — what is tagged goes into the takeoff and the IFC; everything else is drawing.

![An industrial shed with the BIM panel open: the selected columns are tagged as IfcColumn.](images/bim.jpeg)


## Tagging

In the **BIM** panel of the tray:

1. Select the geometry (the wall you just raised, the column, the door).
2. Choose the **class**: wall, slab, column, beam, door, window, stair, railing, roof… (15 IFC classes).
3. **Assign selection**. Done — the geometry now "knows" what it is.

!!! tip "Tag while drawing"
    Activate a class with the **"Tag while drawing"** lock and everything you draw from then on takes that class automatically. Push/pull also **propagates** the tag: thickening a tagged wall does not lose it.

## Live takeoff

The same panel shows the **quantities instantly**, by class:

- Walls: **net m²** of face (openings deducted).
- Slabs: m² and m³.
- Columns and beams: m³ and linear meters.
- Doors and windows: **count** with their dimensions.

The numbers come from the real solid — and since the engine guarantees watertight solids, the takeoff is reliable by construction.

## Exporting

- **IFC 4**: File ▸ Export ▸ IFC. The file passes standard validation (`ifcopenshell.validate`) and any BIM viewer or software opens it. It includes the quantities (`Qto_*BaseQuantities`).
- **Quantities CSV**: your takeoff table ready for the spreadsheet.

## The bridge to IngePresupuestos

The flagship workflow of the ecosystem:

1. Tag your model in IngeTrazo.
2. Export the **IFC**.
3. In [IngePresupuestos](https://ingepresupuestos.com), import that IFC: the line items arrive with their **exact quantities**, ready for unit cost analysis, scheduling and site control.

Verified end to end: the quantities you see in the BIM panel are the ones that land in the cost estimate.
