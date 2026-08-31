# Diyse Asset Forge

**Status:** v0.6 prop-family validation checkpoint

Diyse Asset Forge automates conversion of the current asset library into the locked Diyse visual style while preserving source provenance, atlas registration, animation stability, shared-material reuse, lighting families, technical QA, and explicit visual approval gates.

## Main entry points

- `forge.py` — inventory, classify, plan, provider access, base QA, deterministic review sheets.
- `pipeline.py` — resumable/budget-safe atlas + animation processing.
- `ops.py` — budget, lighting propagation, atlas/alpha/animation QA operations.
- `prop_pack_pipeline.py` — one-command material-first glTF prop-family pilot.

## Safe-batch foundation

The general image pipeline already supports:
- SHA-256 source identity;
- category/treatment routing;
- coordinate-locked atlas patching and feathered reconstruction;
- animation anchor + deterministic zero-call follower propagation;
- base + alternate/directional lighting propagation;
- hard `--max-ai-calls` limits;
- whole-atlas budget preflight;
- checkpoint/resume;
- seam, alpha, aspect, and flicker diagnostics;
- deterministic review boards made from actual outputs.

## v0.6 material-first prop workflow

For 3D prop libraries, Forge analyzes shared material dependencies before doing art work.

The 94-model Quaternius Fantasy Props MegaKit demonstrates why: the main shared BaseColor families are used by Metal **60** models, Furniture **41**, Props **39**, and Cloth **10**. B10's four representative props reduce to only two BaseColor targets: Furniture + Metal.

### Components

`shared_material_engine.py`
- scans glTF material/image/buffer dependencies inside ZIPs;
- reports shared BaseColor usage by model;
- enables material-first rather than model-first conversion.

`material_style_engine.py`
- UV-safe zero-drift deterministic BaseColor treatment;
- painterly value grouping;
- sparse meaningful dark marks rather than universal edge extraction;
- quieter v2 wood line density;
- stronger controlled metal highlight/value separation.

`uv_usage_engine.py`
- rasterizes actual glTF UV triangles;
- measures which parts of shared atlases selected models use;
- supports future occupancy-aware AI patching.

`pbr_qa_engine.py`
- analyzes Normal/ORM intensity, roughness, metallic, and AO distributions;
- flags only maps that actually need review.

`normal_rebalance_engine.py`
- attenuates excessive tangent-normal X/Y strength while preserving dimensions/UV coordinates;
- B10 Furniture normal falls from about 25.2% of pixels above 0.5 XY strength to about 16.6% after the automatic 0.72 correction, with >0.75 relief reduced to 0%.

`model_render_engine.py`
- deterministic headless +Y-up glTF renderer;
- samples styled BaseColor plus source ORM;
- neutral/warm/cool lighting;
- restrained PBR-aware material separation;
- model-space emissive validation.

`emissive_anchor_engine.py`
- derives exportable model-space light metadata for source models that lack authored emissive data;
- currently used for Lantern_Wall.

`gameplay_preview_engine.py`
- scales props by real glTF extents;
- compares them beside a 1.75-unit measurement silhouette;
- prevents hero-close-up framing from hiding gameplay-scale readability problems.

`prop_pack_pipeline.py`
- runs shared-material analysis;
- extracts only required source files;
- creates styled BaseColor candidates;
- runs PBR QA and normal rebalance where flagged;
- exports emissive anchors;
- renders real models under three lighting modes;
- builds close-up review sheets;
- builds gameplay-scale integration previews;
- writes a manifest;
- currently does all of the deterministic B10 refinement with **0 image-generation calls**.

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

## One-command CC0 prop pilot

```bash
python tools/asset_forge/prop_pack_pipeline.py \
  "asset_sources/third_party_cc0/Fantasy Props MegaKit[Standard].zip" \
  --models Barrel Chair_1 Lantern_Wall Workbench \
  --output-root .asset_forge/b10_prop_pilot
```

Outputs include:
- extracted required source dependencies;
- styled shared BaseColor trims;
- any QA-triggered rebalanced Normal candidates;
- PBR diagnostics;
- emissive-anchor metadata;
- neutral/warm/cool real-model renders;
- deterministic review sheet;
- gameplay-scale preview;
- manifest.

## Atlas / animation / lighting tools

Atlas plan:

```bash
python tools/asset_forge/pipeline.py atlas-plan /path/to/atlas.tga --tile 768 --overlap 96
```

Atlas seam QA:

```bash
python tools/asset_forge/ops.py qa-atlas source.png styled.png .asset_forge/atlas_plan.json
```

Animation propagation:

```bash
python tools/asset_forge/pipeline.py animation-propagate \
  styled_anchor.png frame_0.png frame_1.png frame_2.png --anchor-index 0
```

Animation temporal QA:

```bash
python tools/asset_forge/ops.py qa-animation \
  --source source_0.png source_1.png \
  --output output_0.png output_1.png
```

Lighting propagation:

```bash
python tools/asset_forge/ops.py lighting \
  source_base.png styled_base.png \
  --state ra=source_ra.png --state rb=source_rb.png
```

## Provenance

Forge never overwrites source files.

License-unverified Map001–Map116 material remains license-unverified after Forge treatment. Restyling does not make it original or CC0. Important final assets still follow the active source-reference → Diyse-remake pipeline.

Verified CC0 assets may be directly transformed and promoted after style/runtime review.

All work products remain under git-ignored `.asset_forge/` until deliberately promoted.

## Tests

```bash
python -m unittest discover -s tools/asset_forge/tests -p "test_*.py"
```

Coverage includes:
- classification/planning;
- deterministic review sheets;
- pixel-exact atlas identity reconstruction;
- atlas patch dimension rejection;
- animation alpha/anchor preservation;
- fake-provider atlas/animation processing;
- lighting propagation;
- seam/flicker QA;
- budget caps/checkpoint/resume;
- shared material detection;
- UV occupancy;
- material size preservation;
- PBR flags;
- normal rebalance;
- model-space lantern emitter derivation;
- headless glTF validation rendering.

## Current production gate

B10 is currently:

> **VISUAL REFINEMENT CANDIDATE V2 — USER REVIEW PENDING**

See:
`docs/14_ART_AND_VISUALS/PRODUCTION/BENCHMARKS/B10_REAL_PROP_REFINEMENT_CANDIDATE_V2.md`

After B10 visual approval, the next pilot order is:
1. B04 real animated grass;
2. bounded Map086 atlas edit + seam QA;
3. one real base + lighting-state family;
4. family/category batch partitioning + approve/reject/export metadata;
5. then category-sized conversion batches.

## Authority

Visual style: `docs/14_ART_AND_VISUALS/DIYSE_VISUAL_STYLE_CANON.md`  
Conversion rules: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`  
Forge routing: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_FORGE_AUTOMATION.md`  
Asset provenance: `docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/README.md`
