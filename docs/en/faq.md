---
source_blob: aea4b2ba9df073c64a75345855d2bcfb588e6658
---

# Frequently asked questions

## Is it really free?

Yes. IngeTrazo is **free software under the GPL-3.0**: free today and forever, with the code published on GitHub. No accounts, no subscriptions, no locked features.

## Does it work without internet?

Yes — the whole modeler, BIM and the sheet composer work **offline**. Only the satellite map, the 3D terrain, the online component library and the AI (except with local Ollama) use the network while you use them; your drone survey, once imported, also works without a connection.

## Does it have artificial intelligence?

Yes, in two ways: the built-in **AI Assistant** (a chat with the key of whichever provider you prefer; Groq has a free quota, and Ollama runs on your own machine) and the **MCP bridge** so that any MCP-capable agent (Claude Code, Claude Desktop, Cursor, VS Code, Gemini CLI…) can draw in the open app. In both cases the AI generates recipes that the engine runs, every step can be undone and the model stays editable by hand. See [Modeling with AI](ia.md).

## Can I open my `.skp` files?

Yes, directly and **without converters**: the native importer reads `.skp` from every version of the format with geometry, groups, components, materials, textures, layers, scenes and dimensions. IngeTrazo does not write `.skp`: your work is saved as `.igz` and shared in open formats (IFC, DAE, OBJ, glTF, STL, DXF). See [Import and export](importar-exportar.md).

## Are my files locked into a proprietary format?

No. `.igz` is an **open, documented** format (JSON / ZIP). Even if IngeTrazo disappeared tomorrow, your models would remain readable. You can also export to IFC, OBJ, STL, glTF, DAE, SKP and DXF whenever you want.

## Why does the program sometimes reject a push/pull?

Because that operation would have left a broken (non-watertight) solid. IngeTrazo prefers **refusing to corrupt the model**: retry the push from another face or check for overlapping geometry. That guarantee is what makes the takeoffs and the printable STL reliable.

## The dimension on my sheet changed by itself — why?

Because it is **anchored to the model** and the model changed — the dimension followed the vertex and measured again: that is its job. If you want a fixed paper dimension, drag one of its ends (it is released from the anchor) or draw it without snapping to the green points.

## It closed without saving — did I lose my work?

Probably not: **auto-save** (every few minutes, adjustable in [Preferences](preferencias.md)) leaves a copy that the program offers to **recover** the next time you open that document; if you discard it and regret it, File ▸ Recover a discarded auto-save…. And every save leaves the previous one as `.igz.bak` next to the file.

## Are there example files?

Four real documents with their sheets: [Examples to open](primeros-pasos/ejemplos.md).

## How accurate are the terrain and the drone survey?

The satellite 3D terrain uses a global DEM (~30 m resolution) — perfect for context. Your **drone survey** has the accuracy of your flight (centimeter-level in plan with good processing). Without ground control points, the drone's altitude is GNSS and can differ from sea level by a few meters — IngeTrazo notes this in the exported profiles.

## Does it run on my machine?

IngeTrazo needs OpenGL 3.3 (any graphics card from the last decade) and runs especially well on Linux — Windows and macOS too. Real models with hundreds of thousands of triangles orbit at 60 fps. On a laptop with two graphics cards, the program asks for the dedicated one; **Help ▸ About** tells you which one is drawing.

## How do I report a problem?

On [GitHub](https://github.com/ingelibre/ingetrazo/issues), ideally with the file that reproduces it (`.igz` or `.skp`). Users' sample files are the main source of importer improvements.
