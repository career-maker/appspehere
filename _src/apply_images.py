"""One-off: wire real Source Pro logo + photos into sources. Idempotent-ish; run once."""
import re
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def rw(p, f):
    s = open(p, encoding="utf8").read()
    open(p, "w", encoding="utf8").write(f(s))


brand_h = ('<a class="brand" href="{{P}}index.html" aria-label="Source Pro B2B2C — home"><span class="brand__plate">'
           '<img src="{{P}}assets/logo-source-pro.png" width="408" height="128" '
           'alt="Source Pro B2B2C — For the people, by the distributors, through the retailers"></span></a>')
rw("_src/header.html", lambda s: re.sub(r'<a class="brand".*?</a>', lambda m: brand_h, s, count=1, flags=re.S))


def ftr(s):
    new = ('<a class="brand" href="{{P}}index.html" aria-label="Source Pro B2B2C — home"><span class="brand__plate">'
           '<img src="{{P}}assets/logo-source-pro.png" width="408" height="128" alt="Source Pro B2B2C" loading="lazy" decoding="async"></span></a>')
    s = re.sub(r'<a class="brand".*?</a>', lambda m: new, s, count=1, flags=re.S)
    s = s.replace('<h2>App Sphere B2B India Pvt. Ltd.</h2>',
                  '<img class="footer__co" src="{{P}}assets/logo-app-sphere.png" width="784" height="754" alt="App Sphere B2B India Pvt. Ltd." loading="lazy" decoding="async"><h2>App Sphere B2B India Pvt. Ltd.</h2>')
    return s


rw("_src/footer.html", ftr)


def idx(s):
    s = re.sub(r'<link rel="icon" href="data:[^"]*">', '<link rel="icon" href="assets/favicon.png" type="image/png">', s)
    s = s.replace('<meta name="twitter:card" content="summary_large_image">',
                  '<meta property="og:image" content="https://appsphereb2b.com/wp-content/uploads/2026/06/Retailer-Digital-Hyper.png">\n<meta name="twitter:card" content="summary_large_image">')
    s = re.sub(r'<!-- shared illustration symbols -->.*?</svg>\n\n', '', s, count=1, flags=re.S)
    a = s.index('<div class="layer layer--store"')
    b = s.index('<div class="layer layer--catalog"')
    store = '''<div class="layer layer--store" data-depth="1">
        <div class="photo-frame">
          <img src="assets/problem-store.webp" width="784" height="754" alt="A shopkeeper behind the counter of a traditional Indian store, shelves stacked with packaged goods" fetchpriority="high" decoding="async">
          <div class="store-hud">
            <span class="hud-box"></span>
            <span class="hud-chip hud-chip--a">Digital shelf</span>
            <span class="hud-chip hud-chip--b">24/7 orders</span>
          </div>
        </div>
      </div>
      '''
    s = s[:a] + store + s[b:]
    s = s.replace("<h1>India's retail.<br>",
                  "<p class=\"stage__kicker\">For the people · By the distributors · Through the retailers</p>\n        <h1>India's retail.<br>")
    a = s.index('<div class="tear__pane tear__pane--old">')
    b = s.index('<div class="tear__edge"')
    tear = '''<div class="tear__pane tear__pane--old"><img src="assets/problem-store.webp" width="784" height="754" alt="A shopkeeper waiting in his traditional store" loading="lazy" decoding="async"><span class="tear__label">Traditional store</span></div>
      <div class="tear__pane tear__pane--digital"><img src="assets/digital-hypermarket.webp" width="1400" height="1120" alt="A small general store transformed into a multi-storey Source Pro digital hypermarket through the Source Pro app" loading="lazy" decoding="async"><span class="tear__label">Source Pro digital hypermarket</span></div>
      '''
    s = s[:a] + tear + s[b:]
    s = s.replace('<span>Illustrative visuals — not actual app screens.</span>', '<span>Imagery from the Source Pro campaign.</span>')
    figs = {
        'retailer': ('digital-hypermarket', 'A small store becoming a digital hypermarket with Source Pro', 1400, 1120),
        'distributor': ('distributor-warehouse', 'A distributor checking orders on a tablet in a warehouse', 784, 754),
        'manufacturer': ('partners-handshake', 'A manufacturer and a distributor shaking hands in a supermarket aisle', 784, 754),
        'customer': ('ecosystem-india', 'A family buying from their trusted local retailer, part of the Source Pro ecosystem', 1600, 900),
    }
    for k, (f, alt, w, h) in figs.items():
        pat = re.compile(r'(<div class="role-panel" role="tabpanel" id="rp-%s".*?)(\n        </div>)' % k, re.S)
        fig = '\n          <figure class="role-fig"><img src="assets/%s.webp" width="%d" height="%d" alt="%s" loading="lazy" decoding="async"></figure>' % (f, w, h, alt)
        s = pat.sub(lambda m: m.group(1) + fig + m.group(2), s, count=1)
    s = s.replace('id="philosophy" aria-labelledby="phil-h">\n  <div class="container">',
                  'id="philosophy" aria-labelledby="phil-h">\n  <img class="philosophy__bg" src="assets/ecosystem-india.webp" width="1600" height="900" alt="" loading="lazy" decoding="async">\n  <div class="container">')
    s = s.replace('<a class="link-card" href="distributors.html"><div>',
                  '<a class="link-card" href="distributors.html"><img class="link-card__img" src="assets/partners-handshake.webp" width="784" height="754" alt="" loading="lazy" decoding="async"><div>')
    s = s.replace('<a class="link-card" href="partner-infrastructure.html"><div>',
                  '<a class="link-card" href="partner-infrastructure.html"><img class="link-card__img" src="assets/distributor-warehouse.webp" width="784" height="754" alt="" loading="lazy" decoding="async"><div>')
    return s


rw("_src/index.src.html", idx)


def bld(s):
    s = re.sub(r'<link rel="icon" href="data:[^"]*">', '<link rel="icon" href="assets/favicon.png" type="image/png">', s)
    s = s.replace('<section class="page-hero">\n    <div class="container">\n      <p class="crumbs"><a href="index.html">Source Pro</a> / Partnership</p>',
                  '<section class="page-hero">\n    <img class="page-hero__art" src="assets/distributor-warehouse.webp" width="784" height="754" alt="" decoding="async">\n    <div class="container">\n      <p class="crumbs"><a href="index.html">Source Pro</a> / Partnership</p>')
    s = s.replace('<section class="page-hero">\n    <div class="container">\n      <p class="crumbs"><a href="index.html">Source Pro</a> / Distributor network</p>',
                  '<section class="page-hero">\n    <img class="page-hero__art" src="assets/partners-handshake.webp" width="784" height="754" alt="" decoding="async">\n    <div class="container">\n      <p class="crumbs"><a href="index.html">Source Pro</a> / Distributor network</p>')
    return s


rw("_src/build.py", bld)

css = open("css/styles.css", encoding="utf8").read()


def sub(a, b):
    global css
    assert a in css, a[:60]
    css = css.replace(a, b)


sub('.layer--store { right: 4vw; top: 37%; width: min(47vw, 780px); translate: 0 -50%; }\n.layer--store svg { width: 100%; height: auto; filter: drop-shadow(0 40px 60px rgba(0, 0, 0, .5)); }',
    '.layer--store { right: 6vw; top: 38%; width: min(33vw, 540px); translate: 0 -50%; }\n.photo-frame { position: relative; border-radius: var(--radius-lg); overflow: hidden; box-shadow: 0 40px 80px -20px rgba(0, 0, 0, .65); border: 1px solid var(--color-ink-border); }\n.photo-frame img { width: 100%; height: auto; }')
sub('.store-hud { opacity: 0; }', '''.store-hud { position: absolute; inset: 0; opacity: 0; }
.hud-box { position: absolute; left: 50%; top: 3%; width: 47%; height: 56%; border: 2.5px dashed var(--color-accent); border-radius: 10px; background: rgba(242, 163, 58, .08); }
.hud-chip { position: absolute; padding: .3rem .8rem; border-radius: 999px; background: var(--color-accent); color: var(--color-secondary); font-weight: 800; font-size: clamp(.65rem, .5rem + .4vw, .85rem); letter-spacing: .08em; text-transform: uppercase; }
.hud-chip--a { left: 50%; top: 3%; translate: 0 -50%; margin-left: .75rem; }
.hud-chip--b { left: 6%; bottom: 8%; }''')
sub('.layer--store { right: auto; left: 50%; top: 26%; translate: -50% -50%; width: 104vw; }',
    '.layer--store { right: auto; left: 50%; top: 30%; translate: -50% -50%; width: min(64vw, 280px); }')
sub('width: min(92%, 760px); margin: 0 auto 2rem; }', 'width: min(92%, 460px); margin: 0 auto 2rem; }')
sub('.tear__pane svg { width: min(92%, 780px); }', '.tear__pane img { width: 100%; height: 100%; object-fit: cover; }')
sub('overflow: hidden; background: #0d2a3a; aspect-ratio: 16/9; isolation', 'overflow: hidden; background: #0d2a3a; aspect-ratio: 16/10; isolation')
sub('.tear__pane--digital { clip-path: inset(0 0 0 var(--split, 50%)); background: linear-gradient(135deg, #0e5a5e, #0b1f2e); }',
    '.tear__pane--digital { clip-path: inset(0 0 0 var(--split, 50%)); }\n.tear__pane--digital img { object-position: 60% 40%; }\n.tear__pane--old img { filter: saturate(.6) sepia(.2) brightness(.85); }')
sub('.tear__pane--old { background: linear-gradient(180deg, #2a2118, #17110c); }', '')
sub('@media (max-width: 700px) { .tear { aspect-ratio: 4/3.4; }', '@media (max-width: 700px) { .tear { aspect-ratio: 4/5; }')
css += '''
/* ---- real imagery ---- */
.brand__plate { display: inline-flex; align-items: center; background: #fffdf8; border-radius: 12px; padding: 4px 12px; box-shadow: 0 6px 20px -10px rgba(0, 0, 0, .5); }
.brand__plate img { height: 46px; width: auto; }
.footer .brand__plate img { height: 56px; }
.footer__co { width: 72px; height: auto; margin-bottom: .75rem; }
.role-panel { display: grid; grid-template-columns: 1.25fr 1fr; column-gap: clamp(1.5rem, 3vw, 3rem); align-content: start; }
.role-panel > :not(.role-fig) { grid-column: 1; }
.role-panel[hidden] { display: none; }
.role-fig { grid-column: 2; grid-row: 1 / span 4; margin: 0; border-radius: var(--radius); overflow: hidden; align-self: stretch; min-height: 260px; }
.role-fig img { width: 100%; height: 100%; object-fit: cover; }
@media (max-width: 1100px) { .role-panel { grid-template-columns: 1fr; } .role-fig { grid-column: 1; grid-row: auto; order: -1; min-height: 0; aspect-ratio: 16/9; margin-bottom: 1.5rem; } }
.philosophy__bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: .22; mix-blend-mode: luminosity; }
.philosophy::before { z-index: 1; background: radial-gradient(60% 70% at 50% 40%, rgba(11, 31, 46, .2), var(--color-secondary) 95%); }
.philosophy > .container { z-index: 2; }
.link-card__img { position: relative; width: 100%; height: 190px; object-fit: cover; border-radius: var(--radius); }
.page-hero__art { position: absolute; right: 0; top: 0; width: min(46%, 640px); height: 100%; object-fit: cover; opacity: .55; mask-image: linear-gradient(90deg, transparent, #000 55%); -webkit-mask-image: linear-gradient(90deg, transparent, #000 55%); }
@media (max-width: 760px) { .page-hero__art { width: 100%; opacity: .18; } }
'''
open("css/styles.css", "w", encoding="utf8").write(css)
print("applied")
