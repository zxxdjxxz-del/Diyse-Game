# Diyse — Major Hunt #3: Concordance Guardian

**Status:** ACTIVE MAJOR-HUNT ENCOUNTER BODY — REVALIDATION PENDING  
**Authority:** current enemy/encounter owner plus later explicit approved corrections.  


| Ref | Encounter / form | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR | Architecture |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| — | **Concordance Guardian** | 54 | 27,400 | 194 | 210 | 144 | 151 | 49 | 5 | 15 | one bar / Six Faces → Open Concordance same-bar |

## Unlock
After **Sixfold Volition at the end of Chapter 7**.

## Architecture
Six Faces → Open Concordance remains on one continuous HP bar. Do not create six separate boss bodies.

## Scaling
Fixed authored tuning.
No dynamic player-level scaling.


## Current action kit

Enemies do **not** use Cards or Prime Invocation.
The six Face states are encounter states only.

## Six Faces
At encounter load:
> **Might**

At each later beginning-round, advance:
> Might → Elements → Grace → Perception → Memory → Ruin → Might

The state change:
- grants no extra action;
- does not remove player commands;
- does not alter permanent player state.

### Face Verdict
Face Verdict changes by the current Face.

#### Might Verdict
- Physical / Neutral / one target
- **350 Power**
- Base Hit100
- **25% Staggered**

#### Elements Verdict
Two-hit Magical command.

Odd-numbered Elements appearances:
- hit 1 — Fire — **180 Power**
- hit 2 — Ice — **180 Power**

Even-numbered Elements appearances:
- hit 1 — Lightning — **180 Power**
- hit 2 — Earth — **180 Power**

Base Hit100 per hit.

Each hit may attempt its linked status at **15%**:
- Fire → Burn
- Ice → Freeze
- Lightning → Stun
- Earth → Staggered

Maximum:
> **1 newly inflicted harmful status from the whole command**

#### Grace Verdict
- Magical / Colorless / one target
- **330 Power**
- Base Hit100
- after successful damage, restore **600 HP** to Concordance Guardian
- cannot exceed Max HP

#### Perception Verdict
- Magical / Colorless / one target
- **345 Power**
- Base Hit110

#### Memory Verdict
- Hybrid / Neutral
- 50% ATK / 50% MAG
- **350 Power**
- Base Hit100
- after resolution: Attack +10% / Magic +10% through end following round

#### Ruin Verdict
- Magical / Ruin / one target
- **365 Power**
- Base Hit100

### Concordance Pulse
- all conscious party members
- Magical / Colorless
- **255 Power per target**
- Base Hit95
- 2-round repetition lock

## Open Concordance
At first reaching:
> **50% HP**

Six-Face cycling ends.

For the remainder of battle:
- Attack +10%
- Magic +10%
- Speed +10%
- Defense −10%
- Spirit −10%

No HP refill.
No Prime refresh.
No free transition action.

Unlock:

### Open Verdict
- one party member
- Hybrid / Ruin
- **50% ATK / 50% MAG**
- **405 Power**
- Base Hit100

### Sixfold Wave
- all conscious party members
- Magical / Colorless
- **305 Power per target**
- Base Hit95
- 2-round repetition lock

### Open Revision
> **Power: N/A — no direct damage**

Effect:
> Defense +10% / Spirit +10% through the end of the following round

2-round repetition lock.

