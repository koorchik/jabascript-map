---
type: concept
tags: [security, authentication, web, tokens]
---
# JWT

The channel's favorite trick-question subject: a JWT *looks* encrypted but is just base64url-encoded and **signed** — the frontend can read the whole payload without any key ([[hashing-encoding-encryption-difference]]). In [[how-base64-works]] Viktor proves it live: header (algorithm metadata) and payload decode with a plain `base64 --decode`; only verifying the signature needs the secret. Believing JWT encrypts its payload and using it as a hidden session store is his go-to example of the shallow-knowledge trap ([[3-things-that-make-a-programmer-better]]) — the cure is understanding what a [[digital-signatures|signature]] actually is.

Used correctly, though, JWT is powerful: the token carries the whole signed session, so it's stateless and need *not* be stored in a database — that's the point ([[qa-1-will-https-protect-you]]). The signature can be symmetric (HMAC over a shared secret, where issuer = verifier) or asymmetric — and the asymmetric variant shines in microservices: the auth service signs with its private key, and every other service verifies with only the public key, so the secret never leaves the issuer ([[asymmetric-encryption-digital-signatures]]).

## Covered in
- [[hashing-encoding-encryption-difference]] — the opening trick question: JWT looks encrypted, is Base64 + signature; readable without any key
- [[how-base64-works]] — live demo: header and payload decode with plain `base64 --decode`; base64url; signed, not encrypted
- [[asymmetric-encryption-digital-signatures]] — HMAC vs asymmetric signing; the microservices pattern of verify-with-public-key-only
- [[qa-1-will-https-protect-you]] — stateless by design: the signed token carries the session, no DB storage needed; public key lets any service verify
- [[3-things-that-make-a-programmer-better]] — the shallow-knowledge trap: using JWT as a hidden session store because "it's encrypted"

## Related
[[digital-signatures]] — what a JWT actually is.
[[base64]] — how a JWT is packaged (base64url).
[[encryption]] — what a JWT is not.
[[asymmetric-encryption]] — why microservices can verify without sharing secrets.
[[microservices]] — the architecture where asymmetric JWT signing pays off.
