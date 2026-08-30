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

- Routeweaver effects do not create extra ordinary actions; Covered Crossing and Open the Way reposition existing normal turns instead.
- Initiative normally remains fixed at round start. Covered Crossing and Open the Way are explicit authored exceptions that alter the next round's normal turn order during that round's initiative setup.
- If Torren is not a conscious/eligible normal combatant when the affected round's initiative is established, the pending initiative-routing effect fails and ordinary initiative is used.
- If Torren is eligible at initiative setup but later loses his action on his turn, his turn opportunity still occurs; the routed ally/allies remain immediately after that Torren turn slot.
- Source-owned route/link states are Torren-authored constructs and are not ordinary harmful statuses.

## Awakened Prime and normal-round route clocks
Routeweaver's authored route states use **normal-party-round** timing unless an effect explicitly says otherwise.

During an Awakened Prime manifestation:
- Prime rounds do **not** consume the normal-round duration checkpoints of **Throughline**, **Crossroads**, or Route Weaving Rank I's stored next-damaging-Ability window;
- those states remain attached/recorded through suspension unless their own target/link condition ends, such as a linked enemy being defeated or replaced;
- Prime commands do not consume Throughline's MP discount because they are not allied MP-costing Abilities or Standard Cards and already cost 0 MP;
- Prime commands do not trigger Crossroads because they are not qualifying allied Abilities or Standard Cards;
- Prime commands do not count as an ally benefiting from a Routeweaver route effect for Route Weaving Rank II or III;
- **Set the Pace** follows the global temporary-stat pause rule while its ordinary-party subject is suspended.

**Covered Crossing** and **Open the Way** are pending next-**normal-round** initiative effects. If Awakened Prime manifestation begins before that initiative setup occurs, the pending routing waits through the Prime rounds and attempts to resolve at the first normal-round initiative setup after the party returns. Torren's normal eligibility check is made at that setup; if he is not eligible then, the routing fails exactly as otherwise authored.

## Ability spine
| Unlock | Ability | MP | Current effect |
|---:|---|---:|---|
| CL1 | **Throughline** | 12 | One enemy; Hybrid / Neutral **50/50**; **160 Power**; **105 Base Hit**. On hit, establish **Throughline** on that enemy through the remainder of the current round plus the next **2 full normal rounds**. The first allied MP-costing Ability or Standard Card each round that targets the Throughlined enemy costs **20% less MP**, rounded normally, minimum 1 MP. Prime actions are unaffected. Only one enemy may carry Torren's Throughline at once; applying it elsewhere moves the route. |
| CL4 | **Set the Pace** | 15 | **Power: N/A — no direct damage.** One ally gains **Speed +20% for 3 rounds**. Reapplication refreshes rather than stacks. Current-round initiative is not reshuffled. |
| CL7 | **Crossroads** | 24 | **Power: N/A for the link itself.** Link two enemies for **3 rounds**. **Once per round**, when an ally completes a direct-damage Ability or Standard Card that damages exactly one linked enemy, the other linked enemy takes secondary routed damage equal to **40% of the total final direct damage dealt to the struck linked enemy by that action**. One proc per qualifying action regardless of hit count. If the triggering action directly damages both linked enemies, Crossroads does not trigger. Routed damage cannot Crit, reapply statuses, trigger follow-ups, trigger Crossroads again, or pass through Defense/Spirit a second time. Ultimates do not trigger Crossroads. If either linked enemy is defeated, the link ends. |
| CL9 | **Covered Crossing** | 20 | **Power: N/A — no direct damage.** Choose one conscious ally. At the next normal round's initiative setup, if Torren is conscious and eligible for a normal turn, remove that ally's ordinary Speed-derived slot and insert their normal turn **immediately after Torren's normal turn slot**, regardless of relative Speed. The ally still receives exactly one normal turn. If Torren is not eligible when initiative is established, Covered Crossing fails and the ally keeps ordinary initiative. |
| CL11 | **Frozen Passage** | 29 | All enemies; Magical / Ice; **195 Power per target**; **100 Base Hit**; base **20% Freeze** per target. Against an enemy that has not yet taken its normal turn this round, Freeze chance becomes **35%**. Against an enemy that already acted, it remains 20%. Resolve separately per target. |
| CL13 | **Open the Way** | 53 | Subclass Ultimate. Choose up to **3 other conscious allies** and order them. At the next normal round's initiative setup, if Torren is conscious and eligible for a normal turn, remove the selected allies' ordinary Speed-derived slots and insert their normal turns **immediately after Torren's normal turn slot in the chosen order**. Each selected ally still receives exactly one normal turn. Each routed action gains **+10 Base Hit / application reliability** and costs **20% less MP**, rounded normally, minimum 1 MP. If Torren is not eligible when initiative is established, Open the Way's routing fails and all selected allies retain ordinary initiative. Prime manifestation sequencing is unaffected. |

## Masteries
| Unlock | Mastery | Current effect |
|---:|---|---|
| CL3 | **Long Sight** | Throughline's post-application full-round window increases by **1 full normal round**. |
| CL5 | **Guided Crossing** | Set the Pace **Speed +20% → +30%**. A Covered Crossing ally also gains **+10 Evasion** from the moment their routed turn slot begins until that routed action finishes resolving. |
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
