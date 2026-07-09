---
type: video
title_uk: "Що захищає твої дані й гроші від хакерів？ Асиметричне шифрування та цифровий підпис"
youtube_id: rbDsf9DGrqg
tags: [security, cryptography, asymmetric-encryption, digital-signatures, ssh, jwt, nodejs]
date_ingested: 2026-07-09
---
# What Protects Your Data and Money from Hackers? Asymmetric Encryption and Digital Signatures

> Original: "Що захищає твої дані й гроші від хакерів？ Асиметричне шифрування та цифровий підпис" — https://youtu.be/rbDsf9DGrqg

The author's thesis: one pair of concepts — [[asymmetric-encryption]] and [[digital-signatures]] — explains how HTTPS, SSH key login, ProtonMail/PGP, Ukraine's Diia signature ("дієпідпис") and banking signatures, cold blockchain wallets, JWT, and Google Authenticator all work. He explicitly disclaims being a cryptographer and quotes Bruce Schneier — anyone can design a cipher *they themselves* can't break — so never roll your own crypto; understand the concepts and use standard libraries. He walks the whiteboard logic (symmetric = one shared secret; asymmetric = public/private pair where sharing the private key is never needed), shows why encrypting with the private key is pointless for secrecy but is exactly the mechanism of a signature (in practice you sign a hash/checksum of the document, not the document itself), demos real SSH key authentication against a fresh DigitalOcean server (`ssh -v`, `authorized_keys`, the server's random-string challenge), and finishes with runnable Node.js `crypto` examples on GitHub: RSA sign/verify and encrypt/decrypt, elliptic-curve signatures, and AES-256-CBC with an initialization vector — illustrated with the famous ECB-encrypted penguin picture.

## Key takeaways
- In RSA the two keys are interchangeable by properties, but encrypting with the *private* key gives no confidentiality (everyone holds the public key) — that "useless" direction is precisely what a [[digital-signatures|digital signature]] exploits: encrypt a [[hashing|hash]] of the document with the private key, and anyone can verify authenticity and integrity with the public key.
- Asymmetric ciphers are ~100–1000x slower than symmetric ones, so HTTPS, PGP etc. encrypt the actual data symmetrically and use the key pair only to establish the symmetric key; modern [[https-tls|HTTPS]] switched from RSA key exchange to Diffie-Hellman for Perfect Forward Secrecy, and elliptic curves (no RSA-style encryption, DH + signatures only) give the same security with shorter keys.
- The "elephant in the room" he flags for a future HTTPS video: distributing the public key itself. A man-in-the-middle who swaps in his own public key defeats everything — which is why certificates, certificate authorities, and the CA hierarchy exist.
- [[jwt|JWT]] signatures can be symmetric (HMAC with a shared secret — verifier and issuer are the same party) or asymmetric — his microservices example: sign with the private key so any other service can verify tokens holding only the public key, never the secret.
- Google Authenticator (TOTP) is just HMAC over a shared secret plus the current Unix-time interval (e.g. 30-second windows) — which is why a phone with a wrong clock generates invalid one-time codes.
- Cold crypto wallets: the private key lives on an offline machine; you sign the transaction file there, carry it on a flash drive to an online machine, and push it to the blockchain — the signed transaction is safe to expose, and a Bitcoin address is essentially a hash of the public key.
- War story from the SSH demo: he has repeatedly asked developers "send me your key so I'll add you to the server" and received the *private* key. Never share the private key — it is equivalent to the password.
- Randomness is part of security: `Math.random()` in JavaScript makes crypto vulnerable (use `crypto.getRandomValues`); he recalls a Windows update that shipped the NIST-blessed random generator widely considered an NSA backdoor — the outcry got it replaced in the next update.

## Covered
[[asymmetric-encryption]], [[digital-signatures]], [[encryption]], [[hashing]], [[https-tls]], [[jwt]], [[ssh-key-authentication]], [[one-time-passwords]], [[cold-crypto-wallets]], [[security-practices]], [[nodejs]]
