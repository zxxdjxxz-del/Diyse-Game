# Diyse Asset Forge

**Status:** v0.4 resumable safe-batch foundation

Diyse Asset Forge automates conversion of the current asset library into the locked Diyse visual style while preserving source provenance, atlas registration, animation stability, lighting families, and explicit review gates.

## Components

### `forge.py` — inventory / plan / provider / base QA / review sheets

Handles source scanning, SHA-256 identity, dimensions/mode/alpha, category classification, animation and lighting-family grouping, category-specific Diyse prompts, treatment selection, optional OpenAI image edits, base deterministic QA, and review sheets built from actual generated files.

### `pipeline.py` — v0.4 recommended processor

Adds:
- exact-size generated-output normalization;
- coordinate-locked atlas patching;
- overlap feathering/reconstruction;
- animation-anchor generation;
- deterministic non-anchor animation propagation;
- source-alpha preservation for animation sequences;
- hard image-generation call caps;
- whole-atlas budget preflight so an atlas is never partially spent when insufficient calls remain;
- asset-level checkpointing;
- `--resume` reuse of successful prior outputs when source SHA still matches.

### `atlas_engine.py`

Large atlases are split into fixed-coordinate overlapping patches. Patch dimensions cannot change, coordinates never move, overlap is feather-blended, and source alpha may be restored. An identity regression test reconstructs a 1700×1300 atlas pixel-exactly.

### `animation_engine.py`

One approved/generated anchor learns a non-spatial style profile containing palette distribution and selective edge emphasis. Later frames receive the same style behavior using their own moving geometry. The anchor is preserved exactly; source alpha remains unchanged; propagated frames require zero additional image-generation calls.

### `lighting_engine.py`

Transfers each source lighting state's relative RGB change onto an approved styled base. This supports base + `ra`–`rf`-style directional/alternate lighting families without independently restyling every state.

### `qa_engine.py`

Adds technical regression gates for:
- new seams introduced at atlas patch boundaries;
- semi-transparent alpha-edge/fringe diagnostics;
- animation temporal/flicker regression.

Natural source edges are subtracted from atlas seam scoring so an authored object edge on a patch boundary is not automatically treated as a processing seam.

### `budget_engine.py` + `ops.py`

Preflight image-generation calls before work begins:
- direct style edit = 1 call;
- atlas = 1 call per coordinate patch;
- propagated animation frame = 0 new calls.

At the default 768px patch size / 96px overlap, a 2048×2048 atlas uses 9 patch calls.

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

## Recommended workflow

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

### 4. Dry-run

```bash
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl \
  --provider dry-run
```

### 5. Generate a bounded resumable sample

```bash
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl \
  --provider openai \
  --max-ai-calls 10 \
  --limit 20
```

`--max-ai-calls` is a hard cap, not an estimate. If an atlas needs more calls than remain, the atlas is marked `budget_blocked` before its first patch call.

If the run stops or a later batch needs to continue:

```bash
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl \
  --provider openai \
  --max-ai-calls 20 \
  --resume
```

Successful rows are reused only when their output still exists and, when available, the stored source SHA matches the current queue source SHA. Failed, blocked, or missing outputs remain eligible for retry.

Checkpointing is on by default and writes progress to the `--results` JSONL after completed assets.

### 6. Base QA

```bash
python tools/asset_forge/forge.py qa .asset_forge/results_v04.jsonl
```

### 7. Deterministic review sheet

```bash
python tools/asset_forge/forge.py sheet .asset_forge/results_v04.jsonl \
  --qa .asset_forge/qa.jsonl \
  --output .asset_forge/review_sheet.png
```

The image model never invents benchmark headings, statuses, or labels. Python assembles the board from real outputs and exact metadata.

## Atlas tools

Plan coordinates before generation:

```bash
python tools/asset_forge/pipeline.py atlas-plan /path/to/atlas.tga \
  --tile 768 --overlap 96
```

Score patch-boundary regression after processing:

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

## Alpha diagnostic

```bash
python tools/asset_forge/ops.py qa-alpha /path/to/transparent_asset.png
```

This is a review diagnostic rather than an automatic rejection because intentional dark line treatment at some edges can be valid Diyse art.

## Treatment modes

- `direct_style_edit` — isolated assets where full-image editing is reasonably safe.
- `atlas_structure_preserving` — coordinate-locked patch processing and reconstruction.
- `animation_anchor` — one generated/approved frame plus deterministic followers.
- `effect_structure_preserving` — effects where cadence/alpha/registration remain critical.

## Provenance

The Forge never overwrites source files.

License-unverified Map001–Map116 material remains license-unverified after any Forge treatment. Restyling does not make it original or CC0. Important final assets should still be rebuilt/originalized under the active conversion pipeline.

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
- generation-call budgeting;
- hard AI-call cap behavior;
- zero-call follower propagation after the call budget is exhausted;
- resume reuse of successful outputs;
- retry of a previously budget-blocked atlas.

## Next milestone — v0.5

Still open:
1. automatic batch partitioning by category/family and call budget;
2. lighting-family auto-discovery from the manifest;
3. automatic gameplay-scale preview generation;
4. richer alpha-fringe neighborhood analysis;
5. approval/reject/redo metadata and controlled export;
6. semantic atlas-region assistance where reliable;
7. regional/faction originalization recipes;
8. full-loop QA reports and automatic review-package generation;
9. retry/backoff policy for transient provider failures;
10. optional local/non-OpenAI stylization backends for lower-cost bulk passes.

## Authority

Visual style: `docs/14_ART_AND_VISUALS/DIYSE_VISUAL_STYLE_CANON.md`  
Conversion rules: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`  
Forge routing: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_FORGE_AUTOMATION.md`  
Asset provenance: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/README.md`
