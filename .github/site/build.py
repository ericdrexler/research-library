#!/usr/bin/env python3
"""Build the research-library website from the repository.

Usage: python build.py SOURCE_DIR OUTPUT_DIR [BASE_URL]

Every file is copied unchanged, so each Markdown file stays available as plain
text at its own address. In addition:
  - each Markdown file gets an HTML page beside it (name.md -> name.html;
    index.md -> index.md.html, since index.html is the folder page);
  - each folder gets index.html: a breadcrumb, a table of its contents, and
    its README.md rendered below (README.md has no separate HTML page);
  - sitemap.xml lists every page, for search engines.
Requires markdown-it-py and PyYAML. Run by .github/workflows/pages.yml.
"""
import html, os, re, shutil, sys, urllib.parse
import yaml
from markdown_it import MarkdownIt

SRC, OUT = sys.argv[1], sys.argv[2]
BASE = (sys.argv[3] if len(sys.argv) > 3 else "https://ericdrexler.github.io/research-library/").rstrip("/") + "/"
REPO = "https://github.com/ericdrexler/research-library"
SKIP_DIRS = {".git", ".github", "_site", "node_modules"}
SKIP_FILES = {"index.html", ".gitignore", ".nojekyll", ".DS_Store"}
RENAME = {"LICENSE": "LICENSE.txt"}  # served with a text type

md = MarkdownIt("commonmark", {"html": True, "typographer": False}).enable(["table", "strikethrough"])

# ---------- helpers ----------

def html_name(fname):
    """Address of the HTML page for a Markdown file name (README -> folder)."""
    if fname == "README.md":
        return ""
    if fname == "index.md":
        return "index.md.html"
    return fname[:-3] + ".html"

def slugify(text, seen):
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE).replace(" ", "-")
    base, n = s, 1
    while s in seen:
        s = f"{base}-{n}"; n += 1
    seen.add(s)
    return s

def split_front_matter(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            try:
                meta = yaml.safe_load(text[4:end])
                if isinstance(meta, dict):
                    return meta, text[end + 5:]
            except yaml.YAMLError:
                pass
    return None, text

def section_map(edition_dir):
    """Map section numbers to edition file names (NN-secMM-name.md -> MM)."""
    m = {}
    if os.path.isdir(edition_dir):
        for f in os.listdir(edition_dir):
            g = re.match(r"\d+-sec(\d+)-.*\.md$", f)
            if g:
                m[int(g.group(1))] = f
    return m

EDITION = "works/2019-reframing-superintelligence/edition"
SECTIONS = section_map(os.path.join(SRC, EDITION))

def rewrite_href(href, rel_dir):
    """Point links to Markdown files at their HTML pages; resolve →§N cross-references."""
    raw = urllib.parse.unquote(href)
    if raw.startswith("→"):
        g = re.match(r"→§(\d+)$", raw)
        if g and int(g.group(1)) in SECTIONS:
            target = os.path.join(EDITION, SECTIONS[int(g.group(1))])
            return os.path.relpath(target, rel_dir or ".")[:-3] + ".html"
        return None  # unresolved cross-reference: render as text
    if re.match(r"^[a-z][a-z0-9+.-]*:", raw) or raw.startswith(("#", "/")):
        return href
    path, _, frag = href.partition("#")
    if path.endswith(".md"):
        d, f = os.path.split(path)
        new = html_name(f)
        path = (d + "/" if d else "") + (new if new else "")
        if not path:
            path = "./"
    elif os.path.basename(path) in RENAME:
        path = path[: -len(os.path.basename(path))] + RENAME[os.path.basename(path)]
    return path + ("#" + frag if frag else "")

FN_DEF = re.compile(r"^\[\^([\w-]+)\]:[ \t]+(.*)$", re.M)
FN_REF = re.compile(r"\[\^([\w-]+)\]")

def render(text, rel_dir):
    """Markdown to HTML, with heading ids, footnotes and rewritten links."""
    defs = {k: v for k, v in FN_DEF.findall(text)}
    if defs:
        text = FN_DEF.sub("", text)
        order = []
        def ref(m):
            k = m.group(1)
            if k not in defs:
                return m.group(0)
            if k not in order:
                order.append(k)
            n = order.index(k) + 1
            return f'<sup class="fn" id="fnref-{k}"><a href="#fn-{k}">{n}</a></sup>'
        text = FN_REF.sub(ref, text)
    tokens = md.parse(text)
    seen = set()
    for i, t in enumerate(tokens):
        if t.type == "heading_open":
            t.attrSet("id", slugify(tokens[i + 1].content, seen))
        if t.type == "inline" and t.children:
            kids = t.children
            for j, c in enumerate(kids):
                if c.type == "link_open":
                    new = rewrite_href(c.attrGet("href") or "", rel_dir)
                    if new is None:
                        c.type, c.tag = "html_inline", ""
                        c.content = '<span class="xref">'
                        c.attrs = {}
                        depth = 0
                        for k in range(j + 1, len(kids)):
                            if kids[k].type == "link_open":
                                depth += 1
                            elif kids[k].type == "link_close":
                                if depth == 0:
                                    kids[k].type, kids[k].tag, kids[k].content = "html_inline", "", "</span>"
                                    break
                                depth -= 1
                    else:
                        c.attrSet("href", new)
    out = md.renderer.render(tokens, md.options, {})
    if defs and order:
        items = "".join(
            f'<li id="fn-{k}">{md.renderInline(defs[k])} <a href="#fnref-{k}" aria-label="back">↩</a></li>'
            for k in order)
        out += f'<section class="footnotes"><hr><ol>{items}</ol></section>'
    return out

def first_paragraph(body):
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if b and not b.startswith(("#", "<!--", "|", "```", "---", ">", "-", "*")) and len(b) > 60:
            plain = re.sub(r"[*_`]|\[([^\]]*)\]\([^)]*\)", r"\1", b)
            return re.sub(r"\s+", " ", plain)
    return ""

def title_of(meta, body, fallback):
    if meta and meta.get("title"):
        return str(meta["title"])
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return re.sub(r"[*_`]", "", m.group(1)).strip() if m else fallback

def words(path):
    try:
        with open(path, encoding="utf-8") as f:
            return len(f.read().split())
    except (UnicodeDecodeError, OSError):
        return 0

CSS = """:root{--bg:#fdfdfb;--fg:#1d1d1b;--mute:#5d5d58;--line:#dcdcd4;--link:#1f5fa8;--code:#f1f1ec}
@media (prefers-color-scheme:dark){:root{--bg:#141413;--fg:#e6e6e0;--mute:#a3a39b;--line:#3a3a36;--link:#8ab8ef;--code:#22221f}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 Georgia,'Iowan Old Style',serif}
main{max-width:46rem;margin:0 auto;padding:1.5rem 16px 4rem}a{color:var(--link)}
nav.crumbs,.meta-line,.listing,.meta,footer{font-family:system-ui,-apple-system,sans-serif;font-size:.88rem}
nav.crumbs{color:var(--mute);margin-bottom:.4rem}.meta-line{color:var(--mute);margin:.2rem 0 1.2rem}
h1,h2,h3,h4{line-height:1.25;font-family:system-ui,-apple-system,sans-serif}h1{font-size:1.7rem}
table{border-collapse:collapse;width:100%;display:block;overflow-x:auto;font-size:.92rem}
th,td{border:1px solid var(--line);padding:.35rem .5rem;vertical-align:top;text-align:left}
code{background:var(--code);padding:.05rem .25rem;border-radius:3px;font-size:.88em}
pre{background:var(--code);padding:.7rem;overflow-x:auto}pre code{padding:0}
blockquote{border-left:3px solid var(--line);margin-left:0;padding-left:1rem;color:var(--mute)}
.meta td:first-child{white-space:nowrap;color:var(--mute)}.listing td:nth-child(-n+3){white-space:nowrap}
.xref{border-bottom:1px dotted var(--mute)}sup.fn a{text-decoration:none}
footer{color:var(--mute);margin-top:3rem;border-top:1px solid var(--line);padding-top:.8rem}
"""

def page(title, desc, url, rel_root, crumbs, body, alt_md=None):
    alt = f'<link rel="alternate" type="text/markdown" href="{html.escape(alt_md)}">' if alt_md else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc[:300])}">
<link rel="canonical" href="{html.escape(url)}">{alt}
<link rel="stylesheet" href="{rel_root}site.css">
</head><body><main>
<nav class="crumbs">{crumbs}</nav>
{body}
<footer>research-library · <a href="{rel_root}llms.txt">llms.txt</a> (entry point for models) · <a href="{REPO}">GitHub repository</a> · CC0 1.0 except where stated</footer>
</main></body></html>
"""

def crumbs_for(rel_dir, leaf=None):
    parts = [p for p in rel_dir.split("/") if p] if rel_dir else []
    depth = len(parts)
    links = [f'<a href="{"../" * depth or "./"}">research-library</a>']
    for i, p in enumerate(parts):
        up = depth - i - 1
        links.append(f'<a href="{"../" * up or "./"}">{html.escape(p)}</a>' if (leaf or up) else html.escape(p))
    if leaf:
        links.append(html.escape(leaf))
    return " / ".join(links)

def meta_table(meta):
    rows = []
    for k, v in meta.items():
        if k == "related" and isinstance(v, list):
            cell = ", ".join(f'<a href="{html.escape(str(x))}">{html.escape(str(x).strip("./").split("/")[-1] or str(x))}</a>' for x in v)
        else:
            cell = html.escape(", ".join(str(x) for x in v) if isinstance(v, list) else str(v))
        rows.append(f"<tr><td>{html.escape(str(k))}</td><td>{cell}</td></tr>")
    return f'<table class="meta">{"".join(rows)}</table>'

# ---------- build ----------

if os.path.exists(OUT):
    shutil.rmtree(OUT)
pages = []

for dirpath, dirnames, filenames in os.walk(SRC):
    dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
    rel_dir = os.path.relpath(dirpath, SRC)
    rel_dir = "" if rel_dir == "." else rel_dir.replace(os.sep, "/")
    out_dir = os.path.join(OUT, rel_dir)
    os.makedirs(out_dir, exist_ok=True)
    rel_root = "../" * len([p for p in rel_dir.split("/") if p])
    files = sorted(f for f in filenames if f not in SKIP_FILES)
    listing = []

    for f in files:
        src = os.path.join(dirpath, f)
        served = RENAME.get(f, f)
        shutil.copy2(src, os.path.join(out_dir, served))
        if not f.endswith(".md"):
            kind = "PDF" if f.lower().endswith(".pdf") else "text"
            size = f"{os.path.getsize(src) // 1024 + 1} KB" if kind == "PDF" else f"{words(src):,} words"
            listing.append((f'<a href="{served}">{html.escape(served)}</a>', kind, size, ""))
            continue
        with open(src, encoding="utf-8") as fh:
            text = fh.read()
        meta, body = split_front_matter(text)
        title = title_of(meta, body, f)
        if f != "README.md":
            target = html_name(f)
            url = BASE + (rel_dir + "/" if rel_dir else "") + target
            head = (f'<p class="meta-line">Plain text: <a href="{f}">{f}</a> · '
                    f'<a href="{REPO}/blob/main/{(rel_dir + "/" if rel_dir else "") + f}">on GitHub</a></p>')
            content = (meta_table(meta) if meta else "") + render(body, rel_dir)
            with open(os.path.join(out_dir, target), "w", encoding="utf-8") as oh:
                oh.write(page(title, first_paragraph(body) or title, url, rel_root,
                              crumbs_for(rel_dir, f), head + content, alt_md=f))
            pages.append(url)
            listing.append((f'<a href="{target}">{html.escape(f)}</a>', f'<a href="{f}">plain text</a>',
                            f"{len(text.split()):,} words", html.escape(title)))
        else:
            listing.insert(0, (f'<a href="#readme">README.md</a>', f'<a href="README.md">plain text</a>',
                               f"{len(text.split()):,} words", html.escape(title)))

    sub = []
    for d in dirnames:
        rp = os.path.join(dirpath, d, "README.md")
        t = ""
        if os.path.exists(rp):
            with open(rp, encoding="utf-8") as fh:
                m_, b_ = split_front_matter(fh.read())
            t = title_of(m_, b_, "")
        n = sum(len(fs) for _, _, fs in os.walk(os.path.join(dirpath, d)))
        sub.append((f'<a href="{d}/">{html.escape(d)}/</a>', "folder", f"{n} files", html.escape(t)))

    rows = "".join(f'<tr><td class="n">{a}</td><td>{b}</td><td>{c}</td><td>{e}</td></tr>' for a, b, c, e in sub + listing)
    readme_path = os.path.join(dirpath, "README.md")
    readme_html, title, desc = "", (rel_dir.split("/")[-1] if rel_dir else "research-library"), ""
    if os.path.exists(readme_path):
        with open(readme_path, encoding="utf-8") as fh:
            meta, body = split_front_matter(fh.read())
        title = title_of(meta, body, title)
        desc = first_paragraph(body)
        readme_html = (f'<section id="readme"><p class="meta-line">README.md · plain text: '
                       f'<a href="README.md">README.md</a></p>' + (meta_table(meta) if meta else "")
                       + render(body, rel_dir) + "</section>")
    intro = ""
    if not rel_dir:
        intro = ('<p class="meta-line"><strong>Models and tools:</strong> start with <a href="llms.txt">llms.txt</a>, '
                 'which links every item\'s files as plain text. Every Markdown file is served both as plain text '
                 '(name.md) and as a page (name.html).</p>')
    folder_label = "/" + rel_dir + "/" if rel_dir else "/"
    listing_html = (f'<h2 style="font-size:1rem">Contents of {html.escape(folder_label)}</h2>'
                    f'<table class="listing"><tr><th>Name</th><th>Form</th><th>Size</th><th>Title</th></tr>{rows}</table>')
    url = BASE + (rel_dir + "/" if rel_dir else "")
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as oh:
        oh.write(page(title, desc or title, url, rel_root, crumbs_for(rel_dir), intro + listing_html + readme_html))
    pages.append(url)

with open(os.path.join(OUT, "site.css"), "w") as fh:
    fh.write(CSS)
with open(os.path.join(OUT, "sitemap.xml"), "w") as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in sorted(set(pages)):
        fh.write(f"  <url><loc>{html.escape(u)}</loc></url>\n")
    fh.write("</urlset>\n")
print(f"built {len(set(pages))} pages into {OUT}")
