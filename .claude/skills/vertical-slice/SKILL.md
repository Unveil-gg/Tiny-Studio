---
name: vertical-slice
description: >-
  Master orchestration command. Runs the full asset generation pipeline for a
  playable vertical slice: GDD → ADD → provider check → asset plan → generation
  → integration → playtest. Uses LangGraph when available. All paid calls
  require explicit developer confirmation at the planning gate.
---

# /vertical-slice — Playable slice orchestration

## Goal

Fastest **playable** vertical slice with coherent design — not maximum asset
count. Improve gameplay feel before generating more content.

## Lead

All three agents contribute at their designated stages. Developer runs the
orchestration. User confirms at every gate.

## Precondition

`design/pillars.md` must exist. Run `/start` if it does not.

## Pipeline

Run stages in order. Each stage is a gate for the next.

---

### Stage 1 — Design alignment

1. Run `/gen-gdd` — create or confirm `design/gdd.md`.
2. Run `/gen-add` — create or confirm `design/add.md`.

**Gate:** Do not proceed until both documents are confirmed by the developer.

---

### Stage 2 — Provider and budget check

3. Run `/check-providers` — display sanitized status table.
4. Run `/asset-plan` — present asset budget and estimated API calls.

**Gate:** Wait for explicit developer approval. Do not proceed past this point
until the developer confirms. A vague "go" or "ok" counts. Silence does not.

---

### Stage 3 — Asset generation

For each asset in the confirmed plan, run the appropriate skill:

- Audio assets → `/gen-audio`
- 3D assets → `/gen-3d`
- 2D assets → `/gen-2d`

Rules during generation:
- Only generate assets the GDD vertical slice scope explicitly names
- If a provider is unavailable, create a placeholder and continue — do not
  stop the pipeline
- If a single asset fails twice, log it and move to the next asset

---

### Stage 4 — Integration

5. Place all verified assets into the correct project structure.
6. Update `design/asset-plan.md` with final status per asset.
7. Note any asset requiring manual work (rigging, scene placement, etc.)
   in a brief integration summary.

---

### Stage 5 — Playtest

8. Build and launch the project per README instructions.
9. If `take_game_snapshot` MCP is available, capture:
   - Main gameplay view
   - HUD / UI elements
   - Menu or title screen (if present)
10. Run `/qa` — check readability, missing assets, runtime issues, visual
    consistency with ADD, and control feel.
11. Produce actionable feedback sorted by severity.

---

## LangGraph mode (optional)

If Python and LangGraph are available, run the automated workflow:

```
python tools/orchestration/workflow.py --project-root .
```

This executes the same pipeline with shared state in
`tools/orchestration/state.py`. The graph enforces the Stage 2 gate
automatically — Stage 3 nodes will not run until `plan_approved` is set.

If LangGraph is unavailable, follow the manual stage sequence above.
The pipeline is identical; only the state tracking differs.

## Platform defaults

Default to **web prototype** unless the project or GDD implies otherwise.
If the request implies native, desktop, console, or Steam-first:

> "Which platform should be targeted first?"

Default native stack: **SDL3 + bgfx**.

## Iteration philosophy

After the first slice lands:
- Fix feel and pacing issues before generating more assets
- Use `/implement-feature` to add mechanics, not `/gen-2d` to add art
- Re-run `/vertical-slice` only for scope-expanding milestones

## Never

- Spend paid API calls without confirmation at the Stage 2 gate
- Generate environment filler assets not in the confirmed asset plan
- Generate variants by default — one canonical asset per slot
- Block the build because one provider or asset failed
- Allow Stage 3 to begin before Stage 2 approval is explicitly confirmed
