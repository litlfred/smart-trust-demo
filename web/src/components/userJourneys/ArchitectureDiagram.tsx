import React from 'react';
import { Globe2, KeyRound, ShieldCheck, ArrowLeftRight } from 'lucide-react';
import { DPI_H_RA, IG, SPEC } from '../../data/links';
import { ExtLink, countryChip } from './shared';

/**
 * The Thai and Lao components of the demo, laid out on the layers of the
 * DPI-H reference architecture's Integrated View (smart-ra, Fig. 3.2), with
 * WHO GDHCN as the foundation both countries build on. Every building-block
 * name links to its element page in the smart-ra ArchiMate model; every
 * component links to its place in the SMART Trust demonstrator IG.
 *
 * The components are not written here: each is a part of a system actor
 * (`meta.parts` in scenarios/actors/: its name, the RA block it plays, what
 * it does and its IG artefact), in the actor's country (`meta.country`), and
 * its journeys are those whose BPMN (processes/content/) has a lane played by
 * one of its system's roles. All three are read at build time. Only where
 * each RA block is drawn, and how, is kept here.
 */

const RA_MODEL = 'https://litlfred.github.io/smart-ra/en/dpi-h-ra/archimate/0.3.0-draft.1';
const ra = (id: string) => `${RA_MODEL}/elements/${id}/`;
const RA_VIEW = `${RA_MODEL}/views/id-b16aba0577295090bd77388f73c61239/`;

/**
 * DPI-H RA elements (smart-ra ArchiMate model 0.3.0-draft.1): their element
 * ids, for the links. A part names its block by the RA's own name.
 */
export const RA = {
  pos: { name: 'Point-of-service & functional applications', id: 'id-c9b5f2ae923b5e38801bd1dbf8b382b9' },
  reusable: { name: 'DPI-H reusable components', id: 'id-08403902fa3e5df4920a1fbe8eddd82f' },
  shared: { name: 'DPI-H shared data layer', id: 'id-00d4ffa565f55eb996137917386ecac1' },
  dpif: { name: 'Foundational DPI (DPI-F)', id: 'id-077b000f20b95c899adb1143f8ee8cd5' },
  providerSystems: { name: 'Provider Systems', id: 'id-270f6a946e9d5feea37702bdb93980ba' },
  chw: { name: 'CHW & Community', id: 'id-3384363f5f8d5ab09a43380f2f8962ba' },
  citizenApps: { name: 'Citizen / Patient Apps', id: 'id-b1c7360ab5595d6ca684259d405c5889' },
  cdss: { name: 'Computable Decision Support Engine', id: 'id-539b04ae45f147258d8253ae5cb87402' },
  terminology: { name: 'Terminology Service', id: 'id-3f41de2b51c24041b08243bf72b140d1' },
  hmis: { name: 'Health Management Information System', id: 'id-d626508a7dc55b1fb11bf34f57f8ddd9' },
  clientRegistry: { name: 'Client Registry for Health', id: 'id-bc813024f32358c98e5512e43cf2c9bc' },
  facilityRegistry: { name: 'Health Facility Registry', id: 'id-4e0767822dcf46409554156a133fbc67' },
  workforceRegistry: { name: 'Health Workforce Registry', id: 'id-350840520ae44f658b6ad3b3762e382e' },
  productRegistry: { name: 'Product Registry', id: 'id-59c26d672a4248e0bb83cf4d26cba10c' },
  lhr: { name: 'Lifelong Health Record', id: 'id-0e6d89398fff4f20994a31b4de58e7d7' },
  trustServices: { name: 'National Trust Services', id: 'id-847e6eea9ee15a39ad97e8861444ce79' },
  mediator: { name: 'DPI-F Information Mediator', id: 'id-3c5d846710034c4595e206e748d65e36' },
  openStandards: { name: 'Open standards', id: 'id-2610e41fcdf258fe80fd948303fe2d74' },
};
export type RaEl = (typeof RA)[keyof typeof RA];

/** The layout: each layer's row, its tone, and the RA blocks drawn in it, in order. */
const LAYOUT: { ra: RaEl; tone: string; blocks: RaEl[] }[] = [
  { ra: RA.pos, tone: 'bg-teal-50 border-teal-200', blocks: [RA.providerSystems, RA.chw, RA.citizenApps] },
  { ra: RA.reusable, tone: 'bg-sky-50 border-sky-200', blocks: [RA.terminology, RA.cdss, RA.hmis] },
  { ra: RA.shared, tone: 'bg-indigo-50 border-indigo-200', blocks: [RA.lhr, RA.productRegistry, RA.clientRegistry, RA.facilityRegistry, RA.workforceRegistry] },
  { ra: RA.dpif, tone: 'bg-violet-50 border-violet-200', blocks: [RA.trustServices, RA.mediator] },
];

type Country = 'Thailand' | 'Lao PDR';
type ActorPart = { id: string; title: string; raBlock: string; description: string; ig?: string };
type Actor = { id: string; title: string; kind: string; roles?: string[]; meta?: { country?: string; parts?: ActorPart[] } };

const ACTORS = Object.values(
  import.meta.glob('../../../../scenarios/actors/*.json', { eager: true, import: 'default' }) as Record<string, Actor>,
).sort((a, b) => a.id.localeCompare(b.id));

/** Each journey code (J1, J4.0, ...) with the roles that play its BPMN lanes. */
const JOURNEY_LANES: { code: string; roles: Set<string> }[] = Object.values(
  import.meta.glob('../../../../processes/content/*.bpmn', { eager: true, query: '?raw', import: 'default' }) as Record<string, string>,
)
  .map((xml) => ({
    code: /<bpmn:process\b[^>]*\sname="(J\d+(?:\.\d+)?)\s/.exec(xml)?.[1] ?? '',
    roles: new Set(Array.from(xml.matchAll(/<bpmn:lane\b[^>]*\spartitionElementRef="([^"]+)"/g), (m) => m[1])),
  }))
  .filter((j) => j.code)
  .sort((a, b) => a.code.localeCompare(b.code, 'en', { numeric: true }));

const journeysOf = (a: Actor) => JOURNEY_LANES.filter((j) => (a.roles ?? []).some((r) => j.roles.has(r))).map((j) => j.code);

/** A part's IG artefact (`StructureDefinition/X`, `ConceptMap/Y`) as its page in the IG. */
const igPage = (ref?: string) => {
  if (!ref) return undefined;
  const [type, id] = ref.split('/');
  return type === 'StructureDefinition' ? IG.profile(id) : IG.example(type, id);
};

export type Comp = { ra: RaEl; name: string; description: string; system: string; stages: string; first: number; href?: string };
export type Layer = { ra: RaEl; tone: string; th: Comp[]; la: Comp[] };

const BLOCK_BY_NAME = new Map(LAYOUT.flatMap((l) => l.blocks).map((b) => [b.name, b]));

const COMPS: (Comp & { country: Country })[] = ACTORS.flatMap((a) =>
  (a.meta?.parts ?? []).map((p) => {
    const block = BLOCK_BY_NAME.get(p.raBlock);
    if (!block) throw new Error(`scenarios/actors/${a.id}.json: part ${p.id} plays ${p.raBlock}, which the architecture view does not draw`);
    const country = a.meta?.country;
    if (country !== 'Thailand' && country !== 'Lao PDR') throw new Error(`scenarios/actors/${a.id}.json: meta.country is ${country}`);
    const js = journeysOf(a);
    const first = js.length ? JOURNEY_LANES.findIndex((j) => j.code === js[0]) : JOURNEY_LANES.length;
    return { ra: block, name: p.title, description: p.description, system: a.title, stages: js.join(', '), first, href: igPage(p.ig), country };
  }),
);

/** A layer's parts in one country: by block, then in the order of the first journey their system takes part in. */
const inLayer = (l: (typeof LAYOUT)[number], country: Country) =>
  l.blocks.flatMap((b) => COMPS.filter((c) => c.ra === b && c.country === country).sort((x, y) => x.first - y.first));

export const LAYERS: Layer[] = LAYOUT.map((l) => ({ ra: l.ra, tone: l.tone, th: inLayer(l, 'Thailand'), la: inLayer(l, 'Lao PDR') }));

const Box: React.FC<{ c: Comp }> = ({ c }) => (
  <div className="rounded-md border border-slate-300 bg-white px-2 py-1.5 shadow-[1px_1px_0_rgba(15,23,42,0.08)]">
    <a href={ra(c.ra.id)} target="_blank" rel="noopener noreferrer" className="block text-[9px] uppercase tracking-wider text-slate-500 font-semibold hover:text-sky-700" title="DPI-H RA element (smart-ra)">
      {c.ra.name}
    </a>
    <div className="text-xs font-semibold leading-snug" title={`${c.system}: ${c.description}`}>
      {c.href ? <ExtLink href={c.href}>{c.name}</ExtLink> : c.name}
    </div>
    <div className="text-[10px] font-mono text-slate-500">{c.stages}</div>
  </div>
);

const Cell: React.FC<{ comps: Comp[]; country: 'Thailand' | 'Lao PDR' }> = ({ comps, country }) => (
  <div className="rounded-lg border border-dashed border-slate-300/80 bg-white/60 p-1.5">
    <div className="md:hidden text-[9px] font-bold text-slate-500 mb-1">{country}</div>
    {comps.length === 0 ? (
      <div className="text-[10px] italic text-slate-400 px-1 py-2">Not needed in this journey</div>
    ) : (
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-1.5">
        {comps.map((c) => (
          <Box key={`${c.system}:${c.name}`} c={c} />
        ))}
      </div>
    )}
  </div>
);

const Flag: React.FC<{ country: 'Thailand' | 'Lao PDR' }> = ({ country }) => (
  <div className="flex items-center gap-2 text-sm font-bold text-slate-900 px-1">
    <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${countryChip(country)}`}>{country === 'Thailand' ? 'TH' : 'LA'}</span>
    {country === 'Thailand' ? 'Thailand (Chiang Rai)' : 'Lao PDR (home)'}
  </div>
);

export const ArchitectureDiagram: React.FC = () => (
  <section className="bg-white rounded-2xl border border-clinical-divider shadow-sm p-4 md:p-5 space-y-3">
    <div className="space-y-1">
      <h3 className="text-base font-bold text-clinical-ink">Architecture: two countries on one trust foundation</h3>
      <p className="text-xs text-clinical-steel max-w-4xl">
        Each country builds its own stack on the layers of the{' '}
        <ExtLink href={RA_VIEW}>DPI-H reference architecture’s Integrated View</ExtLink> (
        <ExtLink href={DPI_H_RA}>DPI-H RA</ExtLink>). Underneath both is WHO GDHCN: the shared trust list that lets a Lao clinic
        believe a Thai certificate, and a Thai clinic believe a Lao link, with no direct connection between the two. Small
        capitals name the RA building block; the component links to its place in the{' '}
        <ExtLink href={IG.site}>IG</ExtLink> (hover for what it does); codes are the journeys its system takes part in.
      </p>
    </div>

    <div className="grid grid-cols-1 md:grid-cols-[150px_1fr_1fr] gap-1.5">
      <div className="hidden md:block" />
      <div className="hidden md:block"><Flag country="Thailand" /></div>
      <div className="hidden md:block"><Flag country="Lao PDR" /></div>

      {LAYERS.map((l) => (
        <React.Fragment key={l.ra.id}>
          <a
            href={ra(l.ra.id)}
            target="_blank"
            rel="noopener noreferrer"
            className={`rounded-lg border ${l.tone} px-2.5 py-2 text-[11px] font-bold text-slate-700 leading-tight hover:underline md:mt-0 mt-2`}
          >
            {l.ra.name}
          </a>
          <div className={`rounded-lg border ${l.tone} p-1`}>
            <Cell comps={l.th} country="Thailand" />
          </div>
          <div className={`rounded-lg border ${l.tone} p-1`}>
            <Cell comps={l.la} country="Lao PDR" />
          </div>
        </React.Fragment>
      ))}

      {/* Cross-cutting interoperability: the open standards both sides speak */}
      <a
        href={ra(RA.openStandards.id)}
        target="_blank"
        rel="noopener noreferrer"
        className="rounded-lg border bg-slate-50 border-slate-200 px-2.5 py-2 text-[11px] font-bold text-slate-700 leading-tight hover:underline mt-2 md:mt-0"
      >
        Interoperability (cross-cutting): open standards
      </a>
      <div className="md:col-span-2 rounded-lg border bg-slate-50 border-slate-200 px-3 py-2 text-xs text-slate-700 flex flex-wrap gap-x-4 gap-y-1">
        <ExtLink href={SPEC.fhir}>HL7 FHIR</ExtLink>
        <ExtLink href={SPEC.smartImm}>WHO SMART Immunizations</ExtLink>
        <ExtLink href={SPEC.hcertQr}>HCERT (DVC)</ExtLink>
        <ExtLink href={SPEC.vhl}>IHE VHL</ExtLink>
        <ExtLink href={SPEC.ips}>IPS</ExtLink>
        <ExtLink href={SPEC.sdc}>SDC</ExtLink>
        <ExtLink href={SPEC.pcf}>IHE PCF</ExtLink>
        <ExtLink href={SPEC.balp}>IHE BALP</ExtLink>
      </div>

      {/* The foundation */}
      <div className="md:col-span-3 mt-1 rounded-xl border-2 border-amber-300 bg-gradient-to-r from-amber-50 via-amber-100 to-amber-50 p-3">
        <div className="flex flex-wrap items-center gap-x-3 gap-y-1">
          <Globe2 className="w-6 h-6 text-amber-600" />
          <div className="text-sm font-bold text-slate-900">
            Foundation: <ExtLink href={SPEC.gdhcn}>WHO Global Digital Health Certification Network (GDHCN)</ExtLink>
          </div>
          <span className="text-[11px] text-slate-600">
            the trust list of participants’ public keys (<ExtLink href={SPEC.trust}>SMART Trust</ExtLink>)
          </span>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-2 mt-2 text-[11px] text-slate-700">
          <div className="flex gap-1.5"><KeyRound className="w-3.5 h-3.5 text-amber-600 flex-shrink-0 mt-0.5" /> Thailand publishes the key it signs certificates with.</div>
          <div className="flex gap-1.5"><ShieldCheck className="w-3.5 h-3.5 text-amber-600 flex-shrink-0 mt-0.5" /> Lao PDR caches the list, so its clinics verify Thai cards offline; Thailand does the same for Lao VHLs.</div>
          <div className="flex gap-1.5"><ArrowLeftRight className="w-3.5 h-3.5 text-amber-600 flex-shrink-0 mt-0.5" /> <span>Data crosses only as a signed QR the family carries, or a VHL the family shares; never system to system.</span></div>
        </div>
      </div>
    </div>
  </section>
);
