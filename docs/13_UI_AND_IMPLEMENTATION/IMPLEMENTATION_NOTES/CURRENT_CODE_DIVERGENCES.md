# Implementation Notes — Current Code/Canon Divergences

**Status:** ACTIVE VERIFIED RUNTIME / CANON DIVERGENCE REGISTER  
**Use:** engineering reconciliation only; current owner domains remain authoritative.

These are known engineering gaps in the current proof runtime.

## 1. Mastery Points — HIGH
Repository proof/older docs may still contain an 8-point Mastery schedule.

Current authority:
> Mastery Points removed.

Required production implementation:
- delete/avoid point persistence;
- delete/avoid point counters;
- derive automatic unlocks from Base/Subclass CL.

## 2. Prime proof model — HIGH
Proof runtime still uses:
- `first_champion`;
- bearer lock;
- old proof direct-control assumptions;
- stale Prime timing/state behavior.

Current production:
- Last Sentinel current name;
- any acquired Prime can occupy any legal character Prime slot;
- 1 Prime slot/character from Chapter-4 Prime-loadout access until Sixfold Volition; 2 Prime slots/character after Volition;
- Recovered = one signature action/same round;
- Awakened = 3 Prime rounds;
- Prime Invocation costs **0 MP**;
- each Prime identity has **one use until restored by valid rest or an explicitly authored restoration effect**;
- Prime spent/Ready state **persists across battle end** until valid restoration;
- after any Prime manifestation ends, **3 full normal party rounds** must pass before another Ready Prime may be invoked;
- genuine fresh-HP enemy bodies/forms do **not** refresh spent Prime identities;
- same-bar phase/state changes do **not** refresh spent Prime identities;
- form/body transitions do **not** create a new automatic Prime-use allowance and do not erase or shorten an active 3-full-normal-round post-dismissal spacing gate;
- valid rest and explicitly authored restoration effects such as Emergency Kit can restore eligible spent Prime identities without bypassing the spacing gate.

## 3. Normal battle turn flow — HIGH
Proof runtime still implements the retired whole-round queue model.

Current proof code currently:
- locks enemy actions at round start;
- asks the player to select actions for all conscious party members;
- requires **Confirm Round** before resolution;
- sorts **Item** before **Defend** before ordinary commands through `round_resolver.gd`;
- resolves the queued combined action list afterward.

Current production battle flow:
- remains **discrete round-based**, not ATB;
- establishes normal turn order at round start from current effective Speed and tie rules;
- when a player character's turn arrives, the player selects that character's action and target/content from the current battle state;
- that action resolves before the next normal combatant acts;
- enemy/entity AI likewise chooses its legal action when its turn arrives from the then-current legitimate state;
- **Item** and **Defend** have no separate universal priority phases;
- there is no whole-party action queue and no universal **Confirm Round** step;
- Speed changes during the round affect later round ordering unless an explicit authored effect overrides the normal rule.

Do not use the current proof queue/confirm architecture as production battle-flow authority.

The CI suite `tests/combat/validate_round_combat.gd` still regression-locks this proof architecture and the retired `first_champion` Prime fixture. It is an engineering continuity test, not production-mechanics certification, and must migrate with the combat runtime.

## 4. Currency — HIGH
Proof state:
- technical identifier `gold` and old proof values may remain.

Current player-facing currency terminology:
- **G**

Retired player-facing currency name:
- **Auren**

Detailed prices, payouts, balances, and liquidity values are rebuild-pending and must not be hard-coded from old proof fixtures during cleanup. Requires version-safe production state/schema/UI work. Internal migration may preserve a legacy technical identifier temporarily, but final player-facing presentation must use **G** and must not revive Auren.

## 5. Proof equipment/content — HIGH
GameState defaults still include:
- Proof Sword;
- Proof Warden Blade;
- proof armor;
- Potion;
- four-character proof party only.

They are fixtures, not current equipment/content authority.

Ilyra's current primary weapon family is:
> **Wardrods**

## 6. Save schema completeness — HIGH
Schema v1 proves persistence but does not yet carry the complete production progression/quest/loadout state.

Do not treat schema v1 proof completeness as production completeness.

## 7. Dialogue proof panel — LOW/MEDIUM
Current field proof dialogue panel occupies much more vertical space than the general lower-20–25% production target.

Function is proven; final layout remains open.

## 8. Combat proof UI — HIGH
Current proof:
- large text tables/log;
- proof command/target buttons;
- proof **Confirm Round** button;
- proof Flee button;
- proof numeric summaries;
- stale Prime terminology.

It is not the final battle HUD and does not represent the current turn-entry command flow.

## 9. Kessara service UI — MEDIUM
Service logic exists.
No production service menu/fee/timing presentation yet.

## 10. Current-facing naming — ONGOING
Legacy technical identifiers may remain internally until safe migration, but player-facing text must use current names.

## 11. Encounter runtime catalog — HIGH
`game/content/encounters/chapter_01_04_formations.gd` is executable engineering data, but it is not uniformly current encounter authority.

Known gaps:
- Chapter 3 rows still contain superseded pre-September-27 enemy identities/formations;
- Chapter 4 rows preserve inherited Reaction Annex formations while the ordinary-enemy / formation layer is explicitly rework-pending;
- proof enemy stats and encounter tuning remain engineering fixtures rather than production balance authority.

Current production authority:
- `09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/`;
- `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/`;
- current enemy/action/raw-stat owners;
- `10_PROGRESSION_AND_EXP/` for final EXP/CEXP.

Do not use executable stale rows to overwrite current encounter canon. Reconcile the runtime catalog in a dedicated implementation pass, without inventing open Chapter-3/4 formation decisions during cleanup.

`tests/encounters/validate_encounter_runtime_contract.gd` deliberately checks only content-neutral runtime structure: profile schema, weighted-pool integrity, pressure state behavior, and selector legality. `tests/combat/validate_generated_encounter_battle_state.gd` still proves that the mixed-authority engineering catalog can execute through the generated-battle path. Neither suite certifies current Chapter-1/3/4 encounter composition, final EXP/CEXP, or current player-facing economy behavior.
