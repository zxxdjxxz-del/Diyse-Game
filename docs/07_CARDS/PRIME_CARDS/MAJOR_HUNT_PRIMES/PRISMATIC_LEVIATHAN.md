# Diyse — Prime: Prismatic Leviathan
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary Card/Prime authority:** compatible **Audit116**, superseded where applicable by **Audit119**, **Audit122**, and later current v85 working closures.  
**Current written whole-project authority:** **v2.20 / Audit135**.  


**Face:** Elements  
**Source:** Major Hunt #4 — Worldscar Leviathan  
**Acquisition state:** Awakened

## Command package
| Command | Target | Formula | Power | Base Hit | Effect |
|---|---|---|---:|---:|---|
| **Prismatic Breath** | all enemies | Magical / chosen Fire/Ice/Lightning/Earth | 195 each | — | 30% linked Burn/Freeze/Stun/Staggered according to chosen element. |
| **Regulator Fang** | one enemy | Magical / chosen standard element | 250 | — | 25% Spirit penetration; no harmful status. |
| **Regulator Pulse** | all enemies | Magical / chosen standard element | 200 each | 110 | No status; after damage remove one eligible temporary elemental-resistance increase from each affected enemy. Cannot remove innate/permanent affinities, immunities, Fields, boss mechanics, or scripts. |
| **Prismatic Mantle** | all enemies | Magical / chosen standard element | 185 each | 110 | No status; after damage Prismatic Leviathan takes **40% less eligible direct damage from the chosen element until its next selected action begins**. This does not change its actual elemental affinity or linked-status susceptibility. |
| **Legacy/final — Prismatic Deluge** | Prime Round 3/final; all enemies | Magical sequence Fire → Ice → Lightning → Earth | 4 × 90 = 360 per target | — | Each wave may attempt its linked status at 15%; maximum 1 newly inflicted harmful status per target from the whole command; no Colorless finishing hit. |

## Prismatic Mantle exact resolver
- The chosen-element protection becomes active after Prismatic Mantle's complete damage package resolves.
- For eligible incoming **direct** damage of that chosen element while the protection is active:
  > **MantledDamage = PreMantleDirectDamage × 0.60**
- The reduction applies after the attack's ordinary elemental-affinity damage multiplier and other normal damage construction, in the same late direct-damage-reduction layer used by supported direct-damage protection.
- It does not reduce Burn, Bleed, fixed damage, indirect damage, or nonmatching elements merely because they occur while Mantle is active.
- It does not rewrite Weak / Neutral / Resistant / Strongly Resistant / Immune identity and therefore does not alter linked-status application modifiers.
- Prismatic Mantle ends immediately when Prismatic Leviathan's next selected action begins, before that action resolves.
- Reusing Prismatic Mantle later replaces the prior chosen-element protection rather than stacking another Mantle.

Current v85 working closure fixes **Prismatic Deluge at 90 Power × 4 waves = 360 total per target**. Older Audit116 OPEN wording is superseded at tracker level.

## Global Prime references
- `../PRIME_SYSTEM_RULES.md`
- `../PRIME_SCALING.md`
- `../PRIME_STATUS_CONTROL.md`

## Ruin formula scope
If this Prime contains Ruin damage, use the command's explicitly authored Prime formula.
Do **not** force the character-Ability 75/25 Ruin rule onto a Prime command.
