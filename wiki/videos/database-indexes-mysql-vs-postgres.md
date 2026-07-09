---
type: video
title_uk: "Як працюють індекси в базах на прикладі. MySQL vs Postgres. UUID vs Auto Increment."
youtube_id: Ot7b03Fj_mo
tags: [databases, indexes, mysql, postgresql, performance]
date_ingested: 2026-07-09
---
# How Indexes Really Work: MySQL vs Postgres, UUID vs Auto Increment

> Original: "Як працюють індекси в базах на прикладі. MySQL vs Postgres. UUID vs Auto Increment." — https://youtu.be/Ot7b03Fj_mo

The "hardcore" payoff of the index series: half theory, half live experiments on a 16M-row table, all in service of the author's thesis that you must understand internals to predict a technology's properties ([[deep-learning-of-fundamentals]]). Core internals: in [[mysql|MySQL]] the table *itself* is a [[b-tree|B+ tree]] sorted by primary key (clustered index), so every secondary-index lookup is a **double search** — first the secondary index (which stores the primary key as row pointer), then the clustered index; [[postgresql|Postgres]] has no clustered index — secondary indexes store the row's physical file location. He then explains [[mvcc|MVCC]]: both databases copy rows per transaction, and because Postgres row copies land at new physical addresses, updating *one* indexed column forces Postgres to rebuild **all** indexes on the table (the HOT — heap-only tuple — optimization only helps if the copy fits the same block and no indexed column changed); MySQL updates only the affected index. He nods to Uber's famous Postgres→MySQL→Postgres migrations as consequences of exactly these nuances. The practical centerpiece is [[uuid-vs-auto-increment]]: because MySQL duplicates the primary key in every secondary index, a UUID primary key is "catastrophic" there — his measured tables: auto-increment 4.3 GB, auto-increment + separate UUID column 4.9 GB, UUID-as-PK 7.8 GB; secondary indexes ballooned from 2 GB to 5.5 GB, meaning ~70% of index bytes were just the UUID PK. Random UUID inserts also wreck B+ tree node caching — inserts went from ~4 s to ~5.5 s per 1000 rows even on his top-of-the-line SSD (he saw 2.5–3× on slower disks). Further experiments: covering indexes (add a column you never filter by — e.g. `(year, name)` — so the query never touches the main table; `EXPLAIN` shows "covering index"), the hidden cost of `OFFSET 1000000` pagination even with an index (~10 s, because the leaf chain must be scanned a million entries deep), and dropping indexes cutting insert time from 5.5 s to ~1.2 s.

## Key takeaways
- MySQL's table is itself a B+ tree ordered by primary key (clustered index); secondary indexes store the PK, so non-PK lookups search twice. Postgres tables are unordered heaps; indexes point to physical row locations ([[database-indexes]], [[b-tree]]).
- Under [[mvcc]], a Postgres update moves the row physically, so it must update *every* index on the table — even if you changed a non-indexed column (HOT optimization helps only within one 8 KB block); MySQL, referencing rows by PK, touches only the changed index. He cites Uber's back-and-forth database migrations as fallout from these internals.
- [[uuid-vs-auto-increment]] in MySQL: UUID as primary key inflated his table from 4.3 GB to 7.8 GB and secondary indexes from 2 GB to 5.5 GB (~70% of index space was the PK itself, nearly 3× more index RAM needed); the counterintuitive fix — keep an auto-increment PK and store UUID as an extra column — is *smaller* and faster despite "adding" a column. Postgres is largely immune since it never embeds the PK in other indexes.
- Random (UUID) inserts break B+ tree node caching: sequential inserts touch only the rightmost cached nodes, random ones thrash the cache — 1000-row inserts went 4 s → 5.5 s on the fastest consumer SSD, 2.5–3× worse on slower storage.
- MySQL cannot have a table without a primary key — if you omit it, it silently adds a hidden 6-byte auto-increment; declaring your own 4-byte one saves 2 bytes × every row × every index (gigabytes of RAM at 100M rows, and indexes should live in RAM).
- Covering indexes: appending a display-only column to an index (e.g. `(year, name)`) lets the whole query be answered from the index — he demos a query dropping from ~10 s to instant — at the cost of extra copies on disk.
- Even with an index, `ORDER BY ... OFFSET 1000000 LIMIT 1` is slow: the sorted leaf chain must still be walked a million entries — so "last page" pagination hurts at scale.
- Indexes tax writes: dropping his secondary indexes cut insert time ~4× (5.5 s → 1.2 s per batch); don't index everything by default.
- Closing frame: of three programmers — one unaware indexes exist, one who knows "indexes make it faster", one who understands their internals — only the third can actually design for and predict the database's behavior ([[deep-learning-of-fundamentals]]).

## Covered
[[database-indexes]], [[b-tree]], [[mvcc]], [[uuid-vs-auto-increment]], [[algorithmic-complexity]], [[deep-learning-of-fundamentals]], [[mysql]], [[postgresql]], [[full-text-search]]
