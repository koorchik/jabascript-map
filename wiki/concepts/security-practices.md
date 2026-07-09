---
type: concept
tags: [security, infosec, best-practices]
---
# Security practices

The channel's security thesis, stated outright in [[qa-and-plans-for-2024]]: "almost all of information security is understanding how things work inside." Viktor (who started in infosec before Mail.ua, WebbyLab and Google, and later enrolled in a cybersecurity PhD) treats security not as a checklist but as a consequence of knowing internals — if you know how a protocol or mechanism really works, you know its properties and how to break them. That is why his protocol deep-dives are deliberately framed as security stories: the DHCP video is really a café-Wi-Fi man-in-the-middle lesson, and the Base64/hashing/encryption trio exists to demolish false beliefs like "Basic Auth is encrypted because it's Base64." In [[3-things-that-make-a-programmer-better]] he even recommends studying security (injections, XSS/CSRF, buffer overflows, Heartbleed, Shellshock) as the best vehicle for deep learning in general.

Concrete rulings that recur across videos: treat [[base64|Base64]] as plaintext, never as protection; store passwords hashed with scrypt/bcrypt, never encrypted, so even an attacker with the full database and configs can't recover them ([[hashing-encoding-encryption-difference]]); never roll your own crypto (he quotes Schneier), never share private keys, and use `crypto.getRandomValues` instead of `Math.random` — he recalls the NIST/Windows RNG backdoor incident as proof that weak randomness collapses everything ([[asymmetric-encryption-digital-signatures]]). On networks: [[https-tls|HTTPS]] alone won't save you on a hostile network — on plain HTTP an attacker can swap a downloaded file for malware on the fly, and a VPN tunnel is the general defense ([[qa-1-will-https-protect-you]]). The human side gets war stories too: an admin API key plus copy-pasted example code deleted a co-founder's account ([[voice-1-admin-keys-for-developers]] → [[least-privilege]]), and real bank-scam calls are dissected in [[voice-4-phone-scammers]] ([[social-engineering]]).

## Covered in
- [[qa-and-plans-for-2024]] — the manifesto: infosec is understanding internals; the DHCP video was deliberately a security story; promises an infosec learning-resources overview (CTFs, certifications)
- [[dhcp-cafe-wifi]] — practical man-in-the-middle lesson: untrusted café Wi-Fi lets anyone at the next table hand you malicious network settings and read unencrypted traffic
- [[vm-network-isolation]] — defense-in-depth in practice: sandboxing a potentially-compromised VM so it can't pivot into the home network
- [[how-base64-works]] — the Basic Auth demo: the `Authorization: Basic` header decodes to `login:password` with the browser's own `atob` — Base64 is never protection
- [[hashing-encoding-encryption-difference]] — practical rulings: hash passwords (scrypt/bcrypt), never encrypt them; don't mistake encoding for protection
- [[asymmetric-encryption-digital-signatures]] — never roll your own crypto, never share private keys, use real randomness; the NIST RNG-backdoor story
- [[qa-1-will-https-protect-you]] — hostile-network threat model: file-swap attacks over plain HTTP, VPN as the general defense
- [[voice-1-admin-keys-for-developers]] — war story on why credentials must be scoped to the task
- [[voice-4-phone-scammers]] — real banks never ask you to say PINs, passport data or code words aloud; recognizing the manufactured-trust pattern is the defense
- [[google-io-2023-watch-party]] — supply-chain security: reproducible builds, image signing verified at Cloud Run deploy, Google's Assured OSS, npm provenance — with the caveat that a signature only proves *someone's* key signed it
- [[3-things-that-make-a-programmer-better]] — security recommended as the best study vehicle for deep understanding
- [[code-review-how-google-does-it]] — security has its own checklist of common mistakes in WebbyLab's architectural review process

## Related
[[social-engineering]] — the human attack surface no crypto fixes.
[[least-privilege]] — scope credentials to the task.
[[encryption]], [[hashing]], [[encoding]] — the trio whose confusion causes most developer security mistakes.
[[https-tls]] — what TLS does and doesn't protect against.
[[sandboxing-and-isolation]] — containing untrusted code.
[[deep-learning-of-fundamentals]] — security as the ultimate test of whether you understand internals.
