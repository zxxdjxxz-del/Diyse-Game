# Matron Zevraya — True-Battle Snapshot Working Candidate

**Status:** **WORKING SIMULATION CANDIDATE / NOT OWNER CANON / NOT APPROVED FOR MAIN**  
**Encounter owner remains:** `09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/MATRON_ZEVRAYA.md`  
**Purpose:** give DiySim an explicit, reproducible Chapter-6 prepared-play snapshot for mandatory versus high-side testing without hiding inventory or policy assumptions in code.

This file does **not** change Zevraya's owner bodies, action Powers, Reservoir behavior, campaign CEXP, equipment availability, or permanent economy rules.

## Fixed v105 comparison frame
- Mandatory comparison body: **Lv24**.
- High-side comparison body: **Lv28**.
- Active four: **Cyanis / Ilyra / Torren / Vaelira**.
- Same ordinary equipment on both level lines:
  - Cyanis — Deepforge Blade / Caeloran Plate / Yahtrean Shield;
  - Ilyra — Crucible Wardrod / Warden Fieldmail / Warding Focus;
  - Torren — Command War Bow / Annex Guard Mail;
  - Vaelira — Arcanist Staff / Green Arcanist Garb.
- No Relic/Legacy advantage.
- No Cards or Prime in the isolation comparison.
- Full HP / full MP boss-isolation start.

## Learned Base-Class package
The Chapter-6 CEXP stream is already sufficient for this active four to use the **CL9-era Base-Class package** by the Zevraya encounter:
- Cyanis — Crest Knight through CL9;
- Ilyra — Blue Warden through CL9;
- Torren — War Archer through CL9;
- Vaelira — Green Arcanist through CL9.

This candidate does not require an exact point estimate of each character's pre-boss cumulative CEXP because no additional Base-Class Ability unlock sits between CL9 and the encounter-relevant next threshold.

## Prepared consumable candidate
Normal-stock authority by Chapter 6 supports every item below. The test intentionally uses a **finite carried package**, despite unlimited shop stock after unlock.

| Consumable | Count | Intended role |
|---|---:|---|
| **Restorative Salve** | **3** | emergency single-target HP recovery |
| **Deepflow Tonic** | **2** | restore 80 MP when Ilyra or another key actor is resource-bound |
| **Trauma Remedy** | **2** | remove Bleed from Zevraya / Brood pressure |
| **Stability Remedy** | **2** | remove Freeze / Stun / Staggered |
| **Rousing Salts** | **2** | finite revival reserve |

Why this package:
- all five are reliably available by Chapter 6 under `12_ECONOMY_AND_REWARDS/CONSUMABLE_STOCK_PROGRESSION.md`;
- it expands naturally from the earlier prepared true-battle snapshots without using rare/reward-only recovery;
- Greater Rousing Salts is legal in Chapter 6 but is deliberately omitted from the first candidate so the baseline does not overstate preparation quality;
- General Remedy is legal but redundant for this encounter's authored Bleed/control profile when Trauma and Stability Remedies are carried.

This inventory is a **benchmark loadout**, not a mandatory free grant and not a permanent economy lock.

## Player-policy boundary
Two visible-state strategies are required:

### Rush
- prioritize the current Zevraya body;
- do not deliberately dismantle Reservoirs before Form I ends;
- if Crimson/Perfected Brood is deployed, treat that live Brood body as an immediate finite hostile priority until it is destroyed, then return to Zevraya;
- use healing, cleansing, revival, and MP items when survival/resource pressure warrants them.

The explicit Brood rule is part of the deterministic simulator policy. The earlier implementation that could leave a deployed Brood alive for ~20–25 actions was a policy bug and is retired.

### Dismantle
- spend early actions removing the functional Reservoirs that matter to the chosen structural model;
- default full-dismantle order for the first certification pass is **Brood → Conduction → Sustenance → Armor**;
- then return to Zevraya;
- respond to any deployed Brood body as a normal finite hostile target;
- use the same healing/item thresholds as Rush.

Shared competent-play rules:
- Ilyra prioritizes KO recovery, actionable control cleanup, party healing, and emergency single-target healing before offense;
- Torren establishes Hunter's Measure on each fresh Zevraya body and uses strongest legal measured single-target offense while MP permits;
- Vaelira uses a legal chosen standard element; the deterministic simulator choice is Earth unless encounter affinity authority says otherwise;
- Cyanis uses current Crest Knight offense appropriate to a single major target;
- no future enemy action knowledge;
- no Cards / Prime in this isolation candidate.

## Structural modes to compare
### Owner structure
Use `MATRON_ZEVRAYA.md` exactly:
- Adaptive Plating and Warbody Plating are selected non-damage boss actions;
- Controlled Reconstruction consumes the selected action when chosen;
- current Reservoir inheritance rules remain intact.

### v104 non-diluting candidate
Use the already documented working structural candidate from `CH6_ENEMY_POWER_20_PERCENT_SENSITIVITY_v104.md`:
- Armor Reservoir gives continuous functional **Defense +15% / Spirit +15%** while alive instead of consuming a selected boss action;
- surviving Armor carries that branch into Form II;
- Controlled Reconstruction becomes its bounded conditional passive trigger and does not replace a selected attack;
- for this reproducible simulator candidate, if Sustenance is still functional when Crimson Brood begins, that one capped **240-HP** passive Reconstruction resolves **at Crimson entry**; this timing is working-policy detail, not owner canon;
- Sustenance and Conduction remain damaging selected actions;
- Brood remains a finite extra hostile body.

This mode is an experimental simulator overlay. It does not rewrite the encounter owner.

## v106 DiySim calibration — non-diluting + Power ×1.20
The corrected Brood-response policy was tested over **2,000 runs per line**, seed 106, with the finite prepared inventory above.

| Player line | Strategy | Win | Any KO | Wipe | Mean rounds | Mean ending HP | Mean items |
|---|---|---:|---:|---:|---:|---:|---:|
| Lv24 mandatory | Rush | **98.40%** | **27.10%** | **1.60%** | 31.47 | 45.30% | 7.65 |
| Lv24 mandatory | Full dismantle | **97.50%** | **40.85%** | **2.40%** | 32.13 | 40.48% | 7.82 |
| Lv28 high-side | Rush | **100%** | **0.25%** | **0%** | 24.87 | 59.57% | 4.76 |
| Lv28 high-side | Full dismantle | **100%** | **0.25%** | **0%** | 25.47 | 58.00% | 4.98 |

Additional observed signals:
- Lv24 Rush Brood uptime: **1.758 actions** across exactly 2 deployments on average;
- Lv28 Rush Brood uptime: **1.439 actions** across exactly 2 deployments on average;
- full dismantle prevents Brood deployment and destroys all 4 Reservoirs as intended;
- the Lv24 versus Lv28 safety separation is strong and directionally correct under the same ordinary gear and preparation;
- both Lv28 policies remain resource-bearing rather than free: roughly 5 items used and only ~6% MP remaining on average.

### +5 effective-stat-level sensitivity
The exploratory `Power ×1.20 + boss effective-stat level +5` layer is **rejected for Zevraya**.

In the corrected 100-run screen at Lv24:
- non-diluting Rush fell to roughly **67% wins / 86% any-KO / 29% wipes**;
- non-diluting full dismantle fell to roughly **60% wins / 89% any-KO / 37% wipes**.

That layer overshoots the intended mandatory difficulty and is not the current certification candidate.

## Current structural finding
The `Power ×1.20` non-diluting model creates the desired **mandatory-versus-high-side difficulty separation**, but the all-four Reservoir dismantle route still fails its tactical-payoff test:

> **full dismantle is measurably more dangerous than Rush at Lv24 despite spending extra actions to remove all four functions.**

This is not accepted as a finished encounter structure.

Do not promote the non-diluting candidate into the encounter owner yet. The next DiySim pass should test **selective Reservoir dismantling** to determine which functions are worth spending actions to remove and whether a smaller dismantle package can create a genuine safety tradeoff without making the mechanic a trap.

## Difficulty reading rule
Judge Zevraya against the current boss philosophy:
- **mandatory Lv24:** challenging but reliably beatable with competent prepared play;
- **high-side Lv28:** clearly easier, but still meaningfully pressured and still required to respect Zevraya's mechanics;
- neither line should be a faceroll;
- mandatory should not become wipe-heavy or unfair.

Use the complete profile:
- win / wipe / any-KO rates;
- rounds;
- remaining HP / MP;
- consumables spent;
- control/Bleed exposure;
- Reservoirs destroyed;
- Brood deployment/uptime;
- healing/reconstruction/conduction frequency.

Round targets are useful context but are **not a hard blocker in the current sensitivity pass**; local duration tuning can follow after the difficulty layers are understood.
