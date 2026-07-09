---
type: concept
tags: [databases, postgresql, mysql, internals, transactions]
---
# MVCC (Multi-Version Concurrency Control)

Covered as the hidden mechanism behind a real architectural difference between MySQL and Postgres. Both databases copy rows per transaction, but in Postgres the copies land at new physical addresses — and since Postgres secondary indexes point at physical row locations, updating even one indexed column forces a rebuild of ALL indexes on the table. The HOT (heap-only tuple) optimization only helps when the new version fits within the same 8 KB block. MySQL, by contrast, updates only the index actually affected by the change ([[database-indexes-mysql-vs-postgres]]).

Viktor grounds this in industry fallout: Uber's famous Postgres → MySQL → Postgres migration saga was driven by exactly these internals — a reminder that "which database is better" depends on whether your workload is update-heavy on indexed tables, not on hype.

## Covered in
- [[database-indexes-mysql-vs-postgres]] — the full explanation: per-transaction row copies, Postgres all-index rebuilds vs MySQL's targeted updates, HOT limits, and the Uber migration story

## Related
[[database-indexes]] — MVCC determines what an UPDATE costs your indexes
[[b-tree]] — the structures being rebuilt
[[deep-learning-of-fundamentals]] — his broader point: internals like this are what let you predict behavior at scale
