import React from 'react';
import { DeviceType } from '../../types';
import { Smartphone, Tablet, Monitor, Maximize2, Minimize2, Wifi, Battery, Signal } from 'lucide-react';

interface DeviceFrameProps {
  deviceType: DeviceType;
  title?: string;
  appConfig?: string;
  isFramed?: boolean;
  onToggleFrame?: () => void;
  children: React.ReactNode;
}

export const DeviceFrame: React.FC<DeviceFrameProps> = ({
  deviceType,
  title,
  appConfig,
  isFramed = true,
  onToggleFrame,
  children,
}) => {
  const getDeviceIcon = () => {
    switch (deviceType) {
      case 'MOBILE':
        return <Smartphone className="w-4 h-4 text-slate-500" />;
      case 'TABLET':
        return <Tablet className="w-4 h-4 text-slate-500" />;
      case 'DESKTOP':
      default:
        return <Monitor className="w-4 h-4 text-slate-500" />;
    }
  };

  if (!isFramed) {
    return (
      <div className="w-full bg-clinical-alabaster min-h-screen">
        <div className="bg-white border-b border-clinical-divider px-6 py-2.5 flex items-center justify-between text-xs text-clinical-steel">
          <div className="flex items-center gap-2">
            {getDeviceIcon()}
            <span className="font-semibold text-clinical-ink">{title || 'Simulation Viewport'}</span>
            <span className="bg-slate-100 text-slate-700 px-2 py-0.5 rounded font-mono text-[11px]">
              {appConfig}
            </span>
          </div>
          {onToggleFrame && (
            <button
              onClick={onToggleFrame}
              className="flex items-center gap-1.5 px-2.5 py-1 rounded bg-slate-100 hover:bg-slate-200 text-slate-700 transition"
              title="Switch to framed device mode"
            >
              <Minimize2 className="w-3.5 h-3.5" />
              <span>Show Device Shell</span>
            </button>
          )}
        </div>
        <div className="p-4 md:p-6">{children}</div>
      </div>
    );
  }

  if (deviceType === 'MOBILE') {
    return (
      <div className="flex flex-col items-center justify-center p-4 min-h-[calc(100vh-140px)]">
        {/* Device meta header */}
        <div className="w-[390px] mb-2 flex items-center justify-between text-xs text-clinical-steel px-1">
          <div className="flex items-center gap-1.5">
            <Smartphone className="w-3.5 h-3.5 text-dpi-cobalt" />
            <span className="font-medium text-slate-700">Android 390px</span>
            <span className="text-[11px] font-mono text-slate-400">({appConfig})</span>
          </div>
          {onToggleFrame && (
            <button
              onClick={onToggleFrame}
              className="flex items-center gap-1 text-[11px] text-dpi-cobalt hover:underline"
            >
              <Maximize2 className="w-3 h-3" />
              <span>Expand</span>
            </button>
          )}
        </div>

        {/* Mobile Device Mockup */}
        <div className="w-[390px] h-[812px] bg-white rounded-[44px] shadow-2xl border-[10px] border-slate-800 flex flex-col overflow-hidden relative">
          {/* Hardware notch / speaker */}
          <div className="absolute top-2 left-1/2 -translate-x-1/2 w-32 h-5 bg-slate-800 rounded-b-xl z-50 flex items-center justify-center">
            <div className="w-12 h-1 bg-slate-600 rounded-full"></div>
          </div>

          {/* Android Mobile Status Bar */}
          <div className="w-full h-8 bg-slate-900 text-white flex items-center justify-between px-6 text-[11px] font-medium pt-1 z-40 select-none">
            <span>09:41</span>
            <div className="flex items-center gap-1.5">
              <Signal className="w-3 h-3" />
              <Wifi className="w-3 h-3" />
              <Battery className="w-3 h-3" />
            </div>
          </div>

          {/* Screen Content Scrollable Area */}
          <div className="flex-1 overflow-y-auto bg-clinical-alabaster flex flex-col text-slate-900">
            {children}
          </div>

          {/* Android Navigation Home Bar */}
          <div className="h-4 bg-white flex items-center justify-center z-40">
            <div className="w-28 h-1 bg-slate-300 rounded-full"></div>
          </div>
        </div>
      </div>
    );
  }

  if (deviceType === 'TABLET') {
    return (
      <div className="flex flex-col items-center justify-center p-4 min-h-[calc(100vh-140px)]">
        {/* Device meta header */}
        <div className="w-full max-w-[1024px] mb-2 flex items-center justify-between text-xs text-clinical-steel px-1">
          <div className="flex items-center gap-1.5">
            <Tablet className="w-3.5 h-3.5 text-dpi-cobalt" />
            <span className="font-medium text-slate-700">Tablet / Web 1024px</span>
            <span className="text-[11px] font-mono text-slate-400">({appConfig})</span>
          </div>
          {onToggleFrame && (
            <button
              onClick={onToggleFrame}
              className="flex items-center gap-1 text-[11px] text-dpi-cobalt hover:underline"
            >
              <Maximize2 className="w-3 h-3" />
              <span>Expand</span>
            </button>
          )}
        </div>

        {/* Tablet Bezel */}
        <div className="w-full max-w-[1024px] min-h-[720px] max-h-[880px] bg-white rounded-[24px] shadow-2xl border-[12px] border-slate-800 flex flex-col overflow-hidden relative">
          {/* Tablet Status Bar */}
          <div className="w-full h-7 bg-slate-900 text-white flex items-center justify-between px-6 text-xs font-medium z-40 select-none">
            <div className="flex items-center gap-2">
              <span className="font-semibold text-slate-200">OHS Facility Client</span>
              <span className="text-[10px] text-slate-400 font-mono">v2.4.1</span>
            </div>
            <div className="flex items-center gap-3">
              <span className="text-[11px] font-mono text-slate-300">10:14 AM</span>
              <Wifi className="w-3.5 h-3.5 text-emerald-400" />
              <Battery className="w-3.5 h-3.5 text-slate-200" />
            </div>
          </div>

          {/* Screen Content Scrollable Area */}
          <div className="flex-1 overflow-y-auto bg-clinical-alabaster flex flex-col text-slate-900">
            {children}
          </div>
        </div>
      </div>
    );
  }

  // DESKTOP
  return (
    <div className="w-full max-w-[1440px] mx-auto p-4 md:p-6 min-h-[calc(100vh-140px)]">
      <div className="bg-white rounded-2xl shadow-sm border border-clinical-divider overflow-hidden">
        {/* Browser / Canvas Chrome */}
        <div className="bg-slate-900 text-slate-300 px-4 py-2.5 flex items-center justify-between text-xs border-b border-slate-800">
          <div className="flex items-center gap-3">
            <div className="flex items-center gap-1.5">
              <div className="w-3 h-3 rounded-full bg-rose-500"></div>
              <div className="w-3 h-3 rounded-full bg-amber-500"></div>
              <div className="w-3 h-3 rounded-full bg-emerald-500"></div>
            </div>
            <div className="bg-slate-800 px-3 py-1 rounded text-slate-300 font-mono text-[11px] flex items-center gap-2">
              <span className="text-emerald-400">https://</span>
              <span>vaxlink.who.int/storyboard/master-flow</span>
            </div>
          </div>
          <div className="flex items-center gap-2 text-[11px] text-slate-400">
            <span>Canvas: 1440px Desktop Master View</span>
          </div>
        </div>

        <div className="bg-clinical-alabaster min-h-[700px] overflow-x-auto">
          {children}
        </div>
      </div>
    </div>
  );
};
