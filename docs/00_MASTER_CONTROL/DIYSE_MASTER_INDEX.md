# DIYSE MASTER INDEX

## Authority
Newest explicit approved correction → current owning domain → `00_MASTER_CONTROL` cross-domain rule → `90_WORKING` only for unresolved work → `99_ARCHIVE` for provenance only.

Cross-domain terminology handoffs:
- current class names → `CLASS_TERMINOLOGY_CURRENT.md`
- current Face names → `FACE_TERMINOLOGY_CURRENT.md`
- retired-name migration map → `RETIRED_TERMINOLOGY_MAP.md`

## Active domains
### 01_CHARACTERS
Playable/supporting/antagonist identities, relationships and chronology.

### 02_STORY
Chapter 0–13 mandatory spine, arcs, reveal order, recruitment, PONR and ending.

### 03_DIALOGUE
Exact Ch0–4 dialogue and later authoring-status gates.

### 04_WORLD_AND_LORE
Current geography, map, factions, modern/ancient history and lore truth.

### 05_BATTLE_SYSTEM
Global combat formulas, targeting, statuses, elements and boss-form rules.

### 06_CLASSES_AND_ABILITIES
12 classes, Ability/Ultimate roster, Traits, MP and automatic Masteries.

### 07_CARDS
24 Standard Cards, 12 Primes and the six current Faces.

### 08_ITEMS_AND_EQUIPMENT
Consumables, 91 equipment identities, Relics, Legacies and materials.

### 09_ENEMIES_AND_ENCOUNTERS
Chapter rosters, raw stats, bosses, Elites and Hunts.

### 10_PROGRESSION_AND_EXP
Level/EXP spine, CEXP model, encounter pacing and optional progression.

### 11_QUESTS
6 Character Quests, 5 Side Quests and Hunt access/presentation.

### 12_ECONOMY_AND_REWARDS
**G**, prices, shops, ordinary-equipment backfill and reward boundaries.

### 13_UI_AND_IMPLEMENTATION
Production UI/runtime requirements and current Godot proof divergence.

### 14_ART_AND_VISUALS
Exact visual authorities, HD-2D grammar, environment/VFX production rules, and authoritative asset inventory/provenance routing.

Current exact character-image masters are stored under:
`asset_sources/characters/current/`

Current character visual authority index:
`docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`

### 15_AUDIO_AND_MUSIC
OPEN soundtrack authority, sound-design requirements and research archive.

### 16_BALANCE_AND_TESTING
Balance closure/open status, regression plans and release gates.

## Working layer
`90_WORKING/` contains only current unresolved/reopened work. It must not become a second cumulative canon tracker.

## Archive layer
`99_ARCHIVE/` contains migration history and historical authority references. Nothing there is current by default.

## Reorganization status
> **COMPLETE**

Next work should happen inside the owning subject domain, using `90_WORKING` only as a temporary drafting/staging area.

## Current routing checkpoint
- core enemy static design remains closed unless explicitly reopened;
- historical balance reports remain evidence, not an automatic work queue;
- current CEXP/class-progression authority is owned by `10_PROGRESSION_AND_EXP` and `06_CLASSES_AND_ABILITIES`;
- Prime loadout access remains **1 slot from Chapter 4 Prime-loadout access until Sixfold Volition; 2 after Volition**;
- playable-area/route layout production is an active project stream;
- character visual masters and their production locks are now repository-backed under the current visual authority system.

For unresolved work, follow `OPEN_AND_PENDING_WORK.md` rather than historical “Next” lines embedded in older reports.
