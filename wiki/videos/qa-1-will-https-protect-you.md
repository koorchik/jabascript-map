---
type: video
title_uk: "Питання та відповіді №1. Чи захистить HTTPS？"
youtube_id: IMDvIyC4Oes
tags: [security, https-tls, dhcp, dns, jwt, base64, full-text-search, database-indexes, qa]
date_ingested: 2026-07-09
---
# Q&A #1: Will HTTPS Protect You?

> Original: "Питання та відповіді №1. Чи захистить HTTPS？" — https://youtu.be/IMDvIyC4Oes

The channel's first Q&A episode, answering comments left under earlier videos — mainly the popular [[dhcp|DHCP]] video plus questions on full-text search, database indexes, and Base64. The headline question: if an attacker spoofs the network but the site uses [[https-tls|HTTPS]], is there still a threat? His answer is yes, and he enumerates concrete attacks. He also cheerfully reads out and rebuts several dismissive "hater" comments (people who watched the first three minutes and declared the whole thing fake without watching the live demo), noting the DHCP video hit 70,000 views and 400+ comments that were 99% positive, so the Q&A format will continue.

## Key takeaways
- HTTPS does not save you when the attacker controls the network: (1) return the page over plain HTTP so it looks identical but you type your login or card data into a fake site; (2) redirect you to a look-alike domain (rozetka.com.ua → rozetka.com.ui) that has its own valid HTTPS and proxies your requests while harvesting card data; (3) block all traffic and tell you "the cafe internet needs this certificate — double-click to install," after which they can MITM all your HTTPS by issuing certs trusted by the cert you just installed; (4) exploit browser 0-days (he cites Spectre/Meltdown, exploitable from JavaScript to read process memory and scan for private keys).
- HSTS headers would block the HTTP-downgrade/redirect tricks, but many large sites (Rozetka included) don't set them, so the attack works in practice.
- On plain HTTP the attacker can watch all traffic and swap a file you download (a zip/xz) for a malformed or malware-carrying one on the fly. A VPN defeats all of this — the encrypted tunnel to the VPN server can't be inspected.
- DHCP starvation is trivial — a ~100-line script looping DHCP requests with random MAC addresses can exhaust 100 or 1000+ addresses; manually setting DNS to 8.8.8.8 doesn't help because the attacker can still hand you a malicious default gateway and route all traffic through himself.
- Storing UUID primary keys as `BINARY(16)` in [[mysql|MySQL]] instead of 32-char text helps but not dramatically — the 16-byte key still often exceeds half the index size (e.g. ~55% vs 70%), and binary is harder to work with (you must convert to read/display it); he'd rather keep the UUID as a separate column.
- On [[inverted-index|inverted indexes]]: the inverted index *is* the efficient data structure — you don't rewrite it into "something better," you only change the serialization format. Delta compression matters because it shrinks large IDs to small ints (enabling further compression like VByte encoding from the referenced paper), speeds reads from the filesystem, and lets a larger index fit in RAM.
- [[base64|Base64]] earns its ~33% size increase whenever binary data must ride inside a text format: HTTP headers (no newlines allowed in a value), Basic auth, logs you want to open in a text editor, JSON/XML payloads, CSV without escaping, SMTP attachments, and SSH PEM key files.
- [[jwt|JWT]] value: it carries the whole signed session (stateless) rather than a session ID, so it need NOT be stored in the DB to be invalidated-by-design; with asymmetric signing you hand the public key to anyone so any service can verify a token came from you. He notes Express rate-limiter is unrelated to sessions — it's just a rate limiter.

## Covered
[[https-tls]], [[dhcp]], [[dns]], [[nat-and-networking]], [[security-practices]], [[social-engineering]], [[jwt]], [[base64]], [[inverted-index]], [[full-text-search]], [[database-indexes]], [[mysql]]
