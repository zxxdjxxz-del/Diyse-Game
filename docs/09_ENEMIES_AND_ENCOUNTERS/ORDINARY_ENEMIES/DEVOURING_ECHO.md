# Devouring Echo

**Chapter:** 13 — Final Domain  
**Status:** **POWER COMPLETE / BOUNDED ECHO RULE**

Devouring Echo is not a second surviving Entity continuity.

## Body
| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 60 | **1,360** | **174** | **206** | 100 | 116 | 45 | 10 | 15 |

## Actions

### Echo Bite
- one party member
- Hybrid / Ruin
- **75% ATK / 25% MAG**
- **235 Power**
- Base Hit100

### Devoured Replay
Records the most recent completed eligible direct-damage party action.

Eligible:
- Attack;
- direct-damage Ability;
- direct-damage Standard Card.

Not eligible:
- Item;
- Defend;
- healing/support-only actions;
- counters/reactions;
- summons;
- Ultimates;
- Prime Invocation / Prime commands.

Recording occurs only **after the source action completes**.

On a later selected Devoured Replay:

> **Power = clamp(round(source total Power × 0.75), 120, 260)**

Rules:
- Base Hit100;
- preserve source damage school/element;
- preserve source target shape;
- preserve physical/magical/hybrid weighting;
- use Devouring Echo's own ATK/MAG.

Multi-hit:
- convert total source Power first;
- preserve hit count;
- split converted total as evenly as possible.

Does **not** copy:
- status riders;
- penetration;
- healing/drain;
- resource effects;
- stat changes;
- extra actions;
- once-per-battle gates.

No command prediction.
No permanent identity/state copying.
