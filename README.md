# Diyse-Game

Clean Godot production repository for **Diyse**, an **HD-2D**, party-based, command-driven turn-based JRPG targeting Android.

This repository is the active implementation line. The older `zxxdjxxz-del/Diyse` repository is historical prototype reference only and is not a code source unless an explicit task authorizes named reuse.

## Current authority

- Whole-project authority: **Diyse: HD-2D JRPG Clean Active Complete Master Canon v1.98 / Audit113** (August 23, 2026).
- Current implementation-facing summary: `docs/ACTIVE_CANON.md`.
- Current late-game chapter reindex: `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`.
- Current Chapter-10 story authority: `docs/canon/AUDIT112_CHAPTER_10_THE_LAST_BLANK_MIRENA_EASTERN_WAYFINDER_CALDER_AND_BURIED_REGISTRY_CLOSURE.md`.
- Current final map / region authority: `docs/canon/AUDIT111_FINAL_WORLD_MAP_REGION_TERMINOLOGY_AND_VISUAL_AUTHORITY_CLOSURE.md`.
- Current travel / point-of-no-return authority: `docs/canon/AUDIT109_WORLD_MAP_ROAD_TRAVEL_AND_LAST_SHELTER_POINT_OF_NO_RETURN_CLOSURE.md`.

## Current production baseline

- Presentation: **HD-2D** only.
- Field characters: approximately **80 px**.
- Battle characters: approximately **200–220 px**.
- Dialogue: large high-resolution portraits.
- Battle composition: up to four active party members staggered on the left, enemies on the right, open center action/VFX lane.
- Dialogue is fully authored; no player dialogue choices.
- Random encounters remain the ordinary hostile-exploration layer where approved.
- Chapter 0 remains the fixed-authored tutorial exception.
- Android/APK remains the target.
- Target full-game runtime: approximately **25 hours**, subject to revalidation after the added Chapter 10.
- Player level cap: **70**.
- Base/Subclass class cap: **CL13**.
- Permanent commands: **Attack / Ability / Card / Item / Defend**.
- Exactly **24 Standard Cards** and **12 Prime Cards**.
- Standard Cards are unlimited-use.

## Current late-game chapter numbering

Chapter 10 — The Last Blank was inserted after Chapter 9.

Current numbering:

- **Chapter 10 — The Last Blank** — Mirena records lead / Cerythvale / discovery of Eastern Wayfinder / physical-map completion / Calder provenance / Buried Registry.
- **Chapter 11** — Crown Engine / Othmar Calder / Custodian / Truth.
- **Chapter 12 — The Reforged March** — final Black Host campaign / Varkesh / Vhalmarch Forward Hub / Vorathen / Vaelkor / cleanup.
- **Chapter 13 — The Last Command** — final Ancient domain / Last Weapon Archive / Last Shelter / Reconstituted Entity / Final Severance / ending.

Historical pre-insertion mapping:
- old Ch10 → current Ch11
- old Ch11 → current Ch12
- old Ch12 → current Ch13

Never use pre-insertion late-game chapter numbers as current implementation instructions.

Current operational chapter files:
- `docs/chapters/chapter_10/CHAPTER_10_THE_LAST_BLANK_STORY_STRUCTURE_LOCK.md`
- `docs/chapters/chapter_11/CHAPTER_11_CURRENT_SCOPE.md`
- `docs/chapters/chapter_12/CHAPTER_12_REFORGED_MARCH_FORWARD_HUB_AND_CLEANUP_LOCK.md`
- `docs/chapters/chapter_13/CHAPTER_13_MACRO_STORY_STRUCTURE_LOCK.md`

## Current point of no return

The deliberate launch of Chapter 13 is **not** the irreversible point of no return.

Current hard rule:

**Last Shelter → Reactor Galleries = true irreversible threshold.**

The player may enter Chapter 13 and advance through the early final domain while retaining supported return to eligible unfinished world content until that threshold.

## Current world terminology

Use:
- **BLACK HOST TERRITORY**
- **THE WESTWAYS**
- **THE GREYSPIRES**
- **YAHTRENHOLD**
- **The Blackspine**
- **Westguard**
- **Vhalmarch**

Do not restore `Blackstone` as the formal region label, `The Crownhold`, `Westreach`, or `Black Mountains` as current names.

## Current Faces / Story Primes

Faces:
- Might
- Elements
- Grace
- Acuity
- Change
- Ruin

Story Primes:
- Might — **Last Sentinel**
- Elements — **Last Convergence**
- Grace — **Last Sanctuary**
- Acuity — **Last Cartographer**
- Change — **Last Scribe**
- Ruin — **Last Erasure**

No Prime had ever been successfully activated before the modern story.

`Resource / Last Measure` is retired current-facing terminology.

## Current chapter authority state

Chapters 0–4 remain closed at story/dialogue authority level and retain the completed HD-2D conversion work where compatible with later canon.

Current late-game macro files are chapter-correct after Audit113. Detailed line-complete dialogue for Chapters 10–13 remains separate production work unless explicitly locked in a later scene pass.

See `docs/chapters/README.md` for the current chapter index.

## Core system guardrails

- Engine: Godot 4.x production line / GDScript.
- Platform: Android, landscape.
- Combat: discrete round-based command combat.
- Maximum active party: four.
- MP is the universal ordinary Ability resource; no character-specific combat gauges.
- No Ability or Ultimate requires a specific equipped weapon once learned.
- Maximum eight simultaneously active enemies.
- Cards remain outside ordinary inventory.
- Once equipment/Ability access is legally unlocked, it persists under current open-equipment rules.
- Keep authored content data-driven where practical and never invent mechanics/canon to make implementation easier.

## Equipment / item counts

Current architecture:
- Consumables: **20**
- Ordinary Equipment: **48**
- Relics: **64**
- Legacies: **6**
- Total Equipment: **118**
- Standard Cards: **24**
- Prime Cards: **12**
- General Accessories: **0**

Final raw equipment stats and late-game progression tuning remain for the dedicated item/progression pass.

## Production workflow

Before implementation:

1. read `docs/ACTIVE_CANON.md`;
2. read the relevant current chapter source under `docs/chapters/`;
3. read the latest controlling canon audit for that subject;
4. preserve approved wording/story/gameplay and exact map authority;
5. do not use historical chapter numbers or retired regional names as current-facing authority;
6. run the relevant content/regression gates.

Historical audits remain useful provenance, but later explicit overlays and current operational files control implementation.

Read `AGENTS.md`, `docs/ACTIVE_CANON.md`, `docs/IMPLEMENTATION_STATUS.md`, `docs/PRESENTATION_RULES.md`, `docs/chapters/README.md`, `docs/chapters/dialogue/README.md`, and the relevant subsystem rules before implementation.
