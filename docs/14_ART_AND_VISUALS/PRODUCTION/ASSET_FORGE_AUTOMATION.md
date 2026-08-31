# Diyse — Asset Forge Automation

**Status:** ACTIVE AUTOMATION IMPLEMENTATION — v0.2 atlas/animation foundation  
**Core tool:** `../../../tools/asset_forge/forge.py`  
**v0.2 processor:** `../../../tools/asset_forge/pipeline.py`  
**Style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Conversion authority:** `ASSET_STYLE_CONVERSION_PIPELINE.md`  
**Asset/provenance authority:** `ASSET_LIBRARY/README.md`

## Purpose

Diyse Asset Forge automates repetitive asset-library conversion while preserving the separation between source/reference material, style-pass candidates, deterministic QA/review, and explicitly approved Diyse-final assets.

The Forge is an **implementation tool**, not a visual authority. Output that conflicts with the visual canon or conversion pipeline is rejected.

## Automated flow

`SOURCE → INVENTORY → CLASSIFY → PLAN → STYLE/PROPAGATE → QA → DETERMINISTIC REVIEW → APPROVE/REDO → DIYSE-FINAL`

## v0.1 core

`forge.py` currently handles:
- source scanning;
- SHA-256 identity;
- dimensions/mode/alpha inspection;
- category classification;
- animation and lighting-family grouping;
- category-specific Diyse prompts;
- treatment selection;
- optional image-generation provider;
- deterministic QA foundation;
- deterministic review/contact sheets made from actual outputs.

## v0.2 atlas engine

`atlas_engine.py` adds coordinate-safe large-atlas processing.

Rules:
- atlases are split into fixed-coordinate overlapping patches;
- crop coordinates are recorded before processing;
- a backend is forbidden from changing patch dimensions;
- overlap regions are feather-blended during reconstruction;
- original alpha may be restored after RGB treatment;
- atlas dimensions and registration remain fixed.

The identity regression test reconstructs a synthetic **1700×1300** atlas through 12 overlapping patches with **zero pixel difference**.

This does not claim that arbitrary atlas semantics have been solved. It solves the more fundamental requirement: safe coordinate-preserving processing and reconstruction.

## v0.2 animation engine

`animation_engine.py` prevents the dangerous workflow of independently generating every animation frame.

One approved/generated anchor frame establishes a deterministic style profile containing:
- channel/palette distribution mapping;
- selective edge-emphasis behavior.

Later frames receive that profile using each frame's own moving structure. The system does **not** paste spatial details from the anchor onto later frames and does not spend separate image-generation calls on every propagated frame.

For animation sequences:
- exact frame dimensions are retained;
- source alpha is retained;
- the approved anchor is preserved exactly;
- non-anchor frames inherit consistent palette/edge behavior;
- random frame-specific AI detail is avoided.

This conservative approach is specifically intended to reduce flicker, shape drift, and alpha instability.

## v0.2 processing pipeline

`pipeline.py` is now the recommended processing path after `forge.py inventory` and `forge.py plan`.

It performs two passes:

1. direct assets, animation anchors, and atlas patches;
2. deterministic animation propagation after each anchor is available.

Large atlases use coordinate-safe patch generation; animation followers use deterministic propagation. Direct isolated assets may still use full image edits where appropriate.

## Deterministic review boards

Benchmark/review boards must not be giant AI-generated infographics.

The Forge `sheet` command builds review PNGs directly from real output files and exact metadata. This prevents:
- wrong benchmark subjects appearing;
- invented status labels;
- fabricated completion percentages;
- stale previous-benchmark visual carryover;
- generated typography becoming mistaken for authority.

The image model creates **asset candidates**. Python creates the **review board**.

## Current treatment modes

**Direct style edit** — isolated assets where a full image edit is reasonably safe.

**Atlas structure-preserving** — large/composite atlases handled by fixed-coordinate overlapping patches and exact reconstruction.

**Animation anchor** — one frame receives style treatment; later frames inherit the approved profile rather than being independently generated.

**Effect structure-preserving** — effects where silhouette, cadence, alpha, or registration is critical.

## QA status

Existing deterministic QA checks:
- output existence;
- dimensions;
- mode;
- alpha presence;
- aspect-ratio drift;
- partial-alpha statistics.

v0.2 regression coverage additionally verifies:
- pixel-exact identity atlas reconstruction;
- rejection when a backend changes patch dimensions;
- exact approved-anchor preservation;
- alpha preservation across propagated frames;
- end-to-end generated-anchor → propagated-frames → atlas-processing behavior using a fake provider.

Still needed:
- actual seam-difference scoring after styled atlas patches;
- alpha-fringe detection;
- full-loop flicker/line-boil metrics;
- gameplay-scale preview generation;
- lighting-family consistency tests.

## OpenAI provider note

Current OpenAI image-generation documentation supports edit actions through the Responses API, GPT-Image-2 image generation/edit workflows, transparent PNG output, and a broad range of valid image resolutions. The Forge still normalizes generated candidates to exact source registration where the technical asset requires it.

Model/provider details remain configuration rather than visual authority.

## Safety and provenance

Asset Forge never overwrites sources.

License-unverified extracted source material retains that provenance after processing. Restyling does not relabel it as original or CC0.

The local `.asset_forge/` work area is git-ignored so manifests, private paths, generation candidates, temporary patch data, QA outputs, and review sheets do not become repository authority automatically.

## Current implementation status

Implemented:
- inventory and hashing;
- category recipes;
- source-safe planning;
- optional image-edit provider;
- deterministic review sheets;
- coordinate-safe overlapping atlas engine;
- atlas patch manifest generation;
- animation anchor detection;
- deterministic animation style-profile learning;
- non-anchor frame propagation;
- exact-size normalization;
- source-alpha preservation for animation sequences;
- v0.2 orchestrated processing pipeline;
- regression tests for the above.

## Next milestone — v0.3

The next implementation pass should make full-library runs practical rather than merely safe:

1. base + `ra`–`rf` lighting-family propagation;
2. atlas seam-difference QA after actual styled patches;
3. alpha-fringe detection;
4. animation flicker/line-boil metrics;
5. automatic gameplay-scale previews;
6. checkpoint/resume and failed-job retry;
7. generation budget/category caps;
8. approve/reject/redo metadata;
9. controlled export into `STYLE-PASS` and `DIYSE-FINAL` destinations;
10. semantic atlas-region assistance where reliable without changing atlas coordinates.
