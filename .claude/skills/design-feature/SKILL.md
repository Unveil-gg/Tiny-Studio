---
name: design-feature
description: >-
  Leads feature design with game-designer perspective; pulls in developer and
  artist angles for feasibility and readability. Produces a concise feature spec.
  Use before implementing a meaningful gameplay, UI, or content feature.
---

# /design-feature — Lean feature spec

## Roles (single session, three voices)

- **Lead: game-designer** — problem, player outcome, loop fit, scope
- **Contributions: game-developer** — feasibility, edge cases, perf risks
- **Contributions: game-artist** — clarity, telegraphing, UI/motion needs

## Steps

1. **Name the feature** in user’s language; confirm **why now** (priority).
2. **Player story**: “As a player, I can…” + **success moment**.
3. **Rules (plain language)** — inputs, outputs, failure, edge cases (bullet list).
4. **Feel & clarity** — telegraphing, feedback, audio/VFX hooks (light).
5. **Cut line** — what is explicitly **out** for v1.
6. **Acceptance** — 3–5 testable bullets (behavior + feel).

## Output

Write to `design/features/<slug>.md` where `<slug>` is kebab-case (create
`design/features/` if needed). Template:

```markdown
# Feature: <Title>
## Why
## Player experience
## Rules & edge cases
## Visual / UI notes
## Out of scope (v1)
## Acceptance criteria
## Open questions
```

Keep the file **under ~120 lines** unless the user asks for depth.

## End state

Ask: “Ready to `/implement-feature` this, or edit the spec first?”

## Do not

- Hide disagreements — if dev and art pull different ways, state both and let the
  user choose
