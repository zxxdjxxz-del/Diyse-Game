# Diyse — Prime Manifestation Scaling
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary Card/Prime authority:** compatible **Audit116**, superseded where applicable by **Audit119**, **Audit122**, and later current v85 working closures.  
**Current written whole-project authority:** **v2.20 / Audit135**.  


Prime manifestation uses deterministic battle-time scaling.

There is no:
- Prime Level;
- Prime EXP;
- permanent Prime stat growth;
- invoker-stat inheritance.

## Reference Level

> **Reference Level = highest current level among the four active permanent-party members at Invocation**

Clamp:
- minimum 1;
- maximum 70.

The Prime does not permanently store this level.

## Neutral manifestation baseline

At Reference Level `L`:

- HP baseline = **2.25 × Neutral HP(L)**
- Attack baseline = **4.75 × Neutral ATK(L)**
- Magic baseline = **4.75 × Neutral MAG(L)**
- Defense baseline = **1.65 × Neutral DEF(L)**
- Spirit baseline = **1.65 × Neutral SPR(L)**
- Speed baseline = **Neutral SPD(L) + 8**

## State multipliers

| State | HP | ATK/MAG | DEF/SPR | Speed |
|---|---:|---:|---:|---:|
| Recovered Story | 0.85 | 0.82 | 0.85 | 0.95 |
| Awakened Story | 1.00 | 1.00 | 1.00 | 1.00 |
| Awakened Major Hunt | 1.08 | 1.06 | 1.08 | 1.04 |

## Identity multipliers

| Prime | HP | ATK | MAG | DEF | Spirit | SPD |
|---|---:|---:|---:|---:|---:|---:|
| Last Sentinel | 1.12 | 1.16 | 0.74 | 1.18 | 0.95 | 0.90 |
| Last Cartographer | 0.96 | 1.10 | 0.82 | 0.90 | 0.92 | 1.18 |
| Last Convergence | 0.90 | 0.70 | 1.18 | 0.86 | 1.10 | 1.02 |
| Last Scribe | 0.95 | 0.78 | 1.08 | 0.94 | 1.12 | 1.08 |
| Last Sanctuary | 1.05 | 0.72 | 1.05 | 1.05 | 1.20 | 0.92 |
| Last Erasure | 1.10 | 1.12 | 1.08 | 1.08 | 0.92 | 0.90 |
| Dawn Shepherd | 1.08 | 1.05 | 1.05 | 1.00 | 1.15 | 1.00 |
| Oathbound Colossus | 1.18 | 1.20 | 0.65 | 1.22 | 0.90 | 0.82 |
| Living Revision | 1.05 | 1.00 | 1.00 | 1.03 | 1.03 | 1.05 |
| Prismatic Leviathan | 1.10 | 0.65 | 1.18 | 1.00 | 1.18 | 0.90 |
| Parallax Host | 0.98 | 1.02 | 1.02 | 0.90 | 0.90 | 1.18 |
| Starfall Engine | 1.15 | 1.12 | 1.12 | 1.08 | 0.92 | 0.88 |

## Implementation order
1. determine Reference Level;
2. calculate neutral natural stat at that level;
3. apply Prime-neutral baseline;
4. apply state multiplier;
5. apply identity multiplier;
6. round final raw stat to nearest whole number.

Do not round intermediate values.

## No invoker inheritance
Do not copy:
- invoker Attack/Magic/Defense/Spirit;
- equipment;
- current HP%;
- current buffs;
- current harmful statuses.

Prime-specific effects applied after manifestation still modify the Prime normally.
