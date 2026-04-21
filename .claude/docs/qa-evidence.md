# QA — evidence before opinions

## Why

Players experience **builds**, not intentions. The `/qa` workflow assumes **truth
from running software** whenever the environment allows it.

## Ladder (best → fallback)

1. **Run** the game or automated tests using project conventions (README scripts,
   engine shortcuts, CI commands).
2. **Read logs**: stderr, engine console, test output, crash dumps.
3. **Visual capture**: screenshots, GIFs, short clips — especially for UI,
   readability, animation timing.
4. **User-provided evidence** when the agent cannot run binaries (hardware,
   licenses, GPU-only tools).
5. **Static analysis only** as last resort — label guesses as **hypotheses**.

## What to record

- **Command or action** used to produce evidence
- **Result** (pass/fail, observable behavior)
- **Artifact** path or pasted excerpt when helpful

## Honesty rule

If the agent did not run the game, the report must say so. **Speculation** is
fine if labeled; **false certainty** is not.

## Tips for solo devs

- Keep a **`/qa` habit** on every merge-worthy slice — cheap now, expensive
  later if skipped.
- One **GIF** of the core loop beats three paragraphs of “it feels okay.”
