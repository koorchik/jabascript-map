---
type: tool
tags: [databases, search, full-text-search]
---
# Elasticsearch

Presented not as magic but as the packaged version of exactly the mechanism Viktor builds by hand: an [[inverted-index]] plus a tokenization pipeline — "it works the same way." He contrasts it with Sphinx, a fallen predecessor that originally could only rebuild its index from scratch on cron ([[full-text-search-inverted-indexes]]). His standing advice: use Elasticsearch (or built-in FULLTEXT) in real projects, but understand what it's doing underneath.

In the Q&A follow-up he uses Elasticsearch's official tokenizer reference as a catalog of indexing strategies — n-gram, edge n-gram, letter, whitespace, keyword, pattern, URL, custom hashtag/IP extractors — to answer the substring-search question, embodying his maxim that "if you want to search differently, you must index differently" (with the warning that n-grams inflate the index 2–3x) ([[full-text-search-part-2-qa]]).

## Covered in
- [[full-text-search-inverted-indexes]] — named as the productized inverted index; Sphinx as the cautionary predecessor
- [[full-text-search-part-2-qa]] — the tokenizer zoo as a menu of indexing strategies

## Related
[[full-text-search]], [[inverted-index]], [[index-compression]], [[mysql]]
