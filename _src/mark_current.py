"""Mark the current page in the header menu (aria-current). Run after any header/page rebuild."""
import re, glob, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
direct = {'index.html', 'about.html', 'distributors.html', 'partner-infrastructure.html', 'contact.html'}
part = {'retailer-partnership.html', 'distributor-partnership.html', 'manufacturer-partnership.html', 'customer-experience.html'}
res = {'blog.html': 'blog.html', 'kirana-stores.html': 'blog.html', 'news.html': 'news.html', 'gallery.html': 'gallery.html', 'retail-reality.html': 'retail-reality.html'}
for f in glob.glob('*.html'):
    s = open(f, encoding='utf8').read()
    a = s.index('<header'); b = s.index('</header>')
    h = s[a:b].replace(' aria-current="page"', '')
    if f in direct:
        h = re.sub(r'(<a class="nav__link" href="%s")\s*>' % re.escape(f), r' aria-current="page">', h, count=1)
    if f in part or f in res:
        idx = 0 if f in part else 1
        page = f if f in part else res[f]
        btns = [m.start() for m in re.finditer(r'<button class="nav__link"', h)]
        p = btns[idx]
        h = h[:p] + '<button class="nav__link" aria-current="page"' + h[p + len('<button class="nav__link"'):]
        h = h.replace('<a class="mega__card" href="%s"' % page, '<a class="mega__card" href="%s" aria-current="page"' % page)
    open(f, 'w', encoding='utf8', newline='').write(s[:a] + h + s[b:])
