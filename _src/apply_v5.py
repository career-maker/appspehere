"""v5: remove hero grid; clear before/after; problem + app redesigns from the supplied mockups."""
import os
import re

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
rd = lambda p: open(p, encoding="utf8").read()
s = rd("_src/index.src.html")


def section(sid):
    i = s.index('id="%s"' % sid)
    a = s.rindex("<section", 0, i)
    b = s.index("</section>", i) + len("</section>")
    return a, b


# ---- hero grid off ----
s = s.replace('    <div class="hero__grid"></div>\n', "")

# ---- problem ----
a, b = section("problem")
problem = '''<section class="section problem-section" id="problem" aria-labelledby="problem-h">
  <div class="container problem">
    <div class="problem__text">
      <p class="eyebrow">The problem</p>
      <h2 id="problem-h" class="problem__h" data-reveal>The market has changed — but the <mark>traditional trade system</mark> has not changed fast enough.</h2>
      <p class="problem__p">The pandemic exposed that traditional retail could no longer depend on offline business alone.</p>
      <p class="problem__p">Without digital transformation, millions of Kirana stores risk being left behind.</p>
    </div>
    <div class="problem__visual" data-reveal>
      <span class="deco deco--circle" aria-hidden="true"></span>
      <span class="deco deco--square" aria-hidden="true"></span>
      <span class="deco deco--dots" aria-hidden="true"></span>
      <svg class="deco deco--arc" viewBox="0 0 400 120" aria-hidden="true"><path d="M10 10 C 90 110, 300 120, 390 20" fill="none" stroke="#22b45c" stroke-width="2" stroke-dasharray="5 7" stroke-linecap="round"/><circle cx="52" cy="62" r="9" fill="#bdeacf"/><circle cx="52" cy="62" r="4.5" fill="#22b45c"/></svg>
      <figure class="problem__photo"><img src="assets/problem-kirana.webp" srcset="assets/problem-kirana-700.webp 700w, assets/problem-kirana.webp 1400w" sizes="(max-width: 900px) 100vw, 50vw" width="1400" height="933" alt="A worried Kirana store owner checking his phone, with online orders, inventory and falling sales around him" loading="lazy" decoding="async"></figure>
      <div class="float-card float-card--tl" aria-hidden="true"><span class="float-card__ico float-card__ico--red"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l1.5-5h15L21 9M3 9h18v2a3 3 0 01-6 0 3 3 0 01-6 0 3 3 0 01-6 0zM5 14v7h14v-7"/></svg></span></div>
      <div class="float-card float-card--br" aria-hidden="true"><span class="float-card__ico float-card__ico--red"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4l8 7 3-3 5 5M4 20V8M9 20v-6M14 20v-4M19 20v-3"/></svg></span></div>
    </div>
  </div>
</section>'''
s = s[:a] + problem + s[b:]

# ---- before / after ----
a, b = section("transform")
ba = '''<section class="section on-ink tear-section" id="transform" aria-labelledby="transform-h" style="padding-top:0">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">From traditional to digital</p>
      <h2 id="transform-h">Tear the old model open.</h2>
      <p class="lead">The same neighbourhood store — before and after Source Pro.</p>
    </div>
  </div>
  <div class="ba" id="tear">
    <figure class="ba__pane ba__pane--before">
      <img src="assets/problem-store.webp" width="784" height="754" alt="Before: a shopkeeper waiting in his traditional store" loading="lazy" decoding="async">
      <figcaption><span class="ba__tag">Before</span><strong>Traditional store</strong><span>Limited shelf space, limited stock, and customers who can only order by walking in.</span></figcaption>
    </figure>
    <div class="ba__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
    <figure class="ba__pane ba__pane--after">
      <img src="assets/digital-hypermarket.webp" srcset="assets/digital-hypermarket-700.webp 700w, assets/digital-hypermarket.webp 1400w" sizes="(max-width: 760px) 100vw, 50vw" width="1400" height="1120" alt="After: the same store transformed into a multi-storey Source Pro digital hypermarket" loading="lazy" decoding="async">
      <figcaption><span class="ba__tag ba__tag--after">After</span><strong>Source Pro digital hypermarket</strong><span>25,000+ products, a 24/7 storefront under the retailer's own name, and orders from existing customers.</span></figcaption>
    </figure>
  </div>
</section>'''
s = s[:a] + ba + s[b:]

# ---- app / Built for Bharat ----
a, b = section("app")
ico = lambda p: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % p
app = '''<section class="section app-section" id="app" aria-labelledby="app-h">
  <div class="container platform">
    <div class="platform__text">
      <p class="eyebrow">Built for Bharat</p>
      <h2 id="app-h" class="platform__h">Built for Bharat,<br>not just cities.</h2>
      <ul class="bharat">
        <li><span class="bharat__ico">%s</span><span class="bharat__bar" aria-hidden="true"></span><div><strong>Regional language support</strong>So the platform speaks the language of the shop.</div></li>
        <li><span class="bharat__ico">%s</span><span class="bharat__bar" aria-hidden="true"></span><div><strong>Simple app usage</strong>No technical knowledge required.</div></li>
        <li><span class="bharat__ico">%s</span><span class="bharat__bar" aria-hidden="true"></span><div><strong>Local distributor assistance</strong>Someone from your area to help you start.</div></li>
      </ul>
      <p class="app__avail">The Source Pro B2B app is available on Android and iOS.</p>
      <div class="store-badges">
        <a class="store-badge" href="https://play.google.com/store/apps/details?id=com.graeonai.renaissancetradingcompany"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 3.5v17l9-8.5zM14.3 13.2l2.6 2.5-10.7 5.9zM14.3 10.8L6.2 2.4l10.7 5.9zM18.4 9.6l2.6 1.5c.6.4.6 1.4 0 1.8l-2.6 1.5-2.8-2.4z"/></svg><span><small>Get it on</small><strong>Google Play</strong></span></a>
        <a class="store-badge" href="https://apps.apple.com/in/app/source-pro-b2b/id6742049723"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.4 12.6c0-2.3 1.9-3.4 2-3.5-1.1-1.6-2.8-1.8-3.4-1.8-1.4-.1-2.8.9-3.5.9s-1.8-.8-3-.8C6.9 7.4 5.4 8.3 4.6 9.7c-1.6 2.8-.4 6.9 1.2 9.2.8 1.1 1.7 2.3 2.9 2.3s1.6-.7 3-.7 1.8.7 3 .7 2-1.1 2.8-2.2c.9-1.3 1.2-2.5 1.3-2.6-.1 0-2.4-.9-2.4-3.8zM14.2 5.8c.6-.8 1.1-1.8.9-2.8-.9 0-2 .6-2.7 1.4-.6.7-1.1 1.8-1 2.7 1 .1 2.1-.5 2.8-1.3z"/></svg><span><small>Download on the</small><strong>App Store</strong></span></a>
      </div>
    </div>
    <div class="devices" role="img" aria-label="Illustration of two phones over a Source Pro digital hypermarket. Illustrative only, not actual app screens.">
      <svg class="devices__map" viewBox="0 0 100 100" aria-hidden="true"><path d="M40 4 48 3 54 8 52 14 58 18 66 16 72 20 80 22 88 26 92 30 86 32 80 30 76 34 84 38 80 42 74 40 68 38 64 42 62 50 58 58 54 70 50 84 47 96 43 86 38 72 34 60 26 56 20 50 24 44 28 38 26 32 30 28 36 22 34 14Z" fill="#dfe6fb"/></svg>
      <svg class="devices__arc" viewBox="0 0 400 300" aria-hidden="true"><path d="M20 120 C 0 220, 120 270, 220 290" fill="none" stroke="#22b45c" stroke-width="1.6" stroke-dasharray="4 6"/><path d="M270 40 C 360 20, 410 120, 380 190" fill="none" stroke="#22b45c" stroke-width="1.6" stroke-dasharray="4 6"/><circle cx="376" cy="70" r="6" fill="#22b45c"/></svg>
      <div class="devices__photo"><img src="assets/digital-hypermarket.webp" srcset="assets/digital-hypermarket-700.webp 700w, assets/digital-hypermarket.webp 1400w" sizes="(max-width: 900px) 100vw, 50vw" width="1400" height="1120" alt="" loading="lazy" decoding="async"></div>
      <div class="phone phone--a" data-depth="1"><div class="phone__screen"><div class="phone__bar"></div><div class="phone__block phone__block--accent"></div><div class="phone__grid"><i></i><i></i><i></i><i></i><i></i><i></i></div></div></div>
      <div class="phone phone--b" data-depth="1.6"><div class="phone__screen"><div class="phone__bar" style="width:60%%"></div><div class="phone__block"></div><div class="phone__block"></div><div class="phone__block phone__block--accent" style="height:44px"></div><div class="phone__block"></div></div></div>
      <div class="float-card float-card--store" aria-hidden="true"><span class="float-card__ico float-card__ico--green">%s</span></div>
      <div class="float-card float-card--pin" aria-hidden="true"><span class="float-card__ico float-card__ico--green">%s</span></div>
      <p class="device-note">Illustrative device visuals — not actual app screens.</p>
    </div>
  </div>
</section>''' % (
    ico('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'),
    ico('<rect x="7" y="2.5" width="10" height="19" rx="2.2"/><path d="M11 18.5h2"/>'),
    ico('<path d="M12 21s7-6.2 7-11.5a7 7 0 0 0-14 0C5 14.800 12 21 12 21z"/><circle cx="12" cy="9.500" r="2.500"/>'),
    ico('<path d="M3 9l1.5-5h15L21 9M3 9h18v2a3 3 0 01-6 0 3 3 0 01-6 0 3 3 0 01-6 0zM5 14v7h14v-7"/>'),
    ico('<path d="M12 21s7-6.2 7-11.5a7 7 0 0 0-14 0C5 14.800 12 21 12 21z"/><circle cx="12" cy="9.500" r="2.500"/>'))
s = s[:a] + app + s[b:]
open("_src/index.src.html", "w", encoding="utf8").write(s)

# ---- css ----
css = rd("css/styles.css")
css += '''
/* ===== v5: before/after, problem + app redesigns ===== */
.hero__grid { display: none; }

/* before / after */
.ba { display: grid; grid-template-columns: 1fr 1fr; position: relative; width: 100%; }
.ba__pane { position: relative; margin: 0; aspect-ratio: 5/4; max-height: 74vh; overflow: hidden; background: #0a0f3a; }
.ba__pane img { width: 100%; height: 100%; object-fit: cover; }
.ba__pane--before img { object-position: 50% 30%; filter: saturate(.7); }
.ba__pane::after { content: ""; position: absolute; inset: 0; background: linear-gradient(0deg, rgba(9, 13, 51, .92) 0%, rgba(9, 13, 51, .55) 34%, transparent 62%); }
.ba__pane figcaption { position: absolute; z-index: 2; left: clamp(1rem, 3vw, 3rem); right: clamp(1rem, 3vw, 3rem); bottom: clamp(1rem, 3vw, 2.5rem); display: grid; gap: .45rem; max-width: 34rem; }
.ba__pane figcaption strong { font-family: var(--font-display); font-size: clamp(1.4rem, 1rem + 1.6vw, 2.4rem); line-height: 1.05; text-transform: uppercase; }
.ba__pane figcaption span:last-child { color: var(--color-ink-muted); font-size: clamp(.9rem, .85rem + .3vw, 1.05rem); }
.ba__tag { justify-self: start; padding: .35rem .95rem; border-radius: 999px; background: #fff; color: var(--color-secondary); font-weight: 800; font-size: .8rem; letter-spacing: .16em; text-transform: uppercase; }
.ba__tag--after { background: var(--color-accent); }
.ba__arrow { position: absolute; z-index: 5; left: 50%; top: 50%; translate: -50% -50%; width: clamp(48px, 5vw, 72px); aspect-ratio: 1; border-radius: 50%; background: var(--color-accent); color: var(--color-secondary); display: grid; place-items: center; box-shadow: 0 0 0 8px rgba(255, 255, 255, .18), 0 12px 30px rgba(0, 0, 0, .4); }
.ba__arrow svg { width: 46%; height: 46%; }
@media (max-width: 760px) {
  .ba { grid-template-columns: 1fr; }
  .ba__pane { aspect-ratio: 4/3; max-height: none; }
  .ba__arrow svg { rotate: 90deg; }
}

/* problem — mock layout */
.problem-section { background: radial-gradient(60% 70% at 85% 30%, rgba(34, 180, 92, .09), transparent 70%), radial-gradient(40% 50% at 0% 100%, rgba(40, 48, 143, .07), transparent 70%), var(--color-background); overflow: hidden; }
.problem { grid-template-columns: 1fr 1.05fr; align-items: center; gap: clamp(2rem, 5vw, 5rem); }
.problem__h { font-size: clamp(2rem, 1.1rem + 3.4vw, 4.2rem); font-weight: 700; line-height: 1.02; letter-spacing: -.03em; margin-bottom: clamp(1.25rem, 3vw, 2.25rem); }
.problem__h mark { background: #bdeacf; color: inherit; padding: 0 .12em; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
.problem__p { color: var(--color-muted); font-size: var(--fs-lead); max-width: 34rem; }
.problem__p + .problem__p { margin-top: 1rem; }
.problem__visual { position: relative; padding: 1.5rem 1.75rem 2.5rem; }
.problem__photo { position: relative; z-index: 2; margin: 0; border-radius: 22px; overflow: hidden; border: 6px solid #fff; box-shadow: 0 30px 60px -28px rgba(15, 21, 71, .4); aspect-ratio: 3/2; }
.problem__photo img { width: 100%; height: 100%; object-fit: cover; }
.deco { position: absolute; z-index: 0; pointer-events: none; }
.deco--circle { right: -4%; top: -8%; width: 72%; aspect-ratio: 1; border-radius: 50%; background: radial-gradient(circle, #d6f4e2 55%, #bdeacf 100%); opacity: .8; }
.deco--square { left: 4%; bottom: 0; width: 40%; aspect-ratio: 1; border-radius: 28px; background: #dde3fa; rotate: 12deg; }
.deco--dots { right: 0; top: 0; width: 130px; height: 100px; background: radial-gradient(#7fd8a6 2px, transparent 2.5px) 0 0 / 20px 20px; }
.deco--arc { left: 16%; bottom: -2.5rem; width: 62%; height: auto; z-index: 3; }
.float-card { position: absolute; z-index: 4; padding: 12px; border-radius: 22px; background: #fff; box-shadow: 0 18px 40px -16px rgba(15, 21, 71, .35); }
.float-card__ico { display: grid; place-items: center; width: clamp(56px, 6vw, 84px); aspect-ratio: 1; border-radius: 50%; }
.float-card__ico svg { width: 46%; height: 46%; }
.float-card__ico--red { background: #fde6ea; color: #a3122f; }
.float-card__ico--green { background: #e1f6e9; color: #12904a; }
.float-card--tl { left: -1%; top: 8%; }
.float-card--br { right: -2%; bottom: 14%; }
@media (max-width: 900px) { .problem { grid-template-columns: 1fr; } .problem__visual { padding: 1rem 1rem 2rem; } .float-card { padding: 8px; border-radius: 16px; } .float-card__ico { width: 46px; } .float-card--tl { left: -2px; } .float-card--br { right: -2px; } }

/* app — mock layout */
.app-section { background: radial-gradient(50% 60% at 78% 45%, rgba(104, 132, 255, .14), transparent 70%), var(--color-background); overflow: hidden; }
.platform { grid-template-columns: .95fr 1.05fr; }
.platform__h { font-size: clamp(2.2rem, 1.2rem + 3.8vw, 4.6rem); line-height: 1; margin-bottom: clamp(1.5rem, 3vw, 2.5rem); }
.bharat { display: grid; gap: 1.1rem; margin: 0 0 1.75rem; }
.bharat li { display: grid; grid-template-columns: auto auto 1fr; align-items: center; gap: 1rem; padding: 0; border: 0; }
.bharat__ico { display: grid; place-items: center; width: 64px; height: 64px; border-radius: 50%; background: #e1f6e9; color: #12904a; }
.bharat__ico svg { width: 30px; height: 30px; }
.bharat__bar { width: 2px; height: 46px; background: var(--color-accent); border-radius: 2px; }
.bharat strong { display: block; font-family: var(--font-display); font-size: 1.3rem; color: var(--color-text); }
.bharat li div { color: var(--color-muted); }
.app__avail { color: var(--color-muted); margin-bottom: 1.25rem; }
.devices { height: clamp(440px, 46vw, 640px); margin: 0; }
.devices__map { position: absolute; right: -2%; top: -6%; width: 46%; height: auto; opacity: .85; }
.devices__arc { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 1; }
.devices__photo { position: absolute; left: 12%; right: 2%; top: 12%; bottom: 8%; border-radius: 28px; overflow: hidden; box-shadow: 0 30px 60px -30px rgba(40, 48, 143, .35); }
.devices__photo img { width: 100%; height: 100%; object-fit: cover; opacity: .55; }
.devices__photo::after { content: ""; position: absolute; inset: 0; background: linear-gradient(90deg, rgba(243, 245, 251, .85), rgba(243, 245, 251, .15) 55%, rgba(243, 245, 251, .5)); }
.phone { z-index: 3; width: clamp(150px, 19vw, 260px); }
.phone--a { left: 22%; top: 20%; rotate: -8deg; }
.phone--b { right: 12%; top: 6%; rotate: 5deg; background: var(--color-secondary); }
.float-card--store { left: 6%; top: 5%; z-index: 4; }
.float-card--pin { right: 2%; bottom: 10%; z-index: 4; border-radius: 50%; padding: 10px; }
.device-note { left: 12%; bottom: -1.9rem; }
@media (max-width: 900px) { .platform { grid-template-columns: 1fr; } .devices { height: clamp(360px, 90vw, 520px); } .devices__map { display: none; } .bharat__ico { width: 54px; height: 54px; } }
@media (max-width: 479px) { .bharat li { grid-template-columns: auto 1fr; } .bharat__bar { display: none; } .phone--a { left: 12%; } .phone--b { right: 4%; } .float-card--store { left: 0; } }
'''
open("css/styles.css", "w", encoding="utf8").write(css)

# ---- js: wipe reveal ----
js = rd("js/home.js")
if "ba__pane--after" not in js:
    js = js.replace("  /* ---------- reveals ---------- */", '''  /* ---------- before / after wipe ---------- */
  var afterPane = document.querySelector('.ba__pane--after');
  if (afterPane) {
    var vertical = window.matchMedia('(max-width: 760px)').matches;
    gsap.fromTo(afterPane, { clipPath: vertical ? 'inset(100% 0 0 0)' : 'inset(0 0 0 100%)' },
      { clipPath: 'inset(0 0 0 0)', ease: 'none', scrollTrigger: { trigger: '.ba', start: 'top 85%', end: 'top 30%', scrub: 0.5 } });
  }

  /* ---------- reveals ---------- */''')
    open("js/home.js", "w", encoding="utf8").write(js)
print("v5 applied")
