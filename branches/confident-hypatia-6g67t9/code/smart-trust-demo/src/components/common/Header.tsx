import React from 'react';
import { ActiveTab, ScreenId } from '../../types';
import { JOURNEY_STAGES } from '../../data/storylineData';
import { Smartphone, RotateCcw, Globe2, ChevronRight, Eye, Route, BookOpen, Github } from 'lucide-react';
import { IG } from '../../data/links';
import { screenHref, viewHref } from '../../routes';

interface HeaderProps {
  activeTab: ActiveTab;
  setActiveTab: (tab: ActiveTab) => void;
  currentScreenId: ScreenId;
  setCurrentScreenId: (id: ScreenId) => void;
  onResetSimulation: () => void;
  isPresenterMode: boolean;
  setIsPresenterMode: (val: boolean) => void;
}

export const Header: React.FC<HeaderProps> = ({
  activeTab,
  setActiveTab,
  currentScreenId,
  setCurrentScreenId,
  onResetSimulation,
  isPresenterMode,
  setIsPresenterMode,
}) => {
  return (
    <header className="md:sticky md:top-0 z-50 bg-white border-b border-clinical-divider shadow-sm">
      {/* Top Banner: Context & Trust Strip */}
      <div className="bg-slate-900 text-slate-300 text-xs px-4 md:px-8 py-1.5 flex flex-wrap items-center justify-between gap-2 border-b border-slate-800">
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-1.5 text-sky-400 font-semibold tracking-wide">
            <Globe2 className="w-3.5 h-3.5" />
            <span>WHO Pre-GDHF Vignette</span>
          </div>
          <span className="text-slate-600">|</span>
          <span className="text-slate-300">Cross-Border Digital Immunization Portability</span>
          <span className="hidden sm:inline bg-slate-800 text-slate-300 px-2 py-0.5 rounded text-[10px] font-mono">
            J1 → J4.1 (Thailand ⇄ Lao PDR)
          </span>
        </div>

        <div className="flex items-center gap-4 text-[11px]">
          <div className="hidden md:flex items-center gap-2">
            <span className="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span className="font-mono text-emerald-300">GDHCN DEV Trust List: XXR Active</span>
          </div>
          <button
            onClick={() => setIsPresenterMode(!isPresenterMode)}
            className={`flex items-center gap-1.5 px-2.5 py-0.5 rounded transition ${
              isPresenterMode
                ? 'bg-sky-500/20 text-sky-300 border border-sky-400/30'
                : 'text-slate-400 hover:text-slate-200'
            }`}
            title="Toggle Presenter Notes & Guidelines"
          >
            <Eye className="w-3 h-3" />
            <span>{isPresenterMode ? 'Presenter Mode: ON' : 'Presenter Notes'}</span>
          </button>
        </div>
      </div>

      {/* Main App Navigation Bar */}
      <div className="px-4 md:px-8 py-3 flex flex-col md:flex-row md:items-center justify-between gap-3">
        {/* Brand & Narrative Meta */}
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-sky-600 to-indigo-600 flex items-center justify-center text-white font-bold shadow-md shadow-sky-600/20">
            V
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-lg font-bold text-clinical-ink tracking-tight">VaxLink</h1>
              <span className="text-xs bg-sky-100 text-sky-800 font-semibold px-2 py-0.5 rounded-full">
                Interactive Spec
              </span>
            </div>
            <p className="text-xs text-clinical-steel">
              Open Health Stack (OHS) &bull; WHO GDHCN &bull; Verifiable Health Links (VHL)
            </p>
          </div>
        </div>

        {/* Mode switcher: the journey (story + technical layer) or the live device demo */}
        <div className="flex items-center bg-slate-100 p-1 rounded-xl text-xs font-medium text-slate-600 overflow-x-auto">
          <a
            href={viewHref('overview')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg transition whitespace-nowrap ${
              activeTab === 'journeys'
                ? 'bg-white text-clinical-ink shadow-sm font-semibold'
                : 'hover:text-clinical-ink'
            }`}
          >
            <Route className="w-3.5 h-3.5 text-rose-500" />
            <span>Journeys</span>
          </a>

          <a
            href={screenHref(currentScreenId)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg transition whitespace-nowrap ${
              activeTab === 'screens'
                ? 'bg-white text-clinical-ink shadow-sm font-semibold'
                : 'hover:text-clinical-ink'
            }`}
          >
            <Smartphone className="w-3.5 h-3.5 text-sky-600" />
            <span>Device Demo</span>
          </a>
        </div>

        {/* The FHIR IG this demo illustrates, and global reset */}
        <div className="flex flex-wrap items-center gap-2">
          <a
            href={IG.site}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1.5 text-xs text-sky-800 px-2.5 py-1.5 rounded-lg border border-sky-200 bg-sky-50 hover:bg-sky-100 transition"
            title="The FHIR implementation guide this demo illustrates"
          >
            <BookOpen className="w-3.5 h-3.5" />
            <span>FHIR IG</span>
          </a>
          <a
            href={IG.repo}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1.5 text-xs text-clinical-steel hover:text-slate-900 px-2.5 py-1.5 rounded-lg border border-slate-200 hover:bg-slate-50 transition"
            title="Source of the IG on GitHub"
          >
            <Github className="w-3.5 h-3.5" />
            <span>IG source</span>
          </a>
          <button
            onClick={onResetSimulation}
            className="flex items-center gap-1.5 text-xs text-clinical-steel hover:text-slate-900 px-2.5 py-1.5 rounded-lg border border-slate-200 hover:bg-slate-50 transition"
            title="Reset form entries & cryptographic simulations"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span className="hidden lg:inline">Reset Simulation</span>
          </button>
        </div>
      </div>

      {/* Screen / Stage Navigation Scrubber (Active when on Screens tab) */}
      {activeTab === 'screens' && (
        <div className="bg-slate-50 border-t border-clinical-divider px-4 md:px-8 py-2">
          <div className="flex flex-wrap items-center gap-1.5">
            <span className="text-[11px] font-semibold text-clinical-steel uppercase tracking-wider mr-2">
              Journey Stage:
            </span>
            {JOURNEY_STAGES.map((stage, idx) => {
              const isActive = currentScreenId === stage.screenId;
              return (
                <React.Fragment key={stage.screenId}>
                  {idx > 0 && <ChevronRight className="w-3 h-3 text-slate-300 flex-shrink-0" />}
                  <a
                    href={screenHref(stage.screenId)}
                    aria-current={isActive ? 'step' : undefined}
                    className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs transition ${
                      isActive
                        ? 'bg-sky-600 text-white font-semibold shadow-sm'
                        : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100 hover:text-slate-900'
                    }`}
                  >
                    <span className="font-mono text-[10px] opacity-80">{stage.stageCode}</span>
                    <span className="hidden sm:inline">{stage.title}</span>
                  </a>
                </React.Fragment>
              );
            })}
          </div>
        </div>
      )}
    </header>
  );
};
