import { z } from "zod";

/** Studio pace. jam ships fast; studio keeps quality gates. */
export const studioModeSchema = z.enum(["jam", "studio"]);

/** Repo-relative paths the agents read and write. */
export const artifactPathsSchema = z
  .object({
    index: z.string().min(1),
    mechanics: z.string().min(1),
    schema: z.string().min(1),
    artStyle: z.string().min(1),
    assetHooks: z.string().min(1),
  })
  .strict();

/** Hard cap on agent turns. Mirrored by maxTurns in each role card. */
export const turnBudgetSchema = z
  .object({
    designer: z.number().int().positive(),
    developer: z.number().int().positive(),
    artist: z.number().int().positive(),
  })
  .strict();

/** External asset tool. Disabled means Tiny Studio never calls it. */
export const masonHookSchema = z
  .object({
    enabled: z.boolean(),
    mcpServer: z.string().min(1),
  })
  .strict();

/** Typed studio setup. No API keys. */
export const studioConfigSchema = z
  .object({
    studioMode: studioModeSchema,
    turnBudget: turnBudgetSchema,
    artifacts: artifactPathsSchema,
    externalTools: z
      .object({
        mason: masonHookSchema,
      })
      .strict(),
  })
  .strict();

export type StudioConfig = z.infer<typeof studioConfigSchema>;

/**
 * Game data contract. Required keys only; the developer may add fields.
 */
export const gameSchemaSchema = z.object({
  revision: z.number().int().nonnegative(),
  updated: z.string().min(1),
  entities: z.array(z.unknown()),
  state: z.record(z.unknown()),
  serialization: z.record(z.unknown()),
});

/** One slot an external tool may fill later. No generation prompt. */
export const assetSlotSchema = z
  .object({
    id: z.string().min(1),
    kind: z.enum(["model", "sprite", "audio", "ui"]),
    purpose: z.string().min(1),
    status: z.literal("unassigned"),
  })
  .strict();

/** Asset-slot manifest. Metadata only. */
export const assetHooksSchema = z
  .object({
    revision: z.number().int().nonnegative(),
    updated: z.string().min(1),
    slots: z.array(assetSlotSchema),
  })
  .strict();

/** Level-2 headings each markdown spec must contain. */
export const SPEC_HEADINGS = {
  mechanics: [
    "Verbs",
    "Loop",
    "Progression",
    "Win / lose",
    "State machine",
  ],
  artStyle: ["Palette", "Type", "Layout", "Motion"],
} as const;

/** Newest changelog bullets kept on a spec. Older ones are dropped. */
export const CHANGELOG_CAP = 5;

/** Role card whose maxTurns must match turnBudget. */
export const AGENT_FILES = {
  designer: ".claude/agents/game-designer.md",
  developer: ".claude/agents/game-developer.md",
  artist: ".claude/agents/game-artist.md",
} as const;
