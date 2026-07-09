---
type: tool
tags: [networking, web-server, tooling]
---
# nginx

Web server. On the channel it plays a supporting role in the latency episode: he stood up a bare nginx server in Los Angeles serving both HTTP and HTTPS as the real-world test target, with ping confirming a ~192ms round-trip — the concrete endpoint used to measure how TCP and TLS handshakes stack up against the speed-of-light floor ([[speed-of-light-website-latency]]).

## Covered in
- [[speed-of-light-website-latency]] — the LA HTTP/HTTPS test server used to measure real request latency

## Related
[[latency-and-speed-of-light]] — the measurements it made possible
[[https-tls]] — served the HTTPS endpoint whose handshake was timed
