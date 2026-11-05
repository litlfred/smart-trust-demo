import React, { useEffect, useState } from 'react';
import QRCode from 'qrcode';
import { ShieldCheck, Copy, Check } from 'lucide-react';

interface QrCodeViewProps {
  value: string;
  size?: number;
  label?: string;
  badge?: string;
  badgeVariant?: 'verified' | 'unverified' | 'info';
  caption?: string;
  showPayloadCopy?: boolean;
}

export const QrCodeView: React.FC<QrCodeViewProps> = ({
  value,
  size = 180,
  label,
  badge = "GDHCN DEV: XXR",
  badgeVariant = "info",
  caption,
  showPayloadCopy = true,
}) => {
  const [dataUrl, setDataUrl] = useState<string>('');
  const [copied, setCopied] = useState<boolean>(false);

  useEffect(() => {
    QRCode.toDataURL(value, {
      errorCorrectionLevel: 'M',
      margin: 2,
      width: size * 2, // crisp resolution
      color: {
        dark: '#0F172A',
        light: '#FFFFFF',
      },
    })
      .then((url) => setDataUrl(url))
      .catch((err) => console.error('Error generating QR code', err));
  }, [value, size]);

  const handleCopy = () => {
    navigator.clipboard.writeText(value);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const getBadgeStyle = () => {
    switch (badgeVariant) {
      case 'verified':
        return 'bg-emerald-50 text-emerald-800 border-emerald-200';
      case 'unverified':
        return 'bg-amber-50 text-amber-800 border-amber-200';
      case 'info':
      default:
        return 'bg-sky-50 text-sky-800 border-sky-200';
    }
  };

  return (
    <div className="flex flex-col items-center p-4 bg-white rounded-xl border border-clinical-divider shadow-sm">
      {label && (
        <span className="text-xs font-semibold text-clinical-steel uppercase tracking-wider mb-2">
          {label}
        </span>
      )}

      {/* 16px Quiet Zone container as per DESIGN.md */}
      <div className="p-3 bg-white border border-slate-100 rounded-lg shadow-inner mb-3">
        {dataUrl ? (
          <img
            src={dataUrl}
            alt="Vaccine QR Matrix"
            style={{ width: `${size}px`, height: `${size}px` }}
            className="block"
          />
        ) : (
          <div
            style={{ width: `${size}px`, height: `${size}px` }}
            className="flex items-center justify-center bg-slate-50 text-xs text-slate-400 font-mono"
          >
            Generating QR...
          </div>
        )}
      </div>

      {badge && (
        <div
          className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-mono border font-medium mb-2 ${getBadgeStyle()}`}
        >
          <ShieldCheck className="w-3.5 h-3.5" />
          <span>{badge}</span>
        </div>
      )}

      {caption && (
        <p className="text-xs text-center text-clinical-steel max-w-[240px] leading-tight mb-2">
          {caption}
        </p>
      )}

      {showPayloadCopy && (
        <button
          onClick={handleCopy}
          className="inline-flex items-center gap-1 text-[11px] font-mono text-clinical-steel hover:text-dpi-cobalt transition-colors py-1 px-2 rounded hover:bg-slate-50 border border-transparent hover:border-slate-200"
          title="Click to copy raw QR payload string"
        >
          {copied ? (
            <>
              <Check className="w-3 h-3 text-emerald-600" />
              <span className="text-emerald-700 font-medium">Copied Payload</span>
            </>
          ) : (
            <>
              <Copy className="w-3 h-3" />
              <span>Copy Raw Payload ({value.substring(0, 10)}...)</span>
            </>
          )}
        </button>
      )}
    </div>
  );
};
