---
source_blob: a132cb1409f984609aa52c40772e571fef3f775d
---

# Dimensions and 3D annotation

These are the annotations **inside the 3D model**. For dimensions on the printed sheet, see [Sheet layout](../laminas/anotacion.md).

## Dimensions

**`D`** activates Dimension:

1. Click the first point (inferences snap to endpoints and midpoints).
2. Click the second point.
3. Move to pull the dimension line away from the model and click to set it. If you pull the dimension **past an endpoint**, in the direction of an axis, it becomes **linear** (it measures the projection on that axis); if you pull it out square, it stays **aligned** (it measures the true distance). The status bar says which one it is.

The dimension stays **anchored to the geometry**: each end that lands on a vertex holds on to it, so if you later **scale, move or stretch** the drawing, the dimension goes with it and **measures again** — it does not stay floating with the old value. An end inside a component follows the instance. If the vertex disappears (you erase it), the end stays where it was. An end placed on a midpoint or on an edge has no vertex to hold on to and stays fixed.

With **Move** (`M`) on a dimension, the **dimension line shifts** and the extension lines stretch from their vertices; if you select it together with the geometry, it travels with it.

The **Dimension style** drop-down on the toolbar controls color, text height, decimals, **units** (meters, centimeters, inches, feet, and the fractional `1 1/2"` — see [keyboard measurements](dibujo.md#medidas-por-teclado-metros-centimetros-pulgadas-pies)) and the **terminators**: arrows (what a new document comes with), oblique ticks or none — an older document keeps its ticks. Dimensions can be selected, deleted with `Del`, and appear in the [sheet frames](../laminas/marcos.md#extras-del-marco) if you turn on "Model annotations", with the same terminators.

### Dimensioning standard

Dimensions follow the **ISO / UNE** standard: the text goes **above** the dimension line, centered along it, and **the line is never broken**. The text is oriented to be read by turning your head to the **left**: a vertical dimension reads from bottom to top, whether you draw it upward or downward. It is the only standard available for now (the German/Japanese one, with the broken line and the text in the middle, is left for a future version).

The same panel holds the **Baseline spacing**: the distance between rows of a series of [baseline dimensions](../laminas/anotacion.md#cotas-desde-linea-base), AutoCAD's `DIMDLI`.

## Leader text

The **Text** tool (`X`) places labels with a leader line pointing at a face or edge — room names, site notes. The text always faces the camera; it moves with its anchor pinned, and is edited with a double-click. Dimensions and leader texts can live on a **layer**: turn off "Dimensions" and they disappear from the view and from the sheets that don't want them.

## 3D Text

Draw ▸ **3D Text** generates letters with real geometry (extrudable, paintable) — for signs and monuments, like the letters of a town square.

## Tape measure and protractor

- **Tape Measure** (`T`): measures and leaves dotted construction **guides**. From an edge or from an **axis** of the system (click the axis — it works with an empty document too: that is how you place a project "20 m and 5 m from the origin" before drawing anything), a parallel guide at the dragged or typed distance; from a **named point** (endpoint, center, intersection, origin), a **guide point with its dashed segment** back to the starting point, the "guide segment" for centering a circle or marking the overhang of an eave; from point to point it only measures (a midpoint does not count as a point). It has the same axis magnet as the Line: a measurement within a few degrees of an axis snaps onto it, in its color.
- **Protractor** (`Shift+H`): angular guides; its arms also snap to the axes lying in the plane of the disc.
- Guides are not geometry: they do not appear in exports or takeoffs, and are cleared with Edit ▸ Delete Guides.
