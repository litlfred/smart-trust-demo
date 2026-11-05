import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// The walkthrough is published inside the demonstrator's own site, at
// vaxlink/ (main) or STAGING/<branch>/vaxlink/ (a branch): scripts/publish.sh
// passes the base for a branch in VAXLINK_BASE. It reads the BPMN drawings,
// the actors and the moment pictures from the repository itself (../processes,
// ../scenarios, ../docs/images), so the dev server may serve those too.
export default defineConfig({
  plugins: [react()],
  base: process.env.VAXLINK_BASE ?? '/smart-trust-demo/vaxlink/',
  server: {
    host: '0.0.0.0',
    port: 5173,
    strictPort: true,
    fs: { allow: ['.', '../processes/content', '../scenarios/actors', '../docs/images'] },
  },
  preview: {
    host: '0.0.0.0',
    port: 5173,
  },
})
