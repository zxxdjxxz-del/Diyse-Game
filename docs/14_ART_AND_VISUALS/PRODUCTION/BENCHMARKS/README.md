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
| B06 | Fire / light emitter | QUEUED | — |
| B07 | Cave / subterranean | QUEUED | — |
| B08 | High-status interior | QUEUED | — |
| B09 | Ritual / magic surface | QUEUED | — |
| B10 | Verified CC0 prop cluster | **SHARED-MATERIAL PILOT READY** | `B10_CC0_PROP_CLUSTER_EXECUTION_V1.md`; `B10_CC0_PROP_STYLE_STUDY_SPEC_V1.md` |
| B11 | Original Black Host wall/gate | QUEUED | — |

## Promotion states

`QUEUED → SOURCE ANALYSIS → STYLE STUDY → STYLE-PASS CANDIDATE → USER REVIEW → STYLE-PASS → GAMEPLAY TEST → ACCEPTED`

No benchmark is **ACCEPTED** until its visual result passes the benchmark authority and the active style canon at gameplay scale.

Generated-image labels are not authority by themselves. A benchmark only advances when repository text records the approved production state.

B01 has passed user style review and controls the provisional baseline for Diyse stone rendering. It still requires a representative Diyse-original modular gameplay/integration proof before final `ACCEPTED` promotion.

B03 has passed user style review and controls the provisional baseline for Diyse foliage rendering. It still requires a representative Diyse-original tree-family gameplay/integration proof before final `ACCEPTED` promotion. Its runtime gates are clean alpha under movement/scaling, player-vs-tree hierarchy, route readability, foreground/midground/background simplification, and neutral/warm/cool lighting stability.

B10 now uses the actual shared material architecture of the verified CC0 Quaternius Fantasy Props MegaKit. Barrel, Chair_1, and Workbench share Furniture + Metal trim sheets; Lantern_Wall uses Metal. The representative four-prop benchmark therefore reduces to **two BaseColor style targets**: `T_Trim_Furniture_BaseColor.png` and `T_Trim_Metal_BaseColor.png`. The first pilot preserves existing Normal/ORM maps, styles those two BaseColor trims, applies them to the four actual models, then validates gameplay readability and lantern emissive behavior. Shared-material analysis is implemented in `tools/asset_forge/shared_material_engine.py`.

The broader asset library must not enter bulk style conversion until the full benchmark set is coherent enough to define Diyse Visual Material Grammar v1.