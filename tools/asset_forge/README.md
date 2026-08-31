# Diyse Asset Forge

**Status:** v0.1 foundation

Diyse Asset Forge is the automation layer for converting the existing asset library into the locked Diyse visual style without manually building giant benchmark boards for every source asset.

## What it automates

1. scans TGA/PNG/JPEG/WebP assets;
2. records SHA-256, dimensions, alpha, category, animation grouping, and lighting-state grouping;
3. classifies assets into Diyse production recipes;
4. generates category-specific style prompts;
5. chooses a treatment mode per asset;
6. optionally sends safe direct-edit candidates to an image-generation provider;
7. keeps large atlases and non-anchor animation frames structure-preserving by default;
8. writes outputs to a separate local work area;
9. runs deterministic QA such as aspect-ratio and alpha reporting;
10. builds deterministic review sheets from the **actual generated files**, not AI-generated infographics;
11. leaves final promotion to `DIYSE-FINAL` as an explicit review decision.

## Why treatment modes matter

The Forge does **not** independently AI-redraw everything.

- `direct_style_edit` — isolated trees, props, and other assets where a full image edit is reasonably safe.
- `atlas_structure_preserving` — large/composite atlases. v0.1 preserves layout rather than hallucinating new atlas registration.
- `animation_anchor` — one anchor frame receives the style target; later frames are not independently hallucinated because that causes flicker and shape drift.
- `effect_structure_preserving` — animated/effect categories where cadence and silhouette registration matter.

This is deliberate. A one-click independent generation pass over every frame would damage seams, transparency, animation consistency, and tile registration.

## Install

```bash
python -m pip install -r tools/asset_forge/requirements.txt
```

For OpenAI-backed image edits, set `OPENAI_API_KEY` in the environment. Never commit API keys.

Optional model overrides:

```bash
export DIYSE_FORGE_REASONING_MODEL="gpt-5.6-terra"
export DIYSE_FORGE_IMAGE_MODEL="gpt-image-2"
```

## Basic workflow

```bash
python tools/asset_forge/forge.py inventory /path/to/source_assets
python tools/asset_forge/forge.py plan .asset_forge/manifest.jsonl
python tools/asset_forge/forge.py process .asset_forge/queue.jsonl --provider dry-run
```

Review the queue before spending generation credits.

To generate a small sample:

```bash
python tools/asset_forge/forge.py process .asset_forge/queue.jsonl \
  --provider openai \
  --limit 10
```

Then run deterministic QA:

```bash
python tools/asset_forge/forge.py qa .asset_forge/results.jsonl
```

And build the review board from the real outputs:

```bash
python tools/asset_forge/forge.py sheet .asset_forge/results.jsonl \
  --qa .asset_forge/qa.jsonl \
  --output .asset_forge/review_sheet.png
```

This solves the benchmark-board failure mode we hit manually: the image model never writes the board labels or decides which benchmark appears. Python places the actual output thumbnails and exact metadata.

All default work products live under `.asset_forge/`, which remains local and untracked.

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

The recipes embed the active Diyse style direction: mature seinen HD-2D fantasy, painterly shape-first materials, chaotic variable line weight, strong silhouettes, controlled detail, and gameplay readability.

## Source safety

The Forge never overwrites source files.

The Map001–Map116 extracted material remains license-unverified private/reference material under current provenance authority. Running the Forge against that source does not change its provenance. Final important assets should still move toward Diyse-original replacements under the existing conversion pipeline.

Verified CC0 assets may be transformed directly and promoted after style/runtime review.

## What v0.1 does not pretend to solve

The hard production problems are intentionally not hidden:

- automatic semantic slicing/repacking of arbitrary 2048 atlases;
- perfectly consistent AI repaint propagation across long animation sequences;
- final seam validation for every custom atlas family;
- automatic artistic approval;
- region/faction originalization decisions.

Those become later Forge backends/modules rather than being faked with independent image generations.

## Planned v0.2 modules

1. `atlas` — tile/region segmentation and repacking while preserving coordinates;
2. `animation` — structure-preserving style propagation from an approved anchor frame;
3. `lighting` — base-to-`ra`–`rf` consistency handling;
4. `qa` — seam tests, alpha-fringe tests, animation-flicker metrics, and gameplay-scale previews;
5. `approval` — promote/reject/redo metadata without touching source files;
6. `resume` — checkpointed processing for the full library;
7. `batch_budget` — limits by category/credits so thousands of assets cannot accidentally be submitted at once.

## Tests

```bash
python tools/asset_forge/tests/test_forge.py
```

Current tests cover:
- category classification;
- animation-anchor queue behavior;
- large-atlas structure-preserving routing;
- deterministic review-sheet generation from real outputs.

## Authority

Visual style:

`docs/14_ART_AND_VISUALS/DIYSE_VISUAL_STYLE_CANON.md`

Conversion rules:

`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`

Asset inventory/provenance:

`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/README.md`
