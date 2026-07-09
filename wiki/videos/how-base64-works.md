---
type: video
title_uk: "Як працює Base64 й навіщо він потрібен？"
youtube_id: QCL0EOKDqKY
tags: [base64, encoding, jwt, security, hands-on]
date_ingested: 2026-07-09
---
# How Base64 Works and Why You Need It

> Original: "Як працює Base64 й навіщо він потрібен？" — https://youtu.be/QCL0EOKDqKY

A hands-on follow-up to the hashing/encoding/encryption video ([[hashing-encoding-encryption-difference]]): the author demonstrates [[base64]] in three real places you meet it daily — a [[jwt]] token, an HTTP Basic Auth header, and an image inlined into HTML as a data URI — then derives the encoding from first principles on the tablet and decodes everything live in the terminal with `base64 --decode`. His framing: Base64 is simply binary data represented as text, invented so email (originally text-only) could carry attachments; from the same logic you get Base32 and Base16 (which is just hex). All examples are in a GitHub repo linked in the description, and he notes Base64 will resurface in the upcoming inverted-index videos.

## Key takeaways
- The core construction: you can't find 256 (or even 128) characters that survive every [[encoding]] and system, but 64 you can — `A–Z`, `a–z`, `0–9`, `+`, `/`. So take the binary stream 6 bits at a time: 3 bytes (24 bits) become 4 characters. Since each character is then sent as an 8-bit byte, data grows by 8/6 ≈ 33%.
- Demo 1, [[jwt]]: he generates a token and shows the client absolutely CAN read it without the secret — the header (signing algorithm metadata) and payload (`user: Viktor`) are plain Base64-decodable JSON. JWT is signed, not encrypted. It actually uses **base64url**: `+` and `/` are swapped for `-` and `_` so tokens fit in URLs, `=` is padding, and `.` is a safe separator because it's not in the alphabet.
- Demo 2, HTTP Basic Auth: the `Authorization: Basic …` header is just `login:password` in Base64 — decodable even with the browser's built-in `atob`/`btoa`. It is effectively plaintext sent with every request; "the only thing protecting me is [[https-tls|HTTPS]] — Basic Auth itself adds nothing."
- Demo 3, data URIs: an image embedded straight into HTML as `data:<mime-type>;base64,…` — he base64-encodes a frog picture and swaps it in, keeping the HTML file purely textual.
- Base32 (5 bits/char, +60% size) has a real niche: its usual alphabet is case-insensitive and slash-free, so it's safe for file and directory names even on case-insensitive filesystems; `0` and `1` are excluded because they look like `O` and `l`.
- Base16 IS hex: 4 bits per character, 2× size. You've seen it forever in CSS colors — `#FFFFFF` is bytes encoded two characters each.
- Practical payoff tying back to the [[database-indexes]] video (UUID vs auto-increment): a 32-hex-character UUID is Base16 — decode it and the same value is 16 raw bytes, half the size, which he proves with files on disk.

## Covered
[[base64]], [[encoding]], [[jwt]], [[https-tls]], [[security-practices]], [[database-indexes]]
