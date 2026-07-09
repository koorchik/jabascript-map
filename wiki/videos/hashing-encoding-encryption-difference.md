---
type: video
title_uk: "Хешування, кодування, шифрування. В чому різниця？"
youtube_id: GQ0rDbJCKhQ
tags: [hashing, encoding, encryption, security, fundamentals]
date_ingested: 2026-07-09
---
# Hashing vs Encoding vs Encryption — What's the Difference?

> Original: "Хешування, кодування, шифрування. В чому різниця？" — https://youtu.be/GQ0rDbJCKhQ

Three concepts developers constantly confuse, untangled on the tablet as a small taxonomy tree. The author opens with trick questions: is a [[jwt|JSON Web Token]] encrypted — can the frontend read it without the key? Are passwords in your database encrypted? Is HTTP Basic Auth sending credentials in [[base64]] secure? His answers: JWT is *signed and encoded*, not encrypted; passwords are *hashed*, not encrypted; and Base64 is the same as plain text. He treats [[encryption]] as technically a form of [[encoding]] that adds a security property (unreadability without a key), while [[hashing]] stands apart as strictly one-way.

## Key takeaways
- [[hashing|Hashing]] is one-directional compression to a fixed size: feed it 1 TB or 100 TB, you still get e.g. 20 bytes out (SHA-1's size), and there is no way back — it's not archiving.
- He distinguishes three families of hash functions by purpose: checksums (MD5, SHA-1 — which git uses for integrity), cryptographic password hashing (scrypt, bcrypt — how passwords must be stored, a dedicated video promised), and fast hashes for hash tables (MurmurHash — turning keys into array indexes, see [[data-structures]]).
- [[encryption|Encryption]]'s job is that others *cannot understand* the data without a key. Two kinds: symmetric — one key both ways (AES, ChaCha20) — and [[asymmetric-encryption]] with a public/private key pair (RSA, elliptic curves), which works in both directions and therefore also enables [[digital-signatures]].
- [[encoding|Encoding]] is just representing data in a different form for a task: [[base64]] turns binary into text (and once you get it, Base32 and Base85 follow the same idea), and even zip compression is a kind of encoding.
- Answering his own openers: a JWT *looks* encrypted but isn't — it's Base64-encoded and signed (symmetrically or asymmetrically); HTTP Basic Auth in Base64 "is the same as plaintext"; and hashed DB passwords cannot be recovered even by someone holding the entire database and all the configs — that's the point ([[security-practices]]).

## Covered
[[hashing]], [[encoding]], [[encryption]], [[asymmetric-encryption]], [[digital-signatures]], [[base64]], [[jwt]], [[security-practices]]
