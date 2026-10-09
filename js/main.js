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

/* custom dropdowns: replace native <select> UI, keep the native element as the source of truth */
(function () {
  function enhance(sel) {
    if (sel.dataset.cs || sel.multiple) return;
    sel.dataset.cs = '1';
    var wrap = document.createElement('div'); wrap.className = 'cs';
    sel.parentNode.insertBefore(wrap, sel); wrap.appendChild(sel);
    sel.tabIndex = -1; sel.setAttribute('aria-hidden', 'true');
    var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'cs__btn';
    btn.setAttribute('aria-haspopup', 'listbox'); btn.setAttribute('aria-expanded', 'false');
    var lab = sel.id && document.querySelector('label[for="' + sel.id + '"]');
    if (lab) { if (!lab.id) lab.id = sel.id + '-label'; btn.setAttribute('aria-labelledby', lab.id); }
    var list = document.createElement('ul'); list.className = 'cs__list'; list.setAttribute('role', 'listbox');
    wrap.appendChild(btn); wrap.appendChild(list);
    var active = -1;
    function build() {
      list.innerHTML = '';
      Array.prototype.forEach.call(sel.options, function (o, i) {
        var li = document.createElement('li'); li.setAttribute('role', 'option'); li.dataset.i = i; li.textContent = o.textContent;
        if (o.disabled) li.setAttribute('aria-disabled', 'true');
        li.setAttribute('aria-selected', String(i === sel.selectedIndex));
        list.appendChild(li);
      });
      sync();
    }
    function sync() {
      var o = sel.options[sel.selectedIndex];
      btn.textContent = o ? o.textContent : '';
      btn.classList.toggle('is-placeholder', !sel.value);
      btn.disabled = sel.disabled;
      Array.prototype.forEach.call(list.children, function (li, i) { li.setAttribute('aria-selected', String(i === sel.selectedIndex)); });
    }
    function setActive(i) {
      var items = list.children; if (!items.length) return;
      i = Math.max(0, Math.min(items.length - 1, i));
      if (items[active]) items[active].classList.remove('is-active');
      active = i; items[i].classList.add('is-active'); items[i].scrollIntoView({ block: 'nearest' });
    }
    function open() { if (btn.disabled) return; wrap.classList.add('is-open'); btn.setAttribute('aria-expanded', 'true'); setActive(sel.selectedIndex < 0 ? 0 : sel.selectedIndex); }
    function close() { wrap.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); }
    function pick(i) {
      if (sel.options[i] && !sel.options[i].disabled) {
        sel.selectedIndex = i; sel.dispatchEvent(new Event('input', { bubbles: true })); sel.dispatchEvent(new Event('change', { bubbles: true }));
      }
      sync(); close(); btn.focus();
    }
    btn.addEventListener('click', function () { wrap.classList.contains('is-open') ? close() : open(); });
    list.addEventListener('click', function (e) { var li = e.target.closest('li'); if (li) pick(+li.dataset.i); });
    btn.addEventListener('keydown', function (e) {
      var isOpen = wrap.classList.contains('is-open');
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); if (!isOpen) open(); else setActive(active + (e.key === 'ArrowDown' ? 1 : -1)); }
      else if ((e.key === 'Enter' || e.key === ' ') && isOpen) { e.preventDefault(); pick(active); }
      else if (e.key === 'Escape' && isOpen) { e.preventDefault(); e.stopPropagation(); close(); }
      else if (e.key === 'Tab') close();
      else if (e.key.length === 1 && /\S/.test(e.key)) {
        var k = e.key.toLowerCase(), n = sel.options.length;
        for (var j = 1; j <= n; j++) { var idx = ((isOpen ? active : sel.selectedIndex) + j) % n; if (sel.options[idx].textContent.trim().toLowerCase().indexOf(k) === 0) { isOpen ? setActive(idx) : pick(idx); break; } }
      }
    });
    document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) close(); });
    sel.addEventListener('change', sync);
    new MutationObserver(build).observe(sel, { childList: true, subtree: true });
    new MutationObserver(sync).observe(sel, { attributes: true, attributeFilter: ['disabled'] });
    build();
  }
  document.querySelectorAll('select').forEach(enhance);
})();

/* close mega menus when clicking elsewhere */
document.addEventListener('click', function (e) {
  document.querySelectorAll('.has-menu.is-open').forEach(function (li) {
    if (li.contains(e.target)) return;
    li.classList.remove('is-open'); li.querySelector('.menu').classList.remove('is-open');
    li.querySelector('button').setAttribute('aria-expanded', 'false');
  });
});
