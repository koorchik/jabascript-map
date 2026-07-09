---
type: video
title_uk: "Дерева. Пошук. Алгоритми. Бази даних"
youtube_id: 7xoYPVZVHX4
tags: [databases, data-structures, algorithms, trees]
date_ingested: 2026-07-09
---
# Trees, Search, Algorithms, Databases

> Original: "Дерева. Пошук. Алгоритми. Бази даних" — https://youtu.be/7xoYPVZVHX4

A whiteboard "bridge" video the author made deliberately as preparation for his MySQL-vs-Postgres index deep dive: which tree [[data-structures]] databases actually use inside [[database-indexes]] and why. Starting from a products table, he recaps that a sorted copy of a column enables binary search — his recurring number: 100 trillion records searched in ~46 halvings instead of 100 trillion steps ([[algorithmic-complexity]]) — but a sorted array makes inserts O(N), so we need trees. He draws a binary search tree ("everything left of 7 is smaller, everything right is bigger") and shows its trap: insert 1,2,3,4,5 in order and the BST degenerates into a linked list with O(N) search, hence self-balancing variants like AVL trees that rotate nodes on insert to keep left/right heights within 1. Then the key argument: databases still don't use binary trees, because with 100M records the tree is ~23 levels deep, and if each level costs a disk seek (~5 ms on a spinning disk), 23×5 ms is too slow. A [[b-tree|B-tree]] gives each node many children — in Postgres/MySQL a node is sized to a disk block (e.g. 8 KB), giving roughly 200–2000 children per node — collapsing the depth from ~23 levels to ~4, or even 2, disk reads. Finally he explains why databases use the **B+ tree** modification: data lives only in the leaf nodes, and leaves point to each other in a linked chain, so range queries ("price from 100 to 110") and full index scans just walk sideways along the leaves without bouncing up and down the tree.

## Key takeaways
- An index is conceptually a copied, sorted column; you can't keep one table sorted by both name and price at once, so each index is its own sorted structure ([[database-indexes]]).
- Sorted data gives O(log N) binary search — 100 trillion records in ~46 steps — but insertion into a sorted array is O(N), which is why trees are needed ([[algorithmic-complexity]]).
- A plain binary search tree degenerates into a linked list (his example: inserting 1..5 in order — every node hangs off the right), making search O(N); balanced variants (AVL and friends) rotate nodes during insert to keep the tree's height minimal ([[data-structures]]).
- Databases reject binary trees for a hardware reason: ~23 levels deep at 100M rows × ~5 ms per disk seek is too slow; a [[b-tree]] node sized to a disk block (8 KB, ~200–2000 children) cuts depth to ~4 levels, sometimes 2.
- B+ trees (what databases actually use) keep data only in leaf nodes and chain the leaves together, so range scans ("price 100–110") walk the leaf chain without re-descending the tree.
- Deliberately concept-level: he skips rotation/split mechanics — "what matters is understanding how this shapes database behavior" — as setup for the [[database-indexes-mysql-vs-postgres]] video.
- Teaser: file systems use the same ideas — ext4 indexes files with an H-tree, a simplified B-tree analog; k-nearest / quadtrees promised as future topics.

## Covered
[[b-tree]], [[data-structures]], [[algorithmic-complexity]], [[database-indexes]], [[mysql]], [[postgresql]]
