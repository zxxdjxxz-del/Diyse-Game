# Progression Section

Owns progression math and planning only:
- Player Level and natural stats;
- Player EXP curve;
- CEXP and Class Level planning;
- chapter-start/chapter-end and named internal checkpoints;
- source-backed loadout/stat audits;
- explicit selected-class simulation choices after their source-backed unlock;
- explicit assumed-owned native Ordinary equipment choices for loadout testing;
- mandatory/light/typical/heavy/completionist route projections;
- encounter-count and average-EXP solvers;
- level-cap and class-completion checks.

## Source authority versus simulation input

Progression audits must not convert a simulator choice into Diyse canon.

- If no selected class is supplied after Sixfold Volition, DiySim keeps the native Base Class as a source-backed floor and reports `selected_class_route_missing`.
- An explicit selected class is accepted only when it is the character's native Base Class or native Subclass and the Subclass is already unlocked. It resolves the simulation choice; it does not claim that every player route makes that choice.
- If equipment timing/ownership is not published, DiySim keeps the source gap visible rather than guessing a purchase or reward route.
- An explicit equipment choice is an **assumed-owned simulation input**. It currently supports native **Ordinary** gear only, validates slot/ownership/handedness, and still enforces known ordinary-weapon first-availability timing.
- Ordinary armor and Secondary acquisition chapters remain unpublished; explicit choices may supply those slots for a scenario without asserting a canonical acquisition chapter.
- Donor equipment, Relics, and Legacies are not accepted by this explicit-equipment path until Class-Level/access and obtained-item state can be validated.

Do not place battle actor definitions or encounter scripts here.
