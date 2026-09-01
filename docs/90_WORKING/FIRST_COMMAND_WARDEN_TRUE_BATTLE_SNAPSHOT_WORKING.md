# First Command Warden — True-Battle Snapshot Working Candidate

**Status:** **WORKING SIMULATION CANDIDATE / NOT OWNER CANON / NOT APPROVED FOR MAIN**  
**Encounter owner remains:** `09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/FIRST_COMMAND_WARDEN.md`  
**Purpose:** supply the missing exact pre-battle Class-Level and prepared-consumable inputs required by `TRUE_BATTLE_TEST_PROTOCOL.md` so DiySim can test the current owner encounter and v104/v106 overlays without hiding assumptions in code.

This file does **not** change the Warden body, action Powers, AI, Chapter-3 CEXP budgets, shop availability, or permanent campaign inventory.

## Fixed route frame inherited from v105
- Player Level comparison: **Lv11 mandatory vs Lv13 high-side**.
- Active four: **Cyanis / Ilyra / Torren / Nimera**.
- Same ordinary equipment on both level lines.
- Same selected Base Classes and learned-Ability package on both level lines.
- No Relic/Legacy advantage.
- No Prime.
- Full HP / full MP boss-isolation start.

## Working pre-Warden Base Class Levels

| Character | Selected Base Class | Working CL at S020 | Basis |
|---|---|---:|---|
| Cyanis | Crest Knight | **CL5** | Cyanis receives all Ch1–2 CEXP (800). Ch3's full 550 reaches CL6 exactly at 1,350; the S020 pre-boss snapshot is before the full chapter stream is complete. |
| Ilyra | Blue Warden | **CL5** | Same full-stream arithmetic as Cyanis. |
| Torren | War Archer | **CL6** | 600 starting CEXP + 150 late-Ch1 + 450 Ch2 = 1,200 before Ch3; CL6 is 1,350. S020 occurs after the substantial Chapter-3 route combat following S019. |
| Nimera | Cardweaver | **CL4** | Joins at S019 with 600 CEXP and receives only 300 CEXP across the remainder of Ch3; even the full post-recruit chapter remainder stays below CL5's 950 threshold. |

Cross-check:
- the certified Chapter-4 pre-boss planning centers are Cyanis CL6 / Ilyra CL6 / Torren CL7 / Nimera CL5-near6;
- this working Chapter-3 line is therefore the expected one-step-earlier progression shape.

### Ability consequences used by the candidate
- Cyanis CL5: CL1 + CL3 Crest Knight kit; no CL6 Ability/Trait rank/mastery.
- Ilyra CL5: Mend / Clear Warding / Renewal / Warden's Valor; Gentle Continuance Rank I and Gentle Hands mastery; no CL6 Revive or Trait Rank II.
- Torren CL6: Cinder Shot / Sizing Shot / Choose the Route / Pinning Strike / Colossus Draw; Heavy Draw mastery and Veteran's Measure Rank II are active.
- Nimera CL4: Echo Weave / Weave Burst / Hastened Weave / Ancient Override; Quick Study mastery; no CL6 Weave Spark or Trait Rank II.

The first executable Warden diagnostic used only the earlier conservative direct-damage subset. This candidate exists so later true-battle policy can use the actual learned mandatory package instead of equating v105's phrase `same learned ability set` with `CL1 actions only`.

## Working prepared consumable candidate

The true-battle protocol requires carried consumables to be explicit. Current stock authority provides reliable access by Chapter 3 to Restorative Salve, Flow Tonic, Rousing Salts, Stability Remedy, and General Remedy.

For the first reproducible prepared calibration candidate use:

| Consumable | Count | Role in Warden test |
|---|---:|---|
| **Restorative Salve** | **3** | emergency single-target HP recovery |
| **Flow Tonic** | **1** | preserve essential MP when resource pressure becomes binding |
| **Stability Remedy** | **2** | remove actionable Stun / Staggered |
| **Rousing Salts** | **1** | reserve revival after a KO |

Rationale / bracket:
- certified Ch2 v97 prepared inventory: 3 Field Salve / 2 Trauma Remedy / 1 Rousing Salts;
- by late Ch2, Restorative Salve and Flow Tonic are reliably purchasable;
- Chapter 3 adds Stability Remedy before its Stun pressure;
- certified Ch4 v99 prepared inventory: 3 Restorative Salve / 2 Flow Tonic / 2 Stability Remedy / 2 Rousing Salts.

Therefore this Chapter-3 candidate deliberately sits between the certified Ch2 and Ch4 preparation packages. It is a **simulation benchmark inventory, not a free mandatory grant and not a permanent economy lock**.

General Remedy is legal by Chapter 3 but omitted from this first Warden candidate because the Warden's authored harmful-status pressure is Stun / Staggered, already covered by Stability Remedy.

## Smart prepared-policy boundary
- destroy an aligned Command Ring when doing so cancels Major Ruling;
- react only to visible completed state;
- avoid repeating an active Command Seal category when a reasonable legal alternative exists;
- use Stability Remedy when Stun / Staggered is materially denying action economy;
- use Restorative Salve on materially endangered allies when spending the current actor's turn is better than risking a KO;
- reserve Rousing Salts for a KO;
- use Flow Tonic only when MP is the binding resource for an important legal action;
- Ilyra prioritizes survival / cleanse / healing when needed;
- Torren establishes Hunter's Measure and uses strongest legal measured offense while MP permits;
- no Cards or Prime are introduced by this candidate.

## Calibration rule
Do **not** force a runtime-engine true battle to reproduce v105's exact stochastic percentages. v105 explicitly identifies itself as a calibrated design-layer sensitivity rather than runtime-engine QA.

Use these checks instead:
1. Lv13 same-gear should remain meaningfully safer/faster than Lv11;
2. ×1.20 and +5 overlays must be compared on the exact same prepared snapshot and policy;
3. encounter-duration tuning is **deferred** and does not block the present difficulty-sensitivity read.

The former ~10–11-round authored target remains useful future tuning guidance, but exceeding it during the current +5 sensitivity is accepted temporarily. Do not weaken a promising danger/separation result merely to force the old duration target during this pass.

## DiySim 2,000-run sensitivity checkpoint — accepted for current pass
Seed: **106**. Prepared snapshot as defined above unless explicitly labeled itemless.

### Lv11 mandatory — ×1.20 Power + boss +5 effective core-stat levels
- Win rate: **100%**
- Any-KO: **3.40%**
- Wipes: **0%**
- Mean rounds: **14.088**
- Median rounds: **14**
- 10–90% rounds: **13–16**
- Mean remaining party HP: **66.11%**
- Mean remaining party MP: **10.56%**
- Mean Items used: **3.6905**
- Mean Major Ruling attempts: **1.0695**
- Mean Major Ruling disruptions: **0.821**
- Mean Major Ruling resolutions: **0.248**

### Lv13 same gear — ×1.20 Power + boss +5 effective core-stat levels
- Win rate: **100%**
- Any-KO: **0.15%**
- Wipes: **0%**
- Mean rounds: **11.769**
- Median rounds: **12**
- 10–90% rounds: **11–13**
- Mean remaining party HP: **67.17%**
- Mean remaining party MP: **3.59%**
- Mean Items used: **1.914**
- Mean Major Ruling attempts: **0.7585**
- Mean Major Ruling disruptions: **0.7315**
- Mean Major Ruling resolutions: **0.027**

### Lv11 itemless stress — ×1.20 Power only
This is **not** the prepared balance line. It exists to show the importance of preparation/consumables.
- Win rate: **99.55%**
- Any-KO: **26.25%**
- Wipes: **0.45%**
- Mean rounds: **12.447**
- Mean remaining party HP: **37.71%**

## Current read
- The +5 layer creates a clear mandatory-vs-higher-level separation without producing routine wipes.
- Prepared Lv11 is materially more dangerous than Lv13 same-gear.
- The approximately 14-round Lv11 duration is **accepted for now** and is not a blocker to continuing the wider boss-sensitivity pass.
- Round-target tuning should be revisited later as a local Warden pacing/action-tax pass.
- Do **not** promote the +5 layer or this working snapshot to owner canon solely from this checkpoint; continue cross-boss validation first.
