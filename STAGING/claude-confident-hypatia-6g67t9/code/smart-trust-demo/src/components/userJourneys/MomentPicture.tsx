import React from 'react';

/** The moment pictures, read from the repository's docs/images/ (the IG's home page shows the same ones). */
const IMAGES = import.meta.glob('../../../../docs/images/moment-*.jpg', { query: '?url', import: 'default', eager: true }) as Record<string, string>;

/** The illustration of each of the four moments: who is there, and what passes between them. */
const PICTURES: Record<string, { file: string; alt: string }> = {
  'born-abroad': {
    file: 'moment-j1-born-abroad',
    alt: 'At Chiang Rai Hospital, Dr Anan holds up two signed QR cards for Khamla and Bounmy, who hold newborn Somsack',
  },
  'found-at-home': {
    file: 'moment-j2-found-at-home',
    alt: 'In a Lao village with no signal, Vilay, the community health worker, scans the paper cards with her phone while Khamla holds Somsack and Bounmy looks on',
  },
  'made-official': {
    file: 'moment-j3-made-official',
    alt: 'At the district health centre, Nurse Chanthasone checks the cards on a tablet: signature verified, on the Lao schedule; Khamla and Bounmy hold Somsack',
  },
  'crossing-back': {
    file: 'moment-j4-crossing-back',
    alt: 'Back in Thailand, Bounmy shares a vaccine-record link from his phone and Dr Anan sees Somsack’s vaccine history; Khamla and toddler Somsack are beside them',
  },
};

export const MomentPicture: React.FC<{ chapterId: string; className?: string }> = ({ chapterId, className = '' }) => {
  const p = PICTURES[chapterId];
  if (!p) return null;
  return (
    <img
      src={IMAGES[`../../../../docs/images/${p.file}.jpg`]}
      alt={p.alt}
      title={p.alt}
      loading="lazy"
      className={`w-full aspect-[818/299] object-cover rounded-xl border border-slate-200 ${className}`}
    />
  );
};
