# Diyse Asset Forge

**Status:** v0.2 atlas/animation foundation

Diyse Asset Forge is the automation layer for converting the current asset library into the locked Diyse visual style without manually generating or assembling thousands of benchmark assets.

## Current architecture

### `forge.py` — inventory, planning, provider, QA, review sheets

The v0.1 core:
1. scans TGA/PNG/JPEG/WebP assets;
2. records SHA-256, dimensions, alpha, category, animation grouping, and lighting-state grouping;
3. classifies assets into Diyse production recipes;
4. generates category-specific style prompts;
5. chooses treatment modes;
6. provides optional OpenAI-backed image edits;
7. writes outputs to a separate local work area;
8. runs deterministic QA;
9. builds deterministic review sheets from the **actual output files**, never AI-generated infographic boards.

### `pipeline.py` — recommended v0.2 processor

The v0.2 processor adds:
- coordinate-locked atlas patching;
- overlap feathering/reconstruction;
- exact-size output normalization;
- animation-anchor generation;
- deterministic style propagation to non-anchor frames;
- source-alpha preservation for animation sequences;
- no additional AI calls for propagated animation frames.

### `atlas_engine.py`

Large atlases are split into fixed-coordinate overlapping crops. A backend may restyle those crops, but:
- crop dimensions cannot change;
- atlas coordinates cannot move;
- overlapping regions are feather-blended;
- source alpha may be restored after treatment;
- an identity pass reconstructs the original atlas pixel-exactly.

This is safer than sending a whole atlas through an unconstrained redraw and hoping tile registration survives.

### `animation_engine.py`

Only an anchor frame needs an approved style edit. The engine learns:
- per-channel palette distribution;
- selective edge emphasis.

It reapplies those style characteristics to each later frame's **own moving structure**. It does not paste the anchor's spatial detail onto later frames and does not independently hallucinate every frame. Source alpha is preserved.

This is intentionally conservative: motion stability matters more than inventing unique painted detail on every frame.

## Install

```bash
python -m pip install -r tools/asset_forge/requirements.txt
```

Dependencies:
- Pillow
- NumPy
- OpenAI Python SDK

For OpenAI-backed edits, set `OPENAI_API_KEY` in the environment. Never commit API keys.

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

### 3. Dry-run v0.2

```bash
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl \
  --provider dry-run
```

### 4. Generate a bounded sample

```bash
python tools/asset_forge/pipeline.py process .asset_forge/queue.jsonl \
  --provider openai \
  --limit 10
```

Do not begin with the entire library. Approve category/style behavior first, then expand the batch size.

### 5. QA

```bash
python tools/asset_forge/forge.py qa .asset_forge/results_v02.jsonl
```

### 6. Deterministic review sheet

```bash
python tools/asset_forge/forge.py sheet .asset_forge/results_v02.jsonl \
  --qa .asset_forge/qa.jsonl \
  --output .asset_forge/review_sheet.png
```

The image model never writes benchmark headings, statuses, or labels. Python places exact metadata around the real outputs, preventing one benchmark/category from accidentally turning into another.

## Atlas-only tools

Write the coordinate plan without spending generation calls:

```bash
python tools/asset_forge/pipeline.py atlas-plan /path/to/atlas.tga \
  --tile 768 --overlap 96
```

The patch manifest records every crop coordinate before processing.

## Animation-only tools

After approving a styled anchor frame:

```bash
python tools/asset_forge/pipeline.py animation-propagate \
  /path/to/styled_anchor.png \
  /path/to/frame_0.png /path/to/frame_1.png /path/to/frame_2.png \
  --anchor-index 0
```

This writes the propagated frames plus `animation_style_profile.json`.

## Treatment modes

- `direct_style_edit` — isolated trees, props, and similar assets where a complete style edit is relatively safe.
- `atlas_structure_preserving` — large/composite atlases processed through coordinate-locked overlapping patches.
- `animation_anchor` — one frame receives the visual style target; later frames inherit a deterministic style profile.
- `effect_structure_preserving` — effects where cadence, alpha, and silhouette registration remain critical.

## Current category recipes

- stone
- foliage/tree
- grass/vegetation
- water
- fire/emissive
- wood
- cave
- ritual/magic
- interior
- prop
- generic

All recipes inherit the active direction: mature seinen HD-2D fantasy, painterly shape-first materials, chaotic variable line weight, strong silhouettes, controlled detail, and gameplay readability.

## Source and provenance safety

The Forge never overwrites source files.

Map001–Map116 extracted material remains license-unverified reference material under current provenance authority. A Forge output does not become rights-cleared merely because it has been restyled. Important final assets should still move toward Diyse-original replacement/originalization under the production conversion pipeline.

Verified CC0 assets may be transformed directly and promoted after style/runtime review.

All default work products live under `.asset_forge/`, which remains local and untracked.

## Tests

Run all Forge tests:

```bash
python -m unittest discover -s tools/asset_forge/tests -p "test_*.py"
```

Coverage now includes:
- category classification;
- animation-anchor queue routing;
- large-atlas routing;
- deterministic review-sheet generation;
- pixel-exact atlas identity reconstruction;
- rejection of patch-dimension drift;
- animation alpha preservation;
- exact approved-anchor preservation;
- end-to-end anchor → propagation → atlas processing through a fake provider.

## Still open for v0.3+

The Forge now has the safe mechanical foundation, but these remain intentionally open:
- semantic atlas region detection beyond coordinate patches;
- seam-difference scoring after real AI patch edits;
- animation flicker metrics across complete loops;
- base + `ra`–`rf` lighting-family propagation;
- checkpoint/resume for very large runs;
- category/budget limits based on expected generation cost;
- approval/reject/redo state management;
- automatic gameplay-scale preview generation;
- regional/faction originalization rules.

## Authority

Visual style:
`docs/14_ART_AND_VISUALS/DIYSE_VISUAL_STYLE_CANON.md`

Conversion rules:
`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`

Forge production routing:
`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_FORGE_AUTOMATION.md`

Asset inventory/provenance:
`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/README.md`
