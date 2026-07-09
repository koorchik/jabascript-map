---
type: video
title_uk: "Навайбкодив мобільний додаток за два вечори"
youtube_id: 3J8VA4Y3Ba4
tags: [vibe-coding, ai, flutter, shorts]
date_ingested: 2026-07-09
---
# I Vibe-coded a Mobile App in Two Evenings (short)

> Original: "Навайбкодив мобільний додаток за два вечори" — https://youtu.be/3J8VA4Y3Ba4

Short demo of a real itch-scratching app the author vibe-coded in two evenings. His Blackmagic Micro Studio Camera has no screen, barely any interface and no dedicated Blackmagic app — but it does have a REST API over the network (via a USB-C-to-Ethernet adapter). So he built a [[flutter|Flutter]] controller app that runs on Linux, Android "and whatever you want": it scans for the camera (or takes an IP), and since Blackmagic has no continuous autofocus, he added tap-to-focus — tap a point on the monitor feed and the camera refocuses there. The app exposes essentially the full camera feature set: audio and media controls, recording, a monitor view, false color, zebra, various frame guides, and color grading controls — and the same UI works both on a big screen and squeezed down to phone format on Android. "What I liked is that I vibe-coded this" — a working, genuinely useful multi-platform app for hardware nobody wrote an app for.

## Key takeaways
- A concrete, non-toy [[vibe-coding]] success story: a full-featured camera control app for niche hardware, built in two evenings with an [[ai-coding-agents|AI coding agent]] rather than weeks of manual work.
- The gap it fills is real: Blackmagic ships a REST API but no app for this camera — vibe-coding makes "write your own vendor app" economically sane.
- Flutter's cross-platform story is the enabler: one codebase running on desktop Linux and Android, with responsive layout from tablet/monitor size down to phone.
- Tap-to-focus on the video feed compensates for the camera's missing continuous autofocus — the app doesn't just mirror the API, it adds workflow features the hardware lacks.

## Covered
[[vibe-coding]], [[ai-coding-agents]], [[flutter]]
