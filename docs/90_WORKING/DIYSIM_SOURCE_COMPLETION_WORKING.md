# DiySim Source-Completion Working Notes

**Status:** SOURCE/READINESS PASS CLOSED ON FEATURE BRANCH / WORKING COMPLETIONS NOT YET PROMOTED  
**Branch:** `tooling/diysim-phase1`

Purpose: keep simulator-readiness source completions visibly separated from values recovered from current owner/audit authority. Nothing in this file promotes a working completion to `main` or canon by itself.

## Exact values recovered from existing authority

- Crownless War Engine EVA = **0** — current Major Hunt recertification and Audit135 lineage.
- Worldscar Leviathan EVA = **0** — current owner explicitly says EVA0 is intentional; Audit135 lineage agrees.
- The Unfinished World EVA = **0** — recovered from Audit135 raw-stat lineage.
- Maevra — **Linebreaker Thrust: 165 Power / Physical / Neutral / 15% Defense penetration / 10 MP** — recovered from `16_BALANCE_AND_TESTING/BALANCE/MAEVRA_GUEST_COMBAT_REFERENCE.md`. This replaces the earlier simulator-side 175-Power inference; no inferred Linebreaker number remains necessary.

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
- state containers with individually headed actions are audited as separate actions rather than as one aggregate attack;
- Hollow Watch now loads its complete encounter package from repository authority, including support bodies, weighted state actions, threshold behavior, Seal reduction, and recovered Maevra Linebreaker data;
- repository-root discovery is cached for repeated Monte Carlo resolution without changing combat outcomes;
- exact v93 Lv2 mandatory and Lv3 high-side party snapshots are exposed through one shared certification runner.

## Closure evidence

Repo-wide readiness on the feature branch:
- **182 / 182** owner files ready;
- **602** direct-damage sections audited;
- **0 source gaps**;
- **0 parser gaps**;
- full DiySim test suite green before the final regression-gate addition, with the final gate itself now included in branch CI.

Hollow Watch current-canon regression evidence:

### Lv2 mandatory — optimized 20,000-run certification, seed 93
- win rate: **100%**;
- wipe rate: **0%**;
- any-KO rate: **0.005%** — 1 run in 20,000;
- mean rounds: **6.0152**;
- median / p10 / p90: **6 / 6 / 6**;
- mean remaining party HP: **67.344%**;
- mean remaining party MP: **39.7985%**;
- mean Ballista shots: **0**;
- Staggered exposure: **16.48%**.

This is structurally consistent with the v93 calibration anchor while reflecting later current-canon Ability-MP reductions; therefore the old v93 **6.28 mean-round** figure is historical evidence, not the exact current regression target.

### Side-by-side current-rule snapshot check — 2,000 runs each, seed 93
**Lv2 mandatory:**
- 100% wins / 0 KOs / 0 wipes;
- mean rounds **6.011**;
- remaining HP **67.667%**;
- remaining MP **39.431%**;
- Ballista shots **0**.

**Lv3 high-side:**
- 100% wins / 0 KOs / 0 wipes;
- mean rounds **5.9035**;
- remaining HP **72.671%**;
- remaining MP **44.374%**;
- Ballista shots **0**.

The higher-level body therefore preserves the intended direction: **faster clear and greater survivability** with identical current encounter rules and smart policy.

## Ongoing branch gate

Routine feature-branch CI now:
- runs the full DiySim test suite;
- requires repo-wide readiness to remain at **0 source gaps / 0 parser gaps**;
- runs seeded Hollow Watch Lv2/Lv3 regression samples;
- fails if the fight leaves its broad current-canon safety/pace envelope, if the Ballista begins firing on the smart line, or if the Lv3 high-side body loses its speed/survivability advantage over Lv2.

## Promotion boundary

The **source/readiness repair pass itself is closed** on `tooling/diysim-phase1`.

Still not promoted without explicit approval:
- Last Sentinel Base Hit completion;
- Major Hunt Confluence target-shape completions;
- Hollow Watch support EVA/SR/role completions;
- Hollow Watch explicit Walking-State Physical/Neutral identity wording;
- the simulator/tooling branch as a whole.

Do not merge these working completions or the tool into `main` solely because the readiness and regression gates are green.
