# Diyse — Existing Automated Test Inventory
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


Repository checkpoint:
`3fd07e92eda04f31ba613a654b3b1b28071f44e6`

Current GDScript validation files discovered:
> **34**

## combat
- `tests/combat/validate_generated_encounter_battle_state.gd`
- `tests/combat/validate_round_combat.gd`

## dialogue
- `tests/dialogue/validate_authoring_schema.gd`
- `tests/dialogue/validate_c01.gd`
- `tests/dialogue/validate_c02.gd`
- `tests/dialogue/validate_chapter_00_continuity.gd`
- `tests/dialogue/validate_chapter_01_continuity.gd`
- `tests/dialogue/validate_chapter_01_resources.gd`
- `tests/dialogue/validate_chapter_02_continuity.gd`
- `tests/dialogue/validate_chapter_02_resources.gd`
- `tests/dialogue/validate_chapter_03_continuity.gd`
- `tests/dialogue/validate_chapter_03_resources.gd`
- `tests/dialogue/validate_runner_scene_resource.gd`
- `tests/dialogue/validate_s001.gd`
- `tests/dialogue/validate_s002.gd`
- `tests/dialogue/validate_s003.gd`
- `tests/dialogue/validate_s004.gd`
- `tests/dialogue/validate_s005.gd`
- `tests/dialogue/validate_s006.gd`

## encounters
- `tests/encounters/validate_area_encounter_tuning.gd`
- `tests/encounters/validate_audit98_encounters.gd`
- `tests/encounters/validate_field_encounter_controller.gd`
- `tests/encounters/validate_live_movement_encounter_proof.gd`
- `tests/encounters/validate_transient_random_encounter_loop.gd`

## equipment
- `tests/equipment/validate_kessara_relic_copy_service.gd`

## presentation
- `tests/presentation/validate_chapter_00_hd2d.gd`
- `tests/presentation/validate_chapter_01_hd2d.gd`
- `tests/presentation/validate_chapter_02_hd2d.gd`
- `tests/presentation/validate_chapter_03_hd2d.gd`
- `tests/presentation/validate_chapter_04_hd2d.gd`
- `tests/presentation/validate_hd2d_runtime.gd`

## save
- `tests/save/validate_save_load.gd`

## smoke
- `tests/smoke/validate_project.gd`

## visual
- `tests/visual/capture_field_proof.gd`



## Interpretation
These tests prove useful foundation coverage.

They do not all represent current final canon.

Several proof tests still encode stale:
- bearer-locked First Champion;
- proof screen assumptions;
- proof content.

Those tests must be reconciled before being treated as production release gates.
