---
type: concept
tags: [databases, search, compression, indexes]
---
# Index compression

How Viktor shrinks an inverted index stage by stage, with the sizes on screen: raw JSON 4 GB → flattened arrays 3.4 GB → delta-encoded sorted doc ids (store `100, 3, 5` instead of `100, 103, 108`) 2.3 GB → varbyte encoding (7 data bits + 1 continuation bit per byte) wrapped in base64 → 1.3 GB — smaller than MySQL's own FULLTEXT index at 1.7 GB ([[full-text-search-inverted-indexes]]). Delta compression is the enabler: it turns large ids into small integers so VByte (from a paper he references) can pack them tightly, which also speeds filesystem reads and lets a bigger index fit in RAM ([[qa-1-will-https-protect-you]]).

In the Q&A follow-up he shows a survey paper of posting-list compression algorithms and draws the honest conclusions: they all presuppose sorted integers, there is no universal winner, and varbyte is decent everywhere. The corollary bites in practice: UUID doc ids defeat all of them — you must map UUIDs to integers first, exactly what InnoDB's hidden FTS_DOC_ID column does ([[full-text-search-part-2-qa]], [[uuid-vs-auto-increment]]).

## Covered in
- [[full-text-search-inverted-indexes]] — the full compression ladder with on-screen sizes: 4 GB → 1.3 GB, beating MySQL FULLTEXT's 1.7 GB
- [[full-text-search-part-2-qa]] — the survey paper: all algorithms assume sorted integers, no universal winner, UUIDs break everything
- [[qa-1-will-https-protect-you]] — delta compression as the enabler for VByte, faster reads, and RAM-resident indexes

## Related
[[inverted-index]] — the structure being compressed
[[uuid-vs-auto-increment]] — why doc-id choice makes or breaks compression
[[base64]] — the +33% serialization overhead removed in part 2
[[encoding]] — varbyte as an encoding scheme
