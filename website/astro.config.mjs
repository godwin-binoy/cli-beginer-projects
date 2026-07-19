import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  base: '/cli-beginer-projects/',
  vite: {
    plugins: [tailwindcss()],
  },
});
