---
type: concept
tags: [databases, search, elasticsearch, indexes]
---
# Full-text search

The channel treats full-text search not as "just use Elastic" but as a mechanism you can build with your own hands — Viktor did exactly that in production, hand-rolling a 300 TB full-text index. The motivating failure: a B-tree index makes `LIKE 'prefix%'` instant, but `LIKE '%word%'` takes ~40 s (or ~7 s in the earlier demo) because no sort order helps you find a word in the middle of a value ([[why-database-indexes]], [[full-text-search-inverted-indexes]]). The answer is the [[inverted-index]], and the surrounding pipeline he builds live: tokenization (split, stop-word and short-token filtering, lowercasing) and stemming vs lemmatization — with his Ukrainian counterexample that stemming 'німці' → 'німц' misses 'німець', which is why his 300 TB project used a lemmatizer ([[full-text-search-inverted-indexes]]). Crucially, the same pipeline must be applied to queries.

His key maxim from the Q&A follow-up: "if you want to search differently, you must index differently." Substring-inside-word search is not a cleverer query — it's an n-gram tokenizer (he draws trigrams over 'family'), at the cost of inflating the index 2–3x. Elasticsearch's tokenizer catalog (edge n-gram, letter, keyword, pattern, custom hashtag/IP extractors) is really a menu of indexing strategies ([[full-text-search-part-2-qa]]). His pragmatic verdict: in real life use built-in FULLTEXT or [[elasticsearch]] — but now you know what they actually do, and his hand-built index beat MySQL `LIKE` 40 s → 21 ms on 16.5M rows and came out smaller than MySQL's own FULLTEXT index.

## Covered in
- [[why-database-indexes]] — the setup: prefix search instant, substring search ~7 s; "everyone says use Elastic"; teases his 300 TB war story
- [[full-text-search-inverted-indexes]] — the main build: full tokenization/stemming pipeline, 40 s → 21 ms on 16.5M rows, the use-Elastic-in-real-life verdict
- [[full-text-search-part-2-qa]] — "search differently ⇒ index differently": n-gram tokenizers, Elasticsearch's tokenizer zoo, index inflation costs
- [[qa-1-will-https-protect-you]] — Q&A context revisiting the inverted-index internals and compression example

## Related
[[inverted-index]] — the core data structure underneath
[[index-compression]] — how the posting lists get small
[[database-indexes]] — the B-tree failure mode that makes this necessary
[[map-reduce]] — how the index gets built without unbounded RAM
