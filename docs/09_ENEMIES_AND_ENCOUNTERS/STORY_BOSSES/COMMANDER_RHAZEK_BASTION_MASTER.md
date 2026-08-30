# Commander Rhazek — Bastion Master — Current Working Recertification

**Chapter:** 2  
**Scene:** S015 — Red Transfer Bastion  
**Status:** **v78 VALIDATED / POWER COMPLETE**

## Actual party reference

Central mandatory route:
> **~Lv7**

Completionist route:
> **~Lv8**

High-side completionist / extra optional combat:
> can approach **Lv9**

Rationale:
- Chapter 2 begins around Lv5.
- Archive Leviathan occurs earlier in S013.
- Prisoner Galleries and substantial mandatory exploration/combat occur before S015.
- Chapter-1 optional EXP can enter Chapter 2, so a completionist is meaningfully ahead by the Rhazek fight.
- The boss is tuned primarily around the ~Lv7 mandatory route.

## Current raw line

| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | **2,050** | **58** | **44** | **36** | **32** | **27** | **5** | **5** |

The former 2,700 HP / ATK49 / MAG31 line is superseded for the current working balance pass.

## Architecture
- one continuous HP bar
- State A: **Bastion Master**
- State B: **Bastion Master — Ruin Escalation**
- threshold at **45% HP**
- no HP refill
- no free threshold attack
- no fresh body
- no Prime refresh
- finite support only
- destroyed support remains destroyed

At the 45% threshold:
- Rhazek's armor reinforcement activates;
- Rhazek gains **Defense +6% / Spirit +6% for the rest of battle**;
- State-A support does not respawn;
- action priorities shift toward direct Ruin pressure.

## State A — Bastion Master

### Commander's Cut
- one party member
- Physical / Neutral
- **180 Power**
- Base Hit **100**
- no harmful-status rider

### Shieldline Break
- one party member
- Physical / Neutral
- **220 Power**
- Base Hit **95**
- **20% Staggered**
- 1-round repetition lock

### Command-Link Pulse
- all conscious party members
- Magical / Colorless
- **135 Power per target**
- uses Rhazek's Magic
- Base Hit **100**
- no harmful-status rider
- 2-round repetition lock

### Hold the Bastion
> **Power: N/A — no direct damage**

Rhazek takes **10% less direct damage through the end of the following round**.

This is an intentional defensive choice, not Brace.

## Finite support

### Bastion Shield Detachment

| HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|
| **180** | 0 | 0 | **42** | **36** | 24 | 0 | 5 |

#### Shield Screen
> **Power: N/A — no direct damage**

While the detachment survives during State A:
> Rhazek takes **10% less eligible direct damage**.

The detachment does not respawn.

### Bastion Ranged Position

| HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|
| **150** | **52** | 0 | **26** | **24** | **29** | 0 | 5 |

#### Crossfire Bolt
- one party member
- Physical / Neutral
- **165 Power**
- Base Hit **100**
- **15% Bleed**
- 1-round Reload after firing

The position does not respawn.

## State B — Bastion Master: Ruin Escalation

### Ruin-Driven Cut
- one party member
- Hybrid / Ruin
- **75% ATK / 25% MAG**
- **210 Power**
- Base Hit **100**
- **20% Bleed**
- no repetition lock

### Bastion Breaker
- one party member
- Hybrid / Ruin
- **75% ATK / 25% MAG**
- **250 Power**
- Base Hit **95**
- **20% Staggered**
- 2-round repetition lock

### Ruin Sweep
- all conscious party members
- Hybrid / Ruin
- **75% ATK / 25% MAG**
- **145 Power per target**
- Base Hit **95**
- no harmful-status rider
- 2-round repetition lock

### Reinforced Advance
> **Power: N/A — no direct damage**

Rhazek gains **Speed +10% through the end of the following round**.

No extra action is granted.

## Incoming-pressure check

Using the recovered Lv6 defense profile as a conservative floor means the real ~Lv7 mandatory party should take slightly less damage than the values below.

Approximate direct damage:

| Action | Cyanis | Ilyra | Torren | Maevra |
|---|---:|---:|---:|---:|
| Commander's Cut | 43.9 | 60.6 | 58.2 | 64.4 |
| Shieldline Break | 53.6 | 74.0 | 71.2 | 78.7 |
| Command-Link Pulse | 26.9 | 23.3 | 31.1 | 33.5 |
| Ruin-Driven Cut | 48.9 | 62.1 | 63.0 | 69.4 |
| Bastion Breaker | 58.2 | 73.9 | 75.1 | 82.6 |
| Ruin Sweep | 33.7 | 42.8 | 43.5 | 47.9 |

Bastion Ranged Position — Crossfire Bolt:
- Cyanis ~33.8
- Ilyra ~47.5
- Torren ~45.5
- Maevra ~50.7

Bleed and Staggered are resolved separately from the direct damage.

## Duration check

Recovered Lv6 basic-Attack floor against DEF36:
> approximately **170 direct damage per full party round**

The actual ~Lv7 mandatory party should exceed that floor.

The 2,050-HP body therefore sits around:
> **12 basic-only floor rounds**

before class Abilities, critical hits, and other efficient actions.

Finite support and State-A mitigation add tactical action tax, while class Abilities pull the clear time back down.

Expected authored pacing:
- mandatory aggressive: **~9–10 rounds**
- mandatory normal: **~10–11 rounds**
- completionist ~Lv8: **~8–9 rounds**
- high-side ~Lv9: **~7–8 rounds**
- safety/support-clearing route: **~11–12 rounds**

This preserves a meaningful optional-progression advantage without dynamically scaling Rhazek upward.

## Power-completeness verdict
Every direct-damage action in the encounter has exact numeric Power.

Non-damaging commands are explicitly Power N/A.

> **WORKING PASS / POWER COMPLETE**

## Story boundary
- Rhazek is defeated at 0 HP but survives.
- He withdraws after the battle.
- the party prioritizes opening the evacuation route.
- no Reforged Commander or Bastion Devourer appears in Chapter 2.


## v78 broader Chapter-2 validation
The full Lv5→9 Chapter-2 pass confirms the existing ~Lv7 mandatory / ~Lv8 completionist calibration with Maevra included as the fourth combatant. No raw stat, support, phase, or Power change is required.

> **PASS — RETAIN**
