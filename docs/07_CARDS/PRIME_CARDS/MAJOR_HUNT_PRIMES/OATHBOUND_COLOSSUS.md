# Diyse — Prime: Oathbound Colossus
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary Card/Prime authority:** compatible **Audit116**, superseded where applicable by **Audit119**, **Audit122**, and later current v85 working closures.  
**Current written whole-project authority:** **v2.20 / Audit135**.  


**Face:** Might  
**Source:** Major Hunt #2 — Crownless Siege Marshal / Crownless War Engine  
**Acquisition state:** Awakened

## Command package
| Command | Target | Formula | Power | Base Hit | Effect |
|---|---|---|---:|---:|---|
| **Siege Ram** | one enemy | Physical / Neutral | 330 | 105 | 40% Defense penetration; 40% Staggered; gain **Defense +10% / Spirit +10% through the end of the next Prime round, or until dismissal if dismissal occurs first**. |
| **Crownless Barrage** | all enemies | Physical / Neutral | 220 each | 100 | 20% Defense penetration; 25% Staggered per damaged target; self-heal 8% Max HP once. |
| **Iron Oath** | one enemy | Physical / Neutral | 265 | 110 | 25% Defense penetration; gain **Defense +25% / Spirit +25% through the end of the next Prime round, or until dismissal if dismissal occurs first**; arm **Oathbound Momentum** for that same deadline. Unavailable Round 3. |
| **Legacy/final — Citadel Breaker** | Prime Round 3 only; one enemy | Physical / Neutral | 430 | 105 | 55% Defense penetration; 50% Staggered; Oathbound Momentum may boost it. |

## Oathbound Momentum exact resolver
- Oathbound Momentum is a Prime-local one-use setup state.
- It grants **+20% final damage** to Oathbound Colossus's next damaging command that resolves before the end of the next Prime round, or before dismissal if dismissal occurs first.
- A non-damaging command does not consume it.
- The first damaging command consumes Oathbound Momentum after that command resolves, whether or not the attack hits or deals positive damage.
- If no damaging command uses it before the deadline, it expires unused.
- Consuming Oathbound Momentum does not end Iron Oath's separate Defense/Spirit modifier early.

## Global Prime references
- `../PRIME_SYSTEM_RULES.md`
- `../PRIME_SCALING.md`
- `../PRIME_STATUS_CONTROL.md`

## Ruin formula scope
If this Prime contains Ruin damage, use the command's explicitly authored Prime formula.
Do **not** force the character-Ability 75/25 Ruin rule onto a Prime command.
