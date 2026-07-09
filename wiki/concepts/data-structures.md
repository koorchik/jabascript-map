---
type: concept
tags: [data-structures, algorithms, fundamentals]
---
# Data structures

The channel's stance: what matters in practice is knowing each structure's properties and time/memory complexity, not memorizing implementations — though Viktor has implemented topological sort and full-text search himself when the problem demanded it ([[qa-2-answering-questions]]). The tree family gets the hands-on walkthrough: binary search trees ("left smaller, right bigger"), their degenerate case (insert 1..5 in order and the tree collapses into a linked list with O(N) search), AVL-style self-balancing rotations keeping subtree heights within 1, and the jump to disk-friendly [[b-tree|B-trees]] — with the aside that ext4 filesystems use an H-tree, a simplified B-tree analog ([[trees-search-algorithms-databases]]).

Beyond trees: the hash map as the fix for nested-loop merges (build a map keyed by user id once, then O(1) lookups), contrasted with sorted arrays — binary-searchable but expensive to sort, worth it only if you sort once and search a hundred times ([[why-algorithms-matter]]). And the probabilistic branch: [[bloom-filter|Bloom filters]], implemented as a bit array packed into a Uint32Array with div/mod-32 bit addressing. His argument that none of this is theoretical: Firefox ships a Bloom-filter cascade in production since 2025, Silpo runs one in its CRM, and no npm library even exists for the cascade variant — sometimes you must build the structure yourself ([[bloom-filter-and-firefox]]).

## Covered in
- [[trees-search-algorithms-databases]] — the tree family hands-on: BSTs, the degenerate linked-list case, AVL rotations, ext4's H-tree
- [[why-algorithms-matter]] — hash maps vs sorted arrays: which structure for which access pattern
- [[bloom-filter-and-firefox]] — probabilistic structures; bit-array implementation details; "these aren't theoretical"
- [[qa-2-answering-questions]] — know properties and complexity, not memorized code; his own hand-implementations

## Related
[[algorithmic-complexity]] — the yardstick structures are measured by
[[b-tree]] — the tree that databases actually use
[[bloom-filter]] — the probabilistic star of the cluster
[[database-indexes]] — data structures at industrial scale
[[deep-learning-of-fundamentals]] — why properties, not implementations, are the durable knowledge
