# Diyse Asset Binary Preservation Status

**Status date:** 2026-08-31  
**Inventory authority:** DIYSE Asset Library Master v5  
**Checksum authority:** `SOURCE_ARCHIVE_MANIFEST.md`

## Verified source set

The current working source set contains all **25 authoritative ZIP archives** represented by the manifest:

- 22 authoritative map/environment archive ZIPs covering the represented Map001–Map116 source families;
- 1 Quaternius Fantasy Props MegaKit archive;
- 2 Quaternius Universal Animation Library archives.

On 2026-08-31 the available source copies were rechecked against the manifest. All 25 matched their expected byte sizes and SHA-256 values. ZIP member-count validation uses file members only and excludes explicit directory entries, matching the manifest convention.

## Public/private storage state

`zxxdjxxz-del/Diyse-Game` is currently public.

Therefore:

- the license-unverified extracted Map001–Map116 source archives are **not eligible for public-repository upload**;
- the public repository preserves their filenames, sizes, member counts, hashes, inventory, provenance rules, and verification tooling;
- verified CC0 Quaternius source archives may be stored under `asset_sources/third_party_cc0/` through Git LFS;
- license-unverified source archives require at least one verified private/off-repository binary copy.

## Repository safeguards completed

- `.gitignore` blocks `asset_sources/private_reference/`;
- `.gitignore` blocks `assets/environment/extracted_private_reference/`;
- `.gitattributes` routes redistributable source ZIPs under `asset_sources/third_party_cc0/` to Git LFS;
- `asset_sources/.gdignore` prevents source-package scanning by Godot;
- `tools/verify_asset_archives.py` verifies size, ZIP file-member count, SHA-256, missing files, and duplicate staged copies.

## Remaining preservation action

**OPEN:** establish a durable private binary destination for the license-unverified Map001–Map116 source ZIPs, copy the authoritative files there, and run the repository verifier against that destination before declaring the raw-binary preservation layer closed.

This open storage action does not invalidate the already-preserved v5 inventory or checksum authority.
