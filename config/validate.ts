/**
 * Checks studio.config.json, spec artifacts, and agent turn budgets.
 *
 * Usage: npm run validate
 */

import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

import { z, ZodError } from "zod";

import {
  AGENT_FILES,
  CHANGELOG_CAP,
  SPEC_HEADINGS,
  assetHooksSchema,
  gameSchemaSchema,
  studioConfigSchema,
  type StudioConfig,
} from "./schema.js";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");

/** Reads a UTF-8 text file from the repo root. */
function readText(relativePath: string): string {
  return readFileSync(resolve(ROOT, relativePath), "utf8");
}

/** Parses a JSON file. Returns an Error when the file is not JSON. */
function readJson(relativePath: string): unknown | Error {
  try {
    return JSON.parse(readText(relativePath)) as unknown;
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    return new Error(`${relativePath}: ${message}`);
  }
}

/** Formats a Zod failure as path: message pairs. */
function formatZod(error: ZodError): string {
  return error.issues
    .map((issue) => {
      const path = issue.path.join(".") || "(root)";
      return `${path}: ${issue.message}`;
    })
    .join("; ");
}

/** Parses the leading frontmatter block. Null when it is missing. */
function readFrontmatter(
  markdown: string,
): Record<string, string> | null {
  if (!markdown.startsWith("---\n") && !markdown.startsWith("---\r\n")) {
    return null;
  }
  const end = markdown.indexOf("\n---", 3);
  if (end === -1) {
    return null;
  }
  const body = markdown.slice(markdown.indexOf("\n") + 1, end);
  const fields: Record<string, string> = {};
  for (const line of body.split(/\r?\n/)) {
    const splitAt = line.indexOf(":");
    if (splitAt === -1) {
      continue;
    }
    const key = line.slice(0, splitAt).trim();
    const value = line.slice(splitAt + 1).trim();
    if (key) {
      fields[key] = value;
    }
  }
  return fields;
}

/** Returns the text of each level-2 heading. */
function h2Headings(markdown: string): string[] {
  const headings: string[] = [];
  for (const line of markdown.split(/\r?\n/)) {
    const match = /^##\s+(.+?)\s*$/.exec(line);
    if (match) {
      headings.push(match[1]);
    }
  }
  return headings;
}

/** Counts bullets under ## Changelog. Zero when the section is absent. */
function changelogCount(markdown: string): number {
  const lines = markdown.split(/\r?\n/);
  const start = lines.findIndex((line) => line.trim() === "## Changelog");
  if (start === -1) {
    return 0;
  }
  let count = 0;
  for (const line of lines.slice(start + 1)) {
    if (line.startsWith("## ")) {
      break;
    }
    if (/^\s*-\s+/.test(line)) {
      count += 1;
    }
  }
  return count;
}

/** Reads maxTurns from an agent card. */
function readMaxTurns(markdown: string): number | Error {
  const match = /^maxTurns:\s*(\d+)\s*$/m.exec(markdown);
  if (!match) {
    return new Error("maxTurns is missing");
  }
  return Number(match[1]);
}

/** Checks revision, updated, required headings, and changelog length. */
function checkMarkdownSpec(
  relativePath: string,
  required: readonly string[],
  errors: string[],
): void {
  let markdown: string;
  try {
    markdown = readText(relativePath);
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    errors.push(`${relativePath}: ${message}`);
    return;
  }

  const frontmatter = readFrontmatter(markdown);
  if (!frontmatter) {
    errors.push(`${relativePath}: missing frontmatter`);
  } else {
    if (!/^\d+$/.test(frontmatter.revision ?? "")) {
      errors.push(`${relativePath}: revision must be an integer`);
    }
    if (!frontmatter.updated) {
      errors.push(`${relativePath}: updated is empty`);
    }
  }

  const headings = new Set(h2Headings(markdown));
  for (const heading of required) {
    if (!headings.has(heading)) {
      errors.push(`${relativePath}: missing heading "## ${heading}"`);
    }
  }

  const notes = changelogCount(markdown);
  if (notes > CHANGELOG_CAP) {
    errors.push(
      `${relativePath}: changelog has ${notes} entries (max ${CHANGELOG_CAP})`,
    );
  }
}

/** Checks a JSON artifact against a Zod schema. */
function checkJsonArtifact(
  relativePath: string,
  schema: z.ZodTypeAny,
  errors: string[],
): void {
  const parsed = readJson(relativePath);
  if (parsed instanceof Error) {
    errors.push(parsed.message);
    return;
  }
  const result = schema.safeParse(parsed);
  if (!result.success) {
    errors.push(`${relativePath}: ${formatZod(result.error)}`);
  }
}

/** Fails when an agent card's maxTurns drifts from config. */
function checkTurnBudgets(config: StudioConfig, errors: string[]): void {
  const budgets = config.turnBudget;
  const roles = Object.keys(AGENT_FILES) as Array<
    keyof typeof AGENT_FILES
  >;
  for (const role of roles) {
    const relativePath = AGENT_FILES[role];
    let markdown: string;
    try {
      markdown = readText(relativePath);
    } catch (err) {
      const message = err instanceof Error ? err.message : String(err);
      errors.push(`${relativePath}: ${message}`);
      continue;
    }
    const maxTurns = readMaxTurns(markdown);
    if (maxTurns instanceof Error) {
      errors.push(`${relativePath}: ${maxTurns.message}`);
      continue;
    }
    if (maxTurns !== budgets[role]) {
      errors.push(
        `${relativePath}: maxTurns is ${maxTurns}; ` +
          `studio.config.json turnBudget.${role} is ${budgets[role]}`,
      );
    }
  }
}

/** Runs every check. Returns 0 when the studio contract holds. */
function main(): number {
  const errors: string[] = [];
  const rawConfig = readJson("studio.config.json");
  if (rawConfig instanceof Error) {
    console.error(rawConfig.message);
    return 1;
  }
  const configResult = studioConfigSchema.safeParse(rawConfig);
  if (!configResult.success) {
    console.error(
      `studio.config.json: ${formatZod(configResult.error)}`,
    );
    return 1;
  }
  const config = configResult.data;

  checkMarkdownSpec(
    config.artifacts.mechanics,
    SPEC_HEADINGS.mechanics,
    errors,
  );
  checkMarkdownSpec(
    config.artifacts.artStyle,
    SPEC_HEADINGS.artStyle,
    errors,
  );
  checkJsonArtifact(config.artifacts.schema, gameSchemaSchema, errors);
  checkJsonArtifact(config.artifacts.assetHooks, assetHooksSchema, errors);
  checkTurnBudgets(config, errors);

  if (errors.length > 0) {
    for (const error of errors) {
      console.error(error);
    }
    return 1;
  }
  console.log("studio contract ok");
  return 0;
}

process.exit(main());
