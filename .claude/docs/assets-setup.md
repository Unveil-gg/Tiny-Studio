# Tiny Studio asset generation MCP

Local **Model Context Protocol** server for **audio, 2D, and 3D asset
generation**. API keys are read inside the server process from environment
variables only — they are never returned to the LLM.

**Paid providers:** ElevenLabs (audio), Tripo AI (3D), Nano Banana / Gemini
(2D). Missing keys produce **labeled placeholders** under `assets/`.

## 1. Install (Python venv)

From the **repository root**:

```bash
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements-assets.txt
```

**macOS / Linux:**

```bash
source .venv/bin/activate
pip install -r requirements-assets.txt
```

## 2. Environment variables

Set only the providers you plan to use. Never commit keys.

| Provider | Variable | Used by |
|----------|----------|---------|
| ElevenLabs | `ELEVENLABS_API_KEY` | `gen_audio` |
| Tripo AI | `TRIPO_API_KEY` | `gen_3d_draft`, `gen_3d_refine` |
| Nano Banana | `GEMINI_API_KEY` or `GOOGLE_API_KEY` | `gen_2d` |

Optional: `TINY_STUDIO_PROJECT_ROOT` — repo root when MCP cwd differs.

## 3. Tools exposed

| Tool | Purpose |
|------|---------|
| `check_asset_providers` | Sanitized status for all providers (no key values). |
| `gen_audio` | ElevenLabs sound effect → `assets/audio/<category>/`. |
| `gen_2d` | Nano Banana image → `assets/2d/<category>/`. Default model: `nano-banana-2`. |
| `gen_3d_draft` | Tripo text-to-3D draft GLB (~90s timeout). Returns `task_id`. |
| `gen_3d_refine` | Tripo refine from draft `task_id` (~180s timeout). |

Each tool writes a `.meta.json` sidecar next to the asset.

**3D workflow:** call `gen_3d_draft` → review → optionally `gen_3d_refine`
with the returned `task_id`. Refine costs more credits; confirm in
`/asset-plan` first.

## 4. Cursor

1. **Settings → Features → MCP** → add stdio server.
2. **Command:** venv `python` executable.
3. **Arguments:** `-m`, `core.assets.mcp_server`
4. **Working directory:** this repository root.
5. Reload MCP after saving.

Raise `tool_timeout_sec` to at least **200** for Tripo refine calls.

## 5. Claude Code

```bash
claude mcp add tiny-assets -- <path-to-venv-python> -m core.assets.mcp_server
```

Set working directory to the repo root.

## 6. Codex CLI / Desktop

Add to `%USERPROFILE%\.codex\config.toml` or `REPO\.codex\config.toml`:

```toml
[mcp_servers.tiny-assets]
command = "C:\\path\\to\\indie-c\\.venv\\Scripts\\python.exe"
args = ["-m", "core.assets.mcp_server"]
cwd = "C:\\path\\to\\indie-c"
enabled = true
tool_timeout_sec = 200
```

## 7. Skill integration

Generation skills call MCP tools instead of raw HTTP:

- `/gen-audio` → `gen_audio`
- `/gen-2d` → `gen_2d`
- `/gen-3d` → `gen_3d_draft` (then optional `gen_3d_refine` after review)

Verification (duration, style, readability) stays in the skill — the MCP
tool generates and returns metadata; the agent decides accept / retry /
placeholder.

## 8. Local smoke test (no MCP)

```powershell
python -m core.assets.providers
```

With keys set, test one provider:

```powershell
python -c "from core.assets.elevenlabs_gen import generate_audio; print(generate_audio('short click', 'ui-click'))"
```

## 9. Troubleshooting

| Symptom | What to try |
|---------|-------------|
| `Missing MCP SDK` | `pip install -r requirements-assets.txt` |
| Placeholder returned | Check `check_asset_providers` notes; key may be missing. |
| Tripo timeout | Draft ~90s, refine ~180s; raise MCP `tool_timeout_sec`. |
| `banned` task status | Prompt violated content policy — do not retry. |
| Empty GLB / PNG | Tool rejects zero-byte files; check provider dashboard. |
