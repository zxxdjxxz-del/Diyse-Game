# Diyse Asset Library

**Status:** Authoritative visual-production source inventory

This directory owns the current inventory, provenance, verification, and storage rules for reusable environment, VFX, animation, and third-party source inputs. Superseded inventory documents and upload-event history are recoverable through Git history rather than retained as a parallel authority layer.

## Current source authority

Current source records are split by purpose:

- `SOURCE_ARCHIVE_MANIFEST.md` — exact filename, byte size, member count, and SHA-256 identity for the **25 baseline source ZIPs**;
- `SUPPLEMENTAL_INTAKE_INDEX.md` — routing for the **7 current supplemental source ZIPs**;
- `SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md` — exact identity, measured contents, and pending-provenance state for six user-supplied texture ZIPs;
- `VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md` — exact identity, license evidence, and technical structure for the Brackeys CC0 VFX bundle;
- `BINARY_PRESERVATION_STATUS.md` — current durable-storage state and remaining preservation actions.

Together these represent **32 active asset-source ZIPs**. Superseded diagnostic uploads and older consolidated inventory documents are not live source authority.

## Baseline source coverage

The baseline source set represented by `SOURCE_ARCHIVE_MANIFEST.md` contains:

- **22** map/environment archive ZIPs covering **107 represented map families** across Maps 001–116;
- **3** verified-CC0 Quaternius source ZIPs;
- **3,214** previously inventoried canonical map/environment TGA records;
- **2,878** exact-unique extracted TGAs after byte-level deduplication;
- **94** verified-CC0 Quaternius Fantasy Props MegaKit models;
- **86** verified-CC0 Quaternius humanoid animation clips.

Current missing map numbers through 116:
> **015, 033, 042, 085, 097, 098, 099, 101, 102**

The exact source ZIP identities, including the Quaternius rig payload hashes, are owned by `SOURCE_ARCHIVE_MANIFEST.md`. Detailed superseded per-file inventory snapshots remain available in Git history if forensic reconstruction is ever necessary.

## Supplemental Batch 1 — user textures / provenance pending

Six current source archives are recorded in:
`SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

Measured:
- **4,607** file members;
- **4,606** PNG textures;
- **4,600** exact-unique members after seven SHA-confirmed duplicate pairs;
- **1,422,620,538** ZIP bytes.

Status:
> **USER-SUPPLIED / LICENSE NOT YET VERIFIED**

These raw binaries remain private/reference material unless provenance or authorization is established. They must not be represented as redistributable/open merely because the project has their technical inventory.

## Supplemental Batch 2 — verified CC0 VFX

The current Brackeys VFX source archive is recorded in:
`VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`

Measured usable payload:
- **213** VFX images;
- **185** particle textures;
- **14** predrawn animation sheets;
- **14** flipbooks;
- **1,318** implied animation-sheet frames;
- **92** matched particle color/alpha pairs;
- **0** exact duplicate usable images.

Status:
> **VERIFIED CC0 SOURCE POOL — DIRECT MODIFICATION ALLOWED / STYLE + RUNTIME VALIDATION REQUIRED**

This source set is eligible for the verified third-party CC0 storage lane.

## Provenance separation

### License-unverified extracted/private reference

Map001–Map116 extracted material and Supplemental Batch 1 remain private/reference/prototyping material unless rights are separately confirmed. They must not be relabeled as CC0/open.

### Verified open / redistributable

Quaternius Fantasy Props MegaKit, both Quaternius animation libraries, and Brackeys VFX Batch 2 are verified-open sources under their recorded evidence and may be directly modified after Diyse style/runtime validation.

### Diyse-original

Preferred for signature, faction, story-defining, and provenance-sensitive final assets.

## Repository visibility and binary safety

`zxxdjxxz-del/Diyse-Game` is public.

Public visibility does **not** waive provenance, authorization, redistribution, or licensing requirements.

Repository safeguards:
- Diyse-original or otherwise authorized source art belongs only in an appropriate tracked source-art lane;
- license-unverified third-party material remains private/reference only;
- `asset_sources/private_reference/` is ignored for private source material;
- `assets/environment/extracted_private_reference/` is ignored;
- `asset_sources/.gdignore` prevents source-package scanning by Godot;
- redistributable source ZIPs under `asset_sources/third_party_cc0/` are routed through Git LFS by `.gitattributes`.

## Intake and verification tools

Verify baseline source ZIPs against current checksums:

```bash
python tools/verify_asset_archives.py
```

Inventory new ZIP-native source batches:

```bash
python tools/asset_forge/zip_intake_engine.py /path/to/archive.zip
```

Validate VFX source structure:

```bash
python tools/asset_forge/vfx_processing_engine.py /path/to/vfx_bundle.zip
```

## Project-use rule

Source textures/VFX are a production parts/reference library, not a target for reconstructing another game's maps or visual identity. Diyse layouts, collision, traversal, encounter/treasure placement, camera design, landmarks, faction identity, and final composition remain original project work.

## Relationship to current visual canon

Active style authority:
`../../DIYSE_VISUAL_STYLE_CANON.md`

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight**

Required adaptation path:
`../ASSET_STYLE_CONVERSION_PIPELINE.md`

Current exact character masters are separately repository-backed under:
`asset_sources/characters/current/`

Their controlling authority index is:
`../CHARACTERS/README.md`

## Raw binary storage

The 25 baseline source ZIPs total approximately **2.25 GB**. Supplemental Batch 1 adds approximately **1.42 GB** and Batch 2 adds approximately **28.2 MB**.

Current operational preservation state:
`BINARY_PRESERVATION_STATUS.md`

Inventory/checksum recording is not the same as durable binary backup. Each active source batch requires a verified durable copy in the correct provenance/storage lane.
