---
type: video
title_uk: "Як працює повнотекстовий пошук？ Розбираємо на практиці інвертовані індекси"
youtube_id: nu5Le4YDhPA
tags: [databases, full-text-search, inverted-index, javascript, map-reduce]
date_ingested: 2026-07-09
---
# How Full-Text Search Works: Building an Inverted Index in Practice

> Original: "Як працює повнотекстовий пошук？ Розбираємо на практиці інвертовані індекси" — https://youtu.be/nu5Le4YDhPA

The author builds a production-grade [[inverted-index]] from scratch in JavaScript and races it against [[mysql|MySQL]] on his 16.5M-row products table — informed by a real project where his team indexed **300 TB** of data with a hand-written inverted index (existing tools didn't fit: per-day immutable indexes, geo data, a custom query language). Setup: a B-tree index makes `LIKE 'exploiter%'` instant but `LIKE '%telegraphers%'` unusable, because you can't sort a column by a word *inside* the value ([[full-text-search]]). The fix: map each word → list of (document id, position) pairs; positions enable exact-phrase and proximity queries. Conceptually "that's all there is" — the rest is engineering. Since a naive in-memory map of 16.5M descriptions would need 10–15 GB of RAM, he builds the index with [[map-reduce]] (Google's 2004 paper, Hadoop, Hadoop streaming — using his own `hadoop-streaming-utils` npm module): a Node.js `map` script emits word/(doc,position) pairs, Unix `sort` does the shuffle, a `reduce` script groups per token. The tokenize step gets real treatment: splitting into tokens, dropping stop-words and tokens ≤2 chars, stemming ("conferences"→"conferenc") vs lemmatization (better — his Ukrainian counterexample: stemming "німці" gives "німц", so a search for "німець" misses; his 300 TB project used a lemmatizer), and lowercasing. Then [[index-compression]], stage by stage with file sizes on screen: raw index 4 GB → flatten arrays-of-pairs 3.4 GB → delta-encode sorted doc ids (store 100,3,5 instead of 100,103,108) 2.3 GB → varbyte (variable-byte) compression via the `fastintcompress` idea, with binary output wrapped in [[base64]] to stay newline-safe in a text file → **1.3 GB**, smaller than MySQL's own FULLTEXT index (1.7 GB, which also took 14 minutes to build). The showdown: MySQL `LIKE '%three words%'` = 40 seconds; his JS searcher over the file = **21 ms**, same document ids. Verdict: don't hand-roll it in normal life — use built-in FULLTEXT in MySQL/Postgres or Elasticsearch — but now you know what they're doing.

## Key takeaways
- B-tree indexes cannot serve `LIKE '%word%'` — sorting by a column can't sort by a word inside it; the answer is an [[inverted-index]]: word → [(doc id, position), ...], where positions unlock exact-phrase and "within N words" queries ([[full-text-search]], [[database-indexes]]).
- Conceptually the inverted index is the whole trick ("на цьому можна відео закінчити") — everything else is tokenization, compression, and query machinery.
- Tokenization is a pipeline: split to tokens, filter stop-words (articles/prepositions bloat the index without helping search) and short tokens, stem or better lemmatize, lowercase; the same pipeline must run on every search query. Stemming fails on words like "німці/німець"; his 300 TB production system used a lemmatizer.
- He builds the index via [[map-reduce]] because 16.5M docs won't fit RAM: Node.js map emits pairs, `sort` = shuffle, reduce groups per token — the code would run on actual Hadoop streaming, and he wrote the `hadoop-streaming-utils` npm module it uses.
- [[index-compression]] measured live: 4 GB raw → 3.4 GB flat arrays → 2.3 GB after delta-encoding sorted doc ids → 1.3 GB after varbyte encoding (+[[base64]] wrapping, which costs +33% and still wins) — beating MySQL's FULLTEXT index size (1.7 GB).
- Varbyte compression explained on the whiteboard: use 7 bits per byte for the number and 1 continuation bit — small numbers (which delta encoding produces) fit in 1–2 bytes instead of a fixed 4/8.
- Result: 40 s in MySQL with `LIKE` vs 21 ms with his JS searcher on the same 16.5M rows; MySQL's own FULLTEXT index also answers instantly once built (14 min build).
- War story: the 300 TB system stored its inverted index in [[mongodb|MongoDB]], had per-day immutable indexes ("yesterday's index never updates"), geo attributes, and a custom query language parsed with PEG grammars; he gave a KyivJS talk about it. [[elasticsearch|Elasticsearch]] and MySQL/Postgres FULLTEXT are the same mechanism packaged — Sphinx lost popularity partly because it originally could only rebuild its index from scratch via cron.

## Covered
[[full-text-search]], [[inverted-index]], [[index-compression]], [[map-reduce]], [[base64]], [[database-indexes]], [[mysql]], [[postgresql]], [[elasticsearch]], [[mongodb]]
