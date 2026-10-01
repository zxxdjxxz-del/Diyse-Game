# Diyse — Data, Stable IDs & Content Indirection
**Historical migration provenance:** v85-era consolidated tracker.
**Authority treatment:** this repository file is current UI/implementation-domain authority within its stated scope; Audit/v85 references remain provenance only.
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Core rule
Generic runtime/UI code must not own final authored content text or asset paths.

Use data/resources and stable semantic IDs.

## Proven dialogue pattern
- scene ID
- beat ID
- character ID
- expression ID
- portrait registry
- trigger/completion IDs
- cue metadata

This pattern should inform other content-heavy systems where appropriate.

## Save-safe identifiers
Persistent references should prefer stable IDs for:
- items;
- equipment;
- Relics;
- Legacies;
- Cards;
- Primes;
- quests;
- Hunts;
- locations;
- classes;
- world flags.

Do not key durable save data only by display name.

## Technical legacy IDs
Historical technical IDs may remain internally until a reference-safe migration.

But:
> current-facing UI must show current names.

Examples:
- old `first_champion` technical proof ID must not display as the current Prime name;
- old geography technical IDs must not restore retired map labels;
- internal `gold` field must not make the player-facing currency `Gold`.

## Schema change
Adding/removing:
- a dialogue branch field;
- a save field with new semantics;
- a permanent command;
- a new inventory category with gameplay meaning

is not a cosmetic UI change.
It is a system/schema change and requires authority.
