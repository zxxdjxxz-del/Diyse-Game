# Diyse Asset Forge

**Status:** **v0.9 VFX structure-preservation checkpoint**

Diyse Asset Forge automates conversion of the current asset library into the locked Diyse visual style while preserving source provenance, archive identity, atlas/grid registration, animation stability, paired masks, shared-material reuse, lighting families, technical QA, and explicit approval gates.

## Main entry points

- `forge.py` — inventory, classify, plan, provider access, base QA, deterministic review sheets.
- `pipeline.py` — resumable/budget-safe atlas + animation processing.
- `ops.py` — budget, lighting propagation, atlas/alpha/animation QA.
- `prop_pack_pipeline.py` — one-command material-first glTF prop-family validation.
- `zip_intake_engine.py` — ZIP-native supplemental intake, now including metadata filtering and filename-grid metadata.
- `vfx_intake_engine.py` — VFX-specific source-role, particle-pair and spritesheet/flipbook intake.
- `vfx_processing_engine.py` — fixed-grid split/repack, small trailing-padding preservation, palette/transparency preservation and paired-particle validation.

## v0.9 VFX structure preservation

The verified CC0 Brackeys VFX bundle exposed source structures that ordinary texture handling must not flatten.

Forge v0.9 therefore preserves:
- filename-declared spritesheet/flipbook grids;
- frame order and cell registration;
- small transparent right/bottom canvas padding outside the declared active grid;
- palette-mode transparency metadata;
- particle color + alpha-mask pair registration;
- RGB fire flipbooks for additive/emissive testing rather than forced alpha invention.

Real-bundle QA:
- **213** usable VFX images;
- **28** predrawn/flipbook grid sheets;
- **1,318** declared frames;
- **3** padded grid sheets handled without changing frame count;
- **92** matched particle color/alpha pairs;
- **0** unmatched color sprites;
- **1** alpha-only smoke variant;
- **all 28 grid sheets split/repack with 0 pixel difference**.

Padded source cases:
- `star_explosion_6x5.png` — 4 transparent bottom rows;
- `impact_white_6x4.png` — 1 transparent bottom row;
- `flame_02_15x4.tga` — 8 transparent right columns.

The declared grid remains authoritative; trailing padding remains canvas padding and is not treated as an extra frame.

B06 authority:
`docs/14_ART_AND_VISUALS/PRODUCTION/BENCHMARKS/B06_CC0_FIRE_LIGHT_EXECUTION_V1.md`

Verified VFX provenance:
`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`

## v0.8 supplemental ZIP intake

New texture/source batches should be inventoried before extraction or conversion:

```bash
python tools/asset_forge/zip_intake_engine.py \
  /path/to/archive1.zip /path/to/archive2.zip \
  --output .asset_forge/zip_intake.json
```

For authoritative member-level hashing:

```bash
python tools/asset_forge/zip_intake_engine.py \
  /path/to/archive1.zip /path/to/archive2.zip \
  --hash-members \
  --output .asset_forge/zip_intake_hashed.json
```

The intake layer records archive identity, member metadata, image dimensions/mode/alpha, path-aware category, sequence metadata, grid metadata, and duplicate groups without extracting source files into repository authority.

Supplemental Batch 1 remains:
> **INVENTORIED — PROVENANCE PENDING — FAMILY ROUTING READY**

Authority:
`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

## Shared-material prop workflow

Across the verified 94-model Quaternius Fantasy Props MegaKit, the main shared BaseColor families are used by:
- Metal — **60 models**;
- Furniture — **41 models**;
- Props — **39 models**;
- Cloth — **10 models**.

B10 proves Furniture + Metal. Props + Cloth have a broader real-model candidate pass.

Forge resolves the actual glTF chain:

`MATERIAL → baseColorTexture → TEXTURE → IMAGE URI → SHARED FAMILY`

`material_style_engine.py` supports UV-safe Furniture/wood, Metal, mixed Props, and Cloth treatments. PBR data is retained or rebalanced only when QA requires it.

## General image workflow

```bash
python tools/asset_forge/forge.py inventory /path/to/source_assets
python tools/asset_forge/forge.py plan .asset_forge/manifest.jsonl
python tools/asset_forge/ops.py budget .asset_forge/queue.jsonl
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl --provider dry-run
```

Bounded provider run:

```bash
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl \
  --provider openai \
  --max-ai-calls 10 \
  --limit 20
```

Resume:

```bash
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl \
  --provider openai \
  --max-ai-calls 20 \
  --resume
```

VFX structural QA:

```bash
python tools/asset_forge/vfx_processing_engine.py \
  /path/to/brackeys_vfx_bundle.zip \
  --output .asset_forge/vfx_processing_manifest.json
```

## One-command prop-family validation

```bash
python tools/asset_forge/prop_pack_pipeline.py \
  "asset_sources/third_party_cc0/Fantasy Props MegaKit[Standard].zip" \
  --models Barrel Chair_1 Lantern_Wall Workbench \
  --output-root .asset_forge/b10_prop_pilot
```

## Provenance

Forge never overwrites source files.

License-unverified Map001–Map116 material and Supplemental Batch 1 remain license-unverified. Verified CC0 sources such as Quaternius and the Brackeys VFX bundle may be directly transformed and promoted after Diyse style/runtime review.

All work products remain under git-ignored `.asset_forge/` until deliberately promoted.

## Tests

```bash
python -m unittest discover -s tools/asset_forge/tests -p "test_*.py"
```

Coverage includes atlas/animation/lighting/budget/resume behavior, shared 3D materials, UV/PBR handling, real glTF rendering, ZIP-native intake, VFX grid parsing, padded-grid reconstruction, palette transparency preservation and particle-pair validation.

## Current production gates

- B01 — **STYLE-PASS APPROVED — GAMEPLAY TEST READY**
- B03 — **STYLE-PASS APPROVED — GAMEPLAY TEST READY**
- B06 — **SOURCE ANALYSIS COMPLETE — TECHNICAL STYLE PILOT READY**
- B10 — **STYLE-PASS APPROVED — GAMEPLAY/RUNTIME TEST READY**
- Props/Cloth shared families — **REAL-MODEL FAMILY CANDIDATE — USER REVIEW PENDING**
- Supplemental Texture Batch 1 — **INVENTORIED — PROVENANCE PENDING**
- Verified CC0 VFX Batch 2 — **INTAKE COMPLETE — STYLE/RUNTIME VALIDATION READY**

The next B06 step is a bounded Diyse-style fire/light candidate using one open flame, one full fire body, one ring/ground-fire family, sparks and soft light/flare primitives. It must pass temporal, alpha/emission and runtime-scale tests before STYLE-PASS.

## Authority

Visual style: `docs/14_ART_AND_VISUALS/DIYSE_VISUAL_STYLE_CANON.md`  
Conversion rules: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`  
Forge routing: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_FORGE_AUTOMATION.md`  
Asset provenance/index: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/SUPPLEMENTAL_INTAKE_INDEX.md`
