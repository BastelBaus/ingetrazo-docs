---
source_blob: b0704d990494f5a66b3f3480d18ca7a8489a1079
---

# Styles, shadows and display

How the model looks is your decision, per document and per scene: **styles** decide faces, edges, sky and background; **shadows** put your site's sun at the time you choose; and the clean screen leaves just the model.

## Styles

**Camera ▸ Style** changes the document's active style. The built-in ones:

| Style | What it shows |
|---|---|
| **Default** | Faces with materials and textures, edges, gradient sky. |
| **Architectural** | White background, no sky, edges and profiles: the look of a sheet. It is the style every new view frame in the composer is born with. |
| **Shaded** | Colored faces, no textures. |
| **Hidden line** | Lines only, white faces: the technical drawing. |
| **Monochrome** | Faces in a single tone. |
| **Wireframe** | Edges only. |
| **X-ray** | Everything translucent, edges always visible: to look inside (the rebar, the pipes) without cutting. |

**Camera ▸ Edges** and **Camera ▸ Profiles** turn the edges and the thick silhouettes of the active style on or off.

### The style editor

The **Styles** drop-down on the toolbar opens the editor, which edits the active style **live**:

- Face mode (shaded, hidden line, monochrome, wireframe, X-ray), edges, profiles, sky and **section fill**.
- The four colors: front and back of faces, **sky** and **ground** — with a gradient toward the horizon. A color that is not visible in the current mode can still be edited; the status bar says where it will show.
- **Save style…** adds it to **your library** with a name (a built-in name is rejected: the presets are fixed). **Delete** removes it.
- Saved styles appear in Camera ▸ Style and in the style combo of every **composer frame** — each frame can have its own.
- Each **scene** remembers its style, and the `.igz` stores the complete style: a document does not depend on your library.

## Shadows with the real sun

The **Shadows** drop-down on the toolbar (and **Camera ▸ Shadows**) turns on shadows computed from the **real position of the sun**:

- **Date**: day and month, with a slider across the year. **Time**, limited to daylight — from sunrise to sunset for the site and date, so the sun is never below the horizon.
- Shadow **darkness** and **time zone** (derived from the longitude; you can set it).
- **Site**: the project datum if it is [georeferenced](../terreno/ubicacion.md); otherwise, Arequipa. **Add location…** opens the locator and sets the datum.
- **Glass with less than 70 % opacity casts no shadow**; cut-out textures (meshes, leaves) cast their pattern; "face the camera" figures cast their silhouette oriented to the sun.
- The sun also **shades the faces** (those facing away from it look darker) and the ground receives the shadow as a glaze.
- Shadow settings are saved in the document and **composer frames render with them**: a sun-study sheet comes out directly.

!!! note "Accuracy"
    The astronomical calculation is verified (at the equinox the sun rises in the east; in June, in Arequipa, it passes to the north at ~50°). What you see is the sunlight on your site at that date and time.

## Clean screen and layout

- **Window ▸ Clean screen** (`Ctrl+0`) hides toolbars and panels and leaves just the viewport; `Ctrl+0` again brings them back.
- **The layout is remembered**: where you left the toolbars, which tray panels you opened and their size come back in the next session.
- The **Styles**, **Shadows** and **Dimension style** panels are toolbar drop-downs; they do not take up the right tray.
- **Camera ▸ Rest of model while editing**: when you enter a group, everything else is shown normally, **dimmed** (the default) or **hidden** (the fastest mode in heavy models). Also in Preferences.

## Exporting an image

**File ▸ Export ▸ Image (PNG / JPG)…** saves a high-resolution capture of the viewport with the current style and shadows — without selection indicators or tool markers.
