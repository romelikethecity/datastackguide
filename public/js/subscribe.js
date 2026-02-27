// Newsletter subscribe handler — all forms with [data-newsletter-form] attribute
// Update this URL after deploying the Cloudflare Worker:
const SUBSCRIBE_URL = 'https://datastackguide-subscribe.rome-workers.workers.dev';

(function () {
  document.querySelectorAll('[data-newsletter-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var input = form.querySelector('input[type="email"]');
      var btn = form.querySelector('button[type="submit"]');
      var msg = form.querySelector('[data-newsletter-msg]');
      var email = (input.value || '').trim();

      if (!email) return;

      var originalText = btn.textContent;
      btn.disabled = true;
      btn.textContent = 'Subscribing...';
      if (msg) msg.textContent = '';

      fetch(SUBSCRIBE_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email }),
      })
        .then(function (res) {
          if (!res.ok) throw new Error('Failed');
          form.innerHTML =
            '<p class="subscribe-success">You\'re in. First issue drops Tuesday.</p>';
        })
        .catch(function () {
          if (msg) {
            msg.textContent = 'Something went wrong. Try again.';
            msg.style.color = '#f87171';
          }
          btn.disabled = false;
          btn.textContent = originalText;
        });
    });
  });
})();
