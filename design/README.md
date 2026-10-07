# Design artifacts

Agents read and write these files. They do not share one transcript.

- **`gdd.md`** — short index (title, mode, pillars, links). `/start` fills it.
- **`specs/mechanics.md`** — designer. Verbs, loop, progression, win/lose.
- **`specs/schema.json`** — developer. Entities, state, serialization.
- **`specs/art_style.md`** — artist. Palette, type, layout, motion.
- **`specs/asset_hooks.json`** — slot metadata for an external tool. No prompts.
- **`features/`** — one file per feature from `/design-feature`.
- **`reviews/`** — one-role notes from `/playtest-review`, `/qa`, `/ship-check`.
- **`pillars.md`** — legacy scratchpad. The index supersedes it.

`npm run validate` checks the spec contract. Keep files **short**.
