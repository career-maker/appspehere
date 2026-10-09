"""Build the resource pages (gallery, news, retail reality, customer experience, downloads, careers, awards, 404).
Run from the repo root AFTER header/footer changes:  python _src/newpages.py
The head, header, footer and widgets are copied from about.html so every page stays in sync."""
import json, re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
rd = lambda p: open(p, encoding='utf8').read()
tpl = rd('about.html')
head_t, rest = tpl.split('<main id="main">', 1)
tail_t = rest[rest.index('</main>'):]
MARQ = re.search(r'<div class="marquee".*?</div></div></div>', tpl, re.S).group(0)
ARR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
EXT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M8 7h9v9"/></svg>'
TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
DOC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 00-2 2v14a2 2 0 002 2h10a2 2 0 002-2V8zM14 3v5h5M9 13h6M9 17h6"/></svg>'
WA = 'https://wa.me/919778452007?text=Hello%20Source%20Pro%2C%20I%20would%20like%20to%20know%20more.'


def page(fn, title, desc, canon, crumb, h1, lead, art, body, scripts=''):
    h = head_t
    h = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', h)
    h = re.sub(r'(<meta name="description" content=")[^"]*', r'\g<1>' + desc, h)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*', r'\g<1>' + title, h)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*', r'\g<1>' + desc, h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*', r'\g<1>' + canon, h)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*', r'\g<1>' + canon, h)
    hero = (f'<main id="main">\n  <section class="page-hero"><img class="page-hero__art" src="assets/{art}" width="784" height="754" alt="" decoding="async">'
            f'<div class="container"><p><a href="index.html">Source Pro</a> / {crumb}</p><h1>{h1}</h1>{'<p>' + lead + '</p>' if lead else ''}</div></section>\n  {MARQ}\n')
    t = tail_t
    if scripts:
        mm = re.search(r'<script src="js/main\.js(\?v=\w+)?" defer></script>', t)
        v = mm.group(1) or ''
        t = t.replace(mm.group(0), mm.group(0) + '\n' + scripts.replace('.js"', '.js' + v + '"'))
    open(fn, 'w', encoding='utf8', newline='').write(h + hero + body + '\n' + t)
    print('built', fn)


# ---------------- gallery ----------------
GAL = [
    ('gal-current-retailer', 1400, 1050, 'The current retailer: less footfall, more pressure, shrinking margins'),
    ('gal-source-pro-retailer', 1400, 1050, 'Source Pro, the game changer: small store + Source Pro B2B = digital hyper market'),
    ('gal-what-we-are', 1373, 1173, 'Manufacturers, distributors and retailers building one connected ecosystem'),
    ('gal-current-distributor', 1400, 788, 'The current distributor model: more chaos, more burden, less control'),
    ('gal-source-pro-distributor', 1400, 788, 'Source Pro distributor: your business, on autopilot'),
    ('gal-customer', 1373, 1173, 'Customers buying from the neighbourhood shop they already trust'),
    ('gal-vasudhaiva', 1400, 788, 'Vasudhaiva Kutumbakam: the world is one family'),
    ('gal-process', 784, 754, 'A distributor onboarding a retailer in minutes'),
    ('gal-featured', 1024, 576, 'From a small store to a digital hypermarket'),
    ('gal-mission-vision', 1127, 1007, 'People first: building a connected, inclusive India'),
]
items = ''.join(f'<button class="gal__item" type="button"><img src="assets/{n}.webp" width="{w}" height="{h}" alt="{c}" loading="lazy" decoding="async"></button>' for n, w, h, c in GAL)
lb = f'<dialog class="lb" id="lb" aria-label="Image viewer"><div class="lb__in"><img src="" alt=""><p class="lb__cap"></p></div><button class="lb__x" type="button" aria-label="Close">&times;</button><button class="lb__p" type="button" aria-label="Previous image">&#8249;</button><button class="lb__n" type="button" aria-label="Next image">&#8250;</button></dialog>'
page('gallery.html', 'Gallery — Source Pro B2B2C', 'Visualizing the retail revolution: the people, shops and ideas behind Source Pro B2B2C.',
     'https://appsphereb2b.com/gallery/', 'Gallery', 'Gallery',
     'Visualizing the Retail Revolution',
     'partners-handshake.webp', f'<section class="section"><div class="container"><div class="gal">{items}</div></div></section>\n  {lb}',
     '<script src="js/gallery.js" defer></script>')

# ---------------- retail reality ----------------
rr = json.load(open(os.environ['TEMP'] + '/live/rr.json', encoding='utf8'))
cards = ''.join(f'<a class="rr__card" href="{c["href"]}" target="_blank" rel="noopener"><span class="rr__src">{c["src"]}</span><h3>{c["title"]}</h3><p>{c["desc"]}</p><span class="rr__go">Read Article →</span></a>' for c in rr)
page('retail-reality.html', 'Retail Reality — Source Pro B2B2C', 'Media coverage on the challenges faced by India’s traditional retailers, distributors and small businesses.',
     'https://appsphereb2b.com/retail-reality/', 'Retail Reality', 'Retail Reality',
     '',
     'problem-store.webp',
     f'<section class="section"><div class="container"><div class="section-head"><h2>Media Coverage</h2><p>A curated collection of mainstream media reports highlighting the challenges faced by traditional retailers, distributors, and small businesses. These links are shared only for public awareness and industry context. All copyrights belong to the respective publishers.</p></div><div class="rr">{cards}</div><p class="rr-note" style="margin-top:2.5rem">The articles linked on this page are published by independent third-party media organisations. They are shared only for educational, public-awareness, and industry-context purposes. App Sphere B2B India Private Limited does not claim ownership of the content, images, headlines, or trademarks of the respective publishers. If any publisher wishes a link to be removed, we will do so promptly upon request.</p></div></section>')

# ---------------- news ----------------
page('news.html', 'News — Source Pro B2B2C', 'News and reports on how Source Pro B2B2C is empowering India’s traditional retail ecosystem.',
     'https://appsphereb2b.com/news/', 'News', 'News',
     '',
     'cta-handshake.webp',
     f'<section class="section"><div class="container"><div class="section-head"><h2>Media Coverage</h2><p>News and reports highlighting how Source Pro B2B2C is transforming and empowering India\'s traditional retail ecosystem.</p></div><article class="news-feature"><img src="assets/gal-what-we-are.webp" width="1373" height="1173" alt="" loading="lazy" decoding="async"><div><span class="rr__src">Dhanam Online</span><h2>SourcePro B2B: Kerala Startup Brings Digital Power to Small Retailers</h2><p>An in-depth feature by Dhanam Online highlighting how SourcePro B2B is equipping traditional small retailers and neighborhood shops with robust digital tools to compete effectively in a rapidly evolving commerce landscape.</p><a class="btn" href="https://dhanamonline.com/business-kerala/sourcepro-b2b-kerala-startup-brings-digital-power-to-small-retailers-rrn" target="_blank" rel="noopener">Read Full Article →</a></div></article></div></section>')

# ---------------- customer experience ----------------
steps = [('They discover your shop is now digital', 'You contact your existing customers directly through WhatsApp, a shop display, a QR code, social media or word of mouth. They hear about your digital shop from you, not from an algorithm.'),
         ('They browse products from home', 'One free download from the Google Play Store or Apple App Store. Customers explore a wide range of products at their convenience, beyond normal shop hours.'),
         ('They order from a retailer they trust', 'The moment they log in they see your storefront: your shop name, your catalogue and your prices. Not a marketplace with thousands of competing sellers.'),
         ('Online convenience, local support', '25,000+ products with images, descriptions and transparent pricing, available at 10 PM on a Sunday, during a festival or before your shop opens.'),
         ('Better service and local accountability', 'You receive the order, source it from your area distributor and deliver it locally under your own invoice, with payment by UPI or cash.')]
ol = '<ol>' + ''.join(f'<li><span>{i + 1}</span><strong>{t}</strong>{d}</li>' for i, (t, d) in enumerate(steps)) + '</ol>'
gets = [('25,000+ products at their fingertips', 'A catalogue that rivals the biggest e-commerce platforms, through a shop they already know.'),
        ('Credit facility still available', 'Trusted customers continue with the credit arrangements you have always honoured.'),
        ('Competitive pricing, 24/7 ordering', 'Matching or beating major platforms anytime: day, night, weekends and holidays.'),
        ('Personal service, direct accountability', 'Any issue resolved directly with you, immediately, without a helpdesk or chatbot.')]
cx = f'''<section class="section"><div class="container split split--img">
    <div><p>The customer experience</p><h2>Here is what your customer experience looks like.</h2>
      <p>Source Pro B2B2C gives retailers the clarity and confidence to introduce it to their customers in a way that is natural and compelling.</p>
      <p>From the moment customers hear that your shop is now digital to the moment they place their first order, and every order after that, the experience is designed to feel simple, familiar and trustworthy.</p>
      <p>With Source Pro B2B2C, customers do not have to choose between online convenience and neighbourhood trust. They keep buying from the retailer they already know, with the comfort of digital ordering.</p></div>
    <figure class="figure-card"><img src="assets/gal-customer.webp" width="1373" height="1173" alt="A customer and a shopkeeper talking in a neighbourhood store" loading="lazy" decoding="async"></figure>
  </div></section>
  <section class="section on-ink"><div class="container two">
    <div><p>How your customers find you</p><h2>They hear about it from the person they already trust.</h2>
      <p>Your customers will not discover your digital shop through a push notification or a sponsored advertisement. They will hear about it from you: a WhatsApp message to your top 100 regulars, or a mention across the counter the next time they visit.</p></div>
    <div><blockquote>“My shop too is online now — you can order from me anytime through your phone.”</blockquote>
      <p>That is all it takes to get started. The years of trust you have built are, in this moment, more powerful than any marketing budget. Once these customers start ordering and share the experience with neighbours and family, your network grows organically, and it costs you nothing.</p></div>
  </div></section>
  <section class="section"><div class="container">
    <div class="section-head"><p>Step by step</p><h2>From “my shop is online” to every order after.</h2></div>
    {ol}
  </div></section>
  <section class="section on-ink"><div class="container two">
    <div><p>Why they choose you over the giants</p><h2>Trust built over years beats any campaign.</h2>
      <p>If a customer receives the wrong item from a large online platform, they navigate chatbots, support tickets and waiting times. If they receive the wrong item from you, they simply call you and the issue is resolved quickly. Your credit facility continues exactly as it always has.</p>
      <p>Many customers know what is happening to local shops. They want to support you, but they also want the convenience they have grown used to. Source Pro B2B2C gives them both: a guilt-free, easy and genuinely convenient way to shop local every single time.</p></div>
    <div><p>What your customers get</p><h2>Everything they expect, from someone they know.</h2>
      <ul>{''.join(f'<li>{TICK}<span><strong>{t}.</strong> {d}</span></li>' for t, d in gets)}</ul></div>
  </div></section>
  <section class="section"><div class="container" style="text-align:center"><div class="section-head" style="margin-inline:auto"><h2>Ready to take your shop digital?</h2></div>
    <div class="stage__cta" style="justify-content:center"><a class="btn" href="{WA}" target="_blank" rel="noopener">Enquire now on WhatsApp {ARR}</a><a class="btn btn--primary" href="retailer-partnership.html">See the retailer programme</a></div></div></section>'''
page('customer-experience.html', 'Customer Experience — Source Pro B2B2C', 'See how customers discover, browse and order from their trusted local shop with Source Pro B2B2C.',
     'https://appsphereb2b.com/customer-experience/', 'Customer experience', 'The Customer Experience',
     'Here is what your customer experience looks like: simple, familiar and trustworthy from the first message to every order after.',
     'customer-experience-hero.webp', cx)

# ---------------- downloadables ----------------
dl = ''.join(f'<div class="dl__card"><span class="dl__ico">{DOC}</span><h3>{t}</h3><a class="btn" href="{u}">Download PDF {ARR}</a></div>' for t, u in [('B2B2C Mudra Project Report', 'assets/docs/SPB2B2C_Mudra_-Project-Report.pdf'), ('5 Year Financial Projections', 'assets/docs/SPB2B2C_MUDRA_5Y_Fin_Projections.pdf')])
page('downloadables.html', 'Downloadables — Source Pro B2B2C', 'Distributor resources: Mudra loan project report and financial projections for Source Pro distributors.',
     'https://appsphereb2b.com/distributor-resources/', 'Downloadables', 'Distributor Resources', '',
     'distributor-warehouse.webp',
     f'<section class="section"><div class="container"><div class="section-head"><h2>Distributor Finance Support</h2><p>Starting a distribution business may require working capital support. To assist prospective Source Pro distributors, we have made available a downloadable Mudra Loan project report and financial projections.</p><p>Distributors may use these documents while approaching their respective banks for financial assistance. Loan approval will be subject to the eligibility criteria and the discretion of the concerned bank.</p></div><div class="dl">{dl}</div></div></section>')

# ---------------- careers ----------------
page('career.html', 'Careers — Source Pro B2B2C', 'Build inclusive digital commerce with App Sphere B2B India Pvt. Ltd.',
     'https://appsphereb2b.com/career/', 'Careers', 'Build the future of Indian retail',
     'We are always looking for people who believe digital growth must be inclusive, not exclusive.',
     'partners-handshake.webp',
     f'<section class="section"><div class="container split"><div><p>Join the mission</p><h2>Help neighbourhood stores thrive in the digital era.</h2><p>App Sphere B2B India Private Limited is based in Kerala and works with distributors, retailers and manufacturers across India. If our mission speaks to you, we would like to hear from you.</p></div><div><p>How to apply</p><p>There are no listed openings at the moment. Send your CV and a short note about the role you have in mind to <a href="mailto:info@appsphereb2b.com">info@appsphereb2b.com</a>, or message us on WhatsApp.</p><p><a class="btn" href="{WA}" target="_blank" rel="noopener">Message us on WhatsApp {ARR}</a></p></div></div></section>')

# ---------------- awards ----------------
page('awards.html', 'Awards & Recognitions — Source Pro B2B2C', 'Press recognition and milestones for Source Pro B2B2C.',
     'https://appsphereb2b.com/awards-recognitions/', 'Awards &amp; Recognitions', 'Awards &amp; Recognitions',
     'Recognition from the press and the retail community for Source Pro B2B2C.',
     'ecosystem-india.webp',
     f'<section class="section"><div class="container"><div class="section-head"><h2>Media Coverage</h2><p>News and reports highlighting how Source Pro B2B2C is transforming and empowering India\'s traditional retail ecosystem.</p></div><article class="news-feature"><img src="assets/gal-mission-vision.webp" width="1127" height="1007" alt="" loading="lazy" decoding="async"><div><span class="rr__src">In the press</span><h2>Featured by Dhanam Online</h2><p>SourcePro B2B was profiled as a Kerala startup bringing digital power to small retailers. More awards and recognitions will be listed here as they are announced.</p><a class="btn" href="news.html">See media coverage {ARR}</a></div></article></div></section>')

# ---------------- 404 ----------------
page('404.html', 'Page not found — Source Pro B2B2C', 'The page you are looking for could not be found.', 'https://appsphereb2b.com/', 'Not found', 'Page not found',
     'The page you are looking for does not exist or has moved.', 'problem-store.webp',
     '<section class="section"><div class="container" style="text-align:center"><p class="stage__cta" style="justify-content:center"><a class="btn" href="index.html">Back to home</a><a class="btn btn--primary" href="contact.html">Contact us</a></p></div></section>')

# ---------------- distributor registration ----------------
STATES = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']


def field(i, label, t='text', req=True, ac='', ph=''):
    return (f'<div class="sp-field"><label for="{i}">{label}{" <span>*</span>" if req else ""}</label>'
            f'<input id="{i}" name="{i}" type="{t}"{" required" if req else ""}{f" autocomplete=%s{ac}%s" % (chr(34), chr(34)) if ac else ""}'
            f'{f" placeholder=%s{ph}%s" % (chr(34), chr(34)) if ph else ""}></div>')


def select(i, label, opts, placeholder):
    o = f'<option value="">{placeholder}</option>' + ''.join(f'<option>{x}</option>' for x in opts)
    return f'<div class="sp-field"><label for="{i}">{label} <span>*</span></label><select id="{i}" name="{i}" required>{o}</select></div>'


dreg = f'''<section class="form-wrap" id="register"><div class="container">
  <form class="sp-infra-form" data-wa="Hello Source Pro, I would like to apply as a distributor." novalidate>
    <div class="sp-form-section">
      <h2>Distributor application</h2>
      <p>Tell us about yourself and the territory you are interested in. The Source Pro team will review your application and contact you.</p>
      <div class="sp-status" role="alert" tabindex="-1"></div>
      <div class="sp-form-grid">
        {field("dname", "Full name", ac="name")}
        {field("dfirm", "Firm / business name", ac="organization")}
        {field("demail", "Email address", "email", ac="email")}
        {field("dphone", "Mobile number", "tel", ac="tel", ph="+91")}
        {select("dstate", "State", STATES, "Select your state")}
        {field("ddistrict", "District")}
        {field("dterritory", "Preferred territory / constituency")}
        {select("dexp", "Distribution experience", ["No prior experience", "1 to 3 years", "3 to 10 years", "More than 10 years"], "Select experience")}
      </div>
      <button type="submit" class="sp-submit-btn">Submit on WhatsApp</button>
    </div>
  </form></div></section>'''
page('distributor-registration.html', 'Distributor Registration — Source Pro B2B2C', 'Apply to become a Source Pro B2B2C distributor in your territory.',
     'https://appsphereb2b.com/distributor-registration/', 'Distributor registration', 'Become a Source Pro distributor',
     'Zero warehouse investment, zero stock holding and no inventory risk. Apply for an available seat or join the waiting list for your territory.',
     'distributor-warehouse.webp', dreg, '<script src="js/reg-form.js" defer></script>')
