---
type: video
title_uk: "Навіщо потрібні індекси в базі даних？ Розберемо на прикладі"
youtube_id: YF8xDeYlG9w
tags: [databases, indexes, algorithms, performance]
date_ingested: 2026-07-09
---
# Why Do Databases Need Indexes? A Hands-On Example

> Original: "Навіщо потрібні індекси в базі даних？ Розберемо на прикладі" — https://youtu.be/YF8xDeYlG9w

A live-demo introduction to [[database-indexes]]: the author prepares two [[mysql|MySQL]] databases — one `products` table with 1K rows, one with 10 million — and measures the same `SELECT` with SQL profiling enabled. On the small table the query takes ~0.3 ms; on the 10M-row table the identical query takes 3.3 seconds, which he calls a catastrophe for a web app: requests arriving faster than they complete will pile up and take the whole database down. Adding an index on `name` makes the same query run in ~0.05 ms — he does the division on screen: roughly **60,000× faster**. The reason is [[algorithmic-complexity]]: an index is a *separate sorted structure* living next to the table, so lookups become binary search — O(log N) instead of O(N) full scans. His signature illustration: with 50 rows a linear scan does 50 steps, but with 100 trillion rows a binary search needs only ~46 steps — "log N is practically free". He then shows where indexes break: `LIKE 'prefix%'` is instant (sorted data supports prefix search), but `LIKE '%substring%'` takes ~7 seconds, because no sort order helps you find a phrase *in the middle* of a value — that job needs an inverted / full-text index ("everyone says 'use Elastic', but what is Elastic actually doing?"), which he promises to build by hand in a later video, mentioning he once implemented a custom [[full-text-search]] index over 300 TB of data in production. He closes with `EXPLAIN` to check index usage, a peek at how the index stores the indexed column plus a row pointer, and a caveat: every write must rebuild indexes, so write-heavy tables should not index every column.

## Key takeaways
- Real measurement, same query: 1K rows ≈ 0.3 ms, 10M rows ≈ 3.3 s without an index; with an index on `name` ≈ 0.05 ms — about 60,000× faster ([[database-indexes]]).
- A 3-second query is not just slow — under web load requests accumulate faster than they finish and the database collapses.
- An index is a sorted data structure stored *beside* the table (in practice a [[b-tree|B+ tree]]; hash indexes also exist); sorted data enables binary search, and O(log N) means ~46 steps even for 100 trillion rows ([[algorithmic-complexity]]).
- Indexes work for exact matches and `LIKE 'prefix%'`, and even suffix search if you build the index the other way — but never for `LIKE '%word%'`: "sort it or not, nothing helps you find a phrase inside" — that requires an [[inverted-index]] ([[full-text-search]]).
- Use `EXPLAIN` (MySQL and [[postgresql|Postgres]] alike) to verify whether a query actually uses an index.
- The index stores the indexed column plus a pointer to the row; fetching other columns (e.g. `description`) requires a second lookup into the table — and MySQL and Postgres organize tables completely differently (clustered index vs heap; MySQL effectively cannot exist without a primary key).
- Indexes are not free: every INSERT/UPDATE rebuilds every index on the table, so with heavy write traffic, fewer indexes may be better.
- War story: he once built a hand-rolled full-text (inverted) index searching 300 TB of data, including a custom index-packing mechanism.

## Covered
[[database-indexes]], [[algorithmic-complexity]], [[b-tree]], [[full-text-search]], [[inverted-index]], [[mysql]], [[postgresql]]
