# Diyse Asset Binary Preservation Status

**Inventory authority:** current Asset Library records  
**Checksum authority:** `SOURCE_ARCHIVE_MANIFEST.md` plus each supplemental intake record

## Baseline source set

The current baseline contains **25 source ZIP archives** represented by `SOURCE_ARCHIVE_MANIFEST.md`:

- 22 map/environment source ZIPs covering the represented Map001–Map116 families;
- 1 Quaternius Fantasy Props MegaKit archive;
- 2 Quaternius Universal Animation Library archives.

The recorded source copies were verified against the manifest's byte sizes, member counts, and SHA-256 values. The manifest is the active identity authority; older consolidated inventory snapshots are Git-history provenance only.

## Supplemental user texture batch 1

Authority:
`SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

Measured:
- **6** ZIP archives;
- **1,422,620,538** ZIP bytes;
- **4,607** file members / **4,606** PNGs;
- **4,600** exact-unique members after seven SHA-confirmed duplicate pairs.

Current preservation state:
> **INVENTORY/CHECKSUM RECORDED — DURABLE PRIVATE BINARY COPY NOT YET VERIFIED**

## Verified CC0 VFX batch 2

Authority:
`VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`

Archive identity:
- `brackeys_vfx_bundle.zip`
- **28,227,919** ZIP bytes;
- SHA-256 `ac0fbf5d5a07688a5d4d35fd0bbae783597d819a3d8a92893b05eb69ddb144c5`;
- included `LICENSE & CREDITS.txt` declares the bundled assets **CC0**.

Current preservation state:
> **INVENTORY/CHECKSUM/LICENSE RECORDED — DURABLE BINARY COPY NOT YET VERIFIED**

## Public/private storage state

`zxxdjxxz-del/Diyse-Game` is public.

Therefore:
- license-unverified source archives are not eligible for public-repository upload;
- this includes the Map001–Map116 source set and Supplemental Batch 1 until provenance is established;
- the repository preserves current source identities, measured inventory, provenance rules, and verification/intake tooling;
- verified CC0 sources may use `asset_sources/third_party_cc0/` through Git LFS;
- license-unverified sources require a verified private/off-repository binary copy.

## Repository safeguards

- `.gitignore` blocks `asset_sources/private_reference/`;
- `.gitignore` blocks `assets/environment/extracted_private_reference/`;
- `.gitattributes` routes redistributable source ZIPs under `asset_sources/third_party_cc0/` to Git LFS;
- `asset_sources/.gdignore` prevents source-package scanning by Godot;
- `tools/verify_asset_archives.py` verifies the baseline checksum manifest;
- `tools/asset_forge/zip_intake_engine.py` inventories new supplemental ZIPs;
- `tools/asset_forge/vfx_intake_engine.py` records VFX structural relationships.

## Remaining preservation actions

### License-unverified baseline map archives

**OPEN:** establish a durable private destination for the Map001–Map116 source ZIPs and verify the stored copies against `SOURCE_ARCHIVE_MANIFEST.md`.

### Supplemental Batch 1

**OPEN:** copy all six ZIPs to durable private storage and verify each against `SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`.

Also open:
- determine/record license or provenance;
- decide whether any proven-redistributable portion may later move to public/Git-LFS storage;
- keep pending-provenance source binaries isolated from final Diyse-native assets.

### Verified CC0 VFX Batch 2

**OPEN:** place `brackeys_vfx_bundle.zip` and its included license in a durable approved source location and verify the ZIP against SHA-256 `ac0fbf5d5a07688a5d4d35fd0bbae783597d819a3d8a92893b05eb69ddb144c5`.
