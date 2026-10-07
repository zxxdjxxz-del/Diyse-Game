# Implementation Notes — Current Code/Canon Divergences

**Status:** ACTIVE VERIFIED RUNTIME / CANON DIVERGENCE REGISTER  
**Use:** engineering reconciliation only; current owner domains remain authoritative.

These are known engineering gaps where the current proof/runtime can misrepresent or fail to implement current production authority.

Routing rule:
- resolved implementation migrations belong in `../CURRENT_RUNTIME_IMPLEMENTATION_STATUS.md`;
- open production UX without a current code/canon contradiction belongs in `../OPEN_UI_IMPLEMENTATION_ITEMS.md`;
- rebuild-pending balance/economy work belongs in its owning numbered domain and `16_BALANCE_AND_TESTING`.

## 1. Prime proof model — HIGH

The proof runtime does not implement the current Prime manifestation system.

Current production authority requires:

- any acquired Prime may occupy any legal character Prime slot;
- 1 Prime slot/character from Chapter-4 Prime-loadout access until Sixfold Volition; 2 Prime slots/character after Volition;
- Recovered Story Prime = one signature action, then immediate demanifestation;
- Awakened Prime = active allied battlefield replacement using a **3-segment Manifestation Meter**;
- Awakened kit structure = **2 Basic / 2 Medium / 1 Heavy / 1 automatic Dismissal**;
- meter is spent only when a selected Prime command successfully reaches EXECUTION;
- a meter-emptying action enters **Final Return** and Dismissal occurs on the Prime's already-scheduled next TURN;
- active party TURN/EXECUTION/status-duration progression is suspended during Awakened manifestation while enemy timeline progression continues;
- Prime Invocation costs **0 MP** and consumes the invoker's current command opportunity;
- Prime identities use persistent Ready/Spent state until valid restoration;
- post-Prime lockout is owned by the invoker and ends after that character processes **3 personal TURNs**.

The proof runtime must be rebuilt against `../../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md` rather than patched around its current Prime control path.

## 2. Normal battle turn flow — HIGH

Proof runtime still implements a whole-round queue/confirm model that does not match current production battle flow.

Current production uses the ordered **TURN / EXECUTION** timeline owned by `../../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`:

- a combatant receives a TURN and selects one command;
- Immediate actions resolve at once; queued actions create a future EXECUTION marker;
- the combatant's next TURN is scheduled when the command is selected using Return timing;
- other TURNs and EXECUTIONs may occur before a queued action resolves;
- Speed controls personal TURN spacing rather than a round-start initiative sort;
- there is no whole-party action queue;
- there is no universal Confirm Round step;
- Item and Defend do not have separate universal priority phases.

Current CI smoke-checks only the combat proof's loadability and limited surface contracts. It does **not** certify production TURN / EXECUTION behavior, Prime manifestation, final Card costs, or final combat UI. Those runtime mechanics remain implementation debt until an intentional combat migration pass.

## 3. Proof equipment/content — HIGH
GameState defaults still include:
- generic Proof Sword / Proof Wardrod weapon placeholders;
- proof armor;
- Potion;
- four-character proof party only.

They are fixtures, not current equipment/content authority.

The prior Ilyra **Proof Warden Blade** contradiction has been removed; her proof placeholder now stays inside the current **Wardrod** weapon family.

## 4. Save schema completeness — HIGH
Schema v1 proves persistence but does not yet carry the complete production progression/quest/loadout state.

Do not treat schema v1 proof completeness as production completeness.

## 5. Dialogue proof panel — LOW/MEDIUM
Current field proof dialogue panel occupies much more vertical space than the general lower-20–25% production target.

Function is proven; final layout remains open.

## 6. Combat proof UI — HIGH

Current proof UI remains an engineering surface rather than the production combat HUD.

It does not yet represent:

- the ordered TURN / EXECUTION timeline and projected EXECUTION/next-TURN preview;
- current Delay / Interrupt marker inspection;
- the current 4-active / 2-reserve Swap flow;
- the Awakened Prime 3-segment Manifestation Meter;
- Basic / Medium / Heavy meter costs;
- Final Return and automatic Dismissal;
- current Prime Ready/Spent and invoker-owned 3-TURN lockout presentation.

Production combat/Prime UI authority lives in `../COMBAT_UI.md`, `../PRIME_UI.md`, and the owning battle/Prime-system files.

## 7. Current-facing naming — ONGOING
Compatibility or proof technical identifiers may remain internally only while a current runtime dependency requires them; player-facing text must use current names.

## 8. Encounter runtime catalog / balance calibration — HIGH
`game/content/encounters/chapter_01_04_formations.gd` and `game/exploration/encounter_balance.gd` are executable engineering data, but they are not uniformly current encounter/progression authority.

Known gaps:
- Chapter 3 executable rows do not yet match the current Chapter-3 enemy/formation owners;
- Chapter 4 rows preserve inherited Reaction Annex formations while the ordinary-enemy / formation layer is explicitly rework-pending;
- proof enemy stats and encounter tuning remain engineering fixtures rather than production balance authority;
- `encounter_balance.gd` still carries provisional chapter encounter counts, tier weights, EXP anchors and ordinary-EXP pools; these values must not override current encounter or EXP/CEXP owners. Its Chapter-4 encounter-count value is not current production authority and must be replaced during the dedicated runtime migration;
- the generic random-encounter path is not whole-campaign complete: the executable formation catalog currently supplies areas only through Chapter 4, `encounter_balance.gd` has profiles only through Chapter 12, and `area_encounter_tuning.gd` rejects enabled random-encounter contexts above Chapter 12. Current Chapter-13 repeatable formation authority therefore cannot yet execute through this selector stack without a dedicated implementation migration.

Current production authority:
- `09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/`;
- `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/`;
- current enemy/action/raw-stat owners;
- `10_PROGRESSION_AND_EXP/` for final EXP/CEXP.

Do not use executable stale rows to overwrite current encounter canon. Reconcile the runtime catalog in a dedicated implementation pass, without inventing open Chapter-3/4 formation decisions during cleanup.

`tests/encounters/validate_encounter_runtime_contract.gd` deliberately checks only content-neutral runtime structure: profile schema, weighted-pool integrity, pressure state behavior, and selector legality. `tests/combat/validate_generated_encounter_battle_state.gd` still proves that the mixed-authority engineering catalog can execute through the generated-battle path. Neither suite certifies current Chapter-1/3/4 encounter composition, final EXP/CEXP, or current player-facing economy behavior.
