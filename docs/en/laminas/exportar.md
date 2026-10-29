---
source_blob: 2534795441a6e2a7cb014f61f565006531b827bd
---

# Export PDF, image and DXF

Everything is on the **sheet bar**, below the title of the composer window: preview, PDF and image; DXF is in the frame's menu.

## Print preview

**Print preview…** shows the sheet exactly as it will come out: real size, line weights, no handles or snapping. It is the place to check before exporting.

## PDF of a sheet

**Export PDF…** writes the current sheet with exact physical metrics: A3 comes out A3, and a 1:100 scale **measures** 1:100 on the printed paper. The PDF is **vector** — the lines of the Vector style are real curves with their three pens and their poché, not pixels: it prints sharp at any size. Nothing from the screen sneaks in: not the model selection, not the handles, not the snapping.

## PNG or JPG of a sheet

**Export image…** writes the current sheet as **PNG or JPG**: you choose the file and then the resolution in dots per inch (200 by default; the last one is remembered). The image comes out at the exact paper size —a landscape A3 at 200 dpi is 3307 × 2339 pixels—, with a white background and the same painter as the PDF, ready for a report, an email or a presentation.

## The atlas: every sheet in one PDF

**Export all sheets (PDF)…** generates a single file with each sheet of the document on its own page (each with its own paper size) — the complete drawing set of the project in one click.

## DXF to IngeCAD / AutoCAD { #dxf-hacia-ingecad-autocad }

With a frame selected, **Export view as DXF…** writes the vector drawing of that view (the exact visible lines, in model meters, with the view rotation applied) as DXF R12 — [IngeCAD](https://ingecad.org), AutoCAD, LibreCAD or QGIS open it. Line classes go on separate layers —`VISTA`, `VISTA-PERFIL`, `VISTA-CORTE`— for your pen table. It is the bridge for anyone who finishes 2D details in their usual CAD.

!!! tip "Before exporting"
    - **Update the frames** if you edited the model with the composer open (or leave auto-render on).
    - Check at **100 % zoom** (real paper size) or in the preview: line weights and text sizes look exactly as they will print.
    - The four [examples](../primeros-pasos/ejemplos.md) come with the PDF of their sheet alongside, in case you want to compare.
