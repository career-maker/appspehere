"""Rebuild the <main> of the partnership + contact + customer-experience pages from the live site's copy.
Text is pulled from saved copies of the live pages (set LIVE_DIR), so wording stays exact.
Run from the repo root:  LIVE_DIR=<dir with L_*.html> python _src/inner_pages.py
"""
import os, re, html as H
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
LIVE = os.environ.get('LIVE_DIR') or os.path.join(os.environ['TEMP'], 'live')
ARR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
WA = 'https://wa.me/919778452007?text=Hello%20Source%20Pro%2C%20I%20would%20like%20to%20know%20more.'
e = H.escape


def live_lines(name):
    s = BeautifulSoup(open(f'{LIVE}/{name}.html', encoding='utf8', errors='ignore').read(), 'html.parser')
    for t in s(['script', 'style', 'noscript', 'header', 'footer', 'nav', 'svg', 'template']):
        t.decompose()
    for t in s.select('.gtranslate_wrapper,#gt-wrapper,[class*=marquee],[class*=ticker]'):
        t.decompose()
    root = s.find('main') or s.body
    out, prev = [], None
    for el in root.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'summary', 'label', 'button', 'blockquote', 'a', 'span', 'div']):
        if el.name in ('div', 'span', 'a'):
            if el.find(['p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'a', 'span']):
                continue
            if el.name == 'a' and not el.get_text(strip=True):
                continue
        t = el.get_text(' ', strip=True)
        if len(t) < 2 or t == prev:
            continue
        prev = t
        out.append((el.name, t))
    return out


def between(lines, a, b=None, tags=None):
    """lines strictly between the first line containing text a and the next line containing text b."""
    i = next(k for k, (_, t) in enumerate(lines) if a in t) + 1
    j = next((k for k in range(i, len(lines)) if b and b in lines[k][1]), len(lines))
    r = lines[i:j]
    return [x for x in r if not tags or x[0] in tags]


def paras(lines):
    return ''.join(f'<p>{e(t)}</p>' for tg, t in lines if tg == 'p')


def ticks(items):
    return '<ul>' + ''.join(f'<li>{TICK}{e(t)}</li>' for t in items) + '</ul>'


def faq_block(lines, who):
    qa = between(lines, 'Frequently Asked', 'Shopping Basket')
    items, q = [], None
    for tg, t in qa:
        if tg == 'span':
            q = t
        elif tg == 'p' and q:
            items.append((q, t)); q = None
    det = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}<i aria-hidden="true"></i></summary><div class="faq__a"><p>{e(a)}</p></div></details>' for i, (q, a) in enumerate(items))
    art = re.search(r'<svg class="faq__art".*?</svg>', open('index.html', encoding='utf8').read(), re.S).group(0)
    return (f'<section class="section on-ink faq-section" aria-labelledby="faq-h"><div class="container faq"><div class="faq__intro">'
            f'<h2 id="faq-h">Frequently Asked Questions</h2>{art}</div>'
            f'<div class="faq__list">{det}</div></div></section>')


STATES = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Jammu and Kashmir', 'Ladakh', 'Lakshadweep', 'Puducherry']


def form(prefix, title, wa, fields, button, note=''):
    """fields: (kind, label, placeholder, required, options|None)  kind: text|email|tel|number|select|textarea"""
    out = []
    for n, (kind, label, ph, req, opts) in enumerate(fields):
        i = f'{prefix}{n}'
        star = ' <span>*</span>' if req else ''
        r = ' required' if req else ''
        if kind == 'select':
            o = f'<option value="">{e(ph)}</option>' + ''.join(f'<option>{e(x)}</option>' for x in opts)
            ctl = f'<select id="{i}" name="{i}"{r}>{o}</select>'
        elif kind == 'textarea':
            ctl = f'<textarea id="{i}" name="{i}" rows="4" placeholder="{e(ph)}"{r}></textarea>'
        else:
            ctl = f'<input id="{i}" name="{i}" type="{kind}" placeholder="{e(ph)}"{r}>'
        full = ' sp-full' if kind == 'textarea' else ''
        out.append(f'<div class="sp-field{full}"><label for="{i}">{e(label)}{star}</label>{ctl}</div>')
    return (f'<form class="sp-infra-form" data-wa="{e(wa)}" novalidate><div class="sp-form-section"><h2>{e(title)}</h2>{note}'
            f'<div class="sp-status" role="alert" tabindex="-1"></div><div class="sp-form-grid">{"".join(out)}</div>'
            f'<button type="submit" class="sp-submit-btn">{e(button)}</button></div></form>')


F = lambda *a: a  # readability


RETAIL_FIELDS = [
    ('text', 'Name of the Retail Shop Owner', "Enter shop owner's full name", True, None),
    ('text', 'Name of the Retail Store / Trade Name', 'Enter retail store / trade name', True, None),
    ('email', 'Email Address', 'Enter your email address', True, None),
    ('tel', 'Mobile Number', 'Enter your mobile number', True, None),
    ('text', 'Shop Address Line 1', 'Enter address line 1', True, None),
    ('text', 'Shop Address Line 2', 'Enter address line 2', False, None),
    ('select', 'Select your state', 'State', True, STATES),
    ('text', 'District', 'Enter your district', True, None),
    ('text', 'PIN Code', 'Enter PIN code', True, None),
    ('text', 'Assembly Constituency', 'Enter assembly constituency', True, None),
    ('text', 'GSTIN', 'Enter GSTIN', False, None),
    ('select', 'Which category best describes your current retail business?', 'Select retail business category', True,
     ['Grocery Store', 'Stationery Store', 'Supermarket', 'Mobile Shop', 'Paint Shop', 'Hardware Store', 'Medical / Pharmacy', 'Department Store', 'Electrical Store', 'Garment Store', 'Footwear Store', 'Gift Shop', 'Furniture Store', 'Bakery', 'Sweet Shop', 'Fruit & Vegetable Store', 'Dairy Store', 'Home Needs Store', 'General Store', 'Other']),
    ('select', 'Years in Retail Business', 'Select years in business', True, ['Less than 1 Year', '1-2 Years', '3-5 Years', '6-10 Years', '11-20 Years', 'More than 20 Years']),
    ('select', 'Select storage capacity', 'Storage Space', True, ['Less than 50 Sq Ft', '50-100 Sq Ft', '100-200 Sq Ft', '200-500 Sq Ft', '500-1000 Sq Ft', 'More than 1000 Sq Ft']),
    ('select', 'Interested in Loan Assistance?', 'Select an option', False, ['Yes', 'No', 'Maybe - Need More Information']),
]
DIST_FIELDS = [
    ('text', 'Name of Proprietor / Director / Partner', 'Enter proprietor/director/partner name', True, None),
    ('text', 'Trade Name of Existing Distribution Business / Proposed Distribution Name', 'Enter your distribution business name', True, None),
    ('tel', 'Mobile Number', 'Enter your mobile number', True, None),
    ('email', 'Email Address', 'Enter your email address', True, None),
    ('text', 'Shop Address Line 1', 'Enter address line 1', True, None),
    ('text', 'Shop Address Line 2', 'Enter address line 2', False, None),
    ('select', 'State', 'Select State', True, STATES),
    ('text', 'District', 'Enter your District', True, None),
    ('text', 'City', 'Enter your City', True, None),
    ('text', 'PIN Code', 'Enter PIN code', True, None),
    ('text', 'Assembly Constituency', 'Enter assembly constituency', True, None),
    ('select', 'Which product categories are you currently distributing?', 'Select product category', True, ['FMCG', 'Stationery', 'Cosmetics', 'Groceries', 'Electronics', 'Multiple Categories', 'Other']),
    ('text', 'GSTIN', 'Enter GSTIN', False, None),
    ('select', 'Select storage capacity', 'Storage Space', False, ['0-50 Sq Ft', '50-100 Sq Ft', '100-200 Sq Ft', '200-500 Sq Ft', '500+ Sq Ft']),
    ('select', 'Number of Employees', 'Select number of employees', False, ['1-5', '6-10', '11-25', '26-50', '51-100', '100+']),
    ('select', 'Previous Financial Year Turnover', 'Select annual turnover', False, ['Below ₹10 Lakhs', '₹10 Lakhs - ₹25 Lakhs', '₹25 Lakhs - ₹50 Lakhs', '₹50 Lakhs - ₹1 Crore', '₹1 Crore - ₹5 Crore', 'Above ₹5 Crore']),
    ('number', 'Number of Goods Vehicles', 'Enter number of vehicles', False, None),
    ('textarea', 'Questions or Comments', 'Enter your message', False, None),
]
MANU_FIELDS = [
    ('text', 'Name of Concerned Person', 'Enter full name', True, None),
    ('email', 'Email Address', 'Enter your email address', True, None),
    ('tel', 'Mobile Number', 'Enter your mobile number', True, None),
    ('text', 'Company Name', 'Enter company name', True, None),
    ('text', 'Designation', 'E.g., Owner, Director, Sales Manager', True, None),
    ('text', 'Brand Name', 'Enter brand name', True, None),
    ('select', 'Which category of products do you manufacture?', 'Select product category', True,
     ['FMCG', 'Stationery', 'Cosmetics', 'Food Products', 'Beverages', 'Electricals', 'Electronics', 'Home Care Products', 'Personal Care Products', 'Pharmaceuticals', 'Textiles & Garments', 'Footwear', 'Furniture', 'Kitchenware', 'Plastic Products', 'Packaging Materials', 'Building Materials', 'Agricultural Products', 'Automotive Products', 'Multiple Categories', 'Others']),
    ('select', 'State', 'Select your state', True, STATES),
    ('text', 'District', 'Enter your district', True, None),
    ('text', 'PIN Code', 'Enter PIN code', True, None),
    ('text', 'Factory / Office Address Line 1', 'Enter address line 1', True, None),
    ('text', 'Factory / Office Address Line 2', 'Enter address line 2', True, None),
    ('select', 'GST Registration Status', 'Select GST status', True, ['Registered', 'Applied', 'Not Registered']),
    ('text', 'GSTIN', 'Enter GSTIN (Optional)', False, None),
    ('select', 'Number of Years in Operation', 'Select years in operation', True, ['Less than 1 Year', '1-2 Years', '3-5 Years', '6-10 Years', '11-20 Years', 'More than 20 Years']),
    ('select', 'Number of SKUs', 'Select SKU range', True, ['1-50', '51-100', '101-250', '251-500', '501-1000', '1000+']),
    ('text', 'Monthly Production Capacity', 'Enter monthly production capacity', False, None),
]


def swap_main(fn, main, extra_scripts=''):
    s = open(fn, encoding='utf8').read()
    a = s.index('<main id="main">')
    b = s.index('</main>')
    marq = re.search(r'<div class="marquee".*?</div></div></div>', s, re.S).group(0)
    main = main.replace('@@MARQUEE@@', marq)
    s = s[:a] + '<main id="main">\n' + main + '\n  ' + s[b:]
    for sc in extra_scripts.split():
        if sc not in s:
            s = s.replace('<script src="js/main.js', f'<script src="{sc}" defer></script>\n<script src="js/main.js', 1)
    open(fn, 'w', encoding='utf8', newline='').write(s)
    print('rebuilt', fn)


def hero(crumb, h1, lead_html, buttons, img, w=789, hgt=855, alt=''):
    return (f'<section class="page-hero"><img class="page-hero__art" src="assets/{img}" width="{w}" height="{hgt}" alt="{e(alt)}" decoding="async">'
            f'<div class="container"><p><a href="index.html">Source Pro</a> / {crumb}</p><h1>{h1}</h1>{lead_html}'
            f'<div class="stage__cta">{buttons}</div></div></section>\n  @@MARQUEE@@')


def btn(href, text, ghost=False, ext=False):
    t = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="btn{" btn--ghost" if ghost else ""}" href="{href}"{t}>{text}{" " + ARR if not ghost else ""}</a>'


def split_section(img, alt, eyebrow, h2, h3, paragraphs, link=None, ink=False, flip=False, sid=''):
    fig = f'<figure class="figure-card"><img src="assets/{img}" width="784" height="754" alt="{e(alt)}" loading="lazy" decoding="async"></figure>'
    h3h = f'<h3>{e(h3)}</h3>' if h3 else ''
    lk = f'<p><a class="link-arrow" href="{link[0]}">{e(link[1])} {ARR}</a></p>' if link else ''
    txt = f'<div><p>{e(eyebrow)}</p><h2>{e(h2)}</h2>{h3h}{paragraphs}{lk}</div>'
    body = (fig + txt) if flip else (txt + fig)
    return f'<section class="section{" on-ink" if ink else ""}"{f" id=%s{sid}%s" % (chr(34), chr(34)) if sid else ""}><div class="container split split--img">{body}</div></section>'


def table(rows, head):
    th = ''.join(f'<th scope="col">{e(h)}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<{"th scope=%srow%s" % (chr(34), chr(34)) if k == 0 else "td"}>{e(c)}</{"th" if k == 0 else "td"}>' for k, c in enumerate(r)) + '</tr>' for r in rows)
    return f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


# ===================== RETAILER =====================
def retailer():
    L = live_lines('L_retailer-partnership')
    hero_p = next(t for tg, t in L if tg == 'p' and t.startswith('Source Pro B2B2C helps your kirana'))
    tag = 'Your shop. Your customers. Your name. Now with digital convenience.'
    prob = between(L, 'We Know What You Are Going Through', 'See The Solution')
    prob_h3 = prob[0][1]
    sol = between(L, 'Game Changer for Local Retailers', 'See The Process')
    proc = between(L, 'How Source Pro B2B2C Works for Your Shop', 'Enquire Now to Learn More', tags={'li'})
    chg = between(L, 'What Changes. What Stays the Same.', 'RETAILER HIGHLIGHTS')[0][1]
    chg = chg.replace('What Changes What Stays the Same ', '')
    sents = [x.strip() for x in re.split(r'(?<=\.)\s+', chg) if x.strip()]
    changes, stays = sents[0::2], sents[1::2]
    hl = between(L, 'RETAILER HIGHLIGHTS', 'Register with Us', tags={'li'})
    merit = [t for _, t in hl[2:7]]
    benef = [t for _, t in hl[7:]]
    m = hero('Retailer partnership', "You Built This Business With Your Own Hands. Now Let's Make It Digital.",
             f'<p>{e(hero_p)}</p><p>{e(tag)}</p>', btn('#register', 'Enquire Now') + btn('#register', 'Official registration form', ghost=True),
             'retailer-hero.webp', alt='A retailer in his shop using the Source Pro app')
    m += split_section('retailer-challenges.webp', 'Current retailer challenges', 'Strategic Insights', 'We Know What You Are Going Through', prob_h3,
                       paras(prob[1:]), ('#solution', 'See The Solution'), sid='problem')
    m += split_section('retailer-solution.webp', 'Source Pro retailer storefront', 'Strategic Insights', 'Source Pro B2B2C — The Game Changer for Local Retailers', '',
                       paras(sol), ('#process', 'See The Process'), ink=True, flip=True, sid='solution')
    m += (f'<section class="section" id="process"><div class="container"><div class="section-head"><p>Strategic Insights</p><h2>How Source Pro B2B2C Works for Your Shop</h2></div>'
          f'<ol>{"".join(f"<li><span>{i + 1}</span>{e(t)}</li>" for i, (_, t) in enumerate(proc))}</ol>'
          f'<p style="margin-top:2rem">{btn(WA, "Enquire Now to Learn More", ext=True)}</p></div></section>\n  ')
    m += (f'<section class="section on-ink"><div class="container"><div class="section-head"><h2>What Changes. What Stays the Same.</h2></div><div class="hl">'
          f'<div><h3>What Changes</h3>{ticks(changes)}</div><div><h3>What Stays the Same</h3>{ticks(stays)}</div></div></div></section>\n  ')
    m += (f'<section class="section"><div class="container"><div class="section-head"><h2>RETAILER HIGHLIGHTS</h2></div><div class="hl">'
          f'<div><h3>Customers Merit</h3>{ticks(merit)}</div><div><h3>Retailers Benefit</h3>{ticks(benef)}</div></div></div></section>\n  ')
    m += (f'<section class="form-wrap" id="register"><div class="container">'
          + form('r', 'Register with Us', 'Hello Source Pro, I would like to register my retail shop.', RETAIL_FIELDS, 'Submit Enquiry') + '</div></section>\n  ')
    m += faq_block(L, 'retailers')
    swap_main('retailer-partnership.html', m, 'js/reg-form.js')


# ===================== DISTRIBUTOR =====================
CALC = '''<section class="section on-ink" id="numbers"><div class="container">
    <div class="section-head"><p>The Distributor Opportunity — By the Numbers</p><h2>Distributor Earnings Potential Calculator</h2><p>Adjust the sliders to estimate your earning potential.</p></div>
    <div class="calc">
      <div class="calc__in">
        <div class="calc__row"><label for="shops">Number of Shops: <b id="shopsValue">50</b></label><input type="range" id="shops" min="1" max="150" step="1" value="50"><div class="calc__ticks"><span>10</span><span>25</span><span>50</span><span>75</span><span>100</span><span>125</span><span>150</span></div></div>
        <div class="calc__row"><label for="sales">Average Expected Daily Sales MoV per Shop: <b id="salesValue">₹20,000</b></label><input type="range" id="sales" min="0" max="14" step="1" value="4"><div class="calc__ticks"><span>2.5K</span><span>10K</span><span>20K</span><span>30K</span><span>50K</span><span>70K</span><span>1L</span></div></div>
        <div class="calc__row"><label for="margin">Distributor Profit Margin: <b id="marginValue">10%</b></label><input type="range" id="margin" min="0" max="10" step="1" value="5"><div class="calc__ticks"><span>4%</span><span>7%</span><span>9%</span><span>11%</span><span>13%</span><span>15%</span></div></div>
        <ul class="calc__facts"><li><strong>Zero Stock</strong> Inventory-free model</li><li><strong>One Time Cost</strong> ₹41,300 incl. GST</li><li><strong>Refundable Security Deposit</strong> ₹2,50,000</li><li><strong>365 Days</strong> Year-round business potential</li></ul>
      </div>
      <div class="calc__out">
        <h3>Estimated Business Potential</h3>
        <dl><div><dt>Daily Income</dt><dd id="dailyIncome">₹0</dd></div><div><dt>Monthly Income</dt><dd id="monthlyIncome">₹0</dd></div><div><dt>Yearly Income</dt><dd id="yearlyIncome">₹0</dd></div>
        <div><dt>Daily Sales Value</dt><dd id="dailySales">₹0</dd></div><div><dt>Monthly Sales Turnover</dt><dd id="monthlyTurnover">₹0</dd></div><div><dt>Yearly Turnover</dt><dd id="yearlyTurnover">₹0</dd></div>
        <div><dt>Average Time to Recover Total Initial Outlay</dt><dd id="recoveryDays">-</dd></div><div><dt>ROI on Total Initial Outlay</dt><dd id="roiValue">-</dd></div></dl>
        <p>The above calculation is indicative and based on selected assumptions. Actual sales, margin, income, and ROI may vary depending on market performance, retailer activation, product demand, territory strength, and operational efficiency.</p>
      </div>
    </div></div></section>'''


def distributor():
    L = live_lines('L_distributor-partnership-india')
    lead = next(t for tg, t in L if tg == 'p' and t.startswith('Source Pro B2B2C gives distributors a leaner'))
    prob = between(L, 'The Old Way of Distribution Is Becoming Harder', 'See The Solution')
    sol = between(L, 'A New Kind of Distribution', 'The Distributor Opportunity')
    j_intro = between(L, 'Your Journey as a Source Pro B2B2C Distributor', 'Phase 1')[0][1]
    ph1 = between(L, 'Platform Demonstration & Initial Evaluation', 'Platform Fee Payment', tags={'p'})
    ph2 = between(L, 'Platform Fee Payment & Territory Finalisation', 'MoU Execution', tags={'p'})
    ph3 = between(L, 'MoU Execution & Security Deposit', 'How the Distributor Model Works', tags={'p'})
    how = between(L, 'How the Distributor Model Works', 'Why This Model Is Attractive', tags={'li'})
    why = between(L, 'Why This Model Is Attractive', 'Traditional Distributor vs', tags={'p', 'div'})
    cmp_ = between(L, 'Traditional Distributor vs Source Pro B2B2C Distributor', 'Register with Us')[0][1]
    cmp_ = cmp_.replace('Traditional Distribution Source Pro B2B2C Distribution ', '')
    pairs = [
        ('Heavy stock purchase before sales', 'Products sourced against confirmed demand'),
        ('Warehouse rent and maintenance burden', 'No traditional warehouse requirement in initial model'),
        ('Expiry, dead stock, and damaged goods risk', 'Reduced stock risk through demand-led movement'),
        ('Manual order collection and limited coverage', 'Digital order flow and wider retailer connectivity'),
        ('Collections pressure and capital blockage', 'More structured platform-led transactions, subject to agreed payment process'),
        ('Growth limited by field force capacity', 'Growth linked to retailer onboarding and digital adoption')]
    assert all(a in cmp_ and b in cmp_ for a, b in pairs)
    m = hero('Distributor partnership / Become a Distributor', 'Build a Smarter Distribution Business', f'<p>{e(lead)}</p>',
             btn('#register', 'Enquire Now'), 'distributor-hero.webp', alt='A distributor in his warehouse')
    m += split_section('distributor-warehouse.webp', 'A conventional distributor under pressure', 'Strategy Insights', 'The Old Way of Distribution Is Becoming Harder Every Year', '',
                       paras(prob), ('#solution', 'See The Solution'))
    m += split_section('distributor-solution.webp', 'A Source Pro distributor on autopilot', 'Strategy Insights', 'A New Kind of Distribution — Built for the Digital Era.', '',
                       paras(sol), None, ink=True, flip=True, sid='solution')
    m += CALC + '\n  '
    phase = lambda n, title, ps: f'<div class="phase"><span class="phase__n">Phase {n}</span><h3>{e(title)}</h3>{paras(ps)}</div>'
    m += (f'<section class="section"><div class="container"><div class="section-head"><h2>Your Journey as a Source Pro B2B2C Distributor — 3 Phases to Full Operation</h2><p>{e(j_intro)}</p></div>'
          f'<div class="phases">{phase(1, "Platform Demonstration & Initial Evaluation", ph1)}{phase(2, "Platform Fee Payment & Territory Finalisation", ph2)}{phase(3, "MoU Execution & Security Deposit", ph3)}</div>'
          f'<p style="margin-top:2rem">{btn("#register", "Enquire Now")}</p></div></section>\n  ')
    m += (f'<section class="section on-ink"><div class="container two"><div><h2>How the Distributor Model Works</h2><ol>{"".join(f"<li><span>{i + 1}</span>{e(t)}</li>" for i, (_, t) in enumerate(how))}</ol></div>'
          f'<div><h2>Why This Model Is Attractive for Distributors</h2>{ticks([t for _, t in why])}</div></div></section>\n  ')
    m += (f'<section class="section"><div class="container"><div class="section-head"><h2>Traditional Distributor vs Source Pro B2B2C Distributor</h2></div>'
          + table(pairs, ['Traditional Distribution', 'Source Pro B2B2C Distribution']) + '</div></section>\n  ')
    m += (f'<section class="form-wrap" id="register"><div class="container">' + form('d', 'Register with Us', 'Hello Source Pro, I would like to apply as a distributor.', DIST_FIELDS, 'Register Interest') + '</div></section>\n  ')
    m += faq_block(L, 'distributors')
    swap_main('distributor-partnership.html', m, 'js/reg-form.js js/calc.js')


# ===================== MANUFACTURER =====================
def manufacturer():
    L = live_lines('L_manufacturer-partnership')
    h3 = 'Your Products. Wider Retail Visibility. Smarter Digital Distribution.'
    lead = next(t for tg, t in L if tg == 'p' and t.startswith('Source Pro B2B2C gives manufacturers a digital'))
    prob = between(L, 'Traditional Distribution Leaves Gaps', 'See The Solution')
    sol = between(L, 'A Digital Distribution Layer Built Around Your Brand', 'See The Process')
    proc = between(L, 'How the Manufacturer Partnership Works', 'Enquire Now to Learn More', tags={'li'})
    keyb = between(L, 'Manufacturer Partnership – Key Benefits', 'Why Manufacturers Should Not Ignore', tags={'li'})
    whyp = between(L, 'Why Manufacturers Should Not Ignore Digital Retail Visibility', 'Commercial and Operational Clarity', tags={'p'})
    clar = between(L, 'Commercial and Operational Clarity for Manufacturers', 'Register with Us')[0][1]
    clar = clar.replace("Manufacturer’s Key Concern How Source Pro B2B2C Addresses It ", '')
    keys = ['Warehouse & Stock Custody', 'Pricing', 'Returns and Damages', 'Payment Settlement', 'Outbound Logistics', 'Data Access']
    pos = [clar.index(k) for k in keys]
    rows = [(k, clar[p + len(k):(pos[i + 1] if i + 1 < len(pos) else len(clar))].strip()) for i, (k, p) in enumerate(zip(keys, pos))]
    m = hero('Manufacturer partnership', h3, f'<p>{e(lead)}</p>', btn('#register', 'Enquire Now'), 'manufacturer-hero.webp', alt='A manufacturer at his factory')
    m += split_section('manufacturer-process.webp', 'Manufacturing and distribution gaps', 'Strategic Insights', 'Traditional Distribution Leaves Gaps Manufacturers Cannot Always See', '',
                       paras(prob), ('#solution', 'See The Solution'))
    m += split_section('manufacturer-solution.webp', 'A digital distribution layer for brands', 'Strategic Insights', 'A Digital Distribution Layer Built Around Your Brand', '',
                       paras(sol), ('#process', 'See The Process'), ink=True, flip=True, sid='solution')
    m += (f'<section class="section" id="process"><div class="container"><div class="section-head"><p>Strategic Insights</p><h2>How the Manufacturer Partnership Works</h2></div>'
          f'<ol>{"".join(f"<li><span>{i + 1}</span>{e(t)}</li>" for i, (_, t) in enumerate(proc))}</ol>'
          f'<p style="margin-top:2rem">{btn(WA, "Enquire Now to Learn More", ext=True)}</p></div></section>\n  ')
    m += (f'<section class="section on-ink"><div class="container"><div class="section-head"><h2>MANUFACTURER HIGHLIGHTS</h2></div><div class="hl">'
          f'<div><span class="rr__src">Key Benefits</span><h3>Manufacturer Partnership – Key Benefits</h3>{ticks([t for _, t in keyb])}</div>'
          f'<div><span class="rr__src">Listed Brands Benefit</span><h3>Why Manufacturers Should Not Ignore Digital Retail Visibility</h3>{paras(whyp)}</div></div></div></section>\n  ')
    m += (f'<section class="section"><div class="container"><div class="section-head"><h2>Commercial and Operational Clarity for Manufacturers</h2></div>'
          + table(rows, ['Manufacturer’s Key Concern', 'How Source Pro B2B2C Addresses It']) + '</div></section>\n  ')
    m += (f'<section class="form-wrap" id="register"><div class="container">' + form('m', 'Register with Us', 'Hello Source Pro, I would like to list my products as a manufacturer.', MANU_FIELDS, 'Submit Enquiry') + '</div></section>\n  ')
    m += faq_block(L, 'manufacturers')
    swap_main('manufacturer-partnership.html', m, 'js/reg-form.js')


# ===================== CONTACT =====================
def contact():
    s = (f'<section class="section"><div class="container contact">'
         '<div class="contact__info">'
         '<ul><li><h3>Address</h3><p>App Sphere B2B India Private Limited,<br>CSP XXI/271-F, 1st Floor, Emmanuel George Memorial Building, Champakkad Jn, Arthunkal PO, Cherthala, Alappuzha,<br>Kerala<br>- 688530</p></li>'
         '<li><h3>Open Hours</h3><p>day : Monday to Saturday<br>Time : 9:00 AM - 6:00 PM IST</p></li>'
         '<li><h3>Phone</h3><p><a href="tel:+919778452007">+91 97784 52007</a><br><a href="tel:+914782572486">+91 4782 572486</a><br>Phone : <a href="tel:18008907576">1800-890-7576</a></p></li>'
         '<li><h3>Mail</h3><p><a href="mailto:info@appsphereb2b.com">info@appsphereb2b.com</a><br><a href="mailto:info@sourceprob2b.co.in">info@sourceprob2b.co.in</a></p></li></ul></div>')
    contact_fields = [('text', 'Full Name', 'Enter Your full name', True, None), ('email', 'Email Address', 'Enter your email address', True, None),
                      ('tel', 'Mobile Number', 'Enter your mobile number', True, None), ('text', 'Subject', 'Enter Your Text', False, None),
                      ('textarea', 'Message', 'Enter your message', False, None)]
    s += form('c', "Let's Talk", 'Hello Source Pro, I have an enquiry.', contact_fields, 'Submit Enquiry') + '</div></section>\n  '
    tabs = ('<section class="section on-ink"><div class="container"><div class="ctabs" role="tablist" aria-label="Partner enquiry">'
            '<button type="button" role="tab" aria-selected="true" aria-controls="tab-manu" id="t-manu">Manufacturer</button>'
            '<button type="button" role="tab" aria-selected="false" aria-controls="tab-dist" id="t-dist" tabindex="-1">Distributor</button>'
            '<button type="button" role="tab" aria-selected="false" aria-controls="tab-ret" id="t-ret" tabindex="-1">Retailer</button></div>')
    tabs += f'<div class="cpanel" role="tabpanel" id="tab-manu" aria-labelledby="t-manu">{form("pm", "List Products", "Hello Source Pro, I would like to list my products as a manufacturer.", MANU_FIELDS, "Submit Enquiry")}</div>'
    tabs += f'<div class="cpanel" role="tabpanel" id="tab-dist" aria-labelledby="t-dist" hidden>{form("pd", "Secure Territory", "Hello Source Pro, I would like to apply as a distributor.", DIST_FIELDS, "Register Interest")}</div>'
    tabs += f'<div class="cpanel" role="tabpanel" id="tab-ret" aria-labelledby="t-ret" hidden>{form("pr", "Stock Direct", "Hello Source Pro, I would like to register my retail shop.", RETAIL_FIELDS, "Submit Enquiry")}</div></div></section>'
    # hero: keep the blended banner, live copy has no strapline
    h = (f'<section class="page-hero"><img class="page-hero__art" src="assets/contact-hero.webp" width="784" height="754" alt="A Source Pro team member discussing with a visitor" decoding="async">'
         f'<div class="container"><p><a href="index.html">Source Pro</a> / Contact</p><h1>Contact us</h1></div></section>\n  @@MARQUEE@@\n  ')
    swap_main('contact.html', h + s + tabs, 'js/reg-form.js js/contact-tabs.js')


# ===================== CUSTOMER EXPERIENCE =====================
def customer_experience():
    L = live_lines('L_customer-experience')
    intro = between(L, 'Here Is What Your Customer Experience Looks Like.', 'HOW YOUR CUSTOMERS FIND YOU', tags={'p'})
    find = between(L, 'HOW YOUR CUSTOMERS FIND YOU', 'Here Is What Your Customer Experience Looks Like', tags={'p'})
    find = [x for x in find]  # first p holds the quote inline
    steps = []
    k = [i for i, (tg, t) in enumerate(L) if tg == 'h2' and tg == 'h2'][0]
    seg = between(L, 'Here Is What Your Customer Experience Looks Like', 'WHY THEY CHOOSE YOU OVER THE GIANTS')
    seg = [x for x in seg if x[0] in ('h2', 'p') and x[1] not in ('Here Is What Your Customer Experience Looks Like.',)]
    # dedupe pairs (h2,p)
    pairs, i = [], 0
    while i < len(seg) - 1:
        if seg[i][0] == 'h2' and seg[i + 1][0] == 'p':
            pairs.append((seg[i][1], seg[i + 1][1])); i += 2
        else:
            i += 1
    why = between(L, 'WHY THEY CHOOSE YOU OVER THE GIANTS', 'WHAT YOUR CUSTOMERS GET', tags={'p'})
    gets = between(L, 'WHAT YOUR CUSTOMERS GET', 'Shopping Basket')
    gp, i = [], 0
    while i < len(gets) - 1:
        if gets[i][0] == 'h2':
            gp.append((gets[i][1], gets[i + 1][1])); i += 2
        else:
            i += 1
    quote = '"My shop too is online now — you can order from me anytime through your phone."'
    f0 = find[0][1]
    f0a = f0.replace(quote, '').strip()
    m = hero('Customer experience', 'Customer Experience', '<p>Here Is What Your Customer Experience Looks Like.</p>', '', 'customer-experience-hero.webp', alt='A customer ordering from a neighbourhood shop')
    m += (f'<section class="section"><div class="container split split--img"><div><p>The Customer Experience</p><h2>Here Is What Your Customer Experience Looks Like.</h2>{paras(intro)}</div>'
          f'<figure class="figure-card"><img src="assets/gal-customer.webp" width="1373" height="1173" alt="A customer and a shopkeeper talking in a neighbourhood store" loading="lazy" decoding="async"></figure></div></section>\n  ')
    m += (f'<section class="section on-ink"><div class="container two"><div><h2>HOW YOUR CUSTOMERS FIND YOU</h2><p>{e(f0a)}</p></div>'
          f'<div><blockquote>{e(quote)}</blockquote>{paras(find[1:])}</div></div></section>\n  ')
    m += (f'<section class="section"><div class="container"><div class="section-head"><h2>Here Is What Your Customer Experience Looks Like</h2></div>'
          f'<ol>{"".join(f"<li><span>{i + 1}</span><strong>{e(a)}</strong>{e(b)}</li>" for i, (a, b) in enumerate(pairs))}</ol></div></section>\n  ')
    m += (f'<section class="section on-ink"><div class="container two"><div><h2>WHY THEY CHOOSE YOU OVER THE GIANTS</h2>{paras(why)}</div>'
          f'<div><h2>WHAT YOUR CUSTOMERS GET</h2><ul>{"".join(f"<li>{TICK}<span><strong>{e(a)}</strong> {e(b)}</span></li>" for a, b in gp)}</ul></div></div></section>')
    swap_main('customer-experience.html', m)


if __name__ == '__main__':
    retailer(); distributor(); manufacturer(); contact(); customer_experience()
