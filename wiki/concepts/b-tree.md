---
type: concept
tags: [databases, data-structures, indexes, algorithms]
---
# B-tree / B+ tree

Viktor's whiteboard explanation of why database indexes are not binary search trees: a BST over 100M rows is ~23 levels deep, and at ~5 ms per disk seek that depth is fatal. B-trees fix it by sizing each node to a disk block (8 KB in Postgres/MySQL), giving each node roughly 200–2000 children and cutting the tree to ~4 or even 2 levels ([[trees-search-algorithms-databases]]). Databases actually use B+ trees: data lives only in the leaves, and the leaves are chained sideways, so a range scan like "price 100–110" walks the leaf chain instead of re-descending the tree — which is also why B+ trees, not sorted arrays, are the real implementation behind the O(log n) behaviour he benchmarks ([[why-algorithms-matter]]).

The internals matter in practice. In MySQL the table itself IS a B+ tree sorted by primary key (the clustered index) — which is why random UUID inserts thrash the tree's node caching, while sequential auto-increment inserts only ever touch the cached rightmost nodes ([[database-indexes-mysql-vs-postgres]]). He first teased this in the original index video: the index is really a B+ tree, not a plain BST, hash indexes also exist, and a plain sorted list would work too but cost O(N) to maintain ([[why-database-indexes]]).

## Covered in
- [[trees-search-algorithms-databases]] — the definitive treatment: BST depth vs disk seeks, block-sized nodes, B+ leaf chaining for range scans
- [[database-indexes-mysql-vs-postgres]] — the MySQL table as a B+ tree, and why UUID inserts thrash it
- [[why-database-indexes]] — first mention: the index is a B+ tree; hash indexes exist; sorted lists would be O(N) to maintain
- [[why-algorithms-matter]] — real DB indexes are balanced B+ trees, preserving binary search's O(log n) plus range scans

## Related
[[database-indexes]] — what B+ trees are built to serve
[[data-structures]] — BSTs, AVL balancing, and the degenerate cases B-trees avoid
[[algorithmic-complexity]] — the log-N guarantee the tree exists to protect
[[uuid-vs-auto-increment]] — insert order vs B+ tree caching
