# Chapter 5 — Deepforge Colossus Difficulty Recalibration — WORKING v103

**Encounter:** Deepforge Colossus — Assembly Frame → Worldsmith Body  
**Chapter:** 5 — The Mountain Engine  
**Status:** **REOPENED FOR DIFFICULTY / SAME-GEAR COMPARISON ACTIVE**  
**Owner:** `../../09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/DEEPFORGE_COLOSSUS.md`

## User-directed balance change
The mandatory route should be materially harder than a completionist route.

The completionist comparison must not gain an artificial equipment advantage merely because more optional content was completed.

For the core mandatory-vs-completionist difficulty comparison:
- use the **same ordinary equipment** on both routes;
- use the **same normal-stock consumable preparation** on both routes;
- use the same active four and the same competent tactical policy;
- do not give the completionist benchmark Relics/Legacies merely to make the route easier;
- route differences should primarily come from the actual Player Level / CEXP / learned-ability advantage created by optional play;
- Prime-specific advantage is tested separately rather than mixed into the core same-gear comparison.

Duration remains useful, but **temporary-KO incidence, wipe incidence, ending HP/MP, and recovery pressure are now primary difficulty signals**.

This is a design-layer stochastic balance study, not runtime-engine QA.

---

# 1. Exact route snapshots

Current owner route anchors:
- mandatory pre-Deepforge — **Lv20**;
- fixed-content completionist pre-Deepforge — **Lv22**;
- high-side — ~Lv23.

## Same equipment on both routes
To avoid an ambiguous Chapter-5 pickup, the benchmark does **not** assume Deepforge Blade even though its catalog band begins in Chapter 5.

Both routes use the same conservative Chapter-4-or-earlier ordinary loadout:
- Cyanis — **Dunmere Steel / Crest Plate / Yahtrean Shield**;
- Ilyra — **Crucible Wardrod / Blue Warden Mail / Warding Focus**;
- Torren — **Command War Bow / War Archer Gear**;
- Vaelira — **Arcanist Staff / Green Arcanist Garb**.

No Relic or Legacy equipment is used.

## Resulting combat stats

### Mandatory Lv20
| Character | HP | MP | ATK | MAG | DEF | Spirit | SPD |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cyanis | 1,015 | 87 | 107 | 89 | 100 | 81 | 31 |
| Ilyra | 967 | 108 | 100 | 124 | 67 | 97 | 31 |
| Torren | 967 | 91 | 123 | 49 | 72 | 63 | 32 |
| Vaelira | 793 | 120 | 49 | 123 | 57 | 87 | 33 |

### Completionist Lv22 — same gear
| Character | HP | MP | ATK | MAG | DEF | Spirit | SPD |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cyanis | 1,110 | 94 | 112 | 93 | 104 | 85 | 32 |
| Ilyra | 1,057 | 117 | 104 | 129 | 71 | 101 | 32 |
| Torren | 1,057 | 99 | 128 | 53 | 76 | 67 | 33 |
| Vaelira | 867 | 130 | 52 | 129 | 60 | 91 | 34 |

## CEXP state
Using the current Chapter-5 ordinary CEXP pool and named pre-boss awards:
- Cyanis — mandatory ~2,543 Base CEXP / **CL8**;
- Ilyra — mandatory ~2,543 / **CL8**;
- Torren — mandatory ~2,943 / **CL9**;
- Vaelira — mandatory ~2,843 / **CL8**.

A completionist who legally defers the still-available pre-Deepforge optional activities can add approximately **100 optional CEXP** to recruited characters:
- Cyanis — ~2,643 / CL8;
- Ilyra — ~2,643 / CL8;
- Torren — ~3,043 / CL9;
- Vaelira — ~2,943 / **CL9**.

The completionist comparison therefore receives a real but modest progression advantage; Vaelira reaches Spectrum Cascade / Efficient Spectrum while the mandatory snapshot remains CL8.

## Same normal-stock preparation
Reference preparation:
- 3 Vital Salves;
- 2 Restorative Salves;
- 3 Flow Tonics;
- 3 Trauma Remedies;
- 3 Stability Remedies;
- 2 Rousing Salts.

Recovered Last Sentinel exists at this story point, but the core comparison below is no-Prime so the progression signal is not hidden by a one-use burst. Same-Prime stress should be run separately.

---

# 2. Current-package danger check

The current Worldsmith major telegraph is **Forge Collapse — 300 Power AoE Physical**.

Against the same-gear mandatory Lv20 party, current unguarded approximate direct damage is only:
- Cyanis — ~178 / 1,015 HP;
- Ilyra — ~210 / 967 HP;
- Torren — ~205 / 967 HP;
- Vaelira — ~223 / 793 HP.

That is only about **18–28% Max HP before Guard**.

Because all four reference party members act before the Worldsmith at this level, a visible Forge Collapse Preparation can normally be answered with the standard Defend/Guard command, halving eligible direct damage again.

This is too little climax pressure by itself.

## Current same-gear competent-policy sample
Runs:
> **20,000 mandatory + 20,000 completionist**

Mandatory Lv20:
- win rate — **100%**;
- any temporary KO — **0.095%**;
- mean ending combined HP — ~**64%**.

Completionist Lv22, same gear:
- win rate — **100%**;
- any temporary KO — **0.005%**;
- mean ending combined HP — ~**57%**.

The exact round count is policy-sensitive and is not used as the primary verdict in this recalibration.

Difficulty verdict:
> **CURRENT PACKAGE TOO SAFE FOR THE NEW MANDATORY-ROUTE STANDARD**

The boss can create KOs if the player deliberately under-heals/overcommits offense, but a competent recovery policy nearly removes KO risk entirely. That is not the desired consequence for skipping optional progression.

---

# 3. Exploratory Power-only sensitivity

A provisional **~45% increase to the current direct-damage Powers** was tested without changing:
- HP;
- ATK/MAG/DEF/Spirit/SPD raw lines;
- status chances;
- repetition locks;
- fresh-body architecture;
- consumable access;
- equipment;
- player policy.

A clean rounded candidate family would be approximately:

## Form I
- Construction Hammer — **205 → 300**;
- Load-Bearing Sweep — **140 → 205**;
- Forge Discharge — **195 → 285**;
- Clamp and Draw — **170 → 245**.

## Form II
- Worldsmith Clamp — **225 → 325**;
- Foundry Arc — **215 → 310**;
- Construction Sweep — **155 → 225**;
- Worldline Crush — **260 → 375**;
- Forge Collapse — **300 → 435**.

This exact package is **NOT LOCKED** and has not been written into the encounter owner.

### Sensitivity result — same gear
Mandatory Lv20:
- win rate — **99.415%**;
- any temporary KO — **22.21%**;
- wipe incidence — ~**0.585%**.

Completionist Lv22:
- win rate — **100%** in the 20,000-run sample;
- any temporary KO — **4.135%**.

This separation is much closer to the intended progression reward:
> the mandatory route remains clearly viable, but optional progression buys a large reduction in KO risk even when equipment is held constant.

---

# 4. Assembly-choice problem discovered

Do **not** promote the provisional Power package yet.

The harder test exposed a structural interaction that needs correction/confirmation first:
- Guard Press and Repair Arm currently add **selected non-damaging boss actions**;
- destroying those assemblies removes those actions from the Worldsmith's legal menu;
- the party also spends additional turns attacking assembly HP;
- depending on boss action-selection policy, dismantling assemblies can therefore increase hostile attack density enough that the supposed safer Form-II route becomes paradoxically more dangerous overall.

This conflicts with the encounter's authored promise that dismantling pays time in Form I to reduce Form-II pressure rather than becoming a trap choice.

Before Deepforge can be recertified, test/fix the function logic so:
1. leaving assemblies alive is never accidentally safer because their support actions dilute offense;
2. destroying assemblies produces a clear and readable Form-II safety benefit;
3. rush and dismantle remain different valid routes rather than one being a hidden punishment.

Potential solutions include converting one or more inherited support functions into passive/conditional effects rather than ordinary action-menu dilution, or strengthening the explicit offensive/safety penalty attached to surviving assemblies. Exact owner changes require the next tuning step.

---

# 5. Recalibration status

> **REOPENED — CURRENT DIFFICULTY FAILS NEW STANDARD / CANDIDATE OFFENSIVE RANGE IDENTIFIED / ASSEMBLY PAYOFF REQUIRES RESOLUTION**

Do not proceed to final-boss difficulty certification as if the old 100%-win PASS standard were still sufficient.

Next balance action:
> resolve Deepforge assembly payoff/action-density behavior, rerun same-gear Lv20 vs Lv22 distributions, then use the resulting Chapter-5 difficulty profile as the first anchor for the mandatory-route difficulty ramp.
