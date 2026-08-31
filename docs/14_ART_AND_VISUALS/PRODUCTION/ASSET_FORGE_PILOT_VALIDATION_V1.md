# Diyse — Asset Forge Pilot Validation v1

**Status:** PASS — real-sample routing/preflight validation  
**Forge checkpoint:** v0.4  
**Date:** 2026-08-31

## Purpose

Validate the actual Forge inventory → plan → budget flow against real extracted Diyse benchmark samples before pointing the program at the full asset library.

This pilot did **not** spend image-generation calls. It validated classification, treatment routing, dimensions, and generation-call preflight.

## Real samples tested

### Map086 stone atlas

Local pilot source normalized as:
`gt_0_map086_map_color.png`

Observed:
- dimensions: **2048×2048**;
- category: `atlas`;
- treatment: `atlas_structure_preserving`;
- queue action: `structure_preserving_pass`;
- default 768px tile / 96px overlap estimate: **9 image-generation patch calls**.

Result:
> **PASS — routed through the coordinate-safe atlas engine rather than a single unconstrained direct redraw.**

### Map084 full tree sheet

Source:
`gt_1_map084_tree_color.png`

Observed:
- dimensions: **1024×1024**;
- category: `foliage`;
- treatment: `direct_style_edit`;
- queue action: `ai_style_edit`;
- estimated calls: **1**.

Result:
> **PASS — routed as isolated foliage rather than atlas/stone/effect processing.**

### Map084 icon tree

Source:
`gt_4_map084_icon_tree_color.png`

Observed:
- dimensions: **128×128**;
- category: `foliage`;
- treatment: `direct_style_edit`;
- queue action: `ai_style_edit`;
- estimated calls: **1**.

Result:
> **PASS — retained in the foliage family while remaining an independent compact asset.**

## Pilot totals

Assets: **3**

Category routing:
- atlas: **1**;
- foliage: **2**.

Treatment routing:
- atlas structure-preserving: **1**;
- direct style edit: **2**.

Estimated image-generation calls at default atlas settings:
- Map086 atlas patches: **9**;
- Map084 full tree: **1**;
- Map084 icon tree: **1**;
- **total: 11**.

## What this proves

The current pipeline successfully distinguishes a large composite atlas from isolated foliage assets using real source files and produces an actionable cost preflight before generation.

It also confirms why hard call caps matter: a single 2048² atlas can cost more generation calls than several isolated assets, so whole-library processing must be family-aware and budget-aware.

## What this does not prove

This pilot does not yet certify:
- visual quality of real provider outputs;
- seam quality after real AI atlas patch edits;
- animation propagation on a real multi-frame sequence;
- lighting-state propagation on a real `base + ra–rf` family;
- full-library runtime or total expected cost.

Those require the next bounded production pilots.

## Next pilot order

1. **B10 CC0 prop cluster** — clean-provenance direct-edit pilot.
2. **B04 animated grass** — real anchor + deterministic follower propagation.
3. **B01 Map086 atlas** — small-budget real atlas edit with seam QA.
4. **one real lighting family** — styled base + `ra–rf` propagation.
5. only then expand to category-sized batches.

## Decision

**Asset Forge v0.4 passes its first real-source routing and budget-preflight validation.**

The program remains in bounded-pilot mode. Do not submit the full 3,214-file library to generation until the real provider-output pilots above pass their technical and visual gates.
