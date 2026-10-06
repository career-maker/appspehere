"""v7: slider-style tear (taller, full image visible), exclusive FAQ, mobile hero overlap fixes."""
import os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
rd = lambda p: open(p, encoding="utf8").read()
s = rd("_src/index.src.html")

# ---- tear: back to the reveal slider ----
a = s.index('<section class="section on-ink tear-section"')
b = s.index("</section>", a) + len("</section>")
tear = '''<section class="section on-ink tear-section" id="transform" aria-labelledby="transform-h" style="padding-top:0">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">From traditional to digital</p>
      <h2 id="transform-h">Tear the old model open.</h2>
      <p class="lead">The same neighbourhood store — before and after Source Pro. Drag the divider, or use the arrow keys, to compare.</p>
    </div>
  </div>
  <div class="tear tear--tall" id="tear" style="--split:50%">
    <div class="tear__pane tear__pane--old" style="--img:url(assets/problem-store.webp)">
      <img src="assets/problem-store.webp" width="784" height="754" alt="Before: a shopkeeper waiting in his traditional store" loading="lazy" decoding="async">
      <div class="tear__cap"><span class="ba__tag">Before</span><strong>Traditional store</strong><span>Limited shelf space, limited stock, and customers who can only order by walking in.</span></div>
    </div>
    <div class="tear__pane tear__pane--digital" style="--img:url(assets/digital-hypermarket.webp)">
      <img src="assets/digital-hypermarket.webp" width="1400" height="1120" alt="After: the same store transformed into a multi-storey Source Pro digital hypermarket" loading="lazy" decoding="async">
      <div class="tear__cap tear__cap--after"><span class="ba__tag ba__tag--after">After</span><strong>Source Pro digital hypermarket</strong><span>25,000+ products, a 24/7 storefront under the retailer's own name, and orders from existing customers.</span></div>
    </div>
    <div class="tear__edge" aria-hidden="true"></div>
    <input class="tear__range" type="range" min="0" max="100" value="50" aria-label="Compare before and after: drag to reveal the Source Pro digital hypermarket" />
  </div>
</section>'''
s = s[:a] + tear + s[b:]
open("_src/index.src.html", "w", encoding="utf8").write(s)

css = rd("css/styles.css")
css += '''
/* ===== v7 ===== */
/* tear slider — tall, whole photos visible */
.tear--tall { display: block; position: relative; width: 100%; max-width: none; margin: 0; border-radius: 0; border-inline: 0; aspect-ratio: auto; height: min(84vh, 820px); min-height: 420px; max-height: none; background: #0a0f3a; overflow: hidden; touch-action: pan-y; }
.tear--tall .tear__pane { position: absolute; inset: 0; display: block; background: #0a0f3a; overflow: hidden; }
.tear--tall .tear__pane::before { content: ""; position: absolute; inset: -6%; background: var(--img) center / cover; filter: blur(28px) brightness(.55) saturate(1.1); }
.tear--tall .tear__pane--digital { clip-path: inset(0 0 0 var(--split, 50%)); }
.tear--tall .tear__pane img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; object-position: 50% 50%; filter: none; }
.tear--tall .tear__pane--old img { filter: saturate(.75); }
.tear--tall .tear__pane::after { content: ""; position: absolute; inset: auto 0 0 0; height: 46%; background: linear-gradient(0deg, rgba(9, 13, 51, .92), transparent); }
.tear__cap { position: absolute; z-index: 3; left: clamp(1rem, 4vw, 4rem); bottom: clamp(1rem, 4vw, 3rem); max-width: min(30rem, 42vw); display: grid; gap: .45rem; }
.tear__cap--after { left: auto; right: clamp(1rem, 4vw, 4rem); text-align: left; }
.tear__cap strong { font-family: var(--font-display); font-size: clamp(1.3rem, 1rem + 1.6vw, 2.4rem); line-height: 1.05; text-transform: uppercase; }
.tear__cap span:last-child { color: var(--color-ink-muted); font-size: clamp(.85rem, .8rem + .3vw, 1.05rem); }
.tear--tall .tear__edge { z-index: 4; }
.tear--tall .tear__range { z-index: 5; }
@media (max-width: 760px) {
  .tear--tall { height: min(78svh, 620px); min-height: 380px; }
  .tear__cap, .tear__cap--after { max-width: 44vw; bottom: 1rem; }
  .tear__cap span:last-child { display: none; }
  .tear__cap strong { font-size: 1.05rem; }
}

/* hero layers: never rely on the CSS translate property (GSAP parallax rewrites it) */
.layer--store { top: 0; bottom: 0; left: auto; right: 6vw; translate: none; display: flex; align-items: center; padding-bottom: 24svh; }
.layer--store .photo-frame { width: 100%; }
@media (min-width: 768px) and (max-width: 1099px) and (orientation: landscape) { .layer--store { top: 0; bottom: 0; right: 5vw; padding-bottom: 26svh; width: min(34vw, 62svh); translate: none; } }
@media (min-width: 768px) and (max-width: 1099px) and (orientation: portrait) {
  .layer--store { top: calc(var(--header-h) + 5svh); bottom: auto; left: 0; right: 0; margin-inline: auto; padding: 0; display: block; translate: none; width: min(54vw, 40svh); }
}
@media (max-width: 767px) {
  .layer--store { top: calc(var(--header-h) + 3svh); bottom: auto; left: 0; right: 0; margin-inline: auto; padding: 0; display: block; translate: none; width: min(62vw, 38svh); }
  .eco { height: min(42svh, calc(100svh - var(--header-h) - 8svh - 350px)); }
  .stage__cta .btn { min-height: 46px; }
}
@media (max-height: 560px) and (orientation: landscape) { .layer--store { top: calc(var(--header-h) + 1svh); bottom: auto; left: auto; right: 76px; margin: 0; padding: 0; display: block; translate: none; width: min(30vw, 56svh); } }
.hero.is-static .layer--store { position: relative; inset: auto; display: block; padding: 0; margin: 0 auto 2rem; width: min(92%, 460px); translate: none; }

/* short phones (≤720px tall): ecosystem switches to the horizontal composition, buttons sit side by side */
@media (max-width: 767px) and (max-height: 720px) {
  .eco__lines--h { display: block; } .eco__lines--v { display: none; }
  .layer--eco { padding-top: calc(var(--header-h) + 5svh); }
  .eco { width: 94vw; height: min(30svh, 190px); }
  .node:nth-child(1) { left: 12.5%; top: 30%; } .node:nth-child(2) { left: 37.5%; top: 70%; }
  .node:nth-child(3) { left: 62.5%; top: 30%; } .node:nth-child(4) { left: 87.5%; top: 70%; }
  .node__orb { width: 40px; }
  .node__name, .node:nth-child(odd) .node__name, .node:nth-child(even) .node__name { top: 28px; left: 0; right: auto; translate: -50% 0; text-align: center; font-size: .62rem; letter-spacing: .02em; }
  .stage:not(.stage--intro) .stage__kicker { display: none; }
  .stage__cta { gap: .5rem; flex-wrap: nowrap; }
  .stage__cta .btn { flex: 1 1 0; width: auto; min-height: 44px; padding: .45rem .7rem; font-size: .82rem; line-height: 1.15; text-align: center; }
  .stage__cta .btn svg { display: none; }
}
'''
open("css/styles.css", "w", encoding="utf8").write(css)

# ---- exclusive FAQ (all pages) ----
m = rd("js/main.js")
if "exclusive accordion" not in m:
    m = m.rstrip()
    assert m.endswith("})();")
    m = m[:-5] + '''
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
})();
'''
    open("js/main.js", "w", encoding="utf8").write(m)
print("v7 applied")
