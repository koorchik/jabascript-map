# jabascript Knowledge Navigator — Wiki Schema

This repo is an LLM-maintained knowledge wiki built from the subtitles of the
**jabascript** YouTube channel (Ukrainian-language videos about programming,
databases, networking, security, AI/vibe-coding, and engineering craft).
The LLM writes and maintains everything under `wiki/`; the human curates
sources and asks questions. The user browses the wiki in Obsidian.

## Layers

| Layer | Path | Rules |
|---|---|---|
| Raw sources | `raw/` | Immutable `.vtt` subtitle files. NEVER modify. `uk` = original speech (authoritative), `en` = auto-translation (ignore unless uk missing). |
| Transcripts | `transcripts/` | Derived clean text, one `.txt` per video. Regenerate with `python3 scripts/clean_vtt.py raw/*.uk.vtt`. Read these, not the VTTs. |
| Timed transcripts | `transcripts/timed/` | Derived text with `[m:ss]` markers every ~20s, one `<youtube_id>.uk.txt` per video; header line 3 carries `# duration:`. Regenerate with `python3 scripts/vtt_to_timed.py raw/*.uk.vtt`. The ONLY legitimate source for chapter timestamps. |
| Wiki | `wiki/` | LLM-owned markdown. All knowledge lives here. |
| Website | `website/` | Fully generated static learning-navigator site (Ukrainian). NEVER edit by hand — regenerate with `python3 scripts/build_website.py` after wiki changes. Track order/names/taglines and the excluded stale streams live in the script's `TRACKS`/`EXCLUDED` constants. |

**The website must never lag the wiki.** Every ingest of new video data (and
any other change under `wiki/`) ends with `python3 scripts/build_website.py`
in the same session, fixing any warnings it prints. A wiki change without a
site rebuild is an incomplete task.

## Wiki structure

- `wiki/index.md` — catalog of every page by category, one line each. Update on every ingest.
- `wiki/log.md` — append-only. Entry format: `## [YYYY-MM-DD] ingest|query|lint | Title`.
- `wiki/overview.md` — top-level synthesis: the channel's knowledge map.
- `wiki/concepts/` — **the hubs.** One page per concept (e.g. `dns.md`, `database-indexes.md`, `vibe-coding.md`).
- `wiki/videos/` — one page per video.
- `wiki/tools/` — technologies/products discussed (`postgresql.md`, `claude-code.md`…).
- `wiki/books/` — books recommended on the channel.
- `wiki/clusters/` — MOC pages grouping the domain: networking-and-internet,
  databases-and-data-structures, security-and-cryptography, ai-and-vibe-coding,
  engineering-craft-and-career, channel-meta.

## Page conventions

- **Language:** Ukrainian prose — natural, живою мовою (the channel's own language).
  Established dev terms that Ukrainian developers don't translate stay in Latin
  (commit, pull request, B-tree…). Book titles stay in English.
- **File names:** kebab-case English slugs, never translated (Obsidian resolves links
  by filename). Links: `[[slug]]` or `[[slug|український текст]]`; inline links in
  prose should carry Ukrainian display text. Links never include the folder path.
- **Frontmatter (YAML):** every page has `type` (video|concept|tool|book|cluster)
  and `tags` (English identifiers, untranslated). Video pages also: `youtube_id`,
  `title_uk`, `level` (beginner|intermediate|advanced), `date_ingested`.
- **Voice:** concept pages describe ideas *as presented on the channel* —
  the author's examples, analogies, and opinions — not generic textbook
  content. Attribute claims to the video: `([[video-slug]])`.
- Every video page links to ≥1 concept; every concept links back to its
  videos and sideways to related concepts. Avoid orphan pages.

### Video page template

```markdown
---
type: video
title_uk: "<original title>"
youtube_id: <id>
level: beginner|intermediate|advanced
tags: [...]
date_ingested: YYYY-MM-DD
---
# <Українська назва (з title_uk, без хештегів)>

> Оригінал: "<title_uk>" — https://youtu.be/<id>

**Абзац-підсумок.**

## Головне
- ...

## Розділи
- 00:00 — Вступ: про що це відео
- 02:15 — <тема розділу>

## Теми
[[concept-a]], [[concept-b]], [[tool-x]]
```

Chapter rules: format `- MM:SS — тема` (or `H:MM:SS`); first chapter always
`00:00`; times strictly increasing and below the video duration; **every time
must be copied from a `[m:ss]` marker in `transcripts/timed/<youtube_id>.uk.txt`**
where that topic starts — never invented. Granularity: 5–8 chapters (<15 min),
8–15 (15–60 min), up to ~25 for multi-hour streams.

### Concept page template

```markdown
---
type: concept
tags: [...]
---
# <Назва концепції>

Що це таке і як це подано на каналі (1–3 абзаци, з прикладами й аналогіями
автора).

## Де розглядається
- [[video-slug]] — що додає це відео

## Повʼязане
[[other-concept]] — як повʼязані
```

### Cluster page learning paths

Every cluster page has a `## Відео (порядок перегляду)` section: a numbered
list `N. [[video-slug]] — чому саме тут`, the curated watch order the website
turns into a track.

## Workflows

### Ingest (new video)

1. Drop `.vtt` into `raw/`, run `python3 scripts/clean_vtt.py raw/<file>.uk.vtt`
   and `python3 scripts/vtt_to_timed.py raw/<file>.uk.vtt`.
2. Read the transcript; write/update the video page in `wiki/videos/`
   (Ukrainian, with `level` and a `## Розділи` chapter list timed from the
   timed transcript).
3. Create or update every concept/tool/book page the video touches.
   Prefer updating an existing page over creating a near-duplicate —
   check `wiki/index.md` for existing slugs first.
4. Update the relevant cluster page(s) — including the video's place in
   `## Відео (порядок перегляду)` — and `wiki/overview.md` if the new
   material shifts the big picture.
5. Regenerate the index (`python3 scripts/build_index.py`); append to `wiki/log.md`.
6. Rebuild the site: `python3 scripts/build_website.py` (fix any warnings it prints).

### Query

1. Read `wiki/index.md` to locate relevant pages; drill into them.
2. Answer with `[[links]]` and video citations.
3. If the answer is a synthesis worth keeping (comparison, connection,
   analysis), file it as a new wiki page and index it — explorations compound.

### Lint (periodic health check)

Run `python3 scripts/lint_wiki.py` (broken `[[links]]`, orphan pages, missing
frontmatter). Then check by reading: concepts mentioned in ≥2 video pages but
lacking their own page, contradictions between pages, stale claims superseded
by newer videos. Report, fix, log.

## Naming discipline

Before creating a page, grep `wiki/` for likely existing names. One concept =
one page: e.g. all index talk goes in `database-indexes.md`, not per-database
pages. Split a page only when it clearly covers two ideas.
