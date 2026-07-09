---
type: concept
tags: [distributed-systems, big-data, search, algorithms]
---
# Map-reduce

Covered not as big-data buzzword but as the practical trick that let Viktor build a 16.5M-row inverted index without holding 10–15 GB in RAM. He walks through Google's 2004 MapReduce paper, Hadoop, and Hadoop streaming, then demonstrates the streaming model with plain Unix tools: a Node.js map step emits (token, doc) pairs, Unix `sort` plays the role of the shuffle, and a reduce step groups postings per token. The same scripts are runnable on real Hadoop — he wrote his own `hadoop-streaming-utils` npm module for exactly this ([[full-text-search-inverted-indexes]]).

## Covered in
- [[full-text-search-inverted-indexes]] — the whole treatment: Google's 2004 paper, Hadoop streaming with Node.js map + Unix sort as shuffle, and his hadoop-streaming-utils module

## Related
[[inverted-index]] — the artifact the pipeline produces
[[full-text-search]] — the problem being solved
[[algorithmic-complexity]] — the memory-vs-streaming trade-off in action
