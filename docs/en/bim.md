---
source_blob: 8ff4d5465b33b8c5a924cd0535e8dae931fac3cd
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

## Search, filter and group

With many objects, the bar above the table helps you find what you are after:

- **Search**: type part of the name, the class or the outline path (`*` and `?` work, as in the Browser).
- **Funnel**: untick the IFC classes you don't want to see — for example, keep only the IfcSpace objects. The funnel fills while it hides something.
- **Group**: *by group* (each object inside the groups that hold it), *by IFC class* or *by name* (each heading with its object count and the takeoff and volume totals of the visible rows) or *no grouping*.
- **Columns**: the **Outline path** column says which groups each object sits in, for example "Floor 1/Core". The button at the header's right end (or a right-click on the header) shows or hides Takeoff, Vol m³ and Outline path, as in the Browser.

The grouping, the hidden classes and the columns are remembered between sessions.

## Exporting

- **IFC 4**: File ▸ Export ▸ IFC. The file passes standard validation (`ifcopenshell.validate`) and any BIM viewer or software opens it. It includes the quantities (`Qto_*BaseQuantities`).
- **Quantities CSV**: your takeoff table ready for the spreadsheet. **Export all CSV** writes every object; **Export shown CSV** only those the search and the funnel leave.

## The bridge to IngePresupuestos

The flagship workflow of the ecosystem:

1. Tag your model in IngeTrazo.
2. Export the **IFC**.
3. In [IngePresupuestos](https://ingepresupuestos.com), import that IFC: the line items arrive with their **exact quantities**, ready for unit cost analysis, scheduling and site control.

Verified end to end: the quantities you see in the BIM panel are the ones that land in the cost estimate.
