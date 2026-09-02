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

## Stage 0 — Preserve and classify the existing proof — COMPLETE

The existing queued-round/Prime proof remains available as implementation evidence and its coupled combat tests are explicitly classified as legacy proof regressions rather than production battle authority.

Key proof files still intentionally present include:
- `game/combat/battle_state.gd`
- `game/combat/round_resolver.gd`
- `game/combat/combat_proof.gd`
- `game/content/cards/first_champion_recovered.tres`
- `tests/combat/validate_round_combat.gd`
- `tests/smoke/validate_project.gd`

They are to be replaced together with current-authority coverage when the battle/Prime migration reaches those stages.

## Stage 1 — Data terminology normalization — ACTIVE / ONGOING

Completed normalization includes:
- Kessara Relic-copy state writes **Might / Elements / Grace / Perception / Memory / Ruin**;
- Resource/Acuity/Change are compatibility aliases only and normalize into Perception/Memory;
- line-complete dialogue Resources have a narrow current-term compatibility normalization for the retired Acuity/Change Face list while the generated Resource is awaiting clean regeneration;
- production roster display identities normalize from stable character IDs to current first-name-only names.

Continue this pattern for other persistent/current-facing records:
- read old technical values where compatibility requires it;
- normalize to current semantic values;
- write current values going forward;
- never display a retired value merely because an internal ID remains old.

## Stage 2 — Production wallet / G state — COMPLETE

Implemented:
- persistent `wallet_g` state;
- current starting wallet **2,500 G**;
- affordability, credit and spend operations;
- save schema v2 wallet persistence and v1 → v2 migration;
- legacy `rewards.gold` retained only as isolated proof battle-result payload, never reinterpreted as the wallet;
- Kessara exact service fee **6,000 G per successful Relic copy**;
- invalid/insufficient-G attempts charge 0 G;
- successful fee deduction, matching component consumption and forged-copy state commit through one synchronous GameState transaction.

Remaining old `gold` reward payload migration belongs to later reward/battle integration and does not reopen the wallet foundation.

## Stage 3 — Production party / character state — COMPLETE

Implemented in save schema **v3**:
- stable permanent IDs: `cyanis`, `ilyra`, `torren`, `nimera`, `vaelira`, `seyrik`;
- all six permanent character records independent of the four-character proof `party` fixture;
- current first-name-only display identity normalization;
- recruitment state separate from active-party membership;
- active party maximum **4**;
- validation against duplicate, unknown and unrecruited active-party entries;
- canonical production new-game baseline: Cyanis recruited/active; later permanent characters present as records but unrecruited;
- reserved per-character `persistent_state` envelope without inventing final stats/progression;
- v2 → v3 migration that preserves proof `party` data but does not infer production recruitment from it;
- dedicated roster/active-party and save migration/round-trip regression coverage.

The legacy proof `party` array remains only until the production battle/exploration consumers are migrated.

## Stage 4 — Class / Face / loadout state — ACTIVE

Production state must support current class architecture without reintroducing retired systems:
- one Base Class and one reciprocal Subclass per permanent character;
- no Subclass use before Sixfold Volition;
- no Mastery Point currency;
- automatic Mastery unlock state derived from Class Level/current class authority;
- 3 Standard Card slots per character;
- Prime slots: 1 from Chapter-4 loadout access until Sixfold Volition, 2 afterward.

Technical class IDs may remain stable where appropriate, but current-facing names must follow `00_MASTER_CONTROL/CLASS_TERMINOLOGY_CURRENT.md`.

This stage should extend the stable roster/save layer rather than stuffing new production state into the legacy proof `party` dictionaries.

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
- remove production dependence on `CONFIRM ROUND`;
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
