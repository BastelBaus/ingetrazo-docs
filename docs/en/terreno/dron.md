---
source_blob: 1a9adb1631b6c539ef178e8b70848070849fecf1
---

# Drone survey (WebODM)

If you fly your site with a drone and process it in **WebODM/ODM**, IngeTrazo imports the textured photogrammetric mesh as a working base — your real terrain, with its real textures, in its real UTM position.

![A real survey: route drawn on the drone mesh, longitudinal profile open and UTM readout in the status bar.](../images/terreno.jpeg)


## Importing

1. File ▸ Import ▸ **Photogrammetric survey (ODM)…**
2. Choose the textured model from the ODM export (`odm_texturing/odm_textured_model_geo.obj`).
3. IngeTrazo reads the georeferencing from the export itself and places the survey **where it belongs**, with real altitudes.

What it does for you:

- **Real position and elevations**: the export's UTM anchor is respected; the vertical reference is taken from the **base of the survey**, so every elevation you read is the site's real altitude.
- **Textures adapted to your GPU**: ODM's giant atlases (up to 24,576 px) are rescaled automatically to what your card supports, with a cache so the second load is instant.
- **Saved inside the `.igz`**: you move the document to another PC and the survey travels with it — it no longer depends on the export folder.
- **Its own layer**: the import creates the *Levantamiento* (survey) layer; you can turn it off without touching your model.

## Working on the flight

- It is **reference** geometry (display-only): it can be seen, measured and queried, but it does not mix with your solids.
- The **Route** tool queries the survey's elevation live (~20 µs per query): the longitudinal profile comes from **your flight**, not from the 30 m satellite data.
- In top view + parallel projection, drawing on the relief has no parallax: the Route tool switches to that view by itself.

!!! note "On vertical accuracy"
    Without ground control points (GCP), the drone's altitude is GNSS (ellipsoidal) and can differ by a few meters from mean sea level. The profile CSV declares this in its header. For projects with strict tolerances, fly with GCPs.

!!! tip "Performance"
    A real survey of ~360,000 triangles and 21 atlases loads in ~2 s and orbits smoothly. If yours is much larger, consider the decimated version that ODM also exports.
