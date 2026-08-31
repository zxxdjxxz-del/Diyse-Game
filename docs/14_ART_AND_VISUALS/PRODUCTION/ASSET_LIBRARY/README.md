# Diyse Asset Library

**Status:** Authoritative visual-production asset inventory  
**Added:** 2026-08-31

This directory preserves the consolidated Diyse asset-library work and separately indexed post-Master-v5 source intakes. It supports environment construction, VFX, animation reuse, provenance, and visual-style conversion.

## Current authority

The current consolidated inventory remains **DIYSE Asset Library Master v5**.

Repository preservation:
`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/archive/DIYSE_ASSET_LIBRARY_MASTER_2026-08-30_v5/`

- Original master SHA-256: `17648aadd7ad28570b9a017a03362041875e6fa10df173315871dfcb89d57246`
- Original master character count: `175133`
- Original master version/date: `v5` / `2026-08-30`

Master-v5 source archive identity is controlled by:
`SOURCE_ARCHIVE_MANIFEST.md`

Post-Master-v5 intakes are controlled by:
`SUPPLEMENTAL_INTAKE_INDEX.md`

## Master v5 totals

- **3,214** canonical extracted map/environment TGA records.
- **2,878** exact-unique extracted TGAs after byte-level deduplication.
- **107** represented source map families across Maps 001–116.
- Missing map numbers through 116: **015, 033, 042, 085, 097, 098, 099, 101, 102**.
- **94** verified-CC0 Quaternius Fantasy Props MegaKit models.
- **86** verified-CC0 Quaternius humanoid animation clips.

Do not silently add later intake counts to these historical Master-v5 totals.

## Supplemental Batch 1 — user textures / provenance pending

Six uploaded archives were inventoried separately:
- **4,607** file members;
- **4,606** PNG textures;
- **4,600** exact-unique members after seven SHA-confirmed duplicate pairs;
- **1,422,620,538** ZIP bytes.

Major families include Metal, Concrete, Brick, terrain/outdoors, Wood, emission/light support, Fire, Marble, Glass, ritual/mystic, Water and Foliage.

Authority:
`SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

Status:
> **USER-SUPPLIED / LICENSE NOT YET VERIFIED**

These raw binaries must remain outside public Git history unless provenance is established.

## Supplemental Batch 2 — verified CC0 VFX

`brackeys_vfx_bundle.zip` includes its own license/credits file declaring the bundled assets CC0.

Measured usable production payload:
- **213** VFX images;
- **185** particle textures;
- **14** predrawn animation sheets;
- **14** flipbooks;
- **1,318** declared animation-sheet frames;
- **92** matched particle color/alpha pairs;
- **0** exact duplicate usable images.

Asset Forge v0.9 additionally verifies that all **28** predrawn/flipbook sheets split and repack with **0 pixel difference** when source padding/palette transparency are preserved.

Authority:
`VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`

Status:
> **VERIFIED CC0 SOURCE POOL — DIRECT MODIFICATION ALLOWED / STYLE + RUNTIME VALIDATION REQUIRED**

This source set is eligible for the verified third-party CC0 storage lane and is now the preferred production source pool for B06 fire/light testing.

## Provenance separation

Source lanes remain strict:

### License-unverified extracted/private reference

Map001–Map116 extracted material and Supplemental Batch 1 remain private/reference/prototyping material unless rights are separately confirmed. They must not be relabeled as CC0/open.

### Verified open / redistributable

Quaternius Fantasy Props MegaKit, both Quaternius animation libraries, and Brackeys VFX Batch 2 are verified-open sources under their recorded CC0 evidence and may be directly modified after Diyse style/runtime validation.

### Diyse-original

Preferred for signature, faction, story-defining and provenance-sensitive final assets.

## Public-repository safety lock

`zxxdjxxz-del/Diyse-Game` is currently public.

Therefore license-unverified source ZIPs/direct extractions must not be committed, including through Git LFS, until rights are established or storage visibility changes.

Repository safeguards:
- `asset_sources/private_reference/` is ignored;
- `assets/environment/extracted_private_reference/` is ignored;
- `asset_sources/.gdignore` prevents source-package scanning by Godot;
- redistributable source ZIPs under `asset_sources/third_party_cc0/` are routed through Git LFS by `.gitattributes`.

## Intake and verification tools

Master-v5 verifier:

```bash
python tools/verify_asset_archives.py
```

ZIP-native supplemental intake:

```bash
python tools/asset_forge/zip_intake_engine.py /path/to/archive.zip
```

VFX structural validation:

```bash
python tools/asset_forge/vfx_processing_engine.py /path/to/vfx_bundle.zip
```

The intake/processing tools preserve archive identity and technical relationships without overwriting source files.

## Project-use rule

Source textures/VFX are a production parts/reference library, not a target for reconstructing another game's maps or visual identity. Diyse layouts, collision, traversal, encounter/treasure placement, camera design, landmarks, faction identity and final composition remain original project work.

## Relationship to current visual canon

Active style authority:
`../../DIYSE_VISUAL_STYLE_CANON.md`

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight**

Required adaptation path:
`../ASSET_STYLE_CONVERSION_PIPELINE.md`

Merely enlarging, sharpening, recoloring, or applying a uniform filter does not satisfy the Diyse style standard.

## Raw binary storage

Master v5 source ZIPs total approximately **2.25 GB**. Supplemental Batch 1 adds approximately **1.42 GB** and Batch 2 adds approximately **28.2 MB**; neither supplemental batch changes historical Master-v5 totals until deliberate consolidation.

Current operational preservation state:
`BINARY_PRESERVATION_STATUS.md`

Inventory/checksum recording is not the same as durable binary backup. Every authoritative/pending source batch still requires a verified durable copy in the correct provenance/storage lane.
