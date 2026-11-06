import React, { useState } from 'react';
import { PATIENT_DATA, INITIAL_IMMUNIZATIONS, SUBSEQUENT_LAO_IMMUNIZATIONS, MOCK_FHIR_RESOURCES } from '../../data/storylineData';
import { 
  Building2, 
  ShieldCheck, 
  Lock, 
  Unlock, 
  Activity, 
  AlertCircle, 
  FileCheck2, 
  CheckCircle2, 
  Globe2, 
  RotateCcw, 
  Code2, 
  KeyRound,
  Check,
  XCircle,
  Syringe,
  Sparkles
} from 'lucide-react';

interface S8Props {
  onRestart: () => void;
  onOpenFhirInspector?: () => void;
}

export const S8_ForeignClinicViewer: React.FC<S8Props> = ({ onRestart, onOpenFhirInspector }) => {
  const [passcode, setPasscode] = useState<string>('4829');
  const [isUnlocked, setIsUnlocked] = useState<boolean>(true);
  const [passcodeError, setPasscodeError] = useState<string | null>(null);
  const [attemptsRemaining, setAttemptsRemaining] = useState<number>(3);
  const [showManifestJson, setShowManifestJson] = useState<boolean>(false);
  const [auditPulsing, setAuditPulsing] = useState<boolean>(true);

  const handleVerifyPasscode = (code: string) => {
    if (code === '4829') {
      setIsUnlocked(true);
      setPasscodeError(null);
      setAuditPulsing(true);
    } else {
      setIsUnlocked(false);
      const remaining = Math.max(0, attemptsRemaining - 1);
      setAttemptsRemaining(remaining);
      setPasscodeError(`Invalid Passcode! ${remaining} attempt(s) remaining before link revocation.`);
    }
  };

  const testWrongPasscode = () => {
    setPasscode('0000');
    handleVerifyPasscode('0000');
  };

  const testCorrectPasscode = () => {
    setPasscode('4829');
    handleVerifyPasscode('4829');
  };

  return (
    <div className="flex flex-col h-full bg-clinical-alabaster font-sans">
      {/* 1. Facility Top Bar */}
      <div className="bg-white border-b border-clinical-divider px-6 py-3 flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-amber-50 rounded-lg text-amber-800 border border-amber-200">
            <Building2 className="w-5 h-5" />
          </div>
          <div>
            <h2 className="text-base font-bold text-clinical-ink">
              Thailand Clinic Point-of-Care VHL Viewer (Country A)
            </h2>
            <div className="flex items-center gap-2 text-xs text-clinical-steel mt-0.5">
              <span>Practitioner: <strong>Dr. Anan</strong> &bull; Chiang Rai Primary Care Clinic</span>
              <span>&bull;</span>
              <span className="font-mono text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 font-medium">
                VHL Manifest Verified via GDHCN Trust List
              </span>
            </div>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {isUnlocked ? (
            <button
              onClick={testWrongPasscode}
              className="text-xs font-mono text-slate-600 hover:text-tampered-crimson bg-slate-100 hover:bg-rose-50 px-3 py-1.5 rounded-lg border border-slate-200 transition"
              title="Test simulation of failed passcode entry"
            >
              Simulate Wrong Passcode
            </button>
          ) : (
            <button
              onClick={testCorrectPasscode}
              className="text-xs font-mono text-white bg-emerald-600 hover:bg-emerald-700 px-3 py-1.5 rounded-lg transition"
            >
              Auto-fill Correct Passcode (4829)
            </button>
          )}
        </div>
      </div>

      {/* 2. Top Security & Live Audit Strip */}
      <div className="bg-slate-900 text-white px-6 py-2.5 border-b border-slate-800">
        <div className="flex flex-wrap items-center justify-between gap-3 text-xs">
          {/* PoC Access status */}
          <div className="flex items-center gap-2">
            {isUnlocked ? (
              <span className="flex items-center gap-1.5 text-emerald-400 font-medium font-mono">
                <ShieldCheck className="w-4 h-4 text-emerald-400" />
                <span>Passcode Verified (✓) &bull; Read-Only Zero-Retention Clinical Session</span>
              </span>
            ) : (
              <span className="flex items-center gap-1.5 text-amber-300 font-medium font-mono">
                <Lock className="w-4 h-4 text-amber-400" />
                <span>Passcode Lock Active &bull; Awaiting Clinician Unlock</span>
              </span>
            )}
          </div>

          {/* Cross-border telemetry callback */}
          <div className="flex items-center gap-2 font-mono text-[11px]">
            <span className={`w-2 h-2 rounded-full ${isUnlocked ? 'bg-emerald-400 animate-pulse' : 'bg-slate-500'}`}></span>
            <span className="text-slate-300">
              Live AuditEvent: <strong className="text-emerald-400">Logged at Lao OHS Info Gateway</strong>
            </span>
          </div>
        </div>
      </div>

      {/* 3. Primary Content Area */}
      <div className="flex-1 p-6 overflow-y-auto">
        {!isUnlocked ? (
          /* Locked State View */
          <div className="max-w-md mx-auto my-8 bg-white rounded-2xl border-2 border-slate-200 p-6 shadow-md text-center space-y-4">
            <div className="w-12 h-12 rounded-full bg-amber-100 flex items-center justify-center text-amber-700 mx-auto">
              <KeyRound className="w-6 h-6" />
            </div>

            <div>
              <h3 className="font-bold text-base text-clinical-ink">
                Enter Verbal Passcode to Decrypt IPS
              </h3>
              <p className="text-xs text-clinical-steel mt-1">
                Father (Bounmy Sengmany) must verbally provide the 4-digit code generated in the Lao Family Wallet.
              </p>
            </div>

            <div className="flex justify-center gap-2">
              <input
                type="text"
                maxLength={4}
                value={passcode}
                onChange={(e) => setPasscode(e.target.value)}
                placeholder="4829"
                className="w-36 text-center text-xl font-mono tracking-widest py-2 rounded-xl border-2 border-slate-300 focus:outline-none focus:border-dpi-cobalt font-bold text-slate-900"
              />
            </div>

            {passcodeError && (
              <div className="p-2.5 bg-rose-50 border border-rose-200 rounded-lg text-xs text-tampered-crimson flex items-center justify-center gap-1.5">
                <XCircle className="w-4 h-4 flex-shrink-0" />
                <span>{passcodeError}</span>
              </div>
            )}

            <button
              onClick={() => handleVerifyPasscode(passcode)}
              className="w-full py-2.5 bg-dpi-cobalt hover:bg-dpi-cobalt-dark text-white rounded-xl text-xs font-bold transition shadow-sm"
            >
              Verify Passcode & Fetch IPS Bundle
            </button>
          </div>
        ) : (
          /* Unlocked Rendered International Patient Summary (IPS) */
          <div className="space-y-6 max-w-5xl mx-auto">
            
            {/* Patient Header Card */}
            <div className="bg-white rounded-xl border border-clinical-divider p-4 shadow-sm flex flex-wrap items-center justify-between gap-4">
              <div className="flex items-center gap-3">
                <div className="w-11 h-11 rounded-full bg-sky-100 border border-sky-300 flex items-center justify-center font-bold text-sky-800 text-sm">
                  SS
                </div>
                <div>
                  <div className="flex items-center gap-2">
                    <h3 className="text-base font-bold text-clinical-ink">{PATIENT_DATA.infantName}</h3>
                    <span className="text-xs bg-emerald-50 text-emerald-800 border border-emerald-200 px-2 py-0.5 rounded-full font-medium">
                      12 Months (1st Birthday Visit)
                    </span>
                  </div>
                  <div className="text-xs text-clinical-steel mt-0.5">
                    Guardian Present: <strong>Father Bounmy Sengmany</strong> &bull; Sovereign Home: Lao PDR
                  </div>
                </div>
              </div>

              <div className="text-right text-xs">
                <div className="font-mono text-slate-500">Source FHIR Repository:</div>
                <div className="font-mono font-medium text-slate-800">sovereign-fhir.moh.gov.la</div>
              </div>
            </div>

            {/* Prominent Immunization History Table (IPS Section) */}
            <div className="bg-white rounded-xl border border-clinical-divider p-5 shadow-sm space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="font-bold text-sm text-clinical-ink flex items-center gap-2">
                    <Syringe className="w-4 h-4 text-dpi-cobalt" />
                    <span>International Patient Summary (IPS) — Immunization History</span>
                  </h3>
                  <p className="text-xs text-clinical-steel mt-0.5">
                    Cross-border verified provenance linking Thailand birth doses and Lao national EPI
                  </p>
                </div>
                <span className="text-xs font-mono bg-sky-50 text-sky-800 border border-sky-200 px-2.5 py-1 rounded-full font-bold">
                  6 Verified Immunizations
                </span>
              </div>

              {/* Table */}
              <div className="border border-slate-200 rounded-xl overflow-hidden text-xs">
                <table className="w-full text-left">
                  <thead className="bg-slate-50 border-b border-slate-200 text-slate-500 font-mono text-[10px] uppercase">
                    <tr>
                      <th className="p-3">Vaccine & Target</th>
                      <th className="p-3">Date</th>
                      <th className="p-3">Origin / Provenance Loop</th>
                      <th className="p-3">Coding Hierarchy</th>
                      <th className="p-3 text-right">Trust State</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    
                    {/* Row 1: Hep B Birth Dose (Full-circle highlight) */}
                    <tr className="bg-emerald-50/40">
                      <td className="p-3">
                        <div className="font-bold text-slate-900">Hepatitis B Birth Dose</div>
                        <div className="text-[10px] text-slate-500">Hepatitis B &bull; Lot: TH-4821</div>
                      </td>
                      <td className="p-3 font-mono text-slate-700">{PATIENT_DATA.infantDob}</td>
                      <td className="p-3">
                        <span className="inline-flex items-center gap-1 text-[10px] font-medium text-emerald-900 bg-emerald-100/80 px-2 py-0.5 rounded border border-emerald-200">
                          <Globe2 className="w-3 h-3 text-emerald-700" />
                          <span>Born in Thailand → Verified in Lao PDR</span>
                        </span>
                      </td>
                      <td className="p-3 font-mono text-[10px] text-slate-600">
                        <div>PreQual: vp-hepb-peds</div>
                        <div className="text-emerald-700 font-semibold">Lao: LAO-EPI-HEPB-BD</div>
                      </td>
                      <td className="p-3 text-right">
                        <span className="inline-flex items-center gap-1 font-mono text-[10px] font-bold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded">
                          <Check className="w-3 h-3 text-emerald-600" />
                          <span>primarySource: true</span>
                        </span>
                      </td>
                    </tr>

                    {/* Row 2: BCG Birth Dose (Full-circle highlight) */}
                    <tr className="bg-emerald-50/40">
                      <td className="p-3">
                        <div className="font-bold text-slate-900">BCG Vaccine (Freeze-Dried)</div>
                        <div className="text-[10px] text-slate-500">Tuberculosis &bull; Lot: TH-9012</div>
                      </td>
                      <td className="p-3 font-mono text-slate-700">{PATIENT_DATA.infantDob}</td>
                      <td className="p-3">
                        <span className="inline-flex items-center gap-1 text-[10px] font-medium text-emerald-900 bg-emerald-100/80 px-2 py-0.5 rounded border border-emerald-200">
                          <Globe2 className="w-3 h-3 text-emerald-700" />
                          <span>Born in Thailand → Verified in Lao PDR</span>
                        </span>
                      </td>
                      <td className="p-3 font-mono text-[10px] text-slate-600">
                        <div>PreQual: vp-bcg-freeze</div>
                        <div className="text-emerald-700 font-semibold">Lao: LAO-EPI-BCG-BD</div>
                      </td>
                      <td className="p-3 text-right">
                        <span className="inline-flex items-center gap-1 font-mono text-[10px] font-bold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded">
                          <Check className="w-3 h-3 text-emerald-600" />
                          <span>primarySource: true</span>
                        </span>
                      </td>
                    </tr>

                    {/* Rows 3-6: Domestic Lao doses */}
                    {SUBSEQUENT_LAO_IMMUNIZATIONS.map((dose) => (
                      <tr key={dose.id} className="hover:bg-slate-50/60">
                        <td className="p-3">
                          <div className="font-semibold text-slate-800">{dose.vaccineName}</div>
                          <div className="text-[10px] text-slate-500">{dose.targetDisease} &bull; Lot: {dose.lotNumber}</div>
                        </td>
                        <td className="p-3 font-mono text-slate-700">{dose.dateAdministered}</td>
                        <td className="p-3 text-slate-600 font-medium text-[11px]">
                          Vientiane District Health Center (Lao PDR)
                        </td>
                        <td className="p-3 font-mono text-[10px] text-slate-600">
                          {dose.laoEpiCode}
                        </td>
                        <td className="p-3 text-right">
                          <span className="font-mono text-[10px] text-slate-700 bg-slate-100 px-2 py-0.5 rounded">
                            Verified Lao EPI
                          </span>
                        </td>
                      </tr>
                    ))}

                  </tbody>
                </table>
              </div>
            </div>

            {/* Collapsible Sections: Allergies & Problems */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
              <div className="bg-white rounded-xl border border-clinical-divider p-4 shadow-sm">
                <span className="font-bold text-slate-800 uppercase tracking-wider block mb-1">
                  Allergies & Intolerances (IPS Section)
                </span>
                <p className="text-slate-600">No known drug or vaccine allergies recorded.</p>
              </div>

              <div className="bg-white rounded-xl border border-clinical-divider p-4 shadow-sm">
                <span className="font-bold text-slate-800 uppercase tracking-wider block mb-1">
                  Active Problems & Encounters
                </span>
                <p className="text-slate-600">Healthy 12-Month Pediatric Well-Child Checkup.</p>
              </div>
            </div>

            {/* Raw Manifest Inspection */}
            {showManifestJson && (
              <div className="p-4 bg-slate-950 rounded-xl border border-slate-800 font-mono text-xs text-emerald-400 overflow-x-auto space-y-2">
                <div className="text-slate-400 pb-1 border-b border-slate-800 text-[11px] flex justify-between">
                  <span>Cross-Border AuditEvent JSON (Delivered to Lao Info Gateway)</span>
                  <span className="text-amber-400">Timestamp: 2026-10-28T14:30:15+07:00</span>
                </div>
                <pre>{JSON.stringify(MOCK_FHIR_RESOURCES.auditEvent, null, 2)}</pre>
              </div>
            )}

          </div>
        )}
      </div>

      {/* 4. Footer */}
      <div className="bg-white border-t border-clinical-divider px-6 py-4 flex flex-wrap items-center justify-between gap-3">
        <button
          onClick={() => setShowManifestJson(!showManifestJson)}
          className="flex items-center gap-1.5 text-xs text-slate-600 hover:text-slate-900 px-3 py-2 rounded-lg border border-slate-200 hover:bg-slate-50 transition font-mono"
        >
          <Code2 className="w-3.5 h-3.5" />
          <span>{showManifestJson ? 'Hide Audit Log' : 'Inspect Fetched VHL Manifest & Lao AuditEvent JSON'}</span>
        </button>

        <div className="flex items-center gap-3">
          <button
            onClick={onRestart}
            className="flex items-center gap-2 px-5 py-2.5 bg-slate-900 hover:bg-slate-800 text-white rounded-lg text-xs font-semibold shadow-sm transition"
          >
            <RotateCcw className="w-4 h-4" />
            <span>Complete Walkthrough & Restart (J1)</span>
          </button>
        </div>
      </div>
    </div>
  );
};
