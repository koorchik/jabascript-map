---
type: tool
tags: [infrastructure-as-code, devops, cloud]
---
# Terraform

Terraform is the standard infrastructure-as-code tool. Its channel appearance is tied to a specific I/O 2023 announcement ([[google-io-2023-watch-party]]): Firebase resources became Terraform-describable, meaning infra-as-code finally covers Firebase. The watch-party discussion goes practical from there — the relationship between Firebase's JSON config and HCL, generating dynamic resources from parsed JSON, and the observation that in this role Terraform acts as a thin wrapper over Firebase-level configuration rather than a deep abstraction.

## Covered in
- [[google-io-2023-watch-party]] — Firebase goes Terraform-describable; JSON-config vs HCL, dynamic resources from parsed JSON, Terraform as a thin wrapper.

## Related
[[firebase]] — the platform the new Terraform coverage targets.
[[google-cloud-run]] — the neighboring Google Cloud piece in the same stack.
