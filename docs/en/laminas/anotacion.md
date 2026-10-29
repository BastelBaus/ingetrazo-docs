---
source_blob: d089408ea3ccdfa1372b4711d0a914bf2cb37382
---

# Dimensions, texts, shapes and title block

## Dimensions on the sheet

The composer's **Dimension** tool dimensions the frame's drawing:

1. **Click the first point** — over a vertex or edge of the drawing the **green point** appears: the snap catches the real visible geometry of the frame.
2. **Click the second point** (also green).
3. **Move and click a third time** to pull the dimension line away from the drawing — with its extension lines, as technical drawing requires.

The tool **stays active** for the next dimension; `Esc` (with nothing half-done) or the cursor leaves it.

### Forced straight dimension (`Shift`)

Two points that are **not aligned** give, by default, an inclined dimension: it measures the distance between them, which is what an aligned dimension asks for. But often what you want is **the height** or **the width** between those two points, and then the dimension has to come out straight.

**`Shift`** at any moment of the gesture forces it straight: it picks the axis along which the two points are farthest apart, **does not move the points** —each stays where it snapped— and the dimension measures only that part, with **extension lines of different lengths** reaching each point. It is AutoCAD's linear dimension.

You don't need to hit the right moment: the choice **sticks** until you place the dimension, and afterwards the panel's **Direction** drop-down (*Aligned with the two points* / *Forced horizontal* / *Forced vertical*) changes it on any dimension already drawn, with undo.

### Dimensions anchored to the model

If both points snapped green, the dimension is **anchored to the model's 3D points**:

- The label shows the **exact real 3D distance** (not a multiplied paper measurement).
- If you **edit the model** (the wall stretches from 6.00 to 6.20 m), the dimension moves and **measures itself again**.
- If you move the frame, change its scale, its view or its rotation, the dimension follows it.
- When selected, its handles are **green** (anchored) or blue (free paper dimension). Dragging an end by hand releases it from the anchor (with undo).

### Dimension style

In its properties: **separation**, **text height**, **decimals**, **units** (m, cm, mm, inches, feet, feet-inches and their fractional variants), terminators (**arrows**, as the standard requires; oblique ticks or none if you prefer), line weight, color, text background and manual text if you want to replace the measurement. The grip in the middle of the line lets you readjust the separation whenever you like.

**Where the text goes**: always **above** the dimension line and **aligned with it** —a vertical dimension reads from bottom to top, on the left—, as the ISO standard requires (*Text position* offers nothing else for now; *Orientation* keeps "Horizontal" marked as non-standard, in case a dimension has it and you want to put it back). The **separation** is the distance from the line to the baseline of the figures: 0.5 mm on a new dimension, a quarter of the text height, which is what you see on a standard-compliant sheet. *Along the line* puts it **over the middle**, **outside the start** or **outside the end** (the text beside the dimension, to the left or right). And **the text can be dragged with the mouse** by grabbing its letters and stays where you leave it, while the line does not move; **Put the text back** undoes the drag. **The style of the last dimension you edited is the style of new ones**, and it is remembered between sessions — the look (terminators, height, color, background…), not where you put the text: every new dimension is born with the number **over the middle** of its line.

### Chain dimensions

The **Chain dimensions** tool (next to the dimension) dimensions several consecutive segments on **a single dimension line**:

1. Click the first point and the second.
2. A third click sets the line's separation.
3. Each following click adds the next segment on the same line (with a jog, the new segment adjusts to pass through the chain's line).
4. Clicking on the last point, `Esc` or switching tools ends the chain and stacks the **overall dimension** one row further out (with two segments or more; `Ctrl+Z` removes it if you don't need it).

`Shift` **forces the entire chain straight**: all segments measure only their horizontal (or vertical) part and share a single dimension line, even if the points are at different heights. The overall dimension is forced the same way.

### Baseline dimensions { #cotas-desde-linea-base }

The **Baseline dimensions** tool is the chain's sibling: it is used the same way —two points, the separation, then one click per point— but **every dimension measures from the FIRST point**, and each one is stacked **one row further out**. It is classic cumulative dimensioning: distances from a corner or from a grid line.

The difference in one sentence: the **chain** puts the segments one after another on a single line; the **baseline** puts the cumulative distances, staggered. Both accept `Shift` to come out straight, and both end with a click on the last point or `Esc`. The chain also stacks its **overall dimension**; the baseline does not need one, because its last dimension already runs from the base to the farthest point.

#### Continuing from an existing dimension

As in AutoCAD, **you don't need to give two points and the separation again**: **select a dimension** and arm Chain or Baseline, and the series **continues from that one** — the chain from its second point, the baseline from its first —, keeping its line, its separation and whether it was forced straight. From there on it is **one click per point**.

With nothing selected, the series starts from scratch as always: two points, the separation and on you go. *(In AutoCAD, `DIMCONTINUE` and `DIMBASELINE` **only** continue from an existing dimension and never ask for two points; both ways are kept here on purpose.)*

The **spacing** between rows of a baseline series —AutoCAD's `DIMDLI`— is a value you set in **Dimension style ▸ Baseline spacing** (8 mm by default). It lives in the document, so a drawing keeps the spacing it was drawn with.

### The line extends under the text

When the text goes **outside the start or the end** (*Along the line* in the panel), the dimension line **extends to cover it**, as the standard requires: if you change the text to a longer one, the line grows with it. If you drag the text by hand, the line stays where it is — there, you are in charge.

Points snapped green anchor each segment to the model, like a normal dimension.

### Angular dimension

The **Angular dimension** tool: click the **vertex**, click a point on each side and a fourth click for the **arc radius**. It measures the real angle, with its arc, its arrows and the text aligned or upright. The first three clicks **snap to the frame's geometry** (green point), and with **`Shift`** the arm falls on an exact multiple of 15°: the first from the sheet's horizontal and the second **from the first arm**, so the measured angle comes out round — 90°, 45°, 30°.

### Radius and diameter dimensions

The **Radius dimension** tool: click **on the circle or arc** of the drawing and the dimension takes the **center and the radius by itself** — as in AutoCAD, there is no need to look for a center the drawing doesn't mark; the point where you click decides which side the line comes out on, and as you move the cursor over the arc you already see a dotted preview of the dimension it will place. It recognizes circles and arcs that the frame sees **face-on** (in plan, the horizontal ones; in an elevation, the vertical ones) — one seen edge-on is a line and has no radius to dimension. If you click where there is no arc, that click is the **center** and the next one a point on the **arc**. With **`Ctrl`** on the click it comes out as a **diameter** instead of a radius; the panel's *Type* drop-down also changes it afterwards.

It follows the dimensioning standard:

- The line **always reaches the center**: the radius starts from it and the diameter passes through it. A leader that stops halfway does not comply.
- The **symbol accompanies the value**: `R` or `Ø`.
- The text goes **above** the line and is never upside down, whatever quadrant the radius is in.
- If the letters and arrows **fit**, they go inside and the arrows point outward, at the arc. If they **don't fit**, the line extends outside, the text goes on that extension and the arrows point **toward the center**. *Text position* lets you force it (Automatic / Inside / Outside).
- On a diameter the number is not placed over the center, which is where the center lines go: it shifts to the **right** half of the line, whichever way it was drawn (on a vertical diameter, to the upper half, which is the reading direction).

An **arc** is dimensioned just like a circle. The **center mark** (the little cross) can be removed in the panel, and the grip at the end of the arc rotates and resizes the dimension.

## Level marks

The **Level** tool places the level mark with one click on a point of a view: it reads the **height of the point** and writes "N.P.T. +0.15" next to the symbol — a triangle on its vertex in sections and elevations, a quartered circle in plans (the plan frame picks it by itself). Anchored to the model, it follows the point if the geometry changes and updates the height; it can be slid across the sheet and a thin leader remains back to the point.

In an **elevation or a section** you don't even need to snap: the rows of the sheet ARE the model's heights, so a click anywhere in the frame already knows what height it is at and writes that. A **plan** looks down and cannot tell: there the level comes from the snapped point, or you type it.

In its properties: **text** with `{z}` (or without it: the level is appended at the end), **datum** (the model height that reads as ±0.00), decimals, symbol, size, length of the level line, side, line weight and color.

## Leader labels

The **Label** tool: click the point you are pointing at (it snaps green on the drawing) and click where the text goes. The leader follows the point if you move the text; anchored to a frame, it moves with it. Font, size, **bold, italic, underline**, color, background, arrowhead and line to the left or right in the panel.

## Detail callouts

The **Callout** tool frames (dashed rectangle or circle) the part of a view that another drawing enlarges and places the **"3 / L-05"** bubble with a leader. The bubble is dragged separately; the frame moves and resizes like any item. Drawn over a frame, it is linked to it and moves with it. Number, sheet (accepts `{lamina}`), shape, size, line weight and color in the panel.

## Shapes

Line, **arrow**, **ground line**, rectangle (with **corner radius**), ellipse and **regular polygon** (3–24 sides). Each shape with its **line color**, weight, and — for closed ones — **fill with its own color**. For line, arrow and ground line, `Shift` locks them horizontal or vertical.

The **ground line** is the ground of an elevation: the line and, below it, what drawing convention requires — **earth ticks** at 45°, a **hatched band** or a translucent **filled band** (the fill color), with length, spacing and height adjustable in the panel. It accepts a slope and the ground always stays on the lower side; for level changes, one segment per level. Combined with a **Level** mark ("N.T.N. ±0.00"), it says it all.

## Text and images

- **Text**: blocks with font, size in points, **bold, italic and underline**, color, background and alignment. **Double-click** edits it **in place**, with the same font at the same size; clicking outside or `Ctrl+Enter` confirms, `Esc` cancels. A text can be **linked to a frame** ("moves with its frame") and use fields: `{escala}` reads that frame's scale, `{lamina}` and `{proyecto}` the title block, `{fecha}` the date. **Add a scale label** in the frame's panel places such a text, already written.
- **Image**: logos, site photos, auxiliary views (PNG/JPG). With **opacity**, **clip shape** (rectangle, rounded corners, ellipse or circle), **feathered edge** in millimeters, **fit** (stretch, cover by cropping or contain whole) and optional outline — a circular photo blended into the paper, as on presentation sheets.
- **Terrain profile**: the **Profile** tool draws the longitudinal profile of an [alignment](../terreno/rutas-perfil.md) on the sheet, with horizontal and vertical scale, vertical exaggeration, chainages and elevations; sampled from the drone survey or the DEM, and it updates if the alignment changes.

## Title block

The drawing's title block — **the** item of a sheet:

- **Editable fields**: the property table lets you rename, **add and remove rows** (PROYECTO, AUTOR, FECHA, ESCALA, LÁMINA, and whatever your project set requires: DISTRITO, REGIÓN…). Values accept fields: `{fecha}`, `{lamina}`, `{total}`…
- **1 to 4 columns** of fields, side by side, like real wide title blocks.
- **Design**: seven look presets —square, rounded or chamfered corners; grid, header band or minimalist; double border, label fill, colors— that change **how it looks**, never the rows or the size. Each detail can be edited separately: weights of the outer border and the inner lines, width of the label column, colors of label, text and line.
- **Title block templates** (**Templates…** button): save yours —rows, size and look— with a name, apply it to another sheet and mark it as **default**: every new title block is born from it. **Copy style / Paste style** also works between title blocks, and `Ctrl+C` / `Ctrl+V` takes the whole title block to another sheet (it takes the place of any existing one).
- **Rows share the height according to their content**: a long project name drops to two or three lines and its row grows —up to three times its share— at the expense of rows that weren't using theirs, so all values come out the same size; only if it still doesn't fit is the font condensed.

## Scale bar, north arrow and legend

- **Scale bar**: the black/white segmented bar with meters — the reader can measure even on a photocopy. It follows the scale you give it.
- **North arrow**: rotatable to your project's north.
- **Layer legend**: lists the model's visible layers, with manual refresh.
