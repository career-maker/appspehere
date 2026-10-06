/* Home page: cinematic hero, tear reveal, ecosystem, story, steps, roles, quotes */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasGSAP = typeof window.gsap !== 'undefined' && typeof window.ScrollTrigger !== 'undefined';

  /* ---------- non-GSAP interactions (always on) ---------- */

  // Tear / split reveal
  var tear = document.getElementById('tear');
  var range = tear && tear.querySelector('.tear__range');
  function setSplit(v) {
    tear.style.setProperty('--split', v + '%');
    v = Number(v);
    var capB = tear.querySelector('.tear__cap:not(.tear__cap--after)'), capA = tear.querySelector('.tear__cap--after');
    if (capB) capB.classList.toggle('is-hidden', v < 30);   /* little of the Before photo left: hide its label */
    if (capA) capA.classList.toggle('is-hidden', v > 70);   /* little of the After photo left: hide its label */
  }
  setSplit(50);
  if (range) range.addEventListener('input', function () { setSplit(range.value); });

  // Ecosystem tabs
  var ecoTabs = Array.prototype.slice.call(document.querySelectorAll('.eco-tab'));
  var ecoNodes = Array.prototype.slice.call(document.querySelectorAll('[data-eco-node]'));
  function selectEco(i, focus) {
    ecoTabs.forEach(function (t, k) {
      var on = k === i;
      t.setAttribute('aria-pressed', String(on));
      t.tabIndex = on ? 0 : -1;
      if (on && focus) t.focus();
    });
    ecoNodes.forEach(function (n, k) { n.classList.toggle('is-active', k === i); });
  }
  ecoTabs.forEach(function (t, i) {
    t.addEventListener('click', function () { selectEco(i); });
    t.addEventListener('keydown', function (e) {
      var n = ecoTabs.length;
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') { e.preventDefault(); selectEco((i + 1) % n, true); }
      if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') { e.preventDefault(); selectEco((i - 1 + n) % n, true); }
    });
  });
  ecoNodes.forEach(function (n, i) { n.addEventListener('click', function () { selectEco(i); }); });
  if (reduce) document.querySelectorAll('[data-pkt]').forEach(function (p) { p.remove(); });


  // Ecosystem reveal: tap/click toggles on touch laptops (hover handled in CSS)
  var ecoReveal = document.querySelector('.eco-reveal');
  if (ecoReveal) ecoReveal.addEventListener('click', function (e) {
    if (e.target.closest('.eco-tab')) return;
    if (window.matchMedia('(hover: none) and (min-width: 901px)').matches) ecoReveal.classList.toggle('is-open');
  });

  // How-it-works expanding cards
  var steps = Array.prototype.slice.call(document.querySelectorAll('.step'));
  steps.forEach(function (s) {
    function open() { steps.forEach(function (o) { o.setAttribute('aria-expanded', String(o === s)); }); }
    s.addEventListener('click', open);
    s.addEventListener('mouseenter', function () {
      if (window.matchMedia('(hover:hover) and (min-width:861px)').matches) open();
    });
  });

  // Roles tabs
  var roleTabs = Array.prototype.slice.call(document.querySelectorAll('.role-tab'));
  function selectRole(i, focus) {
    roleTabs.forEach(function (t, k) {
      var on = k === i;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      if (on && focus) t.focus();
    });
    var panel = document.getElementById(roleTabs[i].getAttribute('aria-controls'));
    if (hasGSAP && !reduce) gsap.fromTo(panel, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.5, ease: 'power3.out' });
  }
  roleTabs.forEach(function (t, i) {
    t.addEventListener('click', function () { selectRole(i); });
    t.addEventListener('keydown', function (e) {
      var n = roleTabs.length;
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') { e.preventDefault(); selectRole((i + 1) % n, true); }
      if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') { e.preventDefault(); selectRole((i - 1 + n) % n, true); }
    });
  });

  // Testimonials
  var quotes = Array.prototype.slice.call(document.querySelectorAll('.quote'));
  var dots = Array.prototype.slice.call(document.querySelectorAll('.dots button'));
  var qi = 0, timer = null;
  function showQuote(i) {
    qi = (i + quotes.length) % quotes.length;
    quotes.forEach(function (q, k) { q.classList.toggle('is-active', k === qi); });
    dots.forEach(function (d, k) { d.setAttribute('aria-current', String(k === qi)); });
  }
  function stopQuotes() { if (timer) { clearInterval(timer); timer = null; } }
  document.querySelectorAll('[data-q]').forEach(function (b) {
    b.addEventListener('click', function () { stopQuotes(); showQuote(qi + Number(b.dataset.q)); });
  });
  dots.forEach(function (d, k) { d.addEventListener('click', function () { stopQuotes(); showQuote(k); }); });
  if (!reduce) timer = setInterval(function () { showQuote(qi + 1); }, 9000);
  var qWrap = document.querySelector('.quote-controls');
  if (qWrap) qWrap.addEventListener('focusin', stopQuotes);
  var qBox = document.querySelector('.quotes');
  if (qBox) { qBox.addEventListener('pointerenter', stopQuotes); qBox.addEventListener('focusin', stopQuotes); }

  // Spotlight on link cards
  document.querySelectorAll('.link-card').forEach(function (c) {
    c.addEventListener('pointermove', function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      c.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  /* ---------- hero ---------- */
  var hero = document.getElementById('hero');
  var catImg = hero.querySelector('.catalog__img');

  if (!hasGSAP || reduce) {
    hero.classList.add('is-static');
    hero.querySelector('[data-counter]').textContent = '25,000';
    document.querySelectorAll('.story__step, .story__visual').forEach(function (el) { el.style.transition = 'none'; });
    return;
  }

  gsap.registerPlugin(ScrollTrigger);
  var mm = gsap.matchMedia();

  mm.add({ desktop: '(min-width: 768px)', mobile: '(max-width: 767px)' }, function (ctx) {
    var mobile = ctx.conditions.mobile;
    var q = function (s) { return hero.querySelector(s); };
    var stage = function (n) { return q('[data-stage="' + n + '"]'); };
    var counter = q('[data-counter]'), plus = q('[data-plus]');
    var rail = hero.querySelectorAll('.hero__rail i');
    var eco = q('[data-eco]');
    var state = { n: 0 };

    gsap.set([q('.layer--catalog'), q('.layer--eco')], { opacity: 0 });
    gsap.set(catImg, { scale: 0.7, y: 40, opacity: 0 });
    gsap.set(hero.querySelectorAll('.eco__path'), { strokeDasharray: 1, strokeDashoffset: 1 });
    gsap.set(hero.querySelectorAll('.node'), { opacity: 0, scale: 0.8 });
    [1, 2, 3, 4].forEach(function (n) { gsap.set(stage(n), { autoAlpha: 0, y: 40 }); });

    var tl = gsap.timeline({
      defaults: { ease: 'none' },
      scrollTrigger: {
        trigger: hero, start: 'top top', end: '+=' + (mobile ? 360 : 460) + '%',
        pin: q('.hero__pin'), scrub: 0.6, anticipatePin: 1
      }
    });

    // stage 0 → 1: the store starts to transform
    tl.to(stage(0), { autoAlpha: 0, y: -50, duration: 0.6 }, 0)
      .to(q('.layer--store'), { scale: mobile ? 1.15 : 1.12, duration: 1.2 }, 0)
      .to(stage(1), { autoAlpha: 1, y: 0, duration: 0.5 }, 0.55)
      // stage 1 → 2: digital catalogue, 25,000+
      .to(stage(1), { autoAlpha: 0, y: -40, duration: 0.4 }, 1.5)
      .to(q('.layer--store'), { scale: 0.45, opacity: 0, duration: 0.9 }, 1.5)
      .to(q('.layer--catalog'), { opacity: 1, duration: 0.5 }, 1.7)
      .to(catImg, { scale: 1, y: 0, opacity: 1, duration: 0.8, ease: 'power2.out' }, 1.7)
      .to(state, {
        n: 25000, duration: 0.9, ease: 'power2.out',
        onUpdate: function () { counter.textContent = Math.round(state.n).toLocaleString('en-IN'); }
      }, 1.8)
      .to(plus, { opacity: 1, duration: 0.15 }, 2.65)
      .to(stage(2), { autoAlpha: 1, y: 0, duration: 0.5 }, 1.9)
      // stage 2 → 3: camera pulls back, distributor + retailer connect
      .to(stage(2), { autoAlpha: 0, y: -40, duration: 0.4 }, 3)
      .to(q('.layer--catalog'), { scale: 0.35, opacity: 0, duration: 0.9 }, 3)
      .to(q('.layer--eco'), { opacity: 1, duration: 0.4 }, 3.3)
      .to(hero.querySelectorAll('[data-node="2"], [data-node="3"]'), { opacity: 1, scale: 1, duration: 0.4, stagger: 0.1 }, 3.4)
      .to(stage(3), { autoAlpha: 1, y: 0, duration: 0.5 }, 3.4)
      // stage 3 → 4: the full chain
      .to(stage(3), { autoAlpha: 0, y: -40, duration: 0.4 }, 4.4)
      .to(hero.querySelectorAll('[data-node="1"], [data-node="4"]'), { opacity: 1, scale: 1, duration: 0.4, stagger: 0.15 }, 4.5)
      .to(hero.querySelectorAll('.eco__path[data-p="1"], .eco__path[data-p="3"]'), { strokeDashoffset: 0, duration: 0.6 }, 4.6)
      .add(function () { eco.classList.add('is-live'); }, 5.1)
      .to(stage(4), { autoAlpha: 1, y: 0, duration: 0.5 }, 4.7)
      .to({}, { duration: 0.8 }, 5.2);

    // the p2 path exists in both svgs; make sure both are drawn
    tl.to(hero.querySelectorAll('.eco__path[data-p="2"]'), { strokeDashoffset: 0, duration: 0.6 }, 3.6);

    rail.forEach(function (r, k) {
      tl.to(r, mobile ? { scaleX: 1, duration: 1.3 } : { scaleY: 1, duration: 1.3 }, k * 1.3);
    });

    // cursor parallax (fine pointers only)
    var off = null;
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      var setters = Array.prototype.slice.call(hero.querySelectorAll('.layer[data-depth]')).map(function (l) {
        return {
          d: parseFloat(l.dataset.depth),
          x: gsap.quickTo(l, 'x', { duration: 0.8, ease: 'power3.out' }),
          y: gsap.quickTo(l, 'y', { duration: 0.8, ease: 'power3.out' })
        };
      });
      var move = function (e) {
        var nx = e.clientX / window.innerWidth - 0.5, ny = e.clientY / window.innerHeight - 0.5;
        setters.forEach(function (s) { s.x(-nx * 28 * s.d); s.y(-ny * 18 * s.d); });
      };
      hero.addEventListener('pointermove', move);
      off = function () { hero.removeEventListener('pointermove', move); };
    }
    return function () { if (off) off(); };
  });

  /* ---------- digital hypermarket: dots follow the mobile carousel ---------- */
  (function () {
    var track = document.getElementById('story-steps');
    var dotEls = document.querySelectorAll('.story__dots i');
    if (!track || !dotEls.length) return;
    track.addEventListener('scroll', function () {
      var cards = track.querySelectorAll('.story__step');
      var mid = track.scrollLeft + track.clientWidth / 2, best = 0, d = 1e9;
      cards.forEach(function (c, i) { var dd = Math.abs(c.offsetLeft + c.offsetWidth / 2 - mid - track.offsetLeft); if (dd < d) { d = dd; best = i; } });
      dotEls.forEach(function (el, i) { el.classList.toggle('is-active', i === best); });
    }, { passive: true });
  })();

  /* ---------- sticky story steps ---------- */
  var storySteps = Array.prototype.slice.call(document.querySelectorAll('.story__step'));
  var visuals = Array.prototype.slice.call(document.querySelectorAll('.story__visual'));
  storySteps.forEach(function (s, i) {
    ScrollTrigger.create({
      trigger: s, start: 'top 60%', end: 'bottom 60%',
      onToggle: function (self) {
        if (!self.isActive) return;
        storySteps.forEach(function (o, k) { o.classList.toggle('is-active', k === i); });
        visuals.forEach(function (v, k) { v.classList.toggle('is-active', k === i); });
      }
    });
  });

  /* ---------- tear: sweeps on scroll until the user takes over ---------- */
  if (range) {
    var userTouched = false;
    ['pointerdown', 'keydown'].forEach(function (ev) { range.addEventListener(ev, function () { userTouched = true; }); });
    var sweep = { v: 92 };
    gsap.to(sweep, {
      v: 38, ease: 'none',
      onUpdate: function () { if (!userTouched) { range.value = sweep.v; setSplit(sweep.v); } },
      scrollTrigger: { trigger: tear, start: 'top 75%', end: 'center 40%', scrub: 0.6 }
    });
  }

  /* ---------- before / after wipe ---------- */
  var afterPane = document.querySelector('.ba__pane--after');
  if (afterPane) {
    var vertical = window.matchMedia('(max-width: 760px)').matches;
    gsap.fromTo(afterPane, { clipPath: vertical ? 'inset(100% 0 0 0)' : 'inset(0 0 0 100%)' },
      { clipPath: 'inset(0 0 0 0)', ease: 'none', scrollTrigger: { trigger: '.ba', start: 'top 85%', end: 'top 50%', scrub: 0.5 } });
  }

  /* ---------- reveals ---------- */
  gsap.utils.toArray('[data-reveal]').forEach(function (el) {
    gsap.to(el, { opacity: 1, y: 0, duration: 0.8, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 88%', once: true } });
  });
  gsap.utils.toArray('.zero, .pillars article, .cta__cell, .link-card').forEach(function (el, i) {
    gsap.from(el, { opacity: 0, y: 28, duration: 0.7, ease: 'power3.out', delay: (i % 4) * 0.06, scrollTrigger: { trigger: el, start: 'top 90%', once: true } });
  });
})();
