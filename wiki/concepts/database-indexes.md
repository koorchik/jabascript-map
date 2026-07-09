---
type: concept
tags: [databases, performance, indexes, mysql, postgresql]
---
# Database indexes

The channel's single densest topic. Viktor's core framing: an index is conceptually just "copy the column and sort it" — a sorted structure stored beside the table, holding the indexed column plus a pointer to the row ([[why-database-indexes]], [[qa-and-plans-for-2024]]). Because you can't keep one table sorted by two columns at once, each index is its own separate structure ([[trees-search-algorithms-databases]]). His signature demo: an identical query on 1K rows takes 0.3 ms and on 10M rows takes 3.3 s; add an index and it drops to ~0.05 ms — roughly 60,000x faster — because sorting turns an O(N) scan into O(log N) binary search ([[why-database-indexes]], [[why-algorithms-matter]]). In the Bloom-filter benchmarks the same effect shows again: an unindexed MySQL scan takes ~18 s for 10 missing-key queries, while an indexed table does 100,000 queries in ~17 s — "indexes are unbelievably fast" ([[bloom-filter-and-firefox]]).

But indexes are not free, and much of the coverage is about where they hurt or fail. Every write must update all indexes on the table — his 16M-row experiment shows dropping indexes cuts insert time from 5.5 s to 1.2 s per batch, so write-heavy tables should index less ([[database-indexes-mysql-vs-postgres]], [[why-database-indexes]]). Slow queries are not just slow: a 3-second query stacks up under web load and takes down the whole database ([[why-database-indexes]]). And a B-tree index only helps when a sort order exists: `LIKE 'prefix%'` is instant while `LIKE '%word%'` takes 40 s, because you cannot sort a column by a word inside the value — the failure that motivates the [[inverted-index]] ([[full-text-search-inverted-indexes]]).

The deep-dive layer is engine internals. In MySQL the table itself is a clustered index (a [[b-tree|B+ tree]] sorted by primary key), so a secondary-index lookup is a double search: secondary index → primary key → clustered index. Postgres instead stores physical row addresses into an unordered heap ([[database-indexes-mysql-vs-postgres]]). From there come the practical tricks he demos: covering indexes (add display-only columns to an index and a ~10 s query becomes instant; composite two-column indexes are a two-level sort that serves (A) and (A,B) but never (B) alone), the hidden cost of `OFFSET 1000000` pagination even with an index, selectivity governing whether an index helps at all, and even Handler Socket — direct index access bypassing MySQL's query planner, turning it into a key-value store, which turned out only marginally faster than indexed prepared statements ([[database-indexes-mysql-vs-postgres]], [[qa-and-plans-for-2024]], [[bloom-filter-and-firefox]]). Key size matters too: since UUIDs are hex, storing them as raw binary halves them, yet a BINARY(16) primary key still eats over half the index bytes — he'd keep the auto-increment PK and put the UUID in a separate column ([[how-base64-works]], [[qa-1-will-https-protect-you]], [[uuid-vs-auto-increment]]).

## Covered in
- [[why-database-indexes]] — the hands-on origin demo: 3.3 s → 0.05 ms on 10M rows, what an index physically is, and why write-heavy tables should index less
- [[database-indexes-mysql-vs-postgres]] — internals deep dive: clustered vs heap tables, double search, covering indexes, OFFSET cost, insert benchmarks with and without indexes
- [[trees-search-algorithms-databases]] — the conceptual prep: an index as a copied, sorted column; why each index is its own structure
- [[full-text-search-inverted-indexes]] — where B-tree indexes fail: `LIKE '%word%'` takes 40 s because no sort order helps mid-string search
- [[why-algorithms-matter]] — maps the missing index onto his JS benchmarks: without one it's the same linear scan; with one, lookups stay ~1 ms from 1K to 10M rows
- [[bloom-filter-and-firefox]] — benchmark context (full scan vs index) plus Handler Socket direct-to-index access
- [[how-base64-works]] — side note: hex UUIDs stored as raw binary halve in size, shown with actual files
- [[qa-1-will-https-protect-you]] — BINARY(16) UUID keys give only modest savings; he'd keep UUID as a separate column
- [[qa-and-plans-for-2024]] — live whiteboard of composite indexes, covering indexes, and selectivity

## Related
[[b-tree]] — the structure indexes are actually made of
[[algorithmic-complexity]] — O(N) vs O(log N) is the entire point of an index
[[uuid-vs-auto-increment]] — how primary-key choice inflates or shrinks every index
[[mvcc]] — why updates rebuild indexes differently in MySQL vs Postgres
[[inverted-index]] — the index type that takes over where B-trees fail
[[data-structures]] — indexes as the flagship example of knowing structures' properties
