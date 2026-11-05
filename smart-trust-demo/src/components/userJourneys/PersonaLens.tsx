import React from 'react';
import { Play, Target, Heart, AlertTriangle } from 'lucide-react';
import { JOURNEY_STEPS, PERSONAS, PERSONA_BY_ID, PersonaId, CHAPTERS } from '../../data/journeyData';
import { EmotionBadge, PersonaAvatar, emotionLabel } from './shared';

interface Props {
  personaId: PersonaId;
  onSelectPersona: (id: PersonaId) => void;
  onPresentStep: (index: number) => void;
}

/** SVG line chart of a persona's emotion across all journey steps. */
const EmotionCurve: React.FC<{ personaId: PersonaId; onPresentStep: (i: number) => void }> = ({ personaId, onPresentStep }) => {
  const persona = PERSONA_BY_ID[personaId];
  const W = 880;
  const H = 200;
  const padX = 40;
  const padTop = 20;
  const padBottom = 44;
  const n = JOURNEY_STEPS.length;
  const x = (i: number) => padX + (i * (W - padX * 2)) / (n - 1);
  const y = (e: number) => padTop + ((2 - e) * (H - padTop - padBottom)) / 4;

  const points = JOURNEY_STEPS.map((s, i) => ({ i, m: s.moments[personaId] })).filter((p) => p.m);

  // Solid segments between consecutive steps; dashed when the persona is absent in between.
  const segments = points.slice(1).map((p, k) => {
    const prev = points[k];
    return { from: prev, to: p, gap: p.i - prev.i > 1 };
  });

  return (
    <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto" role="img" aria-label={`${persona.name}'s emotional journey`}>
      {/* Chapter bands */}
      {CHAPTERS.map((ch, ci) => {
        const idxs = JOURNEY_STEPS.map((s, i) => (s.chapterId === ch.id ? i : -1)).filter((i) => i >= 0);
        const x0 = idxs[0] === 0 ? 0 : (x(idxs[0]) + x(idxs[0] - 1)) / 2;
        const last = idxs[idxs.length - 1];
        const x1 = last === n - 1 ? W : (x(last) + x(last + 1)) / 2;
        return (
          <g key={ch.id}>
            <rect x={x0} y={0} width={x1 - x0} height={H - padBottom + 8} fill={ci % 2 ? '#f8fafc' : '#ffffff'} />
            <text x={(x0 + x1) / 2} y={H - 6} textAnchor="middle" fontSize="11" fill="#64748b" fontWeight={600}>
              {ch.number}. {ch.title}
            </text>
          </g>
        );
      })}

      {/* Gridlines */}
      {[2, 1, 0, -1, -2].map((e) => (
        <g key={e}>
          <line x1={padX - 10} x2={W - padX + 10} y1={y(e)} y2={y(e)} stroke={e === 0 ? '#cbd5e1' : '#eef2f7'} strokeDasharray={e === 0 ? '4 4' : undefined} />
          <text x={4} y={y(e) + 3} fontSize="9" fill="#94a3b8">
            {e === 2 ? '😀' : e === 0 ? '😐' : e === -2 ? '☹️' : ''}
          </text>
        </g>
      ))}

      {/* Step ticks */}
      {JOURNEY_STEPS.map((s, i) => (
        <text key={s.stageCode} x={x(i)} y={H - padBottom + 22} textAnchor="middle" fontSize="9" fill="#94a3b8" fontFamily="monospace">
          {s.stageCode}
        </text>
      ))}

      {segments.map((seg, k) => (
        <line
          key={k}
          x1={x(seg.from.i)}
          y1={y(seg.from.m!.emotion)}
          x2={x(seg.to.i)}
          y2={y(seg.to.m!.emotion)}
          stroke={persona.color.hex}
          strokeWidth={3}
          strokeLinecap="round"
          strokeDasharray={seg.gap ? '6 6' : undefined}
          opacity={seg.gap ? 0.5 : 1}
        />
      ))}

      {points.map((p) => (
        <g key={p.i} className="cursor-pointer" onClick={() => onPresentStep(p.i)}>
          <circle cx={x(p.i)} cy={y(p.m!.emotion)} r={9} fill="#fff" stroke={persona.color.hex} strokeWidth={3} />
          <title>
            {JOURNEY_STEPS[p.i].stageCode}: {emotionLabel(p.m!.emotion)} — {p.m!.feeling}
          </title>
        </g>
      ))}
    </svg>
  );
};

export const PersonaLens: React.FC<Props> = ({ personaId, onSelectPersona, onPresentStep }) => {
  const persona = PERSONA_BY_ID[personaId];
  const touchpoints = JOURNEY_STEPS.map((s, i) => ({ s, i, m: s.moments[personaId] })).filter((t) => t.m);

  return (
    <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
      {/* Persona picker */}
      <aside className="lg:col-span-3 space-y-2">
        <h3 className="text-xs font-bold text-slate-700 uppercase tracking-wider px-1">Whose journey?</h3>
        {PERSONAS.map((p) => {
          const active = p.id === personaId;
          return (
            <button
              key={p.id}
              onClick={() => onSelectPersona(p.id)}
              className={`w-full flex items-center gap-3 text-left p-3 rounded-xl border transition ${
                active ? `${p.color.soft} ${p.color.border} shadow-sm` : 'bg-white border-slate-200 hover:bg-slate-50'
              }`}
            >
              <PersonaAvatar persona={p} />
              <div className="min-w-0">
                <div className="text-sm font-bold text-slate-900">{p.name}</div>
                <div className={`text-[11px] ${active ? p.color.text : 'text-slate-500'}`}>{p.role}</div>
              </div>
            </button>
          );
        })}
      </aside>

      <div className="lg:col-span-9 space-y-5">
        {/* Profile */}
        <section className={`rounded-2xl border ${persona.color.border} ${persona.color.soft} p-5`}>
          <div className="flex items-start gap-4">
            <PersonaAvatar persona={persona} size="lg" />
            <div className="flex-1 min-w-0">
              <div className="flex flex-wrap items-baseline gap-2">
                <h3 className="text-xl font-bold text-slate-900">{persona.name}</h3>
                <span className={`text-xs font-semibold ${persona.color.text}`}>
                  {persona.role} · {persona.country}
                </span>
              </div>
              <p className="text-sm text-slate-800 mt-1 flex items-start gap-1.5">
                <Target className="w-4 h-4 mt-0.5 flex-shrink-0 text-slate-500" />
                <span>
                  <strong>Goal:</strong> {persona.goal}
                </span>
              </p>
            </div>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-4 text-xs">
            <div className="bg-white/70 rounded-xl p-3 border border-white">
              <div className="font-bold text-slate-800 flex items-center gap-1.5 mb-1.5">
                <Heart className="w-3.5 h-3.5 text-emerald-600" /> Needs
              </div>
              <ul className="space-y-1 text-slate-700">
                {persona.needs.map((n) => (
                  <li key={n}>• {n}</li>
                ))}
              </ul>
            </div>
            <div className="bg-white/70 rounded-xl p-3 border border-white">
              <div className="font-bold text-slate-800 flex items-center gap-1.5 mb-1.5">
                <AlertTriangle className="w-3.5 h-3.5 text-rose-500" /> Frustrations
              </div>
              <ul className="space-y-1 text-slate-700">
                {persona.frustrations.map((n) => (
                  <li key={n}>• {n}</li>
                ))}
              </ul>
            </div>
          </div>
        </section>

        {/* Emotion curve */}
        <section className="bg-white rounded-2xl border border-clinical-divider p-5 shadow-sm space-y-2">
          <div className="flex items-center justify-between">
            <h4 className="text-xs font-bold text-slate-700 uppercase tracking-wider">How {persona.name} feels along the way</h4>
            <span className="text-[10px] text-slate-400">Dashed line = not present in between · click a point to present it</span>
          </div>
          <EmotionCurve personaId={personaId} onPresentStep={onPresentStep} />
        </section>

        {/* Touchpoints */}
        <section className="space-y-2">
          <h4 className="text-xs font-bold text-slate-700 uppercase tracking-wider px-1">
            {persona.name}’s touchpoints ({touchpoints.length})
          </h4>
          <ol className="relative border-l-2 border-slate-200 ml-3 space-y-3">
            {touchpoints.map(({ s, i, m }) => (
              <li key={s.stageCode} className="ml-5">
                <span className={`absolute -left-[7px] mt-4 w-3 h-3 rounded-full ${persona.color.dot} ring-4 ring-white`} />
                <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-sm flex flex-col md:flex-row gap-3 md:items-start">
                  <div className="flex-1 min-w-0 space-y-1">
                    <div className="flex flex-wrap items-center gap-2 text-[11px] text-slate-500">
                      <span className="font-mono font-bold text-slate-700">{s.stageCode}</span>
                      <span>{s.when}</span>
                      <span>·</span>
                      <span>{s.where}</span>
                      {s.lead === personaId && (
                        <span className={`text-[9px] font-bold uppercase px-1.5 py-0.5 rounded ${persona.color.soft} ${persona.color.text}`}>Leads this step</span>
                      )}
                    </div>
                    <div className="text-sm font-bold text-slate-900">{s.title}</div>
                    <p className="text-xs text-slate-700">{m!.doing}</p>
                    <p className="text-xs italic text-slate-500">{m!.feeling}</p>
                    <div className="text-[10px] text-slate-400">Touchpoint: {s.touchpoint}</div>
                  </div>
                  <div className="flex md:flex-col items-center md:items-end gap-2">
                    <EmotionBadge emotion={m!.emotion} />
                    <button
                      onClick={() => onPresentStep(i)}
                      className="inline-flex items-center gap-1 text-[11px] font-semibold text-sky-700 hover:underline"
                    >
                      <Play className="w-3 h-3" /> Present
                    </button>
                  </div>
                </div>
              </li>
            ))}
          </ol>
        </section>
      </div>
    </div>
  );
};
