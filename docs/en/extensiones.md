---
source_blob: 05df8cdcd5a13ace1e9db12a52c862d652b427ed
---

# Extensions

Since version **0.3.2**, IngeTrazo can be extended with **plugins**: small
programs that add new tools without touching the application. Everything lives in
the **Extensions** menu of the top bar.

Several extensions come built in: **Model Info**, the **Python
Console**, the **Solid Inspector** and — since version 0.3.5 — the
**AI Assistant** and the **AI Bridge (MCP)** ([Modeling with AI](ia.md)).

## Model Info

**Extensions ▸ Model Info** opens a complete X-ray of the document,
in three tabs:

- **Geometry** — vertices, edges, faces and triangles (totals, loose
  geometry and groups), the **bounding box** in your document's units, and
  the count of annotations (dimensions, texts, guides, scenes, routes).
- **Materials & Layers** — every material in use with **how many faces carry it
  and how many m² it paints** (direct data for a finishes takeoff), and the list
  of layers with their visibility and lock.
- **BIM** — the tagged objects with their IFC class, **area and volume**. These are
  the same numbers as in the BIM panel and the `.ifc` export: a six-face wall
  with a single tag counts as **one** object, not six.

![Model Info on a real project file](images/extensiones-info-del-modelo.png)

The **Copy to clipboard** button exports the summary as plain text, ready
to paste into a report or an email.

!!! tip "The numbers don't lie"
    Model Info reads the same sources as the rest of the program. If the
    dialog says 3 IfcWall with 45 m², that is exactly what reaches the `.ifc` — and
    [IngePresupuestos](https://ingepresupuestos.com).

## Python Console

**Extensions ▸ Python Console** (or `Ctrl+Shift+P`) opens a programming
console **live on the open model**. It is the tool for advanced users: inspecting the
model, generating geometry by code, automating repetitive tasks.

What matters, even if you never write code:

- **Everything a script creates is ONE undo step.** `Ctrl+Z` (with the
  model window active) removes it completely, like any other edit.
- **A script that fails leaves nothing half-done**: the document reverts by itself to the
  previous state and the console shows the error in red.
- Changes mark the document as **modified** — when closing without saving,
  IngeTrazo warns you, as always.

Want to see it in action without writing a line? Click **"Run script
file…"** and choose `scripts/create_architectural_showcase.py` (it ships with the
program): it builds a small pavilion with slab, columns, walls and roof,
**fully BIM-tagged** — and a single `Ctrl+Z` undoes it. The
**"API help"** button shows the available objects and code snippets to
get started.

![The pavilion from the example script, freshly built from the console](images/extensiones-consola-pabellon.png)

## Solid Inspector

**Extensions ▸ Solid Inspector** diagnoses why a group is not a
watertight solid (3D-printable, measurable by volume): it lists every
problem edge — open borders, edges with more than two faces — and highlights them
in the viewport so you can find them at a glance.

## AI Assistant and AI Bridge (MCP)

The two ways of **modeling with AI** have their own page: [Modeling with AI](ia.md). In short:

- **Extensions ▸ AI Assistant** (`Ctrl+Shift+A`): a chat inside IngeTrazo where you describe what you want —or attach a photo— with the key of the provider you choose (Groq free, Gemini, OpenAI, Anthropic, OpenRouter, DeepSeek or local Ollama).
- **Extensions ▸ AI Bridge (MCP)**: any agent that speaks the Model Context Protocol (Claude Code, Claude Desktop, Cursor, VS Code, Gemini CLI, Codex CLI…) drives the open app; the package includes the server (`ingetrazo-mcp.exe` on Windows, `ingetrazo --mcp` on Linux) and the menu gives you the exact lines to connect it.

In both cases every action is **one undo step** and a failure reverts the whole document — the same guarantees as the Python Console.

## Installing a third-party extension

An extension is a `.py` file. Copy it to your personal plugins folder
(**Extensions ▸ Open plugins folder** creates and opens it for you) and
restart IngeTrazo:

=== "Linux"

    ```
    ~/.local/share/ingetrazo/plugins/
    ```

=== "Windows"

    ```
    %APPDATA%\ingetrazo\plugins\
    ```

Its tools appear in the **Extensions** menu. If the plugin has an
error, **IngeTrazo still opens**: the entry appears grayed out as
`⚠ name (error loading)` and, hovering the mouse over it, you see the exact error
to report to the author. To uninstall, delete the file.

!!! warning "Only install trusted extensions"
    A plugin runs code with the same permissions as IngeTrazo: it can read
    and write your files. It is the same trust arrangement as Blender
    extensions or those of any program — only install what comes from a
    source you know.

## Writing your own extension

If you program in Python, the developer guide is in the
repository — **Extensions ▸ Develop a plugin…** opens it directly:
[`docs/plugins.md`](https://github.com/ingelibre/ingetrazo/blob/main/docs/plugins.md)
— the minimal example is ~10 lines, and the Python Console is the natural
test bench: what works in the console works in a plugin.

The code of all built-in extensions is free (GPL-3.0) and lives in the
[`plugins/`](https://github.com/ingelibre/ingetrazo/tree/main/plugins) folder
of the repository — the AI Assistant itself is a plugin and serves as a complete
example. Contributions are welcome: the extension engine itself
was born from community contributions.

!!! note "The API is not stable yet"
    During the 0.x series the plugin system may change between versions.
    An extension published today may need adjustments in the next version.
