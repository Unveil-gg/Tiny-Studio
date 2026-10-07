# Collaboration — three peers, one human

Roles write files. They do not share one growing transcript.

## Roles (specialty, not rank)

| Agent            | Writes                                         |
|------------------|------------------------------------------------|
| game-developer   | `design/specs/schema.json`, engine code        |
| game-designer    | `design/specs/mechanics.md`, feature intent    |
| game-artist      | `design/specs/art_style.md`, slot metadata     |

No “director class.” A role may **critique** by writing options into the
artifact. **You** resolve conflicts. The next role reads the file, not the
previous chat.

## When to invoke whom

| Situation                         | Lead          | Reads                         |
|-----------------------------------|---------------|-------------------------------|
| New project or reset              | any           | `/start` writes the index     |
| Idea phase                        | designer      | index; then mechanics         |
| Feature before code               | designer      | mechanics; feature file       |
| Implementation                    | developer     | feature file, schema, mechanics |
| Visual consistency                | artist        | art style, mechanics          |
| Playable feedback                 | one role      | `/playtest-review` appends    |
| Evidence-based issues             | developer     | `/qa` writes a review note    |
| Share milestone                   | one role      | `/ship-check` writes a note   |

Invoke the next role in a **new** turn after the file is updated. Do not
simulate the other two voices in the same session.

## Disagreement protocol

1. State **A** and **B** plainly in the artifact (not “some people say…”).
2. Tie each to **pillars** and **scope** when possible.
3. Recommend nothing **by fiat** — recommend **by tradeoff**.
4. Stop. **Ask the human** when the call is creative, not technical.

## Tone

Smart, candid, playful, respectful of **time** and **energy**. The goal is a
**shippable game you’re proud of**, not a performance of being busy.
