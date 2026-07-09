---
type: concept
tags: [databases, mysql, postgresql, primary-keys, performance]
---
# UUID vs auto-increment primary keys

One of the channel's most measured claims: random UUID primary keys are catastrophic in MySQL but largely harmless in Postgres — because in MySQL the table itself is a clustered [[b-tree|B+ tree]] sorted by PK, and every secondary index embeds the PK. His 16M-row numbers: switching to a UUID PK inflates a 4.3 GB table to 7.8 GB and the secondary indexes from 2 GB to 5.5 GB (~70% of index bytes end up being just the primary key); inserts slow from 4 s to 5.5 s per 1000 rows on the fastest SSD, and 2.5–3x on slower disks, because random UUIDs thrash B+ tree node caching while sequential IDs only touch the cached rightmost nodes. Postgres, with heap tables and physical row pointers, is largely immune. Bonus trivia: if you omit a PK, MySQL silently adds a hidden 6-byte one anyway ([[database-indexes-mysql-vs-postgres]]).

His counterintuitive fix: don't choose — keep the auto-increment PK for the engine and store the UUID as an extra column for the outside world; it's smaller and faster than either pure option. Storing UUIDs as BINARY(16) instead of 32-char text helps only modestly (index share drops from ~70% to ~55%) and makes them harder to read and display, so he'd still prefer the separate column ([[qa-1-will-https-protect-you]]). The same problem resurfaces in full-text search: UUID document ids defeat posting-list compression entirely, so you map them to integers — which is exactly what MySQL/InnoDB FULLTEXT does internally with its hidden auto-increment FTS_DOC_ID column ([[full-text-search-part-2-qa]]).

## Covered in
- [[database-indexes-mysql-vs-postgres]] — the definitive benchmark: table/index bloat numbers, insert slowdowns, why Postgres doesn't care, and the auto-increment-plus-UUID-column fix
- [[qa-1-will-https-protect-you]] — follow-up on BINARY(16) storage: modest savings, worse ergonomics
- [[full-text-search-part-2-qa]] — UUIDs as doc ids can't be delta-compressed; InnoDB's hidden FTS_DOC_ID is the same integer-mapping trick
- [[how-base64-works]] — side demonstration that hex-encoded UUIDs stored as raw binary halve in size

## Related
[[database-indexes]] — the PK choice ripples into every index on the table
[[b-tree]] — insert order vs node caching is the mechanism behind the slowdown
[[index-compression]] — sorted integers compress; random UUIDs don't
[[mvcc]] — the other big MySQL-vs-Postgres internals difference from the same video
