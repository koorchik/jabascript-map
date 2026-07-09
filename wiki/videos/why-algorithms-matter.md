---
type: video
title_uk: "Чому алгоритми важливі？ Розберемо на прикладі"
youtube_id: 9Gtwj0Eo8IY
tags: [algorithms, complexity, javascript, databases, performance]
date_ingested: 2026-07-09
---
# Why Algorithms Matter — Shown on a Real Example

> Original: "Чому алгоритми важливі？ Розберемо на прикладі" — https://youtu.be/9Gtwj0Eo8IY

Instead of dry theory, the author live-codes an everyday task — merging an array of messages with an array of users to attach a `username` to each message — and analyzes it through the lens of [[algorithmic-complexity]]. The naive version calls `users.find()` inside a loop over messages, which is O(M × U); the optimized version first builds a hash map keyed by user id, dropping the whole thing to O(M + U). He then benchmarks search over a 100,000-element array (code is on his GitHub, linked in the description): `Array.find` vs `Array.includes` vs a binary search he wrote in plain JavaScript — and the pure-JS binary search beats even `includes`, which is implemented in C++, because O(log n) always wins over O(n) once data grows. He closes by mapping this straight onto [[database-indexes]]: a query without an index is the same linear scan, while an index gives you binary-search-like behaviour over a sorted structure (in practice a balanced [[b-tree]] / B+ tree, not a sorted array).

## Key takeaways
- Algorithmic complexity is about how work grows with input size, not raw language speed: an O(n²) function stays quadratic whether it's JavaScript or C++ — with 10× more data you get ~100× more operations "and it's not obvious from the code why everything got slow".
- The merge example in numbers: 2,000 messages × 100 users ≈ 200,000 operations for the nested `find` version vs ~2,100 for the hash-map version (build the map in O(U), then O(1) lookups per message thanks to [[hashing]]-based maps). The fix added only ~6 lines of code.
- Benchmark surprise #1: `includes` (native C++ loop) is ~23× faster than `find` (which calls a JS callback per element) — constant factors matter too.
- Benchmark surprise #2: binary search written in plain JS beats the C++ `includes`, because it is O(log n). At 100 million elements the linear scans crawl while binary search answers in fractions of a millisecond — "at ~100 billion elements a linear scan needs ~100 billion operations; binary search needs about one more step when data doubles".
- Binary search requires a sorted array and sorting is expensive — but if you sort once and search 100 times, it pays off massively.
- This is exactly what a database does: without an index MySQL/PostgreSQL linearly scan all rows; an index is a sorted structure the engine can binary-search. Real databases use a balanced [[b-tree]] (B+ tree, because it also supports range scans), which keeps O(log n) lookups — 1,000 rows or 10 million rows, the query stays around a millisecond.
- Final merge benchmark with 1,000 users × 1,000 messages showed roughly a 60× difference — and this matters even on the frontend; in Python without a JIT the slow version would hurt ~10× more.

## Covered
[[algorithmic-complexity]], [[data-structures]], [[hashing]], [[database-indexes]], [[b-tree]]
