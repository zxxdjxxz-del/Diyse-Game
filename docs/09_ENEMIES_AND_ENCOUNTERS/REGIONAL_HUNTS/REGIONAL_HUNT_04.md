# Diyse — Regional Hunt #4: Crown Prototype
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later accepted active-balance specifications.  
**Scaling:** fixed authored tuning; no dynamic player-level scaling.


**Recommended Lv:** 20  
**Status:** **POWER COMPLETE**

| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20 | **6,503** | **81** | **68** | 57 | 54 | 33 | 5 | 10 |

## Four-element state
At encounter load:
> **Fire**

At each later beginning-round:
> Fire → Ice → Lightning → Earth → Fire

State change:
- grants no free action;
- does not create a fifth element;
- does not create a Composite Reaction system.

## Actions

### Prototype Edge
- Physical / Neutral / one target
- **265 Power**
- Base Hit100

### Crown Reaction
- Magical / current state element / one target
- **255 Power**
- Base Hit100

Current-state rider:
- Fire — **25% Burn**
- Ice — **25% Freeze**
- Lightning — **25% Stun**
- Earth — **25% Staggered**

Only the current state's rider is eligible.

### Prototype Burst
- Magical / current state element / all conscious party members
- **190 Power per target**
- Base Hit95
- no harmful-status rider
- 2-round repetition lock

### Prototype Guard
> **Power: N/A — no direct damage**
- Defense +10% / Spirit +10% through end following round
- 2-round repetition lock

## Architecture
One HP bar.
No transformation.
