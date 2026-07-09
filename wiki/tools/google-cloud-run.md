---
type: tool
tags: [cloud, serverless, containers, google]
---
# Google Cloud Run

Cloud Run is Google Cloud's serverless container platform — bring any container, get scale-to-zero, metrics and CI/CD "in two clicks" — and it is literally the product Viktor's team at Google built ([[qa-2-answering-questions]]). He speaks about it as both insider and satisfied customer: he moved all his pet projects from DigitalOcean to Cloud Run and found it "much cheaper" (a couple of dollars for a small service), and reveals that Cloud Functions v2 is literally a Cloud Run container underneath ([[qa-and-plans-for-2024]]). His cost advice: don't trust the request calculator — simulate a day of real traffic and multiply by 30. At the I/O 2023 watch party, co-host Mykyta (also on the Cloud Run team) adds the pitch details: deploy-time signature verification for images, custom domains finally integrated via Firebase Hosting, and his mytalks.tech running on it ~3x cheaper than DigitalOcean ([[google-io-2023-watch-party]]). In [[qa-2-answering-questions]] Viktor announces GPU support — "serverless 2.0" — aimed at inference workloads.

Cloud Run is also the stage of his most personal Google story ([[voice-5-why-i-left-google]]): his Application Canvas project let users drag Cloud Run services and databases onto a canvas, deploy whole applications and merge architectures. It shipped first as "Cloud Run integrations," was shown at Google Cloud Next keynotes and praised by top management — then cancelled and deleted, resetting his L6 promotion track and feeding into his decision to leave Google.

## Covered in
- [[google-io-2023-watch-party]] — the team-insider pitch: any container, scale-to-zero, image signature verification, Firebase Hosting domains, mytalks.tech 3x cheaper than DigitalOcean.
- [[qa-2-answering-questions]] — "his team's product"; GPU support announced as serverless 2.0 for inference.
- [[qa-and-plans-for-2024]] — pet projects migrated from DigitalOcean, Cloud Functions v2 = Cloud Run container, traffic-simulation cost estimation.
- [[voice-5-why-i-left-google]] — the Application Canvas rise-and-cancellation story that reset his promo.

## Related
[[firebase]] — the backend-less layer that routes and hosts on top of Cloud Run.
[[docker]] — the container format Cloud Run consumes.
[[terraform]] — infra-as-code coverage of the same Google stack.
[[career-and-growth]] — the Application Canvas story as a big-company career lesson.
