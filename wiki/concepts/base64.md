---
type: concept
tags: [encoding, data-representation, web]
---
# Base64

The channel's canonical example of [[encoding]] — and of what encoding is *not* (protection). The definitive video ([[how-base64-works]]) derives it from first principles: born from text-only email needing binary attachments, it maps data onto 64 universally-safe characters (A-Z, a-z, 0-9, +, /), 6 bits per character, so 3 bytes become 4 chars — a +33% size tax. He tours the family: **base64url** as used in JWTs (+ and / swapped for - and _, = padding, making "." safe as a separator), **Base32** (case-insensitive and slash-free — good for filenames; drops 0/1 as lookalikes of O/l; +60%), and **Base16 = hex** (CSS `#FFFFFF`, 2x size). Neat demo: a UUID's 32 hex characters decode to 16 raw bytes — half the storage.

Then he live-decodes Base64 in three real places: [[jwt|JWT]] tokens (header and payload readable by anyone), HTTP Basic Auth headers (the `Authorization: Basic` value decodes to `login:password` with the browser's own `atob`), and images inlined as data URIs. That Basic Auth demo powers two of his trick questions in [[hashing-encoding-encryption-difference]] — Base64'd credentials and JWT payloads are "the same as plaintext" — and the war story in [[3-things-that-make-a-programmer-better]] about an engineer claiming Basic Auth was "encrypted because it's Base64." In [[qa-1-will-https-protect-you]] he justifies when the +33% is worth paying: any binary inside a text format — HTTP header values (no newlines allowed), logs you can open in a text editor, JSON/XML payloads, CSV without escaping, SMTP attachments, SSH PEM key files. The full-text-search series shows the trade-off live: postings are base64-wrapped to survive a line-oriented text file ([[full-text-search-inverted-indexes]]), then part 2 restructures the index into two files precisely to drop the +33% penalty ([[full-text-search-part-2-qa]]).

## Covered in
- [[how-base64-works]] — the definitive treatment: 6 bits per char, +33%, base64url/Base32/Base16, and live decoding of JWTs, Basic Auth and data URIs
- [[hashing-encoding-encryption-difference]] — the canonical encoding example; punchline of the JWT and Basic Auth trick questions: "same as plaintext"
- [[qa-1-will-https-protect-you]] — when +33% is justified: binary inside text formats, from HTTP headers to PEM keys
- [[full-text-search-inverted-indexes]] — applied: base64-wrapping binary varbyte postings to stay safe in a line-oriented file, still a net win
- [[full-text-search-part-2-qa]] — the two-file index split exists precisely to shed base64's +33% once nothing parses line-by-line
- [[3-things-that-make-a-programmer-better]] — the "Basic Auth is encrypted because it's Base64" war story

## Related
[[encoding]] — the concept Base64 exemplifies; never confuse with [[encryption]].
[[jwt]] — base64url in every token you've ever pasted into a debugger.
[[hashing]] — the third leg of the encoding/encryption/hashing trio.
[[index-compression]], [[inverted-index]] — where the +33% overhead becomes a measurable engineering trade-off.
