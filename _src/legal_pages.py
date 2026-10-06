# Executed from build.py (shares HEAD, header(), footer(), page(), esc, S).
exec(open(os.path.join(S, "legal_data.py"), encoding="utf8").read())
import re as _re


def _slug(t):
    return _re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def _blocks(blocks):
    out = []
    for kind, val in blocks:
        if kind == "p":
            out.append("<p>%s</p>" % esc(val))
        elif kind == "h4":
            out.append("<h3>%s</h3>" % esc(val))
        else:
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % esc(i) for i in val))
    return "".join(out)


def legal_page(doc):
    toc = "".join('<li><a href="#%s"><span>%02d</span>%s</a></li>' % (_slug(h), n + 1, esc(h)) for n, (h, _) in enumerate(doc["sections"]))
    meta = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (esc(k), esc(v)) for k, v in doc["meta"])
    intro = "".join("<p>%s</p>" % esc(t) for t in doc["intro"])
    secs = "".join('<section class="legal__sec" id="%s"><h2><span>%02d</span>%s</h2>%s</section>' % (_slug(h), n + 1, esc(h), _blocks(b)) for n, (h, b) in enumerate(doc["sections"]))
    others = "".join('<a href="%s"%s>%s</a>' % (d["file"], ' aria-current="page"' if d is doc else "", esc(d["title"])) for d in DOCS)
    body = """
  <section class="page-hero page-hero--banner"><div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / %s</p>
    <h1>%s</h1>
    <p>Source Pro B2B2C · App Sphere B2B India Private Limited</p>
  </div></section>
  <div class="section"><div class="container legal">
    <aside class="legal__toc" aria-label="On this page">
      <details class="legal__tocbox" open><summary>On this page</summary><ol>%s</ol></details>
      <nav class="legal__others" aria-label="Legal pages"><h2>Legal</h2>%s</nav>
    </aside>
    <div class="legal__body">
      <dl class="legal__meta">%s</dl>
      <div class="legal__intro">%s</div>
      %s
    </div>
  </div></div>""" % (esc(doc["title"]), esc(doc["title"]), toc, others, meta, intro, secs)
    page(doc["file"], "%s — Source Pro B2B2C" % doc["title"], doc["desc"], doc["canon"], body)


for _d in DOCS:
    legal_page(_d)
print("legal pages built")
