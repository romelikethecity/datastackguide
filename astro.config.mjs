import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://datastackguide.com',
  output: 'static',
  trailingSlash: 'always',
  integrations: [sitemap({
    serialize(item) {
      item.lastmod = new Date('2026-02-14');
      return item;
    }
  })],
  build: {
    format: 'directory'
  },
  redirects: {
    '/compare/apollo-vs-instantly/': '/compare/instantly-vs-apollo/',
    '/compare/6sense-vs-bombora/': '/compare/bombora-vs-6sense/',
    '/compare/apollo-vs-salesloft/': '/compare/salesloft-vs-apollo/',
    '/compare/instantly-vs-smartlead/': '/compare/smartlead-vs-instantly/',
    '/use-cases/crm-for-startups/': '/best/best-crm-for-startups/',
    '/use-cases/crm-for-enterprise/': '/best/best-crm-for-enterprise/',
    '/pricing/gong-pricing/': '/pricing/gong-engage-pricing/',
    '/pricing/monday-sales-crm-pricing/': '/pricing/monday-sales-pricing/',
  }
});
