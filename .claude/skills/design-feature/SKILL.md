---
name: design-feature
description: Designer-led feature spec with dev+artist input. Use before implementing gameplay, UI, or content.
---

# /design-feature -- Lean feature spec

## Roles (single session, three voices)

- **Lead: game-designer** -- problem, player outcome, loop fit, scope
- **Contributions: game-developer** -- feasibility, edge cases, perf risks
- **Contributions: game-artist** -- clarity, telegraphing, UI/motion needs

## Steps

1. **Name the feature** in user's language; confirm **why now** (priority).
2. **Player story**: "As a player, I can..." + **success moment**.
3. **Rules (plain language)** -- inputs, outputs, failure, edge cases (bullet list).
4. **Feel & clarity** -- telegraphing, feedback, audio/VFX hooks (light).
5. **Not in this slice** -- what is explicitly deferred (non-optional; see below).
6. **Risk** -- three mandatory bullets (see below).
7. **Acceptance** -- 3-5 testable bullets (behavior + feel).

## Output

Write to `design/features/<slug>.md` where `<slug>` is kebab-case (create
`design/features/` if needed). Template:

```markdown
# Feature: <Title>
## Why
## Player experience
## Rules & edge cases
## Visual / UI notes
## Not in this slice
## Risk
## Acceptance criteria
## Open questions
```

### Not in this slice (required)

List everything that was discussed but will **not** ship in v1. If nothing was
explicitly deferred, write at least one thing you considered and rejected.
Omitting this section means the spec is incomplete.

### Risk (required)

Exactly three bullets -- one each:
- **What makes this unfun?** (player-facing failure mode)
- **What makes this unreadable?** (clarity / feedback failure)
- **What makes this unmaintainable?** (code / scope failure)

Keep each bullet to one sentence. Not optional.

Keep the file **under ~120 lines** unless the user asks for depth.

## End state

Ask: "Ready to `/proof-of-fun` this, then `/implement-feature`?"

## Do not

- Hide disagreements -- if dev and art pull different ways, state both and let
  the user choose
- Skip "Not in this slice" or "Risk" -- both are required sections
