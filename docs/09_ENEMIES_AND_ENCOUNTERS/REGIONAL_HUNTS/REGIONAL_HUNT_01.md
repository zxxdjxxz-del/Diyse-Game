# Diyse — Regional Hunt #1: Cistern Devourer
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later accepted active-balance specifications.  
**Scaling:** fixed authored tuning; no dynamic player-level scaling.


**Recommended Lv:** 7  
**Status:** **POWER COMPLETE / v78 MAEVRA-CORRECTED DIFFICULTY VALIDATED**

| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | **2,706** | **43** | 26 | 30 | 27 | 24 | 5 | 5 |

## Actions

### Cistern Maw
- Physical / Neutral / one target
- **205 Power**
- Base Hit100

### Devouring Rend
- Physical / Neutral / one target
- **220 Power**
- Base Hit100
- **25% Bleed**
- 1-round repetition lock

### Cold Undertow
- Magical / Ice / all conscious party members
- **145 Power per target**
- Base Hit100
- 2-round repetition lock

Cold Undertow does **not** inflict Freeze because this Hunt is available in the Chapter-1 status window.

### Submerged Guard
> **Power: N/A — no direct damage**

Effect:
> **+10 Total Defense through the end of the following round**

2-round repetition lock.

## Architecture
One HP bar.
No support wave.
No transformation.


## v77 access-vs-recommendation validation
- unlock state: after S011, mandatory route approximately Lv5;
- plausible prepared/completionist immediate-return state: roughly Lv5–6;
- fixed recommendation: **Lv7**.

The early access gap is intentional. The Hunt is not dynamically reduced to Lv5 story strength.

Result:
> **RETAIN CURRENT FIXED BODY AND POWERS**


## v78 Maevra correction
Post-Torren attempts use Cyanis + Ilyra + Torren + Maevra, not a three-person party. At recommended Lv7, four-person all-basic throughput against DEF30 is still only about 178–179 damage/round, leaving 2,706 HP at roughly 15 basic-only rounds before premium actions and Submerged Guard.

> **PASS — RETAIN**
