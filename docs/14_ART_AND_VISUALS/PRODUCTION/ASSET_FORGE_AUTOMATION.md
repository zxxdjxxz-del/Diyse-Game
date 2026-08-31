# Diyse — Asset Forge Automation

**Status:** ACTIVE AUTOMATION IMPLEMENTATION — v0.6 prop-family refinement checkpoint  
**Core:** `../../../tools/asset_forge/forge.py`  
**Processor:** `../../../tools/asset_forge/pipeline.py`  
**Operations:** `../../../tools/asset_forge/ops.py`  
**Prop-pack pilot:** `../../../tools/asset_forge/prop_pack_pipeline.py`  
**Style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Conversion authority:** `ASSET_STYLE_CONVERSION_PIPELINE.md`  
**Asset/provenance authority:** `ASSET_LIBRARY/README.md`

## Purpose

Asset Forge automates repetitive asset conversion while keeping source/reference material, generated or deterministic style-pass candidates, technical QA, real-asset review, and explicitly approved Diyse-final assets separate.

It is an implementation tool, not visual authority. Output that conflicts with current visual canon or the conversion pipeline is rejected.

## Current automated flow

`SOURCE → INVENTORY → CLASSIFY → SHARED-MATERIAL ANALYSIS → PLAN → BUDGET → STYLE/PROPAGATE → PBR QA/REBALANCE → CHECKPOINT → REAL-ASSET RENDER → GAMEPLAY-SCALE PREVIEW → DETERMINISTIC REVIEW → APPROVE/REDO → DIYSE-FINAL`

## Existing safe-batch foundation

Forge already provides:
- SHA-256 source identity and treatment routing;
- coordinate-locked atlas patching and reconstruction;
- animation-anchor generation plus zero-call follower propagation;
- base + alternate/directional lighting propagation;
- seam, alpha, aspect, and temporal/flicker QA;
- image-generation call estimation and hard `--max-ai-calls` caps;
- whole-atlas budget blocking;
- checkpoint/resume reuse when source SHA still matches;
- deterministic review sheets made from actual outputs rather than generated infographics.

## v0.5–v0.6 material-first 3D prop workflow

The verified Quaternius prop pack showed that model-first conversion would waste work because many models share a small number of trim atlases.

`shared_material_engine.py` analyzes actual glTF dependencies. Across the 94 verified CC0 props, major shared BaseColor families are used by:
- Metal — **60 models**;
- Furniture — **41 models**;
- Props — **39 models**;
- Cloth — **10 models**.

For B10's Barrel / Chair_1 / Lantern_Wall / Workbench benchmark, only Furniture + Metal BaseColor families are required.

### `material_style_engine.py`

The deterministic UV-safe v2 material backend now:
- preserves exact dimensions and UV registration;
- builds broad painterly value planes first;
- preserves sparse meaningful existing dark marks instead of generating a full edge field;
- filters small isolated line fragments;
- keeps wood line density quieter than the first technical baseline;
- gives metal stronger controlled light/dark separation;
- remains a zero-generation-call baseline/fallback rather than automatic artistic approval.

### `uv_usage_engine.py`

Rasterizes actual glTF UV triangles into usage masks so Forge can determine which parts of a shared trim sheet selected models actually sample. B10's Barrel + Chair_1 + Workbench use about **29%** of the Furniture trim sheet.

This enables future AI-assisted material work to target active UV regions rather than blindly editing whole 2048 atlases.

### `pbr_qa_engine.py` + `normal_rebalance_engine.py`

PBR QA evaluates Normal/ORM data before modification.

B10 source findings:
- Furniture roughness is predominantly matte;
- Metal roughness is moderately rough, not mirror-glossy;
- Furniture normal intensity crosses the `strong_normal_review` gate;
- Metal does not require the same correction.

When flagged, `normal_rebalance_engine.py` attenuates tangent X/Y strength while preserving UV registration.

For the B10 Furniture normal:
- source XY `> 0.5`: approximately **25.2%**;
- source XY `> 0.75`: approximately **13.4%**;
- after 0.72 rebalance, XY `> 0.5`: approximately **16.6%**;
- after 0.72 rebalance, XY `> 0.75`: **0%**.

ORM remains unchanged in the current pilot because its distributions do not justify an automatic rewrite.

### `model_render_engine.py`

The headless glTF validation renderer now supports:
- +Y-up three-quarter camera;
- shared styled BaseColor sampling;
- source ORM-aware ambient/roughness/metalness response;
- restrained painterly specular separation;
- neutral / warm / cool validation lighting;
- model-space authored light anchors rather than fixed screen-space glow placement.

It remains a validation renderer, not a replacement for final Godot rendering.

### `emissive_anchor_engine.py`

The source Lantern_Wall contains no authored emissive material. Forge therefore exports explicit light-source metadata instead of pretending one exists.

The real B10 pilot derives a lower-cage emitter at approximately:
- position `(0.000000, 0.486414, 0.810444)` source/model units;
- core radius `0.081287`;
- baseline light range `1.136456`;
- warm baseline color `RGB 255 / 176 / 82`.

This can later drive a Godot local light and/or small emissive overlay.

### `gameplay_preview_engine.py`

Builds a deterministic scale/readability scene from actual glTF extents instead of independently zoomed hero renders.

The B10 preview uses:
- real model physical extents;
- consistent pixels-per-unit scaling;
- a neutral 1.75-unit character measurement silhouette;
- a simple non-authoritative workshop backdrop.

This catches props that only appear readable because a close-up render enlarged them.

### `prop_pack_pipeline.py`

The one-command prop pilot now performs:
1. shared-material dependency analysis;
2. selective source extraction;
3. deterministic BaseColor stylization;
4. PBR QA;
5. automatic flagged-normal rebalance;
6. emissive-anchor derivation;
7. neutral/warm/cool real glTF rendering;
8. deterministic close-up review-sheet generation;
9. gameplay-scale integration preview generation;
10. manifest output recording all material, PBR, emissive, render, and call-count evidence.

The current B10 deterministic refinement still uses **0 image-generation calls**.

## Current B10 status

`BENCHMARKS/B10_REAL_PROP_REFINEMENT_CANDIDATE_V2.md` is the current real-prop candidate authority.

B10 is now:
> **VISUAL REFINEMENT CANDIDATE V2 — USER REVIEW PENDING**

Do not promote it to STYLE-PASS until the real v2 wood/metal treatment is explicitly approved.

## Regression coverage

Current tests cover the earlier atlas/animation/lighting/budget/resume foundation plus:
- shared BaseColor detection;
- UV-safe material stylization and size preservation;
- +Y-up glTF review rendering;
- wrapped-UV occupancy masks;
- static Normal/ORM review flags;
- deterministic normal-strength attenuation;
- model-space lantern emitter derivation.

## Next production milestone

After B10 visual approval:
1. promote B10 to STYLE-PASS and define the shared Furniture / Metal / Props / Cloth production material grammar;
2. run B04 real animated-grass anchor/propagation QA;
3. run a bounded real Map086 atlas edit and seam check;
4. run one real base + lighting-state family;
5. add automatic family/category batch partitioning and approve/reject/export metadata;
6. only then widen into category-sized conversion batches.

> Do not submit the entire 3,214-file environment library merely because Forge can queue it. Bounded real-output pilots remain the production gate.
