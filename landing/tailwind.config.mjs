/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        brand: {
          purple: '#8b5cf6',
          light: '#a78bfa',
          dark: '#7c3aed',
        },
        surface: {
          black: '#0a0a0a',
          card: '#111111',
          subtle: '#1a1a1a',
        },
        text: {
          primary: '#e0e0e0',
          secondary: '#a0a0a0',
          muted: '#707070',
        },
        border: {
          default: '#2a2a2a',
          divider: '#1f1f1f',
        },
      },
      fontFamily: {
        heading: ['Exo', 'sans-serif'],
        body: ['Exo', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      boxShadow: {
        glow: '0 0 20px rgba(139, 92, 246, 0.3)',
        'glow-lg': '0 0 40px rgba(139, 92, 246, 0.4)',
      },
    },
  },
  plugins: [],
};
