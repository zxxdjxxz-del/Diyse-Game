# Calamity Memory

**Chapter:** 13 — Final Domain  
**Status:** **POWER COMPLETE / BOUNDED MEMORY RULE**

Calamity Memory is a combat-memory construct.
It is not another Entity fragment or independent ancient survivor.

## Body
| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 62 | **1,720** | **194** | **226** | 112 | **126** | 44 | 5 | 15 |

## Actions

### Memory Rupture
- one party member
- Hybrid / Ruin
- **75% ATK / 25% MAG**
- **255 Power**
- Base Hit100

### Calamity Replay
Records the most recent completed eligible direct-damage party action.

On a later selected Calamity Replay:

> **Power = clamp(round(source total Power × 0.85), 140, 300)**

Eligibility and recording timing match Devouring Echo:
- only after the action completes;
- Attack / direct-damage Ability / direct-damage Standard Card only;
- no Items, Defend, support-only, reactions, summons, Ultimates, Prime Invocation, or Prime commands.

Rules:
- Base Hit100;
- preserve damage school/element;
- preserve target shape;
- preserve physical/magical/hybrid weighting;
- use Calamity Memory's own ATK/MAG.

Multi-hit:
- convert total Power first;
- preserve hit count;
- split converted total as evenly as possible.

Calamity Replay does **not** reproduce:
- status riders;
- penetration;
- healing/drain;
- stat/resource effects;
- forced targeting;
- extra actions;
- once-per-battle gates.

No prediction.
No permanent-state rewrite.
