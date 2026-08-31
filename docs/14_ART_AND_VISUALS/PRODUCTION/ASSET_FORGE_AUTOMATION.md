# Diyse — Asset Forge Automation

**Status:** ACTIVE AUTOMATION IMPLEMENTATION — v0.5 material-first prop-pack checkpoint  
**Core:** `../../../tools/asset_forge/forge.py`  
**Processor:** `../../../tools/asset_forge/pipeline.py`  
**Operations:** `../../../tools/asset_forge/ops.py`  
**Prop-pack pilot:** `../../../tools/asset_forge/prop_pack_pipeline.py`  
**Style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Conversion authority:** `ASSET_STYLE_CONVERSION_PIPELINE.md`  
**Asset/provenance authority:** `ASSET_LIBRARY/README.md`

## Purpose

Asset Forge automates repetitive asset conversion while keeping source/reference material, generated style-pass candidates, deterministic QA/review, and explicitly approved Diyse-final assets separate.

It is an implementation tool, not visual authority. Generated output that conflicts with current visual canon or the conversion pipeline is rejected.

## Current automated flow

`SOURCE → INVENTORY → CLASSIFY → SHARED-MATERIAL ANALYSIS → PLAN → BUDGET → STYLE/PROPAGATE → CHECKPOINT → QA → REAL-ASSET RENDER → DETERMINISTIC REVIEW → APPROVE/REDO → DIYSE-FINAL`

## Core capabilities

### Inventory and planning

Records and routes SHA-256 source identity, dimensions, alpha, category, animation grouping, lighting-family grouping, treatment mode, action queue, and category-specific Diyse style prompts.

### Coordinate-safe atlases

`atlas_engine.py` splits large atlases into fixed-coordinate overlapping patches, forbids patch-size drift, never rearranges atlas coordinates, feather-blends overlaps, can restore source alpha, and reconstructs identity input pixel-exactly in regression tests.

### Animation propagation

`animation_engine.py` directly styles one anchor frame, learns non-spatial palette/edge behavior, propagates that behavior to follower frames using their own moving geometry, preserves source alpha, and spends zero additional image-generation calls on followers.

### Lighting-family propagation

`lighting_engine.py` transfers the source lighting state's relative RGB behavior onto an approved styled base. This supports base + alternate/directional lighting families such as `ra`–`rf` without independently redrawing every state.

### Technical QA

`qa_engine.py` adds atlas seam-regression scoring, alpha-edge/fringe diagnostics, and animation temporal/flicker regression. The original `forge.py qa` still supplies output existence, dimensions, alpha, and aspect checks.

### Budget safety and resume

`budget_engine.py`, `ops.py`, and `pipeline.py` provide generation-call preflight, hard `--max-ai-calls` caps, whole-atlas budget blocking, checkpointing, and `--resume` reuse when source SHA and output files still match.

## v0.5 — material-first 3D prop workflow

The B10 real-source pilot exposed a major production optimization: many 3D props share a small number of trim/material atlases. Forge now treats shared-material libraries **material-first rather than model-first**.

### `shared_material_engine.py`

Reads glTF files directly from source ZIPs and records:
- model names;
- material names;
- image dependencies;
- external buffer dependencies;
- BaseColor usage by model;
- full-pack shared-material counts.

On the verified 94-model Quaternius Fantasy Props MegaKit, the main shared BaseColor families are used by:
- Metal — **60 models**;
- Furniture — **41 models**;
- Props — **39 models**;
- Cloth — **10 models**.

For B10's four representative props, only Furniture + Metal BaseColor sheets are required.

### `material_style_engine.py`

Provides a deterministic, UV-safe, zero-generation-call baseline for shared trim sheets.

It preserves exact texture dimensions and coordinates while applying:
- broad value grouping;
- painterly palette normalization;
- selective dark edge/grain accents;
- reduced micro-noise;
- separate wood and metal material behavior.

This is intentionally conservative. It is a safe baseline and fallback, not automatic artistic approval.

### `uv_usage_engine.py`

Rasterizes actual glTF UV triangles into texture-space usage masks, including wrapped UVs.

Uses:
- determine what percentage of a shared trim sheet selected models actually sample;
- identify active atlas patches for optional AI-assisted edits;
- avoid spending generation calls on irrelevant regions;
- preserve exact UV registration.

For B10's Barrel + Chair_1 + Workbench Furniture material, measured UV coverage is about **29%** of the 2048 trim sheet.

### `pbr_qa_engine.py`

Runs static diagnostics on Normal and ORM maps before modifying them.

The first B10 scan found:
- Furniture roughness is already predominantly matte;
- Metal roughness is moderately rough rather than mirror-glossy;
- Furniture normal intensity triggers a `strong_normal_review` flag;
- Metal normal/roughness data does not currently trigger an automatic review flag.

Forge therefore does not blindly rebuild Normal/ORM maps merely because BaseColor was restyled.

### `model_render_engine.py`

Provides a deterministic headless software renderer for real glTF review without Blender/OpenGL.

Capabilities:
- glTF +Y-up three-quarter review camera;
- texture/UV sampling;
- neutral, warm, and cool validation lighting;
- deterministic output suitable for CI/review packages;
- validation-only lantern glow hint until true emissive data is authored.

It is a review renderer, not a replacement for final Godot runtime validation.

### `prop_pack_pipeline.py`

Runs the material-first prop workflow as one command:

1. analyze selected models inside the source ZIP;
2. extract only required glTF/buffer/image dependencies;
3. stylize supported shared BaseColor families;
4. run PBR diagnostics;
5. render the real selected models under neutral/warm/cool validation lighting;
6. build a deterministic review sheet from those real renders;
7. write a manifest with material usage, PBR flags, render paths, and call count.

The first real B10 run produced:
- **4 real models**;
- **2 styled shared materials**;
- **12 real glTF review renders**;
- **1 deterministic review sheet**;
- **0 image-generation calls**.

## Deterministic review sheets

The image model does not create benchmark infographics.

Forge review boards are assembled from actual output images and exact metadata, preventing stale benchmark imagery, invented approval labels, fabricated completion percentages, wrong-category carryover, and typography hallucinations.

## Provenance rule

Forge never overwrites source assets.

License-unverified extracted assets remain license-unverified after restyling. Automated transformation does not convert them into original or CC0 assets.

Verified CC0 sources may be directly transformed and promoted after style/runtime review.

All temporary Forge products live under git-ignored `.asset_forge/` until deliberately promoted.

## Regression coverage

Current tests cover:
- category classification and work routing;
- deterministic review-sheet creation;
- pixel-exact atlas identity reconstruction;
- rejection of patch dimension drift;
- exact animation anchor preservation;
- animation alpha preservation;
- fake-provider atlas/animation orchestration;
- lighting-state propagation;
- seam and flicker regression behavior;
- generation-call estimation and hard caps;
- checkpoint/resume reuse;
- shared BaseColor detection across selected and full model sets;
- deterministic material stylization and size preservation;
- +Y-up headless glTF rendering;
- wrapped-UV occupancy masks;
- static Normal/ORM review flags.

## Current real-source status

`ASSET_FORGE_PILOT_VALIDATION_V1.md` records the Map084/Map086 routing and budget pilot.

`BENCHMARKS/B10_DETERMINISTIC_MATERIAL_BASELINE_PILOT_V1.md` records the first real CC0 material/model pilot.

B10's **technical material pipeline passes**, but its final visual treatment remains open. Current refinement gates are:
1. quieter wood line density at gameplay scale;
2. stronger controlled metal plane/highlight separation;
3. true Lantern_Wall emissive mask/material authoring;
4. final Normal/ORM compatibility check in the game renderer;
5. gameplay-scale workshop/interior integration proof.

## Next implementation/pilot milestone

Before full-library processing:

1. finish B10 material refinement + true emissive handling;
2. run B04 real animated-grass anchor/propagation QA;
3. run a small real Map086 atlas edit and seam check;
4. run one real base + lighting-state family;
5. add automatic family/category batch partitioning;
6. add gameplay-scale preview generation;
7. add approve/reject/redo metadata and controlled export;
8. add provider retry/backoff;
9. only then consider category-sized or whole-library execution.

> Do not submit the entire 3,214-file environment library to generation merely because Forge can technically queue it. Bounded real-output pilots remain the production gate.
