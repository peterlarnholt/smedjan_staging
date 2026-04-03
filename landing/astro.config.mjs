import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://peterlarnholt.github.io',
  base: '/smedjan/',
  integrations: [tailwind()],
});
