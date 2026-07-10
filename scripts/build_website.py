#!/usr/bin/env python3
"""Generate the static learning-navigator website (Ukrainian) from the wiki.

Reads wiki/ (videos, clusters, concepts, tools, books) and transcripts/timed/
(durations), writes a self-contained static site to website/. Stdlib only.

Usage: python3 scripts/build_website.py
"""
import html
import json
import math
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
TIMED = ROOT / "transcripts" / "timed"
OUT = ROOT / "website"

SITE_NAME = "Віктор Турський про програмування · навігатор"
CHANNEL_URL = "https://www.youtube.com/@AboutProgramming"
SITE_URL = "https://koorchik.github.io/jabascript-map/"

# Streams whose content is time-bound and stale — kept in the wiki, hidden on the site.
EXCLUDED = {"google-io-2023-watch-party", "qa-and-plans-for-2024"}

# Presentation config: global track order, display names, taglines, accent hue.
TRACKS = [
    ("engineering-craft-and-career", "Інженерна майстерність і карʼєра",
     "Почніть звідси. Теза каналу — вивчати все глибоко, — а ще кодревʼю в Google, "
     "дизайн програмного забезпечення і чесна механіка карʼєри.", 145),
    ("networking-and-internet", "Мережі та інтернет",
     "Як насправді працює інтернет, з перших принципів: швидкість світла, DNS, "
     "DHCP і що насправді робить ваш Wi-Fi.", 190),
    ("databases-and-data-structures", "Бази даних і структури даних",
     "Найщільніший трек каналу: від «чому мій запит повільний» до власноруч "
     "побудованих інвертованих індексів і фільтрів Блума — усе з живими вимірами.", 38),
    ("security-and-cryptography", "Безпека і криптографія",
     "Хешування, кодування чи шифрування? Асиметрична криптографія, цифрові підписи "
     "та історії атак від людини з infosec-бекґраундом.", 2),
    ("ai-and-vibe-coding", "ШІ та вайб-кодинг",
     "Шлях від скепсису щодо Gemini у 2023-му до повноцінних стрімів вайб-кодингу — "
     "і чому з ШІ фундаментальні знання важать більше, а не менше.", 270),
    ("channel-meta", "Про канал",
     "Бонусний трек: Q&A-стріми, голосові історії та хто такий Віктор. "
     "Порядок перегляду тут менш важливий.", 215),
]

LEVEL_UK = {"beginner": "початковий", "intermediate": "середній", "advanced": "просунутий"}

# Section headings: Ukrainian is canonical, English accepted as legacy.
SECTION_ALIASES = {
    "chapters": ("Розділи", "Chapters"),
    "takeaways": ("Головне", "Key takeaways"),
    "covered": ("Теми", "Covered"),
    "covered_in": ("Де розглядається", "Covered in"),
    "related": ("Повʼязане", "Пов'язане", "Related"),
}

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)


# ---------------------------------------------------------------- parsing

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
H2_RE = re.compile(r"^## +(.+?)\s*$", re.M)
CHAPTER_RE = re.compile(r"^- ((?:\d{1,2}:)?\d{1,2}:\d{2}) — (.+?)\s*$", re.M)
PATH_ITEM_RE = re.compile(r"^\d+\.\s+\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]\s*—?\s*(.*?)\s*$", re.M)
BULLET_LINK_RE = re.compile(r"^- +\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]\s*—?\s*(.*?)\s*$", re.M)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]")


def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            fm[key.strip()] = [v.strip() for v in val[1:-1].split(",") if v.strip()]
        else:
            fm[key.strip()] = val.strip("\"'")
    return fm, text[m.end():]


def split_sections(body):
    """Return (preamble, [(heading, content), ...]) split on H2 headings."""
    parts = H2_RE.split(body)
    preamble = parts[0]
    sections = [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]
    return preamble, sections


def sect(page, key):
    for name in SECTION_ALIASES[key]:
        if name in page["sections"]:
            return page["sections"][name]
    return ""


def parse_ts(ts):
    parts = [int(p) for p in ts.split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)
    h, m, s = parts
    return h * 3600 + m * 60 + s


def fmt_ts(sec):
    h, rem = divmod(int(sec), 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def fmt_dur(sec):
    h, rem = divmod(int(round(sec / 60) * 60), 3600)
    m = rem // 60
    if h and m:
        return f"{h} год {m} хв"
    if h:
        return f"{h} год"
    return f"{max(m, 1)} хв"


def uk_plural(n, one, few, many):
    n = abs(int(n))
    if n % 10 == 1 and n % 100 != 11:
        return one
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return few
    return many


def first_paragraph(preamble):
    for block in re.split(r"\n\s*\n", preamble):
        block = " ".join(block.split())
        if not block or block.startswith("#") or block.startswith(">"):
            continue
        return block
    return ""


def prose_blocks(preamble):
    out = []
    for block in re.split(r"\n\s*\n", preamble):
        text = " ".join(block.split())
        if not text or text.startswith("#") or text.startswith(">"):
            continue
        out.append(text)
    return out


def load_pages():
    pages = {}
    for sub in ("videos", "concepts", "tools", "books", "clusters"):
        for f in sorted((WIKI / sub).glob("*.md")):
            if f.stem in EXCLUDED:
                continue
            fm, body = parse_frontmatter(f.read_text(encoding="utf-8"))
            preamble, sections = split_sections(body)
            m = re.search(r"^# +(.+?)\s*$", body, re.M)
            pages[f.stem] = {
                "slug": f.stem, "kind": sub, "fm": fm,
                "title": m.group(1) if m else f.stem,
                "preamble": preamble, "sections": dict(sections),
            }
    return pages


def load_durations():
    durations = {}
    for f in TIMED.glob("*.uk.txt"):
        for line in f.read_text(encoding="utf-8").splitlines()[:4]:
            if line.startswith("# duration:"):
                durations[f.name.split(".")[0]] = parse_ts(line.split(": ")[1])
    return durations


# ---------------------------------------------------------------- model

def build_model(pages, durations):
    videos, tracks = {}, {}
    for p in pages.values():
        if p["kind"] != "clusters" and not p["fm"].get("tags"):
            warn(f"{p['slug']}: no tags")
    for p in pages.values():
        if p["kind"] != "videos":
            continue
        vid = p["fm"].get("youtube_id", "")
        chapters = []
        for ts, label in CHAPTER_RE.findall(sect(p, "chapters")):
            chapters.append((parse_ts(ts), label))
        takeaways = [" ".join(l[2:].split()) for l in
                     sect(p, "takeaways").splitlines() if l.startswith("- ")]
        covered = [m[0] for m in WIKILINK_RE.findall(sect(p, "covered"))]
        dur = durations.get(vid)
        videos[p["slug"]] = {
            **p, "youtube_id": vid, "title_uk": p["fm"].get("title_uk", ""),
            "level": p["fm"].get("level", ""), "summary": first_paragraph(p["preamble"]),
            "takeaways": takeaways, "chapters": chapters, "covered": covered,
            "duration": dur,
        }
        # validation
        if not chapters:
            warn(f"{p['slug']}: no chapters")
        else:
            if chapters[0][0] != 0:
                warn(f"{p['slug']}: first chapter is not 00:00")
            secs = [c[0] for c in chapters]
            if secs != sorted(set(secs)):
                warn(f"{p['slug']}: chapter times not strictly increasing")
            if dur and secs[-1] >= dur:
                warn(f"{p['slug']}: last chapter {fmt_ts(secs[-1])} >= duration {fmt_ts(dur)}")
            if len(chapters) < 3:
                warn(f"{p['slug']}: only {len(chapters)} chapters")
        if not p["fm"].get("level"):
            warn(f"{p['slug']}: no level")
        if dur is None:
            warn(f"{p['slug']}: no timed transcript for {vid}")

    for slug, name, tagline, hue in TRACKS:
        p = pages.get(slug)
        if not p:
            warn(f"track {slug}: cluster page missing")
            continue
        section = next((c for h, c in p["sections"].items()
                        if h.lower().startswith(("videos", "відео"))), "")
        path = []
        for vslug, note in PATH_ITEM_RE.findall(section):
            if vslug in EXCLUDED:
                continue
            if vslug in videos:
                path.append((vslug, note))
            else:
                warn(f"track {slug}: path entry [[{vslug}]] is not a video page")
        if not path:
            warn(f"track {slug}: no numbered learning path found")
        tracks[slug] = {
            "slug": slug, "name": name, "tagline": tagline, "hue": hue,
            "intro": prose_blocks(p["preamble"]), "path": path,
        }

    in_track = {v for t in tracks.values() for v, _ in t["path"]}
    for slug in videos:
        if slug not in in_track:
            warn(f"{slug}: not in any track's learning path")
    return videos, tracks


def primary_hue(slug, tracks):
    for tslug, _n, _t, hue in TRACKS:
        t = tracks.get(tslug)
        if t and any(s == slug for s, _ in t["path"]):
            return hue
    return None


# ---------------------------------------------------------------- concept map

MAP_W, MAP_H = 1150, 900


def chip_size(title):
    w = min(7.0 * len(title) + 30, 210)
    return w, 26.0


def layout_map(nodes, edges, sizes):
    """Deterministic Fruchterman–Reingold + rectangle de-overlap. No randomness."""
    order = sorted(nodes)
    n = max(len(order), 1)
    pos = {}
    for i, s in enumerate(order):
        a = 2 * math.pi * i / n
        r = (0.30 + 0.12 * ((i * 7) % 13) / 13) * min(MAP_W, MAP_H)
        pos[s] = [MAP_W / 2 + r * math.cos(a), MAP_H / 2 + r * math.sin(a)]
    k = math.sqrt(MAP_W * MAP_H / n) * 0.95
    temp = MAP_W / 8
    for it in range(200):
        disp = {s: [0.0, 0.0] for s in order}
        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                a, b = order[i], order[j]
                dx = pos[a][0] - pos[b][0]
                dy = (pos[a][1] - pos[b][1]) * 1.9  # wide chips: repel harder vertically
                d2 = dx * dx + dy * dy
                d = math.sqrt(d2) if d2 > 1e-6 else 0.001
                f = k * k / d
                disp[a][0] += dx / d * f; disp[a][1] += dy / d * f
                disp[b][0] -= dx / d * f; disp[b][1] -= dy / d * f
        # sorted: float accumulation order must be deterministic (edges is a set,
        # and set iteration order varies with hash randomization between runs)
        for a, b in sorted(edges):
            dx = pos[a][0] - pos[b][0]
            dy = pos[a][1] - pos[b][1]
            d = math.sqrt(dx * dx + dy * dy) or 0.001
            f = d * d / k
            disp[a][0] -= dx / d * f; disp[a][1] -= dy / d * f
            disp[b][0] += dx / d * f; disp[b][1] += dy / d * f
        for s in order:
            dx, dy = disp[s]
            d = math.sqrt(dx * dx + dy * dy) or 0.001
            step = min(d, temp)
            pos[s][0] += dx / d * step
            pos[s][1] += dy / d * step
        temp = max(temp * 0.96, 1.5)
    # de-overlap chip rectangles, then clamp inside the canvas
    for _ in range(80):
        moved = False
        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                a, b = order[i], order[j]
                aw, ah = sizes[a]; bw, bh = sizes[b]
                ox = (aw + bw) / 2 + 14 - abs(pos[a][0] - pos[b][0])
                oy = (ah + bh) / 2 + 12 - abs(pos[a][1] - pos[b][1])
                if ox > 0 and oy > 0:
                    moved = True
                    if ox * 0.35 < oy:  # cheaper to separate horizontally
                        push, axis = ox / 2, 0
                    else:
                        push, axis = oy / 2, 1
                    sign = 1 if pos[a][axis] >= pos[b][axis] else -1
                    pos[a][axis] += sign * push
                    pos[b][axis] -= sign * push
        if not moved:
            break
    for s in order:
        w, h = sizes[s]
        pos[s][0] = min(max(pos[s][0], w / 2 + 8), MAP_W - w / 2 - 8)
        pos[s][1] = min(max(pos[s][1], h / 2 + 8), MAP_H - h / 2 - 8)
    return pos


def build_concept_map(pages, videos, tracks):
    concepts = {p["slug"]: p for p in pages.values() if p["kind"] == "concepts"}
    votes = {s: {} for s in concepts}
    count = {s: 0 for s in concepts}
    for vslug, v in videos.items():
        hue = primary_hue(vslug, tracks)
        for c in v["covered"]:
            if c in concepts:
                count[c] += 1
                if hue is not None:
                    votes[c][hue] = votes[c].get(hue, 0) + 1
    hues = {s: (max(votes[s], key=votes[s].get) if votes[s] else 215) for s in concepts}
    edges = set()
    for s, p in concepts.items():
        for m in WIKILINK_RE.findall(sect(p, "related")):
            t = m[0].strip()
            if t in concepts and t != s:
                edges.add(tuple(sorted((s, t))))
    sizes = {s: chip_size(concepts[s]["title"]) for s in concepts}
    pos = layout_map(set(concepts), edges, sizes)
    return concepts, edges, pos, hues, count


def render_concept_map(pages, videos, tracks):
    concepts, edges, pos, hues, count = build_concept_map(pages, videos, tracks)
    lines = []
    for a, b in sorted(edges):
        x1, y1 = pos[a]; x2, y2 = pos[b]
        lines.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}"/>')
    chips = []
    for s in sorted(concepts, key=lambda s: (-count[s], s)):
        x, y = pos[s]
        n = count[s]
        title = html.escape(concepts[s]["title"])
        chips.append(
            f'<a class="map-chip{" hot" if n >= 3 else ""}" href="concepts/{s}.html" '
            f'style="left:{100 * x / MAP_W:.2f}%;top:{100 * y / MAP_H:.2f}%;--h:{hues[s]}" '
            f'title="{title} · {n} відео">{title}</a>')
    return f"""<section class="map-section">
  <h2>Мапа знань</h2>
  <p class="meta map-hint">Усі концепції каналу та звʼязки між ними — кольори відповідають трекам.
  Клікніть на будь-яку, щоб побачити, які відео (і з якої хвилини) її пояснюють.</p>
  <div class="map-scroll">
    <div class="map">
      <svg viewBox="0 0 {MAP_W} {MAP_H}" preserveAspectRatio="none" aria-hidden="true">{"".join(lines)}</svg>
      {"".join(chips)}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- html

def url_for(slug, pages):
    p = pages.get(slug)
    if not p:
        return None
    kind = p["kind"]
    if kind == "videos":
        return f"videos/{slug}.html"
    if kind == "clusters":
        return f"tracks/{slug}.html"
    if kind == "concepts":
        return f"concepts/{slug}.html"
    if kind == "tools":
        return f"tools/{slug}.html"
    if kind == "books":
        return f"books.html#{slug}"
    return None


def md_inline(text, pages, depth, source=""):
    """Escape + convert wikilinks, bold, italics, code to HTML."""
    prefix = "../" * depth
    out, pos = [], 0
    for m in WIKILINK_RE.finditer(text):
        out.append(html.escape(text[pos:m.start()]))
        slug, disp = m.group(1).strip(), m.group(2) or m.group(1)
        u = url_for(slug, pages)
        if u:
            label = disp if m.group(2) else pages[slug]["title"]
            out.append(f'<a href="{prefix}{u}">{html.escape(label)}</a>')
        else:
            if slug not in EXCLUDED:
                warn(f"unresolved [[{slug}]] in {source}")
            out.append(html.escape(disp))
        pos = m.end()
    out.append(html.escape(text[pos:]))
    s = "".join(out)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def meta_description(text, pages, limit=160):
    """Plain-text page description: wikilinks → display text, markdown stripped."""
    def link_text(m):
        slug, disp = m.group(1).strip(), m.group(2)
        if disp:
            return disp
        p = pages.get(slug)
        return p["title"] if p else slug
    s = WIKILINK_RE.sub(link_text, text)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"\1", s)
    s = " ".join(s.replace("`", "").split())
    if len(s) > limit:
        s = s[:limit].rsplit(" ", 1)[0].rstrip(" ,;:—–-") + "…"
    return s


def md_blocks(text, pages, depth, source=""):
    """Block-level markdown subset: H2/H3, bullet lists (with indented
    continuation lines), pipe tables, blockquotes, paragraphs."""
    out, para, items, rows = [], [], [], []

    def inline(s):
        return md_inline(s, pages, depth, source)

    def flush_para():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def flush_list():
        if items:
            lis = "".join(f"<li>{inline(' '.join(i.split()))}</li>" for i in items)
            out.append(f"<ul>{lis}</ul>")
            items.clear()

    def flush_table():
        if rows:
            head, *body_rows = rows
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            trs = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                for r in body_rows)
            out.append(f'<div class="table-scroll"><table>'
                       f"<thead><tr>{th}</tr></thead><tbody>{trs}</tbody>"
                       f"</table></div>")
            rows.clear()

    def flush():
        flush_para(); flush_list(); flush_table()

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            flush()
        elif stripped.startswith("### "):
            flush(); out.append(f"<h3>{inline(stripped[4:])}</h3>")
        elif stripped.startswith("## "):
            flush(); out.append(f"<h2>{inline(stripped[3:])}</h2>")
        elif stripped.startswith("# "):
            flush()  # the page renders its own <h1>
        elif stripped.startswith("- "):
            flush_para(); flush_table()
            items.append(stripped[2:])
        elif items and line.startswith(("  ", "\t")):
            items[-1] += " " + stripped
        elif stripped.startswith("|"):
            flush_para(); flush_list()
            # mask pipes inside [[slug|display]] so they don't split cells
            masked = WIKILINK_RE.sub(lambda m: m.group(0).replace("|", "\x00"),
                                     stripped.strip("|"))
            cells = [c.strip().replace("\x00", "|") for c in masked.split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                rows.append(cells)
        elif stripped.startswith("> "):
            flush(); out.append(f"<blockquote><p>{inline(stripped[2:])}</p></blockquote>")
        else:
            para.append(stripped)
    flush()
    return "\n".join(out)


def primary_track(slug, tracks):
    """(track, order_no, step_no) for the first TRACKS entry containing slug."""
    for i, (tslug, *_rest) in enumerate(TRACKS, 1):
        t = tracks.get(tslug)
        if not t:
            continue
        path_slugs = [s for s, _ in t["path"]]
        if slug in path_slugs:
            return t, i, path_slugs.index(slug) + 1
    return None, None, None


def tag_chips(tags, depth):
    prefix = "../" * depth
    chips = "".join(
        f'<a class="chip tag" href="{prefix}tags.html#tag-{html.escape(t)}">#{html.escape(t)}</a>'
        for t in tags)
    return f'<div class="chip-row small tag-row">{chips}</div>' if chips else ""


def level_badge(level):
    if not level:
        return ""
    return (f'<span class="badge badge-{html.escape(level)}">'
            f'{html.escape(LEVEL_UK.get(level, level))}</span>')


def chip_row(slugs, pages, depth, small=False, limit=None):
    prefix = "../" * depth
    chips = []
    for c in slugs[:limit] if limit else slugs:
        u = url_for(c, pages)
        if u:
            chips.append(f'<a class="chip" href="{prefix}{u}">{html.escape(pages[c]["title"])}</a>')
    if not chips:
        return ""
    return f'<div class="chip-row{" small" if small else ""}">{"".join(chips)}</div>'


def page_shell(*, title, body, depth, path, description="", hue=None, active="",
               og_type="website", og_image=None):
    prefix = "../" * depth
    accent = f' style="--h:{hue}"' if hue is not None else ""
    canonical = SITE_URL + path
    esc_title = html.escape(title)
    meta = [f'<link rel="canonical" href="{canonical}">']
    if description:
        esc_desc = html.escape(description)
        meta.append(f'<meta name="description" content="{esc_desc}">')
        meta.append(f'<meta property="og:description" content="{esc_desc}">')
    meta.append(f'<meta property="og:title" content="{esc_title}">')
    meta.append(f'<meta property="og:type" content="{og_type}">')
    meta.append(f'<meta property="og:url" content="{canonical}">')
    meta.append('<meta property="og:locale" content="uk_UA">')
    if og_image:
        meta.append(f'<meta property="og:image" content="{og_image}">')
    meta.append(f'<meta name="twitter:card" content="{"summary_large_image" if og_image else "summary"}">')
    meta_html = "\n".join(meta)
    nav = [("index.html", "Треки", "tracks"), ("videos.html", "Відео", "videos"),
           ("concepts.html", "Теми", "concepts"), ("tools.html", "Інструменти", "tools"),
           ("books.html", "Книги", "books"), ("overview.html", "Огляд", "overview")]
    nav_html = "".join(
        f'<a href="{prefix}{href}"{" class=\"active\"" if key == active else ""}>{label}</a>'
        for href, label, key in nav)
    return f"""<!DOCTYPE html>
<html lang="uk" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc_title}</title>
{meta_html}
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>▶</text></svg>">
<script>(function(){{var t=localStorage.getItem("jsnav-theme");if(!t)t=matchMedia("(prefers-color-scheme: light)").matches?"light":"dark";document.documentElement.dataset.theme=t;}})();</script>
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body{accent} data-root="{prefix}">
<header class="site-head">
  <a class="brand" href="{prefix}index.html"><span class="brand-mark">▶</span> Віктор Турський про програмування <span class="brand-dim">/ навігатор</span></a>
  <nav>{nav_html}</nav>
  <div class="search">
    <input id="search-input" type="search" placeholder="Пошук…" autocomplete="off" aria-label="Пошук по сайту">
    <div id="search-results" hidden></div>
  </div>
  <button id="theme-toggle" type="button" aria-label="Перемкнути тему">◐</button>
</header>
<main>
{body}
</main>
<footer class="site-foot">
  <p>Неофіційна навчальна мапа YouTube-каналу <a href="{CHANNEL_URL}">Віктор Турський про програмування</a>.
  Зібрано з транскриптів відео — таймкоди ведуть на точну хвилину на YouTube.</p>
</footer>
<script src="{prefix}assets/search-index.js" defer></script>
<script src="{prefix}assets/app.js" defer></script>
</body>
</html>
"""


def track_meta_line(track, videos):
    n = len(track["path"])
    total = sum(videos[v]["duration"] or 0 for v, _ in track["path"])
    return f"{n} відео · {fmt_dur(total)}"


def render_books_banner(n_books, pages):
    # A teaser that names a couple of well-known titles in a sentence — not a list.
    teaser_slugs = ["a-philosophy-of-software-design", "clean-architecture",
                    "designing-data-intensive-applications", "the-goal"]
    names = []
    for slug in teaser_slugs:
        p = pages.get(slug)
        if p:
            names.append(f'«<a href="books.html#{slug}">{html.escape(p["title"])}</a>»')
        if len(names) == 2:
            break
    teaser = (f"Від {names[0]} до {names[1]} — " if len(names) == 2 else "")
    return f"""<section class="books-banner">
  <div class="books-banner-glyph" aria-hidden="true">📚</div>
  <div class="books-banner-body">
    <h2>{n_books} {uk_plural(n_books, "книга", "книги", "книг")}, які радить Віктор</h2>
    <p>{teaser}з чесними вердиктами Віктора: що читати, що погортати, а до чого й не братися.</p>
  </div>
  <a class="cta" href="books.html">Відкрити полицю →</a>
</section>"""


def render_index(videos, tracks, pages):
    n_chapters = sum(len(v["chapters"]) for v in videos.values())
    total_sec = sum(v["duration"] or 0 for v in videos.values())
    n_books = sum(1 for p in pages.values() if p["kind"] == "books")
    first_track = tracks[TRACKS[0][0]]
    first_video = first_track["path"][0][0] if first_track["path"] else None
    cta = (f'<a class="cta" href="videos/{first_video}.html">Почати перегляд → '
           f'{html.escape(videos[first_video]["title"])}</a>') if first_video else ""
    books_cta = (f'<a class="cta cta-books" href="books.html">📚 {n_books} '
                 f'{uk_plural(n_books, "книга", "книги", "книг")}, які радить Віктор →</a>')

    cards = []
    for i, (slug, name, tagline, hue) in enumerate(TRACKS, 1):
        t = tracks.get(slug)
        if not t:
            continue
        slugs = ",".join(v for v, _ in t["path"])
        cards.append(f"""<a class="track-card" href="tracks/{slug}.html" style="--h:{hue}">
  <div class="track-no">{i:02d}</div>
  <h3>{html.escape(name)}</h3>
  <p>{html.escape(tagline)}</p>
  <div class="meta mono">{track_meta_line(t, videos)}</div>
  <div class="progress" data-slugs="{slugs}"><span></span></div>
</a>""")

    body = f"""<section class="hero">
  <p class="eyebrow mono">{len(videos)} відео · один канал · одна мапа</p>
  <h1>Компʼютерні науки —<br>у правильному порядку.</h1>
  <p class="lede"><a href="{CHANNEL_URL}">Віктор Турський про програмування</a> — україномовний канал про те, як усе працює насправді:
  бази даних, мережі, криптографія, ШІ та інженерна майстерність.
  Цей навігатор вибудовує {len(videos)} відео у шість навчальних треків,
  веде до потрібної хвилини кожного відео на YouTube — а ще збирає полицю
  з {n_books} {uk_plural(n_books, "книги", "книг", "книг")}, які радить Віктор.</p>
  <div class="stats mono">
    <span><b>{len(videos)}</b> відео</span>
    <span><b>{len(tracks)}</b> {uk_plural(len(tracks), "трек", "треки", "треків")}</span>
    <span><b>{n_chapters}</b> {uk_plural(n_chapters, "розділ", "розділи", "розділів")}</span>
    <span><b>{n_books}</b> {uk_plural(n_books, "книга", "книги", "книг")}</span>
    <span><b>{fmt_dur(total_sec)}</b> матеріалу</span>
  </div>
  <div class="cta-row">{cta}{books_cta}</div>
</section>
<section class="how">
  <h2>Як цим користуватися</h2>
  <ol class="how-list">
    <li><b>Оберіть трек.</b> Кожен — це продуманий порядок перегляду: кожне відео готує до наступного.</li>
    <li><b>Йдіть за кроками.</b> Нумерація не випадкова: починайте з 01, якщо не впевнені, що можна інакше.</li>
    <li><b>Стрибайте по розділах.</b> Кожне відео розбите на розділи — клік по таймкоду відкриває саме те пояснення.</li>
    <li><b>Відмічайте переглянуте.</b> Прогрес зберігається у вашому браузері й більше ніде.</li>
  </ol>
</section>
<section class="tracks" id="tracks">
  <h2>Шість треків</h2>
  <div class="track-grid">
  {"".join(cards)}
  </div>
</section>
{render_books_banner(n_books, pages)}
{render_concept_map(pages, videos, tracks)}
"""
    return page_shell(title=f"{SITE_NAME} — компʼютерні науки у правильному порядку",
                      body=body, depth=0, path="", active="tracks",
                      description=f"Навчальна мапа україномовного YouTube-каналу про програмування: "
                                  f"{len(videos)} відео у шести треках — бази даних, мережі, "
                                  f"криптографія, ШІ та інженерна майстерність.")


def render_track(track, order_no, videos, pages):
    steps = []
    for i, (vslug, note) in enumerate(track["path"], 1):
        v = videos[vslug]
        dur = fmt_ts(v["duration"]) if v["duration"] else "–"
        nch = len(v["chapters"])
        concept_chips = chip_row(v["covered"], pages, 1, small=True, limit=6)
        steps.append(f"""<li class="step">
  <div class="node mono" data-watch-node="{vslug}">{i}</div>
  <div class="step-body">
    <div class="step-top">
      <a class="step-title" href="../videos/{vslug}.html">{html.escape(v["title"])}</a>
      {level_badge(v["level"])}
      <label class="watched-box mono"><input type="checkbox" class="watched" data-slug="{vslug}"> переглянуто</label>
    </div>
    <p class="step-note">{md_inline(note, pages, 1, track["slug"])}</p>
    {concept_chips}
    <div class="meta mono">{dur} · {nch} {uk_plural(nch, "розділ", "розділи", "розділів")}</div>
  </div>
</li>""")
    intro = "".join(f"<p>{md_inline(b, pages, 1, track['slug'])}</p>" for b in track["intro"])
    slugs = ",".join(v for v, _ in track["path"])
    body = f"""<article class="track-page">
  <p class="eyebrow mono"><a href="../index.html#tracks">треки</a> / {order_no:02d}</p>
  <h1>{html.escape(track["name"])}</h1>
  <div class="meta mono">{track_meta_line(track, videos)}</div>
  <div class="progress big" data-slugs="{slugs}"><span></span></div>
  <div class="track-intro">{intro}</div>
  <h2>Порядок перегляду</h2>
  <ol class="stepper">
  {"".join(steps)}
  </ol>
</article>
"""
    return page_shell(title=f"{track['name']} — {SITE_NAME}", body=body,
                      depth=1, path=f"tracks/{track['slug']}.html",
                      description=track["tagline"], hue=track["hue"], active="tracks")


def render_video(slug, v, videos, tracks, pages):
    vid = v["youtube_id"]
    # primary track + path memberships
    memberships = []
    for i, (tslug, name, _tag, hue) in enumerate(TRACKS, 1):
        t = tracks.get(tslug)
        if not t:
            continue
        path_slugs = [s for s, _ in t["path"]]
        if slug in path_slugs:
            idx = path_slugs.index(slug)
            prev_s = path_slugs[idx - 1] if idx > 0 else None
            next_s = path_slugs[idx + 1] if idx + 1 < len(path_slugs) else None
            memberships.append((t, i, idx + 1, prev_s, next_s))
    primary = memberships[0] if memberships else None
    hue = primary[0]["hue"] if primary else None
    crumb = (f'<a href="../tracks/{primary[0]["slug"]}.html">{html.escape(primary[0]["name"])}</a>'
             f' / крок {primary[2]:02d}') if primary else '<a href="../index.html">треки</a>'

    chapters = []
    for sec, label in v["chapters"]:
        chapters.append(f"""<li>
  <button type="button" class="chapter" data-t="{sec}">
    <span class="tc mono">{fmt_ts(sec)}</span>
    <span class="ch-label">{md_inline(label, pages, 1, slug)}</span>
  </button>
  <a class="yt-jump mono" href="https://youtu.be/{vid}?t={sec}" target="_blank" rel="noopener" aria-label="Відкрити {fmt_ts(sec)} на YouTube">↗</a>
</li>""")
    chapters_html = (f'<ol class="chapters">{"".join(chapters)}</ol>' if chapters
                     else '<p class="meta">Розділів поки немає — дивіться з початку.</p>')

    takeaways = "".join(f"<li>{md_inline(t, pages, 1, slug)}</li>" for t in v["takeaways"])
    chips = chip_row(v["covered"], pages, 1)

    paths_html = []
    for t, tno, step, prev_s, next_s in memberships:
        prev_html = (f'<a class="pn prev" href="{prev_s}.html">← {html.escape(videos[prev_s]["title"])}</a>'
                     if prev_s else '<span class="pn dim">← початок треку</span>')
        next_html = (f'<a class="pn next" href="{next_s}.html">{html.escape(videos[next_s]["title"])} →</a>'
                     if next_s else '<span class="pn dim">кінець треку →</span>')
        paths_html.append(f"""<div class="path-slot" style="--h:{t["hue"]}">
  <div class="path-name mono"><a href="../tracks/{t["slug"]}.html">{html.escape(t["name"])}</a> · крок {step:02d}/{len(t["path"]):02d}</div>
  <div class="pn-row">{prev_html}{next_html}</div>
</div>""")

    dur = fmt_ts(v["duration"]) if v["duration"] else ""
    body = f"""<article class="video-page">
  <p class="eyebrow mono">{crumb}</p>
  <div class="video-head">
    <h1>{html.escape(v["title"])}</h1>
    <div class="video-meta mono">{level_badge(v["level"])} <span>{dur}</span>
      <a href="https://youtu.be/{vid}" target="_blank" rel="noopener">дивитися на YouTube ↗</a>
      <label class="watched-box mono"><input type="checkbox" class="watched" data-slug="{slug}"> переглянуто</label>
    </div>
  </div>
  <div class="player-grid">
    <div class="player-frame">
      <iframe id="player" data-embed="https://www.youtube-nocookie.com/embed/{vid}"
        src="https://www.youtube-nocookie.com/embed/{vid}?rel=0"
        title="{html.escape(v["title"])}" loading="lazy" allow="autoplay; encrypted-media; picture-in-picture"
        allowfullscreen></iframe>
    </div>
    <div class="chapter-pane">
      <div class="chapter-pane-inner">
        <h2 class="pane-title mono">Розділи</h2>
        {chapters_html}
      </div>
    </div>
  </div>
  <section class="video-about">
    <h2>Про що це відео</h2>
    <p>{md_inline(v["summary"], pages, 1, slug)}</p>
  </section>
  <section class="video-takeaways">
    <h2>Головне</h2>
    <ul>{takeaways}</ul>
  </section>
  <section class="video-covered">
    <h2>Теми відео</h2>
    {chips or '<p class="meta">Тем поки немає.</p>'}
    {tag_chips(v["fm"].get("tags", []), 1)}
  </section>
  <section class="video-paths">
    <h2>Частина цих треків</h2>
    {"".join(paths_html) or '<p class="meta">Поки не входить до жодного треку.</p>'}
  </section>
</article>
"""
    return page_shell(title=f"{v['title']} — {SITE_NAME}", body=body, depth=1,
                      path=f"videos/{slug}.html",
                      description=meta_description(v["summary"], pages),
                      og_type="video.other",
                      og_image=f"https://img.youtube.com/vi/{vid}/hqdefault.jpg",
                      hue=hue, active="tracks")


def covered_in_list(page, pages, depth, videos):
    items = []
    for vslug, note in BULLET_LINK_RE.findall(sect(page, "covered_in")):
        if vslug not in videos:
            continue
        v = videos[vslug]
        prefix = "../" * depth
        items.append(f"""<li><a href="{prefix}videos/{vslug}.html">{html.escape(v["title"])}</a>
  <span class="meta mono">{fmt_ts(v["duration"]) if v["duration"] else ""}</span>
  <p class="step-note">{md_inline(note, pages, depth, page["slug"])}</p></li>""")
    return "".join(items)


def render_topic(page, pages, videos):
    """Concept or tool page."""
    paras = "".join(f"<p>{md_inline(b, pages, 1, page['slug'])}</p>"
                    for b in prose_blocks(page["preamble"]))
    covered = covered_in_list(page, pages, 1, videos)
    related_src = sect(page, "related").strip()
    related = f"<p>{md_inline(' '.join(related_src.split()), pages, 1, page['slug'])}</p>" if related_src else ""
    if page["kind"] == "concepts":
        kind_label, index_page = "концепції", "concepts.html"
    else:
        kind_label, index_page = "інструменти", "tools.html"
    body = f"""<article class="topic-page">
  <p class="eyebrow mono"><a href="../{index_page}">{kind_label}</a> / {html.escape(page["slug"])}</p>
  <h1>{html.escape(page["title"])}</h1>
  {tag_chips(page["fm"].get("tags", []), 1)}
  <div class="topic-body">{paras}</div>
  <h2>Розібрано у відео</h2>
  <ul class="covered-list">{covered or "<li class='meta'>Поки жодне відео сюди не посилається.</li>"}</ul>
  {"<h2>Повʼязане</h2>" + related if related else ""}
</article>
"""
    return page_shell(title=f"{page['title']} — {SITE_NAME}", body=body, depth=1,
                      path=f"{page['kind']}/{page['slug']}.html",
                      description=meta_description(first_paragraph(page["preamble"]), pages),
                      active=page["kind"])


def render_library(pages, videos, *, kind, heading, lede, path, active):
    """Index page listing every concept or tool."""
    items = []
    for p in sorted((p for p in pages.values() if p["kind"] == kind),
                    key=lambda p: p["title"].lower()):
        first = first_paragraph(p["preamble"])
        first_sentence = re.split(r"(?<=[.!?]) ", first)[0] if first else ""
        n = len(BULLET_LINK_RE.findall(sect(p, "covered_in")))
        items.append(f"""<li>
  <a href="{kind}/{p["slug"]}.html">{html.escape(p["title"])}</a>
  <span class="meta mono">{n} відео</span>
  <p class="step-note">{md_inline(first_sentence, pages, 0, p["slug"])}</p>
</li>""")
    body = f"""<article class="library-page">
  <h1>{html.escape(heading)}</h1>
  <p class="lede">{lede}</p>
  <ul class="library">{"".join(items)}</ul>
</article>
"""
    return page_shell(title=f"{heading} — {SITE_NAME}", body=body, depth=0,
                      path=path, description=lede, active=active)


def render_books(pages, videos):
    entries = []
    for p in sorted((p for p in pages.values() if p["kind"] == "books"),
                    key=lambda p: p["title"].lower()):
        author = p["fm"].get("author", "")
        paras = "".join(f"<p>{md_inline(b, pages, 0, p['slug'])}</p>"
                        for b in prose_blocks(p["preamble"]))
        covered = covered_in_list(p, pages, 0, videos)
        entries.append(f"""<section class="book" id="{p["slug"]}">
  <h2>{html.escape(p["title"])}</h2>
  <div class="meta">{html.escape(author)}</div>
  {tag_chips([t for t in p["fm"].get("tags", []) if t != "book"], 0)}
  {paras}
  <ul class="covered-list">{covered}</ul>
</section>""")
    design_link = ('<a href="videos/3-books-on-software-design.html">окреме відео</a>'
                   if "3-books-on-software-design" in videos else "окреме відео")
    stars_link = ('<a href="videos/five-star-books.html">пʼятизіркових книжок</a>'
                  if "five-star-books" in videos else "пʼятизіркових книжок")
    body = f"""<article class="books-page">
  <h1>Книжкова полиця</h1>
  <p class="lede">Усі книжки, рекомендовані на каналі, з вердиктами Віктора.
  Про канон дизайну ПЗ є {design_link}, а повний список — у добірці {stars_link}.</p>
  {"".join(entries)}
</article>
"""
    return page_shell(title=f"Книжкова полиця — {SITE_NAME}", body=body, depth=0,
                      path="books.html", active="books",
                      description="Усі книжки, рекомендовані на каналі, з чесними вердиктами "
                                  "Віктора: що читати, що погортати, а до чого й не братися.")


def render_overview(pages, videos):
    _fm, body_md = parse_frontmatter((WIKI / "overview.md").read_text(encoding="utf-8"))
    preamble, sections = split_sections(body_md)
    m = re.search(r"^# +(.+?)\s*$", preamble, re.M)
    title = m.group(1) if m else "Мапа знань"
    parts = [md_blocks(preamble, pages, 0, "overview")]
    for heading, content in sections:
        if heading == "Як користуватися цією вікі":
            continue  # wiki-internal workflow section — meaningless on the website
        parts.append(f"<h2>{md_inline(heading, pages, 0, 'overview')}</h2>")
        parts.append(md_blocks(content, pages, 0, "overview"))
    body = f"""<article class="topic-page overview-page">
  <p class="eyebrow mono">огляд</p>
  <h1>{html.escape(title)}</h1>
  <div class="topic-body">{"".join(parts)}</div>
</article>
"""
    return page_shell(title=f"Огляд каналу — {SITE_NAME}", body=body, depth=0,
                      path="overview.html", active="overview",
                      description="Мапа знань каналу: одна теза, шість територій "
                                  "і фірмовий матеріал, який дає лише цей канал.")


def render_video_catalog(videos, tracks, pages):
    ordered, seen = [], set()
    for tslug, *_rest in TRACKS:
        t = tracks.get(tslug)
        if not t:
            continue
        for vslug, _note in t["path"]:
            if vslug not in seen:
                seen.add(vslug)
                ordered.append(vslug)
    ordered += [v for v in videos if v not in seen]

    cards = []
    for vslug in ordered:
        v = videos[vslug]
        t, _no, _step = primary_track(vslug, tracks)
        track_chip = (f'<a class="chip track-chip" style="--h:{t["hue"]}" '
                      f'href="tracks/{t["slug"]}.html">{html.escape(t["name"])}</a>' if t else "")
        first = re.split(r"(?<=[.!?]) ", v["summary"])[0] if v["summary"] else ""
        dur = fmt_ts(v["duration"]) if v["duration"] else ""
        cards.append(f"""<li class="cat-card" data-level="{html.escape(v["level"])}" data-track="{t["slug"] if t else ""}">
  <div class="cat-top">
    <a class="step-title" href="videos/{vslug}.html">{html.escape(v["title"])}</a>
    {level_badge(v["level"])}
    <span class="meta mono">{dur}</span>
  </div>
  <p class="step-note">{md_inline(first, pages, 0, vslug)}</p>
  <div class="cat-foot">{track_chip}{tag_chips(v["fm"].get("tags", []), 0)}</div>
</li>""")

    level_buttons = "".join(
        f'<button type="button" class="fbtn" data-value="{lv}">{LEVEL_UK[lv]}</button>'
        for lv in ("beginner", "intermediate", "advanced"))
    track_buttons = "".join(
        f'<button type="button" class="fbtn" data-value="{tslug}" style="--h:{hue}">{html.escape(name)}</button>'
        for tslug, name, _tag, hue in TRACKS if tslug in tracks)
    body = f"""<article class="catalog-page">
  <h1>Усі відео</h1>
  <p class="lede">Повний каталог каналу в порядку треків: кожне відео на своєму
  місці у навчальному шляху. Фільтруйте за рівнем чи треком.</p>
  <div class="filter-bar" id="video-filters">
    <div class="filter-group" data-filter="level">
      <button type="button" class="fbtn on" data-value="">усі рівні</button>
      {level_buttons}
    </div>
    <div class="filter-group" data-filter="track">
      <button type="button" class="fbtn on" data-value="">усі треки</button>
      {track_buttons}
    </div>
    <div class="meta mono" id="filter-count"></div>
  </div>
  <ol class="cat-list">
  {"".join(cards)}
  </ol>
</article>
"""
    return page_shell(title=f"Усі відео — {SITE_NAME}", body=body, depth=0,
                      path="videos.html", active="videos",
                      description=f"Каталог усіх {len(videos)} відео каналу з фільтрами "
                                  f"за рівнем складності й треком.")


def render_tags(pages, videos):
    kind_labels = (("videos", "відео"), ("concepts", "концепції"),
                   ("tools", "інструменти"), ("books", "книги"))
    kinds = dict(kind_labels)
    tag_map = {}
    for p in pages.values():
        if p["kind"] not in kinds:
            continue
        for t in p["fm"].get("tags", []):
            if t == "book":  # on every book page — pure noise as a tag
                continue
            tag_map.setdefault(t, []).append(p)
    by_count = sorted(tag_map, key=lambda t: (-len(tag_map[t]), t))

    cloud = "".join(
        f'<a class="chip tag" href="#tag-{html.escape(t)}">#{html.escape(t)}'
        f' <span class="tag-n">{len(tag_map[t])}</span></a>'
        for t in by_count)
    sections = []
    for t in by_count:
        groups = []
        for kind, label in kind_labels:
            ps = sorted((p for p in tag_map[t] if p["kind"] == kind),
                        key=lambda p: p["title"].lower())
            if not ps:
                continue
            chips = "".join(
                f'<a class="chip" href="{url_for(p["slug"], pages)}">{html.escape(p["title"])}</a>'
                for p in ps)
            groups.append(f'<div class="tag-group"><span class="meta mono">{label}</span>'
                          f'<div class="chip-row">{chips}</div></div>')
        sections.append(f"""<section class="tag-section" id="tag-{html.escape(t)}">
  <h2 class="mono">#{html.escape(t)} <span class="tag-n">{len(tag_map[t])}</span></h2>
  {"".join(groups)}
</section>""")
    body = f"""<article class="tags-page">
  <h1>Теги</h1>
  <p class="lede">Усі сторінки навігатора — відео, концепції, інструменти
  й книги — згруповані за тегами.</p>
  <div class="tag-cloud">{cloud}</div>
  {"".join(sections)}
</article>
"""
    return page_shell(title=f"Теги — {SITE_NAME}", body=body, depth=0,
                      path="tags.html",
                      description="Відео, концепції, інструменти й книги каналу, "
                                  "згруповані за тегами.")


def build_search_index(pages, videos, tracks):
    """Emit assets/search-index.js: window.SEARCH_INDEX for the client-side search.
    A .js assignment (not fetched JSON) so search also works from file://."""
    def norm(s):
        return re.sub(r"[ʼ'’`]", "", s.lower())

    items = []
    for slug, v in videos.items():
        items.append((v["title"], "video", f"videos/{slug}.html",
                      meta_description(v["summary"], pages, 110), v["fm"].get("tags", []), slug))
    for p in pages.values():
        if p["kind"] in ("concepts", "tools", "books"):
            kind = {"concepts": "concept", "tools": "tool", "books": "book"}[p["kind"]]
            snip = meta_description(first_paragraph(p["preamble"]), pages, 110)
            extra = [p["fm"].get("author", "")] if p["kind"] == "books" else []
            items.append((p["title"], kind, url_for(p["slug"], pages), snip,
                          p["fm"].get("tags", []) + extra, p["slug"]))
    for tslug, name, tagline, _hue in TRACKS:
        if tslug in tracks:
            items.append((name, "track", f"tracks/{tslug}.html",
                          meta_description(tagline, pages, 110), [], tslug))

    index = [{"t": title, "k": kind, "u": url, "d": snip,
              "s": norm(" ".join([title, slug.replace("-", " "), *tags, snip]))}
             for title, kind, url, snip, tags, slug in sorted(items, key=lambda i: (i[1], i[2]))]
    return ("window.SEARCH_INDEX="
            + json.dumps(index, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            + ";\n")


def write_sitemap():
    urls = []
    for f in sorted(OUT.rglob("*.html")):
        rel = f.relative_to(OUT).as_posix()
        loc = SITE_URL if rel == "index.html" else SITE_URL + rel
        urls.append(f"  <url><loc>{loc}</loc></url>")
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    return len(urls)


# ---------------------------------------------------------------- assets

STYLE = """/* jabascript навігатор — згенеровано scripts/build_website.py */
:root {
  --bg: #0d1117; --surface: #151b23; --surface-2: #1b232e;
  --text: #e5e9ee; --muted: #8b96a5; --border: #27313d;
  --h: 215; /* per-track accent hue, overridden inline */
  --acc-s: 75%; --acc-l: 62%; --acc-bg-l: 55%;
  --mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --sans: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
:root[data-theme="light"] {
  --bg: #faf7f2; --surface: #ffffff; --surface-2: #f1ede5;
  --text: #1c2128; --muted: #636e7b; --border: #e2dcd1;
  --acc-s: 65%; --acc-l: 42%; --acc-bg-l: 45%;
}
/* derived per element so an inline --h (track cards, body) re-evaluates them */
* {
  --accent: hsl(var(--h) var(--acc-s) var(--acc-l));
  --accent-dim: hsl(var(--h) 45% 45% / .38);
  --accent-bg: hsl(var(--h) 60% var(--acc-bg-l) / .12);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  * { animation: none !important; transition: none !important; }
}
body {
  margin: 0; background: var(--bg); color: var(--text);
  font: 16px/1.65 var(--sans);
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 2px; }
h1, h2, h3 { line-height: 1.15; letter-spacing: -0.02em; }
h2 { margin-top: 2.2em; font-size: 1.45rem; }
code { font-family: var(--mono); font-size: .88em; background: var(--surface-2); padding: .1em .35em; border-radius: 4px; }
.mono { font-family: var(--mono); font-size: .82rem; letter-spacing: 0; }
.meta { color: var(--muted); }
.eyebrow { color: var(--muted); text-transform: lowercase; margin: 0 0 .6rem; }
.eyebrow a { color: var(--muted); }
main { max-width: 1060px; margin: 0 auto; padding: 2.5rem 1.25rem 4rem; }

/* header / footer */
.site-head {
  display: flex; align-items: center; gap: 1.5rem;
  max-width: 1060px; margin: 0 auto; padding: 1rem 1.25rem;
  border-bottom: 1px solid var(--border);
}
.brand { color: var(--text); font-weight: 650; letter-spacing: -0.01em; }
.brand:hover { text-decoration: none; }
.brand-mark { color: var(--accent); font-size: .8em; }
.brand-dim { color: var(--muted); font-weight: 400; }
.site-head nav { display: flex; gap: 1.1rem; margin-left: auto; }
.site-head nav a { color: var(--muted); font-size: .92rem; }
.site-head nav a.active, .site-head nav a:hover { color: var(--text); text-decoration: none; }
#theme-toggle {
  background: none; border: 1px solid var(--border); color: var(--muted);
  border-radius: 50%; width: 2rem; height: 2rem; cursor: pointer; font-size: .95rem;
}
#theme-toggle:hover { color: var(--text); border-color: var(--muted); }
.site-foot {
  max-width: 1060px; margin: 0 auto; padding: 1.5rem 1.25rem 3rem;
  border-top: 1px solid var(--border); color: var(--muted); font-size: .88rem;
}

/* hero */
.hero { padding: 3rem 0 1rem; }
.hero h1 {
  font-size: clamp(2.2rem, 6vw, 3.9rem); margin: .4rem 0 1.2rem;
  font-weight: 750; letter-spacing: -0.035em;
}
.lede { max-width: 46rem; font-size: 1.08rem; color: var(--muted); }
.stats { display: flex; flex-wrap: wrap; gap: 1.6rem; margin: 1.8rem 0; color: var(--muted); }
.stats b { color: var(--text); font-weight: 600; margin-right: .3em; }
.cta {
  display: inline-block; margin-top: .4rem; padding: .7rem 1.1rem;
  border: 1px solid var(--accent-dim); border-radius: 8px;
  background: var(--accent-bg); color: var(--text); font-weight: 550;
}
.cta:hover { text-decoration: none; border-color: var(--accent); }
.cta-row { display: flex; flex-wrap: wrap; gap: .7rem; align-items: center; }
/* books accent — warm "paper" hue, distinct from every track colour */
.cta-books {
  --h: 34; --acc-s: 60%;
  border-color: hsl(34 55% 50% / .5); background: hsl(34 60% 50% / .13);
}
.cta-books:hover { border-color: hsl(34 60% 55%); }

/* books banner */
.books-banner {
  --h: 34; --acc-s: 60%;
  display: flex; align-items: center; gap: 1.3rem; flex-wrap: wrap;
  margin: 3.2rem 0 1rem; padding: 1.5rem 1.7rem;
  background: hsl(34 55% 50% / .10); border: 1px solid hsl(34 50% 50% / .32);
  border-left: 4px solid hsl(34 60% 52%); border-radius: 12px;
}
.books-banner-glyph { font-size: 2.6rem; line-height: 1; }
.books-banner-body { flex: 1; min-width: 15rem; }
.books-banner-body h2 { margin: 0 0 .3rem; font-size: 1.4rem; }
.books-banner-body p { margin: 0; color: var(--muted); max-width: 42rem; }
.books-banner .cta { margin-top: 0; white-space: nowrap; }

/* how-to */
.how-list { max-width: 46rem; padding-left: 1.2rem; color: var(--muted); }
.how-list li { margin: .45rem 0; }
.how-list b { color: var(--text); }

/* track cards */
.track-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1rem; }
.track-card {
  position: relative; display: flex; flex-direction: column; gap: .35rem;
  background: var(--surface); border: 1px solid var(--border); border-left: 3px solid var(--accent);
  border-radius: 10px; padding: 1.2rem 1.2rem 1rem; color: var(--text);
  transition: border-color .15s, transform .15s;
}
.track-card:hover { text-decoration: none; border-color: var(--accent-dim); border-left-color: var(--accent); transform: translateY(-2px); }
.track-no { font-family: var(--mono); color: var(--accent); font-size: .85rem; }
.track-card h3 { margin: 0; font-size: 1.18rem; }
.track-card p { margin: 0; color: var(--muted); font-size: .92rem; flex: 1; }
.track-card .meta { margin-top: .6rem; }

/* progress bars */
.progress { height: 3px; background: var(--surface-2); border-radius: 2px; margin-top: .55rem; overflow: hidden; }
.progress span { display: block; height: 100%; width: 0; background: var(--accent); transition: width .3s; }
.progress.big { height: 5px; max-width: 24rem; margin: 1rem 0 0; }

/* knowledge map */
.map-hint { max-width: 46rem; margin-top: -.6rem; }
.map-scroll { overflow-x: auto; margin-top: 1.2rem; border: 1px solid var(--border); border-radius: 12px; background: var(--surface); }
.map { position: relative; min-width: 980px; aspect-ratio: 1150 / 900; }
.map svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.map svg line { stroke: var(--muted); stroke-opacity: .22; stroke-width: 1; vector-effect: non-scaling-stroke; }
.map-chip {
  position: absolute; transform: translate(-50%, -50%);
  max-width: 210px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  font-size: .72rem; line-height: 1; padding: .45em .75em; border-radius: 99px;
  background: var(--bg); border: 1px solid var(--accent-dim); color: var(--accent);
}
.map-chip.hot { background: var(--accent-bg); border-color: var(--accent); font-weight: 600; }
.map-chip:hover { text-decoration: none; border-color: var(--accent); color: var(--text); z-index: 2; }

/* track page stepper */
.track-page h1 { font-size: clamp(1.9rem, 4.5vw, 2.8rem); margin: .2rem 0 .5rem; }
.track-intro { max-width: 50rem; color: var(--muted); margin-top: 1.4rem; }
.stepper { list-style: none; margin: 1.5rem 0 0; padding: 0; position: relative; }
.stepper::before {
  content: ""; position: absolute; left: 1.05rem; top: .5rem; bottom: .5rem;
  width: 2px; background: var(--border);
}
.step { position: relative; display: flex; gap: 1.15rem; padding: 0 0 1.9rem; }
.node {
  position: relative; z-index: 1; flex: none; width: 2.15rem; height: 2.15rem;
  border-radius: 50%; display: grid; place-items: center;
  background: var(--bg); border: 2px solid var(--accent-dim); color: var(--accent);
  font-size: .85rem;
}
.node.done { background: var(--accent); border-color: var(--accent); color: var(--bg); }
.step-body { flex: 1; min-width: 0; padding-top: .1rem; }
.step-top { display: flex; align-items: baseline; gap: .7rem; flex-wrap: wrap; }
.step-title { font-weight: 600; font-size: 1.06rem; color: var(--text); }
.step-title:hover { color: var(--accent); text-decoration: none; }
.step-note { margin: .45rem 0 .3rem; color: var(--muted); font-size: .93rem; max-width: 44rem; }
.watched-box { color: var(--muted); margin-left: auto; display: inline-flex; align-items: center; gap: .35rem; cursor: pointer; white-space: nowrap; }
.watched-box input { accent-color: var(--accent); cursor: pointer; }

/* badges & chips */
.badge {
  font-family: var(--mono); font-size: .68rem; text-transform: uppercase; letter-spacing: .05em;
  padding: .12em .5em; border-radius: 99px; border: 1px solid;
}
.badge-beginner { color: #4cc38a; border-color: #4cc38a55; }
.badge-intermediate { color: #d9a842; border-color: #d9a84255; }
.badge-advanced { color: #e5604f; border-color: #e5604f55; }
.chip-row { display: flex; flex-wrap: wrap; gap: .45rem; }
.chip {
  font-size: .84rem; padding: .25em .7em; border-radius: 99px;
  background: var(--surface); border: 1px solid var(--border); color: var(--text);
}
.chip:hover { border-color: var(--accent); text-decoration: none; }
.chip-row.small { margin: .3rem 0 .45rem; }
.chip-row.small .chip { font-size: .74rem; padding: .2em .6em; color: var(--muted); background: transparent; }
.chip-row.small .chip:hover { color: var(--text); }

/* video page */
.video-page h1 { font-size: clamp(1.6rem, 4vw, 2.3rem); margin: .2rem 0 .2rem; }
.video-meta { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; margin: .7rem 0 1.3rem; color: var(--muted); }
.player-grid { display: grid; grid-template-columns: minmax(0, 7fr) minmax(16rem, 3fr); gap: 1rem; align-items: stretch; }
.player-frame { position: relative; align-self: start; aspect-ratio: 16 / 9; background: #000; border-radius: 10px; overflow: hidden; border: 1px solid var(--border); }
.player-frame iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }
.chapter-pane {
  position: relative; overflow: hidden; min-height: 0;
  background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
}
.chapter-pane-inner {
  position: absolute; inset: 0; padding: .9rem; display: flex; flex-direction: column;
}
.pane-title { margin: 0 0 .5rem; font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); }
.chapters { list-style: none; margin: 0; padding: 0; overflow-y: auto; flex: 1; min-height: 0; }
.chapters li { display: flex; align-items: center; gap: .3rem; }
.chapter {
  flex: 1; display: flex; gap: .7rem; align-items: baseline; text-align: left;
  background: none; border: 0; color: var(--text); padding: .42rem .5rem; border-radius: 6px;
  cursor: pointer; font: inherit; font-size: .9rem; line-height: 1.4;
}
.chapter:hover, .chapter.active { background: var(--accent-bg); }
.chapter .tc { color: var(--accent); flex: none; }
.yt-jump { color: var(--muted); padding: .2rem .4rem; border-radius: 5px; }
.yt-jump:hover { color: var(--accent); text-decoration: none; }
.video-about p, .video-takeaways li { max-width: 50rem; }
.video-takeaways li { margin: .5rem 0; }
.path-slot { border: 1px solid var(--border); border-left: 3px solid var(--accent); border-radius: 8px; padding: .8rem 1rem; margin: .7rem 0; background: var(--surface); }
.path-name a { color: var(--text); }
.pn-row { display: flex; justify-content: space-between; gap: 1rem; margin-top: .45rem; flex-wrap: wrap; }
.pn { font-size: .92rem; }
.pn.dim { color: var(--muted); }

/* search */
.search { position: relative; }
#search-input {
  width: 11rem; padding: .35rem .8rem; border-radius: 99px;
  border: 1px solid var(--border); background: var(--surface); color: var(--text);
  font: inherit; font-size: .88rem;
}
#search-input::placeholder { color: var(--muted); }
#search-input:focus { outline: none; border-color: var(--accent); }
#search-results {
  position: absolute; top: calc(100% + .45rem); right: 0; z-index: 30;
  width: min(26rem, calc(100vw - 2.5rem)); max-height: 24rem; overflow-y: auto;
  background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
  box-shadow: 0 10px 34px rgb(0 0 0 / .35);
}
.sr-item { display: block; padding: .55rem .85rem; border-bottom: 1px solid var(--border); color: var(--text); }
.sr-item:last-child { border-bottom: 0; }
.sr-item:hover, .sr-item.sel { background: var(--accent-bg); text-decoration: none; }
.sr-kind { color: var(--accent); font-size: .68rem; text-transform: uppercase; letter-spacing: .05em; margin-right: .55em; }
.sr-title { font-weight: 550; }
.sr-snippet { display: block; color: var(--muted); font-size: .8rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.sr-empty { padding: .7rem .9rem; color: var(--muted); font-size: .88rem; }

/* videos catalog */
.catalog-page h1, .tags-page h1 { font-size: clamp(1.8rem, 4vw, 2.5rem); }
.filter-bar { display: flex; flex-direction: column; gap: .55rem; margin: 1.5rem 0 1.1rem; }
.filter-group { display: flex; flex-wrap: wrap; gap: .4rem; }
.fbtn {
  font-family: var(--mono); font-size: .78rem; cursor: pointer;
  padding: .28em .85em; border-radius: 99px;
  background: var(--surface); border: 1px solid var(--border); color: var(--muted);
}
.fbtn:hover { color: var(--text); border-color: var(--muted); }
.fbtn.on { color: var(--text); border-color: var(--accent); background: var(--accent-bg); }
.cat-list { list-style: none; padding: 0; margin: 0; }
.cat-card { padding: .95rem 0; border-bottom: 1px solid var(--border); }
.cat-top { display: flex; align-items: baseline; gap: .7rem; flex-wrap: wrap; }
.cat-card .step-note { margin: .35rem 0 .45rem; }
.cat-foot { display: flex; flex-wrap: wrap; gap: .3rem .45rem; align-items: center; }
.chip.track-chip { font-size: .74rem; color: var(--accent); border-color: var(--accent-dim); background: var(--accent-bg); }

/* tags */
.chip.tag { font-family: var(--mono); font-size: .74rem; color: var(--muted); background: transparent; }
.chip.tag:hover { color: var(--text); }
.tag-row { margin-top: .5rem; }
.tag-n { color: var(--muted); font-size: .9em; }
.tag-cloud { display: flex; flex-wrap: wrap; gap: .45rem; margin: 1.4rem 0 1.6rem; }
.tag-section { padding: .95rem 0; border-bottom: 1px solid var(--border); }
.tag-section h2 { margin: 0 0 .55rem; font-size: 1rem; }
.tag-group { display: flex; gap: .9rem; align-items: baseline; margin: .4rem 0; }
.tag-group > .meta { flex: none; width: 6.5rem; }

/* block markdown (overview) */
.table-scroll { overflow-x: auto; margin: 1.1rem 0; }
.topic-body table { border-collapse: collapse; font-size: .93rem; min-width: 34rem; }
.topic-body th, .topic-body td { border: 1px solid var(--border); padding: .5em .8em; text-align: left; vertical-align: top; }
.topic-body th { background: var(--surface); }
.topic-body blockquote { margin: 1rem 0; padding: .3rem 1.1rem; border-left: 3px solid var(--accent-dim); color: var(--muted); }
.overview-page .topic-body ul { padding-left: 1.2rem; }
.overview-page .topic-body li { margin: .4rem 0; }

/* topic / library / books */
.topic-page h1, .library-page h1, .books-page h1 { font-size: clamp(1.8rem, 4vw, 2.5rem); }
.topic-body { max-width: 50rem; }
.covered-list { list-style: none; padding: 0; max-width: 50rem; }
.covered-list li { padding: .7rem 0; border-bottom: 1px solid var(--border); }
.covered-list .step-note { margin: .25rem 0 0; }
.library { list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: .4rem 1.6rem; }
.library li { padding: .55rem 0; border-bottom: 1px solid var(--border); }
.library .step-note { margin: .15rem 0 0; font-size: .86rem; }
.book { max-width: 50rem; padding: 1.1rem 0; border-bottom: 1px solid var(--border); }
.book h2 { margin: 0; font-size: 1.25rem; }

@media (max-width: 860px) {
  .player-grid { grid-template-columns: 1fr; }
  .chapter-pane { overflow: visible; }
  .chapter-pane-inner { position: static; }
  .chapters { max-height: 300px; }
  .site-head { flex-wrap: wrap; gap: .6rem 1rem; }
  .site-head nav { margin-left: 0; }
  .watched-box { margin-left: 0; }
  .search { flex: 1 1 12rem; }
  #search-input { width: 100%; }
  .tag-group { flex-direction: column; gap: .25rem; }
  .tag-group > .meta { width: auto; }
}
"""

APP_JS = """// jabascript навігатор — згенеровано scripts/build_website.py
(function () {
  var doc = document.documentElement;

  // theme toggle (initial theme set inline in <head>)
  var toggle = document.getElementById("theme-toggle");
  if (toggle) toggle.addEventListener("click", function () {
    var next = doc.dataset.theme === "dark" ? "light" : "dark";
    doc.dataset.theme = next;
    localStorage.setItem("jsnav-theme", next);
  });

  // chapter click → seek by swapping iframe src (no external JS API)
  var player = document.getElementById("player");
  if (player) {
    var base = player.dataset.embed;
    document.querySelectorAll(".chapter").forEach(function (btn) {
      btn.addEventListener("click", function () {
        player.src = base + "?start=" + btn.dataset.t + "&autoplay=1&rel=0";
        document.querySelectorAll(".chapter.active").forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
      });
    });
  }

  // watched state (localStorage only)
  var KEY = "jsnav-watched";
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function save(w) { localStorage.setItem(KEY, JSON.stringify(w)); }
  var watched = load();

  function refresh() {
    document.querySelectorAll("input.watched").forEach(function (box) {
      box.checked = !!watched[box.dataset.slug];
    });
    document.querySelectorAll("[data-watch-node]").forEach(function (node) {
      node.classList.toggle("done", !!watched[node.dataset.watchNode]);
    });
    document.querySelectorAll(".progress[data-slugs]").forEach(function (bar) {
      var slugs = bar.dataset.slugs ? bar.dataset.slugs.split(",") : [];
      var done = slugs.filter(function (s) { return watched[s]; }).length;
      bar.firstElementChild.style.width = slugs.length ? (100 * done / slugs.length) + "%" : "0";
    });
  }
  document.querySelectorAll("input.watched").forEach(function (box) {
    box.addEventListener("change", function () {
      if (box.checked) watched[box.dataset.slug] = 1; else delete watched[box.dataset.slug];
      save(watched);
      refresh();
    });
  });
  refresh();

  // video catalog filters (videos.html)
  var filters = document.getElementById("video-filters");
  if (filters) {
    var fstate = { level: "", track: "" };
    var cards = document.querySelectorAll(".cat-card");
    var counter = document.getElementById("filter-count");
    var applyFilters = function () {
      var n = 0;
      cards.forEach(function (card) {
        var show = (!fstate.level || card.dataset.level === fstate.level) &&
                   (!fstate.track || card.dataset.track === fstate.track);
        card.hidden = !show;
        if (show) n++;
      });
      if (counter) counter.textContent = n + " відео";
    };
    filters.querySelectorAll(".filter-group").forEach(function (group) {
      group.addEventListener("click", function (e) {
        var btn = e.target.closest(".fbtn");
        if (!btn) return;
        fstate[group.dataset.filter] = btn.dataset.value;
        group.querySelectorAll(".fbtn").forEach(function (b) { b.classList.toggle("on", b === btn); });
        applyFilters();
      });
    });
    applyFilters();
  }

  // site search (index shipped as assets/search-index.js)
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  if (input && results && window.SEARCH_INDEX) {
    var KINDS = { video: "відео", concept: "тема", tool: "інструмент", book: "книга", track: "трек" };
    var root = document.body.dataset.root || "";
    var sel = -1;
    var normQ = function (s) { return s.toLowerCase().replace(/[ʼ'’`]/g, ""); };
    var escQ = function (s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;"); };
    var hide = function () { results.hidden = true; sel = -1; };
    var show = function () {
      var q = normQ(input.value.trim());
      if (q.length < 2) { hide(); return; }
      var found = [];
      window.SEARCH_INDEX.forEach(function (it) {
        var t = normQ(it.t);
        var rank = t.indexOf(q) === 0 ? 0 : t.indexOf(q) > -1 ? 1 : it.s.indexOf(q) > -1 ? 2 : -1;
        if (rank >= 0) found.push([rank, it]);
      });
      found.sort(function (a, b) { return a[0] - b[0]; });
      var top = found.slice(0, 8);
      results.innerHTML = top.length ? top.map(function (r) {
        var it = r[1];
        return '<a class="sr-item" href="' + root + it.u + '">' +
               '<span class="sr-kind mono">' + (KINDS[it.k] || it.k) + '</span>' +
               '<span class="sr-title">' + escQ(it.t) + '</span>' +
               '<span class="sr-snippet">' + escQ(it.d) + '</span></a>';
      }).join("") : '<div class="sr-empty">Нічого не знайдено</div>';
      results.hidden = false;
      sel = -1;
    };
    input.addEventListener("input", show);
    input.addEventListener("focus", function () { if (input.value.trim().length >= 2) show(); });
    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { hide(); input.blur(); return; }
      var items = results.querySelectorAll(".sr-item");
      if (results.hidden || !items.length) return;
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        sel = e.key === "ArrowDown" ? Math.min(sel + 1, items.length - 1) : Math.max(sel - 1, 0);
        items.forEach(function (el, i) { el.classList.toggle("sel", i === sel); });
        items[sel].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter" && sel >= 0) {
        e.preventDefault();
        location.href = items[sel].href;
      }
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".search")) hide();
    });
  }
})();
"""


# ---------------------------------------------------------------- main

def main():
    pages = load_pages()
    durations = load_durations()
    videos, tracks = build_model(pages, durations)

    # website/ is fully generated — start clean so excluded pages disappear
    if OUT.exists():
        shutil.rmtree(OUT)
    for d in ("tracks", "videos", "concepts", "tools", "assets"):
        (OUT / d).mkdir(parents=True, exist_ok=True)

    (OUT / "index.html").write_text(render_index(videos, tracks, pages), encoding="utf-8")
    for i, (tslug, *_rest) in enumerate(TRACKS, 1):
        if tslug in tracks:
            (OUT / "tracks" / f"{tslug}.html").write_text(
                render_track(tracks[tslug], i, videos, pages), encoding="utf-8")
    for slug, v in videos.items():
        (OUT / "videos" / f"{slug}.html").write_text(
            render_video(slug, v, videos, tracks, pages), encoding="utf-8")
    for p in pages.values():
        if p["kind"] in ("concepts", "tools"):
            (OUT / p["kind"] / f"{p['slug']}.html").write_text(
                render_topic(p, pages, videos), encoding="utf-8")
    (OUT / "concepts.html").write_text(render_library(
        pages, videos, kind="concepts", heading="Бібліотека тем",
        lede="Усе, що канал пояснював, у вигляді зворотного індексу: "
             "оберіть тему — і побачите, які саме відео (і хвилини) її розкривають.",
        path="concepts.html", active="concepts"), encoding="utf-8")
    (OUT / "tools.html").write_text(render_library(
        pages, videos, kind="tools", heading="Інструменти й технології",
        lede="Технології та продукти, які канал розбирає на практиці — "
             "від PostgreSQL до Claude Code.",
        path="tools.html", active="tools"), encoding="utf-8")
    (OUT / "books.html").write_text(render_books(pages, videos), encoding="utf-8")
    (OUT / "videos.html").write_text(render_video_catalog(videos, tracks, pages), encoding="utf-8")
    (OUT / "tags.html").write_text(render_tags(pages, videos), encoding="utf-8")
    (OUT / "overview.html").write_text(render_overview(pages, videos), encoding="utf-8")
    (OUT / "assets" / "style.css").write_text(STYLE, encoding="utf-8")
    (OUT / "assets" / "app.js").write_text(APP_JS, encoding="utf-8")
    (OUT / "assets" / "search-index.js").write_text(
        build_search_index(pages, videos, tracks), encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    n_sitemap = write_sitemap()

    n_pages = sum(1 for _ in OUT.rglob("*.html"))
    print(f"built {n_pages} pages ({n_sitemap} in sitemap) -> {OUT}")
    if WARNINGS:
        print(f"\n{len(WARNINGS)} warnings:")
        for w in sorted(set(WARNINGS)):
            print(f"  - {w}")
        return 1
    print("no warnings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
