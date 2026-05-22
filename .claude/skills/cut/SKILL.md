---
name: cut
description: >-
  Explicit descope with memory. Documents what is removed, who proposed it,
  and why. Appends a "## Cuts" section to the relevant feature spec. Nothing
  is silently dropped.
---

# /cut -- Explicit descope

## Purpose

Cuts happen. The problem is when they happen silently. This skill makes every
cut **visible, attributable, and reversible** -- logged where the feature lives,
not buried in chat.

## Steps

1. **Name the feature file**: `design/features/<slug>.md`. If it does not
   exist, create a stub with just the title before adding cuts.
2. **Collect** from the human (or confirm from context):
   - What is being removed
   - Who proposed the cut (human / designer / developer / artist)
   - Why (scope, fun, time, complexity, or other)
3. **Append** the block below to the feature file. Do not overwrite existing
   content.
4. Confirm the append completed.

## Output format (appended to feature file)

```markdown
## Cuts

| What | Proposed by | Why | Date |
|------|-------------|-----|------|
| <item> | <role/human> | <reason> | YYYY-MM-DD |
```

Add one row per cut. Multiple cuts in one session = multiple rows, one append.

## Tone

Neutral, factual. No editorializing. The log is for future-you, not a postmortem.

## Do not

- Delete or rewrite any existing section of the feature spec
- Record cuts to CLAUDE.md or pillars.md -- feature file only
- Mark something as cut without a reason, even if the reason is "human said so"
