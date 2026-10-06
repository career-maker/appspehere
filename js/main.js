/* Shared: header behaviour, mobile nav, dropdowns */
(function () {
  var header = document.querySelector('.header');
  var toggle = document.querySelector('.nav__toggle');
  var nav = document.getElementById('site-nav');
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  function onScroll() { if (header) header.classList.toggle('is-scrolled', window.scrollY > 40); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  function setNav(open) {
    nav.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    document.body.style.overflow = open ? 'hidden' : '';
    if (open) header.classList.add('is-scrolled'); else onScroll();
  }
  if (toggle && nav) {
    toggle.addEventListener('click', function () { setNav(!nav.classList.contains('is-open')); });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && nav.classList.contains('is-open')) setNav(false);
    });
  }

  document.querySelectorAll('.has-menu > button').forEach(function (btn) {
    var li = btn.parentElement;
    btn.addEventListener('click', function () {
      var open = !li.classList.contains('is-open');
      li.classList.toggle('is-open', open);
      li.querySelector('.menu').classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', String(open));
    });
  });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (nav && nav.classList.contains('is-open')) { setNav(false); toggle.focus(); }
    document.querySelectorAll('.has-menu.is-open').forEach(function (li) {
      li.classList.remove('is-open');
      li.querySelector('.menu').classList.remove('is-open');
      li.querySelector('button').setAttribute('aria-expanded', 'false');
    });
  });

  /* exclusive accordion: opening one FAQ item closes the others in its list */
  document.querySelectorAll('.faq__list').forEach(function (list) {
    var items = list.querySelectorAll('details');
    items.forEach(function (d) {
      d.addEventListener('toggle', function () {
        if (!d.open) return;
        items.forEach(function (o) { if (o !== d) o.open = false; });
      });
    });
  });

  /* footer: expandable columns on mobile (buttons are inert on desktop via CSS) */
  document.querySelectorAll('.fcol__btn').forEach(function (btn) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', String(open));
      panel.classList.toggle('is-open', open);
    });
  });

  /* legal pages: highlight the section in view; collapse the contents list on phones */
  (function () {
    var links = document.querySelectorAll('.legal__tocbox a');
    if (!links.length || !('IntersectionObserver' in window)) return;
    var box = document.querySelector('.legal__tocbox');
    if (box && window.matchMedia('(max-width: 960px)').matches) box.removeAttribute('open');
    var map = {};
    links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) { a.classList.remove('is-active'); });
        var a = map[e.target.id]; if (a) a.classList.add('is-active');
      });
    }, { rootMargin: '-20% 0px -70% 0px' });
    document.querySelectorAll('.legal__sec').forEach(function (s) { io.observe(s); });
  })();
})();
