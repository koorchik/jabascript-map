# Log

Append-only record of wiki operations. Entry format: `## [YYYY-MM-DD] ingest|query|lint | Title`.

## [2026-07-09] ingest | Initial batch: all 40 channel videos

Bootstrapped the wiki from the full back-catalog of jabascript video subtitles
(`raw/*.uk.vtt`, Ukrainian tracks, cleaned into `transcripts/`). Created:

- 40 video pages
- 54 concept pages (hubs)
- 36 tool pages
- 37 book pages
- 6 cluster MOCs, plus `overview.md` and `index.md`

Notable naming decisions: the isolation concept is `sandboxing-and-isolation`
(the video slug `vm-network-isolation` was already taken); GoF book is
`design-patterns-gof` (concept owns `design-patterns`); DDD lives as a book
page only; Node.js slug is `nodejs`.

## [2026-07-09] lint | Post-ingest link check

Ran `scripts/lint_wiki.py` after the batch ingest; fixed broken links and
orphans found. See git history for details.
