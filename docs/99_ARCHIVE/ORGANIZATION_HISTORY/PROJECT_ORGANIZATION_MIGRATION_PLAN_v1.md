# DIYSE — PROJECT ORGANIZATION & MIGRATION CONTROL
## 00_MASTER_CONTROL
**Organization revision:** v1
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`
**Purpose:** Establish the permanent subject-folder architecture for Diyse and prevent canon from remaining duplicated across giant cumulative trackers.

---

# 1. CORE ORGANIZATION RULE

Every current rule, asset, table, scene, character fact, enemy kit, item, or progression rule must have exactly **one canonical home**.

Other files may reference that material, but should not redefine it.

The consolidated working tracker remains useful for:
- current work status;
- change history;
- unresolved items;
- handoff notes.

It is no longer intended to be the permanent canonical home of all project material.

---


## Migration note — stale internal revision labels

The v85 tracker itself still contains at least one inherited sentence referring to
`This v65 working revision`. Treat that as stale copy-forward text, not as evidence
that v65 is current. The document header controls: the active consolidated working
revision is **v85**. Correct inherited internal revision labels during extraction
without changing the underlying mechanic unless separately required.


# 2. PROJECT FOLDER STRUCTURE

## 00_MASTER_CONTROL
- `DIYSE_MASTER_INDEX.md`
- `CURRENT_CANON_STATUS.md`
- `OPEN_AND_PENDING_WORK.md`
- `TERMINOLOGY_GLOSSARY.md`
- `RETIRED_TERMINOLOGY_MAP.md`
- `CHANGELOG.md`
- `MIGRATION_LOG.md`

## 01_CHARACTERS
### PLAYABLE
- Cyanis
- Ilyra
- Torren
- Nimera
- Vaelira
- Seyrik

### SUPPORTING
### ANTAGONISTS
### RELATIONSHIPS
- `CHARACTER_TIMELINE.md`
- `CHARACTER_MASTER_INDEX.md`

## 02_STORY
- `MASTER_STORY_STRUCTURE.md`
- `STORY_TIMELINE.md`
- `STORY_CONTINUITY_NOTES.md`
- `CHAPTER_00/`
- `CHAPTER_01/`
- `CHAPTER_02/`
- `CHAPTER_03/`
- `CHAPTER_04/`
- `CHAPTER_05/`
- `CHAPTER_06/`
- `CHAPTER_07/`
- `CHAPTER_08/`
- `CHAPTER_09/`
- `CHAPTER_10/`
- `CHAPTER_11/`
- `CHAPTER_12/`
- `CHAPTER_13/`
- `FINALE/`

## 03_DIALOGUE
- `DIALOGUE_STYLE_BIBLE.md`
- `CHARACTER_VOICES/`
- `PAIR_DYNAMICS/`
- `ENSEMBLE_RULES/`
- chapter dialogue files
- `CHARACTER_QUEST_DIALOGUE/`
- `SIDE_QUEST_DIALOGUE/`

## 04_WORLD_AND_LORE
- `WORLD_MAP.md`
- `LOCATIONS/`
- `REGIONS/`
- `FACTIONS/`
- `YAHTREA_HISTORY.md`
- `DIYSEAN_HISTORY.md`
- `BLACK_HOST.md`
- `CARD_HISTORY.md`
- `WORLD_TIMELINE.md`
- `PLACE_NAME_AUTHORITY.md`

## 05_BATTLE_SYSTEM
- `BATTLE_SYSTEM_MASTER.md`
- `TURN_AND_ROUND_RULES.md`
- `DAMAGE_FORMULAS.md`
- `BASE_HIT_AND_EVASION.md`
- `CRITICAL_HITS.md`
- `STATS.md`
- `TARGETING.md`
- `STATUS_EFFECTS.md`
- `ELEMENTS.md`
- `BUFFS_AND_DEBUFFS.md`
- `DEATH_DEFEAT_SUBDUAL.md`
- `GUARD.md`
- `PARTY_AND_RESERVES.md`
- `BOSS_FORM_RULES.md`

## 06_CLASSES_AND_ABILITIES
- `CLASS_SYSTEM_MASTER.md`
- `CLASS_EXP_AND_MASTERY_RULES.md`
- `ABILITY_RULES.md`
- `MP_COST_RULES.md`
- `BASE_CLASSES/`
- `SUBCLASSES/`
- `ABILITY_MASTER_REGISTER.md`
- `TRAITS.md`
- `ULTIMATES.md`
- `MASTERY.md`

## 07_CARDS
- `CARD_SYSTEM_MASTER.md`
- `SIX_FACES.md`
- `STANDARD_CARDS/`
- `PRIME_CARDS/`
- `CARD_ACQUISITION.md`
- `STANDARD_CARD_MASTER_REGISTER.md`
- `PRIME_MASTER_REGISTER.md`

## 08_ITEMS_AND_EQUIPMENT
- `EQUIPMENT_SYSTEM_MASTER.md`
- `WEAPONS/`
- `ARMOR/`
- `ACCESSORIES/`
- `FOCI/`
- `CONDUITS/`
- `RELICS/`
- `LEGACIES/`
- `CONSUMABLES/`
- `KEY_ITEMS/`
- `MATERIALS/`
- `ITEM_MASTER_REGISTER.md`
- `EQUIPMENT_MASTER_REGISTER.md`

## 09_ENEMIES_AND_ENCOUNTERS
- `ENEMY_SYSTEM_RULES.md`
- `ENEMY_MASTER_REGISTER.md`
- `CHAPTER_ENEMIES/`
- `REGIONAL_ENEMIES/`
- `ELITES/`
- `STORY_BOSSES/`
- `MAJOR_HUNTS/`
- `SUPPORT_OBJECTS/`
- `ENCOUNTER_FORMATIONS/`
- `ENEMY_REUSE_AND_VARIANT_RULES.md`

## 10_PROGRESSION_AND_EXP
- `PROGRESSION_MASTER.md`
- `CHARACTER_EXP.md`
- `CLASS_EXP_CEXP.md`
- `LEVEL_CURVE.md`
- `CHAPTER_LEVEL_BANDS.md`
- `RECRUITMENT_LEVELS.md`
- `RESERVE_PROGRESSION.md`
- `MASTERY_PROGRESSION.md`
- `PROGRESSION_SIMULATIONS/`

## 11_QUESTS
- `QUEST_SYSTEM_MASTER.md`
- `CHARACTER_QUESTS/`
- `SIDE_QUESTS/`
- `MAJOR_HUNTS/`
- `QUEST_UNLOCKS.md`
- `QUEST_MASTER_REGISTER.md`

## 12_ECONOMY_AND_REWARDS
- `ECONOMY_MASTER.md`
- `AUREN.md`
- `SHOP_PRICING.md`
- `ENEMY_REWARDS.md`
- `QUEST_REWARDS.md`
- `BOSS_REWARDS.md`
- `DROP_RULES.md`
- `REWARD_BUDGETS.md`

## 13_UI_AND_IMPLEMENTATION
- `COMBAT_UI.md`
- `MENUS.md`
- `EQUIPMENT_UI.md`
- `CARD_UI.md`
- `DIALOGUE_UI.md`
- `SAVE_DATA.md`
- `IMPLEMENTATION_NOTES/`

## 14_ART_AND_VISUALS
- `VISUAL_STYLE_BIBLE.md`
- `CHARACTER_MASTERS/`
- `ENEMIES/`
- `LOCATIONS/`
- `BLACK_HOST/`
- `UI/`
- `WORLD_MAP/`

## 15_AUDIO_AND_MUSIC
- `MUSIC_DIRECTION.md`
- `ANCIENT_DIYSE_MUSIC/`
- `CHARACTER_THEMES/`
- `REGION_THEMES/`
- `BATTLE_MUSIC/`
- `AUDIO_RESEARCH/`

## 16_BALANCE_AND_TESTING
- `BALANCE_MASTER.md`
- `PLAYER_STAT_TESTING/`
- `ENEMY_STAT_TESTING/`
- `DAMAGE_TESTING/`
- `EXP_CEXP_TESTING/`
- `EQUIPMENT_BALANCE/`
- `CARD_BALANCE/`
- `PLAYTEST_RESULTS/`

## 90_WORKING
- `ACTIVE_TRACKERS/`
- `CURRENT_AUDITS/`
- `UNSORTED_NEW_WORK/`
- `PENDING_APPROVAL/`

## 99_ARCHIVE
- `OLD_MASTER_CANONS/`
- `SUPERSEDED_TRACKERS/`
- `RETIRED_SYSTEMS/`
- `RETIRED_NAMES/`
- `OLD_STORY_VERSIONS/`
- `OLD_BALANCE_PASSES/`

---

# 3. AUTHORITY RULE AFTER MIGRATION

Use this order:

1. newest explicit approved user correction;
2. current domain canonical file;
3. current master-control authority/index;
4. current working tracker for unresolved or unpromoted work;
5. archived material only for provenance or recovery.

Archived material must never silently overwrite a newer domain file.

---

# 4. v85 SECTION MIGRATION MAP

The current v85 consolidated tracker should be split as follows.

| v85 material | Permanent home |
|---|---|
| Current authority / precedence | `00_MASTER_CONTROL/` |
| Core battle presentation rules | `05_BATTLE_SYSTEM/` |
| Player level/cap overview | `10_PROGRESSION_AND_EXP/` |
| Chapter spine | `02_STORY/` |
| Six characters / class identities | `01_CHARACTERS/` + `06_CLASSES_AND_ABILITIES/` |
| Class / mastery progression | `06_CLASSES_AND_ABILITIES/` + `10_PROGRESSION_AND_EXP/` |
| Damage formulas | `05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md` |
| Base Hit / Evasion | `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md` |
| Critical Hit rules | `05_BATTLE_SYSTEM/CRITICAL_HITS.md` |
| Elements / status baseline | `05_BATTLE_SYSTEM/ELEMENTS.md` + `STATUS_EFFECTS.md` |
| Standard Cards | `07_CARDS/STANDARD_CARDS/` |
| Prime system | `07_CARDS/PRIME_CARDS/` |
| Consumables | `08_ITEMS_AND_EQUIPMENT/CONSUMABLES/` |
| Consumable prices / shop timing | `12_ECONOMY_AND_REWARDS/` |
| Ordinary equipment | `08_ITEMS_AND_EQUIPMENT/` |
| Relics | `08_ITEMS_AND_EQUIPMENT/RELICS/` |
| Legacies | `08_ITEMS_AND_EQUIPMENT/LEGACIES/` |
| Legacy precursors | equipment definition in `08`; acquisition/story reference in `11` or `02` |
| Side quests | `11_QUESTS/SIDE_QUESTS/` |
| Open / pending queue | `00_MASTER_CONTROL/OPEN_AND_PENDING_WORK.md` |
| Active unfinished passes | `90_WORKING/` |
| Retired branches | `99_ARCHIVE/` |
| Retired terminology | `00_MASTER_CONTROL/RETIRED_TERMINOLOGY_MAP.md` |
| Change records | `00_MASTER_CONTROL/CHANGELOG.md` |
| Chapter 4 four-element story changes | `02_STORY/CHAPTER_04/` |
| Chapter 4 enemy mechanics | `09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/CHAPTER_04/` |
| Chapter 4 elemental system references | references to `05_BATTLE_SYSTEM/ELEMENTS.md` |

---

# 5. DUPLICATION RULES

## Character vs Class
Character history, age, personality, relationships, appearance, recruitment, and narrative arc belong in `01_CHARACTERS`.

Class commands, Traits, Ultimates, equipment permissions, mastery requirements, and MP costs belong in `06_CLASSES_AND_ABILITIES`.

A character file references their class files rather than copying full kits.

## Story vs Dialogue
Story files contain:
- scene purpose;
- events;
- entrances/exits;
- battles;
- reveals;
- location movement;
- consequences.

Dialogue files contain actual spoken lines and scene dialogue execution.

Do not maintain two separately editable copies of the same dialogue.

## Battle rules vs Ability definitions
Global rules such as damage, Crit, Hit/Evasion, Guard, statuses, and elements belong in `05_BATTLE_SYSTEM`.

Individual abilities reference those mechanics from `06_CLASSES_AND_ABILITIES`.

## Equipment vs Economy
The item itself, its stats, Trait, slot, and eligibility belong in `08_ITEMS_AND_EQUIPMENT`.

Its purchase price, sell price, shop availability, and economic pacing belong in `12_ECONOMY_AND_REWARDS`.

## Enemies vs Progression
Enemy identity, actions, resistances, AI, phases, and encounter role belong in `09_ENEMIES_AND_ENCOUNTERS`.

Global level bands, EXP/CEXP yields, scaling philosophy, and progression simulations belong in `10_PROGRESSION_AND_EXP`.

## Quest vs Story
A quest's structure, unlock, objectives, reward references, and completion state belong in `11_QUESTS`.

Any main-story consequences are referenced from `02_STORY`, not duplicated wholesale.

---

# 6. MIGRATION ORDER

## Phase 1 — Control Layer
1. Master Index
2. Current Canon Status
3. Open / Pending Work
4. Terminology Glossary
5. Retired Terminology Map
6. Changelog / Migration Log

## Phase 2 — Foundational Systems
1. Battle System
2. Classes & Abilities
3. Cards
4. Items & Equipment
5. Progression & EXP

## Phase 3 — Game Content
1. Characters
2. World & Lore
3. Enemies & Encounters
4. Story
5. Dialogue
6. Quests

## Phase 4 — Supporting Production
1. Economy & Rewards
2. UI / Implementation
3. Art / Visuals
4. Audio / Music
5. Balance / Testing

## Phase 5 — Archive Cleanup
Move obsolete trackers, retired terminology, rejected branches, and superseded versions into `99_ARCHIVE`.

---

# 7. IMMEDIATE FIRST EXTRACTION BATCH

The first content extraction should be:

### `05_BATTLE_SYSTEM`
because these rules are foundational and already relatively self-contained in v85.

Create first:
- `BATTLE_SYSTEM_MASTER.md`
- `DAMAGE_FORMULAS.md`
- `BASE_HIT_AND_EVASION.md`
- `CRITICAL_HITS.md`
- `ELEMENTS.md`
- `STATUS_EFFECTS.md`
- `GUARD.md`
- `BOSS_FORM_RULES.md`

After that, extract `06_CLASSES_AND_ABILITIES`, then `07_CARDS`.

---

# 8. MIGRATION SAFETY

During migration:
- do not rewrite mechanics merely for organization;
- do not silently fill missing values;
- preserve open items as OPEN;
- preserve pending items as PENDING;
- flag contradictions instead of choosing arbitrarily;
- apply known retired terminology corrections during extraction;
- preserve historical files in archive;
- never treat archive material as current merely because it is more detailed.

---

# 9. WORKING TRACKER ROLE AFTER MIGRATION

The consolidated tracker becomes:

`90_WORKING/ACTIVE_TRACKERS/DIYSE_CURRENT_WORKING_TRACKER.md`

Its job is to contain:
- what we are currently working on;
- decisions awaiting promotion;
- unresolved questions;
- last migration point;
- change log references.

It should no longer duplicate complete canonical catalogs and rulebooks.

---

# 10. NEXT ACTION

Begin **05_BATTLE_SYSTEM extraction** from the v85 migration baseline.

Once the Battle System folder is complete and reconciled, mark those tracker sections as migrated and proceed to:
1. Classes & Abilities
2. Cards
3. Items & Equipment
4. Progression & EXP
