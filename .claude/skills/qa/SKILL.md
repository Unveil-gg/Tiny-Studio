---
name: qa
description: >-
  Lightweight quality pass: runs game/tests when possible, uses logs, screenshots,
  or captures for evidence. Reviews controls, feedback, readability, pacing,
  bugs, polish. Use before merges, after features, or on release candidates.
---

# /qa -- Evidence-first quality pass

## Philosophy

**Look at reality first**, speculate second. If the environment can run the game
or tests, **do it**. If not, fall back gracefully.

## Evidence ladder (try in order)

1. **Run** -- project scripts (`npm test`, `dotnet test`, engine headless if
   available), or launch build per README.
2. **Logs** -- console output, crash logs, CI artifacts.
3. **Screenshots / GIFs / short video** -- user-provided or captured when tools
   exist (e.g. OS screenshot, engine capture).
4. **Static review** -- only when nothing runs: code + assets + honesty about
   limits.

Document **what was observed** vs **inferred**.

## Checklist (compact)

- **Controls** -- input lag, dead zones, remapping, "do I feel direct?"
- **Feedback** -- hit reactions, audio/visual sync, failure clarity
- **Readability** -- silhouettes, UI contrast, motion noise
- **Pacing** -- downtime, overload, tutorial drag
- **Bugs** -- repro steps if found
- **Polish gaps** -- missing edge cases, placeholder fatigue
- **Charm** -- note moments that **already** delight

## Output

### Environment

What ran; what could not run and why.

### Evidence summary

Bullets tied to artifacts, logs, or screenshots.

### Regression table (required -- all rows must be filled)

| Feature | Expected | Actual | Pass/Fail |
|---------|----------|--------|-----------|
| <name>  | <behavior> | <observed> | Pass / Fail / ESTIMATE |

Label any row where you could not run the feature as **ESTIMATE**. Do not
omit rows -- if you cannot observe a feature, write ESTIMATE in Actual and
explain in a note below the table.

### Severity-sorted issues

P0 blockers first, then P1 important, then P2 nice-to-fix.

### Suggested next command

`/implement-feature`, `/art-direction`, or `/ship-check`.

## Tone

Constructive, precise, kind -- **QA as a sparring partner**, not a tribunal.

## Do not

- Claim you played the game if you only read code
- Invent repro steps -- use "ESTIMATE" or "unverified hypothesis" language
- Omit the regression table, even when evidence is thin
