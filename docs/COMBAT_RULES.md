# Diyse — Combat Engineering Rules

This is the implementation-facing combat baseline for Step 7B.5. It does not replace the full combat authority.

## Core round structure

Diyse uses traditional discrete rounds.

At the start of a round:

1. Resolve beginning-of-round effects and immediate battle-state checks.
2. Each enemy locks one legal action from the legitimate beginning-of-round state without inspecting unconfirmed player commands.
3. The player selects one action for every conscious active party member before the round is confirmed.
4. Resolve Item actions first, ordered by current effective Speed.
5. Resolve Defend actions second, ordered by current effective Speed.
6. Resolve all remaining party and enemy actions from highest to lowest current effective Speed.
7. Party members win exact Speed ties against enemies.
8. Tied party members use player-selected order.
9. Tied enemies/entities use stable deterministic order.
10. Resolve complete action/reaction/state-change packages, then end-of-round processing according to the controlling combat specification.

Speed determines order only. Speed never grants extra ordinary actions.

## Automatic hostile retargeting

If a queued party hostile action targets an enemy that is defeated before that action resolves in the same round, the action is not wasted.

- Retarget to the next living enemy in encounter-slot order after the original target.
- If no later slot is living, wrap to the first living enemy.
- If no enemies remain living, there is no legal target and the battle should already resolve victory as appropriate.
- This rule applies to Attack, damaging Abilities, and hostile Standard Card effects unless an individual authored effect explicitly establishes different legal targeting behavior.
- Retargeting changes only the target; it does not change the action, cost, priority tier, Speed, or actor.
- The presentation/combat log should expose the retarget so the player can understand what happened.

Example: Cyanis and Ilyra both target Enemy A. Cyanis defeats Enemy A before Ilyra acts. If Enemy B is living, Ilyra's already-queued hostile action automatically resolves against Enemy B.

## Permanent command list

Exactly:

- Attack
- Ability
- Card
- Item
- Defend

Do not add universal Swap, Reserve, Assist, Row, Move, Wait, Timeline, or personal-resource commands.

## Active party

Maximum four permanent characters can be active in battle.

Reserve members do not participate mid-battle and cannot be swapped in through a universal command.

## Ability economy

- MP is the universal ordinary Ability resource.
- Do not create character-specific combat gauges/resources.
- The proof may use temporary Ability records, but the engine must not hard-code them into character scripts.

## Card guardrails

Current collection architecture is 24 Standard Cards + 12 Prime Cards.

For the 7B.5 Standard Card proof:

- implement one placeholder Standard Card only;
- Standard Cards are not built around per-battle charges, Essence, ranks, refresh counters, or use counters;
- the implementation must be capable of data-driven Card definitions.

For the 7B.5 Prime proof:

- implement one placeholder manifestation sufficient to prove the control/state architecture;
- Prime manifestation actions are directly selected by the player where required by current Prime rules;
- do not fabricate final Prime abilities or visuals.

## Summon/system caution

Do not infer ordinary-summon rules from the Prime proof. Prime manifestations and ordinary summons are not automatically the same subsystem.

## Determinism and testing

Pure round resolution should be testable without relying on animation timing.

At minimum, tests should cover:

- Item priority over faster ordinary actions;
- Defend priority after Items;
- Speed ordering within a priority tier;
- exact party-versus-enemy Speed tie;
- tied party player-selected order;
- stable tied-enemy order;
- enemy action locking before player confirmation;
- one ordinary selected action maximum per legal unit per round unless a separately legal effect explicitly changes that outcome;
- queued hostile party actions automatically retargeting from a defeated enemy to the next living enemy, including wraparound.

Presentation and animation should consume resolver results rather than define combat legality.
