# Diyse — Data, Stable IDs & Content Indirection
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
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
- internal `gold` field must not make the player-facing currency `Gold`;
- old Face values Resource/Acuity/Change must not be written back as current Face names.

Detailed known mappings live in:
`IMPLEMENTATION_NOTES/RUNTIME_ID_MIGRATION_MAP.md`

## Preferred migration pattern

For an old persisted/serialized value that still needs compatibility:
> **read old → normalize to current semantics → write current**

Do not:
- reject a valid old save merely because a display term was renamed, when a safe semantic mapping exists;
- keep writing retired values indefinitely just because old data can still be read;
- change a durable ID without checking authored Resources, flags, tests, scene references, and save migration;
- expose a legacy technical ID as current UI text.

The Kessara Relic-copy Face migration is the current concrete example: old Resource/Acuity/Change inputs remain readable, but new/current records canonicalize to Perception/Memory.

## Source/reference asset boundary

Source/reference master art is not automatically a runtime asset path.

For current character visuals:
- exact source masters → `asset_sources/characters/current/`
- identity/production authority → `docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`
- deployable runtime derivatives → appropriate runtime asset/content lane with stable character/expression indirection.

Do not make production gameplay depend directly on source-master file paths merely because those files are present in the repository.

## Schema change
Adding/removing:
- a dialogue branch field;
- a save field with new semantics;
- a permanent command;
- a new inventory category with gameplay meaning

is not a cosmetic UI change.
It is a system/schema change and requires authority plus version-safe migration where persistent data is affected.
