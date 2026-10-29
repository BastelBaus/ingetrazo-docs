---
source_blob: e960eb4d365a04f1a7a09938f94a1f7eef66c628
---

# Sheet layout

The **sheet composer** turns your model into printed drawings without leaving IngeTrazo — in the style of the QGIS print composer: you place **views of the model at exact scale** on a sheet, dimension them, add a title block, and export vector PDF.

It opens from the **status bar tabs** (Model | Sheet 1 | … | `+`) — one click on a sheet opens it; `+` creates a new one; **Model** goes back to the modeler — or from **File ▸ Sheet composer…**.

![The sheet composer with sheet D04 of the Yanque arch: rulers, sheet bar, canvas and layout panel.](../images/laminas.jpeg)


## The window

- **Sheet bar** (below the title, with icons): **Save** the document (`Ctrl+S`, from here as well), **Update views**, **Export PDF…**, **Export image…** (PNG or JPG) and **Print preview…**.
- **Central canvas**: the sheet, with shadow and margins, between a **ruler** in millimeters at the top and another on the left (they follow the zoom and mark the cursor position; [guides](#reglas-y-guias) are pulled from them). Zoom with `Ctrl+wheel`, with the combo in the status bar (*Fit page*, *Fit width*, percentages — 100 % is the **real paper size** on your screen) or with the two model tools on the left toolbar: **Zoom** (drag up to zoom in and down to zoom out, around the point where you pressed; one click zooms in one step) and **Zoom window** (drag a box and the view fills with it). **Pan** with the wheel, the middle button or the Hand tool, at any zoom: you never lose the sheet (a strip always stays in view).
- **Left toolbar**: select, hand, format painter, view frame, text, leader label, level, detail callout, image, title block, scale bar, north arrow, legend, terrain profile, line, arrow, **ground line**, rectangle, ellipse, polygon, dimension, chain dimensions and angular dimension. Each tool places one item and returns to Select; **dimension tools stay active** so you can chain one after another (`Esc` or the cursor leaves them).
- **Right panel** (resizable, fits in ~480 px): sheet manager, **Items** list and properties of the selected item. Sections you don't use fold away.
- **Status bar**: the same Model | Sheets tabs, the **Auto-render** checkbox, the coordinates in mm and the zoom.

## Sheets

- Sizes **A4 to A0**, landscape or portrait, with configurable margin and optional **sheet border** (single or double, thickness and color; it is printed).
- **Several sheets per document**: `+` creates, `⧉` duplicates (inherits title block and margins — ideal for keeping the style of the project set), `−` deletes, and *Renumber sheets* updates the L-01, L-02… in the title blocks. The same with a **right-click on a sheet tab** in the status bar, in either window: *Rename*, *Duplicate* (the copy goes right after), *Delete* and *New sheet*.
- **Sheet templates** (**Templates…** button): save a sheet —paper, margins, border, title block, empty frames— as a named template; create new sheets from it and set one as the **default** for every new document. Templates are files in your user folder (*Open the templates folder*): share them by copying.
- Everything is saved **inside the `.igz`**, with its own undo: `Ctrl+S` or the Save button on the sheet bar writes the whole document, model and sheets, and the **auto-save** from Preferences also covers the sheets. You lay out once; each revision of the model is just reopening and re-exporting — or leaving **auto-render** on and watching it update.

## Items

Everything on the sheet is an item: it moves by dragging (with snapping to margins, center, guides and other items) or **with the arrow keys** (1 mm; `Shift` 10 mm; `Alt` 0.1 mm — one undo step per keypress), resizes from the corner (the cursor shows it), and has its properties in the panel. **Double-clicking** a text edits it in place; on a frame it enters view editing.

**Selecting several**: drag a box from empty sheet space — from left to right selects what is **enclosed** (blue), from right to left what it **touches** (dashed green); `Shift` toggles, `Ctrl` adds, `Shift+Ctrl` removes. A click on the empty sheet deselects.

**What is underneath**: when one item covers another (a title over the frame's scale label), `Ctrl+Alt+click` selects the one below and, repeating, keeps going down the stack; or right-click ▸ **Select the item underneath**. The panel's **Items** list always reaches everything.

With a **right-click** on any item:

- **Bring to front / Raise / Lower / Send to back** — the stacking order (draw a background rectangle, send it back, and put everything on top).
- **Lock** (`Ctrl+L`) — the item stays visible but **out of the mouse's reach**: neither a click nor a box picks it up, so dimensions and texts on a locked frame can be edited without catching the frame. The only door is the panel's **Items** list: from there it is selected, edited and unlocked. The padlock marks it.
- **Arrange** — align and distribute the selection (two or more items), **group and ungroup** (`Ctrl+G`, `Ctrl+Shift+G`; a group is dragged together), **duplicate** (`Ctrl+D`). The "Arrange" toolbar with these buttons is hidden by default; right-click the toolbar to show it.
- **Copy style / Paste style** (`Ctrl+Shift+C` / `Ctrl+Shift+V`) between items of the same type — and the toolbar's **Format painter**: click the source item, click the targets, `Esc`.

**Clipboard**: `Ctrl+C`, `Ctrl+X`, `Ctrl+V` copy items within a sheet (the paste lands 5 mm lower and to the right) or **between sheets** (it lands in the same place). Linked texts and dimensions anchored to a copied frame follow the pasted frame. **The title block is copied too**: pasted on another sheet, it takes the place of that sheet's own.

## Rulers and guides { #reglas-y-guias }

As in QGIS: **drag from the top ruler** onto the page and out comes a **vertical guide** (dashed blue line); from the left one, a horizontal guide. Items **snap to guides** when moved or resized. A guide slides along its axis; to remove it, drag it back to the ruler or select it and press `Del`; right-click a ruler ▸ **Clear all guides**. They are saved with the sheet and are not printed.

Continue with **[View frames and scale](marcos.md)** — the heart of the composer.
