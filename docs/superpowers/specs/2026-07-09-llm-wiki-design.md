# LLM Wiki: jabascript Knowledge Navigator — Design

Date: 2026-07-09
Status: approved (user: "Approve — go build it")

## Goal

A persistent, LLM-maintained Obsidian wiki built from the subtitles of the
user's Ukrainian YouTube channel (jabascript, ~40 videos). Purpose: navigate
concepts, ideas, tools covered on the channel and see how they connect.

## Decisions (user-confirmed)

- **Language:** wiki pages in English; original Ukrainian video titles preserved.
- **Ingest:** batch all 40 videos in one pass, user reviews afterwards.
- **Structure:** concepts are the hub pages; videos, tools, books link into them.

## Architecture

Three layers per the LLM-wiki pattern:

1. `raw/` — immutable YouTube `.vtt` subtitle files (uk = original speech,
   en = auto-translation; the uk track is authoritative).
2. `transcripts/` — derived clean plain-text, one `.txt` per video, produced
   by `scripts/clean_vtt.py` (dedupes rolling captions, strips cue timing).
   Regenerable; sessions read these, never the raw VTT.
3. `wiki/` — the LLM-owned knowledge base:
   - `concepts/` — hub pages (DNS, database indexes, hashing, vibe-coding…)
   - `videos/` — one page per video: summary, key takeaways, outbound links
   - `tools/` — technologies and products discussed
   - `books/` — books recommended on the channel
   - `clusters/` — ~6 MOC pages (Networking, Databases & Data Structures,
     Security & Crypto, AI & Vibe-coding, Craft & Career, Channel Meta)
   - `overview.md`, `index.md`, `log.md`

`CLAUDE.md` at the repo root is the schema: page conventions, naming rules,
and the ingest / query / lint workflows.

## Conventions

- Obsidian `[[wikilinks]]`; kebab-case English file names.
- YAML frontmatter: `type` (video|concept|tool|book|cluster), `tags`,
  plus `youtube_id` and `title_uk` on video pages.
- Concept pages describe the idea *as presented on the channel* — the
  author's examples and opinions — and link to covering videos and
  related concepts.
- `log.md` entries: `## [YYYY-MM-DD] ingest|query|lint | Title`.

## Non-goals (YAGNI)

- No search engine (qmd) at 40 sources — index.md suffices; revisit if the
  vault grows past a few hundred pages.
- No Dataview/Marp setup now.
- No modification of raw sources, ever.
