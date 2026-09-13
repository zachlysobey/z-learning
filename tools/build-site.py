#!/usr/bin/env python3
"""Build the GitHub Pages site for z-learning into _site/.

Zero configuration: every top-level directory with a README.md becomes a topic
landing page. Lessons and reference sheets are discovered by globbing; their
titles come from the HTML itself. Markdown notes are not rendered, they are
linked back to GitHub. Adding a lesson or a topic needs no edit to this file.
"""

from __future__ import annotations

import html
import os
import re
import shutil
import subprocess
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
SKIP = {"tools", "node_modules"}
# (light, dark) accent pairs for topics that have no stylesheet of their own.
# Picked by a stable hash of the directory name, so colours never shift.
FALLBACK_ACCENTS = [
    ("#6b4fbb", "#b39ddb"),
    ("#0f766e", "#5eead4"),
    ("#1d4ed8", "#93b8ff"),
    ("#3f6212", "#a3d977"),
    ("#9d174d", "#f0a6c0"),
]
DEFAULT_ACCENT = FALLBACK_ACCENTS[0]
COPY_DIRS = ("assets", "lessons", "reference")
NOTE_FILES = ("MISSION.md", "GLOSSARY.md", "RESOURCES.md", "NOTES.md")


# --- tiny markdown-to-inline-HTML, enough for a one-paragraph blurb ----------

def inline_md(text: str) -> str:
    out = html.escape(" ".join(text.split()))
    out = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", out)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*(.+?)\*\*(?!\*)", r"<strong>\1</strong>", out)
    out = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", out)
    return out


def read_readme(path: Path) -> tuple[str, str]:
    """Return (title, blurb) from a README: its first heading and paragraph."""
    title, blurb, lines = path.parent.name, [], path.read_text().splitlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith("# "):
            title = lines[i][2:].strip()
            i += 1
            break
        i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    while i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
        blurb.append(lines[i])
        i += 1
    return title, inline_md(" ".join(blurb))


# --- HTML lesson metadata ---------------------------------------------------

def page_meta(path: Path) -> tuple[str, str]:
    """Return (title, subtitle) for a lesson or reference sheet."""
    text = path.read_text()
    t = re.search(r"<title>(.*?)</title>", text, re.S)
    s = re.search(r'<p class="subtitle">(.*?)</p>', text, re.S)
    clean = lambda m, fb: " ".join(re.sub(r"<[^>]+>", "", m.group(1)).split()) if m else fb
    return clean(t, path.stem), clean(s, "")


def accent_of(topic: Path) -> tuple[str, str]:
    """The topic's (light, dark) accent, reusing its own stylesheet if it has one."""
    css = topic / "assets" / "style.css"
    if css.exists():
        light_src, _, dark_src = css.read_text().partition("prefers-color-scheme: dark")
        light = re.findall(r"--accent:\s*([^;]+);", light_src)
        dark = re.findall(r"--accent:\s*([^;]+);", dark_src)
        if light:
            return light[0].strip(), (dark[0].strip() if dark else light[0].strip())
    return FALLBACK_ACCENTS[zlib.crc32(topic.name.encode()) % len(FALLBACK_ACCENTS)]


def repo_slug() -> str:
    slug = os.environ.get("GITHUB_REPOSITORY")
    if slug:
        return slug
    try:
        url = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip()
        m = re.search(r"[:/]([^/:]+/[^/]+?)(?:\.git)?$", url)
        if m:
            return m.group(1)
    except Exception:
        pass
    return "zachlysobey/z-learning"


BLOB = f"https://github.com/{repo_slug()}/blob/main"


# --- page rendering ---------------------------------------------------------

def shell(title: str, accent: tuple[str, str], depth: int, body: str) -> str:
    css = "../" * depth + "site.css"
    light, dark = accent
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{css}">
<style>
:root {{ --accent: {light}; }}
@media (prefers-color-scheme: dark) {{ :root {{ --accent: {dark}; }} }}
</style>
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""


def link_list(items: list[tuple[str, str, str]]) -> str:
    rows = []
    for href, title, note in items:
        note_html = f'<span class="note">{html.escape(note)}</span>' if note else ""
        rows.append(
            f'<li><a href="{html.escape(href)}">{html.escape(title)}</a>{note_html}</li>'
        )
    return '<ul class="links">\n' + "\n".join(rows) + "\n</ul>"


def built_pdfs(topic: Path) -> list[Path]:
    """PDFs we are allowed to publish: only those built from a .tex source here.

    Keeps unrelated PDFs sitting in a topic directory (reference books, scans)
    out of the public site, whatever the local working tree happens to contain.
    """
    return [p for p in sorted(topic.glob("*.pdf")) if p.with_suffix(".tex").exists()]


def collect(topic: Path) -> dict:
    title, blurb = read_readme(topic / "README.md")
    lessons = [(f"lessons/{p.name}", *page_meta(p))
               for p in sorted((topic / "lessons").glob("*.html"))]
    refs = [(f"reference/{p.name}", *page_meta(p))
            for p in sorted((topic / "reference").glob("*.html"))]
    pdfs = [(p.name, p.stem.replace("-", " ").capitalize(), f"{p.stat().st_size // 1024} KB")
            for p in built_pdfs(topic)]
    notes = [(f"{BLOB}/{topic.name}/{n}", n, "")
             for n in NOTE_FILES if (topic / n).exists()]
    notes += [(f"{BLOB}/{topic.name}/learning-records/{p.name}", p.name, "")
              for p in sorted((topic / "learning-records").glob("*.md"))]
    return dict(name=topic.name, title=title, blurb=blurb, accent=accent_of(topic),
                lessons=lessons, refs=refs, pdfs=pdfs, notes=notes)


def topic_page(t: dict) -> str:
    parts = [
        '<nav class="crumbs"><a href="../">z-learning</a></nav>',
        f'<h1>{html.escape(t["title"])}</h1>',
        f'<p class="lede">{t["blurb"]}</p>',
    ]
    for heading, items in (
        ("Lessons", t["lessons"]),
        ("Reference sheets", t["refs"]),
        ("Documents", t["pdfs"]),
    ):
        if items:
            parts += [f"<h2>{heading}</h2>", link_list(items)]
    if t["notes"]:
        parts += ["<h2>Notes on GitHub</h2>", link_list(t["notes"])]
    parts.append(
        f'<p class="foot"><a href="{BLOB}/{t["name"]}">Source for this topic on GitHub</a></p>'
    )
    return shell(t["title"], t["accent"], 1, "\n".join(parts))


def index_page(topics: list[dict], title: str, blurb: str) -> str:
    cards, dark_rules = [], []
    for t in topics:
        counts = []
        for n, word in ((len(t["lessons"]), "lesson"),
                        (len(t["refs"]), "reference sheet"),
                        (len(t["pdfs"]), "document")):
            if n:
                counts.append(f"{n} {word}{'s' if n != 1 else ''}")
        meta = f'<p class="note">{" · ".join(counts)}</p>' if counts else ""
        light, dark = t["accent"]
        cards.append(
            f'<li class="{t["name"]}" style="--accent: {light}">'
            f'<a class="card-title" href="{t["name"]}/">{html.escape(t["title"])}</a>'
            f'<p>{t["blurb"]}</p>{meta}</li>'
        )
        dark_rules.append(f'  ul.cards li.{t["name"]} {{ --accent: {dark}; }}')
    dark = ("<style>\n@media (prefers-color-scheme: dark) {\n"
            + "\n".join(dark_rules) + "\n}\n</style>\n")
    body = (
        f'<h1>{html.escape(title)}</h1>\n<p class="lede">{blurb}</p>\n'
        + dark + '<ul class="cards">\n' + "\n".join(cards) + "\n</ul>\n"
        + f'<p class="foot"><a href="https://github.com/{repo_slug()}">Repository on GitHub</a></p>'
    )
    return shell(title, DEFAULT_ACCENT, 0, body)


# --- build ------------------------------------------------------------------

def copy_topic(topic: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for sub in COPY_DIRS:
        src = topic / sub
        if src.is_dir():
            shutil.copytree(src, dest / sub, dirs_exist_ok=True)
    for pdf in built_pdfs(topic):
        shutil.copy2(pdf, dest / pdf.name)
    # Breadcrumbs point at Markdown files that Pages does not render; send them
    # to the topic landing page instead.
    for page in dest.rglob("*.html"):
        text = page.read_text()
        fixed = re.sub(r'href="\.\./[A-Za-z0-9._-]+\.md"', 'href="../"', text)
        if fixed != text:
            page.write_text(fixed)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    topics = []
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        if d.name.startswith((".", "_")) or d.name in SKIP or not (d / "README.md").exists():
            continue
        t = collect(d)
        copy_topic(d, OUT / d.name)
        (OUT / d.name / "index.html").write_text(topic_page(t))
        topics.append(t)

    title, blurb = read_readme(ROOT / "README.md")
    (OUT / "index.html").write_text(index_page(topics, title, blurb))
    shutil.copy2(ROOT / "tools" / "site.css", OUT / "site.css")
    (OUT / ".nojekyll").write_text("")

    for t in topics:
        print(f"{t['name']}: {len(t['lessons'])} lessons, "
              f"{len(t['refs'])} reference, {len(t['pdfs'])} pdf")
    print(f"built {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
