# Archive Leviathan — True-Battle Certified

**Chapter:** 2
**Scene:** S013 — Sunken Archive
**Status:** **v97 TRUE-BATTLE CERTIFIED / RETAIN — HP / RAW OFFENSE / DIRECT-DAMAGE POWERS CLOSED**

## Actual player-state reference
Chapter 2 starts around Lv5.

Archive Leviathan is the first fixed named/story EXP reward in Chapter 2.

Central route:
> **Lv6**

Completionist/high-side route:
> **Lv7**

The completionist route can carry Chapter-1 optional EXP into Chapter 2, and the Archive Duplicant is optional before the basin. Do not balance the mandatory boss around that optional advantage.

## Current raw line

| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | **1,900** | **50** | **52** | 31 | 33 | 25 | 0 | 5 |

## Architecture
- one continuous HP bar
- visible Recorded Pattern behavior
- only completed eligible actions may be recorded
- no hidden command reading
- same-bar Emergent state
- no HP refill
- no transition damage
- no fresh body
- no Prime refresh
- no Water element

## Recovered signatures

### Leviathan Rend
- one party member
- Physical / Neutral
- **220 Power**
- Base Hit **100**
- **25% Bleed**
- 1-round repetition lock

### Vault Crash
- all conscious party members
- Physical / Neutral
- **140 Power per target**
- Base Hit **95**
- **15% Staggered per target**
- 2-round repetition lock

### Archive Undertow
- Emergent state only
- all conscious party members
- Magical / Colorless
- **150 Power per target**
- Base Hit **100**
- no harmful-status rider
- 2-round repetition lock
- aquatic presentation does **not** create a Water element

## Lv6 throughput proof
Against DEF31:

| Character | Basic Attack |
|---|---:|
| Cyanis | 51.24 |
| Ilyra | 37.80 |
| Torren | 58.58 |
| Maevra | 30.86 |

Total:
> **178.48 damage per all-basic party round**

Inherited 2,592 HP:
> **14.52 all-basic rounds**

Recovered legal premium substitutions add about:
> **+262.48 damage**

across the available MP budget over their replaced basic attacks.

That places the recovered ten-round no-heal envelope around:
> **2,047 damage**

The prior working analysis supported an HP corridor of:
> **1,800–1,950**

Current center:
> **1,900 HP**

## Round target

| Route | Target |
|---|---:|
| Mandatory aggressive | ~8–9 |
| Mandatory normal | **~9–10** |
| Completionist / Lv7 high-side | **~8–9** |
| Safety / heavier mechanic response | ~10–11 |

Completionists are intentionally allowed to finish somewhat faster.

## Raw-offense certification

Current raw offense:
- **ATK 50**
- **MAG 52**

### Leviathan Rend — 220 Power
Approximate Lv6 direct damage:
- Cyanis **42.3**
- Ilyra **59.8**
- Torren **57.3**
- Maevra **64.0**

### Vault Crash — 140 Power per target
Approximate Lv6 direct damage:
- Cyanis **26.9**
- Ilyra **38.0**
- Torren **36.5**
- Maevra **40.7**

### Archive Undertow — 150 Power per target
Approximate Lv6 direct damage:
- Cyanis **38.6**
- Ilyra **33.8**
- Torren **44.1**
- Maevra **47.2**

## Recorded Pattern — v97 exact deterministic trigger
Recorded Pattern itself is:
> **Power: N/A — no direct damage**

Recorded Pattern reacts to **repeated completed offense**; it does not randomly record an unrelated first use and never predicts a menu choice.

Eligible actions:
- Basic Attack;
- direct-damage Ability;
- direct-damage Standard Card.

Items, healing/support-only commands, unresolved reactions/counters, and Prime commands are not eligible.

Exact trigger:
1. Track each actor's most recently completed eligible direct-damage action identity.
2. If that actor next completes the **same exact eligible direct-damage action** on their next offensive action, that use is a repeat candidate.
3. A non-eligible action by that actor breaks that actor's consecutive-offense repetition chain.
4. The repeat that creates the candidate deals full damage; the Pattern never taxes the triggering hit retroactively.
5. At the end of the full party round, if one or more repeat candidates occurred, the **last repeated eligible action to resolve that round** becomes the single visible Recorded Pattern.
6. Identity is actor-qualified: Cyanis's Basic Attack and Ilyra's Basic Attack are different action identities.

While active, using that same actor-qualified action against the Leviathan causes:
> **20% less final direct damage from that action**

No status, penetration, healing, resource, or support component is copied or modified.

Duration:
- State A — **2 full party rounds**;
- State B / Emergent — newly recorded patterns last **1 full party round**;
- a later qualifying repeat may replace/refresh the single Pattern; Patterns never stack.

Same-bar emergence threshold:
> **45% HP**

At threshold there is no refill, transition damage, fresh body, or Prime refresh. Any already-active Pattern keeps its remaining duration.

## v97 representative true-battle certification
Using the exact Chapter-2 party state and v96 Bleed rules, 20,000-run prepared distributions produced:

| Route | Win rate | Mean rounds | Median | 10th–90th | Any-KO incidence | Mean party HP left |
|---|---:|---:|---:|---:|---:|---:|
| Mandatory Lv6 | **100%** | **10.05** | **10** | 9–11 | **0.05%** | **53.74%** |
| Completionist/high-side Lv7 | **100%** | **8.58** | **9** | 8–9 | **0%** | **59.02%** |

The prepared mandatory test uses legal early-core stock: 3 Field Salves, 2 Trauma Remedies, and 1 Rousing Salts. It is a reproducible test inventory, not a new free story grant.

A no-item mandatory stress line still won 99.955% of runs but produced 40.96% any-KO incidence, confirming that the stronger v96 Bleed now makes cleansing/consumable preparation materially valuable.

Full snapshot, policy, distributions, and representative turn log:
`../../16_BALANCE_AND_TESTING/TRUE_BATTLES/ARCHIVE_LEVIATHAN_TRUE_BATTLE_v97.md`

## Verdict
> **v97 TRUE-BATTLE PASS / RETAIN / POWER COMPLETE**

Closed:
- HP **1,900**
- route level references
- duration target
- architecture
- status/accuracy/repetition fields
- deterministic Recorded Pattern formation trigger
- Recorded Pattern 20% effect/duration
- 45% same-bar emergence threshold
- representative mandatory/completionist design-layer true battle

Direct-damage Power remains closed.
