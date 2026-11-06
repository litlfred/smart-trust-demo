import React, { useState } from 'react';
import { PATIENT_DATA } from '../../data/storylineData';
import { 
  CheckCircle2, 
  Layers, 
  ArrowRight, 
  Calendar, 
  Clock, 
  ShieldCheck, 
  Code2, 
  AlertCircle, 
  Check, 
  BookmarkCheck,
  Building2
} from 'lucide-react';

interface S5Props {
  onNext: () => void;
  onOpenFhirInspector?: () => void;
}

export const S5_TerminologyAdjudication: React.FC<S5Props> = ({ onNext }) => {
  const [adjudicated, setAdjudicated] = useState<boolean>(true);
  const [appointmentBooked, setAppointmentBooked] = useState<boolean>(true);
  const [showCodingDiff, setShowCodingDiff] = useState<boolean>(false);

  return (
    <div className="flex flex-col h-full bg-clinical-alabaster font-sans">
      {/* 1. Clinical Header */}
      <div className="bg-white border-b border-clinical-divider px-6 py-3 flex flex-wrap items-center justify-between gap-3">
        <div>
          <div className="flex items-center gap-2">
            <h2 className="text-base font-bold text-clinical-ink">
              {PATIENT_DATA.infantName} (4 Weeks Old)
            </h2>
            <span className="text-xs bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono">
              #{PATIENT_DATA.householdId}
            </span>
          </div>
          <div className="flex flex-wrap items-center gap-2 text-xs mt-1">
            <span className="inline-flex items-center gap-1 text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200 font-medium">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
              <span>2 Foreign Doses Cryptographically Verified &bull; Provenance Attached</span>
            </span>
            <span className="inline-flex items-center gap-1 text-slate-600 bg-slate-100 px-2 py-0.5 rounded font-mono text-[11px]">
              AuditEvent Logged at OHS Info Gateway
            </span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={() => setShowCodingDiff(!showCodingDiff)}
            className="flex items-center gap-1.5 text-xs font-mono text-slate-700 bg-slate-100 hover:bg-slate-200 px-3 py-1.5 rounded-lg transition"
          >
            <Code2 className="w-3.5 h-3.5" />
            <span>{showCodingDiff ? 'Hide Coding Array' : 'Inspect Dual Coding Array'}</span>
          </button>
        </div>
      </div>

      {/* 2. Primary Content Area: 2-Column Clinical Workspace */}
      <div className="flex-1 p-6 grid grid-cols-1 lg:grid-cols-12 gap-6 overflow-y-auto">
        
        {/* Left Column (6 cols): 3-Layer Terminology Adjudication */}
        <div className="lg:col-span-6 space-y-4">
          <div className="bg-white rounded-xl border border-clinical-divider p-5 shadow-sm space-y-4">
            <div>
              <h3 className="font-bold text-sm text-clinical-ink flex items-center gap-2">
                <Layers className="w-4 h-4 text-dpi-cobalt" />
                <span>3-Layer Terminology & ConceptMap Adjudication</span>
              </h3>
              <p className="text-xs text-clinical-steel mt-0.5">
                Resolve missing national concept mapping for foreign birth doses
              </p>
            </div>

            {/* 3-Step Chain */}
            <div className="space-y-2.5">
              
              {/* Layer 1 */}
              <div className="p-3 bg-slate-50 rounded-lg border border-slate-200 text-xs space-y-1">
                <div className="flex items-center justify-between text-[11px] font-mono text-slate-500">
                  <span>LAYER 1: CERTIFICATE PRODUCT CODE (ISSUED THAILAND)</span>
                  <span className="text-amber-700 font-semibold">Foreign Source</span>
                </div>
                <div className="font-mono text-slate-900 font-bold">
                  vp-hepb-peds-monovalent
                </div>
                <p className="text-[11px] text-slate-500">
                  Stored exactly as issued in DVCMinPreQual logical model.
                </p>
              </div>

              {/* Arrow */}
              <div className="flex justify-center">
                <ArrowRight className="w-4 h-4 text-slate-400 rotate-90" />
              </div>

              {/* Layer 2 */}
              <div className="p-3 bg-slate-50 rounded-lg border border-slate-200 text-xs space-y-1">
                <div className="flex items-center justify-between text-[11px] font-mono text-slate-500">
                  <span>LAYER 2: DERIVED VACCINE TYPE (WHO SMART IG)</span>
                  <span className="text-sky-700 font-semibold">WHO IG PreQual</span>
                </div>
                <div className="font-medium text-slate-900">
                  Hepatitis B Pediatric Monovalent (WHO PreQual Class)
                </div>
                <p className="text-[11px] text-slate-500">
                  Derived from global WHO Prequalification metadata catalogue.
                </p>
              </div>

              {/* Arrow */}
              <div className="flex justify-center">
                <ArrowRight className="w-4 h-4 text-slate-400 rotate-90" />
              </div>

              {/* Layer 3 */}
              <div className="p-3 bg-amber-50 rounded-lg border border-amber-200 text-xs space-y-1.5">
                <div className="flex items-center justify-between text-[11px] font-mono text-amber-800">
                  <span>LAYER 3: LAO PDR NATIONAL SCHEDULE VALUESET</span>
                  <span className="text-amber-800 font-semibold">ConceptMap Gap</span>
                </div>
                <p className="text-[11px] text-amber-900">
                  No automated ConceptMap match found in Lao national registry for Thai GPO lot TH-4821.
                </p>
              </div>

            </div>

            {/* Clinician Decision Box */}
            <div className="p-4 bg-sky-50 border-2 border-sky-300 rounded-xl space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold text-sky-950 uppercase tracking-wide">
                  Clinician Adjudication & Equivalence Confirmation
                </span>
                {adjudicated && (
                  <span className="text-[10px] bg-emerald-100 text-emerald-900 border border-emerald-300 px-2 py-0.5 rounded font-mono font-bold flex items-center gap-1">
                    <Check className="w-3 h-3 text-emerald-600" />
                    <span>CONFIRMED</span>
                  </span>
                )}
              </div>

              <div className="p-2.5 bg-white rounded-lg border border-sky-200 text-xs space-y-1">
                <div className="text-[11px] text-slate-500 font-mono">Proposed Lao EPI Match:</div>
                <div className="font-bold text-slate-900">
                  Lao EPI: HepB-BD (Birth Dose Monovalent)
                </div>
                <div className="text-[11px] font-mono text-slate-600">
                  Code: LAO-EPI-HEPB-BD
                </div>
              </div>

              <div className="flex items-center justify-between pt-1">
                <button
                  type="button"
                  onClick={() => setAdjudicated(!adjudicated)}
                  className={`w-full py-2 px-3 rounded-lg text-xs font-bold transition flex items-center justify-center gap-2 ${
                    adjudicated
                      ? 'bg-emerald-600 hover:bg-emerald-700 text-white'
                      : 'bg-dpi-cobalt hover:bg-dpi-cobalt-dark text-white'
                  }`}
                >
                  <BookmarkCheck className="w-4 h-4" />
                  <span>
                    {adjudicated
                      ? 'Equivalence Confirmed & Dual-Coding Active'
                      : 'Confirm Equivalence & Add Second Coding'}
                  </span>
                </button>
              </div>
            </div>

            {/* Dual Coding Preview */}
            {showCodingDiff && (
              <div className="p-3 bg-slate-950 rounded-lg text-xs font-mono text-emerald-400 border border-slate-800">
                <div className="text-slate-400 pb-1 border-b border-slate-800 mb-2 text-[11px]">
                  Immunization.vaccineCode.coding[] (Preserved Source + Local Map)
                </div>
                <pre className="text-[11px] overflow-x-auto">{`[
  {
    "system": "http://smart.who.int/immunizations/CodeSystem/PreQual",
    "code": "vp-hepb-peds-monovalent",
    "display": "WHO PreQual Hepatitis B Monovalent"
  },
  {
    "system": "http://moh.gov.la/fhir/CodeSystem/epi-schedule",
    "code": "LAO-EPI-HEPB-BD",
    "display": "Lao EPI: HepB-BD (Birth Dose)"
  }
]`}</pre>
              </div>
            )}

          </div>
        </div>

        {/* Right Column (6 cols): Calculated National Schedule (PlanDefinition) */}
        <div className="lg:col-span-6 space-y-4">
          <div className="bg-white rounded-xl border border-clinical-divider p-5 shadow-sm space-y-4">
            <div>
              <h3 className="font-bold text-sm text-clinical-ink flex items-center gap-2">
                <Calendar className="w-4 h-4 text-dpi-cobalt" />
                <span>Calculated National Schedule (PlanDefinition)</span>
              </h3>
              <p className="text-xs text-clinical-steel mt-0.5">
                Evaluated via FHIRPath against Lao PDR Pediatric Immunization Plan
              </p>
            </div>

            {/* Schedule Table */}
            <div className="border border-slate-200 rounded-lg overflow-hidden text-xs">
              <table className="w-full text-left">
                <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 font-mono text-[10px] uppercase">
                  <tr>
                    <th className="p-2.5">Milestone</th>
                    <th className="p-2.5">Vaccines</th>
                    <th className="p-2.5 text-right">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {/* Birth */}
                  <tr className="bg-emerald-50/50">
                    <td className="p-2.5 font-semibold text-slate-800">Birth (T0)</td>
                    <td className="p-2.5 text-slate-700">BCG + HepB-BD</td>
                    <td className="p-2.5 text-right">
                      <span className="inline-flex items-center gap-1 text-[10px] font-mono text-emerald-800 bg-emerald-100 px-1.5 py-0.5 rounded font-semibold">
                        <Check className="w-3 h-3 text-emerald-600" />
                        <span>Verified</span>
                      </span>
                    </td>
                  </tr>

                  {/* 6 Weeks */}
                  <tr className="bg-sky-50/50">
                    <td className="p-2.5 font-semibold text-slate-800">6 Weeks (T0+2w)</td>
                    <td className="p-2.5 text-slate-700">Penta-1, OPV-1, PCV-1</td>
                    <td className="p-2.5 text-right">
                      <span className="text-[10px] font-mono text-sky-800 bg-sky-100 px-1.5 py-0.5 rounded font-semibold">
                        Due in 2 Wks
                      </span>
                    </td>
                  </tr>

                  {/* 10 Weeks */}
                  <tr>
                    <td className="p-2.5 font-medium text-slate-700">10 Weeks</td>
                    <td className="p-2.5 text-slate-600">Penta-2, OPV-2, PCV-2</td>
                    <td className="p-2.5 text-right text-[10px] text-slate-400 font-mono">
                      Upcoming
                    </td>
                  </tr>

                  {/* 14 Weeks */}
                  <tr>
                    <td className="p-2.5 font-medium text-slate-700">14 Weeks</td>
                    <td className="p-2.5 text-slate-600">Penta-3, OPV-3, PCV-3, IPV-1</td>
                    <td className="p-2.5 text-right text-[10px] text-slate-400 font-mono">
                      Upcoming
                    </td>
                  </tr>

                  {/* 9 Months */}
                  <tr>
                    <td className="p-2.5 font-medium text-slate-700">9 Months</td>
                    <td className="p-2.5 text-slate-600">Measles-Rubella (MR-1), JE</td>
                    <td className="p-2.5 text-right text-[10px] text-slate-400 font-mono">
                      Upcoming
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            {/* Appointment Booking Widget */}
            <div className="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
              <div className="flex items-center justify-between text-xs font-semibold text-clinical-ink">
                <span className="flex items-center gap-1.5">
                  <Clock className="w-3.5 h-3.5 text-dpi-cobalt" />
                  <span>Book Next Routine EPI Appointment</span>
                </span>
                <span className="text-[10px] font-mono bg-sky-100 text-sky-800 px-1.5 py-0.5 rounded">
                  FHIR Task / Appointment
                </span>
              </div>
              <p className="text-xs text-clinical-steel">
                Recommended date: <strong>2 Weeks from today</strong> for Pentavalent-1 & OPV-1 catchup.
              </p>
              <div className="flex items-center gap-2 pt-1">
                <input
                  type="date"
                  defaultValue="2025-11-25"
                  className="text-xs px-2.5 py-1.5 rounded-lg border border-slate-200 font-mono bg-white text-slate-900"
                />
                <button
                  type="button"
                  onClick={() => setAppointmentBooked(true)}
                  className="px-3 py-1.5 bg-white border border-slate-300 hover:bg-slate-50 text-slate-800 rounded-lg text-xs font-semibold"
                >
                  {appointmentBooked ? '✓ Appointment Booked' : 'Confirm Date'}
                </button>
              </div>
            </div>

          </div>
        </div>

      </div>

      {/* 3. Footer / Action Bar */}
      <div className="bg-white border-t border-clinical-divider px-6 py-4 flex flex-wrap items-center justify-between gap-3">
        <div className="text-xs text-clinical-steel">
          Dual coding saved in local OHS FHIR database &bull; Ready to sync to national EPI
        </div>

        <button
          onClick={onNext}
          className="flex items-center gap-2 px-5 py-2.5 bg-dpi-cobalt hover:bg-dpi-cobalt-dark text-white rounded-lg text-xs font-semibold shadow-sm transition"
        >
          <span>Fast-Forward 1 Year & Open Family Wallet (J4.0a)</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};
