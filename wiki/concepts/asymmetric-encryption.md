---
type: concept
tags: [security, cryptography, encryption]
---
# Asymmetric encryption

The channel's "one key-pair concept that explains half of modern security": a public/private key pair where — unlike symmetric crypto's single shared secret — you never need to share the private key with anyone. In the dedicated video ([[asymmetric-encryption-digital-signatures]]) Viktor shows with runnable Node.js `crypto` demos how this single idea underlies HTTPS, SSH keys, PGP, JWT signing, blockchain wallets and even Google Authenticator. He's precise about the algebra: in RSA the two keys are interchangeable by their mathematical properties, while on elliptic curves the public and private roles are fixed — EC gives you Diffie-Hellman key exchange and signatures, but no RSA-style direct encryption.

A key practical point he stresses: asymmetric crypto is roughly 100-1000x slower than symmetric, so real systems use it only to exchange a symmetric key, then switch to AES/ChaCha20 for the actual data — that's how TLS works. And the standing warning, via a Bruce Schneier quote: never roll your own crypto. In [[3-things-that-make-a-programmer-better]] he argues that even ABC-level understanding of public/private keys is exactly what inoculates developers against the classic JWT-is-encrypted and Basic-Auth-is-safe misconceptions.

## Covered in
- [[asymmetric-encryption-digital-signatures]] — the core video: key pairs, RSA vs elliptic curves, why asymmetric only bootstraps a symmetric key, Node.js demos, Schneier's warning
- [[hashing-encoding-encryption-difference]] — introduced as the two-key variant (RSA, elliptic curves) that works in both directions — which is exactly what makes digital signatures possible
- [[3-things-that-make-a-programmer-better]] — ABC-level key-pair understanding as the antidote to JWT/Basic-Auth misconceptions

## Related
[[encryption]] — the symmetric half of the picture (one shared key, fast).
[[digital-signatures]] — the second capability the key pair unlocks.
[[ssh-key-authentication]], [[jwt]], [[https-tls]], [[cold-crypto-wallets]] — the applications the channel derives from this one concept.
[[hashing]] — signatures are computed over a hash of the document.
