---
name: vertical-slice
description: >-
  Master orchestration for a playable vertical slice. Requires design/gdd.md
  (run /start first). Checks providers, gates paid calls at asset-plan
  confirmation, runs generation skills, integrates, and playtests. No
  framework dependency — pipeline.py is the optional automation layer.
---

# /vertical-slice — Playable slice orchestration

## Goal

Fastest playable vertical slice with coherent design — not maximum asset
count. Improve feel and pacing before generating more content.

## Precondition

`design/gdd.md` must exist with a confirmed `## Vertical slice scope`.
Run `/start` if it does not.

## Pipeline

---

### Stage 1 — Provider check

Call MCP tool `check_asset_providers`, or run
`python tools/orchestration/providers.py`:

| Provider    | Env var                         | Status if absent  |
|-------------|---------------------------------|-------------------|
| ElevenLabs  | `ELEVENLABS_API_KEY`            | missing           |
| Tripo AI    | `TRIPO_API_KEY`                 | missing           |
| Nano Banana | `GEMINI_API_KEY` / `GOOGLE_API_KEY` | missing       |
| Blender     | `blender --version` → 0         | unavailable       |
| Snapshots   | `take_game_snapshot` MCP        | unavailable       |

For each missing provider: note which asset type uses a placeholder.

---

### Stage 2 — Asset plan

Run `/asset-plan` — present the budget and estimated API calls.

**Gate: wait for explicit developer approval before Stage 3.**
A "go" or "ok" counts. Silence does not.

---

### Stage 3 — Asset generation

Requires **`tiny-assets` MCP** (see `.claude/docs/assets-setup.md`).
For each asset in the confirmed plan:
- Audio → `/gen-audio` → `gen_audio`
- 3D models → `/gen-3d` → `gen_3d_draft` (optional `gen_3d_refine`)
- 2D assets → `/gen-2d` → `gen_2d`

If a provider is unavailable, create a placeholder and continue — do not
stop the pipeline. Log each failure.

---

### Stage 4 — Integration

Place all verified assets in the correct project structure.
Update `design/asset-plan.md` with final status per asset.
Note assets requiring manual work (rigging, scene placement, etc.).

---

### Stage 5 — Playtest

Build and launch per README. If `take_game_snapshot` MCP is available,
capture the gameplay view, HUD, and menu.
Run `/qa` — check readability, missing assets, runtime issues, visual
consistency with GDD art direction, and control feel.

---

## Optional automation

```
python tools/orchestration/pipeline.py --project-root .
```

Runs Stages 1–2 checks and prints a status summary. Generation (Stage 3)
is always driven by skill prompts, not automated code.

## Platform defaults

Default to **web prototype** unless the GDD implies otherwise.
If the request implies native, desktop, console, or Steam-first:
> "Which platform should be targeted first?"

Default native stack: **SDL3 + bgfx**.

## Never

- Spend paid API calls without Stage 2 approval
- Generate filler assets not in the confirmed asset plan
- Generate variants by default — one canonical asset per slot
- Block the build because one provider or asset failed
