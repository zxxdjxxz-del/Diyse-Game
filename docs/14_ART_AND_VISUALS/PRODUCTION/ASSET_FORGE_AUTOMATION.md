# Diyse — Asset Forge Automation

**Status:** ACTIVE AUTOMATION IMPLEMENTATION — **v0.8 supplemental ZIP-intake checkpoint**  
**Core:** `../../../tools/asset_forge/forge.py`  
**Processor:** `../../../tools/asset_forge/pipeline.py`  
**Operations:** `../../../tools/asset_forge/ops.py`  
**Prop-pack pipeline:** `../../../tools/asset_forge/prop_pack_pipeline.py`  
**ZIP intake:** `../../../tools/asset_forge/zip_intake_engine.py`  
**Style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Conversion authority:** `ASSET_STYLE_CONVERSION_PIPELINE.md`  
**Asset/provenance authority:** `ASSET_LIBRARY/README.md`

## Purpose

Asset Forge automates repetitive asset conversion while keeping source/reference material, deterministic/generated candidates, technical QA, real-asset validation, and explicitly approved final assets separate.

It is an implementation tool, not visual authority.

## Current automated flow

`SOURCE ARCHIVE → ZIP INTAKE / PROVENANCE RECORD → INVENTORY → CLASSIFY → SHARED-FAMILY ANALYSIS → PLAN/BUDGET → STYLE/PROPAGATE → QA → REAL-ASSET/GAMEPLAY PREVIEW → DETERMINISTIC REVIEW → APPROVE/REDO → EXPORT`

## v0.8 — supplemental ZIP-native intake

`zip_intake_engine.py` allows new user/source texture archives to be inspected **without extracting them into the repository**.

It records:
- archive SHA-256 and byte size;
- ZIP member count and uncompressed bytes;
- member path/size/CRC;
- optional member SHA-256 through `--hash-members`;
- image dimensions, mode and alpha;
- path-aware material family;
- animation family/frame metadata;
- duplicate candidate or exact duplicate groups depending on hashing mode.

This is now the required first step for large supplemental texture uploads.

First real v0.8 intake:

`ASSET_LIBRARY/SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

Measured:
- **6** user-supplied ZIP archives;
- **4,607** file members;
- **4,606** PNG textures;
- **4,600** exact-unique members after seven SHA-confirmed duplicate pairs;
- approximately **1.42 GB** ZIP bytes;
- major routed families: Metal, Concrete, Brick, terrain/outdoors, Wood, emission/light, Fire, Marble, Glass, ritual/mystic, Water and Foliage;
- structured animation content: six 19-image Fire families, six 10-image Mystic families, plus a separate 10-image Mystic emission/support sequence.

The intake remains **USER-SUPPLIED / LICENSE NOT YET VERIFIED** and is not merged into Asset Library Master v5.

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

Major BaseColor family reach:
- Metal — **60 models**;
- Furniture — **41 models**;
- Props — **39 models**;
- Cloth — **10 models**.

The active family grammar is:

`DIYSE_CC0_PROP_MATERIAL_GRAMMAR_V1.md`

Current validation state:
- Furniture — **B10 APPROVED**;
- Metal — **B10 APPROVED**;
- Props — real-model family candidate / user review pending;
- Cloth — real-model family candidate / user review pending.

## v0.7 — data-driven glTF material routing

Earlier prop-pipeline versions still contained material-name heuristics. v0.7 resolves the actual glTF chain:

`MATERIAL → baseColorTexture → TEXTURE → IMAGE URI → SHARED FAMILY`

This correctly handles valid source names such as:
- `MI_Trim_Props_Vertex` → `T_Trim_Props_BaseColor.png`;
- `MI_Banner` → `T_Trim_Cloth_BaseColor.png`.

Material names no longer need to contain the family name.

`shared_material_engine.py` records per-model `material_basecolors` in addition to whole-pack usage.

## Deterministic material families

`material_style_engine.py` supports four UV-safe kinds:
- `wood` → Furniture;
- `metal` → Metal;
- `prop` → mixed Props atlas;
- `cloth` → Cloth.

Furniture uses broad painterly wood planes, sparse construction/damage accents, quiet grain, and QA-triggered normal attenuation where required.

Metal uses controlled cool/neutral planes, stronger material separation than wood, restrained roughness-aware highlights, and selective joint/recess accents.

Props preserve authored hue/category separation while simplifying values/noise and keeping dark accents sparse.

Cloth uses broad fold/value modulation, restrained source hue, very low texture-space ink pressure, and preserves intended graphic insignia/decal regions.

## PBR handling

Forge does not rebuild Normal/ORM maps just because BaseColor changed.

Current source QA examples:
- B10 Furniture normal crosses the strong-normal gate and is attenuated to 0.72 X/Y strength;
- Props normal XY >0.5 ratio is about 13.1% and does not currently require automatic rebalance;
- Cloth normal XY >0.5 ratio is about 4.1%; Cloth roughness median is about 1.0 and remains source-authored for the first family pass.

## Real-model proof state

### B10
Approved real models:
- Barrel;
- Chair_1;
- Lantern_Wall;
- Workbench.

B10 status:
> **STYLE-PASS APPROVED — GAMEPLAY/RUNTIME TEST READY**

Approval authority:
`BENCHMARKS/B10_STYLE_PASS_APPROVAL_V1.md`

### Props / Cloth family candidate

Current broader validation models:
- Bottle_1;
- Book_5;
- Potion_1;
- Banner_1_Cloth;
- Bag;
- Bed_Twin1.

Evidence authority:
`CC0_PROP_CLOTH_FAMILY_VALIDATION_CANDIDATE_V1.md`

Props/Cloth remain user-review pending before family-level production approval.

## Regression coverage

Tests cover the earlier atlas/animation/lighting/budget/resume foundation plus:
- four-family material stylization and dimension preservation;
- actual glTF material-to-BaseColor index resolution;
- shared material discovery and UV usage;
- PBR review/rebalance;
- real glTF validation rendering;
- model-space emitter metadata;
- gameplay-scale previews;
- ZIP-native archive inspection, path-aware classification, animation grouping, and exact member-hash duplicate reporting.

## Next production milestone

1. finish provenance/storage routing for Supplemental Batch 1 before treating it as a redistributable library;
2. add explicit paired BaseColor/emission animation-family matching for the new Fire/Mystic source sets;
3. user-review the Props/Cloth six-model CC0 family candidate;
4. run B04 animated vegetation and B06/B09 effect-family tests using the strongest appropriate source families;
5. run a bounded real Map086 atlas edit + seam QA;
6. add controlled approval/export metadata and automatic family/category partitioning;
7. only then widen into category-sized conversion batches.

> Do not submit either the full Master v5 environment library or the new 4,607-member supplemental batch merely because Forge can inventory/queue them. Provenance, bounded visual gates, and runtime tests remain authoritative.
