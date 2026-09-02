# Progression Section

Owns progression math and planning only:
- Player Level and natural stats;
- Player EXP curve;
- CEXP and Class Level planning;
- chapter-start/chapter-end and named internal checkpoints;
- source-backed loadout/stat audits;
- explicit selected-class simulation choices after their source-backed unlock;
- explicit assumed-owned Ordinary and source-gated Relic equipment choices for loadout testing;
- explicit source-bounded Legacy project/completion proofs for endgame loadout testing;
- source-validated mandatory-route Base/Subclass CEXP states at exact named checkpoints;
- Class-Level-gated reciprocal donor Ordinary/Relic/Legacy equipment access;
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
- Legacy availability is never treated as ownership. A Legacy loadout choice requires explicit project evidence and the exact item to be listed as completed.

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
- native Legacies only when an explicit project proof validates the actual completed item;
- reciprocal donor Legacies only when the donor's actual completed item is proven and the receiver has reached Subclass CL11;
- authored two-slot Relic and Legacy weapons continue to consume Secondary.

Relic first-acquisition placement proves only that the inventory item could have been obtained by that checkpoint; it does not convert optional content into guaranteed ownership.

## Legacy project proof

DiySim parses and audits the full **17-piece Legacy package inventory**, all six reciprocal donor relationships, the native project contract, Character Quest/component handoffs, per-character precursor timing, and the complete 12-row Legacy Gate source matrix.

`LegacyProjectProof` combines the project owner's exact `ClassCexpState` with explicit `LegacyProjectEvidence`. Native completion requires:
- native Base CL13; this also proves all four native Core Masteries because current class authority unlocks them by Base CL12;
- explicit Character Quest completion; the quest handoff then source-proves that character's unique Legacy Component grant;
- explicit precursor ownership;
- explicit Gate A ownership;
- explicit Kessara project availability for the scenario;
- Gate B ownership for non-weapon package pieces;
- the exact Legacy item in `completed_items`, proving the forge/project was actually completed.

Gate A can release the package weapon. Gate B releases the remaining package pieces. Availability, material access, Class Level, or donor eligibility by themselves never create an inventory item.

The repo still does not publish the exact chapter in which Kessara's Legacy-project service first opens. DiySim therefore uses a conservative source-backed completion window:
- `end_ch12`;
- `ch13_start`;
- `ch13_last_shelter`.

Earlier completion is not inferred. New completion after Last Shelter is rejected because the authored handoff closes Legacy completion at **Last Shelter → Reactor Galleries**.

Donor Legacy use remains stricter than eligibility: Subclass CL11 is required, but the reciprocal donor owner's native project proof must also validate that the **actual unique item already exists**. Legacies are moved, not copied.

Some current Legacy material/precursor documents retain older Face labels. DiySim deliberately avoids a character→material join through those names. Character prerequisites are keyed by character/item package, and the Gate matrix is used only for the conservative point at which all 12 authored Legacy Gate rows are already available.

The programmatic progression API supports these Legacy proofs now. The CLI does **not yet** expose Legacy project-proof flags; its existing equipment-choice help also still needs the corresponding wording update.

Do not place battle actor definitions or encounter scripts here.
