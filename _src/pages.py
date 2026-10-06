"""Generates about / blog / post / contact / retailer / distributor / manufacturer pages.
Executed from build.py (shares HEAD, header(), footer(), ROOT)."""
import json
import os
from html import escape as esc

FAQ = json.load(open(os.path.join(S, "faq.json"), encoding="utf8"))
WA = "https://wa.me/919778452007"


def wa(text):
    from urllib.parse import quote
    return WA + "?text=" + quote(text)


ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'


def img(name, alt, w, h, cls="", lazy=True):
    return '<img %ssrc="assets/%s.webp" width="%d" height="%d" alt="%s"%s decoding="async">' % (
        ('class="%s" ' % cls) if cls else "", name, w, h, esc(alt), ' loading="lazy"' if lazy else "")


def ticks(items):
    return '<ul class="ticks ticks--one">' + "".join("<li>%s%s</li>" % (CHECK, esc(i)) for i in items) + "</ul>"


def faq_html(key):
    out = ['<div class="faq__list">']
    for n, item in enumerate(FAQ[key]):
        body = ""
        lis = [t for k, t in item["a"] if k == "li"]
        for k, t in item["a"]:
            if k == "p":
                body += "<p>%s</p>" % esc(t)
        if lis:
            body += "<ul>" + "".join("<li>%s</li>" % esc(t) for t in lis) + "</ul>"
        out.append('<details%s><summary>%s<i aria-hidden="true"></i></summary><div class="faq__a">%s</div></details>' % (
            " open" if n == 0 else "", esc(item["q"]), body))
    out.append("</div>")
    return "".join(out)


def hero(crumb, h1, lead, art, alt, ctas=""):
    return """
  <section class="page-hero page-hero--photo">
    <div class="container page-hero__grid">
      <div>
        <p class="crumbs"><a href="index.html">Source Pro</a> / %s</p>
        <h1>%s</h1>
        <p>%s</p>
        %s
      </div>
      <figure class="page-hero__fig">%s</figure>
    </div>
  </section>""" % (crumb, h1, lead, ('<div class="stage__cta">%s</div>' % ctas) if ctas else "", img(art, alt, 789, 855, lazy=False))


def page(fname, title, desc, canon, body, scripts="", nav=None):
    nav = nav or {}
    html = HEAD.format(title=title, desc=desc, canon=canon) + header("", **nav) + '\n<main id="main">' + body + "\n</main>\n" + footer("") + \
        '\n<script src="js/main.js" defer></script>\n' + scripts + "</body>\n</html>\n"
    open(os.path.join(ROOT, fname), "w", encoding="utf8").write(html)


def cta_band(text, sub, extra=""):
    return """
  <section class="section on-ink cta-band">
    <div class="container cta-band__in">
      <div><p class="eyebrow">Next step</p><h2>%s</h2><p class="lead">%s</p></div>
      <div class="stage__cta"><a class="btn" href="%s" target="_blank" rel="noopener">Enquire now on WhatsApp %s</a>%s</div>
    </div>
  </section>""" % (text, sub, wa("Hello Source Pro, I would like to know more."), ARROW, extra)


# ======================= ABOUT =======================
about = hero("About", "About Source Pro B2B2C",
             "We are not just building another technology platform. We are building a digital empowerment ecosystem for India's traditional retail economy — one that protects livelihoods, preserves relationships, and helps local businesses compete in a changing market.",
             "about-hero", "A smiling Kirana store owner in his shop") + """
  <section class="section"><div class="container split">
    <div><p class="eyebrow">Who we are</p><h2 class="h2">A platform founded in Kerala, built for India.</h2>
      <p class="lead">App Sphere B2B India Private Limited operates Source Pro B2B2C, founded and headquartered in Kerala. The platform enables kirana stores, local retailers, distributors, and manufacturers to participate in digital commerce while preserving existing business relationships.</p></div>
    <div><p class="eyebrow">The story behind Source Pro B2B2C</p>
      <p class="lead">Neighbourhood stores have historically provided credit, employment, and relationships, but now face pressure from digital ordering expectations and quick-commerce platforms. Source Pro B2B2C aims to strengthen — not replace — traditional retail with the digital infrastructure it needs.</p></div>
  </div></section>
  <section class="section on-ink"><div class="container">
    <div class="section-head"><p class="eyebrow">Mission, vision &amp; goal</p><h2>Technology that strengthens communities.</h2></div>
    <div class="mvg">
      <article><h3>Mission</h3><p>Empower traditional kirana stores, distributors, and manufacturers in India with zero-investment digital tools enabling competition and growth while maintaining identity and community relationships.</p></article>
      <article><h3>Vision</h3><p>A Digital India where every neighbourhood shop functions as a digital hypermarket, with technology strengthening rather than replacing communities.</p></article>
      <article><h3>Goal</h3><p>Build a structured digital retail ecosystem enabling millions of retailers and entrepreneurs to increase sales, formalize businesses, and contribute to the economy — targeting 10 million digitally empowered income earners.</p></article>
    </div></div></section>
  <section class="section"><div class="container">
    <div class="section-head"><p class="eyebrow">Core values</p><h2>What we stand for.</h2></div>
    <div class="values"><div><strong>01</strong>Inclusion First</div><div><strong>02</strong>Community Before Commerce</div><div><strong>03</strong>Trust as Currency</div><div><strong>04</strong>Business With a Conscience</div></div>
  </div></section>
  <section class="section on-ink philosophy" style="text-align:left"><div class="container">
    <p class="eyebrow">Founder's message</p>
    <figure><blockquote style="margin:0;font-family:var(--font-display);font-weight:600;font-size:clamp(1.5rem,1rem+2.4vw,3rem);line-height:1.12;max-width:44rem">“The future of retail must not only be digital — it must also remain <span style="color:var(--color-accent)">human</span>.”</blockquote>
    <figcaption style="margin-top:1.25rem"><strong>Jaideep Oommen</strong><br><span class="muted">Founder Director &amp; CEO</span></figcaption></figure>
    <p class="lead" style="margin-top:2rem">India's retail is undergoing massive transformation. Traditional retailers face displacement by billion-dollar corporations, but the solution isn't choosing between technology and tradition — it's creating bridges that enable digital inclusion without displacement.</p>
  </div></section>
  <section class="section"><div class="container">
    <div class="section-head"><p class="eyebrow">Core team</p><h2>The people behind it.</h2></div>
    <ul class="team">
      <li><strong>Jaideep Oommen</strong><span>Founder Director &amp; CEO</span></li>
      <li><strong>Sunija Jaideep</strong><span>Co-Founder Director</span></li>
      <li><strong>Ajay Joseph K</strong><span>Director</span></li>
      <li><strong>Shubham Bhartiya</strong><span>Director, CTO</span></li>
      <li><strong>Shrey Singh</strong><span>Director, CPO</span></li>
    </ul>
  </div></section>""" + cta_band("Be part of the ecosystem.", "Retailers, distributors, manufacturers — find your place in Source Pro.",
                                 '<a class="btn btn--ghost" href="index.html#roles">Find where you belong</a>')
page("about.html", "About Source Pro B2B2C — App Sphere B2B India Pvt. Ltd.",
     "Source Pro B2B2C is a digital empowerment ecosystem for India's traditional retail economy, founded and headquartered in Kerala.",
     "https://appsphereb2b.com/about-us/", about)

# ======================= BLOG =======================
POST_SLUG = "kirana-stores.html"
POST_URL = "https%3A%2F%2Fappsphereb2b.com%2Findia-cannot-afford-to-lose-kirana-stores%2F"
POST_TITLE = "Why%20India%20Cannot%20Afford%20to%20Lose%20Its%20Kirana%20Stores"


def share():
    return ('<div class="share" aria-label="Share this article"><span>Share</span>'
            '<a href="https://www.facebook.com/sharer/sharer.php?u=' + POST_URL + '" target="_blank" rel="noopener" aria-label="Share on Facebook"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5H16l.5-3h-3V8.6c0-.9.3-1.6 1.6-1.6h1.500V4.300c-.3 0-1.200-.1-2.300-.1-2.300 0-3.800 1.400-3.800 3.900v2.400H8v3h2.500V21z"/></svg></a>'
            '<a href="https://wa.me/?text=' + POST_TITLE + '%20' + POST_URL + '" target="_blank" rel="noopener" aria-label="Share on WhatsApp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 20l1.200-4A8 8 0 118 19z"/></svg></a>'
            '<a href="https://www.linkedin.com/sharing/share-offsite/?url=' + POST_URL + '" target="_blank" rel="noopener" aria-label="Share on LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M5 9h3v10H5zM6.500 4.500a1.700 1.700 0 110 3.400 1.700 1.700 0 010-3.400zM10 9h2.900v1.400c.5-.9 1.600-1.600 3.100-1.600 3 0 3.600 2 3.600 4.600V19h-3v-5c0-1.200 0-2.600-1.600-2.600S13 12.700 13 14v5h-3z"/></svg></a>'
            '<a href="https://twitter.com/intent/tweet?url=' + POST_URL + '&amp;text=' + POST_TITLE + '" target="_blank" rel="noopener" aria-label="Share on X"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.500 4h2.800l-6.100 7 7.200 9h-5.600l-4.400-5.500L6.300 20H3.500l6.500-7.500L3.100 4h5.700l4 5.100zM16.500 18.300h1.500L8.500 5.600H6.900z"/></svg></a></div>')


SIDEBAR = ('<aside class="sidebar" aria-label="Blog sidebar">'
           '<section class="widget"><h2>Search</h2><form class="widget-search" role="search" onsubmit="return false"><label class="sr-only" for="bs">Search articles</label><input id="bs" type="search" placeholder="Search articles…" autocomplete="off"><button type="submit" aria-label="Search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="6.500"/><path d="M16 16l4 4"/></svg></button></form></section>'
           '<section class="widget"><h2>Recent posts</h2><ul class="recent"><li><a href="kirana-stores.html">' + img("problem-store", "", 120, 115) + '<span><strong>Why India Cannot Afford to Lose Its Kirana Stores</strong><small>June 29, 2026</small></span></a></li></ul></section>'
           '<section class="widget"><h2>Categories</h2><ul class="cats"><li><a href="blog.html">Retailer Empowerment <span>1</span></a></li></ul></section>'
           '<section class="widget widget--cta"><h2>Join Source Pro</h2><p>Retailer, distributor or manufacturer — find your place in India\'s connected retail ecosystem.</p>'
           '<a class="btn btn--sm" href="retailer-partnership.html">Retailer partnership</a><a class="btn btn--sm btn--ghost" href="distributor-partnership.html">Become a distributor</a><a class="btn btn--sm btn--ghost" href="manufacturer-partnership.html">List your products</a></section>'
           '<section class="widget"><h2>Get in touch</h2><ul class="mini-contact"><li><a href="tel:+919778452007">+91 97784 52007</a></li><li><a href="mailto:info@appsphereb2b.com">info@appsphereb2b.com</a></li><li><a href="contact.html">Contact page →</a></li></ul></section>'
           '</aside>')

blog = ('<section class="page-hero page-hero--banner"><img class="page-hero__art" src="assets/problem-kirana.webp" width="1400" height="933" alt="" decoding="async"><div class="container">'
        '<p class="crumbs"><a href="index.html">Home</a> / Blog</p><h1>Insights</h1>'
        '<p>Perspectives on India\'s kirana stores, distribution and the people who keep local commerce running.</p></div></section>'
        '<section class="section"><div class="container blog-layout"><div class="blog-grid">'
        '<article class="blog-card"><a class="blog-card__img" href="' + POST_SLUG + '" tabindex="-1" aria-hidden="true">' + img("problem-kirana", "A worried Kirana store owner checking his phone", 1400, 933) + '</a>'
        '<div class="blog-card__body"><p class="meta"><span class="cat">Retailer Empowerment</span><time datetime="2026-06-29">June 29, 2026</time></p>'
        '<h2><a href="' + POST_SLUG + '">Why India Cannot Afford to Lose Its Kirana Stores</a></h2>'
        '<p>India\'s neighbourhood stores are more than retail outlets. They are part of the country\'s social and economic fabric. For generations, kirana stores, stationer…</p>'
        '<a class="link-arrow" href="' + POST_SLUG + '">View more ' + ARROW + '</a></div></article></div>' + SIDEBAR + '</div></section>')
page("blog.html", "Insights — Source Pro B2B2C Blog", "Articles from Source Pro B2B2C on India's kirana stores, distribution and digital retail.",
     "https://appsphereb2b.com/blog/", blog)

post = ('<section class="page-hero page-hero--banner"><div class="container">'
        '<p class="crumbs"><a href="index.html">Home</a> / <a href="blog.html">Insights</a> / Why India Cannot Afford to Lose Its Kirana Stores</p>'
        '<h1 style="max-width:22ch">Why India Cannot Afford to Lose Its Kirana Stores</h1>'
        '<p class="meta meta--hero"><span class="cat">Retailer Empowerment</span><span>By Source Pro Editorial Team</span><time datetime="2026-06-29">June 29, 2026</time></p></div></section>'
        '<section class="section"><div class="container blog-layout"><article class="article"><figure>' + img("problem-store", "A shopkeeper waiting behind the counter of his traditional store", 784, 754, lazy=False) + '</figure>' + share() +
        '''<p class="lead">India's neighbourhood stores represent more than commercial spaces — they form part of the nation's social and economic infrastructure. For many decades, kirana stores and small retailers have sustained families, created local jobs, offered credit based on trust, and delivered community services with personal connections that large corporations cannot replicate.</p>
<p>However, consumer expectations have evolved. Modern shoppers seek convenience through digital platforms, expanded product availability, rapid delivery, and better value. This transformation is significant, and traditional retailers must acknowledge and adapt to this reality. Yet India cannot permit millions of small business owners to become obsolete simply due to technological barriers.</p>
<h2>The path forward</h2>
<p>The path forward involves digitally transforming neighbourhood retailers rather than eliminating them.</p>
<p>A technologically advanced kirana store can preserve its local brand identity while offering digital ordering capabilities, expanded inventory options, and improved operational systems. It can maintain community ties and personal relationships while remaining competitive in contemporary markets.</p>
<p>Source Pro B2B2C operates from this principle: technology should enhance rather than destroy economic livelihoods. When small retailers embrace digital solutions, local commerce thrives, communities maintain cohesion, and India's retail sector becomes more equitable.</p>
<blockquote>India requires not fewer retailers, but better-equipped, digitally-enabled neighbourhood shops.</blockquote>
<nav class="post-nav" aria-label="Post navigation"><a class="link-arrow" href="blog.html">← Back to all insights</a></nav></article>''' + SIDEBAR + '</div></section>')
page(POST_SLUG, "Why India Cannot Afford to Lose Its Kirana Stores — Source Pro Insights",
     "Why India cannot afford to lose its kirana stores — and how digital transformation can strengthen, not replace, neighbourhood retail.",
     "https://appsphereb2b.com/india-cannot-afford-to-lose-kirana-stores/", post)

# ======================= CONTACT =======================
contact = """
  <section class="page-hero page-hero--photo"><div class="container page-hero__grid">
    <div><p class="crumbs"><a href="index.html">Source Pro</a> / Contact</p>
    <h1>Contact us</h1>
    <p>For the people. By the distributor. Through the retailer.</p></div>
    <figure class="page-hero__fig">%s</figure>
  </div></section>
  <section class="section"><div class="container contact">
    <div class="contact__info">
      <p class="eyebrow">Get in touch</p>
      <h2 class="h2">Talk to the Source Pro team.</h2>
      <ul class="contact-list">
        <li><strong>Address</strong>App Sphere B2B India Private Limited, CSP XXI/271-F, 1st Floor, Emmanuel George Memorial Building, Champakkad Jn, Arthunkal PO, Cherthala, Alappuzha, Kerala – 688530</li>
        <li><strong>Hours</strong>Monday to Saturday, 9:00 AM – 6:00 PM IST</li>
        <li><strong>Phone</strong><a href="tel:+919778452007">+91 97784 52007</a><br><a href="tel:+914782572486">+91 4782 572486</a><br><a href="tel:18008907576">1800-890-7576</a></li>
        <li><strong>Email</strong><a href="mailto:info@appsphereb2b.com">info@appsphereb2b.com</a><br><a href="mailto:info@sourceprob2b.co.in">info@sourceprob2b.co.in</a></li>
      </ul>
      <div class="partner-links"><a class="link-card link-card--sm" href="retailer-partnership.html"><h3>Retailer</h3><span class="link-arrow">Stock direct %s</span></a><a class="link-card link-card--sm" href="distributor-partnership.html"><h3>Distributor</h3><span class="link-arrow">Secure a territory %s</span></a><a class="link-card link-card--sm" href="manufacturer-partnership.html"><h3>Manufacturer</h3><span class="link-arrow">List products %s</span></a></div>
    </div>
    <form class="sp-infra-form contact__form" id="contactForm" novalidate>
      <div class="sp-form-section">
        <h2>Send an enquiry</h2>
        <div id="cStatus" class="sp-status" role="alert" tabindex="-1"></div>
        <div class="sp-form-grid">
          <div class="sp-field"><label for="cName">Full name <span>*</span></label><input id="cName" name="name" type="text" required autocomplete="name"></div>
          <div class="sp-field"><label for="cEmail">Email address <span>*</span></label><input id="cEmail" name="email" type="email" required autocomplete="email"></div>
          <div class="sp-field"><label for="cPhone">Mobile number <span>*</span></label><input id="cPhone" name="phone" type="tel" placeholder="+91" required autocomplete="tel"></div>
          <div class="sp-field"><label for="cSubject">Subject <span>*</span></label><input id="cSubject" name="subject" type="text" required></div>
          <div class="sp-field sp-full"><label for="cMsg">Message <span>*</span></label><textarea id="cMsg" name="message" rows="5" required></textarea></div>
        </div>
        <p class="sp-form-note" style="margin-bottom:1rem">Sending opens WhatsApp with your message ready to send to +91 97784 52007.</p>
        <button type="submit" class="sp-submit-btn">Send on WhatsApp</button>
      </div>
    </form>
  </div></section>""" % (img("contact-hero", "A Source Pro team member discussing with a visitor", 784, 754, lazy=False), ARROW, ARROW, ARROW)
contact_js = """<script>
(function(){
  var f=document.getElementById('contactForm'),st=document.getElementById('cStatus');
  function wrap(el){return el.closest('.sp-field');}
  function err(el,msg){var w=wrap(el),e=w.querySelector('.sp-error');if(!e){e=document.createElement('p');e.className='sp-error';e.setAttribute('role','alert');w.appendChild(e);}
    w.classList.toggle('has-error',!!msg);e.textContent=msg||'';el.toggleAttribute('aria-invalid',!!msg);}
  function check(el){if(el.checkValidity()){err(el,'');return true;}err(el,el.validity.valueMissing?'This field is required.':'Enter a valid '+(el.type==='email'?'email address.':'value.'));return false;}
  f.addEventListener('input',function(e){if(wrap(e.target).classList.contains('has-error'))check(e.target);});
  f.addEventListener('submit',function(e){e.preventDefault();
    var bad=[].filter.call(f.querySelectorAll('input,textarea'),function(el){return !check(el);});
    if(bad.length){st.className='sp-status sp-status--error is-visible';st.textContent='Please fix '+bad.length+' field'+(bad.length>1?'s':'')+' before sending.';bad[0].focus();return;}
    var v=function(n){return f.elements[n].value.trim();};
    var text='Hello Source Pro,\\nName: '+v('name')+'\\nEmail: '+v('email')+'\\nMobile: '+v('phone')+'\\nSubject: '+v('subject')+'\\n\\n'+v('message');
    st.className='sp-status sp-status--success is-visible';st.textContent='Opening WhatsApp with your message…';
    window.open('https://wa.me/919778452007?text='+encodeURIComponent(text),'_blank','noopener');});
})();
</script>
"""
page("contact.html", "Contact Source Pro B2B2C — App Sphere B2B India Pvt. Ltd.",
     "Contact Source Pro B2B2C: address, phone numbers, email and business hours, plus an enquiry form.",
     "https://appsphereb2b.com/contact/", contact, contact_js)

# ======================= RETAILER =======================
R = hero("Retailer partnership", "You built this business with your own hands. Now let's make it digital.",
         "Source Pro B2B2C helps your kirana or local retail shop become a digital hypermarket with 25,000+ products, online ordering, and support from your area distributor — at zero setup cost for retailers.",
         "retailer-hero", "A retailer using his phone in his store", '<a class="btn" href="%s" target="_blank" rel="noopener">Enquire now %s</a><a class="btn btn--ghost" href="https://appsphereb2b.com/retailer-partnership/" target="_blank" rel="noopener">Official registration form</a>' % (wa("Hello Source Pro, I am a retailer and would like to join."), ARROW))
R += """
  <section class="section"><div class="container split split--img">
    <div><p class="eyebrow">We know what you are going through</p><h2 class="h2">Your shop is open. But the market around you has changed.</h2>
    <p class="lead">Customers now expect:</p>
    %s</div>
    <figure class="figure-card">%s</figure>
  </div></section>
  <section class="section on-ink"><div class="container split split--img">
    <figure class="figure-card">%s</figure>
    <div><p class="eyebrow">The game changer for local retailers</p><h2 class="h2">Source Pro B2B2C brings both worlds together.</h2>
    <p class="lead">Your store. Your orders. Your customers. Your success.</p>
    <div class="what"><div><h3>What changes</h3>%s</div><div><h3>What stays the same</h3>%s</div></div></div>
  </div></section>
  <section class="section"><div class="container">
    <div class="section-head"><p class="eyebrow">How it works</p><h2>Eight steps from kirana to digital hypermarket.</h2></div>
    <ol class="steps8">%s</ol>
    <figure class="photo-band" style="margin-top:2.5rem">%s</figure>
  </div></section>
  <section class="section on-ink"><div class="container two">
    <div><p class="eyebrow">Retailer benefits</p><h2 class="h2">What you get.</h2>%s</div>
    <div><p class="eyebrow">Customer merits</p><h2 class="h2">What your customers get.</h2>%s</div>
  </div></section>
  <section class="section"><div class="container faq"><div><p class="eyebrow">FAQ</p><h2 class="h2">Retailer questions, answered.</h2></div>%s</div></section>
""" % (
    ticks(["More choice", "Better prices", "Easy browsing", "Digital payments", "Doorstep delivery", "Phone ordering convenience"]),
    img("retailer-challenges", "Current challenges facing a traditional city retailer: less footfall, shrinking margins", 1400, 1050),
    img("retailer-solution", "Source Pro turns a small store into a digital hypermarket", 1400, 1050),
    ticks(["Digital storefront added", "Online customer ordering enabled", "Access to products beyond your physical shelf", "24/7 business operation", "Competitive online convenience"]),
    ticks(["Your shop name and identity", "Personal customer relationships", "Customer trust", "Credit relationships", "Community connection"]),
    "".join("<li><span>%d</span>%s</li>" % (i + 1, esc(t)) for i, t in enumerate([
        "The distributor visits and explains the platform.", "Free onboarding with a digital storefront under your shop name.",
        "Access 25,000+ products without stocking all items.", "Invite your existing customers online.", "Your shop operates 24×7 digitally.",
        "Customers order; you fulfil with distributor support.", "Increased sales and local employment.", "Stock fast-moving products to compete as a quick-commerce store."])),
    img("retailer-process", "Retailers and customers in a store", 784, 754),
    ticks(["25,000+ products in your digital catalogue", "Zero setup cost; ₹2,500 + 18% GST monthly fee", "Your own storefront under your business name",
           "List your existing shop products", "Distributor support for onboarding and fulfilment", "Retain customers moving toward online ordering"]),
    ticks(["Trust in their existing local retailer", "Online convenience maintained", "Broader product browsing", "Anytime ordering", "Doorstep delivery", "Support for a local business"]),
    faq_html("retailer-partnership")) + cta_band("Ready to go digital?", "Talk to Source Pro about becoming a digital hypermarket.",
                                                  '<a class="btn btn--ghost" href="https://appsphereb2b.com/retailer-partnership/" target="_blank" rel="noopener">Official registration form</a>')
page("retailer-partnership.html", "Retailer Partnership — Source Pro B2B2C",
     "Turn your kirana or local shop into a digital hypermarket with 25,000+ products, online ordering and distributor support at zero setup cost.",
     "https://appsphereb2b.com/retailer-partnership/", R)

# ======================= DISTRIBUTOR =======================
D = hero("Distributor partnership", "Build a smarter distribution business.",
         "Source Pro B2B2C enables distributors with an assigned territory, digital retailer onboarding, app-based order flow, and distributor margins without heavy stockholding — and no large warehouse requirement initially.",
         "distributor-hero", "A distributor in a warehouse", '<a class="btn" href="%s" target="_blank" rel="noopener">Enquire now %s</a><a class="btn btn--ghost" href="distributors.html">Find a distributor seat</a>' % (wa("Hello Source Pro, I would like to become a distributor."), ARROW))
D += """
  <section class="section"><div class="container split split--img">
    <div><p class="eyebrow">The old way</p><h2 class="h2">The old way of distribution is becoming harder every year.</h2>
    <p class="lead">Many existing distributors are struggling with shrinking sales, rising receivables, high stock pressure, increasing competition, and the cost of manual market coverage.</p>
    <p class="eyebrow" style="margin-top:2rem">A new kind of distribution</p><h3 class="h3">Built for the digital era.</h3>
    %s</div>
    <figure class="figure-card">%s</figure>
  </div></section>
  <section class="section on-ink"><div class="container">
    <div class="section-head"><p class="eyebrow">Zero-stock model</p><h2>How distribution works with Source Pro.</h2></div>
    <ol class="steps8 steps8--4">%s</ol>
    %s
  </div></section>
  <section class="section"><div class="container">
    <div class="section-head"><p class="eyebrow">Onboarding &amp; investment</p><h2>Three phases, no surprises.</h2></div>
    <div class="phases">
      <article><span>Phase 1</span><h3>Platform demonstration &amp; initial evaluation</h3><ul><li>Live platform demonstration with real credentials</li><li>Experience order flow and retailer interaction</li><li>No financial commitment required</li></ul></article>
      <article><span>Phase 2</span><h3>Platform fee &amp; territory finalisation</h3><ul><li>One-time platform fee: ₹35,000 + 18%% GST (₹41,300 total)</li><li>Territory review and provisional allotment</li><li>Documentation and KYC completion</li></ul></article>
      <article><span>Phase 3</span><h3>MoU &amp; security deposit</h3><ul><li>Formal Memorandum of Understanding</li><li>Refundable security deposit: ₹2,50,000</li><li>Financial assistance for working capital may be available through banks / NBFCs</li></ul></article>
    </div>
  </div></section>
  <section class="section on-ink"><div class="container">
    <div class="section-head"><p class="eyebrow">Traditional vs. Source Pro</p><h2>What changes for a distributor.</h2></div>
    <div class="table-wrap"><table class="cmp"><thead><tr><th>Aspect</th><th>Traditional distribution</th><th>Source Pro B2B2C</th></tr></thead><tbody>
      <tr><th>Stock purchase</th><td>Before sales</td><td>Against confirmed demand</td></tr>
      <tr><th>Warehouse</th><td>Rent and maintenance burden</td><td>No traditional requirement initially</td></tr>
      <tr><th>Risk</th><td>Expiry, dead stock</td><td>Reduced through demand-led movement</td></tr>
      <tr><th>Order collection</th><td>Manual, limited coverage</td><td>Digital flow, wider connectivity</td></tr>
      <tr><th>Collections</th><td>High pressure, capital blockage</td><td>Structured platform transactions</td></tr>
      <tr><th>Growth</th><td>Limited by field-force capacity</td><td>Linked to retailer onboarding</td></tr>
    </tbody></table></div>
  </div></section>
  <section class="section"><div class="container two">
    <div><p class="eyebrow">Who can apply</p><h2 class="h2">Eligibility.</h2>%s<p class="muted" style="margin-top:1rem">Selection requires company approval, suitability assessment and territory availability.</p></div>
    <div><p class="eyebrow">Territory rollout</p><h2 class="h2">4–5 distributors per assembly constituency.</h2><p class="lead">Additional distributors may be added in densely populated areas. See the seats available in your constituency.</p><p style="margin-top:1.25rem"><a class="btn btn--primary" href="distributors.html">View distributor seats %s</a></p></div>
  </div></section>
  <section class="section on-ink"><div class="container faq"><div><p class="eyebrow">FAQ</p><h2 class="h2">Distributor questions, answered.</h2></div>%s</div></section>
""" % (
    ticks(["Assigned territory", "Digital retailer onboarding", "App-based order flow", "Distributor margins without heavy stockholding burden", "No large warehouse requirement initially"]),
    img("distributor-solution", "Source Pro B2B distribution: app, trucks and retailers connected", 1400, 788),
    "".join("<li><span>%d</span>%s</li>" % (i + 1, esc(t)) for i, t in enumerate([
        "You are assigned a defined territory.", "You personally onboard kirana and local retail stores.",
        "Retailers onboard customers and receive digital orders.", "You fulfil retailer orders based on confirmed demand."])),
    '<p class="lead" style="margin-top:2rem">Products are sourced against confirmed demand — reducing expiry, dead-stock and damaged-goods risk. Your income grows with retailer adoption and order flow.</p>',
    ticks(["Existing distributors", "Aspiring entrepreneurs", "Retailers looking to expand", "Sales and marketing professionals", "Business-minded individuals"]),
    ARROW, faq_html("distributor-partnership-india")) + cta_band("Secure your territory.", "Talk to the team about distributor seats in your constituency.",
                                                                  '<a class="btn btn--ghost" href="https://appsphereb2b.com/distributor-registration/" target="_blank" rel="noopener">Official registration form</a>')
page("distributor-partnership.html", "Distributor Partnership — Source Pro B2B2C",
     "Become a Source Pro B2B2C distributor: assigned territory, zero-stock model, digital retailer onboarding and app-based orders.",
     "https://appsphereb2b.com/distributor-partnership-india/", D)

# ======================= MANUFACTURER =======================
M = hero("Manufacturer partnership", "Your products. Wider retail visibility. Smarter digital distribution.",
         "Source Pro B2B2C lists your SKU catalogue, improves visibility through retailer and distributor networks, and strengthens the connection between consumer demand and supply — while complementing your existing distribution.",
         "manufacturer-hero", "A manufacturer in a production facility", '<a class="btn" href="%s" target="_blank" rel="noopener">Enquire now %s</a><a class="btn btn--ghost" href="https://appsphereb2b.com/manufacturer-partnership/" target="_blank" rel="noopener">Official registration form</a>' % (wa("Hello Source Pro, I am a manufacturer and would like to list my products."), ARROW))
M += """
  <section class="section"><div class="container split split--img">
    <div><p class="eyebrow">The gap</p><h2 class="h2">Traditional distribution leaves gaps manufacturers cannot always see.</h2>
    <p class="lead">Manual sales coverage remains uneven; premium outlets receive regular visits while smaller retail points go underserved. Digital visibility gaps harm products even when demand exists.</p>
    <p class="eyebrow" style="margin-top:2rem">The solution</p><h3 class="h3">A digital distribution layer built around your brand.</h3>
    <p class="lead">Source Pro B2B2C lists SKU catalogues, improves visibility through retailer and distributor networks, and strengthens consumer demand-to-supply connections while complementing existing distribution relationships.</p></div>
    <figure class="figure-card">%s</figure>
  </div></section>
  <section class="section on-ink"><div class="container">
    <div class="section-head"><p class="eyebrow">How it works</p><h2>Five steps to wider reach.</h2></div>
    <ol class="steps8 steps8--5">%s</ol>
  </div></section>
  <section class="section"><div class="container split split--img">
    <figure class="figure-card">%s</figure>
    <div><p class="eyebrow">Key benefits</p><h2 class="h2">What you get.</h2>%s</div>
  </div></section>
  <section class="section on-ink"><div class="container">
    <div class="section-head"><p class="eyebrow">Commercial &amp; operational clarity</p><h2>The questions manufacturers ask first.</h2></div>
    <div class="table-wrap"><table class="cmp"><thead><tr><th>Concern</th><th>Source Pro solution</th></tr></thead><tbody>
      <tr><th>Warehouse &amp; stock custody</th><td>Dedicated/shared warehouse support; joint stock management through state-level mother warehouses and district-level hubs.</td></tr>
      <tr><th>Pricing</th><td>Manufacturers provide the pricing framework; platform pricing follows agreed terms.</td></tr>
      <tr><th>Returns &amp; damages</th><td>Zero-return model for unsold stock; returns apply only to previously sold items; damages limited to transit cases.</td></tr>
      <tr><th>Payment settlement</th><td>Single-window system per mutually agreed timelines; transparent invoicing and transaction visibility.</td></tr>
      <tr><th>Outbound logistics</th><td>Managed through the Source Pro B2B2C distribution network.</td></tr>
      <tr><th>Data access</th><td>Product movement, demand trends, retailer reach, sales performance (subject to platform policy).</td></tr>
    </tbody></table></div>
    <figure class="photo-band" style="margin-top:2.5rem">%s</figure>
  </div></section>
  <section class="section"><div class="container faq"><div><p class="eyebrow">FAQ</p><h2 class="h2">Manufacturer questions, answered.</h2></div>%s</div></section>
""" % (
    img("manufacturer-solution", "A manufacturer reviewing products with partners", 789, 855),
    "".join("<li><span>%d</span>%s</li>" % (i + 1, esc(t)) for i, t in enumerate([
        "Submit company, brand, product, pricing, GST and catalogue data.", "Approved SKUs are listed with product details and images.",
        "Retailers and distributors gain regional product visibility.", "Orders are generated through platform-led demand.",
        "Receive market data and payment settlement per commercial terms."])),
    img("manufacturer-process", "A brand presenting products to a distribution team", 789, 855),
    ticks(["Complete SKU listing with specifications and pricing", "Improved visibility across onboarded retailers", "Distributor-led market activation and fulfilment",
           "Real-time / periodic sales and demand data", "Structured payment and settlement", "Dedicated warehousing options",
           "Your responsibilities reduced to production and brand awareness"]),
    img("contact-hero", "A manufacturer discussing a partnership", 784, 754),
    faq_html("manufacturer-partnership")) + cta_band("List your products.", "Put your catalogue in front of every retailer in the region.", "")
page("manufacturer-partnership.html", "Manufacturer Partnership — Source Pro B2B2C",
     "List your SKUs on Source Pro B2B2C: wider retail visibility, distributor-led activation, demand data and structured settlement.",
     "https://appsphereb2b.com/manufacturer-partnership/", M)
print("pages built")
