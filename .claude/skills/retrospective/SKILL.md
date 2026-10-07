---
name: retrospective
description: >-
  Post-ship self-improvement loop. The invoked role answers three questions
  and appends only its subsection to design/retros.md. Run after every
  /ship-check. Other roles append on their own turns.
---

# /retrospective -- Post-ship loop

## Purpose

Learn from each ship. The invoked role answers three questions and appends
only its subsection. Other roles write later. No shared transcript.

## When to run

After every `/ship-check`. Can also run after a major `/playtest-review` or
mid-project if the team feels stuck.

## Three questions (the role that was invoked)

1. **What worked?** -- one concrete thing that helped ship or improve quality
2. **What slowed us?** -- one concrete friction point, not blame
3. **One change for next time** -- actionable, specific, small

## Steps

1. Write only your subsection. Leave the other roles for a later invocation.
   If a subsection already exists, do not rewrite it.
2. Human may add their own answers in a later edit.
3. **Append** your subsection to `design/retros.md` (create if missing).
   Use the date heading if it is not there yet; do not duplicate it.
4. Confirm the append completed. Suggest one next step, then stop.

## Output format (appended to retros.md)

```markdown
## Retro: YYYY-MM-DD -- <milestone or feature name>

### game-developer
- Worked: <one sentence>
- Slowed: <one sentence>
- Change: <one sentence>

### game-designer
- Worked: <one sentence>
- Slowed: <one sentence>
- Change: <one sentence>

### game-artist
- Worked: <one sentence>
- Slowed: <one sentence>
- Change: <one sentence>

### Human (optional)
- <freeform>
```

## Do not

- Expand into multi-paragraph post-mortems
- Write another role's subsection -- they append on their own turn
- Run this during a ship-check; it comes after

## Stop

**Target:** `design/retros.md`

Done when your subsection is appended. If `maxTurns` hits first, append
`## Blocked` and stop.
