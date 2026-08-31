# Diyse — B10 CC0 Prop Style-Pass Approval v1

**Benchmark:** B10 — Verified CC0 Prop Cluster  
**Status:** **STYLE-PASS APPROVED — GAMEPLAY/RUNTIME TEST READY**  
**Approved candidate:** `B10_REAL_PROP_REFINEMENT_CANDIDATE_V2.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`

## Approval

The B10 v2 real-prop treatment is approved as the active Diyse style direction for the verified CC0 prop benchmark.

This approval promotes the benchmark from:

`VISUAL REFINEMENT CANDIDATE V2 → USER REVIEW`

to:

`STYLE-PASS APPROVED → GAMEPLAY/RUNTIME TEST READY`

It does **not** mark B10 final `ACCEPTED`; final acceptance still requires representative runtime validation in the actual game renderer.

## Approved visual/material decisions

### Furniture / wood
- broad painterly value planes dominate over grain;
- wood keeps readable directionality without dense realistic pore/noise;
- dark line influence is sparse and concentrated at construction seams, deep overlaps, damage and selected large grain accents;
- tiny edge fragments are suppressed rather than promoted into ink;
- the same Furniture family may serve barrels, chairs, benches, work surfaces and related props with controlled local variation.

### Metal
- cool/neutral painterly planes remain the base;
- material separation is stronger than wood through controlled value contrast and restrained roughness-aware highlights;
- dark accents concentrate at joints, recessed construction, silhouette turns and contact points;
- metal is not rendered as mirror-realistic, chrome-like or surrounded by a universal toon outline.

### Normal / ORM handling
- source PBR data is retained unless QA identifies a specific problem;
- Furniture normal relief may be deterministically attenuated after `strong_normal_review` without changing UV registration;
- current B10 Furniture correction uses 0.72 X/Y strength and removes the extreme >0.75 XY relief population;
- current Furniture and Metal ORM maps remain valid as the working baseline because their roughness distributions are compatible with the approved treatment.

### Emissive prop handling
- emissive behavior is authored as data, not painted into every lighting state;
- Lantern_Wall uses exportable model-space emitter metadata derived from the real model geometry;
- the bright core stays relatively line-free;
- surrounding structure may carry the stronger dark metal accents;
- warm spill and bloom remain restrained and runtime-controlled.

### Scale/readability
- the four representative models remain recognizable at shared physical scale;
- prop-detail hierarchy stays subordinate to player/route readability unless a prop is intentionally interactive;
- close-up beauty renders never substitute for gameplay-scale validation.

## Shared-material production decision

B10 confirms the **material-first** workflow for clean-provenance 3D prop libraries:

`SHARED MATERIAL FAMILY → STYLE / PBR QA → REAL MODEL RENDERS → GAMEPLAY SCALE → RUNTIME`

Do not treat every model as a separate texture-authoring job when the source library already shares trim atlases.

For the Quaternius 94-model pack, current dependency analysis finds these major BaseColor families:
- Metal — 60 models;
- Furniture — 41 models;
- Props — 39 models;
- Cloth — 10 models.

Furniture and Metal are approved by B10. Props and Cloth enter family-level validation under `DIYSE_CC0_PROP_MATERIAL_GRAMMAR_V1.md` before they are treated as equally proven.

## Runtime gate before final ACCEPTED

B10 may become final `ACCEPTED` only after a representative Godot/runtime scene verifies:
- normal/roughness response under actual project lighting;
- Lantern_Wall emitter/light/bloom integration;
- field-scale readability and absence of shimmer;
- no universal outline artifact;
- consistent appearance beside approved Diyse environment materials;
- acceptable performance for repeated prop use.

Until that runtime gate passes, the correct benchmark status is:

> **STYLE-PASS APPROVED — GAMEPLAY/RUNTIME TEST READY**
