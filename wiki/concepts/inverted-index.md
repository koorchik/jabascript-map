---
type: concept
tags: [databases, search, data-structures, indexes]
---
# Inverted index

The data structure that solves what B-tree indexes cannot: mid-string word search. The structure is word → list of (document id, position) pairs; the positions unlock exact-phrase and proximity queries. Viktor's summary: "conceptually that's all there is — the rest is engineering" ([[full-text-search-inverted-indexes]]). And the engineering is where his war story lives: he hand-wrote an inverted index over 300 TB of data in production — per-day immutable indexes, geo attributes, a custom query language parsed with a PEG grammar, stored in [[mongodb]] and queried per-day in parallel — and gave a KyivJS talk about it.

The follow-up Q&A carries a viewer-suggested optimization he loved: split the index into a tiny tokens file (token + byte offset/length, ~2 MB for 88K tokens — real dictionaries rarely exceed 200–300K tokens, so it fits fully in memory for binary search) plus a raw binary postings file, killing the base64 overhead: 1.3 GB → 938 MB, search latency 15 ms → 5 ms. His favorite consequence: the postings file can live on S3 or a CDN and be queried via HTTP Range requests — serverless full-text search ([[full-text-search-part-2-qa]]). The Q&A episode adds the framing that the inverted index IS the efficient structure — optimizations change serialization (delta compression, VByte) rather than replacing it ([[qa-1-will-https-protect-you]]).

## Covered in
- [[why-database-indexes]] — introduced as the mechanism (aka full-text index) for mid-string search; teased as a future hands-on video
- [[full-text-search-inverted-indexes]] — built live in JavaScript: word → (doc id, position), phrase/proximity queries, the 300 TB production war story
- [[full-text-search-part-2-qa]] — the tokens-file + binary-postings split (1.3 GB → 938 MB, 15 ms → 5 ms) and S3 Range-request serverless search
- [[qa-1-will-https-protect-you]] — you change serialization, not the structure; delta compression makes bigger indexes fit in RAM

## Related
[[full-text-search]] — the pipeline around the structure
[[index-compression]] — delta encoding and varbyte over the posting lists
[[map-reduce]] — how he built it without 10–15 GB of RAM
[[database-indexes]] — the B-tree counterpart it complements
[[base64]] — the serialization overhead the part-2 optimization removed
