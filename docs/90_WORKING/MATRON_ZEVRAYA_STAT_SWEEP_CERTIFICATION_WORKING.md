# Matron Zevraya — DiySim Stat Sweep Certification

**Status:** WORKING SIMULATION RESULT / NOT OWNER CANON / NOT APPROVED FOR MAIN  
**Branch:** `tooling/diysim-phase1`  
**Encounter owner remains:** `09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/MATRON_ZEVRAYA.md`

This report records the boss-local effective-stat sweep run after the Brood-response policy fix and selective Reservoir-plan certification. It does not alter owner canon.

## Fixed test frame
- Structure: **non-diluting Reservoir candidate**.
- Global direct-damage floor: **Power ×1.20**.
- Prepared benchmark inventory enabled.
- Mandatory line: **Lv24**.
- High-side line: **Lv28**.
- Competent dismantle line: **Brood → Armor**.
- Comparison line: **Rush**, with deployed Brood treated as an immediate finite hostile target.
- Effective-stat offset applies to ATK / MAG / DEF / Spirit / SPD only; HP / MP remain unchanged.

## 1,000-run intermediate sweep
Seed 109, competent Brood → Armor line.

| Zevraya effective-stat offset | Lv24 Win | Lv24 Any KO | Lv24 Wipe | Lv24 Ending HP | Lv24 Items | Lv24 Rounds |
|---:|---:|---:|---:|---:|---:|---:|
| +0 | 99.8% | 13.0% | 0.2% | 52.78% | 6.98 | 29.99 |
| +1 | 99.5% | 18.9% | 0.5% | 49.29% | 7.17 | 30.59 |
| +2 | 99.1% | 31.2% | 0.9% | 44.31% | 7.49 | 31.22 |
| +3 | 97.7% | 45.3% | 2.3% | 39.40% | 7.76 | 31.81 |
| +4 | 94.2% | 57.8% | 5.8% | 33.00% | 8.14 | 32.59 |

Screen read:
- +0 and +1 remain too forgiving for the mandatory boss line.
- +2 and +3 are the useful candidate band.
- +4 begins pushing competent prepared play into an unnecessarily wipe-heavy range.
- the previously tested +5 layer remains rejected as a clear overshoot.

## 2,000-run +2 / +3 certification
Seed 110.

| Player line | Offset | Strategy | Win | Any KO | Wipe | Mean rounds | Mean ending HP | Mean items | Mean ending MP |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| Lv24 mandatory | +2 | Brood → Armor | **98.85%** | **32.95%** | **1.15%** | 31.29 | 43.59% | 7.56 | 10.49% |
| Lv24 mandatory | +2 | Rush | **93.70%** | **54.10%** | **5.95%** | 32.87 | 34.38% | 8.25 | 8.84% |
| Lv24 mandatory | +3 | Brood → Armor | **97.05%** | **45.95%** | **2.90%** | 31.85 | 38.98% | 7.85 | 10.47% |
| Lv24 mandatory | +3 | Rush | **90.10%** | **67.15%** | **9.30%** | 33.65 | 28.59% | 8.59 | 8.84% |
| Lv28 high-side | +2 | Brood → Armor | **100%** | **0.20%** | **0%** | 24.52 | 59.93% | 4.58 | 6.16% |
| Lv28 high-side | +2 | Rush | **100%** | **0.90%** | **0%** | 25.92 | 57.42% | 5.37 | 6.10% |
| Lv28 high-side | +3 | Brood → Armor | **100%** | **0.30%** | **0%** | 25.02 | 59.03% | 4.90 | 6.08% |
| Lv28 high-side | +3 | Rush | **100%** | **1.70%** | **0%** | 26.45 | 56.15% | 5.71 | 6.06% |

## Certified working read
**+3 effective-stat levels is the preferred Zevraya working candidate.**

Why +3 beats +2 for the current boss goal:
- competent prepared Lv24 play is still reliably successful at **97.05% wins**, so the fight is not wipe-heavy;
- nearly half of competent runs contain a KO (**45.95%**), which gives the boss credible danger rather than mere attrition;
- the mechanic matters strongly: Brood → Armor reduces wipe incidence from **9.30% to 2.90%** and any-KO incidence from **67.15% to 45.95%** compared with Rush;
- Lv28 remains decisively safer at **100% wins / 0% wipes**, preserving strong mandatory-versus-high-side separation;
- +4 already raises competent Lv24 wipes to **5.8%** in the 1,000-run screen, so there is no evidence that a larger stat layer is needed;
- +5 remains rejected.

## Current DiySim working recommendation
Test and balance Matron Zevraya around:

> **non-diluting Reservoir structure + global Power ×1.20 + boss effective-stat level +3, with Brood → Armor as the competent selective dismantle line.**

This is a **DiySim working recommendation only**. Do not rewrite the owner encounter or merge this result to `main` until it is explicitly approved through normal change control.

## Validation
- Dedicated 2,000-run certification workflow: all 8 matrix cells completed successfully.
- Normal DiySim branch test gate after the certification workflow commit: **passed**.
- Hollow Watch regression, First Command Warden matrix, Zevraya sensitivity matrix, readiness report, and source-gap reporting all completed successfully in the normal branch gate.
