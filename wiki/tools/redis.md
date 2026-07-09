---
type: tool
tags: [databases, caching, in-memory, key-value]
---
# Redis

Benchmarked on the channel as the standard caching answer — "practically an in-memory database" — in the 10M-key Bloom-filter shootout: ~6 s per 100,000 lookups, roughly 3x faster than indexed [[mysql]]'s ~17 s. But the point of the video is that it still loses by ~100x to an 11 MB in-process [[bloom-filter]] (~55 ms per 100k), while carrying far more memory and infrastructure weight ([[bloom-filter-and-firefox]]). The takeaway isn't "Redis is slow" — it's that network-hop key-value stores are unnecessary when a probabilistic filter fits in process memory and no false negatives are acceptable losses.

## Covered in
- [[bloom-filter-and-firefox]] — the caching baseline in the benchmark ladder: full scan → index → Redis/Memcached → Bloom filter

## Related
[[bloom-filter]], [[memcached]], [[algorithmic-complexity]], [[database-indexes]]
