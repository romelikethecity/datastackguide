import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://datastackguide.com',
  output: 'static',
  trailingSlash: 'always',
  integrations: [sitemap({
    filter(page) {
      // Exclude redirect source pages from sitemap
      const redirectSources = [
        '/compare/apollo-vs-instantly/',
        '/compare/6sense-vs-bombora/',
        '/compare/apollo-vs-salesloft/',
        '/compare/instantly-vs-smartlead/',
        '/use-cases/crm-for-startups/',
        '/use-cases/crm-for-enterprise/',
        '/pricing/gong-pricing/',
        '/pricing/monday-sales-crm-pricing/',
        '/best/best-data-cleaning-tools/',
        '/best/best-review-buyer-intent-platforms/',
        '/compare/airbyte-vs-stitch/',
        '/compare/demandtools-vs-ringlead/',
        '/integrations/salesforce-gong/',
      ];
      const path = page.replace('https://datastackguide.com', '');
      return !redirectSources.includes(path);
    },
    serialize(item) {
      item.lastmod = new Date('2026-02-23');
      const url = item.url;

      // Set priority based on page type
      if (url === 'https://datastackguide.com/') {
        item.priority = 1.0;
        item.changefreq = 'weekly';
      } else if (url.includes('/tools/') && !url.endsWith('/tools/')) {
        item.priority = 0.9;
        item.changefreq = 'monthly';
      } else if (url.includes('/reports/')) {
        item.priority = 0.8;
        item.changefreq = 'monthly';
      } else if (url.includes('/compare/') || url.includes('/best/') || url.includes('/alternatives/')) {
        item.priority = 0.7;
        item.changefreq = 'monthly';
      } else if (url.includes('/pricing/') || url.includes('/integrations/') || url.includes('/guides/')) {
        item.priority = 0.6;
        item.changefreq = 'monthly';
      } else if (url.includes('/glossary/') || url.includes('/categories/') || url.includes('/use-cases/')) {
        item.priority = 0.5;
        item.changefreq = 'monthly';
      } else {
        item.priority = 0.4;
        item.changefreq = 'monthly';
      }
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
    '/best/best-data-cleaning-tools/': '/best/best-data-quality-tools/',
    '/best/best-review-buyer-intent-platforms/': '/best/best-b2b-intent-data-tools/',
    '/compare/airbyte-vs-stitch/': '/compare/airbyte-vs-fivetran/',
    '/compare/demandtools-vs-ringlead/': '/compare/demandtools-vs-clay/',
    '/integrations/salesforce-gong/': '/tools/gong-engage/',
  }
});
