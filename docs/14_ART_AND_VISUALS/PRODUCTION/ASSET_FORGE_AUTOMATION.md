# Diyse — Asset Forge Automation

**Status:** ACTIVE AUTOMATION IMPLEMENTATION — **v0.9 VFX structure-preservation checkpoint**  
**Core:** `../../../tools/asset_forge/forge.py`  
**Processor:** `../../../tools/asset_forge/pipeline.py`  
**Operations:** `../../../tools/asset_forge/ops.py`  
**Prop-pack pipeline:** `../../../tools/asset_forge/prop_pack_pipeline.py`  
**ZIP intake:** `../../../tools/asset_forge/zip_intake_engine.py`  
**VFX intake:** `../../../tools/asset_forge/vfx_intake_engine.py`  
**VFX processor:** `../../../tools/asset_forge/vfx_processing_engine.py`  
**Style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Conversion authority:** `ASSET_STYLE_CONVERSION_PIPELINE.md`  
**Asset/provenance authority:** `ASSET_LIBRARY/README.md`

## Purpose

Asset Forge automates repetitive asset conversion while keeping source/reference material, generated/deterministic candidates, technical QA, real-asset validation, provenance, and explicit approval gates separate.

It is an implementation tool, not visual authority.

## Current automated flow

`SOURCE ARCHIVE → ZIP/VFX INTAKE → PROVENANCE LANE → INVENTORY/CLASSIFY → STRUCTURE ANALYSIS → PLAN/BUDGET → STYLE/PROPAGATE → REPACK → QA → GAMEPLAY/RUNTIME PREVIEW → DETERMINISTIC REVIEW → APPROVE/REDO → EXPORT`

## v0.9 — VFX structure preservation

The verified-CC0 Brackeys bundle is the first dedicated VFX production source to exercise this layer.

Forge now preserves:
- spritesheet/flipbook grid registration and frame order;
- small transparent right/bottom source padding outside a declared frame grid;
- palette-mode transparency metadata;
- paired particle color/alpha masks;
- RGB fire sheets for additive/emissive shader testing rather than forced alpha conversion.

Full real-bundle validation:
- **213** usable VFX images;
- **28** predrawn/flipbook sheets;
- **1,318** declared frames;
- **3** padded source sheets;
- **92** matched particle color/alpha pairs;
- all 28 sheets split and reconstruct with **0 pixel difference**.

Padded cases are preserved exactly:
- `star_explosion_6x5.png`: 4 transparent bottom rows;
- `impact_white_6x4.png`: 1 transparent bottom row;
- `flame_02_15x4.tga`: 8 transparent right columns.

This prevents false extra frames and avoids animation drift from naive even-grid assumptions.

B06 now uses this verified-open source pool as its primary fire/light production basis:

`BENCHMARKS/B06_CC0_FIRE_LIGHT_EXECUTION_V1.md`

Current B06 state:
> **SOURCE ANALYSIS COMPLETE — TECHNICAL STYLE PILOT READY**

The source board is technical evidence only; B06 is not STYLE-PASS until a Diyse-styled animated result passes temporal, alpha/emission and runtime-scale review.

## v0.8 — supplemental ZIP-native intake

`zip_intake_engine.py` inspects new archives without extracting them into repository authority and records archive identity, member metadata, dimensions/mode/alpha, path-aware family, animation/grid metadata and duplicate groups.

It now automatically ignores packaging noise such as `__MACOSX`, `.DS_Store`, and AppleDouble `._*` files from production counts while leaving raw archive identity untouched.

Supplemental Texture Batch 1 remains:
> **USER-SUPPLIED / LICENSE NOT YET VERIFIED**

Authority:
`ASSET_LIBRARY/SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

Verified CC0 VFX Batch 2 is:
> **VERIFIED-OPEN SOURCE POOL — STYLE/RUNTIME VALIDATION REQUIRED**

Authority:
`ASSET_LIBRARY/VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`

All post-Master-v5 intakes are indexed at:
`ASSET_LIBRARY/SUPPLEMENTAL_INTAKE_INDEX.md`

## Safe-batch foundation

Forge provides:
- SHA-256 source identity and treatment routing;
- coordinate-locked atlas patching/reconstruction;
- animation-anchor generation plus zero-call follower propagation;
- lighting-family propagation;
- seam/alpha/aspect/flicker QA;
- hard image-generation call caps;
- checkpoint/resume;
- deterministic review sheets from actual outputs.

## Four-family shared prop architecture

The verified 94-model Quaternius pack is material-shared rather than model-bespoke.

Major BaseColor reach:
- Metal — **60 models**;
- Furniture — **41 models**;
- Props — **39 models**;
- Cloth — **10 models**.

Furniture and Metal are B10-approved. Props and Cloth remain broader real-model candidates pending user review.

Forge resolves actual glTF material bindings rather than relying on material-name heuristics and only alters Normal/ORM data when PBR QA calls for it.

## Regression coverage

Tests cover:
- atlas/animation/lighting/budget/resume behavior;
- four-family material styling and glTF routing;
- UV/PBR QA and rebalancing;
- real-model rendering/emissive anchors/gameplay-scale previews;
- ZIP-native intake and duplicate handling;
- VFX grid parsing;
- small source-padding resolution;
- exact grid split/repack;
- palette transparency preservation;
- particle color/alpha pairing.

## Next production milestone

1. build the first actual Diyse B06 fire/light style candidate from the bounded CC0 subset;
2. run temporal/flicker, alpha/fringe and additive/emissive QA on that animated candidate;
3. test B06 at actual field/battle runtime scale before any STYLE-PASS promotion;
4. user-review the Props/Cloth six-model family candidate;
5. run B04 animated vegetation and then B05/B09 bounded source-family tests;
6. finish provenance/storage routing for Supplemental Batch 1;
7. run bounded Map086 atlas/seam validation;
8. only then widen into category-sized conversion batches.

> Do not bulk-convert Master v5, Supplemental Batch 1, or the full VFX library merely because Forge can queue them. Provenance, bounded style gates and runtime proof remain authoritative.
