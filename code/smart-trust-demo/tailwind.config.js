/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        clinical: {
          alabaster: '#F8FAFC',
          surface: '#FFFFFF',
          ink: '#0F172A',
          steel: '#475569',
          divider: '#E2E8F0',
        },
        dpi: {
          cobalt: '#0284C7',
          'cobalt-light': '#E0F2FE',
          'cobalt-dark': '#0369A1',
        },
        verified: {
          emerald: '#15803D',
          'emerald-light': '#DCFCE7',
          'emerald-dark': '#166534',
        },
        unverified: {
          amber: '#B45309',
          'amber-light': '#FEF3C7',
          'amber-dark': '#92400E',
        },
        tampered: {
          crimson: '#B91C1C',
          'crimson-light': '#FEE2E2',
          'crimson-dark': '#991B1B',
        }
      },
      fontFamily: {
        sans: ['Plus Jakarta Sans', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      }
    },
  },
  plugins: [],
}
