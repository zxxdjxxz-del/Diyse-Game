# Diyse — Visual Style Benchmark Execution Status

**Authority:** `../STYLE_BENCHMARK_SET_V1.md`  
**Style:** `../../DIYSE_VISUAL_STYLE_CANON.md`

This directory contains execution sheets and result notes for the eleven visual-style benchmarks. The benchmark definitions remain controlled by `STYLE_BENCHMARK_SET_V1.md`; this directory records actual production progress.

| Benchmark | Subject | Status | Execution/result file |
|---|---|---|---|
| B01 | Stone / fortified exterior | **STYLE-PASS APPROVED — GAMEPLAY TEST READY** | `B01_STONE_EXECUTION_V1.md`; `B01_STONE_STYLE_PASS_CANDIDATE_V1.md`; `B01_DIYSE_ORIGINAL_STONE_KIT_SPEC_V1.md`; `B01_GAMEPLAY_TEST_SCENE_SPEC_V1.md` |
| B02 | Rustic wood/interior | QUEUED | — |
| B03 | Tree / foliage silhouette | **STYLE-PASS APPROVED — GAMEPLAY TEST READY** | `B03_FOLIAGE_EXECUTION_V1.md`; `B03_FOLIAGE_STYLE_STUDY_SPEC_V1.md`; `B03_FOLIAGE_STYLE_PASS_CANDIDATE_V1.md`; `B03_DIYSE_ORIGINAL_FOLIAGE_KIT_SPEC_V1.md`; `B03_GAMEPLAY_TEST_SCENE_SPEC_V1.md` |
| B04 | Animated vegetation | QUEUED | — |
| B05 | Water + splash | QUEUED | — |
| B06 | Fire / light emitter | **STYLE-PASS CANDIDATE — USER REVIEW PENDING** | `B06_CC0_FIRE_LIGHT_EXECUTION_V1.md`; `B06_FLAME_STYLE_PASS_CANDIDATE_V1.md` |
| B07 | Cave / subterranean | QUEUED | — |
| B08 | High-status interior | QUEUED | — |
| B09 | Ritual / magic surface | QUEUED | — |
| B10 | Verified CC0 prop cluster | **STYLE-PASS APPROVED — GAMEPLAY/RUNTIME TEST READY** | `B10_CC0_PROP_CLUSTER_EXECUTION_V1.md`; `B10_CC0_PROP_STYLE_STUDY_SPEC_V1.md`; `B10_DETERMINISTIC_MATERIAL_BASELINE_PILOT_V1.md`; `B10_REAL_PROP_REFINEMENT_CANDIDATE_V2.md`; `B10_STYLE_PASS_APPROVAL_V1.md` |
| B11 | Original Black Host wall/gate | QUEUED | — |

## Promotion states

`QUEUED → SOURCE ANALYSIS → STYLE STUDY → STYLE-PASS CANDIDATE → USER REVIEW → STYLE-PASS → GAMEPLAY TEST → ACCEPTED`

No benchmark is **ACCEPTED** until its visual result passes the benchmark authority and the active style canon at gameplay scale.

Generated-image labels are not authority by themselves. A benchmark only advances when repository text records the approved production state.

B01 has passed user style review and controls the provisional baseline for Diyse stone rendering. It still requires a representative Diyse-original modular gameplay/integration proof before final `ACCEPTED` promotion.

B03 has passed user style review and controls the provisional baseline for Diyse foliage rendering. It still requires a representative Diyse-original tree-family gameplay/integration proof before final `ACCEPTED` promotion. Its runtime gates are clean alpha under movement/scaling, player-vs-tree hierarchy, route readability, foreground/midground/background simplification, and neutral/warm/cool lighting stability.

B06 is now grounded primarily in the verified-CC0 Brackeys VFX bundle. Asset Forge v0.9 confirms exact split/repack round-trips across the bundle's **28 grid sheets / 1,318 declared frames** when small source padding and palette transparency are preserved, and it detects **92 matched particle color/alpha pairs**.

The first real B06 style candidate now exists on `flame_01_16x4`: a deterministic 64-frame treatment that preserves source alpha exactly, keeps the original 16×4 registration, converts the photographic source into broader ember/orange/gold/cream masses, uses selective broken dark accents, and protects bright cores from universal outlining. Real-sheet temporal QA passes with **0.9884485553** luminance-rhythm correlation and **1.2963046945×** peak temporal amplification under the declared 1.35 cap. B06 is therefore at **STYLE-PASS CANDIDATE / USER REVIEW PENDING**, not yet STYLE-PASS.

B10 v2 has passed user style review. The approved benchmark uses actual Quaternius glTF assets, a material-first shared Furniture + Metal workflow, quieter painterly wood, controlled roughness-aware metal separation, deterministic Furniture normal attenuation when QA requires it, model-space Lantern_Wall emitter data, and actual physical-scale previewing. B10 remains pending final Godot/runtime validation before `ACCEPTED`.

The resulting shared-material authority is `../DIYSE_CC0_PROP_MATERIAL_GRAMMAR_V1.md`. Furniture and Metal are B10-approved. Props and Cloth are family-level candidates and require a broader real-model validation batch before receiving the same production-ready status.

A full dependency scan of all 94 glTF props found major shared BaseColor usage of: Metal **60 models**, Furniture **41**, Props **39**, and Cloth **10**. This supports converting the pack by shared material family before model-specific overrides.

The broader asset library must not enter bulk style conversion until the full benchmark set is coherent enough to define Diyse Visual Material Grammar v1.
