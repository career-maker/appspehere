"""v3: logo-matched theme, live-site widgets (side contact, Smatbot chatbot, GTranslate), more photos, full-width tear."""
import os
import re

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
rd = lambda p: open(p, encoding="utf8").read()


def wr(p, s):
    open(p, "w", encoding="utf8").write(s)


# ---------- 1. recolour to the logo palette (indigo + green) ----------
MAP = [
    ("#f2a33a", "#22b45c"), ("rgba(242, 163, 58", "rgba(34, 180, 92"), ("rgba(242,163,58", "rgba(34,180,92"),
    ("#ffb752", "#3fcd78"), ("#d98512", "#0d8a42"),
    ("#0e5a5e", "#28308f"), ("#0a4346", "#1c2370"), ("rgba(14, 90, 94", "rgba(40, 48, 143"),
    ("#1a7478", "#3641b0"), ("#137176", "#2f3aa8"),
    ("#0b1f2e", "#0f1547"), ("rgba(11, 31, 46", "rgba(15, 21, 71"),
    ("#0d2a3a", "#141b5c"), ("#143a4c", "#1b2470"), ("#12304a", "#1a2372"), ("#0f2c3e", "#131a58"),
    ("#07151f", "#090d33"), ("#17384c", "#1f2878"), ("#0f2a3b", "#151d60"),
    ("#12212b", "#12163d"), ("#4f5e68", "#4a4f72"),
    ("#f6f1e7", "#f3f5fb"), ("#fffdf8", "#ffffff"), ("#d9d2c3", "#d3d8ea"),
    ("#f3eee3", "#f2f4fb"), ("rgba(243, 238, 227", "rgba(242, 244, 251"), ("#a9b8bf", "#aab1d8"),
    ("#efe9da", "#e8ecf7"), ("#ece7da", "#e6e9f4"), ("#fbf8f0", "#f7f8fd"), ("#b9b19f", "#a9afcc"),
    ("#fff3da", "#e9ecfa"),
]
for p in ["css/styles.css", "_src/index.src.html", "_src/header.html", "_src/footer.html", "_src/build.py", "js/home.js", "js/distributors.js"]:
    s = rd(p)
    for a, b in MAP:
        s = s.replace(a, b)
    wr(p, s)

css = rd("css/styles.css")
css = css.replace(".sp-status-limited { background: #fdf0d5; color: #7a4a05; border-color: #f2c66f; }",
                  ".sp-status-limited { background: #fff3d6; color: #7a4a05; border-color: #e8c36a; }")
wr("css/styles.css", css)

# ---------- 2. widgets partial ----------
widgets = '''<!-- widgets mirrored from appsphereb2b.com: side contact (WhatsApp + phone), GTranslate language switcher, Smatbot chatbot -->
<div class="side-widgets" role="complementary" aria-label="Quick contact">
  <a class="sw sw--wa" href="https://wa.me/919778452007" target="_blank" rel="noopener" aria-label="Chat with Source Pro on WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5.1-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.700 6.700 0 0 1-3.300-2.900c-.2-.4.2-.4.700-1.300.1-.2 0-.3 0-.4l-.8-1.800c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.200 5.200 5.200 0 0 0 1.100 2.800 11.800 11.800 0 0 0 4.500 4c1.700.7 2.300.8 3.200.6a2.700 2.700 0 0 0 1.800-1.300 2.200 2.200 0 0 0 .2-1.300c-.1-.1-.3-.2-.5-.3z"/></svg></a>
  <a class="sw sw--call" href="tel:+919778452007" aria-label="Call Source Pro: +91 97784 52007"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.200 2 19.800 19.800 0 0 1-8.600-3.100 19.500 19.500 0 0 1-6-6A19.800 19.800 0 0 1 2.100 4.200 2 2 0 0 1 4.100 2h3a2 2 0 0 1 2 1.700c.1 1 .4 1.900.7 2.800a2 2 0 0 1-.5 2.100L8.100 9.900a16 16 0 0 0 6 6l1.300-1.300a2 2 0 0 1 2.100-.4c.9.3 1.800.6 2.800.7a2 2 0 0 1 1.700 2z"/></svg></a>
</div>
<div id="gt-wrapper" class="gtranslate_wrapper"></div>
<script>
window.gtranslateSettings = {"default_language":"en","languages":["bn","en","hi","kn","ml","mr","pa","ta","te","ur"],"url_structure":"none","flag_style":"2d","wrapper_selector":"#gt-wrapper","alt_flags":[],"float_switcher_open_direction":"top","switcher_horizontal_position":"left","switcher_vertical_position":"bottom"};
</script>
<script src="https://cdn.gtranslate.net/widgets/latest/float.js" defer></script>
<script>
chatbot_id=26200;!function(){var t,e,a=document,s="smatbot-chatbot";a.getElementById(s)||(t=a.createElement("script"),t.id=s,t.type="text/javascript",t.src="https://plugin.smatbot.com/smatbot_plugin.js.gz",e=a.getElementsByTagName("script")[0],e.parentNode.insertBefore(t,e))}();
</script>
'''
wr("_src/widgets.html", widgets)

b = rd("_src/build.py")
if "widgets.html" not in b:
    b = b.replace('header_t, footer_t = rd("header.html"), rd("footer.html")', 'header_t, footer_t = rd("header.html"), rd("footer.html")\nwidgets_t = rd("widgets.html")')
    b = b.replace('def footer(prefix):\n    return footer_t.replace("{{P}}", prefix)', 'def footer(prefix):\n    return footer_t.replace("{{P}}", prefix) + widgets_t')
    wr("_src/build.py", b)
idx = rd("_src/index.src.html")
if "{{WIDGETS}}" not in idx:
    idx = idx.replace("{{FOOTER}}", "{{FOOTER}}")  # footer() now appends widgets

# ---------- 3. index: tear full-bleed, hide caption, more photos ----------
a = idx.index('<section class="section on-ink" id="transform"')
b_ = idx.index("<!-- ================= ECOSYSTEM")
tear = '''<section class="section on-ink tear-section" id="transform" aria-labelledby="transform-h" style="padding-top:0">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">From traditional to digital</p>
      <h2 id="transform-h">Tear the old model open.</h2>
      <p class="lead">Drag the divider — or use the arrow keys — to see the same neighbourhood store become a Source Pro digital hypermarket.</p>
    </div>
  </div>
  <div class="tear tear--full" id="tear" style="--split:50%">
    <div class="tear__pane tear__pane--old"><img src="assets/problem-store.webp" width="784" height="754" alt="A shopkeeper waiting in his traditional store" loading="lazy" decoding="async"><span class="tear__label">Traditional store</span></div>
    <div class="tear__pane tear__pane--digital"><img src="assets/digital-hypermarket.webp" width="1400" height="1120" alt="A small general store transformed into a multi-storey Source Pro digital hypermarket through the Source Pro app" loading="lazy" decoding="async"><span class="tear__label">Source Pro digital hypermarket</span></div>
    <div class="tear__edge" aria-hidden="true"></div>
    <input class="tear__range" type="range" min="0" max="100" value="50" aria-label="Reveal: traditional store versus Source Pro digital hypermarket" />
  </div>
  <div class="container">
    <div class="tear-grid">
      <div><h3>Before</h3><p>Limited shelf space, limited stock, and customers who can only order by walking in.</p></div>
      <div><h3>With Source Pro</h3><p>25,000+ products, a 24/7 storefront under the retailer's own name, and orders from existing customers.</p></div>
    </div>
  </div>
</section>

'''
idx = idx[:a] + tear + idx[b_:]

# problem: add photo
idx = idx.replace('''    <div class="problem__body" data-reveal>
      <p>The pandemic exposed that traditional retail could no longer depend on offline business alone.</p>
      <p>Without digital transformation, millions of Kirana stores risk being left behind.</p>
    </div>''', '''    <div class="problem__body" data-reveal>
      <figure class="photo-card"><img src="assets/problem-store.webp" width="784" height="754" alt="A Kirana store owner waiting behind his counter" loading="lazy" decoding="async"></figure>
      <p>The pandemic exposed that traditional retail could no longer depend on offline business alone.</p>
      <p>Without digital transformation, millions of Kirana stores risk being left behind.</p>
    </div>''')
# solution: photo band
idx = idx.replace('''    <div class="zeros" data-reveal>''', '''    <figure class="photo-band" data-reveal><img src="assets/digital-hypermarket.webp" width="1400" height="1120" alt="A small general store becomes a Source Pro digital hypermarket" loading="lazy" decoding="async"></figure>
    <div class="zeros" data-reveal>''')
# ecosystem: wide image
idx = idx.replace('''    <div class="ecosystem">''', '''    <figure class="photo-band photo-band--wide" data-reveal><img src="assets/ecosystem-india.webp" width="1600" height="900" alt="Manufacturer, super stockist, distributor, retailer and customers connected across India" loading="lazy" decoding="async"></figure>
    <div class="ecosystem">''')
# story visuals -> photos
for i, (img, pos, alt) in enumerate([
        ("problem-store", "50% 40%", "A traditional store shelf"),
        ("digital-hypermarket", "50% 50%", "A digital catalogue of products"),
        ("digital-hypermarket", "78% 40%", "A digital hypermarket"),
        ("ecosystem-india", "88% 55%", "A family ordering from their trusted local shop"),
        ("distributor-warehouse", "50% 50%", "Orders prepared for local fulfilment")]):
    pat = re.compile(r'(<div class="story__visual[^"]*" data-v="%d">).*?(</div>\n(?=        <div class="story__visual|      </div>\n      <ol))' % i, re.S)
    inner = '<img src="assets/%s.webp" alt="%s" style="object-position:%s" loading="lazy" decoding="async">' % (img, alt, pos)
    if i == 2:
        inner += '<div class="story__big">25,000+<div class="catalog__label">Products</div></div>'
    idx, n = pat.subn(lambda m: m.group(1) + inner + m.group(2), idx, count=1)
    assert n == 1, i
# how it works: photos in cards
cards = ["partners-handshake", "digital-hypermarket", "ecosystem-india", "distributor-warehouse"]
pos = ["50% 50%", "50% 40%", "88% 55%", "50% 50%"]
k = 0


def add_bg(m):
    global k
    r = m.group(0) + '<img class="step__bg" src="assets/%s.webp" alt="" style="object-position:%s" loading="lazy" decoding="async">' % (cards[k], pos[k])
    k += 1
    return r


idx = re.sub(r'<button class="step" type="button" aria-expanded="(?:true|false)" aria-controls="s\d">', add_bg, idx)
# app: backdrop photo
idx = idx.replace('<div class="devices" role="img"', '<div class="devices" role="img"')
idx = idx.replace('<div class="phone phone--a"', '<img class="devices__bg" src="assets/digital-hypermarket.webp" width="1400" height="1120" alt="" loading="lazy" decoding="async">\n      <div class="phone phone--a"', 1)
# cta backdrop
idx = idx.replace('id="cta" aria-labelledby="cta-h" style="padding-top:0">\n  <div class="container">', 'id="cta" aria-labelledby="cta-h" style="padding-top:0">\n  <img class="cta__bg" src="assets/partners-handshake.webp" width="784" height="754" alt="" loading="lazy" decoding="async">\n  <div class="container">')
wr("_src/index.src.html", idx)

# ---------- 4. css ----------
css = rd("css/styles.css")
css += '''
/* ===== v3: widgets, full-bleed tear, more photos ===== */
.side-widgets { position: fixed; right: 0; top: 50%; translate: 0 -50%; z-index: 90; display: grid; gap: 2px; }
.sw { width: 52px; height: 52px; display: grid; place-items: center; color: #fff; transition: width var(--t-fast) var(--ease), background var(--t-fast); border-radius: 12px 0 0 12px; }
.sw svg { width: 26px; height: 26px; }
.sw--wa { background: #25d366; } .sw--call { background: var(--color-primary); }
.sw:hover, .sw:focus-visible { width: 62px; }
.gtranslate_wrapper { position: relative; z-index: 95; }
@media (max-width: 760px) { .sw { width: 46px; height: 46px; } .side-widgets { top: auto; bottom: 90px; translate: none; } }

.tear-section { overflow: hidden; }
.tear--full { max-width: none; width: 100%; margin: 0; border-radius: 0; border-inline: 0; aspect-ratio: 21/8; max-height: 56vh; min-height: 300px; }
.tear--full .tear__pane--old img { object-position: 50% 32%; }
.tear--full .tear__pane--digital img { object-position: 50% 30%; }
.tear--full + .container .tear-grid { max-width: none; }
@media (max-width: 700px) { .tear--full { aspect-ratio: 16/11; max-height: none; } }
.tear__caption { display: none; }

.photo-card { margin: 0 0 1.25rem; border-radius: var(--radius-lg); overflow: hidden; aspect-ratio: 16/10; }
.photo-card img, .photo-band img { width: 100%; height: 100%; object-fit: cover; }
.photo-band { margin: 0 0 clamp(1.5rem, 4vw, 3rem); border-radius: var(--radius-lg); overflow: hidden; aspect-ratio: 21/8; }
.photo-band img { object-position: 50% 35%; }
.photo-band--wide { aspect-ratio: 16/7; }
.photo-band--wide img { object-position: 50% 45%; }
@media (max-width: 700px) { .photo-band, .photo-band--wide { aspect-ratio: 16/10; } }

.story__visual { padding: 0; }
.story__visual img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.story__visual::after { content: ""; position: absolute; inset: 0; background: linear-gradient(0deg, rgba(15, 21, 71, .55), transparent 55%); }
.story__visual .story__big { position: relative; z-index: 2; text-shadow: 0 6px 30px rgba(0, 0, 0, .6); }
.story__visual .catalog__label { color: #fff; }

.step__bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transition: opacity var(--t-med) var(--ease); }
.step::before { content: ""; position: absolute; inset: 0; z-index: 1; background: linear-gradient(180deg, rgba(28, 35, 112, .55), rgba(28, 35, 112, .92)); opacity: 0; transition: opacity var(--t-med); }
.step[aria-expanded="true"] .step__bg { opacity: .55; }
.step[aria-expanded="true"]::before { opacity: 1; }
.step > span { position: relative; z-index: 2; }

.devices__bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-lg); opacity: .35; }
.devices { overflow: visible; }
.cta { position: relative; }
.cta__bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: .12; mix-blend-mode: luminosity; }
.cta > .container { position: relative; }
'''
wr("css/styles.css", css)
print("v3 applied")
