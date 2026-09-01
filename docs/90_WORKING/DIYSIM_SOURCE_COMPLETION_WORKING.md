# DiySim Source-Completion Working Notes

**Status:** WORKING / FEATURE-BRANCH ONLY / NOT OWNER PROMOTION  
**Branch:** `tooling/diysim-phase1`

Purpose: keep simulator-readiness source completions visibly separated from values recovered from current owner/audit authority. Nothing in this file promotes a working completion to `main` or canon by itself.

## Exact values recovered from existing authority

- Crownless War Engine EVA = **0** — current Major Hunt recertification and Audit135 lineage.
- Worldscar Leviathan EVA = **0** — current owner explicitly says EVA0 is intentional; Audit135 lineage agrees.
- The Unfinished World EVA = **0** — recovered from Audit135 raw-stat lineage.

These are restoration/synchronization corrections, not new tuning choices.

## Working completions that were not historically recovered

### Last Sentinel damaging Base Hit
Working branch value:
> **Base Hit 100** for every damaging Last Sentinel command.

Reason:
- current `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md` requires Prime commands to own an authored Base Hit;
- current/historical Last Sentinel command packages omitted the exact value;
- Audit122 defines approximately 100 as the standard reliable-action authoring band.

This is a working completion, **not a recovered historical number**. Hold the Line remains non-damaging and uses Base Hit N/A.

### Major Hunt current-plus-next Confluence target shape
Working branch target for:
- Worldscar Leviathan — **Confluence Spear**
- The Unfinished World — **Confluence Rupture**

is:
> **one party member**

Reason: both commands are two-hit focused Confluence attacks whose owner text had complete per-hit Power/Base Hit/element-cycle behavior but omitted an explicit target declaration. This is a working source completion, not a recovered Audit135 target line.

### Hollow Watch support targeting / role completion
Working branch values:
- Fortress Ballista — **EVA 0 / SR 10**; explicit **acting combatant** while functional.
- Watch Seal — **EVA 0 / SR 10**; explicit **passive target** with no independent ordinary turn and no direct damage.

These values were not recovered as exact historical support-object rows. They exist only to make the targetable support bodies complete for the simulator and remain subject to approval before any owner/main promotion.

### Hollow Watch Walking-State action identity
Working branch identity completion:
- Fortress Slam — **Physical / Neutral**
- Iron Pursuit — **Physical / Neutral**
- Wall-Shear Sweep — **Physical / Neutral**

The v93 true-battle evidence already resolves these through the Castellan physical direct-damage line; the migrated owner had retained their Power/Base Hit/target/status behavior but omitted the explicit formula/affinity wording in the Walking-State shorthand. This completion is recorded here rather than treated as independently recovered historical text.

## Parser/runtime closures completed in this pass

- generic cross-owner linking for support `Enables:` summaries now requires one unique complete action owner;
- conditional capability qualifiers such as `if inherited, Perfected Siphon` are normalized without fuzzy owner matching;
- explicit `Authority:` action references can be resolved against their named owner rather than requiring duplicate local action data;
- current-element + next-element Confluence commands now have a repo-backed two-hit runtime with per-hit elements/status checks and a command-wide newly-inflicted-status cap;
- partial stat tables preserve authored fields instead of discarding the whole entity because another field is absent;
- state containers with individually headed actions are audited as separate actions rather than as one aggregate attack.

## Remaining gate for this source-completion pass

- full feature-branch test suite must be green after the final Hollow Watch/reference changes;
- repo-wide simulation readiness must report **0 source gaps / 0 parser gaps** before this pass is considered complete;
- no working completion in this file is promoted to `main` without explicit approval.
