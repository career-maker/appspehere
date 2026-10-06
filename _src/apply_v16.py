import os
import re

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
s = open("_src/index.src.html", encoding="utf8").read()

thumbs = [
    ("problem-store", "50% 40%", "A traditional store shelf", ""),
    ("digital-hypermarket", "50% 50%", "A digital catalogue of products", ""),
    ("digital-hypermarket", "78% 40%", "A digital hypermarket", '<span class="story__thumb-num">25,000+</span>'),
    ("ecosystem-india", "88% 55%", "A family ordering from their trusted local shop", ""),
    ("distributor-warehouse", "50% 50%", "Orders prepared for local fulfilment", ""),
]
for i, (img, pos, alt, extra) in enumerate(thumbs):
    pat = re.compile(r'(<li class="story__step[^"]*" data-s="%d">)(?!<figure)' % i)
    fig = '<figure class="story__thumb"><img src="assets/%s.webp" alt="%s" style="object-position:%s" loading="lazy" decoding="async">%s</figure>' % (img, alt, pos, extra)
    s, n = pat.subn(lambda m: m.group(1) + fig, s, count=1)
    assert n == 1, i

if 'class="story__dots"' not in s:
    s = s.replace('      <ol class="story__steps">', '      <ol class="story__steps" id="story-steps">', 1)
    # dots after the ol (inside .story)
    j = s.index('id="story-steps"')
    k = s.index("</ol>", j) + 5
    dots = '\n      <div class="story__dots" aria-hidden="true"><i class="is-active"></i><i></i><i></i><i></i><i></i></div>'
    s = s[:k] + dots + s[k:]
open("_src/index.src.html", "w", encoding="utf8").write(s)

css = open("css/styles.css", encoding="utf8").read()
css += '''
/* ===== v16: digital hypermarket — mobile carousel ===== */
.story__thumb, .story__dots { display: none; }
@media (max-width: 860px) {
  .story { display: block; }
  .story__sticky { display: none; }
  .story__steps { display: flex; gap: .9rem; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; margin-inline: calc(-1 * var(--gutter)); padding-inline: var(--gutter); padding-bottom: .5rem; scrollbar-width: none; overscroll-behavior-x: contain; }
  .story__steps::-webkit-scrollbar { display: none; }
  .story__step { flex: 0 0 min(84vw, 22rem); min-height: 0; scroll-snap-align: center; opacity: 1; background: rgba(255, 255, 255, .06); border: 1px solid var(--color-ink-border); border-radius: var(--radius-lg); overflow: hidden; padding: 0 0 1.4rem; justify-content: flex-start; }
  .story__step.is-active { opacity: 1; }
  .story__thumb { display: block; position: relative; margin: 0 0 1.1rem; aspect-ratio: 16/11; overflow: hidden; }
  .story__thumb img { width: 100%; height: 100%; object-fit: cover; }
  .story__thumb::after { content: ""; position: absolute; inset: 0; background: linear-gradient(0deg, rgba(15, 21, 71, .7), transparent 55%); }
  .story__thumb-num { position: absolute; z-index: 2; inset: 0; display: grid; place-items: center; font-family: var(--font-display); font-weight: 800; font-size: 2.6rem; color: var(--color-accent); text-shadow: 0 6px 24px rgba(0, 0, 0, .7); }
  .story__step .n, .story__step h3, .story__step p, .story__step .cat-list { margin-inline: 1.2rem; }
  .story__step .n { display: block; }
  .story__step h3 { font-size: 1.45rem; margin-block: .35rem .6rem; }
  .story__step p { font-size: 1rem; }
  .story__step .cat-list { margin-top: .8rem; gap: .35rem; }
  .story__step .cat-list .chip { font-size: .72rem; padding: .2rem .55rem; }
  .story__dots { display: flex; justify-content: center; gap: .45rem; margin-top: 1rem; }
  .story__dots i { width: .5rem; height: .5rem; border-radius: 999px; background: var(--color-ink-border); transition: width var(--t-med) var(--ease), background var(--t-fast); }
  .story__dots i.is-active { width: 1.6rem; background: var(--color-accent); }
}
'''
open("css/styles.css", "w", encoding="utf8").write(css)

js = open("js/home.js", encoding="utf8").read()
if "story__dots" not in js:
    js = js.replace("  /* ---------- sticky story steps ---------- */", '''  /* ---------- digital hypermarket: dots follow the mobile carousel ---------- */
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

  /* ---------- sticky story steps ---------- */''', 1)
    open("js/home.js", "w", encoding="utf8").write(js)
print("v16 applied")
