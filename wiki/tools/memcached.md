---
type: tool
tags: [databases, caching, in-memory, key-value]
---
# Memcached

Benchmarked alongside [[redis]] in the Bloom-filter shootout as a distributed in-memory hash table: comparable lookup speed to Redis (~6 s per 100,000 lookups on 10M keys), though oddly the slowest of everything to populate. Both in-memory stores are shown to be unnecessary for existence checks when an 11 MB [[bloom-filter]] in process memory answers the same 100k lookups in ~55 ms ([[bloom-filter-and-firefox]]).

## Covered in
- [[bloom-filter-and-firefox]] — benchmarked as the second in-memory cache; slowest to populate, outclassed by the in-process filter

## Related
[[bloom-filter]], [[redis]], [[data-structures]]
