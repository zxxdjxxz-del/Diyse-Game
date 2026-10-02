# Diyse — Major Hunt #6: The Unfinished World

**Status:** ACTIVE MAJOR-HUNT ENCOUNTER BODY — REVALIDATION PENDING  
**Authority:** current enemy/encounter owner plus later explicit approved corrections.  


| Ref | Encounter / form | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR | Architecture |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| — | **The Unfinished World** | 70 | 78,000 | 304 | 318 | 226 | 232 | 61 | — | 15 | one bar / three same-bar states |

## Unlock
After **Final Archive Arbiter is cleared** and **Vaelkor is defeated in Chapter 12**.

## Architecture
Exactly one 78,000-HP bar: WORLDFRAME → WORLDHEART EXPOSED → FINAL CONSTRUCTION. No second/third HP bar and no hidden post-defeat body.

## Scaling
Fixed authored tuning.
No dynamic player-level scaling.

## Current action kit

This encounter has exactly:
> **one 78,000-HP bar**

No state transition refreshes Prime availability.

## State I — WORLDFRAME
From 100% HP through above 70% HP:
> **Defense +15% / Spirit +15%**

### Frame Hammer
- one party member
- Physical / Neutral
- **475 Power**
- Base Hit95
- **30% Staggered**
- 2-round repetition lock

### Worldline Ruin
- one party member
- Magical / Ruin
- **465 Power**
- Base Hit100

### Foundation Storm
At encounter load use Fire; on each later Foundation Storm selection advance:
> Fire → Ice → Lightning → Earth → Fire

- all conscious party members
- Magical / current standard element
- **345 Power per target**
- Base Hit95

Linked harmful status:
> **20% per successfully damaged target**

Fire→Burn / Ice→Freeze / Lightning→Stun / Earth→Staggered.

2-round repetition lock.

### Frame Guard
> **Power: N/A — no direct damage**

Effect:
> Defense +10% / Spirit +10% through end following round

2-round repetition lock.

## State II — WORLDHEART EXPOSED
At first reaching:
> **70% HP**

WORLDFRAME's Defense +15% / Spirit +15% ends.

For the remainder of this state:
- Magic +10%
- Speed +10%
- Defense −10%
- Spirit −10%

No HP refill.
No Prime refresh.
No free action.

Unlock:

### Worldheart Flare
- one party member
- Magical / Colorless
- **500 Power**
- Base Hit100

### Confluence Rupture
Two-hit Magical command.

Use the current Foundation Storm element and the next element in cycle:
- hit 1 — **280 Power**
- hit 2 — **280 Power**

Total:
> **560 Power**

Base Hit100 per hit.

Each hit may attempt its linked harmful status at **20%**.

Maximum:
> **1 newly inflicted harmful status from the whole command**

### Heart Rupture
- all conscious party members
- Magical / Ruin
- **370 Power per target**
- Base Hit95
- 2-round repetition lock

## State III — FINAL CONSTRUCTION
At first reaching:
> **35% HP**

For the remainder of battle:
- Attack +15%
- Magic +15%
- Speed +10%
- Defense −15%
- Spirit −15%

These replace the State-II modifiers rather than stacking with them.

No HP refill.
No Prime refresh.
No free transition action.

Unlock:

### Final Construction
- one party member
- Hybrid / Ruin
- **50% ATK / 50% MAG**
- **540 Power**
- Base Hit100

### Unfinished End
- all conscious party members
- Magical / Ruin
- **390 Power per target**
- Base Hit95
- 2-round repetition lock

### Worldfall Preparation
> **Power: N/A — no direct damage**

Rules:
- consumes The Unfinished World's selected action;
- locks Worldfall as its next selected action if it remains able to act;
- cannot be selected while Worldfall is already prepared;
- no command prediction;
- no free action;
- 3-round repetition lock begins after Worldfall resolves.

### Worldfall
- all conscious party members
- Hybrid / Ruin
- **75% MAG / 25% ATK**
- **450 Power per target**
- Base Hit95
- **30% Staggered per target**

Worldfall is legal only after Worldfall Preparation.

## Final architecture firewall
No:
- fresh second body;
- hidden fourth state;
- post-defeat body;
- extra-action system;
- new normal element;
- permanent player-state rewrite.

Standard elements remain:
> Fire / Ice / Lightning / Earth

Ruin remains a special damage school.

