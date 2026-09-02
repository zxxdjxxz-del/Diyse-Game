# Progression Section

Owns progression math and planning only:
- Player Level and natural stats;
- Player EXP curve;
- CEXP and Class Level planning;
- chapter-start/chapter-end and named internal checkpoints;
- source-backed loadout/stat audits;
- explicit selected-class simulation choices after their source-backed unlock;
- explicit assumed-owned Ordinary equipment choices for loadout testing;
- source-validated mandatory-route Base/Subclass CEXP states at exact named checkpoints;
- Class-Level-gated reciprocal donor Ordinary equipment access;
- mandatory/light/typical/heavy/completionist route projections;
- encounter-count and average-EXP solvers;
- level-cap and class-completion checks.

## Source authority versus simulation input

Progression audits must not convert a simulator choice into Diyse canon.

- If no selected class is supplied after Sixfold Volition, DiySim keeps the native Base Class as a source-backed floor and reports `selected_class_route_missing`.
- An explicit selected class is accepted only when it is the character's native Base Class or native Subclass and the Subclass is already unlocked. It resolves the simulation choice; it does not claim that every player route makes that choice.
- If equipment timing/ownership is not published, DiySim keeps the source gap visible rather than guessing a purchase or reward route.
- An explicit equipment choice is an **assumed-owned simulation input**. Native Ordinary gear remains supported through the ordinary loadout resolver, with slot/ownership/handedness checks and known ordinary-weapon first-availability timing enforced.
- Ordinary armor and Secondary acquisition chapters remain unpublished; explicit choices may supply those slots for a scenario without asserting a canonical acquisition chapter.

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

`resolve_class_aware_loadout_at_checkpoint(...)` first validates the supplied `ClassCexpState`, then permits source-proven reciprocal donor **Ordinary** gear at the CL1/3/5 gates. Donor ordinary weapons still obey their published first-availability chapters, Secondary families must be source-proven, and two-slot weapons still consume Secondary.

Relics and Legacies remain blocked in this path even at CL7/CL11. Class Level proves only eligibility; DiySim must separately prove actual Relic ownership or donor Legacy completion/ownership before those items can be simulated as available.

Do not place battle actor definitions or encounter scripts here.
