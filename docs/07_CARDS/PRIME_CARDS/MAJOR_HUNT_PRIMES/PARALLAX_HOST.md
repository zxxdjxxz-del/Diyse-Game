# Diyse — Prime: Parallax Host
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Historical provenance:** Audit116/Audit119/Audit122, v85-era closures, and later approved corrections as applicable.
**Authority treatment:** this repository file is current Card/Prime-domain authority. Audit/v85 references remain provenance; later explicit corrections and current owner-domain rules supersede conflicting historical text.

**Face:** Perception  
**Source:** Major Hunt #5 — Final Archive Arbiter  
**Acquisition state:** Awakened

## Command package
| Command | Target | Formula | Power | Base Hit | Effect |
|---|---|---|---:|---:|---|
| **Double Exposure** | one enemy | Hit 1 Physical / Neutral; Hit 2 Magical / Colorless | 145 + 145 = 290 | 120 each | 25% Defense penetration on Physical hit; 25% Spirit penetration on Magical hit; no harmful status. |
| **Blind Angle** | one enemy | Automatically chooses weaker current defensive axis | 315 | 125 | 40% relevant-axis penetration; lower Defense → Physical/Neutral; lower Spirit → Magical/Colorless; deterministic tie logic, Physical default if still tied. |
| **Occluded Sightline** | all enemies | Each target independently uses weaker current defensive axis | 190 per target | 115 | 20% relevant-axis penetration; after successful damage Base Hit −15 for 2 rounds; this is an ordinary stat change. |
| **Legacy/final — Parallax Collapse** | Prime Round 3 only; all enemies | Physical / Neutral + Magical / Colorless | 150 + 150 = 300 per target | 120 each | 30% Defense penetration on Physical hit; 30% Spirit penetration on Magical hit; surviving target hit by ≥1 component gets Defense −15% and Spirit −15% for 2 full normal party rounds after dismissal. |

Parallax Host's Perception identity is battlefield reading and exploitation of defensive openings, sightlines, hit control, and positioning logic. It does not create a natural Accuracy stat.

## Global Prime references
- `../PRIME_SYSTEM_RULES.md`
- `../PRIME_SCALING.md`
- `../PRIME_STATUS_CONTROL.md`
- `../../../05_BATTLE_SYSTEM/PRIME_ROUND_SEQUENCING.md`

## Ruin formula scope
If this Prime contains Ruin damage, use the command's explicitly authored Prime formula.
Do **not** force the character-Ability 75/25 Ruin rule onto a Prime command.
