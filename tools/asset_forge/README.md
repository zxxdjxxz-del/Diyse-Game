# Diyse Asset Forge

**Status:** v0.3 safe-batch foundation

Diyse Asset Forge is the automation layer for converting the current asset library into the locked Diyse visual style without manually processing or documenting thousands of assets.

## Components

### `forge.py` — inventory / plan / provider / base QA / review sheets

Handles:
- TGA/PNG/JPEG/WebP scanning;
- SHA-256 source identity;
- dimensions/mode/alpha;
- category classification;
- animation and lighting-family grouping;
- category-specific Diyse prompts;
- treatment selection;
- optional OpenAI image edits;
- base deterministic QA;
- review/contact sheets built from actual generated files.

### `pipeline.py` — v0.2 safe processor

Recommended processor after inventory/plan. It adds:
- exact-size output normalization;
- coordinate-locked atlas patching;
- overlap feathering/reconstruction;
- animation-anchor generation;
- deterministic non-anchor propagation;
- source-alpha preservation for animation sequences;
- zero extra image-generation calls for propagated frames.

### `atlas_engine.py`

Large atlases are split into fixed-coordinate overlapping patches. Patch dimensions cannot change; coordinates never move; overlap is feather-blended; source alpha may be restored. An identity pass is regression-tested to reconstruct a 1700×1300 atlas pixel-exactly.

### `animation_engine.py`

One approved/generated anchor learns a non-spatial style profile:
- channel/palette distribution;
- selective edge emphasis.

Later frames receive the profile using their own moving geometry. The anchor is preserved exactly and source alpha remains unchanged.

### `lighting_engine.py` — v0.3

Transfers each source lighting state's relative RGB change onto an approved styled base. This supports base + directional/alternate lighting families without independently restyling every state.

### `qa_engine.py` — v0.3

Adds fast technical regression gates for:
- new atlas seams introduced at patch boundaries;
- semi-transparent alpha-edge/fringe diagnostics;
- animation temporal/flicker regression.

Natural source edges are subtracted from atlas seam scoring so an authored wall edge is not mistaken for a processing seam merely because it intersects a patch boundary.

### `budget_engine.py` + `ops.py` — v0.3

Preflight estimates image-generation calls before processing:
- direct edit = 1 call;
- atlas = 1 call per coordinate patch;
- propagated animation frame = 0 new calls.

At default 768px patches / 96px overlap, a 2048×2048 atlas requires 9 patch calls.

`ops.py` also exposes lighting propagation and the v0.3 QA checks.

## Install

```bash
python -m pip install -r tools/asset_forge/requirements.txt
```

Dependencies:
- Pillow
- NumPy
- OpenAI Python SDK

Set `OPENAI_API_KEY` only in the environment. Never commit keys.

Optional model overrides:

```bash
export DIYSE_FORGE_REASONING_MODEL="gpt-5.6-terra"
export DIYSE_FORGE_IMAGE_MODEL="gpt-image-2"
```

## Recommended batch workflow

### 1. Inventory

```bash
python tools/asset_forge/forge.py inventory /path/to/source_assets
```

### 2. Plan

```bash
python tools/asset_forge/forge.py plan .asset_forge/manifest.jsonl
```

### 3. Budget before generation

```bash
python tools/asset_forge/ops.py budget .asset_forge/queue.jsonl
```

### 4. Dry-run the safe processor

```bash
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl --provider dry-run
```

### 5. Generate a bounded sample

```bash
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl \
  --provider openai \
  --limit 10
```

Do not begin with the whole library. Approve category behavior first, then expand batches.

### 6. Base QA

```bash
python tools/asset_forge/forge.py qa .asset_forge/results_v02.jsonl
```

### 7. Deterministic review sheet

```bash
python tools/asset_forge/forge.py sheet .asset_forge/results_v02.jsonl \
  --qa .asset_forge/qa.jsonl \
  --output .asset_forge/review_sheet.png
```

The image model never invents the board title, benchmark, status, or labels. Python assembles the board from real assets and exact metadata.

## Atlas tools

Plan coordinates before generation:

```bash
python tools/asset_forge/pipeline.py atlas-plan /path/to/atlas.tga \
  --tile 768 --overlap 96
```

After processing, score patch-boundary regression:

```bash
python tools/asset_forge/ops.py qa-atlas \
  /path/to/source_atlas.png \
  /path/to/styled_atlas.png \
  .asset_forge/atlas_plan.json
```

## Animation tools

Propagate an approved anchor:

```bash
python tools/asset_forge/pipeline.py animation-propagate \
  /path/to/styled_anchor.png \
  /path/to/frame_0.png /path/to/frame_1.png /path/to/frame_2.png \
  --anchor-index 0
```

Check temporal regression:

```bash
python tools/asset_forge/ops.py qa-animation \
  --source /path/to/source_0.png /path/to/source_1.png \
  --output /path/to/output_0.png /path/to/output_1.png
```

## Lighting-family tools

```bash
python tools/asset_forge/ops.py lighting \
  /path/to/source_base.png \
  /path/to/styled_base.png \
  --state ra=/path/to/source_ra.png \
  --state rb=/path/to/source_rb.png \
  --state rc=/path/to/source_rc.png
```

This keeps the approved style base while carrying source lighting direction/color behavior into each state.

## Alpha diagnostic

```bash
python tools/asset_forge/ops.py qa-alpha /path/to/transparent_asset.png
```

This is a review metric, not an automatic art rejection, because intentional dark ink at foliage/fire edges can be valid Diyse styling.

## Treatment modes

- `direct_style_edit` — isolated assets where full-image editing is reasonably safe.
- `atlas_structure_preserving` — coordinate-locked patch processing and reconstruction.
- `animation_anchor` — one generated/approved frame plus deterministic followers.
- `effect_structure_preserving` — effects where cadence/alpha/registration remain critical.

## Provenance

The Forge never overwrites source files.

License-unverified Map001–Map116 material stays license-unverified after any Forge treatment. Restyling does not make it original or CC0. Important final assets should still be rebuilt/originalized under the active conversion pipeline.

Verified CC0 assets may be directly transformed and promoted after style/runtime review.

All work products remain under git-ignored `.asset_forge/` until explicitly promoted.

## Tests

```bash
python -m unittest discover -s tools/asset_forge/tests -p "test_*.py"
```

Coverage includes:
- classification and planning;
- deterministic review sheets;
- pixel-exact atlas identity reconstruction;
- patch-dimension drift rejection;
- animation alpha preservation;
- exact anchor preservation;
- end-to-end fake-provider atlas + animation processing;
- lighting-state propagation;
- zero seam regression on identity output;
- flicker regression behavior;
- generation-call budgeting.

## Next milestone — v0.4

Still open:
1. checkpoint/resume and failed-job retry;
2. hard `--max-ai-calls` enforcement rather than estimation only;
3. automatic batch partitioning by category/family;
4. richer alpha-fringe detection using neighboring opaque pixels;
5. gameplay-scale preview generation;
6. lighting-family auto-discovery from the manifest;
7. approval/reject/redo metadata and controlled export;
8. semantic atlas-region assistance where reliable;
9. regional/faction originalization recipes;
10. full-loop QA reports and automatic review-package generation.

## Authority

Visual style: `docs/14_ART_AND_VISUALS/DIYSE_VISUAL_STYLE_CANON.md`  
Conversion rules: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`  
Forge routing: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_FORGE_AUTOMATION.md`  
Asset provenance: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/README.md`
