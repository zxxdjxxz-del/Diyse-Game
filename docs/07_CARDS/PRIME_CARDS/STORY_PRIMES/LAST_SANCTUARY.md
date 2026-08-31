# Diyse — Prime: Last Sanctuary
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary Card/Prime authority:** compatible **Audit116**, superseded where applicable by **Audit119**, **Audit122**, and later current v85 working closures.  
**Current written whole-project authority:** **v2.20 / Audit135**.  


**Face:** Grace  
**Narrative bearer:** Ilyra  
**Progression:** Recovered → Awakened

## Command package
| Command | Target | Formula | Power | Base Hit | Effect |
|---|---|---|---:|---:|---|
| **Recovered — Sanctuary Descends** | all enemies | Magical / Colorless | 215 each | — | On party return: conscious party heals 30% Max HP + 0.85 × Last Sanctuary Magic and clears 1 eligible harmful status; defeated members revive at 30% Max HP with eligible status clear; conscious party gains **Defense +15% / Spirit +15% for 1 full normal round**. |
| **Awakened — Merciful Radiance** | one enemy | Magical / Colorless | 285 | — | 20% Spirit penetration; Last Sanctuary restores 18% of its own Max HP. |
| **Awakened — Hallowed Wave** | all enemies | Magical / Colorless | 205 each | — | Last Sanctuary restores 8% of its own Max HP once and gains **Defense +15% / Spirit +15% through the end of the next Prime round, or until dismissal if dismissal occurs first**. |
| **Awakened — Consecrated Refuge** | self | Recovery / setup | — | — | Restore 25% Last Sanctuary Max HP; gain **Defense +25% / Spirit +25% through the end of the next Prime round, or until dismissal if dismissal occurs first**; prepare **Held Sanctuary** until the current manifestation dismisses. Legal on Round 3 because Held Sanctuary can resolve immediately at normal dismissal. |
| **Legacy/final — Sanctuary Returned** | Prime Round 3 only; all enemies | Magical / Colorless | 245 each | 105 | 20% Spirit penetration; dismiss after damage. Return: conscious party heals 35% Max HP + 0.85 × Sanctuary Magic, clears all eligible harmful statuses; defeated revive at 40%; conscious party gains Regen 5% Max HP × 3 rounds and **Defense +20% / Spirit +20% for 1 full normal round**; restores 0 party MP. Held Sanctuary adds +10% Max-HP return healing and raises revival to 55%. |

## Held Sanctuary exact resolver
Held Sanctuary is a Prime-local prepared return state.

- Only one Held Sanctuary state may be prepared; using Consecrated Refuge again refreshes/re-establishes the same state rather than stacking it.
- Held Sanctuary persists until the current Last Sanctuary manifestation dismisses and is not consumed by intervening Prime commands.
- If **Sanctuary Returned** resolves while Held Sanctuary is prepared, use Sanctuary Returned's normal return package with the established Held enhancements:
  - conscious return heal becomes **45% target Max HP + 0.85 × Last Sanctuary Magic**;
  - defeated party members revive at **55% Max HP**;
  - full eligible harmful-status cleanse, Regen 5% Max HP × 3 rounds, Defense +20% / Spirit +20% for 1 full normal round, and 0 MP restoration remain unchanged.
- If Last Sanctuary reaches normal dismissal with Held Sanctuary prepared **without** using Sanctuary Returned — including Consecrated Refuge selected on Prime Round 3 — resolve the same **Held-enhanced party return package only**, with **no Sanctuary Returned enemy damage or Spirit penetration**.
- If Held Sanctuary was never prepared and Sanctuary Returned was not used, ordinary Last Sanctuary dismissal creates no extra party-heal/revival package beyond another explicitly authored command/effect.
- Held Sanctuary clears after its dismissal handoff resolves.

All Last Sanctuary return healing/revival uses the current eligible active-party/KO-party rules and does not target summons, devices, or the dismissed Prime body.

## Global Prime references
- `../PRIME_SYSTEM_RULES.md`
- `../PRIME_SCALING.md`
- `../PRIME_STATUS_CONTROL.md`

## Ruin formula scope
If this Prime contains Ruin damage, use the command's explicitly authored Prime formula.
Do **not** force the character-Ability 75/25 Ruin rule onto a Prime command.
