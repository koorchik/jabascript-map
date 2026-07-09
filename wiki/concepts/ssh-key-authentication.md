---
type: concept
tags: [security, authentication, ssh, cryptography]
---
# SSH key authentication

Presented on the channel as [[asymmetric-encryption]] you use every day without noticing. In [[asymmetric-encryption-digital-signatures]] Viktor does a live DigitalOcean demo: `ssh -v` shows the client offering keys one by one, the public key goes into `authorized_keys`, and the actual authentication is a challenge: the server sends a random string, the client proves possession of the private key cryptographically, and the server verifies using only the public key. No password, and nothing secret ever crosses the wire.

The war story that anchors it: when he asked developers to send him "their key" for server access, more than one sent the *private* key. His rule: never — the private key is equivalent to your password; only the public key is ever shared.

## Covered in
- [[asymmetric-encryption-digital-signatures]] — live `ssh -v` DigitalOcean demo, `authorized_keys`, the challenge-response flow, and the developers-emailing-private-keys war story

## Related
[[asymmetric-encryption]] — the mechanism underneath.
[[digital-signatures]] — proving key possession is a signature-style operation.
[[security-practices]] — never share private keys, ever.
[[remote-development]] — SSH as the transport for VS Code remote workflows.
