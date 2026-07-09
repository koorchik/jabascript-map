---
type: concept
tags: [web, gpu, browser, machine-learning]
---
# WebGPU

The channel calls WebGPU the quiet killer feature of the Google I/O showcase ([[google-io-2023-watch-party]]). WebGL descends from cut-down 90s OpenGL, and doing machine learning in the browser used to mean *abusing* shaders — encoding your data as pixel colors and praying anti-aliasing didn't corrupt a value along the way. WebGPU instead exposes direct GPU compute, which he cites as roughly a 3x speedup for TensorFlow.js-style workloads like background removal — and jokes that it's also "one more way to mine Bitcoin in visitors' browsers."

## Covered in
- [[google-io-2023-watch-party]] — WebGPU vs the shader-abuse era of browser ML, ~3x for TensorFlow.js, the Bitcoin-mining quip

## Related
[[web-performance]] — the other browser-capability thread from the same I/O stream
[[deep-learning-of-fundamentals]] — GPU compute as an enabler for in-browser ML
