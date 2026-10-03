# Encounter Runtime Content Boundary

This folder contains a mix of current implementation structure and **engineering/proof encounter data**. Executable data here does not override the owning encounter canon under `docs/09_ENEMIES_AND_ENCOUNTERS/`.

## Current authority

Use these owners before treating any runtime row as current:

- `docs/09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/`
- `docs/09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/`
- `docs/09_ENEMIES_AND_ENCOUNTERS/ORDINARY_ENEMIES/`
- authored/boss/Hunt owners in the same domain
- `docs/10_PROGRESSION_AND_EXP/` for final EXP/CEXP authority

## Current files

### `chapter_01_04_formations.gd`

This is an executable engineering formation catalog, **not a whole-file canon source**.

Known authority boundaries:

- Chapters 1–2 still defer to their current `docs/09` owners for identity, composition, placement, body caps, and any later correction.
- **Chapter 3 runtime rows are stale.** Current September 27 authority includes these explicit successor mappings: Judgment Frame → **Maul Construct**, Erasure Wisp → **Scriptshade**, Authority Lens → **Flash Drone**, and Archive Current → **Arcdrift**. Command Guard Frame, Command Ring Drone, Watch Sentry, Watch Ballista, Grand Inquisitor Frame, and Watch Captain Frame are retired from current Chapter 3 with no approved rename.
- Current Chapter 3 roster/formations are owned by:
  - `docs/09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/CHAPTER_03.md`
  - `docs/09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_03_FORMATIONS.md`
- **Chapter 4 runtime rows are historical/rework inputs only.** The ordinary-enemy roster and formation layer are explicitly rework-pending and must not be treated as final simply because these rows execute.

Do not silently update the executable catalog by guessing through open Chapter 3/4 formation gaps. Reconcile it only from current owning authority when the implementation pass is intentionally undertaken.

### Adjacent selector calibration — `game/exploration/encounter_balance.gd`

Executable engineering calibration only. Its chapter encounter counts, tier weights, EXP anchors, and ordinary-EXP pools include historical/provisional values and do not override current `docs/09` encounter authority or `docs/10` progression authority. In particular, the Chapter-4 19-encounter value belongs to the retired pre-redesign volume model.

The generic selector stack is not whole-campaign complete: this directory's executable formation catalog currently covers Chapters 1–4, balance profiles stop at Chapter 12, and the reusable area-tuning schema does not yet accept Chapter 13. Do not fabricate missing Chapter 5–13 runtime pools during cleanup; migrate them deliberately from current owner files.

### `proof_enemy_combat_data.gd`

Engineering proof stats only. Its HP/MP/Speed rows are not production raw-stat authority.

### `tuning/proof_field_greenhollow.tres`

Engineering-only field encounter tuning proof. It does not lock final encounter rate, traversal pacing, or production tuning.

## Implementation rule

When runtime encounter data conflicts with current `docs/09` authority:

1. current owning authority wins;
2. preserve proof data only as clearly labeled implementation evidence;
3. do not promote stale executable values into canon;
4. do not invent missing formations, weights, stats, or Chapter 4 roster decisions during cleanup.
