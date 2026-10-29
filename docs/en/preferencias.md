---
source_blob: 39b89b874215b54477fc0d9fcb438c46bfe3fe10
---

# Preferences

**Window ▸ Preferences…** gathers the program's settings. **OK** saves; **Cancel** touches nothing. Almost everything applies live; the language needs a restart.

## General { #general }

- **Language**: Spanish, English or Brazilian Portuguese (also in Window ▸ Language). Applies after a restart. A system in Portuguese starts in Portuguese the first time; anything not yet translated appears in English.
- **Rest of model while editing**: when you enter a group, everything else normal, **dimmed** or **hidden**. Same as Camera ▸ Rest of model while editing.
- **Auto-save every N minutes.** IngeTrazo saves a backup copy of the document in your data folder (never next to the file: cloud-synced drives have truncated writes there). The copy only exists between a change and the next clean save: if there is a copy the next time you open that document, the session was interrupted, and the program **offers to recover it**. The timer does not fire while a mouse button is held down.
- **Recover a discarded auto-save…** (in the File menu): if you said no to recovery and regret it, discarded copies are kept separately and can be opened from there.
- **Keep a backup of the previous save (`.igz.bak`)**: before writing, the previous file is copied alongside as `name.igz.bak`. A truncated save (power cut, full disk) never takes the good version with it.
- **Invert mouse wheel zoom.**
- **Anti-aliasing (MSAA)**: 0, 2, 4 or 8 samples. More samples, smoother edges and more work for the graphics card.
- **Undo steps**: how many operations the history keeps (200 by default; 0 = unlimited). Each step carries a snapshot of the model, so in a large model the limit is memory. Applies immediately.
- **Ask for a name and symbol when placing a section plane**: turns back on the dialog that appears when placing a [section plane](modelado/secciones.md) if you turned it off with "Don't ask again".

## Import

- **Suggested unit for OBJ** and **for DXF/DWG**: the preselected answer in the dialog that asks for the unit on import (the dialogs still ask: CAD headers often lie, and IngeTrazo also **suggests it by measuring the drawing**).
- **Coordinates**: geographic (lat/lon) or UTM WGS84, for the terrain panel.

## Units { #unidades }

The **units of the document you have open** — they are saved with it, not in the program. Choose the length unit (meters, centimeters, millimeters, inches, feet, feet and inches, or the fractional `1 1/2"`) and the decimals. It governs both directions:

- A number typed **without a unit** is in it: `2` is 2 mm in a millimeter document; `2m` is always 2 m (the explicit unit wins).
- Everything the program **displays** —tools, Entity info, status bar, per-material summary— reads in it.
- The **dimension style** follows it when you change it; its own panel can override it afterwards.

A new document is born in meters, and documents from before 0.4.9 open in meters. Changing the unit **does not change the geometry**, only how it is read and typed. With the fractional ones, **Decimals** sets the finest denominator: 0 = whole inches, 1 = 1/4, 2 = 1/16, 3 = 1/32, 4 = 1/64.

## AI Assistant

The same fields as the [AI Assistant](ia.md): provider, key, model, Ollama URL and whether viewport captures are sent to the model.

## What the program remembers on its own

- **File ▸ Open Recent**: the last ten `.igz` documents opened or saved, with "Clear list"; the ones that no longer exist disappear by themselves. An import (`.skp`, `.dxf`…) does not count as a recent document.
- **Folders**: every open, save, import or export dialog starts in the **last folder you chose** in any of them (if there is none, in the open document's folder; failing that, in Documents).
- **The layout** of toolbars and panels.
- **The dimension style** of the last dimension you edited in the composer, and the default **title block** and **sheet** templates.
- On Windows, with a dual-graphics laptop (Intel + NVIDIA/AMD), the first run asks the system for the **dedicated graphics card** for IngeTrazo. If the viewport is slow, **Help ▸ About** tells you which card is drawing and warns if it is a software rasterizer.
