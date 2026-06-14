---
name: check-providers
description: >-
  Checks availability of all asset-generation providers (ElevenLabs, Tripo AI,
  Nano Banana, Blender, snapshot tools). Returns sanitized status only. Never
  reads or logs API key values. Use before /asset-plan or /vertical-slice.
---

# /check-providers — Provider status report

## Purpose

Tell the developer which providers are ready before any paid call is made.
Output is **sanitized status only** — `configured` / `missing` /
`unavailable` / `installed`. No key values ever reach chat, logs, or LLM
context.

## Steps

1. **Run** the provider check module if Python is available:

   ```
   python tools/orchestration/providers.py
   ```

   Capture and display the status table it returns.

2. **If Python is unavailable**, check manually:
   - ElevenLabs: `ELEVENLABS_API_KEY` env var set? → `configured` / `missing`
   - Tripo AI: `TRIPO_API_KEY` env var set? → `configured` / `missing`
   - Nano Banana: `GOOGLE_API_KEY` env var set? → `configured` / `missing`
   - Blender: `blender --version` exits 0? → `installed` / `unavailable`
   - Snapshot tools: `take_game_snapshot` MCP available? →
     `configured` / `unavailable`

3. **Display** a compact status table:

   | Provider       | Status       | Used by          |
   |----------------|--------------|------------------|
   | ElevenLabs     | configured   | /gen-audio       |
   | Tripo AI       | missing      | /gen-3d          |
   | Nano Banana    | configured   | /gen-2d          |
   | Blender        | installed    | /gen-3d (post)   |
   | Snapshot tools | unavailable  | /vertical-slice  |

4. **For each missing provider**: note which asset type uses a placeholder.
   Do not block. Do not suggest workarounds that introduce unlisted tools.

5. **Never**:
   - Print, echo, or log any API key value
   - Pass key values into any prompt or tool argument
   - Stop the session because a provider is missing

## Output

Status table + one-line note per missing provider describing what placeholder
replaces it. Suggest `/asset-plan` as the next step.
