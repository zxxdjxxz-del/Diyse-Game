# Diyse — Asset Forge Automation

**Status:** ACTIVE AUTOMATION IMPLEMENTATION — **v0.7 four-family prop routing checkpoint**  
**Core:** `../../../tools/asset_forge/forge.py`  
**Processor:** `../../../tools/asset_forge/pipeline.py`  
**Operations:** `../../../tools/asset_forge/ops.py`  
**Prop-pack pipeline:** `../../../tools/asset_forge/prop_pack_pipeline.py`  
**Style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Conversion authority:** `ASSET_STYLE_CONVERSION_PIPELINE.md`  
**Asset/provenance authority:** `ASSET_LIBRARY/README.md`

## Purpose

Asset Forge automates repetitive asset conversion while keeping source/reference material, deterministic/generated candidates, technical QA, real-asset validation, and explicitly approved final assets separate.

It is an implementation tool, not visual authority.

## Current automated flow

`SOURCE → INVENTORY → CLASSIFY → SHARED-MATERIAL ANALYSIS → REAL glTF MATERIAL BINDING → PLAN/BUDGET → STYLE/PROPAGATE → PBR QA/REBALANCE → REAL-ASSET RENDER → GAMEPLAY-SCALE PREVIEW → DETERMINISTIC REVIEW → APPROVE/REDO → EXPORT`

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

`shared_material_engine.py` now records per-model `material_basecolors` in addition to whole-pack usage.

## Deterministic material families

`material_style_engine.py` supports four UV-safe kinds:
- `wood` → Furniture;
- `metal` → Metal;
- `prop` → mixed Props atlas;
- `cloth` → Cloth.

### Furniture
Approved B10 behavior:
- broad painterly wood planes;
- sparse construction/damage accents;
- quiet grain;
- QA-triggered normal attenuation where required.

### Metal
Approved B10 behavior:
- controlled cool/neutral planes;
- stronger material separation than wood;
- restrained roughness-aware highlights;
- selective joint/recess accents.

### Props
Mixed-use atlas behavior:
- preserve authored hue/category separation;
- simplify values/noise;
- only sparse structural dark accents;
- do not recolor the whole sheet to one palette.

### Cloth
Soft-surface behavior:
- broad fold/value modulation;
- source hue retained with restrained saturation;
- very low texture-space ink pressure;
- preserve intended graphic insignia/decal regions;
- highly matte source PBR data retained unless later QA requires change.

## PBR handling

Forge does not rebuild Normal/ORM maps just because BaseColor changed.

Current source QA examples:
- B10 Furniture normal crosses the strong-normal gate and is attenuated to 0.72 X/Y strength;
- Props normal XY >0.5 ratio is about 13.1% and does not currently require automatic rebalance;
- Cloth normal XY >0.5 ratio is about 4.1%; Cloth roughness median is about 1.0 and remains source-authored for the first family pass.

`model_render_engine.py` now resolves source ORM family from the actual styled BaseColor filename, so renamed/exception materials still receive the correct roughness/metalness validation data.

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

The six-model pass validates real glTF routing, neutral/warm/cool rendering, source PBR compatibility and physical-scale readability while still using **0 image-generation calls**.

Props/Cloth remain user-review pending before family-level production approval.

## Regression coverage

Tests now cover the earlier atlas/animation/lighting/budget/resume foundation plus:
- four-family material stylization and dimension preservation;
- actual glTF material-to-BaseColor index resolution;
- non-obvious material names such as Banner/Props-Vertex routing;
- hue preservation for Props/Cloth families;
- shared material discovery;
- UV usage masks;
- PBR review/rebalance;
- real glTF validation rendering;
- model-space emitter metadata;
- gameplay-scale previews.

## Next production milestone

1. user-review the Props/Cloth six-model family candidate;
2. if approved, promote all four major CC0 shared families and switch the 94-model pack to **exception detection / model-specific overrides**;
3. run B04 real animated-grass anchor/propagation QA;
4. run a bounded real Map086 atlas edit + seam QA;
5. run one real base + lighting-state family;
6. add controlled approval/export metadata and automatic family/category partitioning;
7. only then widen into category-sized conversion batches.

> Do not submit the full 3,214-file environment library merely because Forge can queue it. Bounded real-output and runtime gates remain authoritative.
