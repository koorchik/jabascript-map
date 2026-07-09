---
type: video
title_uk: "Як працює повнотекстовий пошук？ Частина 2. Питання та відповіді"
youtube_id: LaXU5tlY3ZM
tags: [databases, full-text-search, inverted-index, q-and-a]
date_ingested: 2026-07-09
---
# How Full-Text Search Works, Part 2: Q&A and Further Optimizations

> Original: "Як працює повнотекстовий пошук？ Частина 2. Питання та відповіді" — https://youtu.be/LaXU5tlY3ZM

The first video in a new format the author invented for his patrons: collect questions under an existing video and answer them in depth — here, follow-ups to his hand-built [[inverted-index]] ([[full-text-search-inverted-indexes]]). The headline improvement came from a viewer's suggestion and kills the [[base64]] overhead from part 1: instead of one text file with base64-wrapped binary postings, split the index into **two files** — a tiny `tokens` file (sorted tokens + byte offset/length of each postings block) and a raw binary `entries` file. Result: 1.3 GB shrinks to 938 MB + a 2 MB token file; search latency drops from 15 ms to ~5 ms, because the 2 MB token file (typically 200–300K tokens even at scale, ~6 MB) is simply read into memory and binary-searched there, then exactly one ranged read fetches the needed postings. His favorite consequence: the big entries file can sit on S3/cloud storage and be queried via HTTP Range requests — a working full-text search over huge data "without any server holding things in memory". Q1: how to search by a *fragment* of a word (e.g. "cks" inside "socks")? Answer: you can't search differently, you must *index* differently — the tokenizer decides what's searchable: n-gram tokenizers (he draws trigrams sliding over "family"), edge n-grams, letter/whitespace/keyword/pattern tokenizers, URL-splitting, even hashtag- or IP-extracting custom tokenizers — walking through the [[elasticsearch|Elasticsearch]] tokenizer reference — at the cost of a 2–3× bigger index. Q2: how do you compress the index when doc ids are UUIDs? Answer: you basically can't — every serious posting-list compression scheme (he shows a survey paper of them) assumes sorted *integers*; so map UUIDs to ints (extra int column or a separate UUID↔int mapping), which is exactly what [[mysql|MySQL]]/InnoDB does internally with its hidden auto-increment `FTS_DOC_ID` column ([[index-compression]], [[uuid-vs-auto-increment]]).

## Key takeaways
- Splitting the index into a small tokens file (token + byte offset/length) and a raw binary entries file eliminates base64's +33% overhead: 1.3 GB → 938 MB + 2 MB, and search went from 15 ms to ~5 ms ([[inverted-index]], [[base64]]).
- The token dictionary is tiny (88K tokens ≈ 2 MB; rarely above 200–300K ≈ 6 MB), so it can live fully in memory and be binary-searched in ~0.2 ms — no more risky binary search over a huge file where you can land mid-line.
- Serverless search idea he highlights: park the entries file on S3/CDN and fetch postings via HTTP Range requests — full-text search over massive data with no stateful search server.
- "If you want to search differently, you must index differently": substring-in-word search needs an n-gram (or other custom) tokenizer, not a cleverer query — demonstrated with trigrams over "family" and the Elasticsearch tokenizer reference (n-gram, edge n-gram, letter, keyword, pattern, URL, custom hashtag/IP extractors) ([[full-text-search]]).
- N-gram indexing multiplies index size 2–3×: same documents, but each doc id now appears against every n-gram instead of one word — "there's nothing much to be done about it".
- Posting-list [[index-compression]] algorithms (delta, varbyte, the many variants in the survey paper he shows) all presuppose sorted integers; there's no best one — different data favors different schemes, and varbyte works decently everywhere.
- UUID doc ids defeat these compressors; the standard fix is a UUID→integer mapping — MySQL's FULLTEXT does precisely this via a hidden 8-byte auto-increment `FTS_DOC_ID` column (you can declare it yourself to avoid the hidden column) ([[uuid-vs-auto-increment]], [[mysql]]).
- On slower hardware the gap is brutal: plain `LIKE` search on the same data on an HDD simply timed out after minutes, while the split-file inverted index worked fine.

## Covered
[[full-text-search]], [[inverted-index]], [[index-compression]], [[base64]], [[uuid-vs-auto-increment]], [[elasticsearch]], [[mysql]]
