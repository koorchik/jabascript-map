---
type: concept
tags: [security, cryptography, blockchain]
---
# Cold crypto wallets

The channel's cleanest illustration of why [[digital-signatures]] matter: a cold wallet is simply a private key that never touches the internet. In [[asymmetric-encryption-digital-signatures]] Viktor walks the flow: the private key lives on an offline machine; you compose and *sign* the transaction file there, carry it to an online machine on a flash drive, and push it to the blockchain from there. The signed transaction is completely safe to expose — it proves authorization without revealing the key, and nobody can alter it without breaking the signature.

Bonus detail from the same video: a Bitcoin address is essentially a [[hashing|hash]] of the public key — so the whole wallet system is asymmetric keys plus hashes, nothing more exotic.

## Covered in
- [[asymmetric-encryption-digital-signatures]] — the offline-sign, flash-drive, online-broadcast flow; signed transactions are safe to expose; a Bitcoin address as a hash of the public key

## Related
[[asymmetric-encryption]] — the key pair the wallet is built on.
[[digital-signatures]] — signing offline is the entire security model.
[[hashing]] — addresses are hashes of public keys.
[[security-practices]] — the extreme form of "never expose the private key."
