# Diyse — Visual Style Benchmark Execution Status

**Authority:** `../STYLE_BENCHMARK_SET_V1.md` + `B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md`  
**Style:** `../../DIYSE_VISUAL_STYLE_CANON.md`

This directory contains execution sheets and result notes for the visual-style benchmarks. B00 is the required character-style prerequisite for cross-game visual validation.

| Benchmark | Subject | Status | Execution/result file |
|---|---|---|---|
| B00 | Permanent party / character style anchor | **IN PROGRESS — CYANIS + ILYRA APPROVED / 2 OF 6 LOCKED** | `B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md`; `CYANIS_CURRENT_VISUAL_LOCK.md`; `ILYRA_CURRENT_VISUAL_LOCK.md` |
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

No benchmark is **ACCEPTED** until its visual result passes the benchmark authority and active style canon at gameplay scale. Generated-image labels are not authority by themselves; repository text records production state.

## B00 current state

The permanent party covers **Cyanis, Ilyra, Torren, Nimera, Vaelira, and Seyrik**.

Cyanis and Ilyra now have approved B00 high-resolution masters. Their exact render fingerprints and current visual authorities are controlled by:
- `CYANIS_CURRENT_VISUAL_LOCK.md`
- `ILYRA_CURRENT_VISUAL_LOCK.md`

The remaining four party members still require new-style high-resolution masters. B00 does not pass until all six are approved and battle/field derivative logic is validated.

The active B00 target is **mature seinen HD-2D fantasy with chaotic variable line weight and graphic anime-stylized rendering**. “Painterly” is retired from the active art direction and must not be used as a target or approval criterion.

## Existing benchmark implications

B01, B03, and B10 retain their within-family approvals, but any earlier language or visual choices that depend on soft-brushed/painterly treatment must be rechecked against the revised graphic-anime authority before final `ACCEPTED` promotion.

B06 remains grounded primarily in the verified-CC0 Brackeys VFX bundle. Asset Forge v0.9 confirms exact split/repack round-trips across **28 grid sheets / 1,318 declared frames** and detects **92 matched particle color/alpha pairs**.

The first deterministic `flame_01_16x4` pass is retained only as a **technical preservation proof**: exact alpha, original 16×4 / 64-frame registration, luminance-rhythm correlation **0.9884485553**, peak temporal amplification **1.2963046945×**. Its visual treatment is rejected because it did not read strongly enough as Diyse’s graphic seinen/anime style.

The replacement B06 pilot must use large cel-like graphic flame masses, hand-drawn asymmetry, ember/red → orange → gold → pale cream hierarchy, selective broken/tapered line accents, bright mostly-unoutlined cores, controlled HD-2D emissive spill, and strong battle/field readability.

B10 remains pending final Godot/runtime validation and B00 cross-check. Shared-material authority remains `../DIYSE_CC0_PROP_MATERIAL_GRAMMAR_V1.md`; Furniture and Metal are approved within B10, while Props and Cloth require broader validation. The full 94-glTF dependency scan remains: Metal **60**, Furniture **41**, Props **39**, Cloth **10**.

The broader asset library must not enter bulk final-style conversion until B00 and the remaining benchmark set are coherent enough to define Diyse Visual Material Grammar v1 under the revised non-painterly style authority.
