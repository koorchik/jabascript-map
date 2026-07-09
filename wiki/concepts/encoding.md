---
type: concept
tags: [security, data-representation, fundamentals]
---
# Encoding

Representation, not secrecy — the most misunderstood member of the channel's deliberately-taught trio of [[encoding]], [[encryption]] and [[hashing]]. Per [[hashing-encoding-encryption-difference]], encoding is just representing data in another form for some task: Base64 turns binary into text (the same idea yields Base32 and Base85), and even zip compression is an encoding. There is no key and no secret — anyone can reverse it. Viktor's sharpest framing: encryption is technically a *kind* of encoding that adds a security property; plain encoding adds none.

The practical companion video [[how-base64-works]] shows *why* encodings exist: you can't just ship raw bytes as "text" — control characters and encoding-specific alphabets break things — hence a lowest-common-denominator 64-character alphabet. The stakes of confusing encoding with encryption are illustrated by his favorite war story in [[3-things-that-make-a-programmer-better]]: an engineer who claimed HTTP Basic Auth was "encrypted because it's Base64." Knowing this distinction is, in his words, the ABC-level knowledge that reveals a mechanism's real security properties.

## Covered in
- [[hashing-encoding-encryption-difference]] — the definition: another representation for a task (Base64/Base32/Base85, even zip); encryption framed as encoding plus a security property
- [[how-base64-works]] — why raw bytes can't travel as text, and how the 64-char lowest-common-denominator alphabet solves it
- [[3-things-that-make-a-programmer-better]] — the encoding-vs-encryption distinction as ABC-level knowledge that exposes real security properties

## Related
[[base64]] — the canonical encoding, dissected bit by bit.
[[encryption]] — encoding plus a key; the thing encoding is not.
[[hashing]] — the third of the trio: not reversible at all.
[[security-practices]] — "it's encoded" never means "it's protected."
