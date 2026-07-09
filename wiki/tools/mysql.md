---
type: tool
tags: [databases, sql, relational]
---
# MySQL

The channel's default experiment platform: nearly every database demo runs on MySQL, using `SET profiling`, `CREATE INDEX`, and `EXPLAIN` ([[why-database-indexes]]). Its defining architectural trait in Viktor's telling is the clustered index: the table itself is a [[b-tree|B+ tree]] sorted by primary key — it literally can't exist without one (omit a PK and MySQL silently adds a hidden 6-byte one). That drives everything he measures: secondary lookups are a double search, and random-UUID primary keys inflate a 4.3 GB table to 7.8 GB and slow inserts 2.5–3x on slow disks — the core of the [[uuid-vs-auto-increment]] verdict ([[database-indexes-mysql-vs-postgres]]). The upside vs [[postgresql]]: under [[mvcc]], MySQL updates only the index actually affected by a change rather than rebuilding all of them.

In the full-text arc MySQL plays both baseline and rival: `LIKE '%...%'` takes 40 s on 16.5M rows (and times out entirely on an HDD), while `CREATE FULLTEXT INDEX` takes 14 minutes and 1.7 GB — bigger than his hand-rolled 1.3 GB inverted index — though it does support boolean must/must-not queries; internally InnoDB FULLTEXT solves the UUID-doc-id problem with a hidden auto-increment FTS_DOC_ID column ([[full-text-search-inverted-indexes]], [[full-text-search-part-2-qa]]). In the Bloom-filter benchmarks he notes MySQL point lookups are nearly cache-fast — the slowness lives in scans and joins — and demos Handler Socket, direct-to-index access bypassing the query planner (a trick he evaluated back in his Portal-era work), which turns out only marginally faster than indexed prepared statements ([[bloom-filter-and-firefox]]). MySQL is also his stock example of necessary depth: if you don't know how it processes an UPDATE or handles growing data, you don't know its properties ([[3-things-that-make-a-programmer-better]]).

## Covered in
- [[why-database-indexes]] — all the original index demos: profiling, EXPLAIN, 3.3 s → 0.05 ms
- [[database-indexes-mysql-vs-postgres]] — three 16M-row tables, covering indexes in EXPLAIN, insert benchmarks, clustered-index architecture
- [[trees-search-algorithms-databases]] — index tree nodes bounded by block size, not element count
- [[full-text-search-inverted-indexes]] — LIKE baseline vs FULLTEXT rival (1.7 GB, 14 min build)
- [[full-text-search-part-2-qa]] — InnoDB's hidden FTS_DOC_ID column; LIKE timing out on an HDD
- [[bloom-filter-and-firefox]] — 10M-key benchmarks and the Handler Socket detour
- [[qa-1-will-https-protect-you]] — BINARY(16) UUID keys in practice
- [[3-things-that-make-a-programmer-better]] — MySQL internals as the example of needed depth

## Related
[[database-indexes]], [[b-tree]], [[uuid-vs-auto-increment]], [[mvcc]], [[full-text-search]], [[postgresql]]
