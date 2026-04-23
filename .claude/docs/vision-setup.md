# Tiny Studio vision MCP

Local **Model Context Protocol** server for **screen snapshots**: primary
monitor (all platforms) or a **Windows** window matched by title substring.
Images are capped to **720p-class** (max 1280×720, aspect preserved), saved under
**`.tiny_studio/snapshots/`**, and old files are pruned automatically.

**Privacy:** snapshots can include anything on screen. Pause on a safe frame
before capturing.

## 1. Install (Python venv)

From the **repository root** (the folder that contains `core/` and
`.claude/`):

```bash
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements-vision.txt
```

**macOS / Linux:**

```bash
source .venv/bin/activate
pip install -r requirements-vision.txt
```

### macOS note

Screen capture may require **Screen Recording** permission for the app that
starts Python (Terminal, Cursor, Codex, etc.). Grant it in **System Settings →
Privacy & Security → Screen Recording**.

## 2. Tools exposed

| Tool | Purpose |
|------|---------|
| `take_game_snapshot` | Capture primary monitor (`window_title` empty) or a Windows window whose title contains the given string. Returns `path`, `base64_png`, `capture_mode`, `error`. |
| `prune_snapshots` | Manually delete old PNGs (`max_age_hours`, `keep_latest`). |

**Workflow tip:** Use **borderless fullscreen** on the **primary** monitor, then
call `take_game_snapshot` with an empty `window_title` for the most reliable
frame.

## 3. Claude Code

Use your venv’s `python` and run the module from the repo root:

```bash
claude mcp add tiny-vision -- <path-to-venv-python> -m core.vision.mcp_server
```

Set the process **working directory** to the repo root if your Claude Code MCP
wrapper supports `cwd` (some configs require it so `core` resolves).

Example (Windows paths, adjust user and clone location):

```text
claude mcp add tiny-vision -- C:\Users\you\indie-c\.venv\Scripts\python.exe -m core.vision.mcp_server
```

## 4. Cursor

1. Open **Settings → Features → MCP** (wording may vary slightly by version).
2. Add a server with transport **stdio** / type **command**.
3. **Command:** path to the venv `python` executable.
4. **Arguments:** `-m`, `core.vision.mcp_server` (two separate args).
5. **Working directory:** this repository root (`indie-c`).
6. Save and **reload** MCP or restart Cursor if tools do not appear.

## 5. Codex CLI and Codex Desktop (Windows focus)

Codex stores MCP servers in **`config.toml`**. Defaults live at
**`%USERPROFILE%\.codex\config.toml`**. You can also scope servers to a **trusted
project** with **`.codex/config.toml`** at the repo root (same shape).

Official overview: [Model Context Protocol (Codex)](https://developers.openai.com/codex/mcp).

### Codex Desktop on Windows (recommended order)

1. **Repo path** — Use your real clone path (example:
   `C:\Users\you\src\indie-c`). Below, replace `REPO` with that path.
2. **Venv + deps** — In PowerShell: `cd REPO`, then
   `python -m venv .venv`, `.\.venv\Scripts\Activate.ps1`,
   `pip install -r requirements-vision.txt`.
3. **Register MCP** — Prefer **Option B** (`config.toml` with **`cwd`**) so
   `python -m core.vision.mcp_server` always resolves the `core` package.
   Add the `[mcp_servers.tiny-vision]` block under **`%USERPROFILE%\.codex\config.toml`**
   or **`REPO\.codex\config.toml`** (project scope requires a **trusted**
   project in Codex).
4. **Restart Codex Desktop** completely so it reloads MCP config.
5. **Prepare the screen** — Game or scene on the **primary** monitor
   (borderless fullscreen is ideal).
6. **In chat** — Ask Codex to use the **`take_game_snapshot`** tool with
   **`window_title` empty** (full primary monitor).
7. **Verify** — Check **`.tiny_studio\snapshots\`** for a new `.png` and a tool
   result with **`path`** and **`base64_png`**. If the tool hangs or times out,
   add **`tool_timeout_sec`** under `[mcp_servers.tiny-vision]` (see Codex MCP
   docs; default is often 60s).

### Option A — `codex mcp add` (CLI)

From any shell, after activating the same venv you use for Codex:

```bash
codex mcp add tiny-vision -- C:\path\to\indie-c\.venv\Scripts\python.exe -m core.vision.mcp_server
```

If the CLI supports setting cwd for the server, set it to the **repo root**.
If snapshots fail to import `core`, add a project **`config.toml`** (Option B)
with `cwd` set.

Check registration:

```bash
codex mcp --help
```

In the Codex **TUI**, use **`/mcp`** to see active servers.

### Option B — `config.toml` (CLI + Desktop + IDE extension)

Codex shares this configuration across **CLI**, **Desktop**, and the **IDE
extension**. In the Desktop app, open **MCP settings → Open config.toml** from
the gear menu if available, or edit the file directly.

Add (adjust `command` and `cwd` to your machine):

```toml
[mcp_servers.tiny-vision]
command = "C:\\path\\to\\indie-c\\.venv\\Scripts\\python.exe"
args = ["-m", "core.vision.mcp_server"]
cwd = "C:\\path\\to\\indie-c"
enabled = true
```

**Desktop test checklist**

1. Create the venv under the repo and `pip install -r requirements-vision.txt`.
2. Add the server via **`codex mcp add`** or **`config.toml`** as above.
3. Restart **Codex Desktop** so it picks up MCP changes.
4. Put your game (or desktop) on the **primary monitor** in a representative
   state.
5. Ask Codex to call **`take_game_snapshot`** with `window_title` empty (or a
   substring of the game window title on Windows).
6. Confirm a PNG appears under **`.tiny_studio/snapshots/`** and that the tool
   returns a non-empty `path` and `base64_png`.

If tools time out, raise **`tool_timeout_sec`** for `tiny-vision` in
`config.toml` (see Codex MCP docs).

## 6. Troubleshooting

| Symptom | What to try |
|---------|-------------|
| `Missing MCP SDK` / import error | `pip install -r requirements-vision.txt` in the same interpreter used in MCP config. |
| `No visible window title containing ...` | Use `window_title: ""` for primary monitor, or windowed mode with a distinctive title. |
| Wrong crop / scaling (Windows) | Prefer primary-monitor capture with borderless fullscreen. |
| `core` module not found | Set MCP **`cwd`** to the repo root; use `python -m core.vision.mcp_server`. |
| macOS blank or denied | Grant **Screen Recording** to the parent app. |

## 7. Cleanup

Snapshots are ignored by Git (see root **`.gitignore`**). Automatic pruning runs
after each successful capture; call **`prune_snapshots`** if you want to tidy up
mid-session.

## 8. Local smoke test (no MCP)

From the **repo root**, with the venv active and vision deps installed:

```powershell
python -c "from core.vision.capture import take_snapshot; print(take_snapshot(''))"
```

Expect `('ok', {..., 'path': '...', 'base64_png': '...'})`. If imports fail,
re-run `pip install -r requirements-vision.txt` using that same `python`.
