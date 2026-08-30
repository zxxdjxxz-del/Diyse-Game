# Diyse — Regional Hunt #7: Rift Gate Colossus
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later accepted active-balance specifications.  
**Scaling:** fixed authored tuning; no dynamic player-level scaling.


**Recommended Lv:** 38  
**Status:** **VALIDATED v83 / POWER COMPLETE**

| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 38 | **13,276** | **144** | **127** | 107 | 98 | 36 | 0 | 10 |

True construct:
> **Bleed Immune**

## Actions

### Gate Hammer
- Physical / Neutral / one target
- **325 Power**
- Base Hit100

### Rift Cannon
- Magical / Ruin / one target
- **320 Power**
- Base Hit100

### Gate Pulse
- Magical / Ruin / all conscious party members
- **235 Power per target**
- Base Hit95
- 2-round repetition lock

### Gate Guard
> **Power: N/A — no direct damage**
- +15 Total Defense through end following round
- 2-round repetition lock

## 50% — Marching Protocol
At first reaching 50% HP:
- Speed +10 for the rest of battle;
- Total Defense −10 for the rest of battle;
- unlock Marching Crush.

No HP refill.
No Prime refresh.

### Marching Crush
- Physical / Neutral / one target
- **355 Power**
- Base Hit95
- **25% Staggered**
- 2-round repetition lock

## Architecture
One continuous HP bar.

"Gate Form" / "Marching" is presentation and same-bar escalation only.
