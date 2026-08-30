# Diyse — Cardweaver
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization and later current working corrections, including the approved 2026-08-30 Ability-MP reduction and the 2026-08-30 Cardweaver redesign.  
**Authority treatment:** explicit/newer working corrections are preserved as working overrides when they have not yet been promoted into the audit chain.

**Owner:** Nimera  
**Class line:** Native Base Class  
**Identity:** Speed, Standard-Card MP efficiency, action archiving/copying, and party MP economy  
**Trait:** **Living Archive**  
**Ultimate:** **Grand Reweaving**

## Living Archive recording rules
While Cardweaver is selected, Nimera records eligible allied actions performed between her turns.

- Rank I retains the last **2** eligible allied actions in the current recording window.
- Rank II retains the last **3**.
- When Nimera completes her next turn, the ordinary archive clears and a new recording window begins.
- **Perfect Recall** may preserve one chosen record beyond the ordinary window.
- The archive records normal allied Abilities and Standard Cards that can resolve as ordinary immediate actions.
- It does not record Ultimates, Prime invocation/commands, Items, Basic Attack, Defend, Prepared/reaction actions, Field-creating actions, summons, other copy/replay actions, scripted actions, source-owned persistent class constructs such as Throughline/Crossroads/Covered Crossing, or any action whose effect **grants additional actual actions or changes the number of normal actions**.
- Therefore Standard Card **Split Moment** is not eligible for Living Archive, Echo Weave, Perfect Recall, or Grand Reweaving.

## Trait ranks — Living Archive
- **Rank I — CL1:** Nimera's Standard Cards cost **20% less MP**, rounded normally, minimum 1 MP; Living Archive retains the last **2** eligible allied actions in the current recording window.
- **Rank II — CL6:** Living Archive capacity increases **2 → 3 eligible actions** per recording window.
- **Rank III — CL12:** Nimera's personal Standard-Card MP reduction increases **20% → 30%**.

Living Archive's personal Standard-Card reduction uses the global compatible MP-cost-modifier rules in `MP_COST_RULES.md`; it does not reduce Prime actions, which already cost 0 MP.

## Copy resolution rules
When Echo Weave or Grand Reweaving reproduces an eligible record:
- **Echo Weave / Grand Reweaving remains the acting Cardweaver Ability identity.** The copied record supplies a reproducible effect package; Nimera is not treated as literally using the source Ability or Standard Card identity.
- The reproduction therefore does **not** trigger source-action-specific Traits, Masteries, equipment clauses, Card-use counters, or "after using a Standard Card" effects merely because the recorded source was that action.
- A general effect that legally checks properties of the resolving reproduction itself — such as its resulting damage type, element, target count, or whether it successfully damages — may still apply if all of that effect's normal requirements are satisfied.
- Nimera chooses legal targets at resolution.
- Targeting pattern, damage type, element, **authored Base Hit**, authored penetration, ordinary Critical eligibility, ordinary status/application chances, cleanses, and other immediate legal effects are retained.
- Nimera uses her own applicable stats.
- Direct damage, direct healing, and revival recovery are multiplied by the copy's stated potency modifier after the copied action resolves its ordinary authored calculations.
- Effects with no scalable damage/healing number retain their authored immediate magnitude unless explicitly excluded.
- Copied actions cannot create further archive/copy chains.

## Awakened Prime interaction
Living Archive and Perfect Recall remain Cardweaver-owned ordinary-party states; they do not become Prime commands or Prime resources.

- Prime Invocation and Prime commands are never eligible Living Archive records.
- If another party member invokes an Awakened Prime before Nimera completes her next turn, Nimera's current Living Archive recording window remains intact through the Prime suspension. Prime rounds do not count as Nimera turns and do not clear the archive.
- If **Nimera herself** selects Prime Invocation on her turn, that invocation is still her selected action. When that turn completes, the ordinary Living Archive window clears normally; a separately active Perfect Recall record remains preserved according to its own duration.
- Perfect Recall's printed round duration is a **normal-round** duration. Awakened Prime rounds do not consume that duration; it resumes when normal party-round flow returns.
- A Preserved Record cannot be selected or copied by the manifested Prime body.
- **Ancient Override** follows the global Field pause rule during Awakened Prime rounds.
- **Hastened Weave** follows the global temporary-stat pause rule while Nimera is suspended.

## Ability spine
| Unlock | Ability | MP | Current effect |
|---:|---|---:|---|
| CL1 | **Echo Weave** | Variable | Choose one eligible action currently recorded by Living Archive and reproduce it at **80% direct-damage/direct-healing/revival potency**. Echo Weave costs **75% of the recorded action's authored Base MP**, rounded normally, minimum **8 MP**; ordinary legal cost modifiers may then apply. |
| CL1 | **Weave Burst** | 19 | All enemies; Magical / Colorless; **130 Power per target**; **100 Base Hit**; no secondary effect. |
| CL1 | **Hastened Weave** | 10 | **Power: N/A — no direct damage.** Nimera gains **Speed +20% for 3 rounds**. Reapplication refreshes rather than stacks. Current-round initiative is not reshuffled. |
| CL3 | **Ancient Override** | 26 | **Power: N/A — no direct damage.** Create a 3-round Field. While active, all party members' MP-costing Abilities, Ultimates, and Standard Cards cost **15% less MP**, rounded normally, minimum 1 MP. Prime actions remain 0 MP and are unaffected. Recasting refreshes this Field rather than stacking another copy. |
| CL6 | **Weave Spark** | 17 | One enemy; Magical / Lightning; **160 Power**; **100 Base Hit**; **35% Stun**. |
| CL9 | **Perfect Recall** | 24 | **Power: N/A — no direct damage.** Choose one action currently recorded in Living Archive and preserve it for **3 rounds**. The Preserved Record remains selectable by Echo Weave despite newer recordings and is not consumed by being copied. Only one Preserved Record may exist; creating another replaces it. |
| CL13 | **Grand Reweaving** | 48 | Base Ultimate. Choose up to **3 different** eligible records currently available through Living Archive and/or Perfect Recall and reproduce them sequentially at **75% direct-damage/direct-healing/revival potency**. No additional MP is paid for the reproduced actions. The same record cannot be selected more than once. Normal copy exclusions remain in force. |

## Masteries
| Unlock | Mastery | Current effect |
|---:|---|---|
| CL3 | **Quick Study** | Echo Weave copy potency **80% → 90%** for direct damage, direct healing, and revival recovery. |
| CL6 | **Charged Weave** | Weave Spark Stun **35% → 50%**. |
| CL9 | **Efficient Override** | Ancient Override party MP reduction **15% → 20%**. |
| CL12 | **Perfect Reconstruction** | Perfect Recall duration **3 → 4 rounds** and Grand Reweaving copy potency **75% → 85%** for direct damage, direct healing, and revival recovery. |

All four Core Masteries unlock automatically at the listed Class Levels under the current working rule.

## Global references
- Standard Cards: `../../07_CARDS/CARD_SYSTEM_MASTER.md` and `../../07_CARDS/STANDARD_CARDS/STANDARD_CARD_USE_RULES.md`
- Damage/penetration/direct-damage reduction: `05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- Fields: `05_BATTLE_SYSTEM/FIELDS.md`
- Turn/round and initiative timing: `05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`
- Temporary stat changes: `05_BATTLE_SYSTEM/STAT_CHANGES.md`
- Elements/statuses: `05_BATTLE_SYSTEM/ELEMENTS.md` and `STATUS_EFFECTS.md`

## Firewall
Do not restore retired Weave Bolt, Weave Guard, Sovereign Index, Card-Seal mechanics, or the old first-Card potency Trait package. Cardweaver's current core is Card economy, Speed, archiving, and copying.
