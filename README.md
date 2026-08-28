# Diyse-Game

Clean Godot production repository for **Diyse**, an **HD-2D**, party-based, command-driven turn-based JRPG targeting Android.

This repository is the active implementation line. The older `zxxdjxxz-del/Diyse` repository is historical prototype reference only and is not a code source unless an explicit task authorizes named reuse.

## Current authority

- Whole-project authority: **Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.20 / Audit135** (August 27, 2026).
- Current implementation-facing summary: `docs/ACTIVE_CANON.md`.
- Current Major-Hunt raw-stat authority: `docs/canon/AUDIT135_MAJOR_HUNT_RAW_STAT_RECERTIFICATION_LOCK.md`.
- Current Regional-Hunt raw-stat authority: `docs/canon/AUDIT134_REGIONAL_HUNT_RAW_STAT_RECERTIFICATION_LOCK.md`.
- Current class/progression authority: `docs/canon/AUDIT123_CLASS_MP_CEXP_MASTERY_AND_LATE_GAME_PROGRESSION_LOCK.md` through Audits124–128.
- Current mandatory/optional named raw-stat chain: Audits129–135.
- Current late-game chapter reindex: `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`.
- Current final map / region authority: `docs/canon/AUDIT111_FINAL_WORLD_MAP_REGION_TERMINOLOGY_AND_VISUAL_AUTHORITY_CLOSURE.md` plus compatible later corrections.
- Current travel / point-of-no-return authority: `docs/canon/AUDIT109_WORLD_MAP_ROAD_TRAVEL_AND_LAST_SHELTER_POINT_OF_NO_RETURN_CLOSURE.md`.

## Current production baseline

- Presentation: **HD-2D** only.
- Field characters: approximately **80 px**.
- Battle characters: approximately **200–220 px**.
- Dialogue: large high-resolution portraits.
- Battle composition: up to four active party members staggered on the left, enemies on the right, open center action/VFX lane.
- Dialogue is fully authored; no player dialogue choices.
- Random encounters remain the ordinary hostile-exploration layer where approved.
- Chapter 0 remains the fixed-authored tutorial exception and grants no player levels.
- Android/APK remains the target.
- Target full-game runtime: approximately **25 hours**, subject to revalidation as production matures.
- Player level cap: **70**.
- Base/Subclass class cap: **CL13**.
- Permanent commands: **Attack / Ability / Card / Item / Defend**.
- Exactly **24 Standard Cards** and **12 Prime Cards**.
- Standard Cards are reusable MP-cost commands.

## Current classes / Faces

| Character | Base | Subclass | Face |
|---|---|---|---|
| Cyanis | Crest Knight | Crest Arcanist | Might |
| Ilyra | Blue Warden | Vowblade | Grace |
| Torren | War Archer | Routeweaver | Acuity |
| Nimera | Cardweaver | Proofhunter | Change |
| Vaelira | Green Arcanist | Axiomblade | Elements |
| Seyrik | Ruin Vanguard | Ruin Warden | Ruin |

Synthesis is removed. No permanent Subclass use occurs before the end-Ch7 **Sixfold Volition**.

## Current progression spine

Class Ability MP certification is closed under Audit123.

- CL13 cumulative CEXP: **6,000**.
- Exactly 8 automatic Mastery Points: **Lv5 / 10 / 15 / 20 / Sixfold Volition / 40 / 50 / 60**.
- Normal-route player anchors: Ch1 5 / Ch2 9 / Ch3 13 / Ch4 17 / Ch5 22 / Ch6 27 / Ch7 32 / Ch8 37 / Ch9 42 / Ch10 47 / Ch11 52 / Ch12 57 / Last Shelter 60 / ending 62.
- Level cap: **70**.
- Normal full Base + Subclass Class-Level completion occurs during Ch12; final Mastery-board completion lands around Lv60.

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
- **Vorathen**
- **The Veiled Citadel**

Do not restore `Blackstone` as the formal region label, `The Crownhold`, `Southhold`, `Westreach`, `Yahtrens Stand`, or `Black Mountains` as current names.

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

## Core combat guardrails

- Physical direct damage: `Attack² / (Attack + EffectiveDefense) × Power/100`.
- Magical direct damage: `Magic² / (Magic + EffectiveSpirit) × Power/100`.
- **Spirit** is magical defense.
- There is no natural Accuracy stat; actions use **Base Hit** against target **Evasion**.
- Status Resistance general bands: **0 / 5 / 10 / 15**; explicit immunity remains separate.
- **Barrier does not exist.**
- **Brace does not exist.**
- There is no global Break/Stagger meter; **Staggered** is an ordinary harmful status only.
- **Guard** remains valid.
- Genuine fresh-HP boss forms refresh Prime availability; same-bar state changes do not.

## Equipment / item counts

Current architecture:
- Consumables: **20**
- Ordinary Equipment: **38**
- Relics: **36**
- Legacies: **17**
- Total Equipment: **91**
- Standard Cards: **24**
- Prime Cards: **12**
- General Accessories: **0**

Current hierarchy:

> **Ordinary < Relic < Legacy**

## Optional challenge raw-stat closure

Progression-dependent raw-stat recertification is closed through Audit135.

- 12 current numbered-chapter optional Elites; no approved Ch10 Elite.
- 11 Regional Hunts closed under Audit134.
- 6 Major Hunts closed under Audit135.
- Fixed authored tuning; no dynamic Hunt scaling.
- Recommended Hunt level is a preparedness target, not an access gate.

Current tier principle:

> **Ordinary < Elite < mandatory story boss < Regional Hunt < Major Hunt**

The Unfinished World remains the Lv70 apex Major Hunt at **78,000 HP** on one continuous WORLDFRAME → WORLDHEART EXPOSED → FINAL CONSTRUCTION bar.

## Current implementation frontier

Current next concrete content/implementation frontier:

**Kessara Relic-copy service implementation.**

Closed core rule:
- Relic must already be obtained;
- one matching copy component is required;
- maximum one forged duplicate per Relic;
- maximum quantity = 2;
- copy is mechanically identical;
- Legacies cannot be copied.

Remaining design/implementation work may decide service fee, menu timing, and original-vs-copy UI presentation.

## Production workflow

Before implementation:

1. read `docs/ACTIVE_CANON.md`;
2. read `docs/IMPLEMENTATION_STATUS.md`;
3. read `AGENTS.md` and `docs/AI_ENGINEERING_RULES.md`;
4. read the relevant current chapter source under `docs/chapters/`;
5. read the latest controlling canon audit for that subject;
6. preserve approved wording/story/gameplay and exact map authority;
7. do not use historical chapter numbers, retired systems, or retired regional names as current-facing authority;
8. run the relevant content/regression gates.

Historical audits remain useful provenance, but later explicit overlays and current operational files control implementation.