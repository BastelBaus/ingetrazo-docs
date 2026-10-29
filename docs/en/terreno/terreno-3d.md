---
source_blob: d8fbeda9873881931022e50522370b168394e66c
---

# 3D terrain

With the location set, turn on **3D terrain** in the Terrain panel: IngeTrazo downloads the elevation model of your area (DEM) and **drapes the satellite image over the real relief**.

- The relief covers the capture area defined in the locator.
- The **origin altitude** is referenced to the project datum, so the elevations you read are real elevations.
- It is **visual reference** geometry: you can orbit it, measure on it and draw on top, but it does not enter the solid engine or the takeoff.

## Drawing on the terrain

- The **Route** tool ([see Routes and profile](rutas-perfil.md)) reads the terrain elevation under the cursor and gives you the longitudinal profile of the alignment.
- The flat base map and the 3D terrain are interchangeable: the same site, with or without relief.

!!! note "The step between elevation sources"
    The global DEM uses orthometric altitudes (above sea level); a drone survey without control points uses GNSS (ellipsoidal) altitudes. If you see a small vertical step between the 3D terrain and your survey, it is the real difference between vertical datums — not a fitting error.

## Reference surface

When there are several sources (DEM, drone survey), elevation queries use the **most accurate one available** at each point: your flight takes precedence over the 30 m satellite DEM.
