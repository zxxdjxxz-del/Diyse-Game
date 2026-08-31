# Diyse — Prime: Last Convergence
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary Card/Prime authority:** compatible **Audit116**, superseded where applicable by **Audit119**, **Audit122**, and later current v85 working closures.  
**Current written whole-project authority:** **v2.20 / Audit135**.  


**Face:** Elements  
**Narrative bearer:** Vaelira  
**Progression:** Recovered → Awakened

## Command package
| Command | Target | Formula | Power | Base Hit | Effect |
|---|---|---|---:|---:|---|
| **Recovered — Fourfold Convergence** | one enemy | Magical sequence Fire / Ice / Lightning / Earth | 4 × 95 | — | Each hit may attempt linked status at 15%; maximum 1 newly inflicted harmful status for whole command. |
| **Awakened — Elemental Crown** | one enemy | Magical / chosen standard element | 300 | 110 | 30% Spirit penetration; 40% linked status. |
| **Awakened — Twin Convergence** | one enemy | Magical / choose 2 different standard elements | 2 × 155 | 110 per hit | 20% linked status per hit; maximum 1 newly inflicted harmful status for whole command. |
| **Awakened — Resonant Shift** | self | Setup | — | — | Choose one standard element and arm Resonant Shift **through the end of the next Prime round, or until dismissal if dismissal occurs first**. The first later damaging Last Convergence command containing that element consumes the setup; matching-element hit(s) gain +35% final damage and the exact elemental-resistance adjustment below. Unavailable Round 3. |
| **Legacy/final — World in Four** | Prime Round 3 only; all enemies | Magical waves Fire / Ice / Lightning / Earth | 4 × 80 = 320 per target | 105 per wave | 15% linked status per wave; maximum 1 newly inflicted harmful status per target. No Composite Reaction. |

## Resonant Shift exact resolver
- A damaging command that does **not** contain the chosen element does not consume Resonant Shift.
- When a later command contains the chosen element, only the hit(s) using that chosen element receive Resonant Shift's +35% final-damage bonus and resistance adjustment; other elemental hits in the same command resolve normally.
- Resonant Shift ignores **25% of the target's direct-damage reduction from elemental resistance relative to Neutral**, without changing the target's actual affinity identity.
- Exact matching-hit direct-damage multipliers while Resonant Shift applies:
  - Weak: **125% → 125%**;
  - Neutral: **100% → 100%**;
  - Resistant: **80% → 85%**;
  - Strongly Resistant: **60% → 70%**;
  - Immune: **0% → 0%**.
- Because the target's actual affinity identity is not rewritten, Resonant Shift does **not** alter linked-status affinity modifiers or bypass status/element immunity.
- The setup is consumed after that qualifying command resolves, even if the matching hit misses or deals 0 damage because of immunity/protection.
- If no qualifying command occurs before the deadline, the setup expires unused.

## Global Prime references
- `../PRIME_SYSTEM_RULES.md`
- `../PRIME_SCALING.md`
- `../PRIME_STATUS_CONTROL.md`

## Ruin formula scope
If this Prime contains Ruin damage, use the command's explicitly authored Prime formula.
Do **not** force the character-Ability 75/25 Ruin rule onto a Prime command.
