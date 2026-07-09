---
type: tool
tags: [mobile, cross-platform, ui, vibe-coding]
---
# Flutter

Flutter is Google's cross-platform UI toolkit, and on the channel it is the proof that vibe-coding is past the toy stage: Viktor vibe-coded a full-featured controller app for his screen-less Blackmagic camera against its REST API in two evenings ([[vibe-coded-mobile-app]]) — one codebase running on Linux, Android "and whatever you want", responsive from a big monitor down to a phone, with tap-to-focus added to compensate for the camera's missing continuous autofocus. Demoing the same app in [[vibe-coding-new-project]], he shows builds for Linux, Windows and web (GitHub Pages), notes that web/debug builds were "super slow" until Claude optimized local state while native builds fly, and defends keeping the default Flutter design: component structure and UX first, styling later.

His verdict in the Flutter-vs-React-Native debate ([[vibe-coding-part-2]]) is balanced: RN is more mature, uses native UI components and is easier for React devs, but Flutter compiles natively, covers iOS/web/desktop from one codebase, and beats QT/GTK for Linux desktop apps. He is skeptical of the quoted "42% market share" stat, and plans to try Flutter's testing story (Storybook-style, golden and unit tests all exist).

## Covered in
- [[vibe-coded-mobile-app]] — the two-evening Blackmagic camera app: one responsive codebase across platforms, tap-to-focus on the video feed.
- [[vibe-coding-new-project]] — the same app demoed: multi-platform builds, slow web/debug vs fast native, default design kept deliberately.
- [[vibe-coding-part-2]] — Flutter vs React Native trade-offs, Linux desktop advantage, testing plans.

## Related
[[vibe-coding]] — the workflow that made a vendor-replacement app a weekend project.
[[claude-code]] — the agent that wrote and optimized the Flutter code.
[[declarative-ui]] — Flutter's widget model as declarative UI in practice.
