# Diyse Asset Binary Preservation Status

**Status date:** 2026-08-31  
**Inventory authority:** DIYSE Asset Library Master v5 + separately inventoried supplemental batches  
**Checksum authority:** `SOURCE_ARCHIVE_MANIFEST.md` plus each supplemental intake manifest

## Verified Master v5 source set

The current working Master v5 source set contains all **25 authoritative ZIP archives** represented by `SOURCE_ARCHIVE_MANIFEST.md`:

- 22 authoritative map/environment archive ZIPs covering the represented Map001–Map116 source families;
- 1 Quaternius Fantasy Props MegaKit archive;
- 2 Quaternius Universal Animation Library archives.

On 2026-08-31 the available source copies were rechecked against the manifest. All 25 matched their expected byte sizes and SHA-256 values. ZIP member-count validation uses file members only and excludes explicit directory entries, matching the manifest convention.

## Supplemental user texture batch 1

A separate six-archive user-supplied texture batch was inventoried on 2026-08-31.

Authority record:

`SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

Measured:
- **6** ZIP archives;
- **1,422,620,538** ZIP bytes;
- **4,607** file members / **4,606** PNGs;
- **4,600** exact-unique members after seven SHA-confirmed duplicate pairs.

Archive-level SHA-256 values are preserved in the supplemental intake record.

Current preservation state:
> **INVENTORY/CHECKSUM RECORDED — DURABLE PRIVATE BINARY COPY NOT YET VERIFIED**

The sandbox/upload copies used during intake must not be treated as durable archival storage.

## Verified CC0 VFX batch 2

A separate Brackeys VFX source bundle was inventoried on 2026-08-31.

Authority record:

`VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`

Archive identity:
- `brackeys_vfx_bundle.zip`
- **28,227,919** ZIP bytes;
- SHA-256 `ac0fbf5d5a07688a5d4d35fd0bbae783597d819a3d8a92893b05eb69ddb144c5`;
- **213** usable VFX images after macOS metadata/resource-fork filtering;
- included `LICENSE & CREDITS.txt` declares all bundled assets **Creative Commons Zero (CC0)**.

Current preservation state:
> **INVENTORY/CHECKSUM/LICENSE RECORDED — DURABLE BINARY COPY NOT YET VERIFIED**

Unlike Supplemental Batch 1, this archive is eligible for the project’s verified third-party CC0 storage lane. The current sandbox/upload copy is still not durable archival storage.

## Public/private storage state

`zxxdjxxz-del/Diyse-Game` is currently public.

Therefore:

- license-unverified source archives are **not eligible for public-repository upload**;
- this includes both the extracted Map001–Map116 source set and Supplemental Batch 1 until provenance is established;
- the public repository preserves filenames, sizes, member counts, hashes, inventory, provenance rules, and verification/intake tooling;
- verified CC0 archives such as Quaternius sources and Brackeys VFX Batch 2 may be routed to `asset_sources/third_party_cc0/` through the project’s Git-LFS policy when a durable repository copy is deliberately added;
- license-unverified source archives require at least one verified private/off-repository binary copy.

## Repository safeguards completed

- `.gitignore` blocks `asset_sources/private_reference/`;
- `.gitignore` blocks `assets/environment/extracted_private_reference/`;
- `.gitattributes` routes redistributable source ZIPs under `asset_sources/third_party_cc0/` to Git LFS;
- `asset_sources/.gdignore` prevents source-package scanning by Godot;
- `tools/verify_asset_archives.py` verifies the existing Master v5 archive manifest;
- `tools/asset_forge/zip_intake_engine.py` inventories new supplemental ZIPs without extraction and supports member-level SHA hashing;
- `tools/asset_forge/vfx_intake_engine.py` records VFX sheet grids, implied frame counts, VFX families and particle color/alpha pair relationships.

## Remaining preservation actions

### Master v5 license-unverified archives

**OPEN:** establish a durable private binary destination for the license-unverified Map001–Map116 source ZIPs, copy the authoritative files there, and run the repository verifier against that destination before declaring that raw-binary preservation layer closed.

### Supplemental Batch 1

**OPEN:** copy all six newly uploaded ZIPs to durable private storage, then verify each stored copy against the archive SHA-256 values in `SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`.

Also still open:
- determine/record license or provenance for the supplemental source set;
- decide whether any proven-redistributable portion may later move to public/Git-LFS storage;
- keep pending-provenance source binaries isolated from final Diyse-native assets.

### Verified CC0 VFX Batch 2

**OPEN:** place `brackeys_vfx_bundle.zip` in a durable approved CC0 source location and verify the stored copy against SHA-256 `ac0fbf5d5a07688a5d4d35fd0bbae783597d819a3d8a92893b05eb69ddb144c5`.

Preserve the included `LICENSE & CREDITS.txt` alongside the durable source copy.

These open storage actions do not invalidate the already-preserved inventory, checksum and license authority records.
