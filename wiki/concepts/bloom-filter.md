---
type: concept
tags: [data-structures, probabilistic, performance, security]
---
# Bloom filter

"A genius data structure": a probabilistic set membership test with no false negatives ever and a tunable false-positive rate — its size depends only on element count and target FPR, not on key size. Viktor hand-implements one in JavaScript and benchmarks it against everything: 10M keys fit in an 11 MB filter at 1% FPR and answer 100,000 lookups in ~55 ms, versus ~800 MB for a JS Map, ~17 s per 100k for indexed [[mysql]], and ~6 s per 100k for [[redis]]/[[memcached]]. The tuning math is dramatic: doubling the filter's size buys 100x accuracy, while undersizing by half degrades 1% FPR to ~15%. His analogy for collisions: a club bouncer who remembers visitors only by their clothes — he'll never miss someone he's seen, but two people in the same jacket look identical ([[bloom-filter-and-firefox]]).

The climax is Firefox's CRLite: a cascade of ~13 Bloom filter levels, each holding the previous level's false positives, which turns the probabilistic filter into a deterministic binary classifier — shipping all ~4M revoked TLS certificates to every browser in ~300 KB of daily updates, in production since 2025 (and no npm library exists for the cascade variant). Real-world deployments he cites: Silpo's 25M-client CRM using one for 0.1 ms vs 50 ms lookups at 1000 RPS, Cassandra, Google Safe Browsing lists, RTB ad systems, and premium-user classification. Teased sequels: Counting Bloom Filter, Count-Min Sketch, HyperLogLog ([[bloom-filter-and-firefox]]).

## Covered in
- [[bloom-filter-and-firefox]] — the definitive video: hand-built in JS, the full benchmark ladder against Map/MySQL/Redis/Memcached, sizing math, the CRLite cascade, and production deployments

## Related
[[data-structures]] — its home among probabilistic structures
[[hashing]] — the k hash functions that drive it
[[algorithmic-complexity]] — the benchmark ladder is an exercise in orders of magnitude
[[database-indexes]] — what it outruns by living in process memory
[[https-tls]] — the revoked-certificate problem CRLite solves
