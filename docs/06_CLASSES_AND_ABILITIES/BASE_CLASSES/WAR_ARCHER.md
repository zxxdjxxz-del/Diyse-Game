# Diyse — War Archer
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization and later current working corrections, including the approved 2026-08-30 Ability-MP reduction and the 2026-08-30 War Archer redesign.  
**Authority treatment:** explicit/newer working corrections are preserved as working overrides when they have not yet been promoted into the audit chain.

**Owner:** Torren  
**Class line:** Native Base Class  
**Identity:** physical precision, enemy assessment, and route control; War Archer is not a Speed-focused class  
**Trait:** **Veteran's Measure**  
**Ultimate:** **The Great Beast Falls**

## Hunter's Measure
Hunter's Measure is an authored tactical state, not a universal harmful status.

When applied:
- target suffers **Evasion −10**;
- all party members gain **+10 percentage points Critical Chance** against that target;
- duration is the remainder of the current round plus the next **2 full normal rounds**;
- reapplication refreshes duration rather than stacking;
- ordinary Status Resistance does not block it;
- a genuinely separate fresh-HP form does not inherit the previous form's Measure unless explicitly authored.

## Ability spine
| Unlock | Ability | MP | Current effect |
|---:|---|---:|---|
| CL1 | **Cinder Shot** | 10 | One enemy; Physical / Fire; **155 Power**; **110 Base Hit**; **20% Burn**. |
| CL1 | **Sizing Shot** | 10 | One enemy; Physical / Neutral; **135 Power**; **110 Base Hit**; on hit applies **Hunter's Measure**. |
| CL1 | **Choose the Route** | 17 | **Power: N/A — no direct damage.** Choose one 3-round War Archer Route Field. **Clear Route:** all allies gain **+10 Base Hit**. **Covered Route:** all allies gain **+10 Evasion**. Only one Torren-authored War Archer Route Field may be active at once; choosing the other replaces the current one. |
| CL3 | **Pinning Strike** | 15 | One enemy; Physical / Neutral; **145 Power**; **110 Base Hit**; on hit target suffers **Base Hit −10 for 2 rounds**; if target has Hunter's Measure, penalty becomes **Base Hit −15**. Reapplication refreshes rather than stacks. |
| CL6 | **Colossus Draw** | 22 | One enemy; Physical / Neutral; **245 Power**; **105 Base Hit**; **25% Defense penetration**; against Hunter's Measure, penetration becomes **35%**. |
| CL9 | **Relentless Barrage** | 26 | All enemies; Physical / Neutral; **160 Power per target**. Each target with Hunter's Measure also receives one separate **80-Power** follow-up hit; that follow-up may Crit independently under normal direct-hit rules. |
| CL13 | **The Great Beast Falls** | 44 | Base Ultimate; one enemy; Physical / Neutral; **600 Power**; **115 Base Hit**; **40% Defense penetration**; against Hunter's Measure gains **+15 percentage points Critical Chance**. |

## Masteries
| Unlock | Mastery | Current effect |
|---:|---|---|
| CL3 | **Veteran's Eye** | Sizing Shot **135 → 155 Power**. |
| CL6 | **Heavy Draw** | Colossus Draw **245 → 265 Power**. |
| CL9 | **Fieldcraft** | Clear Route **+10 → +15 Base Hit** and Covered Route **+10 → +15 Evasion**. |
| CL12 | **Relentless Hand** | Relentless Barrage AoE portion **160 → 180 Power per target**; the separate measured-target follow-up remains **80 Power**. |

All four Core Masteries unlock automatically at the listed Class Levels under the current working rule.

## Global references
- Damage/penetration/direct-damage reduction: `05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- Fields: `05_BATTLE_SYSTEM/FIELDS.md`
- Hit/Evasion: `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- Critical: `05_BATTLE_SYSTEM/CRITICAL_HITS.md`
- Elements/statuses: `05_BATTLE_SYSTEM/ELEMENTS.md` and `STATUS_EFFECTS.md`

## Firewall
Do not restore retired Quarry Appraisal, Watchful Aim, or Speed-focused War Archer mechanics merely because an archived version used them.
