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

Master v5:
- **3,214** canonical extracted map/environment TGA records.
- **2,878** exact-unique extracted TGAs after byte-level deduplication.
- **107** represented source map families across Maps 001–116.
- Missing map numbers through 116: **015, 033, 042, 085, 097, 098, 099, 101, 102**.
- **94** verified-CC0 Quaternius Fantasy Props MegaKit models.
- **86** verified-CC0 Quaternius humanoid animation clips across Universal Animation Library 1 and 2.

### Supplemental user texture intake — pending provenance

A new six-archive user-supplied batch was inventoried on 2026-08-31 but is **not yet merged into Master v5**.

Measured supplemental totals:
- **6** ZIP archives;
- **4,607** file members;
- **4,606** PNG textures;
- **4,600** exact-unique members after seven SHA-confirmed duplicate pairs;
- **1,422,620,538** ZIP bytes;
- **1,428,899,744** uncompressed bytes.

Major routed families include Metal, Concrete, Brick, terrain/outdoors, Wood, emission/light support, Fire, Marble, Glass, ritual/mystic, Water, and Foliage. The set also contains six 19-image Fire families, six 10-image Mystic families, and a separate 10-image Mystic emission/support sequence.

Exact archive checksums, counts, duplicate records, family routing, resolution statistics, animation observations, and provenance gates are recorded in:

`SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

Until provenance is established, this supplemental batch is **USER-SUPPLIED / LICENSE NOT YET VERIFIED** and must remain outside public Git binary history.

## Provenance separation

The extracted Map001–Map116 texture material is **license-unverified extracted source material**. It must not be relabeled as CC0 or freely redistributable material. Keep it segregated from verified-open assets and treat it as private/reference/prototyping material unless rights are separately confirmed.

The new supplemental user texture batch is also **license-unverified until evidence is recorded**. Uploading source material to the project does not itself establish redistribution rights.

The Quaternius Fantasy Props MegaKit and both Universal Animation Libraries are verified **CC0 1.0 Universal / Public Domain Dedication** and may be modified and used directly.

## Public-repository safety lock

`zxxdjxxz-del/Diyse-Game` is currently a **public repository**. Therefore license-unverified source ZIPs and directly extracted source textures must **not** be committed to this repository, including through Git LFS, unless rights are separately confirmed or repository/storage visibility is explicitly changed.

Repository safeguards now enforce this split:

- `asset_sources/private_reference/` is ignored by `.gitignore`;
- `assets/environment/extracted_private_reference/` is ignored by `.gitignore`;
- `asset_sources/.gdignore` prevents archival source packages from being scanned/imported by Godot;
- verified redistributable ZIPs under `asset_sources/third_party_cc0/` are routed through Git LFS by `.gitattributes`.

Source-storage routing and local staging rules are documented at repository root in:

`asset_sources/README.md`

## Archive verification

Before any source ZIP is accepted into private storage, Git LFS, or another archival destination, verify it against its controlling checksum manifest.

Master v5 archives use:

`SOURCE_ARCHIVE_MANIFEST.md`

Supplemental Batch 1 archive identities are recorded in:

`SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

Repository verifier for the Master v5 archive set:

`python tools/verify_asset_archives.py`

ZIP-native supplemental intake:

`python tools/asset_forge/zip_intake_engine.py /path/to/archive.zip`

The ZIP intake engine scans archive metadata and images without requiring extraction, and can use `--hash-members` for authoritative member-level hashing.

## Project-use rule

These source textures are a **parts/reference library for building original Diyse maps**, not a target for reconstructing source maps. Diyse layouts, collision, traversal, encounter placement, treasure placement, camera design, landmarks, faction identity, and final environment composition remain original project work.

## Relationship to current visual canon

This inventory records **available source material and production capability**. It does not override exact approved character/location appearance authority or newer explicit visual decisions.

The active rendering authority is:

`../../DIYSE_VISUAL_STYLE_CANON.md`

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight**

The required production path for adapting/rebuilding these assets into that style is:

`../ASSET_STYLE_CONVERSION_PIPELINE.md`

Source assets must be adapted, replaced, or rebuilt where necessary. Merely enlarging, sharpening, or applying a uniform filter does not satisfy the Diyse style conversion standard.

## Raw binary storage

The authoritative Master v5 source ZIP set represented by `SOURCE_ARCHIVE_MANIFEST.md` is approximately **2.25 GB**. Supplemental Batch 1 adds approximately **1.42 GB** of newly uploaded source ZIPs, but those binaries are not yet part of the canonical Master archive set.

Current storage policy:

- **public `Diyse-Game` repository:** authoritative inventory, provenance, hashes, verification tooling, and optionally verified-redistributable CC0 source archives through Git LFS;
- **private storage:** license-unverified source archives and directly derived source material;
- **acceptance rule:** a binary copy becomes authoritative only after its identity is verified against the controlling manifest/intake record.

Current operational preservation state is recorded in:

`BINARY_PRESERVATION_STATUS.md`

Do not treat a public-repository omission of license-unverified binaries as loss of authority: manifest/checksum records preserve source identity. The remaining preservation requirement is maintaining at least one verified private binary copy of every license-unverified authoritative or pending-provenance source batch.
