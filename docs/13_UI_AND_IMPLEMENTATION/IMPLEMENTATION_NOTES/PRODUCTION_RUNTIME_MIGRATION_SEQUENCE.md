# Diyse — Production Runtime Migration Sequence

**Status:** ACTIVE ENGINEERING MIGRATION PLAN  
**Purpose:** move the current Godot proof runtime toward current Diyse authority without allowing proof behavior, stale terminology, or cosmetic ID renames to become accidental canon.

This is an implementation sequence, not a new game-design authority. Exact system behavior remains owned by the relevant numbered domains.

## Controlling authorities

Before changing the affected runtime, read:
- `../../00_MASTER_CONTROL/CURRENT_CANON_STATUS.md`
- `../../00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md`
- `../../05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`
- `../../05_BATTLE_SYSTEM/PRIME_ROUND_SEQUENCING.md`
- `../../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`
- `../../07_CARDS/PRIME_CARDS/PRIME_LOADOUT_AND_ACCESS.md`
- `../DATA_AND_STABLE_ID_RULES.md`
- `RUNTIME_ID_MIGRATION_MAP.md`

## Migration principle

Do not try to make the proof runtime "look current" by renaming a few labels while keeping incompatible state/behavior underneath.

Use this pattern:
> **preserve compatible data → add migration/normalization → implement current state model → replace stale behavior → replace stale tests → retire obsolete proof paths only after coverage exists**

## Stage 0 — Preserve and classify the existing proof

Before the structural combat/Prime migration:
- keep the existing proof files available as implementation evidence;
- classify `tests/combat/validate_round_combat.gd` as a **legacy proof regression**, not current combat authority;
- classify the bearer-lock/Confirm-Round assertions in `tests/smoke/validate_project.gd` the same way;
- do not weaken or silently reinterpret those assertions while they still exercise the old proof architecture;
- replace them with current-authority tests in the same migration that replaces the corresponding runtime behavior.

The key proof files currently coupled to retired behavior include:
- `game/combat/battle_state.gd`
- `game/combat/round_resolver.gd`
- `game/combat/combat_proof.gd`
- `game/content/cards/first_champion_recovered.tres`
- `tests/combat/validate_round_combat.gd`
- `tests/smoke/validate_project.gd`

## Stage 1 — Data terminology normalization — STARTED

Current completed piece:
- the Kessara Relic-copy state path writes the current Face set **Might / Elements / Grace / Perception / Memory / Ruin**;
- Resource/Acuity/Change remain accepted only as compatibility aliases and normalize into Perception/Memory.

Continue this pattern for other persistent/current-facing records:
- read old technical values where save/content compatibility requires it;
- normalize to current semantic values;
- write current values going forward;
- never display a retired value merely because an internal ID remains old.

## Stage 2 — Production wallet / G state

The proof currently uses `gold` as a technical reward/state key. Current player-facing currency is **G**.

Production migration must establish a durable wallet/currency state with current G semantics before currency-dependent services are considered complete.

Requirements:
- preserve a version-safe path for any legacy persisted currency value that is actually intended to survive migration;
- do not infer a numeric conversion for old proof values unless the owning economy/save authority explicitly requires one;
- current UI displays **G**, never Gold/Auren as the ordinary currency name;
- Kessara's closed fee is **6,000 G per successful Relic copy**;
- fee deduction and Relic-copy commit must ultimately be atomic so currency/component/item state cannot partially apply.

Do not bolt a 6,000 subtraction onto the proof `rewards.gold` field and call the production wallet complete.

## Stage 3 — Production party / character state

Replace four-character proof fixtures with a production-capable roster model that distinguishes:
- the six permanent recruited characters;
- the active battle party, maximum **4**;
- per-character persistent progression/loadout state;
- current first-name-only character identity/display names;
- current class/Face terminology.

This stage does not require every final stat value to be authored in code at once. It requires the state shape to stop assuming the proof four are the whole permanent roster.

## Stage 4 — Class / Face / loadout state

Production state must support current class architecture without reintroducing retired systems:
- one Base Class and one reciprocal Subclass per permanent character;
- no Subclass use before Sixfold Volition;
- no Mastery Point currency;
- automatic Mastery unlock state derived from Class Level/current class authority;
- 3 Standard Card slots per character;
- Prime slots: 1 from Chapter-4 loadout access until Sixfold Volition, 2 afterward.

Technical class IDs may remain stable where appropriate, but current-facing names must follow `00_MASTER_CONTROL/CLASS_TERMINOLOGY_CURRENT.md`.

## Stage 5 — Prime collection / persistence model

Replace the proof `first_champion` one-use/bearer-owned structure with production-capable Prime state.

Required semantic state includes:
- Prime identity;
- acquired/not acquired;
- Story Prime progression: Recovered or Awakened;
- Ready/spent availability that persists across battle end;
- legal restoration handling;
- per-character Prime-slot assignments;
- narrative bearer association separate from combat ownership/access.

Current rules that must be represented:
- any acquired Prime may occupy a legal Prime slot;
- Story bearer association is narrative/thematic, not owner-lock;
- each Prime identity has one use until restored;
- battle end and fresh boss forms do not restore spent identities;
- valid explicit restoration such as Emergency Kit can restore acquired identities to Ready;
- restoration does not bypass the separate post-dismissal spacing gate.

The old technical ID `first_champion` should be migrated deliberately rather than merely relabeled in place. Current Story Prime identity is **Last Sentinel**.

## Stage 6 — Normal battle core: turn-entry command selection

This is a structural replacement, not a patch to `confirm_round()`.

Production battle core must:
1. resolve beginning-of-round checks;
2. construct and lock the round's Speed/tie/reroute order;
3. advance one eligible actor slot at a time;
4. when a player character's slot arrives, request that character's command/content/target from the **current** battle state;
5. when an enemy slot arrives, choose AI action from the **current legitimate** state;
6. resolve that action immediately and completely;
7. advance to the next slot;
8. perform end-of-round processing after all eligible slots complete or are lost.

Remove as production concepts:
- whole-party action prequeue;
- enemy action locking before future player choices;
- universal Confirm Round;
- Item/Defend priority phases.

Preserve the current exact Speed/tie and authored initiative-reroute rules from the battle-system owner.

## Stage 7 — Recovered Prime sequencing

Recovered Story Prime Invocation:
- is selected on the invoking character's normal turn;
- costs 0 MP;
- spends that Prime identity when Invocation legally resolves;
- performs exactly one strong Recovered signature action in the current normal round;
- dismisses in that same normal round;
- does not create a persistent two- or three-round replacement body;
- normal remaining eligible round slots continue under the already-locked order.

Retire the current proof's two-round Recovered direct-control model.

## Stage 8 — Awakened Prime sequencing

Awakened Invocation:
- consumes the invoking character's current normal-turn action;
- suspends the ordinary active party immediately when Invocation resolves;
- skips remaining ordinary party slots in that invocation round while allowing remaining enemy/support slots to resolve once;
- after the invocation round ends, runs exactly **3 Prime rounds**;
- builds a fresh Speed-based Prime/enemy/support initiative order for each Prime round;
- gives the Prime exactly one selected Prime command per Prime round;
- uses turn-entry enemy AI and immediate action resolution;
- returns the party at the next fresh normal round after normal dismissal or early Prime defeat;
- starts the **2 full normal party rounds** spacing gate on return.

Do not restore boss-form Prime refresh.

## Stage 9 — Production combat UI migration

Once the core battle state no longer queues a whole party:
- remove the production dependence on `CONFIRM ROUND`;
- show the current actor clearly;
- present the five permanent commands only on an eligible player-controlled turn;
- present current legal Card/Prime content and targets based on current state;
- keep proof/debug views separate from final combat UX.

`BATTLE_FLOW_UI.md` owns the production logical UI states.

## Stage 10 — Test replacement and migration gates

The battle/Prime migration is not complete until tests assert the **current** rules rather than merely deleting old assertions.

Required replacement coverage should include at minimum:
- Speed-derived round order and tie behavior;
- player action chosen at turn entry, not round start;
- enemy AI decision at its turn, with no knowledge of future player choices;
- immediate action resolution before the next actor decision;
- Item/Defend as ordinary Speed-slot commands;
- no universal Confirm Round requirement;
- hostile retargeting/current target legality;
- Standard Card MP/use behavior under current authority;
- Story Prime not bearer-locked after acquisition;
- Recovered one-signature-action same-round flow;
- Awakened 3-Prime-round flow;
- party suspension/targeting;
- persistent Prime spent state across battles;
- valid restoration;
- two-full-normal-round spacing gate;
- no fresh-boss-form restoration;
- save/load of new production state;
- compatibility migration for retained legacy technical IDs/Face labels.

Keep tests deterministic. Do not make animation timing the source of combat legality.

## Stage 11 — Character runtime asset derivatives

The current repository character masters are source/reference authority, not direct runtime deployment files.

When production character portraits/models are created:
- derive them from `asset_sources/characters/current/` and the matching visual locks;
- place deployable derivatives in an appropriate runtime asset lane;
- update registries/Resources through stable character/expression IDs rather than hardwiring source-master paths;
- remove proof placeholder dependencies only after equivalent runtime derivatives exist and validation points to them.

## Completion gate

The migration stream is complete only when:
- current domain rules and runtime behavior agree;
- current-facing terminology is consistent;
- durable state has explicit migration handling;
- stale proof assumptions are no longer required by production code;
- replacement tests cover the current behavior;
- proof fixtures that remain are unmistakably labeled as proof/history rather than current requirements.
