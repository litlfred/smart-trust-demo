/**
 * Where to read more. The journey is documented as a WHO SMART Guidelines L2
 * DAK and L3 FHIR implementation guide in litlfred/smart-trust-demo; the
 * standards are linked lightly, one click from the moment that uses them.
 */

/**
 * The demonstrator's own site. The walkthrough is published inside it, at
 * vaxlink/ (STAGING/<branch>/vaxlink/ for a branch), and routes in the URL
 * hash, so the page is always one level below the site's root: a relative
 * link reaches the pages built from the same commit.
 */
const SITE = '../';

export const IG = {
  site: SITE,
  repo: 'https://github.com/litlfred/smart-trust-demo',
  journeys: `${SITE}journeys.html`,
  personas: `${SITE}personas.html`,
  processes: `${SITE}business-processes.html`,
  examples: `${SITE}vaxlink-examples.html`,
  /** The page of one IG example, e.g. igExample('ConceptMap', 'TrustDemoProductToLaoEpi'). */
  profile: (id: string) => `${SITE}artifact/StructureDefinition-${id}.html`,
  profiles: `${SITE}vaxlink-examples.html#country-profiles`,
  example: (type: string, id: string) => `${SITE}artifact/${type}-${id}.html`,
};

/** The WHO draft architecture whose DPI-H building blocks the architecture view uses. */
export const DPI_H_RA = 'https://litlfred.github.io/smart-ra/en/dpi-h-ra/index.html';

export const SPEC = {
  fhir: 'https://hl7.org/fhir/',
  fhirR4: 'https://hl7.org/fhir/R4/',
  conceptMap: 'https://hl7.org/fhir/conceptmap.html',
  valueSet: 'https://hl7.org/fhir/valueset.html',
  planDefinition: 'https://hl7.org/fhir/plandefinition.html',
  cql: 'https://cql.hl7.org/',
  provenance: 'https://hl7.org/fhir/provenance.html',
  questionnaire: 'https://hl7.org/fhir/questionnaire.html',
  group: 'https://hl7.org/fhir/group.html',
  immunization: 'https://hl7.org/fhir/immunization.html',
  serviceRequest: 'https://hl7.org/fhir/servicerequest.html',
  consent: 'https://hl7.org/fhir/consent.html',
  auditEvent: 'https://hl7.org/fhir/auditevent.html',
  sdc: 'https://hl7.org/fhir/uv/sdc/',
  ips: 'https://hl7.org/fhir/uv/ips/',
  smartImm: 'https://smart.who.int/immunizations/',
  trust: 'https://smart.who.int/trust/',
  hcertQr: 'https://smart.who.int/trust/hcert_spec.html#422-qr-2d-barcode',
  gdhcn: 'https://www.who.int/initiatives/global-digital-health-certification-network',
  vhl: 'https://profiles.ihe.net/ITI/VHL/',
  pcf: 'https://profiles.ihe.net/ITI/PCF/',
  balp: 'https://profiles.ihe.net/ITI/BALP/',
  ohsSdk: 'https://github.com/google/android-fhir',
  ohsGateway: 'https://github.com/google/fhir-gateway',
  ohsPipes: 'https://github.com/google/fhir-data-pipes',
};

type Bpmn = { file: string; title: string; igAnchor: string; scenarioAnchor: string };

/** The IG's business process (BPMN) for each moment, drawn as SVG in processes/content/. */
export const BPMN_FOR_STAGE: Record<string, Bpmn> = {
  J1: { file: 'j1-birth-dose-dvc', title: 'J1 Issue the newborn’s birth-dose DVCs', igAnchor: 'j1-issue-the-newborns-birth-dose-dvcs-in-country-a', scenarioAnchor: 'j1--born-abroad-thailand-birth-day' },
  J2a: { file: 'j2-chw-discovery-referral', title: 'J2 Discover and refer an unregistered infant', igAnchor: 'j2-discover-and-refer-an-unregistered-infant-in-country-b', scenarioAnchor: 'j2--found-at-home-lao-pdr-3-weeks-later' },
  J2b: { file: 'j2-chw-discovery-referral', title: 'J2 Discover and refer an unregistered infant', igAnchor: 'j2-discover-and-refer-an-unregistered-infant-in-country-b', scenarioAnchor: 'j2--found-at-home-lao-pdr-3-weeks-later' },
  J3a: { file: 'j3-clinic-verification-schedule', title: 'J3 Verify, import and schedule at the home clinic', igAnchor: 'j3-verify-import-and-schedule-at-the-home-clinic', scenarioAnchor: 'j3--made-official-vientiane-district-health-center-4-weeks-later' },
  J3b: { file: 'j3-clinic-verification-schedule', title: 'J3 Verify, import and schedule at the home clinic', igAnchor: 'j3-verify-import-and-schedule-at-the-home-clinic', scenarioAnchor: 'j3--made-official-vientiane-district-health-center-4-weeks-later' },
  'J4.0a': { file: 'j4-0-family-vhl-issuance', title: 'J4.0 Issue the family’s records to one phone as VHLs', igAnchor: 'j40-issue-the-familys-records-to-one-phone-as-vhls', scenarioAnchor: 'j40--crossing-back-one-family-one-phone-lao-pdr-12-months-later' },
  'J4.0b': { file: 'j4-0-family-vhl-issuance', title: 'J4.0 Issue the family’s records to one phone as VHLs', igAnchor: 'j40-issue-the-familys-records-to-one-phone-as-vhls', scenarioAnchor: 'j40--crossing-back-one-family-one-phone-lao-pdr-12-months-later' },
  'J4.1': { file: 'j4-1-vhl-point-of-care', title: 'J4.1 Read a family member’s records at the point of care', igAnchor: 'j41-read-a-family-members-records-at-the-point-of-care-abroad', scenarioAnchor: 'j41--crossing-back-a-thai-doctor-sees-the-full-history-chiang-rai-12-months-later' },
};

export const BPMN_PROCESSES = Array.from(
  new Map(Object.entries(BPMN_FOR_STAGE).map(([stage, p]) => [p.file, { ...p, stages: [] as string[] }])).values(),
).map((p) => ({ ...p, stages: Object.entries(BPMN_FOR_STAGE).filter(([, q]) => q.file === p.file).map(([s]) => s) }));

/** Where each process lives in the IG: its section, the process viewer, the scenario and the BPMN source. */
export const bpmnLinks = (p: Bpmn) => ({
  ig: `${IG.processes}#${p.igAnchor}`,
  viewer: `${IG.site}cat-harness/processes/${p.file}.html`,
  scenario: `${IG.journeys}#${p.scenarioAnchor}`,
  source: `${IG.repo}/blob/main/processes/content/${p.file}.bpmn`,
});

/**
 * The BPMN drawings, read from the repository's processes/content/ at build
 * time (the harness renders them there from the .bpmn), so the walkthrough
 * always shows the processes of its own commit.
 */
const BPMN_SVG = import.meta.glob('../../../processes/content/*.svg', { query: '?url', import: 'default', eager: true }) as Record<string, string>;
export const bpmnSvg = (file: string) => {
  const url = BPMN_SVG[`../../../processes/content/${file}.svg`];
  if (!url) throw new Error(`no BPMN drawing processes/content/${file}.svg`);
  return url;
};

/**
 * The demonstrator's ArchiMate views: its journeys and systems as an overlay on
 * the DPI-H RA's own ArchiMate model (`archimate/`), drawn as SVG by the
 * site build (cat-harness's archimate subgraph, at archimate/0.1.0/views/ of
 * the published site). They are shown from there, not copied: every box links
 * to its element page, relative to the drawing.
 */
const ARCHIMATE_MODEL = `${IG.site}en/smart-trust-demo/archimate/0.1.0/`;
export type ArchimateView = { file: string; slug: string; id: string; label: string; title: string; bpmn?: string };
export const ARCHIMATE = {
  page: `${IG.site}architecture.html`,
  model: ARCHIMATE_MODEL,
  views: [
    { file: 'systems', slug: 'smart-trust-demo-on-the-dpi-h-integrated-view', id: 'id-249a1002c32e50199e27a502ef0ec3d8', label: 'Systems', title: 'Thai and Lao systems on the DPI-H Integrated View' },
    { file: 'journeys', slug: 'smart-trust-demo-journeys-use-cases', id: 'id-c6cae81c85da5fc197ab58547274a481', label: 'Journeys', title: 'Journeys (use cases), people and RA capabilities' },
    { file: 'j1', slug: 'j1-on-the-dpi-h-ra', id: 'id-18d2033f445f5b8895f20719cb97bd91', label: 'J1', title: 'J1 on the DPI-H RA', bpmn: 'j1-birth-dose-dvc' },
    { file: 'j2', slug: 'j2-on-the-dpi-h-ra', id: 'id-099b088dc52f57289c647bfb64e8c4d6', label: 'J2', title: 'J2 on the DPI-H RA', bpmn: 'j2-chw-discovery-referral' },
    { file: 'j3', slug: 'j3-on-the-dpi-h-ra', id: 'id-c1154579a67d5815921b72f71587df50', label: 'J3', title: 'J3 on the DPI-H RA', bpmn: 'j3-clinic-verification-schedule' },
    { file: 'j4-0', slug: 'j4-0-on-the-dpi-h-ra', id: 'id-ae1502fd9fb158c3bcb643bf39006d41', label: 'J4.0', title: 'J4.0 on the DPI-H RA', bpmn: 'j4-0-family-vhl-issuance' },
    { file: 'j4-1', slug: 'j4-1-on-the-dpi-h-ra', id: 'id-42b408eba96159c187c0612ce7c2c6cf', label: 'J4.1', title: 'J4.1 on the DPI-H RA', bpmn: 'j4-1-vhl-point-of-care' },
  ] as ArchimateView[],
  /** The view's page on the demonstrator's site, addressed by name. */
  viewPage: (v: ArchimateView) => `${ARCHIMATE_MODEL}views/${v.slug}/`,
  /** The view's drawing, as the site build draws it. */
  svg: (v: ArchimateView) => `${SITE}archimate/0.1.0/views/${v.id}.svg`,
  /** The journey view for a BPMN process, if there is one. */
  forBpmn: (file: string) => ARCHIMATE.views.find((v) => v.bpmn === file),
};
