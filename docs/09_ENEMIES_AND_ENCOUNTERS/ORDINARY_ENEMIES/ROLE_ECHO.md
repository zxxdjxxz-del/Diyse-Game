# Role Echo

**Chapter:** 7 — Prison of Names  
**Status:** **POWER COMPLETE / BOUNDED ECHO RULE**

Role Echo never predicts a player command and never erases or changes permanent class identity.

## Body
| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 31 | **820** | **102** | **112** | 62 | 70 | 40 | 5 | 10 |

## Actions

### Echo Strike
- one party member
- Hybrid / Neutral
- **50% ATK / 50% MAG**
- **190 Power**
- Base Hit100

### Replayed Role
The Echo records the most recent completed eligible direct-damage party action.

Eligible:
- Attack;
- direct-damage Ability;
- direct-damage Standard Card.

Not eligible:
- Items;
- Defend;
- healing/support-only actions;
- counters/reactions;
- summons;
- Ultimates;
- Prime Invocation / Prime commands.

Recording happens:
> **only after the party action actually completes**

On a later selected Role Echo action:

> **Power = clamp(round(source total Power × 0.70), 100, 220)**

Also:
- Base Hit100;
- preserve source damage school / element;
- preserve source target shape;
- preserve source physical/magical/hybrid weighting;
- use Role Echo's own ATK/MAG.

Multi-hit:
- convert source total Power first;
- preserve hit count;
- split converted total as evenly as possible.

Replayed Role does **not** copy:
- status riders;
- penetration;
- healing/drain;
- stat/resource effects;
- forced targeting;
- extra actions;
- once-per-battle gates.

It cannot alter:
- permanent class;
- Masteries;
- equipment;
- Cards;
- character identity.

This is a bounded combat echo, not identity theft.
