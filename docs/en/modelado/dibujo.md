---
source_blob: f47255b182150c0860aa6ec27322d4570d4f1e50
---

# Drawing tools

They all speak the same language: click to start, the **inferences** snap you to existing geometry, and the **VCB** accepts the exact measurement from the keyboard (type and press Enter, without clicking any field).

## Lines and polygons

| Tool | Shortcut | How to use it |
|---|---|---|
| **Line** | `L` | Click by click; type the length for an exact segment. Close an outline and the face is created automatically. |
| **Rectangle** | `R` | Two corners; type `width,height` (e.g. `6,4`). **`Ctrl`** toggles **from the center** (center and one corner): the pencil badge changes, and the typed `width,height` is the **full** size. When you pick the tool up again it starts from the corner. |
| **Rotated Rectangle** | `K` | First the base (two points), then the height. |
| **Circle** | `C` | Center and radius; type the radius. |
| **Polygon** | — | Center and radius; type the number of sides (`G` is Make Component). |
| **Freehand** | — | Drag and release: a smoothed polyline that is selected whole with one click, like a circle; if it closes, it creates the face. |

## Arcs

| Tool | Shortcut | How to use it |
|---|---|---|
| **Arc** | `A` | The two endpoints (the chord) and then the bulge. This is the 2-point arc. Type the bulge, or `2r` for the radius. **Rounding a corner**: start on an edge, and on the neighboring edge, at the same distance from the corner, the arc turns **magenta** (tangent to both); a double-click there draws it and trims the corner, and while the arc is magenta **a typed number is the fillet radius**, keeping the tangencies. |
| **3-Point Arc** | `J` | Endpoint, a point it passes through and the other endpoint. |
| **Center Arc** | `Shift+O` | Center, starting radius and sweep. |
| **Pie** | — | Like Center Arc, but closes the sector with the two radii and its face. |

## Derived tools

| Tool | Shortcut | How to use it |
|---|---|---|
| **Offset** | `F` | Copies the outline of a face inward or outward at an exact distance. The classic for wall thicknesses. It also works on **edges**: click a loose edge and it offsets its whole connected chain (open or closed), or preselect the edges you want and click one of them. |
| **Follow Me** | `W` | Extrudes a profile along a path: moldings, pipes, curbs. |
| **3D Text** | — | Draw ▸ 3D Text: letters with real volume (font, bold, italic, height and thickness), ready to extrude or paint. |

### Follow Me, three ways

Draw the profile **perpendicular to the path** (easiest: on a face, then erase the leftover edges).

1. **Drag along the path** — activate Follow Me (`W`), click the profile and move the cursor along the path touching its edges: the path is highlighted in **red** and the extrusion is previewed live, with its miters. Click (or release the button, if you dragged) when you reach the end; `Esc` starts over. If you skip segments of an arc, the connected edges in between are followed; if you go back, the path gets shorter.
2. **Preselected path** — select the path's edges (one click on a circle segment takes the whole outline), activate Follow Me and click the profile: it extrudes in one go.
3. **Perimeter of a face** — select the face whose border is the path and click the profile; or, while dragging, hold `Alt` over a face to use its perimeter. This is the shortcut for moldings around a slab and for **lathing**: a circle as the path and half a profile as the section.

## Keyboard measurements: meters, centimeters, inches, feet { #medidas-por-teclado-metros-centimetros-pulgadas-pies }

Numbers without a suffix are in the **document unit** (meters unless you change it in [Preferences ▸ Units](../preferencias.md#unidades): in a millimeter document, `500` is half a meter). Each field can carry its own unit, so you can draw the timber or the piping in inches and the spans in meters within the same model:

| You type | It means |
|---|---|
| `3,2` | 3.20 m |
| `30cm` · `1500mm` | 0.30 m · 1.50 m |
| `2"` · `2in` | 2 inches |
| `1'` · `1ft` | 1 foot |
| `1'6"` | 1 foot 6 inches |
| `3/4"` · `1'3/4"` | inch fractions |
| `1 1/2"` · `1-1/2"` · `1'6 1/2"` | one and a half inches, one foot six and a half (mixed number) |
| `2";4"` | 2 × 4 inch rectangle |
| `3,2;1'6";10cm` | X, Y, Z displacement with mixed units |

Quote marks and the fraction slash are only accepted after a number, so `I` and `F` remain tool shortcuts.

**Dimensioning in inches or feet.** In the tray's dimension style (and in each sheet dimension, in its panel) choose the units: `m`, `cm`, `mm`, `in`, `ft`, `ft-in`, or the fractional `in-frac` (`1 1/2"`) and `ft-in-frac` (`1'6 1/2"`). With the fractional ones, **Decimals** sets the finest denominator: 0 = whole inches, 1 = 1/4, 2 = 1/16, 3 = 1/32, 4 = 1/64.

## The working plane

The tools draw on the **plane you are looking at**: in top view you draw in plan; if you start on an existing face, you draw on that face. The first point without an inference lands on the plane of the current view — so the stroke never "escapes" to an unexpected depth.

**Locking the plane with the arrow keys** (circle, polygon, rectangle and arcs): before the first click, `→` locks the plane normal to X (YZ), `←` the one normal to Y (XZ) and `↑` the one normal to Z (XY); the same arrow again, or `Esc`, releases it, and a label in the axis color shows it. With the plane locked, the center can land on a face and the shape still comes out on the chosen plane. The shape uses up the lock; after the first click, the arrows go back to being the usual axis lock.

**Perpendicular to an edge with `↓`** (the magenta lock): before the first click, with the cursor over an edge, `↓` locks the drawing plane perpendicular to that edge; over a face, parallel to it. The cursor ring turns magenta and `↓` again releases it. This is how you draw a pipe on an inclined axis: draw the axis line, press `↓` over it, put the circle's center on its end, give the radius and apply Follow Me; the circle already comes out perpendicular to the axis, with no rotating afterwards.

!!! tip "Drawing in standard views"
    For precise 2D-style work, combine **standard view + parallel projection** (`P`): front for elevations, top for plans. The measurements you see on screen are the real ones on that plane, without perspective distortion.

## Inferences

The colored points while you draw:

- **Green** — edge endpoint.
- **Cyan** — midpoint.
- **Red/green/blue** — on an axis of the system (X east, Y north, Z vertical). The **axis magnet** (a stroke within a few degrees of an axis snaps onto it) is available in every tool that draws: Line, Arc, Circle, Polygon, Rotated Rectangle, Tape Measure, Protractor, Dimension, Text and Move.
- **Magenta** — parallel or perpendicular to an existing edge.

Hold the mouse over a point for a moment to "memorize" it and project from it: when you line up with it along an axis, a dotted line appears from the point (**From point**).

And on **another wall** —perpendicular or the opposite one—, when you pass at the height of a memorized point the cursor snaps to a dotted line running along that wall at that height (**Level with point**): that is how you place all the windows of a house at the same height without guide lines. On the ground, below a high point, the same happens in plan (**In line with point**).
