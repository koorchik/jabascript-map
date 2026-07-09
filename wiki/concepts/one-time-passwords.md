---
type: concept
tags: [security, authentication, 2fa, cryptography]
---
# One-time passwords (TOTP)

The channel demystifies Google Authenticator in one line: TOTP is just an HMAC over a shared secret plus the current Unix-time interval (e.g. 30-second windows). When you scan the QR code, your phone and the server end up holding the same secret; both compute the same HMAC for the current window, so the six digits match without any network round-trip ([[asymmetric-encryption-digital-signatures]]).

The corollary Viktor points out is the classic support mystery solved: if your phone's clock is wrong, your codes are computed for the wrong time window and are simply invalid. No magic, no per-code server push — just a keyed hash and a synchronized clock.

## Covered in
- [[asymmetric-encryption-digital-signatures]] — TOTP = HMAC(shared secret, Unix-time interval); phone and server hold the same secret; wrong clock means wrong codes

## Related
[[hashing]] — HMAC is a keyed hash construction.
[[digital-signatures]] — HMAC is the symmetric cousin of signing.
[[security-practices]] — 2FA as a standard defense layer.
