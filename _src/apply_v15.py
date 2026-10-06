import os
from PIL import Image

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
im = Image.open(r"D:/downloads/B2B Retail App Hero Collage.png").convert("RGBA")
for n, w in [("solution-collage", 1400), ("solution-collage-700", 700)]:
    r = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    r.save("assets/%s.webp" % n, quality=86, method=6, exact=True)

s = open("_src/index.src.html", encoding="utf8").read()
i = s.index('id="solution"')
a = s.rindex("<section", 0, i)
b = s.index("</section>", i) + 10


def ic(p):
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % p


new = '''<section class="section on-ink solution" id="solution" aria-labelledby="solution-h">
  <div class="container solution__grid">
    <div class="solution__text">
      <p class="eyebrow">The Source Pro solution</p>
      <h2 id="solution-h" data-reveal>Zero compromise <span class="grad">on livelihoods.</span></h2>
      <p class="lead">Source Pro B2B2C is a mobile-application-based digital commerce ecosystem created to empower India's traditional retailers, distributors, manufacturers and end customers.</p>
      <ul class="roles4">
        <li><span class="roles4__ico roles4__ico--g">%s</span><strong>For<br>Retailers</strong><span>Sell more without increasing stock</span></li>
        <li><span class="roles4__ico roles4__ico--b">%s</span><strong>For<br>Distributors</strong><span>Zero-stock digital distribution</span></li>
        <li><span class="roles4__ico roles4__ico--p">%s</span><strong>For<br>Manufacturers</strong><span>Reach every retailer in the region</span></li>
        <li><span class="roles4__ico roles4__ico--o">%s</span><strong>For<br>End Customers</strong><span>Order from the shop you trust</span></li>
      </ul>
      <ul class="zero-strip" aria-label="Source Pro promise"><li><b>Zero</b> investment</li><li><b>Zero</b> disruption</li><li><b>Zero</b> compromise on livelihoods</li></ul>
      <p class="vision">Digital growth must be inclusive, not exclusive.</p>
    </div>
    <figure class="solution__fig"><img src="assets/solution-collage.webp" srcset="assets/solution-collage-700.webp 700w, assets/solution-collage.webp 1400w" sizes="(max-width: 900px) 100vw, 55vw" width="1400" height="788" alt="A shopkeeper using the Source Pro B2B app, with the app showing categories and connected icons for ordering, delivery, analytics and stock" loading="lazy" decoding="async"></figure>
  </div>
</section>''' % (
    ic('<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M3 4h2.5l2.2 11h10.600l2-8H6.500"/>'),
    ic('<path d="M12 3l8 4.500v9L12 21l-8-4.500v-9z"/><path d="M4 7.500l8 4.500 8-4.500M12 12v9"/>'),
    ic('<path d="M3 21V9l6 4V9l6 4V4h6v17z"/>'),
    ic('<circle cx="9" cy="8" r="3.500"/><path d="M2.500 20c0-3.500 3-5.500 6.500-5.500s6.500 2 6.500 5.500"/><circle cx="17" cy="9" r="2.500"/><path d="M17 14c2.500 0 4.500 1.500 4.500 4.500"/>'))
open("_src/index.src.html", "w", encoding="utf8").write(s[:a] + new + s[b:])

css = open("css/styles.css", encoding="utf8").read()
css += open("_src/v15.css", encoding="utf8").read()
open("css/styles.css", "w", encoding="utf8").write(css)
print("v15 applied")
