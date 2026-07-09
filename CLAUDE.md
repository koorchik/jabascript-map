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
| Wiki | `wiki/` | LLM-owned markdown. All knowledge lives here. |

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

- **Language:** English prose. Keep original Ukrainian video titles, and
  Ukrainian terms in parentheses where the author's phrasing matters.
- **File names:** kebab-case English slugs. Links: Obsidian `[[slug]]` or `[[slug|display text]]`.
  Links never include the folder path — Obsidian resolves by filename.
- **Frontmatter (YAML):** every page has `type` (video|concept|tool|book|cluster)
  and `tags`. Video pages also: `youtube_id`, `title_uk`, `date_ingested`.
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
tags: [...]
date_ingested: YYYY-MM-DD
---
# <English title>

> Original: "<title_uk>" — https://youtu.be/<id>

**One-paragraph summary.**

## Key takeaways
- ...

## Covered
[[concept-a]], [[concept-b]], [[tool-x]]
```

### Concept page template

```markdown
---
type: concept
tags: [...]
---
# <Concept name>

What it is and the channel's take on it (1-3 paragraphs, with the author's
examples/analogies).

## Covered in
- [[video-slug]] — what that video adds

## Related
[[other-concept]] — how they relate
```

## Workflows

### Ingest (new video)

1. Drop `.vtt` into `raw/`, run `python3 scripts/clean_vtt.py raw/<file>.uk.vtt`.
2. Read the transcript; write/update the video page in `wiki/videos/`.
3. Create or update every concept/tool/book page the video touches.
   Prefer updating an existing page over creating a near-duplicate —
   check `wiki/index.md` for existing slugs first.
4. Update the relevant cluster page(s) and `wiki/overview.md` if the new
   material shifts the big picture.
5. Update `wiki/index.md`; append to `wiki/log.md`.

### Query

1. Read `wiki/index.md` to locate relevant pages; drill into them.
2. Answer with `[[links]]` and video citations.
3. If the answer is a synthesis worth keeping (comparison, connection,
   analysis), file it as a new wiki page and index it — explorations compound.

### Lint (periodic health check)

Look for: orphan pages (no inbound links), broken `[[links]]`, concepts
mentioned in ≥2 video pages but lacking their own page, contradictions
between pages, stale claims superseded by newer videos. Report, fix, log.

## Naming discipline

Before creating a page, grep `wiki/` for likely existing names. One concept =
one page: e.g. all index talk goes in `database-indexes.md`, not per-database
pages. Split a page only when it clearly covers two ideas.
