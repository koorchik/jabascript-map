---
type: concept
tags: [security, cryptography, integrity]
---
# Digital signatures

The second superpower of [[asymmetric-encryption]], as the channel presents it: encrypting a document's hash with your *private* key **is** the signature. Anyone can verify it with your public key, which gives authenticity (it was you), integrity (nothing changed — a changed document changes the checksum), and non-forgeability, since nobody else holds the private key ([[asymmetric-encryption-digital-signatures]]). A practical detail he insists on: in reality you never sign the whole document, you sign its checksum/hash. He also covers the symmetric counterpart — HMAC-based MACs — where signer and verifier share one secret.

Signatures are the channel's answer to its favorite trick question: is a JWT encrypted? No — it's *signed* (symmetrically or asymmetrically), which proves integrity but hides nothing; the frontend can read every byte of the payload ([[hashing-encoding-encryption-difference]]). Understanding what a signature actually is — versus encryption — is presented in [[3-things-that-make-a-programmer-better]] as the marker of deep versus shallow knowledge.

## Covered in
- [[asymmetric-encryption-digital-signatures]] — the mechanics: private key signs the hash, public key verifies; authenticity + integrity + non-forgeability; HMAC for the symmetric case
- [[hashing-encoding-encryption-difference]] — the second capability unlocked by asymmetric crypto; the JWT trick-question answer hinges on it
- [[3-things-that-make-a-programmer-better]] — JWT is a signature, not encryption; knowing the difference is what lets you use it correctly

## Related
[[asymmetric-encryption]] — the key pair that makes signatures possible.
[[hashing]] — what actually gets signed.
[[jwt]] — the canonical everyday signed (not encrypted) artifact.
[[encryption]] — the constantly-confused sibling: encryption hides, signatures prove.
[[cold-crypto-wallets]] — signing a transaction offline is the whole trick.
[[security-practices]] — supply-chain image/package signing (with the caveat that a signature only proves whose key signed it).
