---
type: video
title_uk: "Геніальна структура даних й як її покращив Firefox"
youtube_id: WEtSsPF58Bk
tags: [data-structures, bloom-filter, hashing, benchmarks, tls, firefox]
date_ingested: 2026-07-09
---
# A Genius Data Structure — and How Firefox Improved It

> Original: "Геніальна структура даних й як її покращив Firefox" — https://youtu.be/WEtSsPF58Bk

A deep dive into the [[bloom-filter]], framed by a real war story: how browsers check revoked HTTPS certificates. The topic came out of a meetup with channel sponsors in Kyiv. Millions of certificates are issued daily (many via Let's Encrypt); if a private key is stolen the cert gets revoked, but the old OCSP online check added an extra request per site, so browsers dropped it — Chrome ships a ~600 KB daily list covering only the top ~1% of sites, leaving everyone else exposed. [[firefox]] instead ships **all ~4 million revoked certificates** in ~300 KB/day plus a 4 MB snapshot every 45 days, using **CRLite — a cascade of Bloom filters** that turns a probabilistic structure into a deterministic one (100% guaranteed answers, in production for all users since 2025, and not available as an npm library). The author benchmarks the alternatives on 10M keys (JS Map in memory, MySQL with/without index, MySQL Handler Socket, Redis, Memcached), then hand-implements a Bloom filter and the cascade in JavaScript, with all code in a public GitHub repo.

## Key takeaways
- The benchmark ladder for "is this key in the set?" over 10M keys: an in-memory JS `Map` is blazing fast but the 219 MB data file balloons to ~800 MB of process memory; MySQL without an index takes ~18 s for just 10 misses (full scan); with an index ~17 s per 100,000 queries; Redis ~6 s per 100,000; the Bloom filter does 100,000 lookups in ~55 ms **in 11 MB of RAM** — see [[database-indexes]] for the index side of this.
- A Bloom filter never gives false negatives — "if it says the key is not there, it is 100% not there" — but has a tunable false-positive rate. Its size depends only on element count and target FPR, never on key length; hash long URLs and store the fingerprint ([[hashing]]).
- The accuracy/size trade is asymmetric and beautiful: going from 1% to 0.01% FPR (100× more accurate) only grew the filter from 11 MB to 22 MB. But undersizing hurts the same way: allocate for 5M elements and insert 10M, and FPR jumps from 1% to ~15%.
- His analogy: a club bouncer who doesn't remember banned people's faces, only checkboxes of their clothing (yellow sneakers, red hat…). "Red hat never seen" → definitely allowed in; but someone wearing a banned person's hat plus another's shoes gets falsely flagged — that's a hash collision, and adding more attributes (size, brand = more bits/hash functions) shrinks the false-positive rate.
- Implementation tricks: a bit array packed into a `Uint32Array`; the fast **xxHash** — compute one 64-bit hash, split it into two 32-bit halves h1 and h2, then derive any number of hash functions as `h1 + i*h2` (a mathematically proven double-hashing scheme), so k hashes cost roughly one hash computation. Naive "sum the char codes" hashes fail because they can never reach the far end of a 10M-bit array — you need a uniform distribution.
- The Firefox cascade idea: put all 1M revoked ("bad") certs in filter #1; run all 9M good certs through it, collect the ~1% false positives into filter #2; its false positives go into filter #3… ~13 levels until only a handful of exceptions remain. Result: a deterministic binary **classifier** (`classify()` instead of `has()`), FPR exactly 0 in his benchmark, and 1M revoked-of-10M keys fit in ~1 MB. It's "like machine learning without generalization". Works whenever the full key space is enumerable.
- Practical uses he cites: checking username/email availability without hitting the database; Google Safe Browsing-style malicious-URL lists (only ~1 in 10,000 visits needs a server round-trip at 0.01% FPR); Cassandra internals; real-time bidding systems counting ad impressions at hundreds of thousands of RPS; a premium/free user classifier (10M users, 1M premium → ~1 MB structure, refreshed with small deltas like Firefox's daily 30–50 KB updates); and a fresh post from Ukrainian retailer Silpo whose 25M-client CRM uses a Bloom filter for 0.1 ms lookups instead of 50 ms — "a trifle? at 1000 RPS it decides everything".
- Teasers for the curious: Counting Bloom Filter, Count-Min Sketch, HyperLogLog (approximate set cardinality); hash-table collision attacks (an old Python vulnerability) deserve their own video; he once gave a talk on topological sort saving a JS spreadsheet, and learned many of these algorithms preparing for his Google interview.

## Covered
[[bloom-filter]], [[data-structures]], [[hashing]], [[https-tls]], [[database-indexes]], [[algorithmic-complexity]], [[firefox]], [[mysql]], [[redis]], [[memcached]]
