// Cloudflare Worker — Resend newsletter subscribe endpoint
//
// Secrets (set via wrangler secret put):
//   RESEND_API_KEY
//   RESEND_AUDIENCE_ID

const ALLOWED_ORIGINS = [
  'https://datastackguide.com',
  'http://localhost:4321',
  'http://localhost:3000',
];

function corsHeaders(request) {
  const origin = request.headers.get('Origin') || '';
  const allowed = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    'Access-Control-Allow-Origin': allowed,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  };
}

function json(request, data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...corsHeaders(request), 'Content-Type': 'application/json' },
  });
}

export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders(request) });
    }

    if (request.method !== 'POST') {
      return json(request, { error: 'Method not allowed' }, 405);
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return json(request, { error: 'Invalid JSON' }, 400);
    }

    const email = (body.email || '').trim().toLowerCase();
    if (!email || !email.includes('@')) {
      return json(request, { error: 'Valid email required' }, 400);
    }

    try {
      const res = await fetch(
        `https://api.resend.com/audiences/${env.RESEND_AUDIENCE_ID}/contacts`,
        {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${env.RESEND_API_KEY}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email, unsubscribed: false }),
        }
      );

      if (!res.ok) {
        const err = await res.text();
        console.error('Resend error:', res.status, err);
        return json(request, { error: 'Subscription failed' }, 502);
      }

      return json(request, { success: true });
    } catch (err) {
      console.error('Worker error:', err);
      return json(request, { error: 'Internal error' }, 500);
    }
  },
};
