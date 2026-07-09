---
type: cluster
tags: [security, cryptography, moc]
---
# Security & Cryptography

Security is the channel's home turf: Viktor started his career in infosec, later enrolled in a cybersecurity PhD, and states the thesis directly in [[qa-and-plans-for-2024]] — "almost all of information security is understanding how things work inside." Accordingly, the channel almost never teaches security as a checklist. It teaches internals — how DHCP hands out settings, what a JWT is made of, what a key pair can and cannot do — and lets the security conclusions fall out, sharpened by trick questions ("is a JWT encrypted?"), live attacks (a rogue DHCP server built at a café table), and WebbyLab war stories (an admin key that renamed a client to "Raul"). The deliberate centerpiece is the [[encoding]] / [[encryption]] / [[hashing]] trio, taught as a set precisely because confusing them is the root of most developer security mistakes.

## Core concepts

### The confused trio
- [[encoding]] — representation, not secrecy; anyone can reverse it
- [[encryption]] — no key, no understanding; symmetric vs asymmetric
- [[hashing]] — one-way, fixed output; his three families: checksums, password hashing, hash-table hashes
- [[base64]] — the canonical encoding, decoded live in JWTs, Basic Auth and data URIs

### Cryptography in practice
- [[asymmetric-encryption]] — the one key-pair concept behind HTTPS, SSH, PGP, JWT and blockchain
- [[digital-signatures]] — private key signs a hash; anyone verifies; integrity without secrecy
- [[jwt]] — signed, not encrypted; stateless sessions; asymmetric signing for microservices
- [[ssh-key-authentication]] — challenge-response with the key pair; never send the private key
- [[one-time-passwords]] — TOTP demystified: HMAC over a shared secret and the clock
- [[cold-crypto-wallets]] — sign offline, broadcast online; the signature is safe to expose
- [[https-tls]] — what TLS protects, and what it doesn't on a hostile network

### Defense and the human factor
- [[security-practices]] — the hub: hash passwords, never roll your own crypto, treat Base64 as plaintext, supply-chain defenses
- [[least-privilege]] — scope credentials to the task; the admin-key "Raul" incident
- [[social-engineering]] — manufactured trust, dissected on a real scam call
- [[sandboxing-and-isolation]] — contain untrusted VMs/code so compromise has zero blast radius

### Neighboring concepts
- [[dhcp]] and [[dns]] — the protocols behind the café-Wi-Fi attack
- [[nat-and-networking]] — subnets and routing that isolation is built from
- [[bloom-filter]] — Firefox's CRLite: probabilistic structures checking revoked certificates
- [[deep-learning-of-fundamentals]] — why studying security is the best vehicle for learning internals

## Videos

- [[hashing-encoding-encryption-difference]] — the trio untangled via trick questions: JWTs are signed, DB passwords are hashed, Basic Auth is plaintext
- [[asymmetric-encryption-digital-signatures]] — one key-pair concept explains HTTPS, SSH, PGP, JWT, wallets and Authenticator, with runnable Node.js demos
- [[how-base64-works]] — Base64 from first principles, live-decoded in JWTs, Basic Auth headers and data URIs
- [[qa-1-will-https-protect-you]] — HTTPS won't save you on a hostile network; plus Base64, JWT and UUID follow-ups
- [[dhcp-cafe-wifi]] — the café-Wi-Fi rogue-DHCP attack, built live with dnsmasq and Wireshark
- [[vm-network-isolation]] — sandboxing a VM behind a pfSense virtual router so it can't roam the home LAN
- [[voice-1-admin-keys-for-developers]] — why developers shouldn't get admin keys: the deleted co-founder and client "Raul"
- [[voice-4-phone-scammers]] — a real scam call recorded and dissected until the script collapses
- [[bloom-filter-and-firefox]] — Bloom filters and Firefox's CRLite cascade for revoked-certificate checking
- [[google-io-2023-watch-party]] — supply-chain security: reproducible builds, image signing, Assured OSS, npm provenance
- [[3-things-that-make-a-programmer-better]] — security study as the best route to deep understanding; the Base64 war story
- [[qa-and-plans-for-2024]] — the infosec origin story and the "understanding internals" thesis

## Tools seen in this cluster

- [[pfsense]] — the virtual router doing the isolating
- [[virtualbox]] — where the sandboxed VMs live
- [[dnsmasq]] — the rogue DHCP/DNS server in the café attack
- [[nodejs]] — the `crypto` module powering the encryption/signature demos
- [[firefox]] — home of the CRLite certificate-revocation cascade

## Related clusters

The networking side of these attacks lives in the networking cluster ([[dns]], [[dhcp]], [[https-tls]], [[nat-and-networking]]); the craft argument for learning security deeply lives with [[deep-learning-of-fundamentals]] and [[domain-knowledge]].
