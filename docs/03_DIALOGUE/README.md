# 03_DIALOGUE
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicit user corrections/current domain migrations.  
**Repository source checkpoint used for exact dialogue extraction:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Dialogue authority rule:** exact accepted spoken wording is preserved unless a later bounded canon correction directly supersedes a term or line. Story function lives in `02_STORY`; combat mechanics live in `05_BATTLE_SYSTEM` / `09_ENEMIES_AND_ENCOUNTERS`; Card mechanics live in `07_CARDS`; progression lives in `10_PROGRESSION_AND_EXP`.


This is the canonical home for **spoken dialogue and dialogue-scene authoring**.

## Current status
- **Chapter 0:** exact runtime dialogue existed as Godot Resources; migrated here into readable Markdown transcripts without changing spoken text.
- **Chapters 1–4:** line-complete approved Markdown authoring exists and is migrated here.
- **Chapters 5–13:** not silently rewritten. Their current authoring status is recorded under `AUTHORING_STATUS/`.

## Line-complete closed set
Exactly **41 current dialogue/scene sources** are preserved:
- Ch0: S001–S006 + C01–C02 = 8
- Ch1: S007–S011 + C03–C05 = 8
- Ch2: S012–S016 + C06–C07 = 7
- Ch3: S017–S021 + H01–H04 = 9
- Ch4: S022–S026 + C08/C09/H05 + Crown Prototype = 9

## What this folder owns
- exact spoken lines;
- speaker order;
- dialogue-scene staging that materially controls delivery;
- optional Character-Life/camp dialogue;
- dialogue-specific identity/continuity overlays.

## What this folder does not own
Embedded old source notes may mention mechanics for context, but those are **not editable authority here**. Current mechanics must be read from their canonical system folders.

## Current bounded dialogue corrections applied during migration
1. Ch1 S009 production firewall: `Sixfold Accord` → **Sixfold Volition**.
2. Ch3 S019 spoken Face list: `Resource` → **Acuity**.
3. Ch0 old internal `Broken Champion's Ward` wording is not carried into current-facing transcript staging; it is described as the **incomplete protective response**.
4. Ch0 negative old `First Champion` terminology is normalized to **Last Sentinel** where it appears in nonspoken staging context.
5. Current region/place corrections already present in the repository source are preserved: **Yahtrenhold**, **Reaction Annex**, etc.

These are bounded current-canon reconciliations, not general dialogue rewrites.
