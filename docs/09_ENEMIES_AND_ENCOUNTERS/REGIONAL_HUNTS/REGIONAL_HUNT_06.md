# Diyse — Regional Hunt #6: Winterglass Titan
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later accepted active-balance specifications.  
**Scaling:** fixed authored tuning; no dynamic player-level scaling.


**Recommended Lv:** 32  
**Status:** **POWER COMPLETE**

| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 32 | **10,879** | **101** | **125** | 90 | 94 | 34 | 0 | 10 |

True construct:
> **Bleed Immune**

## State A — Frozen Shell
From 100% HP through above 50% HP:
> **+15 Total Defense**

### Winterglass Fist
- Physical / Neutral / one target
- **300 Power**
- Base Hit100

### Frostline
- Magical / Ice / all conscious party members
- **225 Power per target**
- Base Hit95
- **20% Freeze per target**
- 2-round repetition lock

### Shell Resonance
- Magical / Ice / one target
- **285 Power**
- Base Hit100
- 2-round repetition lock

## 50% — Thawed Core
At first reaching 50% HP:
- Frozen Shell's +15 Total Defense ends;
- Speed +10 for the rest of battle;
- Attack +10% / Magic +10% for the rest of battle;
- unlock Core Crush and Glassburst.

This is:
> **same-bar escalation**

No HP refill.
No Prime refresh.

### Core Crush
- Physical / Neutral / one target
- **335 Power**
- Base Hit95
- **25% Staggered**
- 2-round repetition lock

### Glassburst
- Magical / Colorless / all conscious party members
- **245 Power per target**
- Base Hit95
- 2-round repetition lock

## Architecture
One continuous HP bar:
> Frozen Shell → Thawed Core

No fresh body.


## v82 mandatory-vs-completionist check
Retained without numerical change. See `../../16_BALANCE_AND_TESTING/BALANCE/CHAPTER_06_MANDATORY_COMPLETIONIST_VALIDATION.md`.
