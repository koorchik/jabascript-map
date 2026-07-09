---
type: concept
tags: [security, cryptography]
---
# Encryption

One third of the channel's deliberately-taught trio — [[encoding]], [[encryption]], [[hashing]] — that developers constantly confuse. The defining property, per [[hashing-encoding-encryption-difference]]: without the key, others cannot understand the data. Symmetric encryption uses one key both ways (AES, ChaCha20); asymmetric uses a public/private pair. Viktor even frames encryption as technically a kind of encoding *plus* a security property — which is exactly why the distinction matters. His key message: most things developers casually call "encrypted" — JWTs, Base64 — aren't encrypted at all.

The hands-on video ([[asymmetric-encryption-digital-signatures]]) goes deep on the symmetric side: an AES-256-CBC demo with an initialization vector, the famous ECB-penguin image showing why identical input blocks producing identical output leaks the structure of the data, CBC's XOR chaining as the fix, and stream ciphers like Google's ChaCha20 explained as XOR against a long pseudo-random keystream. Because symmetric is fast and asymmetric is 100-1000x slower, real protocols encrypt data symmetrically and use [[asymmetric-encryption]] only to agree on the key.

## Covered in
- [[hashing-encoding-encryption-difference]] — the defining property (no key, no understanding), symmetric (AES, ChaCha20) vs asymmetric, and why JWTs and Base64 are not encryption
- [[asymmetric-encryption-digital-signatures]] — symmetric vs asymmetric in depth: AES-256-CBC with IV, the ECB penguin, CBC chaining, ChaCha20 as a keystream XOR
- [[3-things-that-make-a-programmer-better]] — contrasted with encoding via the Base64/Basic-Auth war story; understanding symmetric vs asymmetric leads to better decisions

## Related
[[encoding]] — representation, not secrecy; the thing encryption is most often confused with.
[[hashing]] — one-way, no key, no decryption — the third member of the trio.
[[asymmetric-encryption]] — the two-key scheme and why it only bootstraps symmetric encryption.
[[https-tls]] — encryption in transit, and its limits on a hostile network.
[[base64]] — looks scrambled, is plaintext.
