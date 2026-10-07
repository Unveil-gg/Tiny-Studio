---
name: playtest-review
description: >-
  One role reviews a build or feature and appends a short note to
  design/reviews/<date>.md, then stops. Invoke each role separately.
---

# /playtest-review — One role, one note

## Who writes this turn

The role that was invoked. Write only that lens:

- **game-designer** — loop, motivation, difficulty, clarity of rules
- **game-developer** — responsiveness, bugs, perf, implementation risks
- **game-artist** — readability, UI, motion, mood, cohesion

Read the specs and any notes already in the review file. Do not rewrite
another role's note. Do not speak in their voice.

## Target

`design/reviews/<YYYY-MM-DD>.md` (create the folder and file if needed).

If playable, prefer a real run or `/qa` evidence. This skill interprets
what would confuse a new player.

## Append

```markdown
## <role> — YYYY-MM-DD

- Working: <one sentence>
- Friction: <one sentence>
- Next: <one concrete step>
```

If you disagree with a note already in the file, add one bullet:
`Disagree: A vs B — human picks.` Then stop.

## Stop

Done when your note is appended. If `maxTurns` hits first, append
`## Blocked` with what you could not judge, then stop.

## Do not

- Write the other two roles' sections
- Pretend a missing role agrees with you
- Turn the note into an essay
- Generate assets
