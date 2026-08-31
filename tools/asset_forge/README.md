# Diyse Asset Forge

**Status:** **v0.8 supplemental ZIP-intake checkpoint**

Diyse Asset Forge automates conversion of the current asset library into the locked Diyse visual style while preserving source provenance, archive identity, atlas registration, animation stability, shared-material reuse, lighting families, technical QA, and explicit approval gates.

## Main entry points

- `forge.py` — inventory, classify, plan, provider access, base QA, deterministic review sheets.
- `pipeline.py` — resumable/budget-safe atlas + animation processing.
- `ops.py` — budget, lighting propagation, atlas/alpha/animation QA.
- `prop_pack_pipeline.py` — one-command material-first glTF prop-family validation.
- `zip_intake_engine.py` — inspect supplemental texture ZIPs without extraction; hash archives, classify internal paths, identify animations, and report duplicate groups.

## Safe-batch foundation

The general pipeline supports SHA-256 source identity, coordinate-locked atlas patching, animation-anchor + zero-call follower propagation, lighting-family propagation, hard AI-call caps, checkpoint/resume, seam/alpha/aspect/flicker QA, and deterministic review boards made from actual outputs.

## v0.8 supplemental ZIP intake

New texture/source batches should be inventoried before extraction or conversion:

```bash
python tools/asset_forge/zip_intake_engine.py \
  /path/to/archive1.zip /path/to/archive2.zip \
  --output .asset_forge/zip_intake.json
```

For authoritative member-level duplicate/provenance hashing:

```bash
python tools/asset_forge/zip_intake_engine.py \
  /path/to/archive1.zip /path/to/archive2.zip \
  --hash-members \
  --output .asset_forge/zip_intake_hashed.json
```

The intake layer records:
- archive SHA-256 and byte size;
- ZIP member count and uncompressed bytes;
- internal member path/size/CRC;
- optional member SHA-256;
- image dimensions/mode/alpha;
- path-aware material family;
- animation group/frame metadata;
- duplicate candidate/exact groups depending on hashing mode.

The engine intentionally does **not** treat upload as license approval and does not extract raw source files into repository authority.

First real supplemental intake authority:

`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

That batch contains six user-supplied archives, **4,607 file members / 4,606 PNGs**, approximately **1.42 GB ZIP size**, and only **7 SHA-confirmed exact duplicate pairs**. It remains pending provenance and is not merged into Asset Library Master v5.

## v0.7 shared-material prop workflow

Across the verified 94-model Quaternius Fantasy Props MegaKit, the main shared BaseColor families are used by:
- Metal — **60 models**;
- Furniture — **41 models**;
- Props — **39 models**;
- Cloth — **10 models**.

B10 proves Furniture + Metal. Props + Cloth now have their own broader real-model candidate pass.

### Data-driven material routing

Forge resolves actual glTF bindings:

`MATERIAL → baseColorTexture → TEXTURE → IMAGE URI → SHARED FAMILY`

This correctly handles non-obvious names such as:
- `MI_Trim_Props_Vertex` → Props;
- `MI_Banner` → Cloth.

The prop pipeline no longer depends on family words appearing in material names.

### `material_style_engine.py`

Supported deterministic UV-safe kinds:
- `wood` — Furniture;
- `metal` — Metal;
- `prop` — mixed Props atlas with hue/category preservation;
- `cloth` — soft fold/value treatment with minimal texture-space ink.

All treatments preserve exact texture dimensions and UV registration.

### PBR handling

`pbr_qa_engine.py` evaluates source Normal/ORM data before changes.

Current examples:
- B10 Furniture normal triggers automatic attenuation;
- Props source Normal/ORM remains usable for the first family pass;
- Cloth source Normal is restrained and its roughness is nearly fully matte, so it remains unchanged for the first family pass.

`model_render_engine.py` resolves ORM family from the actual BaseColor texture path, allowing Props/Cloth and renamed/exception materials to receive correct source PBR validation data.

### Real-model validation

B10 approved set:
- Barrel;
- Chair_1;
- Lantern_Wall;
- Workbench.

Broader Props/Cloth candidate set:
- Bottle_1;
- Book_5;
- Potion_1;
- Banner_1_Cloth;
- Bag;
- Bed_Twin1.

Both flows use real glTF assets, neutral/warm/cool validation, shared physical-scale previews, and deterministic review sheets.

## Install

```bash
python -m pip install -r tools/asset_forge/requirements.txt
```

Dependencies:
- Pillow
- NumPy
- OpenCV (headless)
- trimesh
- OpenAI Python SDK

Set `OPENAI_API_KEY` only in the environment. Never commit keys.

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

## One-command prop-family validation

B10:

```bash
python tools/asset_forge/prop_pack_pipeline.py \
  "asset_sources/third_party_cc0/Fantasy Props MegaKit[Standard].zip" \
  --models Barrel Chair_1 Lantern_Wall Workbench \
  --output-root .asset_forge/b10_prop_pilot
```

Props/Cloth family candidate:

```bash
python tools/asset_forge/prop_pack_pipeline.py \
  "asset_sources/third_party_cc0/Fantasy Props MegaKit[Standard].zip" \
  --models Bottle_1 Book_5 Potion_1 Banner_1_Cloth Bag Bed_Twin1 \
  --output-root .asset_forge/props_cloth_family
```

Outputs include required source dependencies, styled shared BaseColor trims, QA-triggered Normal candidates, PBR diagnostics, emissive metadata where applicable, neutral/warm/cool model renders, a deterministic review sheet, gameplay-scale preview, and manifest.

## Provenance

Forge never overwrites source files.

License-unverified Map001–Map116 material remains license-unverified after Forge treatment. User-supplied supplemental archives also remain license-unverified until evidence is recorded. Verified CC0 sources may be directly transformed and promoted after style/runtime review.

All work products remain under git-ignored `.asset_forge/` until deliberately promoted.

## Tests

```bash
python -m unittest discover -s tools/asset_forge/tests -p "test_*.py"
```

Coverage includes the atlas/animation/lighting/budget/resume foundation plus shared-material detection, actual glTF material-to-image routing, four-family material styling, hue preservation for Props/Cloth, UV occupancy, PBR flags/rebalance, emissive anchors, real glTF rendering, gameplay-scale validation, and ZIP-native supplemental intake/classification/duplicate handling.

## Current production gates

B10:
> **STYLE-PASS APPROVED — GAMEPLAY/RUNTIME TEST READY**

Authority:
`docs/14_ART_AND_VISUALS/PRODUCTION/BENCHMARKS/B10_STYLE_PASS_APPROVAL_V1.md`

Props/Cloth shared families:
> **REAL-MODEL FAMILY CANDIDATE — USER REVIEW PENDING**

Authority:
`docs/14_ART_AND_VISUALS/PRODUCTION/CC0_PROP_CLOTH_FAMILY_VALIDATION_CANDIDATE_V1.md`

Supplemental texture Batch 1:
> **INVENTORIED — PROVENANCE PENDING — FAMILY ROUTING READY**

Authority:
`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

The new batch materially expands Metal, Concrete, Brick, terrain, Wood, emission/light, Fire, ritual/mystic, Water, Glass, Marble and Foliage source families. It should be processed family-first after provenance/storage decisions, not file-by-file.

## Authority

Visual style: `docs/14_ART_AND_VISUALS/DIYSE_VISUAL_STYLE_CANON.md`  
Shared prop grammar: `docs/14_ART_AND_VISUALS/PRODUCTION/DIYSE_CC0_PROP_MATERIAL_GRAMMAR_V1.md`  
Conversion rules: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`  
Forge routing: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_FORGE_AUTOMATION.md`  
Asset provenance: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/README.md`
