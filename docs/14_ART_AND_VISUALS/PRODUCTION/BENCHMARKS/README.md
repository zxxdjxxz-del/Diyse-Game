# Diyse — Visual Style Benchmark Execution Status

**Authority:** `../STYLE_BENCHMARK_SET_V1.md` + `B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md`  
**Style:** `../../DIYSE_VISUAL_STYLE_CANON.md`

This directory contains execution sheets and result notes for the visual-style benchmarks. B00 is now a required character-style prerequisite because the six permanent-party designs have not yet been redrawn in the newly locked seinen/chaotic-line rendering style. The original B01–B11 definitions remain controlled by `STYLE_BENCHMARK_SET_V1.md`; B00 is controlled by `B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md`.

| Benchmark | Subject | Status | Execution/result file |
|---|---|---|---|
| B00 | Permanent party / character style anchor | **REQUIRED — NEW-STYLE PARTY MASTERS NOT YET PRODUCED** | `B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md` |
| B01 | Stone / fortified exterior | **STYLE-PASS APPROVED — GAMEPLAY TEST READY / B00 CROSS-CHECK PENDING** | `B01_STONE_EXECUTION_V1.md`; `B01_STONE_STYLE_PASS_CANDIDATE_V1.md`; `B01_DIYSE_ORIGINAL_STONE_KIT_SPEC_V1.md`; `B01_GAMEPLAY_TEST_SCENE_SPEC_V1.md` |
| B02 | Rustic wood/interior | QUEUED | — |
| B03 | Tree / foliage silhouette | **STYLE-PASS APPROVED — GAMEPLAY TEST READY / B00 CROSS-CHECK PENDING** | `B03_FOLIAGE_EXECUTION_V1.md`; `B03_FOLIAGE_STYLE_STUDY_SPEC_V1.md`; `B03_FOLIAGE_STYLE_PASS_CANDIDATE_V1.md`; `B03_DIYSE_ORIGINAL_FOLIAGE_KIT_SPEC_V1.md`; `B03_GAMEPLAY_TEST_SCENE_SPEC_V1.md` |
| B04 | Animated vegetation | QUEUED | — |
| B05 | Water + splash | QUEUED | — |
| B06 | Fire / light emitter | **TECHNICAL PRESERVATION PROOF COMPLETE — ANIME STYLE PILOT REQUIRED AFTER B00 ANCHOR** | `B06_CC0_FIRE_LIGHT_EXECUTION_V1.md`; `B06_FLAME_STYLE_PASS_CANDIDATE_V1.md` |
| B07 | Cave / subterranean | QUEUED | — |
| B08 | High-status interior | QUEUED | — |
| B09 | Ritual / magic surface | QUEUED | — |
| B10 | Verified CC0 prop cluster | **STYLE-PASS APPROVED — GAMEPLAY/RUNTIME TEST READY / B00 CROSS-CHECK PENDING** | `B10_CC0_PROP_CLUSTER_EXECUTION_V1.md`; `B10_CC0_PROP_STYLE_STUDY_SPEC_V1.md`; `B10_DETERMINISTIC_MATERIAL_BASELINE_PILOT_V1.md`; `B10_REAL_PROP_REFINEMENT_CANDIDATE_V2.md`; `B10_STYLE_PASS_APPROVAL_V1.md` |
| B11 | Original Black Host wall/gate | QUEUED | — |

## Promotion states

`QUEUED → SOURCE ANALYSIS → STYLE STUDY → STYLE-PASS CANDIDATE → USER REVIEW → STYLE-PASS → GAMEPLAY TEST → ACCEPTED`

No benchmark is **ACCEPTED** until its visual result passes the benchmark authority and the active style canon at gameplay scale.

Generated-image labels are not authority by themselves. A benchmark only advances when repository text records the approved production state.

## B00 correction

The six permanent party members already have approved **design/appearance references**, but they do **not** yet have approved masters rendered in the newly locked **Seinen HD-2D Fantasy with Chaotic Variable Line Weight** style.

Those existing character approvals continue to control identity, face, age read, hair, body type, clothing, armor, equipment, palette, silhouette, and other character-specific design details. They must not be described as completed new-style character masters.

Because characters are intended to carry Diyse's strongest line identity, B00 is now the missing primary visual anchor. B01, B03, and B10 retain their existing within-family approvals, but final cross-game cohesion must be rechecked against B00 before those families can support a claim that the whole game has been visually unified.

B00 covers **Cyanis, Ilyra, Torren, Nimera, Vaelira, and Seyrik**. It does not pass until all six have approved high-resolution new-style masters, with battle- and field-scale derivative logic validated.

B01 has passed user style review and controls the provisional baseline for Diyse stone rendering. It still requires a representative Diyse-original modular gameplay/integration proof and later B00 cross-check before final `ACCEPTED` promotion.

B03 has passed user style review and controls the provisional baseline for Diyse foliage rendering. It still requires a representative Diyse-original tree-family gameplay/integration proof and later B00 cross-check before final `ACCEPTED` promotion. Its runtime gates are clean alpha under movement/scaling, player-vs-tree hierarchy, route readability, foreground/midground/background simplification, and neutral/warm/cool lighting stability.

B06 is grounded primarily in the verified-CC0 Brackeys VFX bundle. Asset Forge v0.9 confirms exact split/repack round-trips across the bundle's **28 grid sheets / 1,318 declared frames** when small source padding and palette transparency are preserved, and it detects **92 matched particle color/alpha pairs**.

The first deterministic `flame_01_16x4` pass is retained only as a **technical preservation proof**: it preserves source alpha exactly, keeps the original 16×4 / 64-frame registration, and passes temporal QA at **0.9884485553** luminance-rhythm correlation and **1.2963046945×** peak temporal amplification. User visual review rejected its art direction because it remained too painterly/material-filter-like and did not read strongly enough as Diyse's locked mature seinen anime style. Its former STYLE-PASS CANDIDATE promotion is retired.

The replacement B06 pilot must be judged after the B00 party anchor exists. Its target remains unmistakably anime/seinen fire VFX: large cel-like graphic flame masses, hand-drawn asymmetry, a deep ember/red → orange → gold → pale cream hierarchy, selective broken/tapered chaotic line accents at meaningful dark folds/overlaps, bright mostly-unoutlined cores, controlled HD-2D emissive spill, and strong field/battle readability. It must avoid both photoreal fire and cheap flat cel shading.

B10 v2 has passed user style review. The approved benchmark uses actual Quaternius glTF assets, a material-first shared Furniture + Metal workflow, quieter painterly wood, controlled roughness-aware metal separation, deterministic Furniture normal attenuation when QA requires it, model-space Lantern_Wall emitter data, and actual physical-scale previewing. B10 remains pending final Godot/runtime validation and later B00 cross-check before `ACCEPTED`.

The resulting shared-material authority is `../DIYSE_CC0_PROP_MATERIAL_GRAMMAR_V1.md`. Furniture and Metal are B10-approved. Props and Cloth are family-level candidates and require a broader real-model validation batch before receiving the same production-ready status.

A full dependency scan of all 94 glTF props found major shared BaseColor usage of: Metal **60 models**, Furniture **41**, Props **39**, and Cloth **10**. This supports converting the pack by shared material family before model-specific overrides.

The broader asset library must not enter bulk style conversion until B00 and the remaining benchmark set are coherent enough to define Diyse Visual Material Grammar v1.
