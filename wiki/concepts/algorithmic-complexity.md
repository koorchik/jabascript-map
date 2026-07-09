---
type: concept
tags: [algorithms, performance, fundamentals]
---
# Algorithmic complexity

The channel's recurring backbone: complexity is how work grows with input size, independent of language speed. Viktor's signature illustration is the power of log N: 50 rows take 50 steps linearly, but 100 trillion rows take only ~46 binary-search steps — "log N is practically free" ([[why-database-indexes]], [[database-indexes-mysql-vs-postgres]], [[trees-search-algorithms-databases]]). The flip side he always adds: sorted-array insertion is O(N), which is the entire motivation for tree structures ([[trees-search-algorithms-databases]]).

His hands-on proof is the message-merge example: joining 2000 messages with 100 users via nested `find` costs ~200,000 operations; building a hash map first cuts it to ~2100 (O(n*m) → O(n+m)). And constants matter too: a pure-JS binary search (O(log n)) beats C++-implemented `Array.includes` (O(n)) at scale, while the ~23x gap between `find` and `includes` shows implementation constants are real — but never beat asymptotics ([[why-algorithms-matter]]). The same lens runs through the Bloom-filter benchmarks: full scan vs index vs in-memory vs filter is about orders of magnitude, not tuned configs — "what interests us is the order of the numbers" ([[bloom-filter-and-firefox]]).

His career-level take: you rarely hand-code algorithms, but you must analyze complexity — in code reviews he routinely spots O(n²) and cubic hotspots just by reading. War story: an Excel-in-JS engine required rewriting topological sort iteratively with a hand-rolled stack, because JS's ~10k stack-frame limit broke on dependency chains longer than 10k cells ([[qa-2-answering-questions]]). He also singles out Cracking the Coding Interview's complexity-analysis chapter as one of the two genuinely valuable parts of that book ([[five-star-books]]).

## Covered in
- [[why-algorithms-matter]] — the core lesson: O(n*m) vs O(n+m) live-coded, JS benchmarks, constants vs asymptotics
- [[why-database-indexes]] — O(N) scan vs O(log N) index; the 100-trillion-rows-in-46-steps illustration
- [[database-indexes-mysql-vs-postgres]] — recaps why sorted data makes indexes work at all
- [[trees-search-algorithms-databases]] — binary search's ~46 halvings vs O(N) sorted-array insertion motivating trees
- [[bloom-filter-and-firefox]] — the benchmark ladder as an exercise in orders of magnitude
- [[qa-2-answering-questions]] — complexity analysis in code review; the topological-sort stack-limit war story
- [[five-star-books]] — Cracking the Coding Interview's complexity chapter praised

## Related
[[data-structures]] — structures are chosen by their complexity properties
[[database-indexes]] — the industrial-scale application of O(log N)
[[b-tree]] — keeping the logarithm shallow on disk
[[deep-learning-of-fundamentals]] — complexity as trunk-level knowledge that never falls off
