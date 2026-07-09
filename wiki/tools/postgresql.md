---
type: tool
tags: [databases, sql, relational]
---
# PostgreSQL

On the channel, Postgres is the architectural counterpoint to [[mysql]]: no clustered indexes at all. Tables are unordered heaps, indexes store physical row addresses (visible via `ctid`), and secondary indexes don't embed the primary key — which is why random UUID primary keys cost Postgres little while devastating MySQL ([[database-indexes-mysql-vs-postgres]], [[uuid-vs-auto-increment]]). The trade-off runs the other way under [[mvcc]]: because updated row versions land at new physical addresses, updating one indexed column forces a rebuild of ALL indexes on the table (the HOT optimization only helps within one 8 KB block) — internals Viktor connects to Uber's famous Postgres → MySQL → Postgres migrations.

Elsewhere it appears as the same-but-different sibling: `EXPLAIN` exists there too ([[why-database-indexes]]), its 8 KB block size determines B+ tree fan-out (~200–2000 children per node) and thus tree depth ([[trees-search-algorithms-databases]]), and knowing what an UPDATE actually does in Postgres vs MySQL is his example of the internals knowledge that lets you predict behavior at scale ([[3-things-that-make-a-programmer-better]]).

## Covered in
- [[database-indexes-mysql-vs-postgres]] — heap tables, ctid, MVCC index rebuilds, UUID immunity
- [[why-database-indexes]] — contrast mention: no clustered indexes, deep dive promised
- [[trees-search-algorithms-databases]] — 8 KB blocks sizing B+ tree nodes
- [[3-things-that-make-a-programmer-better]] — internals knowledge as what separates good from great

## Related
[[mysql]], [[database-indexes]], [[mvcc]], [[uuid-vs-auto-increment]], [[b-tree]]
