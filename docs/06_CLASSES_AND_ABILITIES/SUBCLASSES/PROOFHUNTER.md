# Diyse — Proofhunter
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization and later current working corrections, including the approved 2026-08-30 Ability-MP reduction and the 2026-08-30 Proofhunter redesign.  
**Authority treatment:** explicit/newer working corrections are preserved as working overrides when they have not yet been promoted into the audit chain.

**Owner:** Nimera  
**Donor tradition:** War Archer  
**Identity:** hybrid precision, Hunter's Measure, and evidence-based exploitation  
**Trait:** **Applied Evidence**  
**Ultimate:** **Final Annotation**

## Shared Hunter's Measure
Proofhunter uses the same Hunter's Measure state as War Archer; it does not create a separate Nimera-specific version.

Hunter's Measure:
- target suffers **Evasion −10**;
- all party members gain **+10 percentage points Critical Chance** against that target;
- lasts the remainder of the current round plus the next **2 full normal rounds**;
- refreshes rather than stacks;
- is an authored tactical state, not a universal harmful status.

### Awakened Prime interaction
Proofhunter uses War Archer's same Hunter's Measure Prime lifecycle:
- Prime rounds do **not** consume Hunter's Measure's normal-round duration checkpoints;
- Hunter's Measure remains attached to the target during suspension unless the target/body is replaced or another explicit effect removes it;
- the target's **Evasion −10** remains active on that target;
- the manifested Prime is not an ordinary party member, so the **+10 percentage points party Critical Chance** does not automatically apply to Prime commands;
- normal-round duration resumes when the ordinary party returns.

**Pin the Variable** Defense/Spirit reductions also use normal-round duration clocks. Prime rounds do not consume their printed 4-round or 3-round duration checkpoints. **Applied Evidence Rank I** is a temporary Magic modifier on Nimera and follows the global suspended-party temporary-stat rule.

## Ability spine
| Unlock | Ability | MP | Current effect |
|---:|---|---:|---|
| CL1 | **Measured Shot** | 12 | One enemy; Hybrid / Neutral **50/50**; **140 Power**; **110 Base Hit**. On hit, apply Hunter's Measure if absent; if target is already Measured, the attack instead gains **+15 percentage points Critical Chance** and refreshes Measure. |
| CL4 | **Held Argument** | 17 | One enemy; Hybrid / Neutral **50/50**; **175 Power**; **105 Base Hit**. Against Hunter's Measure: **210 Power**, **+10 Base Hit**, and **20% applicable defensive-axis penetration**. |
| CL7 | **Pin the Variable** | 19 | One enemy; Hybrid / Neutral **50/50**; **155 Power**; **110 Base Hit**. On hit: if unmeasured, **Defense −10% / Spirit −10% for 4 rounds**; if Measured, **Defense −20% / Spirit −20% for 3 rounds** and refresh Hunter's Measure. |
| CL9 | **Structural Failure** | 26 | One enemy; Hybrid / Neutral **50/50**; **240 Power**; **105 Base Hit**; **30% applicable defensive-axis penetration**. Against Hunter's Measure: **280 Power**, penetration **30% → 40%**, and **+10 Base Hit**. If target currently has Defense Down or Spirit Down, also gain **+10 percentage points Critical Chance**. |
| CL11 | **Corroboration** | 29 | All enemies; Hybrid / Neutral **50/50**; **185 Power per target**; **100 Base Hit**. Against already-Measured targets: **+10 Base Hit** and **+15 percentage points Critical Chance**. If Corroboration successfully hits at least one already-Measured enemy, every other enemy hit by the action gains Hunter's Measure after damage resolution. |
| CL13 | **Final Annotation** | 51 | Subclass Ultimate; one enemy; Hybrid / Neutral **50/50**; **360 Power**; **115 Base Hit**; **40% applicable defensive-axis penetration**. Against Hunter's Measure: **+20% final damage**. If target currently has Defense Down or Spirit Down: **+15 percentage points Critical Chance**. If both conditions are true, penetration becomes **50%** and Hunter's Measure refreshes after resolution. |

## Masteries
| Unlock | Mastery | Current effect |
|---:|---|---|
| CL3 | **Proven Measure** | Measured Shot **140 → 155 Power**; its already-Measured Critical bonus **+15pp → +20pp**. |
| CL5 | **Decisive Argument** | Held Argument **175 → 190 Power**; against Hunter's Measure its empowered Power becomes **225** instead of 210. |
| CL7 | **Equipment Mastery** | Unlocks class eligibility for the donor **War Archer Relic**, subject to actual Relic ownership and other established requirements. |
| CL11 | **Legacy Mastery** | Unlocks class eligibility for the donor **War Archer Legacy**, subject to donor/shared Legacy completion/ownership and other established requirements. |

## Trait ranks — Applied Evidence
- **Rank I — CL1:** whenever Nimera successfully applies or refreshes Hunter's Measure with a Proofhunter Ability, she gains **Magic +10% for 4 rounds**. Reapplication refreshes rather than stacks.
- **Rank II — CL6:** damaging Proofhunter Abilities gain **+10 percentage points Critical Chance** against Hunter's Measure.
- **Rank III — CL12:** damaging Proofhunter Abilities gain **15% additional applicable defensive-axis penetration** against targets that both have Hunter's Measure and are currently suffering Defense Down or Spirit Down. This stacks with explicitly authored same-axis penetration subject to the global penetration cap.

## Global references
- Damage/penetration: `05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- Temporary stat changes: `05_BATTLE_SYSTEM/STAT_CHANGES.md`
- Hit/Evasion: `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- Critical: `05_BATTLE_SYSTEM/CRITICAL_HITS.md`
- Elements/statuses: `05_BATTLE_SYSTEM/ELEMENTS.md` and `STATUS_EFFECTS.md`

## Firewall
Do not restore the retired Prepared-action interrupt version of Held Argument, old Speed-down Pin the Variable, Bleed-heavy Proofhunter package, or authored large/Hunt/structural-target bonus tags.
