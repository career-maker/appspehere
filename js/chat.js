/* Source Pro assistant — a self-contained FAQ chat widget.
   All answers are taken from appsphereb2b.com content. No backend required. */
(function () {
  var WA = 'https://wa.me/919778452007';
  var KB = [
    { id: 'what', label: 'What is Source Pro?', keys: ['what is', 'source pro', 'b2b2c', 'about', 'explain', 'platform'],
      a: ['Source Pro B2B2C is a mobile-application-based digital commerce ecosystem created to empower India\'s traditional retailers, distributors, manufacturers, and end customers.',
          'It enables B2B2C trade between distributors and retailers, and lets retailers serve their own customers digitally.'],
      links: [['About Source Pro', 'about.html']] },
    { id: 'retailer', label: 'I\'m a retailer', keys: ['retailer', 'kirana', 'shop', 'store', 'shopkeeper', 'digital hypermarket', 'setup', 'fee'],
      a: ['Transform your store into a digital hypermarket — 25,000+ products, zero setup cost, and no technical knowledge required. You keep your shop name, your customers and your margins.',
          'Retailer plan: ₹2,500 + 18% GST monthly fee (as listed on the retailer page).'],
      links: [['Retailer partnership', 'retailer-partnership.html']] },
    { id: 'distributor', label: 'I\'m a distributor', keys: ['distributor', 'distribution', 'territory', 'seat', 'zero stock', 'warehouse', 'investment', 'deposit'],
      a: ['Build a zero-stock digital distribution business across your assigned territory — no warehouse, no inventory risk, and a growing flow of retailer-generated digital orders.',
          'The model plans 4–5 distributors per assembly constituency. You can check seats by state and district.'],
      links: [['Distributor partnership', 'distributor-partnership.html'], ['View distributor seats', 'distributors.html']] },
    { id: 'manufacturer', label: 'I\'m a manufacturer', keys: ['manufacturer', 'brand', 'sku', 'catalogue', 'catalog', 'list products', 'factory'],
      a: ['Get your entire product catalogue in front of every retailer in the region — 24/7, without a ground salesperson, with real-time analytics and zero stock dumping.'],
      links: [['Manufacturer partnership', 'manufacturer-partnership.html']] },
    { id: 'products', label: 'What products are listed?', keys: ['product', 'category', 'categories', 'sell', 'listed', '25,000', '25000'],
      a: ['25,000+ products on one platform. Categories include stationery, groceries, cosmetics, fashion, electronics, baby care, pet care, home care, toys, beverages, and other daily-use products.'],
      links: [] },
    { id: 'diff', label: 'How is it different from e-commerce?', keys: ['different', 'ecommerce', 'e-commerce', 'amazon', 'quick commerce', 'quick-commerce', 'compete'],
      a: ['Most online platforms sell directly to end customers, often bypassing the traditional retailer. Source Pro B2B2C is different. It is built around the existing retail and distribution ecosystem.'],
      links: [] },
    { id: 'app', label: 'Get the app', keys: ['app', 'download', 'android', 'ios', 'iphone', 'play store', 'app store'],
      a: ['The Source Pro B2B app is available on Android and iOS.'],
      links: [['Google Play', 'https://play.google.com/store/apps/details?id=com.graeonai.renaissancetradingcompany'], ['App Store', 'https://apps.apple.com/in/app/source-pro-b2b/id6742049723']] },
    { id: 'contact', label: 'Contact the team', keys: ['contact', 'call', 'phone', 'email', 'address', 'hours', 'talk', 'human', 'whatsapp', 'support'],
      a: ['Monday to Saturday, 9:00 AM – 6:00 PM IST.', 'Phone: +91 97784 52007 · 1800-890-7576', 'Email: info@appsphereb2b.com'],
      links: [['Chat on WhatsApp', WA], ['Contact page', 'contact.html']] }
  ];
  var CHIPS = ['what', 'retailer', 'distributor', 'manufacturer', 'products', 'contact'];

  var root = document.createElement('div');
  root.className = 'chat';
  root.innerHTML =
    '<button class="chat__fab" type="button" aria-expanded="false" aria-controls="chat-panel" aria-label="Open Source Pro assistant">' +
      '<svg class="chat__ico chat__ico--open" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.500l1.500-4.600A8 8 0 1 1 21 12z"/><path d="M8.500 11h.01M12 11h.01M15.500 11h.01"/></svg>' +
      '<svg class="chat__ico chat__ico--close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>' +
      '<span class="chat__dot" aria-hidden="true"></span></button>' +
    '<section class="chat__panel" id="chat-panel" role="dialog" aria-label="Source Pro assistant" hidden>' +
      '<header class="chat__head"><span class="chat__avatar" aria-hidden="true">S</span><div><strong>Source Pro assistant</strong><small>Answers from appsphereb2b.com</small></div></header>' +
      '<div class="chat__log" role="log" aria-live="polite"></div>' +
      '<div class="chat__chips" aria-label="Suggested questions"></div>' +
      '<form class="chat__form"><label class="sr-only" for="chat-in">Type your question</label><input id="chat-in" type="text" autocomplete="off" placeholder="Ask about retailers, distributors…"><button type="submit" aria-label="Send"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button></form>' +
    '</section>';
  document.body.appendChild(root);

  var fab = root.querySelector('.chat__fab'), panel = root.querySelector('.chat__panel'),
      log = root.querySelector('.chat__log'), chips = root.querySelector('.chat__chips'),
      form = root.querySelector('.chat__form'), input = root.querySelector('#chat-in');
  var greeted = false;

  function add(kind, html) {
    var m = document.createElement('div'); m.className = 'chat__msg chat__msg--' + kind; m.innerHTML = html;
    log.appendChild(m); log.scrollTop = log.scrollHeight; return m;
  }
  function esc(t) { var d = document.createElement('div'); d.textContent = t; return d.innerHTML; }
  function answer(entry) {
    var html = entry.a.map(function (p) { return '<p>' + esc(p) + '</p>'; }).join('');
    if (entry.links.length) html += '<p class="chat__links">' + entry.links.map(function (l) {
      var ext = /^https?:/.test(l[1]); return '<a href="' + l[1] + '"' + (ext ? ' target="_blank" rel="noopener"' : '') + '>' + esc(l[0]) + '</a>'; }).join('') + '</p>';
    add('bot', html);
  }
  function fallback() {
    add('bot', '<p>I couldn\'t find that in the Source Pro information I have. The team can help directly:</p><p class="chat__links"><a href="' + WA + '" target="_blank" rel="noopener">Chat on WhatsApp</a><a href="tel:18008907576">Call 1800-890-7576</a></p>');
  }
  function ask(text) {
    add('user', esc(text));
    var q = text.toLowerCase(), best = null, score = 0;
    KB.forEach(function (e) {
      var s = 0; e.keys.forEach(function (k) { if (q.indexOf(k) > -1) s += k.length > 4 ? 2 : 1; });
      if (e.label.toLowerCase() === q) s += 10;
      if (s > score) { score = s; best = e; }
    });
    setTimeout(function () { best ? answer(best) : fallback(); }, 350);
  }
  CHIPS.forEach(function (id) {
    var e = KB.filter(function (k) { return k.id === id; })[0];
    var b = document.createElement('button'); b.type = 'button'; b.textContent = e.label;
    b.addEventListener('click', function () { ask(e.label); });
    chips.appendChild(b);
  });
  form.addEventListener('submit', function (ev) {
    ev.preventDefault(); var v = input.value.trim(); if (!v) return; input.value = ''; ask(v);
  });

  function toggle(open) {
    panel.hidden = !open; root.classList.toggle('is-open', open);
    fab.setAttribute('aria-expanded', String(open));
    fab.setAttribute('aria-label', open ? 'Close Source Pro assistant' : 'Open Source Pro assistant');
    if (open) {
      if (!greeted) { greeted = true; add('bot', '<p>Hi! I\'m the Source Pro assistant. What would you like to know?</p>'); }
      setTimeout(function () { input.focus(); }, 50);
    } else { fab.focus(); }
  }
  fab.addEventListener('click', function () { toggle(panel.hidden); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) toggle(false); });
})();
