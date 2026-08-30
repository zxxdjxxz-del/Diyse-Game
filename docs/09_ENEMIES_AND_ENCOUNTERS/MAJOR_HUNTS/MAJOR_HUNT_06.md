# Diyse — Major Hunt #6: The Unfinished World
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary enemy-production authority:** compatible **Audit90 / Audit93** plus accepted later tracker roster/action cleanups.  
**Primary raw-stat authority:** **Audit129 + Audit130 / Audit131 / Audit132 / Audit133 / Audit134 / Audit135**.  
**Current whole-project written authority:** **v2.20 / Audit135**.  
**Migration rule:** later current names, chapter reindexing, four-element rules, removed-system firewalls, and fresh-body Prime-refresh rules supersede stale earlier enemy text.


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

## Power-complete action kit — v74
**Status:** **POWER COMPLETE**

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


## v88 mandatory-vs-completionist recertification
**Status:** **TWO-BASELINE PAPER RECERTIFIED / RUNTIME DURATION GATE REMAINS**

- mandatory-route level immediately after Vaelkor: **Lv56**, chapter clear **Lv57**;
- because Final Archive Arbiter clear is a prerequisite, a route clearing it only after Vaelkor reaches about **Lv58** from the Arbiter reward and is still intentionally far below preparedness;
- exhaustive completionist after Chapter-12 clear + RH11 + post-Vaelkor `What We Build After`: approximately **Lv68**;
- recommendation remains **Lv70**;
- on a deliberately fragile unequipped Lv68 Green Arcanist reference, Final Construction is roughly **44% Max HP** and prepared Worldfall roughly **37% per target**;
- no healthy-character one-shot appears on that fragile reference; geared endgame parties are materially safer;
- the 78,000-HP duration still requires runtime testing with full Ultimates/Cards/Primes/Relics/Legacies before final production certification.

Retain all current raw stats, state thresholds, Powers, and same-bar Prime rules.
