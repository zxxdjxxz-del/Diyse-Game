# Progression Section

Owns progression math and planning only:
- Player Level and natural stats;
- Player EXP curve;
- CEXP and Class Level planning;
- chapter-start/chapter-end and named internal checkpoints;
- source-backed loadout/stat audits;
- explicit selected-class simulation choices after their source-backed unlock;
- explicit assumed-owned Ordinary and source-gated Relic equipment choices for loadout testing;
- source-validated mandatory-route Base/Subclass CEXP states at exact named checkpoints;
- Class-Level-gated reciprocal donor Ordinary/Relic equipment access;
- mandatory/light/typical/heavy/completionist route projections;
- encounter-count and average-EXP solvers;
- level-cap and class-completion checks.

## Source authority versus simulation input

Progression audits must not convert a simulator choice into Diyse canon.

- If no selected class is supplied after Sixfold Volition, DiySim keeps the native Base Class as a source-backed floor and reports `selected_class_route_missing`.
- An explicit selected class is accepted only when it is the character's native Base Class or native Subclass and the Subclass is already unlocked. It resolves the simulation choice; it does not claim that every player route makes that choice.
- If equipment timing/ownership is not published, DiySim keeps the source gap visible rather than guessing a purchase or reward route.
- An explicit equipment choice is an **assumed-owned simulation input**, never a claim that the mandatory route owns it.
- Native Ordinary gear remains supported through the ordinary loadout resolver, with slot/ownership/handedness checks and known ordinary-weapon first-availability timing enforced.
- Ordinary armor and Secondary acquisition chapters remain unpublished; explicit choices may supply those slots for a scenario without asserting a canonical acquisition chapter.
- At a class-aware exact checkpoint, a Relic choice may be supplied as an assumed-owned inventory item only after its authored first-acquisition chapter is reachable. This proves scenario legality, not guaranteed acquisition.
- Shared Relic Shield/Focus access remains blocked because current source authority does not map those shared Secondary items to a native/donor class-access route.

## CEXP checkpoint state

`ClassCexpState(base_cexp=..., subclass_cexp=...)` is an explicit simulation state, not a canonical class-allocation route.

At exact named checkpoints DiySim can validate that state against current mandatory-route authority:
- before Sixfold Volition, Base CEXP is exact and Subclass CEXP must be 0;
- after Volition, Base/Subclass gains cannot exceed the published mandatory post-Volition CEXP stream;
- unaccounted CEXP is legal only when a class has reached CL13, because additional CEXP assigned to a capped selected class is lost rather than spilled;
- DiySim does **not** invent a mandatory "finish Base first" or other hidden switching policy.

This class-state proof currently supports the **mandatory route only**. Optional-content CEXP timing/order must be modeled before `expected`, `best_available`, or completionist class states can be certified.

## Donor equipment access

Current class-system authority is read directly from `CLASS_SYSTEM_MASTER.md`:
- Subclass CL1 — reciprocal donor Primary access;
- Subclass CL3 — reciprocal donor Armor access;
- Subclass CL5 — reciprocal donor Secondary access;
- Subclass CL7 — Equipment Mastery opens donor Base-Class **Relic eligibility**;
- Subclass CL11 — Legacy Mastery opens donor Base-Class **Legacy eligibility**.

`resolve_class_aware_loadout_at_checkpoint(...)` first validates the supplied `ClassCexpState`, then applies the source-backed equipment gates:
- reciprocal donor Ordinary Primary/Armor/Secondary at CL1/3/5 respectively;
- native Relics when the explicit assumed-owned item has reached its authored first-acquisition chapter;
- reciprocal donor Relics only when the item has reached its first-acquisition chapter **and** the receiver has reached Subclass CL7;
- two-slot Great Bow and Two-Handed Sword Relics continue to consume Secondary.

Relic first-acquisition placement proves only that the inventory item could have been obtained by that checkpoint; it does not convert optional content into guaranteed ownership.

## Legacy boundary

DiySim now parses and audits the full **17-piece Legacy package inventory**, all six reciprocal donor relationships, and the authored Legacy project prerequisite contract. That source layer proves what the Legacy items are and who may eventually share them; it still does **not** mark any Legacy as completed or owned.

Legacy equipment remains blocked in class-aware loadouts even at Subclass CL11. CL11 proves donor **eligibility only**. Native project completion separately requires the authored completion chain (Base CL13, Core Masteries, Character Quest/component, precursor, Gate A, Gate B, and Kessara/project availability), while donor use additionally requires the actual unique donor Legacy item to already exist. Legacies are not copied.

Some current Legacy material/precursor documents retain older Face labels. DiySim therefore keys the Legacy source layer by **character, item package, and reciprocal donor relationship**, not by Face-name strings, until the owner terminology is reconciled.

Do not place battle actor definitions or encounter scripts here.
