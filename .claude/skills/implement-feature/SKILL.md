---
name: implement-feature
description: >-
  Leads implementation with game-developer; verifies design intent and visual
  implications before coding. Encourages small iterative builds. Use after a
  feature is specified (or with explicit assumptions if spec is thin).
---

# /implement-feature — Build the thing

## Lead

**game-developer** drives. Pull **game-designer** and **game-artist** in for:

- Ambiguous behavior → designer
- Readability, feedback, UI → artist

## Preconditions

- Prefer an existing `design/features/<slug>.md`. If missing, **draft a micro-spec
  in-chat** (5 bullets max) and get user confirmation before large edits.

## Steps

1. **Restate** the feature in one paragraph — dev voice.
2. **Check intent** — any contradictions with `design/pillars.md`? Flag early.
3. **Plan** the smallest shippable slice (tasks in order).
4. **Implement** with frequent checkpoints:
   - After each logical step, note how to **run / try** it.
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
