// The FHIR examples the walkthrough's payload drawer shows are this
// repository's own IG examples (input/fsh/examples/), as SUSHI writes them to
// fsh-generated/resources/. They are copied into src/data/ig/ so the
// walkthrough builds without SUSHI and the FHIR packages; the copy is never
// edited by hand:
//
//   node web/scripts/ig-examples.mjs           # after `sushi build .`: refresh the copy
//   node web/scripts/ig-examples.mjs --check   # fail if the copy differs from SUSHI's output
//
// CI runs --check in the ig-sushi job, after SUSHI.
import { mkdir, readFile, writeFile } from 'node:fs/promises';

const examples = [
  'Patient-TrustDemoSomsack',
  'Group-TrustDemoHousehold',
  'Immunization-TrustDemoJ3HepB',
  'ServiceRequest-TrustDemoJ2Referral',
  'Provenance-TrustDemoJ3Verification',
  'AuditEvent-TrustDemoJ41Access',
  'ConceptMap-TrustDemoProductToLaoEpi',
];
const from = new URL('../../fsh-generated/resources/', import.meta.url);
const to = new URL('../src/data/ig/', import.meta.url);

// A generated narrative is left out: it is derived from the resource, and the drawer shows the data.
const pretty = (text) => {
  const json = JSON.parse(text);
  if (json.text?.status === 'generated') delete json.text;
  return JSON.stringify(json, null, 2) + '\n';
};

const check = process.argv.includes('--check');
const bad = [];
await mkdir(to, { recursive: true });
for (const n of examples) {
  const src = await readFile(new URL(`${n}.json`, from), 'utf8').catch(() => {
    throw new Error(`fsh-generated/resources/${n}.json is missing: run SUSHI (sushi build .) first`);
  });
  const want = pretty(src);
  const dest = new URL(`${n}.json`, to);
  if (!check) {
    await writeFile(dest, want);
    continue;
  }
  const got = await readFile(dest, 'utf8').catch(() => undefined);
  if (got !== want) bad.push(`web/src/data/ig/${n}.json: ${got === undefined ? 'missing' : 'differs from fsh-generated/resources/'}`);
}
if (bad.length) {
  console.error(`the walkthrough's FHIR examples are not SUSHI's:\n  ${bad.join('\n  ')}\nEdit input/fsh/, then run SUSHI and node web/scripts/ig-examples.mjs.`);
  process.exit(1);
}
console.log(`${examples.length} FHIR examples ${check ? 'match' : 'copied from'} fsh-generated/resources/`);
