---
name: gen-add
description: >-
  Creates or updates design/add.md — the formal Art Direction Document
  referenced by all generation skills. Artist-led. Run /art-direction first
  for the vibe pass; run /gen-add to formalize it into a generation-ready
  spec. Separate from design/art-notes.md.
---

# /gen-add — Art Direction Document

## Lead

**game-artist** drives. Consult:
- **game-designer** — emotional beat, player readability needs
- **game-developer** — shader/material constraints, texture budget, platform

## Preconditions

1. Read `design/pillars.md` — visual direction section.
2. Read `design/gdd.md` — ADD must serve the gameplay (e.g. fast-read
   silhouettes if the GDD has enemies to dodge). If `gdd.md` is missing,
   stop and run `/gen-gdd` first.
3. Read `design/art-notes.md` if it exists — `add.md` formalizes those notes,
   it does not replace them. Keep the two files consistent.

## Steps

1. **Check** whether `design/add.md` already exists. If so, present proposed
   changes as a diff rather than silent overwrite.
2. **Fill** every section in the template below. Mark genuinely unknown
   values as `TBD` — never omit a field.
3. **Cross-check** the "Explicitly avoid" section against `design/art-notes.md`
   do/don't pairs. They must not contradict each other.
4. **Confirm** with the developer before writing.

## Template: `design/add.md`

```markdown
# Art Direction Document — <title>

_Last updated: <date>. References: design/gdd.md, design/art-notes.md._

## Visual style
One paragraph: the overall look and feel.

## Inspiration references
3–5 titles or artworks. One sentence why each is relevant.

## Color palette
Primary, secondary, accent, danger, success, neutral — hex values.

## Lighting direction
Time of day, shadow hardness, ambient tone.

## Character proportions
Silhouette style, detail level, anatomy note.

## Environment style
Materials, density, landmark readability.

## UI style
Hierarchy approach, corner language, spacing personality.

## Iconography style
Literal vs abstract, stroke weight, fill rules.

## Texture / material guidelines
PBR vs stylized, texture budget, atlas approach.

## Animation tone
Snappy vs floaty, anticipation level, idle personality.

## Audio direction
SFX palette (dry/wet, synthetic/organic), music genre anchor.

## Explicitly avoid
Bullet list of things that would break this style. Be specific — not
"avoid generic AAA" but "avoid lens flare, avoid desaturated palettes,
avoid humanoid proportions above 6 heads tall."
```

## Do not

- Contradict `design/art-notes.md` without noting the change explicitly
- Mark a field `TBD` that the GDD clearly implies
- Exceed ~80 lines unless the developer requests depth
- Proceed to `/asset-plan` until the developer approves this file
