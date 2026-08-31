# Diyse — Asset Forge Automation

**Status:** ACTIVE AUTOMATION IMPLEMENTATION — v0.1 foundation  
**Tool:** `../../../tools/asset_forge/forge.py`  
**Style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Conversion authority:** `ASSET_STYLE_CONVERSION_PIPELINE.md`  
**Asset/provenance authority:** `ASSET_LIBRARY/README.md`

## Purpose

Diyse Asset Forge exists to automate repetitive asset-library conversion work while preserving the separation between:

- source/reference material;
- style-pass candidates;
- deterministic QA/review;
- explicitly approved Diyse-final assets.

The program is an **implementation tool**, not a new visual authority. If its generated output conflicts with the visual canon or the conversion pipeline, the generated output is rejected.

## Automated flow

`SOURCE → INVENTORY → CLASSIFY → PLAN → GENERATE/PRESERVE → QA → REVIEW SHEET → APPROVE/REDO → DIYSE-FINAL`

### Inventory

Records:
- source path;
- relative path;
- SHA-256;
- byte size;
- dimensions;
- image mode/alpha;
- visual category;
- animation-frame grouping;
- lighting-state grouping;
- selected treatment mode.

### Classification recipes

Current recipes include:
- stone;
- foliage;
- grass/vegetation;
- water;
- fire/emissive;
- wood;
- cave;
- ritual/magic;
- interior;
- props;
- generic fallback.

### Treatment modes

The Forge deliberately avoids one universal AI pass.

**Direct style edit**  
For isolated assets where full-image generation is reasonably safe.

**Atlas structure-preserving**  
For large/composite atlases where coordinate/tile registration matters. v0.1 does not independently hallucinate a replacement atlas.

**Animation anchor**  
Only a chosen anchor frame is eligible for direct style treatment by default. Remaining frames are reserved for structure-preserving propagation rather than independent generation.

**Effect structure-preserving**  
For effects where silhouette, cadence, registration, or transparency consistency matters.

## Deterministic review boards

Benchmark/review boards should no longer be requested as giant AI-generated infographics.

The Forge `sheet` command builds a review PNG directly from the real generated output files and exact metadata. This prevents:
- wrong benchmark subjects appearing;
- invented status labels;
- fabricated completion percentages;
- stale prior-benchmark visual carryover;
- generated typography becoming mistaken for project authority.

The image model creates **asset candidates**. Python creates the **review board**.

## QA foundation

v0.1 records/checks:
- output existence;
- dimensions;
- image mode;
- alpha presence;
- aspect-ratio drift;
- partial-alpha statistics for transparent assets.

Future QA should add:
- atlas seam checks;
- alpha-fringe detection;
- animation flicker/line-boil metrics;
- frame registration comparison;
- gameplay-scale previews;
- lighting-family consistency;
- duplicate/near-duplicate detection.

## Safety and provenance

Asset Forge never overwrites source assets.

License-unverified extracted source material retains that provenance after processing. An AI repaint or automated transformation does not relabel it as original/CC0.

The local `.asset_forge/` work area is git-ignored. This keeps manifests, private paths, generation candidates, QA data, and temporary review sheets out of repository authority until explicitly promoted.

## Current implementation status

Implemented and locally tested:
- inventory scanning;
- SHA-256 recording;
- alpha/dimension inspection;
- filename/category classification;
- animation-anchor planning;
- large-atlas safe routing;
- category prompt generation;
- dry-run planning;
- optional OpenAI image-edit provider;
- deterministic QA foundation;
- deterministic contact/review sheet generation.

Current automated tests cover:
- category classification;
- animation anchor vs propagation routing;
- large-atlas structure-preserving routing;
- review-sheet creation from actual output files.

## Next implementation milestone

**Asset Forge v0.2** should focus on the pieces required to process the full library economically and reliably:

1. atlas segmentation/repacking with coordinate preservation;
2. anchor-to-animation style propagation;
3. base-to-`ra`–`rf` lighting-family handling;
4. seam, fringe, flicker, and registration QA;
5. checkpoint/resume and failed-job retry;
6. category and generation-credit budgeting;
7. approve/reject/redo metadata;
8. production export into controlled `STYLE-PASS` and `DIYSE-FINAL` directories.
