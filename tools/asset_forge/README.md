# Diyse Asset Forge

**Status:** **v1.0 texture-style bridge candidate** built on the v0.9 VFX/structure-preservation pipeline.

Diyse Asset Forge automates conversion of the current asset library into the approved Diyse visual language while preserving source provenance, archive identity, atlas/grid registration, animation stability, paired masks, shared-material reuse, lighting families, technical QA, and explicit approval gates.

Asset Forge is an implementation/processing system. It does **not** define visual canon and it cannot auto-approve or lock its own outputs.

## Current style authority

For new texture planning, use:

- `texture_style_contract_v1.json` — Art Director → Asset Forge texture-facing style contract;
- `forge_current.py` — current planning entrypoint that injects that contract into the existing Forge planner;
- `material_style_engine.py` — deterministic UV-safe material treatment, now including Stone, Foliage, and Grass;
- `validation_texture_batch_v1.json` — bounded first texture validation: exactly 6 Stone + 6 Foliage jobs;
- `validation_source_stager.py` — exact-filename resolver/hash/stager for that validation batch.

The legacy `forge.py` remains the implementation core and backward-compatible API surface, but its embedded historical prompt constants are **not current visual authority**. New planning should run through `forge_current.py`.

The texture contract translates the established character-side visual language into material rules rather than copying character identity, costume, palette, or props into environment textures.

Key texture principles:
- controlled saturation and local material color;
- clear authored light/mid/dark grouping;
- strong material separation;
- deliberate detail hierarchy;
- selective edge emphasis rather than uniform outlines;
- reduced high-frequency noise at HD-2D gameplay scale;
- graphic anime-stylized shape design rather than photoreal or soft-brushed finishes;
- preservation of alpha, animation registration, atlas structure, lighting-state relationships, and channel semantics.

## First texture-style validation

Do **not** bulk-convert the environment library yet.

The first texture pass is exactly 12 bounded source jobs:
- 6 Stone/environment-atlas representatives;
- 6 Foliage/Grass representatives.

Source filenames and required lighting/icon/state companions are fixed in `validation_texture_batch_v1.json`.

The extracted Map001–Map116 material remains license-unverified private/reference/prototyping material. The manifest does not change its provenance status.

Where the raw archive library is mounted:

```bash
python tools/asset_forge/validation_source_stager.py /path/to/raw/map_library \
  --stage-dir .asset_forge/texture_validation_sources
```

The stager fails closed on missing or ambiguous basenames, hashes every resolved source, validates declared sequence counts, preserves companions, and never modifies the raw library. Successful staging ends in:

`READY_FOR_ASSET_FORGE_PROCESSING`

After staging, process only the bounded candidates, build deterministic review evidence, then stop for Art Director + user review. **APPROVED does not mean LOCKED.**

## Main entry points

- `forge_current.py` — current inventory/classify/plan/provider/base-QA entrypoint with active texture contract injection.
- `forge.py` — legacy implementation core used by `forge_current.py`.
- `pipeline.py` — resumable/budget-safe atlas + animation processing.
- `ops.py` — budget, lighting propagation, atlas/alpha/animation QA.
- `material_style_engine.py` — deterministic UV-safe material-family processing.
- `prop_pack_pipeline.py` — one-command material-first glTF prop-family validation.
- `zip_intake_engine.py` — ZIP-native supplemental intake, metadata filtering, filename/grid metadata.
- `vfx_intake_engine.py` — VFX source-role, particle-pair and spritesheet/flipbook intake.
- `vfx_processing_engine.py` — fixed-grid split/repack, padding preservation, palette/transparency preservation and paired-particle validation.

## General image workflow

```bash
python tools/asset_forge/forge_current.py inventory /path/to/source_assets \
  --output .asset_forge/manifest.jsonl
python tools/asset_forge/forge_current.py plan .asset_forge/manifest.jsonl \
  --output .asset_forge/queue.jsonl
python tools/asset_forge/ops.py budget .asset_forge/queue.jsonl
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl --provider dry-run
```

Asset Forge has two distinct execution lanes:

1. **Deterministic material lane** — used where UV/pixel registration must remain exact; Stone/Foliage/Grass now have first-pass deterministic profiles in `material_style_engine.py`.
2. **Optional bounded provider lane** — `pipeline.py` may use the existing OpenAI provider when a task explicitly calls for a generative/edit pass, under hard call caps, atlas/animation propagation rules, and review gates.

Do not describe the entire Forge as “zero AI.” The deterministic lane is non-generative; the broader pipeline retains the existing optional bounded provider architecture.

Bounded provider example:

```bash
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl \
  --provider openai \
  --max-ai-calls 10 \
  --limit 20
```

## v0.9 VFX structure preservation

The verified CC0 Brackeys VFX bundle exposed source structures that ordinary texture handling must not flatten.

Forge preserves:
- filename-declared spritesheet/flipbook grids;
- frame order and cell registration;
- small transparent right/bottom canvas padding outside the declared active grid;
- palette-mode transparency metadata;
- particle color + alpha-mask pair registration;
- RGB fire flipbooks for additive/emissive testing rather than forced alpha invention.

Real-bundle QA established:
- **213** usable VFX images;
- **28** predrawn/flipbook grid sheets;
- **1,318** declared frames;
- **3** padded grid sheets handled without changing frame count;
- **92** matched particle color/alpha pairs;
- **0** unmatched color sprites;
- all 28 grid sheets split/repack with **0 pixel difference**.

B06 authority:
`docs/14_ART_AND_VISUALS/PRODUCTION/BENCHMARKS/B06_CC0_FIRE_LIGHT_EXECUTION_V1.md`

## Shared-material prop workflow

Across the verified 94-model Quaternius Fantasy Props MegaKit, the major shared BaseColor families reach:
- Metal — **60 models**;
- Furniture — **41 models**;
- Props — **39 models**;
- Cloth — **10 models**.

Furniture and Metal are B10-approved. Props and Cloth remain real-model candidates pending user review. Forge resolves actual glTF material bindings rather than relying on material-name heuristics and only changes Normal/ORM data when PBR QA requires it.

One-command prop validation:

```bash
python tools/asset_forge/prop_pack_pipeline.py \
  "asset_sources/third_party_cc0/Fantasy Props MegaKit[Standard].zip" \
  --models Barrel Chair_1 Lantern_Wall Workbench \
  --output-root .asset_forge/b10_prop_pilot
```

## Supplemental ZIP / VFX intake

New archives should be inventoried before extraction or conversion:

```bash
python tools/asset_forge/zip_intake_engine.py \
  /path/to/archive1.zip /path/to/archive2.zip \
  --hash-members \
  --output .asset_forge/zip_intake_hashed.json
```

VFX structural QA:

```bash
python tools/asset_forge/vfx_processing_engine.py \
  /path/to/brackeys_vfx_bundle.zip \
  --output .asset_forge/vfx_processing_manifest.json
```

## Provenance

Forge never overwrites source files.

License-unverified Map001–Map116 material and Supplemental Batch 1 remain license-unverified. Verified CC0 sources such as Quaternius and the Brackeys VFX bundle may be directly transformed and promoted after Diyse style/runtime review.

All work products remain under git-ignored `.asset_forge/` until deliberately promoted.

## Tests

```bash
python -m unittest discover -s tools/asset_forge/tests -p "test_*.py"
```

Coverage includes atlas/animation/lighting/budget/resume behavior, material-family styling, glTF routing, UV/PBR handling, real-model rendering, ZIP-native intake, VFX structure preservation, current texture-style contract injection, and exact bounded validation-source staging.

## Current production gates

- Texture Style v1 — **IMPLEMENTED CANDIDATE — 12-SOURCE VALIDATION REQUIRED**
- B01 — **STYLE-PASS APPROVED — GAMEPLAY TEST READY**
- B03 — **STYLE-PASS APPROVED — GAMEPLAY TEST READY**
- B06 — **SOURCE ANALYSIS COMPLETE — TECHNICAL STYLE PILOT READY**
- B10 — **STYLE-PASS APPROVED — GAMEPLAY/RUNTIME TEST READY**
- Props/Cloth shared families — **REAL-MODEL FAMILY CANDIDATE — USER REVIEW PENDING**
- Supplemental Texture Batch 1 — **INVENTORIED — PROVENANCE PENDING**
- Verified CC0 VFX Batch 2 — **INTAKE COMPLETE — STYLE/RUNTIME VALIDATION READY**

Immediate texture milestone:
1. resolve/stage the exact 12 Stone/Foliage jobs;
2. run deterministic first-pass texture candidates;
3. generate original-vs-processed + gameplay-scale review evidence;
4. Art Director reviews Diyse visual fit, material readability, color/value control and technical integrity;
5. user approves/reworks/rejects representative results;
6. only then decide whether a family is ready for wider conversion.

> Do not bulk-convert Master v5, Supplemental Batch 1, or the full VFX library merely because Forge can queue them. Provenance, bounded style gates, technical preservation, Art Director review and explicit user approval remain authoritative.

## Authority

Visual style: `docs/14_ART_AND_VISUALS/DIYSE_VISUAL_STYLE_CANON.md`  
Conversion rules: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`  
Forge routing: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_FORGE_AUTOMATION.md`  
Asset provenance/index: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/SUPPLEMENTAL_INTAKE_INDEX.md`
