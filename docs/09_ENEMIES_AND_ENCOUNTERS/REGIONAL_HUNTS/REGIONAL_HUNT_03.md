# Diyse — Regional Hunt #3: Archive Judgment Engine
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later accepted active-balance specifications.  
**Scaling:** fixed authored tuning; no dynamic player-level scaling.


**Recommended Lv:** 15  
**Status:** **POWER COMPLETE**

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
