# Diyse Asset Library

**Status:** Authoritative visual-production asset inventory  
**Added:** 2026-08-31

This directory preserves the consolidated Diyse asset-library work created during the August 30–31, 2026 asset pass. It lives under `14_ART_AND_VISUALS/PRODUCTION` because the library supports environment construction, visual production, animation reuse, asset provenance, and future art-style conversion.

## Current authority

The current consolidated inventory is **DIYSE Asset Library Master v5**.

Repository preservation is split into exact UTF-8 parts under:

`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/archive/DIYSE_ASSET_LIBRARY_MASTER_2026-08-30_v5/`

Concatenating `part_01.txt` through `part_10.txt` in numeric order reconstructs the original master file byte-for-byte as UTF-8 text.

- Original master SHA-256: `17648aadd7ad28570b9a017a03362041875e6fa10df173315871dfcb89d57246`
- Original master character count: `175133`
- Original master version: `v5`
- Original master date: `2026-08-30`

The exact source-archive names, sizes, member counts, and SHA-256 hashes are recorded in `SOURCE_ARCHIVE_MANIFEST.md`.

## Current inventory totals

- **3,214** canonical extracted map/environment TGA records.
- **2,878** exact-unique extracted TGAs after byte-level deduplication.
- **107** represented source map families across Maps 001–116.
- Missing map numbers through 116: **015, 033, 042, 085, 097, 098, 099, 101, 102**.
- **94** verified-CC0 Quaternius Fantasy Props MegaKit models.
- **86** verified-CC0 Quaternius humanoid animation clips across Universal Animation Library 1 and 2.

## Provenance separation

The extracted Map001–Map116 texture material is **license-unverified extracted source material**. It must not be relabeled as CC0 or freely redistributable material. Keep it segregated from verified-open assets and treat it as private/reference/prototyping material unless rights are separately confirmed.

The Quaternius Fantasy Props MegaKit and both Universal Animation Libraries are verified **CC0 1.0 Universal / Public Domain Dedication** and may be modified and used directly.

## Public-repository safety lock

`zxxdjxxz-del/Diyse-Game` is currently a **public repository**. Therefore the license-unverified Map001–Map116 source ZIPs and directly extracted source textures must **not** be committed to this repository, including through Git LFS, unless rights are separately confirmed or repository/storage visibility is explicitly changed.

Repository safeguards now enforce this split:

- `asset_sources/private_reference/` is ignored by `.gitignore`;
- `assets/environment/extracted_private_reference/` is ignored by `.gitignore`;
- `asset_sources/.gdignore` prevents archival source packages from being scanned/imported by Godot;
- verified redistributable ZIPs under `asset_sources/third_party_cc0/` are routed through Git LFS by `.gitattributes`.

The source-storage routing and local staging rules are documented in `../../../..//../asset_sources/README.md` conceptually; from the repository root the canonical path is simply:

`asset_sources/README.md`

## Archive verification

Before any source ZIP is accepted into private storage, Git LFS, or another archival destination, verify it against `SOURCE_ARCHIVE_MANIFEST.md`.

Repository verifier:

`python tools/verify_asset_archives.py`

The verifier checks:

- expected byte size;
- ZIP file-member count, excluding directory entries;
- SHA-256;
- duplicate copies of an expected archive in the configured roots.

Use `--present-only` to validate a partial staging set without failing for archives that have not yet been copied into that storage location.

## Project-use rule

These extracted map textures are a **parts/reference library for building original Diyse maps**, not a target for reconstructing source maps. Diyse layouts, collision, traversal, encounter placement, treasure placement, camera design, landmarks, faction identity, and final environment composition remain original project work.

## Relationship to current visual canon

This inventory records **available source material and production capability**. It does not override `ART_VISUAL_MASTER.md`, the environment visual-language documents, approved character visual authorities, or newer explicit visual decisions. Source assets must be adapted or replaced as needed to match the current Diyse HD-2D anime direction.

## Raw binary storage

The authoritative source ZIP set represented by the manifest is approximately **2.25 GB**.

Current storage policy:

- **public `Diyse-Game` repository:** authoritative inventory, provenance, hashes, verification tooling, and optionally verified-redistributable CC0 source archives through Git LFS;
- **private storage:** license-unverified extracted Map001–Map116 source archives and directly derived extracted-source material;
- **acceptance rule:** a binary copy becomes authoritative only after its size/member-count/SHA-256 verification passes against `SOURCE_ARCHIVE_MANIFEST.md`.

Do not treat a public-repository omission of the extracted binaries as loss of authority: the manifest and exact v5 inventory remain the authority records. The remaining preservation requirement is maintaining at least one verified private binary copy of the license-unverified source set.
