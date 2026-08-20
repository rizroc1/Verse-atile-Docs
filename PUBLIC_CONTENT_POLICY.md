# PUBLIC CONTENT POLICY

This repository is intentionally **PUBLIC** and contains documentation only.

## Never publish here

- Files copied from the private Verse-atile production repository.
- Private C/C++ implementation source.
- Unreal `.uasset`, `.umap`, `.uproject`, `.uplugin`, packaged builds, DLLs, PDBs, or binaries.
- Private receipts, internal evidence logs, machine inventories, or sensitive local paths.
- API keys, OAuth tokens, passwords, certificates, secrets, or `.env` files.
- Private user/customer data.
- Unreleased proprietary artwork/assets.
- Security-sensitive private implementation details.

## Allowed public material

- User documentation.
- Tutorials and examples written specifically for public release.
- Public compatibility matrices.
- Public release notes/changelogs.
- Public roadmap summaries explicitly approved for release.
- Beginner guides and preset documentation.
- Public privacy/security explanations.
- Approved third-party credits and license notices.
- Rights-truthful Special Thanks entries backed by evidence or authorization.
- Copyright, ownership, privacy, security, and public terms/disclaimer pages.
- Community links and feedback instructions.

## Protected private production repository

The public-docs build must never crawl, copy, sync, mirror, or auto-publish from the private Verse-atile production checkout.

Any future automation importing documentation must use an explicit allowlist of public-ready files and must pass the public-safety gate before deployment.
