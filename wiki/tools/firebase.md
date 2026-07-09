---
type: tool
tags: [cloud, backend-as-a-service, google]
---
# Firebase

Firebase is Google's backend-less application platform, covered on the channel through the I/O 2023 watch party where co-host Mykyta Galkin gives a guided tour ([[google-io-2023-watch-party]]). The framing: Firebase sits on top of Google Cloud with one billing account and a shared project, so it composes with the rest of the stack rather than living in its own silo. Highlights from the tour: Hosting preview channels per pull request; Hosting rewrites that route `/api` paths straight to Cloud Run services (getting you a free custom domain and certificates for containers); Firestore's two modes and realtime sync; the Extensions marketplace (Stripe payments, email and the like); and the reveal that Cloud Functions are now built on Cloud Run containers underneath.

## Covered in
- [[google-io-2023-watch-party]] — the full tour: preview channels, rewrites to Cloud Run, Firestore modes, Extensions marketplace, Functions-on-Cloud-Run.

## Related
[[google-cloud-run]] — the container platform Firebase Hosting routes to and Functions run on.
[[terraform]] — I/O 2023 made Firebase resources Terraform-describable.
