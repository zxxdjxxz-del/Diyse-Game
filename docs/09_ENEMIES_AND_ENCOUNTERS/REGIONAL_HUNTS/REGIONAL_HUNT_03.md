# Diyse — Regional Hunt #3: Archive Judgment Engine
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later accepted active-balance specifications and Chapter-3 cleanup corrections.  
**Scaling:** fixed authored tuning; no dynamic player-level scaling.

**Recommended Lv:** 15  
**Status:** **POWER COMPLETE**

## Story access / placement
- **Archive Judgment Engine is optional Chapter-3 cleanup content.**
- it becomes available only after the mandatory Old City / First Command Warden sequence is resolved and **Cresthaven has been established as the party's headquarters**.
- the Hunt is a **return to the Old City Archive complex in Caelora**, using a deeper / side Archive branch that was not part of the mandatory S019–S021 route.
- the permanent combat party for the Hunt is **Cyanis + Ilyra + Torren + Nimera**.
- after the Cresthaven handoff, **Maevra has returned to Caelora with Mirena and is no longer a default traveling companion**; neither Maevra nor Mirena joins this Hunt as a combatant.
- lawful Crown / archive access may permit the return, but the Hunt does not require either woman to accompany the party through the branch.
- the Hunt does **not** solve the Queen-seal mystery, expose Calder's hidden role, recover / manifest Last Sentinel, or reveal the destination of the Ancient route continuing north beyond Cresthaven.
- completing or skipping the Hunt does not block the player's ability to begin Chapter 4 from Cresthaven.

| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 15 | **4,928** | **58** | **67** | 46 | 48 | 28 | 0 | 10 |

True construct:
> **Bleed Immune**

## Actions

### Judgment Lance
- Physical / Neutral / one target
- **245 Power**
- Base Hit100

### Archive Verdict
- Magical / Colorless / all conscious party members
- **175 Power per target**
- Base Hit100
- 2-round repetition lock

### Lock Verdict
- Magical / Lightning / one target
- **230 Power**
- Base Hit100
- **25% Stun**
- 2-round repetition lock

### Enforcement Crash
- Hybrid / Neutral / 50% ATK / 50% MAG / one target
- **270 Power**
- Base Hit95
- 2-round repetition lock

### Record Guard
> **Power: N/A — no direct damage**
- Defense +10% / Spirit +10% through end following round
- 2-round repetition lock

## Architecture
One HP bar.
No permanent record/name/player-state alteration.
