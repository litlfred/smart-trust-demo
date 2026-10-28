/**
 * Draw each journey's BPMN (processes/content/*.bpmn) as an SVG beside its
 * source, with bootstrap-tools' renderer (bpmn-js in headless Chromium), as
 * bootstrap commits its own diagrams. ig_gen.py embeds these SVGs in the
 * business processes page, so the page shows the diagrams whichever publish
 * route builds the site.
 *
 *   bun tools/render-bpmn/render_bpmn.ts          (write)
 *   bun tools/render-bpmn/render_bpmn.ts --check  (fail if an SVG is stale)
 */
import { existsSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, relative, resolve } from "node:path";
import { besideSource, openRenderer, processIds, VIEWER_BUNDLE } from "@litlfred/bootstrap-tools/scripts/render-bpmn.ts";

const root = resolve(import.meta.dir, "..", "..");
const dir = join(root, "processes", "content");
const check = process.argv.includes("--check");
const sources = readdirSync(dir).filter((f) => f.endsWith(".bpmn")).sort().map((f) => join(dir, f));

let viewer: string;
try {
  viewer = Bun.resolveSync("bpmn-js/dist/bpmn-viewer.production.min.js", root);
} catch {
  viewer = join(root, VIEWER_BUNDLE);
}
if (!existsSync(viewer)) {
  console.error(`bpmn-js is not installed (${viewer}): run bun install`);
  process.exit(1);
}
const processFile = new Map<string, string>();
for (const f of sources) for (const id of processIds(readFileSync(f, "utf-8"))) processFile.set(id, f);
const r = await openRenderer(viewer);
let bad = 0;
for (const file of sources) {
  const out = file.replace(/\.bpmn$/, ".svg");
  const shown = relative(root, out);
  const got = await besideSource(r, file, processFile);
  if ("error" in got) {
    console.error(`✗ ${relative(root, file)}: ${got.error}`);
    bad++;
    continue;
  }
  const prev = existsSync(out) ? readFileSync(out, "utf-8") : undefined;
  if (check) {
    if (prev === got.svg) console.log(`✓ ${shown} up to date`);
    else {
      console.error(`✗ ${shown} is stale: run bun tools/render-bpmn/render_bpmn.ts`);
      bad++;
    }
    continue;
  }
  writeFileSync(out, got.svg);
  console.log(`${prev === got.svg ? "=" : "✓"} ${shown}`);
}
await r.close();
process.exit(bad > 0 ? 1 : 0);
