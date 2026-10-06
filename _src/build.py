"""Assemble static pages from partials. Run: python _src/build.py"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(ROOT, "_src")
rd = lambda n: open(os.path.join(S, n), encoding="utf8").read()

header_t, footer_t = rd("header.html"), rd("footer.html")
widgets_t = rd("widgets.html")
TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'


def header(prefix, home=False, dist=False, infra=False, solid=True):
    cur = 'aria-current="page"'
    return (header_t.replace("{{P}}", prefix).replace("{{HCLASS}}", "header--solid" if solid else "")
            .replace("{{CUR_HOME}}", cur if home else "").replace("{{CUR_DIST}}", cur if dist else "")
            .replace("{{CUR_INFRA}}", cur if infra else ""))


def footer(prefix):
    return footer_t.replace("{{P}}", prefix) + widgets_t.replace("{{P}}", prefix)


HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0f1547">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Source Pro B2B2C">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300;12..96,600;12..96,700;12..96,800&family=Manrope:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""

# ---------- index ----------
idx = rd("index.src.html")
idx = idx.replace("{{HEADER}}", header("", home=True, solid=False)).replace("{{FOOTER}}", footer("")).replace("{{TICK}}", TICK)
open(os.path.join(ROOT, "index.html"), "w", encoding="utf8").write(idx)

# ---------- infrastructure partner ----------
form = rd("infra-form.fragment.html")
infra = HEAD.format(
    title="Partner With Source Pro B2B2C — Warehouses, Land & Vehicles",
    desc="Warehouse owners, landowners, infrastructure partners and vehicle owners: support Source Pro's digital retail distribution network across South India and Maharashtra.",
    canon="https://appsphereb2b.com/infrastructure-partner/") + header("", infra=True) + """
<main id="main">
  <section class="page-hero">
    <img class="page-hero__art" src="assets/distributor-warehouse.webp" width="784" height="754" alt="" decoding="async">
    <div class="container">
      <p class="crumbs"><a href="index.html">Source Pro</a> / Partnership</p>
      <h1>Partner With Source Pro B2B2C</h1>
      <p>We invite warehouse owners, landowners, infrastructure partners, and vehicle owners to support our digital retail distribution network across South India and Maharashtra.</p>
    </div>
  </section>
  <section class="form-wrap">
    <div class="container form-layout">
      <aside class="form-aside" aria-label="About this form">
        <h2>How this works</h2>
        <ol>
          <li>Choose your state, district and what you can offer.</li>
          <li>Share your details and the specifics of your property or vehicle.</li>
          <li>Confirm and submit. The team may verify and get in touch.</li>
        </ol>
        <p class="muted" style="font-size:.85rem">Fields marked <span style="color:var(--color-error)">*</span> are required.</p>
      </aside>
      <div>
        <div id="spStatus" class="sp-status" role="alert" tabindex="-1"></div>
""" + form + """
      </div>
    </div>
  </section>
</main>
""" + footer("") + """
<script src="js/main.js" defer></script>
<script src="js/infra-form.js" defer></script>
</body>
</html>
"""
open(os.path.join(ROOT, "partner-infrastructure.html"), "w", encoding="utf8").write(infra)

# ---------- distributors ----------
dist = HEAD.format(
    title="Meet Our Local Distribution Partners — Source Pro B2B2C",
    desc="Source Pro B2B2C is building a constituency-wise distributor network. Select your state and district to view onboarded distributors and available distributor seats.",
    canon="https://appsphereb2b.com/meet-our-distributors/") + header("", dist=True) + """
<main id="main">
  <section class="page-hero">
    <img class="page-hero__art" src="assets/partners-handshake.webp" width="784" height="754" alt="" decoding="async">
    <div class="container">
      <p class="crumbs"><a href="index.html">Source Pro</a> / Distributor network</p>
      <h1>Meet Our Local Distribution Partners</h1>
      <p>Source Pro B2B2C is building a constituency-wise distributor network across multiple states. Select your state and district to view onboarded distributors and available distributor seats.</p>
    </div>
  </section>
  <section class="form-wrap">
    <div class="container">
<div class="sp-distributor-network">
  <section class="sp-filter-section" aria-label="Choose location">
    <div class="sp-filter-field">
      <label for="spState">Select State</label>
      <select id="spState">
        <option value="">Select State</option>
        <option value="Kerala">Kerala</option>
        <option value="Tamil Nadu">Tamil Nadu</option>
        <option value="Karnataka">Karnataka</option>
        <option value="Andhra Pradesh">Andhra Pradesh</option>
        <option value="Telangana">Telangana</option>
        <option value="Maharashtra">Maharashtra</option>
      </select>
    </div>

    <div class="sp-filter-field">
      <label for="spDistrict">Select District</label>
      <select id="spDistrict" disabled>
        <option value="">Select District</option>
      </select>
    </div>
  </section>

  <section id="spDistrictSummary" class="sp-summary-section" style="display:none;" aria-live="polite">
    <h2 id="spDistrictTitle"></h2>

    <div class="sp-summary-grid">
      <div class="sp-summary-card">
        <strong id="spTotalConstituencies">0</strong>
        <span>Total Constituencies</span>
      </div>

      <div class="sp-summary-card">
        <strong id="spTotalSeats">0</strong>
        <span>Planned Distributor Seats</span>
      </div>

      <div class="sp-summary-card">
        <strong id="spOnboardedSeats">0</strong>
        <span>Onboarded Distributors</span>
      </div>

      <div class="sp-summary-card">
        <strong id="spAvailableSeats">0</strong>
        <span>Available Seats</span>
      </div>
    </div>
  </section>

  <section id="spConstituencyOutput" class="sp-constituency-output" aria-live="polite"></section>
</div>
    </div>
  </section>
</main>
""" + footer("") + """
<script src="js/main.js" defer></script>
<script src="js/distributors.js" defer></script>
</body>
</html>
"""
open(os.path.join(ROOT, "distributors.html"), "w", encoding="utf8").write(dist)
exec(open(os.path.join(S, "pages.py"), encoding="utf8").read())
print("built")
