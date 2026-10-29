---
source_blob: e01c1d9807f15ad9c5a84655d7ee1832e0753322
---

# Modeling with AI

IngeTrazo has two ways to let an artificial intelligence model for you. In both, the AI **does not touch the mesh**: it writes a *recipe* —revolutions, extrusions, Python on the actions API— and IngeTrazo's deterministic engine runs it. That is why the usual guarantees still hold:

- **Every AI action is one undo step.** `Ctrl+Z` removes it completely.
- **If its code fails, the document reverts by itself** to the previous state — it is never left half-done.
- Every recipe goes through the **watertightness guard**: the solids it produces are real solids, measurable and printable.
- What it builds is normal geometry: named groups that you edit by hand, paint, dimension and take to the sheets.

| | AI Assistant (inside the app) | MCP bridge (from an external agent) |
|---|---|---|
| Where | **Extensions ▸ AI Assistant** (`Ctrl+Shift+A`) | **Extensions ▸ AI Bridge (MCP)** + any MCP client: Claude Code, Claude Desktop, Cursor, VS Code, Antigravity CLI (Google), Codex CLI… |
| What you need | An API key from the provider you choose (Groq has a free quota) or a local Ollama | An installed MCP client (with its own account or key) |
| How you talk | Chat inside IngeTrazo, with an optional photo | Conversation in your agent; it draws in the open app |
| Who sees the model | The assistant receives viewport captures (optional) | The agent asks for captures and queries the model whenever it wants |

## The AI Assistant, step by step

![The AI Assistant open over a solar street-light pole: provider, key, the captures checkbox and the request typed in the text box.](images/asistente-ia.jpeg)

1. **Extensions ▸ AI Assistant** (or `Ctrl+Shift+A`). A floating dialog opens over the model.
2. **Provider.** Pick one or leave *Auto*: the key's prefix detects it automatically (`sk-ant-` is Anthropic, `gsk_` is Groq, `AIza` is Gemini…). Each provider **remembers its own key and model**: if you run out of quota on one, you switch to another in two clicks.

    | Provider | Key | Sees images | Notes |
    |---|---|:-:|---|
    | **Groq** | [console.groq.com/keys](https://console.groq.com/keys) | — | Generous free quota; very fast. Default model `openai/gpt-oss-120b`. |
    | **Google Gemini** | [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) | ✔ | Free quota. Default `gemini-2.5-flash`. |
    | **Anthropic (Claude)** | console.anthropic.com | ✔ | Paid. |
    | **OpenAI** | platform.openai.com | ✔ | Paid. `gpt-4o` by default. |
    | **OpenRouter** | openrouter.ai | ✔ | One place for many models. |
    | **DeepSeek** | platform.deepseek.com | — | Cheap. |
    | **Ollama** | *(no key)* | depends on the model | **On your own machine, without internet.** Install Ollama and leave the key empty; the default URL is `http://localhost:11434`. |

3. **API key.** Paste it into the field. It is saved in your user profile, never in the document. The link under the field takes you to the page where you get one. **No key, no answer** (Groq is free, but it needs a key): if you leave it empty or the provider rejects it, the assistant says so plainly with the link to get one, instead of a raw 401 error.
4. **Model.** Empty = the provider's default model. **Models** lists the ones your key can actually use; **Test connection** validates the key before you start.
5. **Send viewport screenshots to the model.** With a provider that *sees* (Claude, GPT, Gemini), after each step the assistant receives an image of what it built, looks at it and corrects itself. With a model without vision the checkbox does no harm: the image is simply not sent.
6. **Type the request and press Enter.** With dimensions: *"draw a circular fountain 4 m in diameter and 0.6 m high, with a 20 cm rim"*. The assistant replies, shows the recipe it is going to run and the result appears in the model. Keep the conversation going to correct it: *"make it 20 cm taller"*, *"paint it stone"*.
7. **Photo…** attaches an image (a photo of the real piece, a sketch, a capture of a drawing) and the model **reconstructs what it shows**. Give it the real dimensions in the same message — the photo gives the shape; you give the size.

!!! tip "How to ask so it comes out right"
    - **One piece per message**, with its dimensions: "4.5 m pole, 3" pipe" works better than "a complete park".
    - **Correct instead of repeating**: the assistant keeps the context and the groups it created; "the arm is too long, make it 60 cm" edits what is there.
    - If the answer gets cut off, the assistant detects it and **asks for the continuation on its own**; if it goes over the step limit, it tells you and with "continue" it picks up where it left off.
    - **Ctrl+Z** with the model window active undoes the last recipe completely.

!!! note "What is stored where"
    Keys and provider live in your user preferences (they can also be edited in **Window ▸ Preferences ▸ AI Assistant**). The `.igz` document only stores the resulting geometry: you can share it without exposing any key.

## The MCP bridge, step by step

![Full Ubuntu desktop: Claude Code in the terminal, on the left, lists the dimensions of the table with four chairs it has just drawn through the bridge; IngeTrazo, on the right, shows the model and the AI Bridge (MCP) dialog with the connection line.](images/mcp-claude.jpeg)

The [Model Context Protocol](https://modelcontextprotocol.io) is an **open standard**, not something specific to Claude: any agent that speaks MCP —Claude Code, Claude Desktop, Cursor, VS Code with Copilot, Windsurf, Google's Antigravity CLI, Codex CLI…— can operate IngeTrazo **live, with the app open**: it draws, queries and looks at the model, and each of its actions is one undo step. IngeTrazo neither chooses nor pays for the model: that is up to your client.

1. **Turn on the bridge**: **Extensions ▸ AI Bridge (MCP)**. IngeTrazo starts a local server (only on `127.0.0.1`, port 4763) and opens a window with the exact lines for your system, with a **Copy** button. The same menu turns it off.
2. **Connect your client** — just once:

    === "Claude Code (terminal)"

        ```bash
        # Windows (installer or zip)
        claude mcp add ingetrazo -- "C:\Program Files\IngeTrazo\ingetrazo-mcp.exe"
        # Linux: AppImage, tar.gz, Flatpak or snap
        claude mcp add ingetrazo -- <IngeTrazo executable> --mcp
        # from source
        claude mcp add ingetrazo -- python3 /path/to/app/scripts/ingetrazo_mcp.py
        ```

        You do not need Python installed: the package includes the MCP server (`ingetrazo-mcp.exe` on Windows, `ingetrazo --mcp` on Linux).

    === "Claude Desktop"

        Paste this into its configuration file (`%APPDATA%\Claude\claude_desktop_config.json` on Windows, `~/.config/Claude/claude_desktop_config.json` on Linux) and restart Claude Desktop:

        ```json
        {
          "mcpServers": {
            "ingetrazo": {
              "command": "C:\\Program Files\\IngeTrazo\\ingetrazo-mcp.exe",
              "args": []
            }
          }
        }
        ```

    === "Other MCP clients"

        They all take the **same** `mcpServers` **block** from above (or its equivalent), each in its own file:

        | Client | Where to paste it |
        |---|---|
        | Cursor | `~/.cursor/mcp.json` (or Settings ▸ MCP ▸ *Add new server*) |
        | VS Code (Copilot) | the project's `.vscode/mcp.json`, with the key `servers` instead of `mcpServers` |
        | Windsurf | `~/.codeium/windsurf/mcp_config.json` |
        | Antigravity CLI (Google) | `~/.gemini/config/mcp_config.json` (or `.agents/mcp_config.json` in the project folder). It is the successor of Gemini CLI: Google ended free Google-account access to Gemini CLI on 2026-06-18 and that account no longer gets in; Antigravity has a **free Individual** plan with weekly limits. Install it with `curl -fsSL https://antigravity.google/cli/install.sh \| bash`; the command is `agy`. |
        | Codex CLI | `~/.codex/config.toml`, section `[mcp_servers.ingetrazo]` with `command` and `args` |

        In all of them, `command` is the IngeTrazo executable with `--mcp` (or `ingetrazo-mcp.exe` on Windows), exactly as the bridge window shows it.

3. **Ask it for things**, with IngeTrazo open and the bridge on: *"design a 1.60 × 0.90 dining table with four wooden chairs"*, *"draw the arch from sheet E02 with all its rebar"*, *"show me how it turned out"*. The agent writes recipes, runs them, takes captures to check itself and tells you what it did. You watch the result in the app in real time and correct it as you would with any colleague: *"the chairs are too close together"*.

What the agent can do:

| Tool | What it does |
|---|---|
| `run_python` | Runs Python on the live document, with `scene`, `selection`, `groups`, `QVector3D`… and the builders `revolve(profile)` and `extrude(outline, z0, z1)`: one line → a solid, smooth, oriented group. One undo per call; if it fails, nothing changes. |
| `query_model` | Counts, names of groups and components, materials, layers, bounding box. |
| `screenshot` | Renders the real viewport: the agent looks and iterates. |
| `undo` / `redo` | The usual history. |

!!! tip "If the agent does not respond"
    Check that IngeTrazo is still open **with the bridge on** (the Extensions menu shows it as *listening*), that the command path exists, and in your client that the `ingetrazo` server shows as connected and without errors (in Claude Desktop: Settings ▸ Developer ▸ MCP). The server accepts one client at a time and never listens outside your machine.

## What has been made this way

The [examples](primeros-pasos/ejemplos.md) that come with IngeTrazo were largely drawn through the MCP bridge: the solar street light (pole, truncated-cone pedestal, footing and its rebar), the Yanque welcome arch with all its rebar, lampposts, letters and sculpture, and the pedestal of the *campesino* statue with its footing. Open them and look at the groups: they are executed recipes, not black boxes.

!!! info "Other modelers sell this as a subscription"
    In IngeTrazo the AI is free: you use whatever key you want (or a local model) and nothing goes through IngeTrazo servers. Without AI, the program works exactly the same and without internet.
