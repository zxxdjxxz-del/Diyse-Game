# Diyse — Asset Forge Automation

**Status:** ACTIVE AUTOMATION IMPLEMENTATION — **v1.0 texture-style bridge candidate**, retaining the v0.9 VFX structure-preservation foundation  
**Current planner:** `../../../tools/asset_forge/forge_current.py`  
**Legacy/core planner:** `../../../tools/asset_forge/forge.py`  
**Texture style contract:** `../../../tools/asset_forge/texture_style_contract_v1.json`  
**Deterministic material engine:** `../../../tools/asset_forge/material_style_engine.py`  
**Texture validation batch:** `../../../tools/asset_forge/validation_texture_batch_v1.json`  
**Validation source stager:** `../../../tools/asset_forge/validation_source_stager.py`  
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

Asset Forge automates repetitive asset conversion while keeping source/reference material, deterministic or provider-assisted candidates, technical QA, real-asset validation, provenance, and explicit approval gates separate.

It is an implementation tool, not visual authority. Art Director/style authority defines the visual language; Asset Forge consumes the texture-facing contract and returns candidates/evidence. Asset Forge cannot promote its own outputs to APPROVED or LOCKED.

## Current automated flow

`SOURCE ARCHIVE → INTAKE/PROVENANCE → EXACT SOURCE RESOLUTION → INVENTORY/CLASSIFY → STRUCTURE ANALYSIS → STYLE CONTRACT → PLAN/BUDGET → DETERMINISTIC STYLE OR BOUNDED PROVIDER PASS → PROPAGATE/REPACK → QA → GAMEPLAY/RUNTIME PREVIEW → DETERMINISTIC REVIEW → ART DIRECTOR + USER DECISION → EXPORT`

## v1.0 candidate — texture-style bridge

The approved current Diyse character-side visual language is now translated into a texture-specific contract rather than copied literally into materials.

`texture_style_contract_v1.json` defines:
- controlled saturation/local material color;
- authored light/mid/dark grouping;
- strong material separation;
- deliberate detail hierarchy;
- selective edge emphasis rather than uniform outlines;
- reduced high-frequency noise at HD-2D gameplay scale;
- graphic anime-stylized shape design;
- preservation requirements for dimensions, alpha, tileability, animation registration, lighting-state relationships, and channel semantics.

Character identity, costume, signature props, and character-specific palettes are not texture authority.

The old positive finish language still embedded in the historical `forge.py` constants is not current authority. `forge_current.py` injects the current contract into that implementation core before new planning.

### Deterministic Stone / Foliage / Grass lane

`material_style_engine.py` now supports:
- Stone;
- Foliage;
- Grass;

in addition to the established Wood/Furniture, Metal, Props and Cloth paths.

The new environment profiles are contract-driven and preserve pixel/UV registration. Foliage/Grass preserve source alpha exactly and suppress universal silhouette outlining by restricting edge emphasis to interior material structure.

This deterministic lane is the preferred first validation mechanism where exact registration matters.

### First texture validation — bounded to 12 jobs

`validation_texture_batch_v1.json` contains exactly:
- 6 Stone/environment-atlas representative jobs;
- 6 Foliage/Grass representative jobs.

The batch records exact canonical source filenames plus required lighting/icon/state companions.

Stone atlas jobs remain structure-aware: mixed environment atlases must be analyzed/isolated by material region before a stone result is judged. Non-stone atlas content is not automatically converted into stone.

Map001–Map116 source material remains license-unverified private/reference/prototyping material. The validation batch does not alter that provenance status.

`validation_source_stager.py` runs wherever the authoritative raw archives are mounted and:
- resolves exact basenames;
- fails closed on missing sources;
- fails closed on ambiguous duplicate basenames;
- verifies declared sequence counts;
- SHA-256 hashes each source;
- stages primary and companion files per job;
- never overwrites the source library.

Successful staging produces:

`READY_FOR_ASSET_FORGE_PROCESSING`

After the 12 candidates are produced, processing stops for Art Director + user review. No family-wide promotion is automatic.

## Provider architecture clarification

Asset Forge is **not globally zero-AI**.

It contains:
- deterministic/non-generative processing lanes for UV/pixel-sensitive shared materials and technical transformations;
- the existing optional OpenAI image-edit provider for explicitly selected tasks.

The provider lane remains bounded by hard image-generation call caps, checkpoint/resume, atlas/animation propagation rules, technical QA and approval gates.

This distinction supersedes older shorthand that described the entire Forge as zero-AI-generation.

## v0.9 — VFX structure preservation retained

The verified-CC0 Brackeys bundle remains the first dedicated VFX production source to exercise the VFX preservation layer.

Forge preserves:
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

B06 authority:
`BENCHMARKS/B06_CC0_FIRE_LIGHT_EXECUTION_V1.md`

Current B06 state:
> **SOURCE ANALYSIS COMPLETE — TECHNICAL STYLE PILOT READY**

The source board is technical evidence only; B06 is not STYLE-PASS until a Diyse-styled animated result passes temporal, alpha/emission and runtime-scale review.

## Supplemental ZIP-native intake retained

`zip_intake_engine.py` inspects new archives without extracting them into repository authority and records archive identity, member metadata, dimensions/mode/alpha, path-aware family, animation/grid metadata and duplicate groups.

It ignores packaging noise such as `__MACOSX`, `.DS_Store`, and AppleDouble `._*` files from production counts while leaving raw archive identity untouched.

Supplemental Texture Batch 1 remains:
> **USER-SUPPLIED / LICENSE NOT YET VERIFIED**

Verified CC0 VFX Batch 2 remains:
> **VERIFIED-OPEN SOURCE POOL — STYLE/RUNTIME VALIDATION REQUIRED**

All post-Master-v5 intakes are indexed at:
`ASSET_LIBRARY/SUPPLEMENTAL_INTAKE_INDEX.md`

## Safe-batch foundation

Forge provides:
- SHA-256 source identity and treatment routing;
- coordinate-locked atlas patching/reconstruction;
- animation-anchor generation plus zero-call follower propagation;
- lighting-family propagation;
- seam/alpha/aspect/flicker QA;
- hard provider-call caps where the optional provider is used;
- checkpoint/resume;
- deterministic review sheets from actual outputs;
- exact bounded texture-validation source staging.

## Shared prop architecture retained

The verified 94-model Quaternius pack is material-shared rather than model-bespoke.

Major BaseColor reach:
- Metal — **60 models**;
- Furniture — **41 models**;
- Props — **39 models**;
- Cloth — **10 models**.

Furniture and Metal are B10-approved. Props and Cloth remain broader real-model candidates pending user review.

## Regression coverage

Tests cover:
- atlas/animation/lighting/budget/resume behavior;
- shared material styling and glTF routing;
- UV/PBR QA and rebalancing;
- real-model rendering/emissive anchors/gameplay-scale previews;
- ZIP-native intake and duplicate handling;
- VFX grid/padding/palette/pair preservation;
- active texture-style contract injection;
- deterministic Stone/Foliage/Grass material profiles;
- exact 12-job source-resolution/staging behavior.

## Immediate production sequence

Texture-style bridge:
1. mount the authoritative raw map-source library outside repository authority;
2. resolve/stage `DIYSE_TEXTURE_VALIDATION_12_V1`;
3. produce deterministic first-pass Stone/Foliage/Grass candidates;
4. generate original-vs-processed, 100%-crop and gameplay-scale review evidence;
5. Art Director reviews visual fit, material readability, color/value control and technical integrity;
6. user approves/reworks/rejects representative results;
7. only after approval decide whether a texture family may widen beyond the 12-job validation set.

Existing parallel production gates such as B06 Fire/Light and Props/Cloth review remain valid, but they do not bypass the texture-style validation gate.

> Do not bulk-convert Master v5, Supplemental Batch 1, or the full VFX library merely because Forge can queue them. Provenance, bounded style gates, technical preservation, Art Director review and explicit user approval remain authoritative.
