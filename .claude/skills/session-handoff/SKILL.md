---
name: session-handoff
description: >-
  End-of-session continuity artifact. Captures branch intent, files in flight,
  next tasks, blockers, and one surprise. Appends a dated entry to
  design/session-log.md. Use at the end of every working session.
---

# /session-handoff -- End-of-session continuity

## Purpose

Leave a clear trail so the next session (human or agent) starts oriented, not
lost. Five fields, fixed format, no improvising.

## Steps

1. **Ask** the human if anything in the summary looks wrong before saving.
2. **Append** the block below to `design/session-log.md` (create if missing).
3. Confirm the file was written.

## Output format (fixed -- all fields required)

```markdown
## Session: YYYY-MM-DD

**Branch intent:** <one sentence: what this branch is trying to prove or ship>

**Files in flight:**
- <path> -- <why it is unfinished>

**Next 3 tasks (ordered):**
1. <most urgent>
2. <second>
3. <third>

**Known blockers:**
- <blocker or "none">

**One thing that surprised us today:**
<one sentence>
```

## Tone

Honest, minimal. If you don't know a field, write "unknown" -- never skip it.

## Do not

- Summarize the whole session in prose
- Invent tasks that were not discussed
- Run before asking the human to confirm the summary
