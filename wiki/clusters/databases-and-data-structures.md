---
type: cluster
tags: [moc, databases, data-structures, algorithms, search]
---
# Databases & Data Structures

The channel's densest and most deliberately sequenced cluster. Viktor builds a learning path where each video creates the problem the next one solves: first the raw shock of *why indexes* (the same query, 60,000x faster), then *trees* to explain what an index physically is and why disks demand shallow B+ trees, then *index internals* (MySQL vs Postgres, clustered vs heap, UUID vs auto-increment — with 16M-row experiments), then the place where B-trees fail — mid-string search — which opens *full-text search and inverted indexes* (hand-built, compressed, and benchmarked against MySQL's own FULLTEXT), and finally *Bloom filters* as the probabilistic capstone that outruns every database and cache in the ladder. Everything is measured live, everything is grounded in his war stories — above all the 300 TB full-text search system he hand-built in production — and the recurring moral is the channel's thesis: know your tools' properties and internals, not the hype.

## Concepts

- [[database-indexes]] — the hub: what an index is, when it saves you 60,000x, and when it betrays you
- [[algorithmic-complexity]] — O(N) vs O(log N); 100 trillion rows in ~46 steps; "log N is practically free"
- [[data-structures]] — BSTs, AVL rotations, hash maps, sorted arrays: properties over implementations
- [[b-tree]] — why databases use shallow, block-sized B+ trees instead of binary trees
- [[mvcc]] — row versioning, and why a Postgres UPDATE can rebuild every index on the table
- [[uuid-vs-auto-increment]] — measured verdict: catastrophic in MySQL, fine in Postgres; keep both columns
- [[full-text-search]] — tokenization, stemming vs lemmatization, "search differently ⇒ index differently"
- [[inverted-index]] — word → (doc, position); his 300 TB production war story; serverless search via S3 Range requests
- [[index-compression]] — delta encoding + varbyte: 4 GB → 1.3 GB, smaller than MySQL FULLTEXT
- [[map-reduce]] — building the index without RAM: Node.js map, Unix sort as shuffle, Hadoop streaming
- [[bloom-filter]] — no false negatives, tunable false positives, and Firefox's CRLite cascade

## Videos (the learning path)

1. [[why-database-indexes]] — live MySQL demo: 3.3 s → 0.05 ms on 10M rows, plus where indexes break down
2. [[why-algorithms-matter]] — O(n*m) vs O(n+m) live-coded in JS, mapped onto database indexes
3. [[trees-search-algorithms-databases]] — whiteboard bridge: binary search → BSTs → AVL → shallow disk-block B+ trees
4. [[database-indexes-mysql-vs-postgres]] — hardcore internals with 16M-row experiments: clustered vs heap, MVCC, UUID penalties
5. [[full-text-search-inverted-indexes]] — hand-builds a production-grade inverted index via map-reduce; beats MySQL LIKE 40 s → 21 ms
6. [[full-text-search-part-2-qa]] — tokens-file + binary-postings split, n-gram tokenizers, S3 Range-request search
7. [[bloom-filter-and-firefox]] — Bloom filters vs Map/MySQL/Redis/Memcached on 10M keys, and Firefox's CRLite cascade
8. [[qa-1-will-https-protect-you]] — Q&A follow-ups on UUID keys and inverted-index compression
9. [[qa-and-plans-for-2024]] — live whiteboard of composite and covering indexes and selectivity
10. [[qa-2-answering-questions]] — real-world algorithms: complexity analysis in review, the topological-sort stack war story

## Tools

- [[mysql]] — the default lab bench: clustered indexes, FULLTEXT, Handler Socket, all the benchmarks
- [[postgresql]] — the architectural counterpoint: heap tables, ctid pointers, MVCC index rebuilds
- [[elasticsearch]] — the packaged inverted index; its tokenizer zoo as a menu of indexing strategies
- [[mongodb]] — stored his 300 TB production inverted index; also the "web scale" hype punchline
- [[redis]] — the caching baseline a Bloom filter beats by ~100x
- [[memcached]] — Redis's benchmark twin; oddly slowest to populate

## Related clusters & concepts

[[deep-learning-of-fundamentals]] — this cluster is the channel's proof that internals knowledge pays; [[hashing]] — underlies both hash indexes and Bloom filters; [[base64]] — the serialization overhead in the index-compression story; [[web-performance]] — where slow queries end up hurting.
