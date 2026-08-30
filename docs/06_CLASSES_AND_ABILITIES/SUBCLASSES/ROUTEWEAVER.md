# Diyse — Routeweaver
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization and later current working corrections, including the approved 2026-08-30 Ability-MP reduction and the 2026-08-30 Routeweaver redesign.  
**Authority treatment:** explicit/newer working corrections are preserved as working overrides when they have not yet been promoted into the audit chain.

**Owner:** Torren  
**Donor tradition:** Cardweaver  
**Identity:** party routing, action sequencing, MP efficiency, and battlefield path control  
**Trait:** **Route Weaving**  
**Ultimate:** **Open the Way**

## Route state rules
Routeweaver translates Cardweaver's archive/tempo/economy concepts into battlefield paths rather than literal action copying.

- Routeweaver effects do not create extra ordinary actions unless explicitly stated; Covered Crossing and Open the Way reposition normal turns instead.
- Initiative normally remains fixed at round start. Covered Crossing and Open the Way are explicit authored exceptions that move a character's existing normal turn.
- Source-owned route/link states are Torren-authored constructs and are not ordinary harmful statuses.

## Ability spine
| Unlock | Ability | MP | Current effect |
|---:|---|---:|---|
| CL1 | **Throughline** | 12 | One enemy; Hybrid / Neutral **50/50**; **160 Power**; **105 Base Hit**. On hit, establish **Throughline** on that enemy through the remainder of the current round plus the next **2 full normal rounds**. The first allied MP-costing Ability or Standard Card each round that targets the Throughlined enemy costs **20% less MP**, rounded normally, minimum 1 MP. Prime actions are unaffected. Only one enemy may carry Torren's Throughline at once; applying it elsewhere moves the route. |
| CL4 | **Set the Pace** | 15 | **Power: N/A — no direct damage.** One ally gains **Speed +20% for 3 rounds**. Reapplication refreshes rather than stacks. Current-round initiative is not reshuffled. |
| CL7 | **Crossroads** | 24 | **Power: N/A for the link itself.** Link two enemies for **3 rounds**. **Once per round**, when an ally completes a direct-damage Ability or Standard Card that damages exactly one linked enemy, the other linked enemy takes secondary routed damage equal to **40% of the total final direct damage dealt to the struck linked enemy by that action**. One proc per qualifying action regardless of hit count. If the triggering action directly damages both linked enemies, Crossroads does not trigger. Routed damage cannot Crit, reapply statuses, trigger follow-ups, trigger Crossroads again, or pass through Defense/Spirit a second time. Ultimates do not trigger Crossroads. If either linked enemy is defeated, the link ends. |
| CL9 | **Covered Crossing** | 20 | **Power: N/A — no direct damage.** Choose one conscious ally. At the next normal round's initiative setup, that ally retains an ordinary initiative slot but is marked to reroute. When Torren completes his normal turn, the ally immediately takes their normal turn, then is removed from their original slot for that round. If Torren cannot take his normal turn before the ally's original slot arrives, the ally acts normally at that original slot and Covered Crossing expires. No extra action is created. |
| CL11 | **Frozen Passage** | 29 | All enemies; Magical / Ice; **195 Power per target**; **100 Base Hit**; base **20% Freeze** per target. Against an enemy that has not yet taken its normal turn this round, Freeze chance becomes **35%**. Against an enemy that already acted, it remains 20%. Resolve separately per target. |
| CL13 | **Open the Way** | 53 | Subclass Ultimate. Choose up to **3 other conscious allies** and order them. On the next normal round, when Torren completes his normal turn, the selected allies immediately take their normal turns one after another in the chosen order; each is removed from their original initiative slot for that round. Each routed action gains **+10 Base Hit / application reliability** and costs **20% less MP**, rounded normally, minimum 1 MP. No extra actions are created. If Torren cannot take his normal turn before a selected ally's original slot arrives, that ally acts normally at that slot and is removed from the routed sequence. Prime manifestation sequencing is unaffected. |

## Masteries
| Unlock | Mastery | Current effect |
|---:|---|---|
| CL3 | **Long Sight** | Throughline's post-application full-round window increases by **1 full normal round**. |
| CL5 | **Guided Crossing** | Set the Pace **Speed +20% → +30%**. A Covered Crossing ally also gains **+10 Evasion** from the moment Torren completes his turn until that ally's routed action finishes resolving. |
| CL7 | **Equipment Mastery** | Unlocks class eligibility for the donor **Cardweaver Relic**, subject to actual Relic ownership and other established requirements. |
| CL11 | **Legacy Mastery** | Unlocks class eligibility for the donor **Cardweaver Legacy**, subject to donor/shared Legacy completion/ownership and other established requirements. |

## Trait ranks — Route Weaving
- **Rank I — CL1:** after Torren uses a Routeweaver Ability that establishes or manipulates a route — Throughline, Set the Pace, Crossroads, or Covered Crossing — his next damaging Routeweaver Ability before the end of the following round gains **+10 Base Hit**. One stored benefit maximum; refresh rather than stack.
- **Rank II — CL6:** when an ally successfully benefits from one of Torren's route effects, Torren restores **4% Max MP**, at most **once per normal round**. Qualifying benefits include consuming Throughline's MP reduction, acting while Set the Pace is active, triggering Crossroads, or taking the rerouted turn from Covered Crossing/Open the Way.
- **Rank III — CL12:** the first ally each normal round to successfully benefit from one of Torren's route effects gains **+10 Base Hit / application reliability** for that benefiting action where relevant.

## Global references
- Turn/round and initiative timing: `05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`
- Damage/penetration/direct-damage reduction: `05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md`
- Temporary stat changes: `05_BATTLE_SYSTEM/STAT_CHANGES.md`
- Hit/Evasion: `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- Elements/statuses: `05_BATTLE_SYSTEM/ELEMENTS.md` and `STATUS_EFFECTS.md`

## Firewall
Do not restore the retired Clear Route single-target cleanse/Speed package, old Crossroads buff-choice package, Covered Crossing Card-potency package, or Open the Way buff Field. Routeweaver's current identity is routing and sequencing, not a second War Archer Field kit.
