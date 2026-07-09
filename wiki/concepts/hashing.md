---
type: concept
tags: [security, cryptography, data-structures, algorithms]
---
# Hashing

Strictly one-way: arbitrary input to fixed-size output — 1 TB or 100 TB in, 20 bytes out, and as Viktor quips, "it's not archiving": you cannot get the data back. The taxonomy video ([[hashing-encoding-encryption-difference]]) sorts hash functions into his three families by purpose: **checksums** (MD5, SHA-1 — git uses SHA-1), **cryptographic password hashing** (scrypt/bcrypt — how passwords are actually stored, so even an attacker with the full database and configs cannot recover them), and **hash-table hashes** (MurmurHash) built for speed and distribution rather than security. This one-way property is his answer to another trick question: database passwords aren't "encrypted," they're hashed — there is nothing to decrypt.

The channel treats hashing as a bridge concept between security and data structures. In [[why-algorithms-matter]] JS Maps/objects are revealed as hash tables with average O(1) lookup — the thing that turns an O(n·m) merge into O(n+m). In [[bloom-filter-and-firefox]] he gets into serious implementation detail: Bloom filters need fast, *uniformly distributed* hashes (a naive char-code sum can never reach the far end of a 10M-bit array), so he uses xxHash and the proven double-hashing trick — compute one 64-bit hash, split it into h1/h2, and derive k hashes as h1 + i·h2; he also recalls hash-table collision chains and an old Python hash-collision-attack vulnerability. On the crypto side, signatures are computed over a hash of the document ([[asymmetric-encryption-digital-signatures]]), and an encryption IV is likened to a password salt defeating rainbow tables.

## Covered in
- [[hashing-encoding-encryption-difference]] — the definition (one-way, fixed output) and the three-family taxonomy by purpose: checksums, password hashing, hash-table hashes; promises a dedicated password-storage video
- [[bloom-filter-and-firefox]] — hash quality in anger: uniform distribution, xxHash, the h1 + i·h2 double-hashing trick, collision chains, the Python collision-attack story
- [[why-algorithms-matter]] — JS Maps/objects are hash tables; average O(1) lookup is what collapses O(n·m) to O(n+m)
- [[asymmetric-encryption-digital-signatures]] — signatures sign a hash/checksum, not the document; changing the document changes the checksum; IV likened to a password salt

## Related
[[encoding]] and [[encryption]] — the other two thirds of the constantly-confused trio: encoding is reversible by anyone, encryption reversible with the key, hashing reversible by no one.
[[digital-signatures]] — built on top of hashes.
[[bloom-filter]] — a data structure that is nothing but hashes and bits.
[[data-structures]], [[algorithmic-complexity]] — hash tables as the O(1) workhorse.
