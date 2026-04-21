---
name: qa
description: >-
  Lightweight quality pass: runs game/tests when possible, uses logs, screenshots,
  or captures for evidence. Reviews controls, feedback, readability, pacing,
  bugs, polish. Use before merges, after features, or on release candidates.
---

# /qa — Evidence-first quality pass

## Philosophy

**Look at reality first**, speculate second. If the environment can run the game
or tests, **do it**. If not, fall back gracefully.

## Evidence ladder (try in order)

1. **Run** — project scripts (`npm test`, `dotnet test`, engine headless if
   available), or launch build per README.
2. **Logs** — console output, crash logs, CI artifacts.
3. **Screenshots / GIFs / short video** — user-provided or captured when tools
   exist (e.g. OS screenshot, engine capture).
4. **Static review** — only when nothing runs: code + assets + honesty about
   limits.

Document **what was observed** vs **inferred**.

## Checklist (compact)

- **Controls** — input lag, dead zones, remapping, “do I feel direct?”
- **Feedback** — hit reactions, audio/visual sync, failure clarity
- **Readability** — silhouettes, UI contrast, motion noise
- **Pacing** — downtime, overload, tutorial drag
- **Bugs** — repro steps if found
- **Polish gaps** — missing edge cases, placeholder fatigue
- **Charm** — note moments that **already** delight

## Output

```markdown
## Environment (what ran, what couldn’t)
## Evidence summary (bullets tied to artifacts/logs)
## Severity-sorted issues
## Quick wins vs deeper fixes
## Suggested next command (/implement-feature, /art-direction, /ship-check)
```

## Tone

Constructive, precise, kind — **QA as a sparring partner**, not a tribunal.

## Do not

- Claim you played the game if you only read code
- Invent repro steps — use “unverified hypothesis” language instead
