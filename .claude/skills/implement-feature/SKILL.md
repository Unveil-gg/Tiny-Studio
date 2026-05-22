---
name: implement-feature
description: Developer-led build in slices; verifies design/visual intent before coding. Use after feature is specified.
---

# /implement-feature -- Build the thing

## Lead

**game-developer** drives. Pull **game-designer** and **game-artist** in for:

- Ambiguous behavior -> designer
- Readability, feedback, UI -> artist

## Preconditions

- Prefer an existing `design/features/<slug>.md`. If missing, **draft a micro-spec
  in-chat** (5 bullets max) and get user confirmation before large edits.
- Check `design/pillars.md` for studio mode (`jam` vs `studio`) -- calibrate
  quality gates accordingly.

## Steps

1. **Restate** the feature in one paragraph -- dev voice.
2. **Check intent** -- any contradictions with `design/pillars.md`? Flag early.
3. **Plan** the smallest shippable slice (tasks in order).
4. **Implement** one slice at a time:
   - After each slice, **stop and check**:

     > Stop. Does this slice run? What is broken? Do not begin the next slice
     > until the current slice is confirmed playable or the breakage is logged.

   - Note how to **run / try** it before moving on.
5. **Self-review** (dev + quick art/design pass in prose):
   - Does it match acceptance criteria?
   - **Juice** list: missing feedback, default sounds, placeholder art risks.

## Engineering habits

- Prefer **data/config** for tuning when the designer will iterate numbers.
- Avoid drive-by refactors outside the feature unless necessary for safety.
- Log or expose **debug views** temporarily if it speeds validation (remove or
  gate later).

## End state

Summarize: **files touched**, **how to test**, **known gaps**. Suggest
`/playtest-review` or `/qa` when something is runnable.

## Do not

- Gold-plate or expand scope without user approval
- Skip mentioning breaking changes
- Begin the next slice while the current one is broken and unlogged
