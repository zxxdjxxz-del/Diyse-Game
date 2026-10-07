# DIYSE MASTER INDEX

## Authority

Newest explicit approved correction → current owning numbered domain → `00_MASTER_CONTROL` cross-domain rule → `90_WORKING` only for unresolved sequencing/work.

Git history is recovery infrastructure, not part of the normal authority chain.

Cross-domain terminology handoffs:
- current class names → `CLASS_TERMINOLOGY_CURRENT.md`
- current Face names → `FACE_TERMINOLOGY_CURRENT.md`
- current glossary → `TERMINOLOGY_GLOSSARY.md`

## Active domains

### 01_CHARACTERS
Playable/supporting/antagonist identities, relationships, chronology, and character-specific boundaries.

### 02_STORY
Chapter 0–13 mandatory spine, arcs, reveal order, recruitment, PONR, and ending.

### 03_DIALOGUE
Exact current dialogue for completed chapters plus authoring status for later chapters.

### 04_WORLD_AND_LORE
Current geography, map, factions, modern/ancient history, and lore truth.

### 05_BATTLE_SYSTEM
Global TURN / EXECUTION combat formulas, action timing, targeting, statuses, elements, and boss-form rules.

### 06_CLASSES_AND_ABILITIES
12 classes, Ability/Ultimate roster, Traits, MP, class progression structure, and automatic Masteries.

### 07_CARDS
24 Standard Cards, 12 Primes, the six current Faces, 4-slot Standard Card loadouts, Prime loadouts, progression, Manifestation Meter rules, and Prime runtime behavior.

### 08_ITEMS_AND_EQUIPMENT
Consumables, 91 equipment identities, Relics, Legacies, Forge Components, and project materials.

### 09_ENEMIES_AND_ENCOUNTERS
Chapter rosters, formations, raw-stat/action owners, bosses, **strong normal-pool enemies**, Regional Hunts, Major Hunts, and support objects.

There is no separate Elite encounter category.

### 10_PROGRESSION_AND_EXP
Player EXP, level curve, CEXP, overlevel controls, reward/progression placement, and the current rebuild frontier.

### 11_QUESTS
6 Character Quests, 5 ordinary Side Quests, 8 active Regional Hunts, 6 Major Hunts, and optional-content cutoff.

### 12_ECONOMY_AND_REWARDS
Player-facing **G**, prices/shops/rewards, with detailed numeric recalibration still open.

### 13_UI_AND_IMPLEMENTATION
Production UI/runtime requirements, save-state boundaries, current Godot proof status, and implementation debt.

### 14_ART_AND_VISUALS
Exact visual authorities, HD-2D world/presentation grammar, environment/VFX production rules, and asset provenance.

Permanent-party field/battle runtime direction:
> **rigged 3D models matched to the exact current 2D masters**

Current character masters:
> `asset_sources/characters/current/`

Current character visual authority:
> `docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`

### 15_AUDIO_AND_MUSIC
Open soundtrack authority, sound-design requirements, and implementation boundary.

### 16_BALANCE_AND_TESTING
Current balance/rebuild frontier, regression matrices, test methods, and release gates.

Current true-battle certification method:
> `../16_BALANCE_AND_TESTING/TRUE_BATTLES/TRUE_BATTLE_TEST_PROTOCOL.md`

## Working layer

`../90_WORKING/` is not a second canon tracker.

Live contents are limited to:
- `../90_WORKING/ACTIVE_WORK_QUEUE.md`;
- playable-area/route production files and blueprints.

## Repository retention

`main` contains current authority and active production dependencies. Compatibility, validation, and source-provenance data remain only where a current production requirement depends on them.

## Reorganization status

> **COMPLETE**

New work should update its numbered owner domain first. Temporary cross-domain production notes belong in `90_WORKING` only when a dedicated working surface is genuinely needed.
