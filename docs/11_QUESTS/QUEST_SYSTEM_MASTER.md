# Diyse — Quest System Master
**Historical migration provenance:** v85-era consolidated tracker.
**Authority treatment:** this repository file is current quest-domain authority. Audit/v85 references remain provenance only; exact EXP/CEXP values are owned by `10_PROGRESSION_AND_EXP` and remain provisional pending the planned progression rebuild.
**Historical quest-architecture provenance:** Audit103 plus later accepted quest reductions/corrections.
**Domain rule:** this folder owns optional-activity identity, unlocks, objectives, route/area flow, quest-state outcomes, combat/no-combat classification, completion conditions, and world-state payoff. Exact enemy kits/stats live in `09_ENEMIES_AND_ENCOUNTERS`; exact EXP/CEXP in `10_PROGRESSION_AND_EXP`; item/equipment mechanics in `08_ITEMS_AND_EQUIPMENT`; exact dialogue in `03_DIALOGUE`.


## No branching quest morality system
Current quest architecture has:
- no player dialogue-choice tree;
- no romance route;
- no affinity route;
- no alternate moral ending;
- no mutually exclusive quest resolution tree.

Characters make their authored decisions.

## Availability
Once a current Character Quest or ordinary Side Quest unlocks, it normally remains available while world return remains supported.

Current hard cutoff:
> **Last Shelter → Reactor Galleries**

A quest may still have a narrower prerequisite or location-access requirement.

## Failure
Optional civic/personal quests should not normally use:
- hidden real-time timers;
- irreversible civilian deaths because the player delayed optional content;
- punitive moral scoring;
- surprise expiration before the stated final cutoff.

Completed objective steps may persist when the player leaves and returns where appropriate.

## Production economy
Prefer:
- existing maps;
- existing environment kits;
- prop swaps;
- NPC-state swaps;
- route signs/boards;
- lighting states;
- carts/supply states;
- repaired infrastructure;
- limited authored interactions.

Do not turn every quest into:
- a new dungeon;
- a new boss;
- a unique enemy family;
- a sprawling minigame.

## Local expertise
Party members may help, but local workers/professionals do not become incompetent so a playable character can demonstrate expertise.

## Dialogue
Quest gameplay/content structure may contain functional beat notes.
Final line-by-line quest dialogue remains separate under `03_DIALOGUE`.
