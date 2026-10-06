"""v4: device-tier responsive system + responsive images."""
import os
import re
from PIL import Image

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---- responsive image variants ----
for name, w in [("digital-hypermarket", 700), ("ecosystem-india", 800), ("problem-store", 520), ("partners-handshake", 520), ("distributor-warehouse", 520)]:
    im = Image.open("assets/%s.webp" % name).convert("RGB")
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save("assets/%s-%d.webp" % (name, w), quality=78, method=6)
SMALL = {"digital-hypermarket": (700, 1400), "ecosystem-india": (800, 1600), "problem-store": (520, 784),
         "partners-handshake": (520, 784), "distributor-warehouse": (520, 784)}

p = "_src/index.src.html"
s = open(p, encoding="utf8").read()


def add_srcset(m):
    tag = m.group(0)
    name = m.group(1)
    if "srcset=" in tag or name not in SMALL or "fetchpriority" in tag:
        return tag
    sm, big = SMALL[name]
    return tag.replace('src="assets/%s.webp"' % name,
                       'src="assets/%s.webp" srcset="assets/%s-%d.webp %dw, assets/%s.webp %dw" sizes="(max-width: 700px) 100vw, 60vw"' % (name, name, sm, sm, name, big))


s = re.sub(r'<img [^>]*src="assets/([a-z-]+)\.webp"[^>]*>', add_srcset, s)
open(p, "w", encoding="utf8").write(s)

css = open("css/styles.css", encoding="utf8").read()
css += '''
/* =========================================================
   v4 — DEVICE-TIER RESPONSIVE SYSTEM
   phone-s ≤479 · phone 480–767 · tablet 768–1099 (portrait + landscape)
   laptop 1100–1439 · desktop 1440–1699 · wide ≥1700
   ========================================================= */

/* wide screens: let the layout breathe */
@media (min-width: 1700px) {
  :root { --max: 1560px; --gutter: 5rem; --fs-hero: 8.5rem; --fs-h2: 5.25rem; }
  .layer--store { width: min(28vw, 640px); right: 8vw; }
  .eco { width: min(80vw, 1300px); }
}

/* tablet + phones: contact widgets become floating buttons, no scroll cue */
@media (max-width: 1100px) {
  .side-widgets { top: auto; bottom: 92px; right: 12px; translate: none; gap: 10px; }
  .sw { width: 46px; height: 46px; border-radius: 50%; box-shadow: 0 10px 24px -8px rgba(0, 0, 0, .55); }
  .sw:hover, .sw:focus-visible { width: 46px; transform: scale(1.08); }
  .hero__scroll { display: none; }
}

/* ---- laptop / small desktop ---- */
@media (min-width: 1100px) and (max-width: 1439px) {
  .layer--store { width: min(36vw, 520px); right: 5vw; }
  .stage h1 { font-size: clamp(4rem, 7vw, 6.5rem); }
}

/* ---- tablet landscape (e.g. 1024×768) ---- */
@media (min-width: 768px) and (max-width: 1099px) and (orientation: landscape) {
  .layer--store { width: min(34vw, 62svh); top: 36%; right: 5vw; }
  .stage h1 { font-size: clamp(3rem, 7.4vw, 5.5rem); }
  .stage__title { font-size: clamp(1.8rem, 4.4vw, 3.4rem); }
}

/* ---- tablet portrait (e.g. 768×1024, 820×1180) — its own composition ---- */
@media (min-width: 768px) and (max-width: 1099px) and (orientation: portrait) {
  .layer--store { right: auto; left: 50%; top: calc(var(--header-h) + 5svh); translate: -50% 0; width: min(54vw, 40svh); }
  .stage { bottom: 4.5rem; }
  .stage h1 { font-size: clamp(3.5rem, 11vw, 6.5rem); }
  .stage__title { font-size: clamp(2rem, 6.4vw, 4rem); }
  .layer--eco { padding-top: calc(var(--header-h) + 9svh); }
  .eco { width: 90vw; height: min(32svh, 380px); }
  .catalog { width: 88vw; aspect-ratio: 4/3; }
  .hero__rail { bottom: 4.5rem; }
}
@media (min-width: 768px) and (max-width: 1099px) {
  .section { padding-block: clamp(4rem, 8vw, 6rem); }
  .zeros { grid-template-columns: repeat(3, 1fr); }
  .photo-card { aspect-ratio: 16/9; }
  .footer__grid { grid-template-columns: 1.3fr 1fr 1fr; }
  .footer__grid address { grid-column: 1 / -1; }
}
@media (min-width: 641px) and (max-width: 860px) { .zeros { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 860px) { .photo-card { aspect-ratio: 16/9; } }

/* ---- phones: one composition for 320 → 767 ---- */
@media (max-width: 767px) {
  .hero__pin { min-height: 520px; }
  .layer--store { right: auto; left: 50%; top: calc(var(--header-h) + 3svh); translate: -50% 0; width: min(62vw, 38svh); }
  .stage { bottom: 5rem; }
  .stage h1 { font-size: clamp(2.2rem, 11.5vw, 4.5rem); }
  .stage__title { font-size: clamp(1.7rem, 8.4vw, 3rem); }
  .stage__cta .btn { width: calc(100% - 58px); }
  /* progress rail moves to the top under the header */
  .hero__rail { top: calc(var(--header-h) + 6px); bottom: auto; left: var(--gutter); right: var(--gutter); flex-direction: row; gap: 6px; }
  .hero__rail li { flex: 1; width: auto; height: 3px; }
  .layer--eco { padding-top: calc(var(--header-h) + 8svh); }
  .eco { height: 42svh; }
  .catalog__num { font-size: clamp(2.75rem, 17vw, 5rem); }
  .section-head h2 { font-size: clamp(1.8rem, 8.4vw, 2.6rem); }
  .tear__label { top: auto; bottom: .6rem; font-size: .62rem; padding: .25rem .6rem; }
  .tear__pane--old .tear__label { left: .6rem; } .tear__pane--digital .tear__label { right: .6rem; }
  .tear-grid { gap: 1rem; }
  .quote blockquote { font-size: clamp(1.2rem, .9rem + 2.6vw, 1.7rem); }
  .quote blockquote::before { font-size: 2.2em; }
  .philosophy blockquote { font-size: clamp(1.25rem, 5.2vw, 1.8rem); }
  .cta h2 { font-size: clamp(2.2rem, 11vw, 3.5rem); }
  .btn { width: auto; }
  .role-panel { padding: 1.25rem; }
  .role-panel h3 { font-size: clamp(1.5rem, 6.4vw, 2rem); }
  .links-grid { gap: 1rem; }
  .link-card { min-height: 0; }
  .devices { height: clamp(320px, 90vw, 460px); }
  .phone { width: clamp(130px, 38vw, 190px); }
  .story__sticky { height: 34svh; }
  .store-badges .store-badge { flex: 1 1 100%; }
  .footer__legal { flex-direction: column; }
}
@media (max-width: 479px) {
  .stage__kicker { font-size: .64rem; letter-spacing: .1em; }
  .role-tabs { gap: .4rem; }
  .role-tab { font-size: .8rem; padding: .7rem .6rem; min-height: 48px; }
  .eco-tab { padding: .9rem; gap: .75rem; }
  .step { padding: 1.1rem; }
  .step__n { font-size: 2.6rem; }
  .sp-form-section { padding: 1.1rem; }
  .sp-summary-grid { grid-template-columns: 1fr 1fr; }
  .sp-summary-card strong { font-size: 1.75rem; }
  .page-hero h1 { font-size: clamp(2rem, 11vw, 3rem); }
  .nav .btn { font-size: 1rem; }
}
/* short phones (iPhone SE, 320×568) */
@media (max-width: 767px) and (max-height: 700px) {
  .stage--intro .lead, .stage__sub { display: none; }
  .stage { bottom: 4.5rem; }
}
/* landscape phones (e.g. 812×375) */
@media (max-height: 560px) and (orientation: landscape) {
  .hero__pin { min-height: 0; }
  .stage--intro .lead, .stage__sub, .stage__kicker { display: none; }
  .stage { bottom: 1.5rem; }
  .stage h1 { font-size: min(8vw, 17svh); }
  .stage__title { font-size: min(5vw, 11svh); }
  .stage__cta { margin-top: .75rem; }
  .layer--store { width: min(30vw, 56svh); top: calc(var(--header-h) + 1svh); right: 6vw; translate: 0 0; left: auto; }
  .layer--eco { padding-top: calc(var(--header-h) + 1svh); }
  .eco { height: 36svh; }
  .hero__rail { display: none; }
  .side-widgets { bottom: 60px; }
}
/* hover-less devices: no hover-only affordances */
@media (hover: none) {
  .eco-tab:hover, .link-card:hover { transform: none; }
}
'''
open("css/styles.css", "w", encoding="utf8").write(css)
print("v4 applied")
