---
source_blob: 1ef056e44e4260ab50a82ab2da7fe6a26a279b2e
---

# Project location and base map

All terrain work starts by setting **where** your project is. That anchors the coordinate system and enables the satellite map, the 3D terrain and the field data.

## Setting the location

In the tray, **Terrain / Base map** panel:

1. **Search location…** opens the locator: search for the place by name, use "Locate me", or browse the map.
2. Adjust the map until the **center pin is exactly on your site** — zoom in without fear.
3. Accept and then **Go to location**.

!!! warning "The pin IS your model's origin"
    The point you choose becomes the model's **origin (0,0,0)**. Draw around the origin and your model lands exactly there on the satellite image — no need to move it afterwards. The map itself says so: the pin is labeled *origin (0,0)*.

    If the project already had a location and you choose another, IngeTrazo **asks before moving the origin** (everything drawn keeps its local coordinates and is relocated on the map).

## Coordinates: UTM or geographic

With the **Coordinates** selector you choose how to view and type the position — and the program remembers your choice:

- **UTM WGS84**: Zone, hemisphere, **Easting** and **Northing** — exactly as your drone or total station reports them, with the standard conventions (false easting 500 km; false northing 10,000 km in the southern hemisphere).
- **Geographic**: latitude and longitude in decimal degrees.

Both frames are always synchronized under the hood; switching mode loses nothing. With the project georeferenced, the **status bar shows the live UTM readout** of the cursor.

## North: rotate the map, not the model

A building or a square is drawn **square to the axes** (red and green): that way the Front, Right and Left views, the axis locks and the rectangle work without thinking. But the site rarely faces north. If you rotate the model to fit it on the satellite image, you lose all of that.

The model stays on its axes and **the map rotates underneath**. The panel's **North** field says where true north lies, in degrees clockwise from the green axis (0° = the green axis points north). When you change it, the base map, the 3D terrain, the imported routes and points and the shadows rotate; the model does not move.

**Already rotated and dragged the model onto the map?** Select it (it has to be a single top-level component — group it if needed) and press **Straighten model on the map**: the model goes back to its own axes, the origin moves to the model's corner and the north angle is calculated, so that **nothing moves on the map**. Saved scenes, dimensions and sheets anchored to the model travel with it. It is a single undo step.

!!! note "Height"
    When straightening, the model recovers the heights it was drawn with and the map stays at z = 0 (it is the reference plane). If the model was floating above the map, it comes down into place.

## The base map

- **Sources**: Esri satellite, OpenStreetMap and any you add — any **XYZ** tile server (your own orthophoto served from QGIS, for example) is saved with a name and stays in the menu for good.
- **Capture area**: in the locator you can draw a rectangle — a square for a site, a long strip for a road.
- **Zoom** controls the detail of the tiles; huge captures reduce the detail automatically to keep the program fluid.
- The map is **visual reference only**: it never enters your geometry or your takeoffs, and the capture is saved with the document (the tiles are downloaded again on opening).
