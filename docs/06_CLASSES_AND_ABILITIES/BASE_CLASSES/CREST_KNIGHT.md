# Diyse — Crest Knight
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization and later current working corrections, including the approved 2026-08-30 Ability-MP reduction.  
**Authority treatment:** explicit/newer working corrections are preserved as working overrides when they have not yet been promoted into the audit chain.


**Owner:** Cyanis  
**Class line:** Native Base Class  
**Identity:** physical-forward Crest fighter with strong Defense and mixed Physical/Magical tools  
**Trait:** **Harmonized Crest**  
**Ultimate:** **Crest of Companions**

## Ability spine
| Unlock | Ability | MP | Current effect |
|---:|---|---:|---|
| CL1 | **Crest Strike** | 9 | One enemy; Physical / Neutral; **140 Power**; no harmful status. |
| CL1 | **Crest Reprisal** | 15 | **Power: N/A on selection.** Self Prepared state through the end of the following normal round. Intercepts the next eligible single-target hostile direct-damage action aimed at another conscious active-party member; Cyanis becomes the target and takes the complete intercepted action. If Cyanis remains conscious and the attacker remains a legal target after that action resolves, Cyanis immediately counters that attacker with **155 Power, Physical / Neutral**. One successful intercept consumes the state. |
| CL1 | **Resonant Pulse** | 10 | One enemy; Magical / Colorless; **150 Power**; no harmful status. |
| CL3 | **Sweeping Edge** | 17 | All enemies; Physical / Neutral; **130 Power per target**; **10% Bleed** per target. |
| CL6 | **Twin Advance** | 19 | One enemy; Physical / Neutral; exactly 2 authored hits at **100 Power each (200 total)**. |
| CL9 | **Crest Rend** | 27 | One enemy; Hybrid / Neutral **75% Attack / 25% Magic**; **240 Power**; **35% Bleed**; Attack-derived share has **30% Defense penetration** and Magic-derived share has **30% Spirit penetration**. |
| CL13 | **Crest of Companions** | 48 | Base Ultimate; all enemies; Magical / Colorless; **300 Power per target**. After enemy damage resolves, each conscious active-party member removes **1 eligible universal harmful status** and gains **Defense +30% / Spirit +30% for 2 rounds**. Does not revive. |

## Crest Reprisal Prepared rules
Crest Reprisal establishes an authored Prepared self-state; it does not select or mark an ally when cast.

Eligible interception requires:
- a hostile action that directly damages exactly one party target;
- that target to be another conscious active-party member;
- Cyanis to be conscious, present, and a legal target when interception occurs.

When eligible:
1. retarget the complete hostile action from the original ally to Cyanis;
2. resolve that action normally against Cyanis, including all legal hits and attached effects;
3. consume Crest Reprisal's Prepared state;
4. if Cyanis remains conscious and the hostile actor is still a legal target, resolve the **155-Power Physical / Neutral counter** immediately.

Crest Reprisal does not intercept:
- an action already targeting Cyanis;
- multi-target or all-party actions;
- indirect-only damage without a single direct target;
- scripted effects that explicitly prohibit interception/retargeting.

If an attempted hostile action is ineligible, Crest Reprisal remains pending until it triggers or its window expires. The counter is part of the Prepared reaction package and does not grant Cyanis an additional normal turn.

During Awakened Prime suspension, the state cannot intercept attacks because the ordinary party is suspended; its normal-round expiry clock follows the global tactical-state pause rule.

## Crest Rend penetration
Crest Rend resolves its two Hybrid shares through their corresponding defensive axes:
- **75% Attack-derived share:** 30% Defense penetration;
- **25% Magic-derived share:** 30% Spirit penetration.

**Penetrating Crest** adds +10 percentage points to both applicable shares, producing **40% Defense penetration / 40% Spirit penetration** for Crest Rend after that Mastery unlocks, subject to the global penetration cap.

## Crest of Companions support resolution
After all enemy damage from Crest of Companions resolves:
- for each conscious active-party member, remove **1 eligible universal harmful status**; if more than one is eligible, the player chooses which status to remove for that party member;
- then apply **Defense +30% / Spirit +30% for 2 rounds** to each conscious active-party member.

The defensive bonuses are Major temporary core-stat increases under `05_BATTLE_SYSTEM/STAT_CHANGES.md`; they may stack with different legal effects only up to the global **+40% per-axis cap**.

Crest of Companions does not revive KO party members and does not cleanse or buff a party member who remains KO when the support package resolves.

## Masteries
| Unlock | Mastery | Current effect |
|---:|---|---|
| CL3 | **Guardian Geometry** | When Crest Reprisal successfully intercepts an eligible single-target direct attack, Cyanis takes **10% less final direct damage** from that intercepted attack. |
| CL6 | **Balanced Assault** | Crest Strike +15 Power; Twin Advance +15 total Power, not +15 per hit. |
| CL9 | **Clear Channel** | Resonant Pulse costs 1 less MP: 10 → **9**. |
| CL12 | **Penetrating Crest** | Crest Rend gains **+10 percentage points** of applicable penetration on both its Attack-derived and Magic-derived shares, raising its current base 30%/30% package to **40% Defense penetration / 40% Spirit penetration**. |

All four Core Masteries unlock automatically at the listed Class Levels under the current v85 working override.


## Global references
- Damage/penetration: `05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- Hit/Evasion: `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- Critical: `05_BATTLE_SYSTEM/CRITICAL_HITS.md`
- Elements/statuses: `05_BATTLE_SYSTEM/ELEMENTS.md` and `STATUS_EFFECTS.md`
- Temporary stat changes: `05_BATTLE_SYSTEM/STAT_CHANGES.md`
- Prepared/retargeting: `05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md` and `TARGETING_AND_RETARGETING.md`

## Firewall
Do not restore the retired dual Physical/Magical route versions of Crest Reprisal, Twin Advance, or Crest Rend; each current Ability uses the fixed damage type/formula printed above. Do not restore the retired Vulnerability rider on Crest Rend.
