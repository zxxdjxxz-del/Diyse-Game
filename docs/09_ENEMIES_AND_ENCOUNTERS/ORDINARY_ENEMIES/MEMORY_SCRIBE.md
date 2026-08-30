# Memory Scribe

**Chapter:** 2 — Sunken Archive  
**Story anchor:** S013 authored teaching encounter, then ordinary formations  
**Status:** **POWER COMPLETE / RAW BODY AUTHORED / COPY RULE BOUNDED**

## Body
| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | **230** | 25 | **44** | 24 | **30** | 26 | 0 | 10 |

True construct:
> **Bleed Immune**

## Actions

### Archive Bolt
- one party member
- Magical / Colorless
- **135 Power**
- Base Hit100
- no harmful-status rider

### Recorded Echo
The Scribe may reproduce a weaker version of a previously completed eligible party action.

Eligibility:
- ordinary Attack;
- a direct-damage Ability;
- a direct-damage Standard Card.

Not eligible:
- menu selection before resolution;
- healing/support-only actions;
- Items;
- Defend;
- counters/reactions;
- summons;
- Ultimates;
- Prime Invocation or Prime commands.

Recording occurs:
> **only after the eligible party action actually completes**

The most recent eligible completed action replaces the previous record.

On the Scribe's later selected action, Recorded Echo uses:
- source damage school / element;
- source target shape;
- source physical / magical / hybrid weighting;
- **Power = clamp(round(source Power × 0.65), 80, 180)**
- **Base Hit100**
- Memory Scribe's own ATK/MAG as appropriate.

Multi-hit:
- convert the source action's **total Power** first;
- preserve the original hit count;
- split converted total as evenly as possible across those hits.

Recorded Echo does **not** reproduce:
- source status riders;
- penetration;
- healing/drain;
- stat changes;
- resource effects;
- forced targeting;
- extra actions;
- special once-per-battle gates.

This is the exact bounded implementation of:
> **sees the action after it happens, then reproduces a weaker functional version**

It does not predict commands.

## S013 authored teaching encounter
The first authored Memory Scribe uses this same ordinary body and rules.

After that encounter:
> Memory Scribes may enter normal Archive formations.
