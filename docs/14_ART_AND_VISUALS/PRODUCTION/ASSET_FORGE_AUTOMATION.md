# Diyse — Asset Forge Automation

**Status:** ACTIVE AUTOMATION IMPLEMENTATION — v0.4 resumable safe-batch foundation  
**Core:** `../../../tools/asset_forge/forge.py`  
**Processor:** `../../../tools/asset_forge/pipeline.py`  
**Operations:** `../../../tools/asset_forge/ops.py`  
**Style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Conversion authority:** `ASSET_STYLE_CONVERSION_PIPELINE.md`  
**Asset/provenance authority:** `ASSET_LIBRARY/README.md`

## Purpose

Asset Forge automates repetitive asset conversion while keeping source/reference material, generated style-pass candidates, deterministic QA/review, and explicitly approved Diyse-final assets separate.

It is an implementation tool, not visual authority. Generated output that conflicts with current visual canon or the conversion pipeline is rejected.

## Current automated flow

`SOURCE → INVENTORY → CLASSIFY → PLAN → BUDGET → STYLE/PROPAGATE → CHECKPOINT → QA → DETERMINISTIC REVIEW → APPROVE/REDO → DIYSE-FINAL`

## Core capabilities

### Inventory and planning

Records and routes:
- SHA-256 source identity;
- dimensions and alpha;
- category;
- animation grouping;
- lighting-family grouping;
- treatment mode;
- action queue;
- category-specific Diyse style prompt.

### Direct assets

Isolated assets may receive full style edits where technically safe. Generated candidates are normalized to exact source dimensions when registration matters.

### Coordinate-safe atlases

`atlas_engine.py`:
- splits large atlases into fixed-coordinate overlapping patches;
- forbids patch-size drift;
- never rearranges atlas coordinates;
- feather-blends overlaps;
- can restore source alpha;
- reconstructs identity input pixel-exactly in regression tests.

### Animation propagation

`animation_engine.py`:
- directly styles one anchor frame;
- learns non-spatial palette and edge behavior;
- propagates that behavior to each follower frame's own moving geometry;
- preserves source alpha;
- spends zero additional image-generation calls on follower frames.

### Lighting-family propagation

`lighting_engine.py` transfers the source lighting state's relative RGB behavior onto an approved styled base. This is intended for base + directional/alternate state families such as `ra`–`rf` without independently redrawing every state.

### Technical QA

`qa_engine.py` adds:
- atlas seam-regression scoring relative to the source;
- alpha-edge/fringe diagnostics;
- animation temporal/flicker regression.

The original `forge.py qa` still supplies basic output existence, dimensions, alpha, and aspect checks.

### Deterministic review sheets

The image model does not create benchmark infographics.

`forge.py sheet` builds review boards from the actual output images and exact metadata, preventing stale benchmark imagery, invented approval labels, fabricated completion percentages, and wrong-category carryover.

### Budget safety

`budget_engine.py` estimates image-generation calls before submission.

Rules:
- direct edit = 1 image-generation call;
- atlas = 1 call per patch;
- propagated animation follower = 0 new calls.

`pipeline.py --max-ai-calls N` is a **hard runtime cap**. If an atlas cannot finish within the remaining budget, it is marked `budget_blocked` before its first patch call.

### Checkpoint and resume

v0.4 checkpoints completed asset results by default.

`--resume` reuses successful outputs only when:
- the output still exists; and
- source SHA still matches when both old/new records contain a SHA.

Failed, blocked, missing, or changed-source rows are processed again.

This lets a large library run proceed in bounded batches without regenerating already successful work.

## Current treatment modes

**Direct style edit** — isolated assets where full-image editing is reasonably safe.

**Atlas structure-preserving** — coordinate-locked patch processing and reconstruction.

**Animation anchor** — one generated/approved frame plus deterministic followers.

**Effect structure-preserving** — effects where cadence, alpha, silhouette, or registration is critical.

## Provenance rule

Forge never overwrites source assets.

License-unverified extracted assets remain license-unverified after restyling. Automated transformation does not convert them into original or CC0 assets.

Verified CC0 sources may be directly transformed and promoted after style/runtime review.

All temporary Forge products live under git-ignored `.asset_forge/` until deliberately promoted.

## Regression coverage

Current tests cover:
- category classification and work routing;
- deterministic review-sheet creation;
- pixel-exact atlas identity reconstruction;
- rejection of patch dimension drift;
- exact anchor preservation;
- animation alpha preservation;
- end-to-end fake-provider atlas/animation processing;
- lighting-state propagation;
- zero seam regression on identity output;
- animation flicker-regression behavior;
- generation-call estimation;
- hard call-cap behavior;
- zero-call follower propagation after budget exhaustion;
- resume reuse of successful outputs;
- retry of previously budget-blocked atlases.

## Real-source pilot

`ASSET_FORGE_PILOT_VALIDATION_V1.md` records the first real source routing/preflight test.

Validated:
- Map086 2048×2048 → atlas structure-preserving → **9 default patch calls**;
- Map084 1024×1024 tree → foliage direct edit → **1 call**;
- Map084 128×128 icon tree → foliage direct edit → **1 call**;
- total pilot preflight → **11 calls**.

No generation calls were spent in that pilot; it tested real-source inventory, routing, and cost preflight.

## Next implementation/pilot milestone

Before full-library processing:

1. run a bounded real-provider B10 CC0 prop pilot;
2. run B04 real animated-grass anchor/propagation QA;
3. run a small real Map086 atlas edit and seam check;
4. run one real base + lighting-state family;
5. add automatic batch partitioning by family/category/call budget;
6. add gameplay-scale preview generation;
7. add approve/reject/redo metadata and controlled export;
8. add provider retry/backoff;
9. only then consider category-sized or whole-library execution.

> Do not submit the entire 3,214-file library to generation merely because v0.4 can technically queue it. Bounded real-output pilots remain the production gate.
