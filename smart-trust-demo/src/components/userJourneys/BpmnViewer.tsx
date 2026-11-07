import React, { useEffect, useRef, useState } from 'react';
import { Maximize2, X } from 'lucide-react';
import { BPMN_PROCESSES, bpmnLinks, bpmnSvg } from '../../data/links';

/**
 * The BPMN sources, read from the repository's processes/content/ at build
 * time, for the steps each drawing holds: every activity of each process,
 * by its id and name.
 */
const BPMN_XML = import.meta.glob('../../../../processes/content/*.bpmn', { eager: true, query: '?raw', import: 'default' }) as Record<string, string>;
const STEP = /<bpmn:(?:task|userTask|serviceTask|manualTask|scriptTask|sendTask|receiveTask|businessRuleTask|callActivity|subProcess)\b([^>]*)>/g;
const stepsOf = (file: string) =>
  Array.from((BPMN_XML[`../../../../processes/content/${file}.bpmn`] ?? '').matchAll(STEP), (m) => ({
    id: /\sid="([^"]+)"/.exec(m[1])?.[1],
    name: /\sname="([^"]*)"/.exec(m[1])?.[1],
  })).filter((s): s is { id: string; name: string } => !!s.id && !!s.name);

const SVG_NS = 'http://www.w3.org/2000/svg';
// bpmn-js draws an invisible hit area over each shape, which would cover the titles.
const LINK_STYLE = '.djs-hit,.djs-outline{pointer-events:none!important}.vx-step-link{cursor:pointer}.vx-step-link text{text-decoration:underline}.vx-step-link:focus-visible{outline:2px solid #2563eb;outline-offset:2px}';

/**
 * The drawing with each step's TITLE (its label, not the whole box) linked to
 * where the journeys viewer links it: the process's section of the IG's
 * business-processes page. Undefined when the drawing has no step to link.
 */
function linkedSvg(text: string, file: string): SVGSVGElement | undefined {
  const proc = BPMN_PROCESSES.find((p) => p.file === file);
  if (!proc) return undefined;
  const href = bpmnLinks(proc).ig;
  const svg = new DOMParser().parseFromString(text, 'image/svg+xml').querySelector('svg');
  if (!svg) return undefined;
  let n = 0;
  for (const s of stepsOf(file)) {
    const label = svg.querySelector(`g.djs-element[data-element-id="${CSS.escape(s.id)}"] text.djs-label`);
    if (!label) continue;
    const a = document.createElementNS(SVG_NS, 'a');
    a.setAttribute('class', 'vx-step-link');
    a.setAttribute('href', href);
    a.setAttribute('target', '_blank');
    a.setAttribute('rel', 'noopener noreferrer');
    const name = s.name.replace(/&#10;|\s+/g, ' ').replace(/&amp;/g, '&').replace(/&#x27;|&apos;/g, "'").replace(/&quot;/g, '"').trim();
    a.setAttribute('aria-label', `${name}: the process in the IG`);
    const tip = document.createElementNS(SVG_NS, 'title');
    tip.textContent = `${name}: the process in the IG`;
    a.appendChild(tip);
    label.replaceWith(a);
    a.appendChild(label);
    n++;
  }
  if (n === 0) return undefined;
  const style = document.createElementNS(SVG_NS, 'style');
  style.textContent = LINK_STYLE;
  svg.insertBefore(style, svg.firstChild);
  return document.importNode(svg, true);
}

/** Each BPMN drawing's width at 100% (its SVG viewBox), so a zoom level is a real size. */
const NATURAL_WIDTH: Record<string, number> = {
  'j1-birth-dose-dvc': 1580,
  'j2-chw-discovery-referral': 1580,
  'j3-clinic-verification-schedule': 1755,
  'j4-0-family-vhl-issuance': 1755,
  'j4-1-vhl-point-of-care': 1930,
};

type Zoom = 'fit' | 1 | 1.5 | 2;
const ZOOMS: { z: Zoom; label: string }[] = [
  { z: 'fit', label: 'Fit' },
  { z: 1, label: '100%' },
  { z: 1.5, label: '150%' },
  { z: 2, label: '200%' },
];

const ZoomBar: React.FC<{ zoom: Zoom; setZoom: (z: Zoom) => void; children?: React.ReactNode }> = ({ zoom, setZoom, children }) => (
  <div className="flex flex-wrap items-center gap-1.5" role="group" aria-label="Diagram size">
    {ZOOMS.map(({ z, label }) => (
      <button
        key={label}
        type="button"
        aria-pressed={zoom === z}
        onClick={() => setZoom(z)}
        className={`text-xs font-semibold px-3 py-1.5 min-h-[36px] min-w-[52px] rounded-lg border ${
          zoom === z ? 'bg-slate-900 text-white border-slate-900' : 'bg-white text-slate-700 border-slate-300 hover:bg-slate-50'
        }`}
      >
        {label}
      </button>
    ))}
    {children}
  </div>
);

/**
 * The drawing, inline so that its step titles are links (an <img> is inert);
 * the plain picture stands in until it is fetched, or if it cannot be.
 */
const Drawing: React.FC<{ file: string; title: string; zoom: Zoom }> = ({ file, title, zoom }) => {
  const w = NATURAL_WIDTH[file] ?? 1600;
  const width = zoom === 'fit' ? '100%' : `${w * zoom}px`;
  const host = useRef<HTMLDivElement>(null);
  const [linked, setLinked] = useState(false);
  useEffect(() => {
    let live = true;
    setLinked(false);
    host.current?.replaceChildren();
    fetch(bpmnSvg(file))
      .then((r) => (r.ok ? r.text() : Promise.reject(new Error(`HTTP ${r.status}`))))
      .then((text) => {
        const svg = live && host.current ? linkedSvg(text, file) : undefined;
        if (!svg || !host.current) return;
        svg.setAttribute('role', 'img');
        svg.setAttribute('aria-label', `BPMN diagram: ${title}`);
        host.current.replaceChildren(svg);
        setLinked(true);
      })
      .catch(() => undefined);
    return () => {
      live = false;
    };
  }, [file, title]);
  useEffect(() => {
    const svg = host.current?.querySelector('svg');
    if (svg) Object.assign(svg.style, { width, maxWidth: 'none', height: 'auto', display: 'block' });
  }, [width, linked]);
  return (
    <>
      <div ref={host} />
      {!linked && <img src={bpmnSvg(file)} alt={`BPMN diagram: ${title}`} loading="lazy" className="max-w-none h-auto block" style={{ width }} />}
    </>
  );
};

/**
 * A BPMN drawing a room can read: at actual size by default, scrolling inside
 * its frame, with tap-sized zoom buttons and a full-screen view.
 */
export const BpmnViewer: React.FC<{ file: string; title: string }> = ({ file, title }) => {
  const [zoom, setZoom] = useState<Zoom>(1);
  const [full, setFull] = useState(false);
  return (
    <div className="space-y-2">
      <ZoomBar zoom={zoom} setZoom={setZoom}>
        <FullScreenButton onClick={() => setFull(true)} />
      </ZoomBar>
      <div className="overflow-auto max-h-[80vh] rounded-lg bg-white border border-slate-100">
        <Drawing file={file} title={title} zoom={zoom} />
      </div>
      {full && <BpmnFullScreen file={file} title={title} onClose={() => setFull(false)} />}
    </div>
  );
};

export const FullScreenButton: React.FC<{ onClick: () => void }> = ({ onClick }) => (
  <button
    type="button"
    onClick={onClick}
    className="inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 min-h-[36px] rounded-lg border border-slate-300 bg-white text-slate-700 hover:bg-slate-50"
  >
    <Maximize2 className="w-3.5 h-3.5" /> Full screen
  </button>
);

/** The drawing over the whole page; Esc or the close button returns. */
export const BpmnFullScreen: React.FC<{ file: string; title: string; onClose: () => void }> = ({ file, title, onClose }) => {
  const [zoom, setZoom] = useState<Zoom>('fit');
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && onClose();
    window.addEventListener('keydown', onKey);
    const overflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      window.removeEventListener('keydown', onKey);
      document.body.style.overflow = overflow;
    };
  }, [onClose]);
  return (
    <div role="dialog" aria-modal="true" aria-label={`BPMN diagram: ${title}`} className="fixed inset-0 z-[1000] bg-white flex flex-col">
      <div className="flex flex-wrap items-center gap-3 px-4 py-3 border-b border-slate-200">
        <span className="text-sm font-bold text-slate-900 flex-1 min-w-0">{title}</span>
        <ZoomBar zoom={zoom} setZoom={setZoom} />
        <button
          type="button"
          onClick={onClose}
          aria-label="Close"
          className="inline-flex items-center gap-1.5 text-sm font-semibold px-3 py-1.5 min-h-[40px] rounded-lg bg-slate-900 text-white"
        >
          <X className="w-4 h-4" /> Close
        </button>
      </div>
      <div className="flex-1 overflow-auto p-4">
        <Drawing file={file} title={title} zoom={zoom} />
      </div>
    </div>
  );
};
