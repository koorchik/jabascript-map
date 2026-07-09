---
type: concept
tags: [networking, security, cryptography, https, tls]
---
# HTTPS and TLS

The channel keeps returning to a blunt thesis: HTTPS guarantees an encrypted channel and a URL-matching certificate, and *nothing more*. In the Google I/O watch party he explains why Chrome replaced the padlock with a neutral "tune" icon — the padlock "says nothing about the trustworthiness of the content," and phishing sites get the identical padlock that users misread as a trust badge ([[google-io-2023-watch-party]]). The Q&A drives it home: on an attacker-controlled network HTTPS fails in several ways — an HTTP downgrade to a fake page, a redirect to a look-alike domain with its *own* valid HTTPS proxying your requests, being tricked into installing a rogue CA cert ("café internet needs this certificate") to MITM all HTTPS, or browser 0-days like Spectre/Meltdown from JS. HSTS blocks downgrade and redirect, but big sites like Rozetka don't set it; a VPN defeats the whole class ([[qa-1-will-https-protect-you]]).

Mechanically, the latency episode shows the TLS handshake (Hello, certificate, key exchange each direction) adding ~200ms, so a real HTTPS request measured ~800ms against ~400ms for plain HTTP ([[speed-of-light-website-latency]]). The cryptography episode explains the hybrid design — a symmetric cipher for the data, asymmetric for the key exchange — and notes modern HTTPS moved from RSA key exchange to Diffie-Hellman for Perfect Forward Secrecy, flagging the still-unsolved "elephant in the room" of distributing the public key safely, which is what certificates and the CA hierarchy exist for ([[asymmetric-encryption-digital-signatures]]). The deep-learning episode uses TLS as its forgetting example: a viewer read a whole TLS book and forgot the protocol details in two months, but the *branch* remains — certificate chains, a symmetric session key, forward secrecy guaranteed only with Diffie-Hellman ([[learning-deeply-and-remembering]]).

Two more angles: certificate *revocation* is the war story behind the Bloom-filter episode — OCSP added a per-site request so browsers dropped it, cert lifetimes were shortened instead (Let's Encrypt: 3 months), Chrome ships only the top ~1% of revocations (600 KB) leaving small sites exposed, and Firefox's CRLite covers all of them ([[bloom-filter-and-firefox]]). And on Basic Auth, credentials go Base64'd (readable) with every request — "the only thing protecting me is HTTPS; Basic Auth itself adds nothing" ([[how-base64-works]]).

## Covered in
- [[qa-1-will-https-protect-you]] — the ways HTTPS fails on a hostile network; HSTS, rogue CA, VPN as the fix
- [[google-io-2023-watch-party]] — Chrome dropping the padlock; HTTPS ≠ trustworthiness
- [[speed-of-light-website-latency]] — the ~200ms TLS handshake, 800ms vs 400ms measured
- [[asymmetric-encryption-digital-signatures]] — hybrid symmetric+asymmetric, RSA→Diffie-Hellman, the CA key-distribution problem
- [[learning-deeply-and-remembering]] — TLS as the "remember the branch, not the leaves" example
- [[bloom-filter-and-firefox]] — certificate revocation, OCSP, CRLite
- [[how-base64-works]] — Basic Auth is only safe because of HTTPS

## Related
[[asymmetric-encryption-digital-signatures]] — the key-exchange machinery underneath TLS
[[encryption]] — symmetric vs asymmetric, the pieces TLS combines
[[bloom-filter]] — the structure Firefox uses for revocation
[[dns]] — spoofed DNS is caught by the certificate check
[[dhcp]] — hostile-network attacks that TLS may or may not survive
[[latency-and-speed-of-light]] — the handshake is a major latency cost
[[security-practices]] — the "will HTTPS protect you" threat model
