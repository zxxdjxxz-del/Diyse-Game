# Diyse — Migration Validation Cleanup Record

**Date:** 2026-09-01  
**Purpose:** remove one-time repository/domain migration checklists from active authority surfaces after the subject-folder reorganization was completed, while preserving provenance through Git history.

## Active rule after this cleanup
- `00_MASTER_CONTROL` contains current cross-domain authority/navigation only.
- numbered domains contain current owner-domain authority.
- `90_WORKING` contains unresolved/reopened work only.
- `99_ARCHIVE` contains migration/provenance history only.
- migration snapshots do not remain active merely because many of their historical checks once passed.

## Master-control history removed from active control
The following files were completed reorganization records, not continuing authority:
- `docs/00_MASTER_CONTROL/FINAL_CONSOLIDATION_VALIDATION.md` — source blob `0f6baadeb7836ba4dfe5da4630330649fc673750`
- `docs/00_MASTER_CONTROL/MIGRATION_COMPLETION_STATUS.md` — source blob `b0ccba10e2e4236da90c5bfcd89d0655e113f18e`

Their exact prior contents remain recoverable in Git history.

## Domain migration validations removed from active domains
These files were migration-time completeness/checkpoint snapshots. Several now also contain retired terminology or superseded numeric/status statements, so keeping them beside current owner files created avoidable authority ambiguity.

- `01_CHARACTERS/MIGRATION_VALIDATION.md` — `9104988b038104d5229fc405564b5dbf9d144cc4`
- `02_STORY/MIGRATION_VALIDATION.md` — `882ae4c8cb12ff8124140436f4e4fe44327c5d33`
- `03_DIALOGUE/MIGRATION_VALIDATION.md` — `c3471c6b5d2970b9e48b82e3cdb7d6ae1e77eae7`
- `04_WORLD_AND_LORE/MIGRATION_VALIDATION.md` — `b4badd819d2d1a05f4b4cab0abf62a4d45ff7d48`
- `06_CLASSES_AND_ABILITIES/MIGRATION_VALIDATION.md` — `8989a61d4f67490b9ca490e780be356222dd08c5`
- `07_CARDS/MIGRATION_VALIDATION.md` — `d5fb6f1464bb839f021fc15f371440c4cfaad8fd`
- `08_ITEMS_AND_EQUIPMENT/MIGRATION_VALIDATION.md` — `dff4659b8bdbdb22641ab873db163118ca522081`
- `09_ENEMIES_AND_ENCOUNTERS/MIGRATION_VALIDATION.md` — `264827680cbb2cdc4bc51494e828b767ce9e0d4a`
- `10_PROGRESSION_AND_EXP/MIGRATION_VALIDATION.md` — `c327f535990d4d91cb17ced0bc42bd91a7b6f824`
- `11_QUESTS/MIGRATION_VALIDATION.md` — `63d28d6c89561667f725ede0e0dbe13afbc333c1`
- `13_UI_AND_IMPLEMENTATION/MIGRATION_VALIDATION.md` — `f7a0b70c4dc8a6d095298902c06d1b2b831bb0f5`
- `14_ART_AND_VISUALS/MIGRATION_VALIDATION.md` — `e0e1d015f64a2dc429c2f3496e50271852244046`
- `15_AUDIO_AND_MUSIC/MIGRATION_VALIDATION.md` — `32059c2787eb61ac8d97e287a7b5fd6b7d9a2fe7`
- `16_BALANCE_AND_TESTING/MIGRATION_VALIDATION.md` — `6bb70ac87016f3e4c26bd7a99e3f03c837b69804`

`05_BATTLE_SYSTEM` had no active `MIGRATION_VALIDATION.md` at this cleanup boundary.

## Deliberate exception — economy validation remains live
`docs/12_ECONOMY_AND_REWARDS/MIGRATION_VALIDATION.md` is **not** archived in this pass.

It has already evolved from a migration-only checklist into the current G economy certification covering:
- G terminology and scale;
- current Consumable/equipment pricing and resale;
- exact payout totals;
- mandatory/completionist calibration;
- chapter-by-chapter liquidity certification.

Until it is separately renamed/replaced by an equivalent current validation owner, it remains a live current-domain validation despite its legacy filename.

## Recovery rule
Do not recreate the removed migration snapshots in active domain roots. If historical detail is needed, use Git history and the source blob identifiers above. If a continuing validation is needed, author it as an explicitly current owner-domain validation rather than reviving a migration checklist.
