---
name: retrospective
description: >-
  Post-ship self-improvement loop. Each agent answers three questions: what
  worked, what slowed us, one change for next time. Appends to
  design/retros.md. Run after every /ship-check.
---

# /retrospective -- Post-ship loop

## Purpose

Learn from each ship. Three questions, three voices, one append to the retro
log. Keeps the studio improving without turning into a feelings meeting.

## When to run

After every `/ship-check`. Can also run after a major `/playtest-review` or
mid-project if the team feels stuck.

## Three questions (each agent answers all three)

1. **What worked?** -- one concrete thing that helped ship or improve quality
2. **What slowed us?** -- one concrete friction point, not blame
3. **One change for next time** -- actionable, specific, small

## Steps

1. Each agent (developer, designer, artist) answers the three questions in
   their own voice -- brief, honest, specific.
2. Human may add their own answers or amend any agent's answer.
3. **Append** the block below to `design/retros.md` (create if missing).
4. Confirm the append completed.
5. Suggest one `/implement-feature` or process tweak that addresses the most
   common "slowed us" answer.

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
- Skip an agent's section -- write "no input" if truly nothing to say
- Run this during a ship-check; it comes after
