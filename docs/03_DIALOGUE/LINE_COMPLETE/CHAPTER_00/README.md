# Chapter 0 — Dialogue Source
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicit user corrections/current domain migrations.  
**Repository source checkpoint used for exact dialogue extraction:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Dialogue authority rule:** exact accepted spoken wording is preserved unless a later bounded canon correction directly supersedes a term or line. Story function lives in `02_STORY`; combat mechanics live in `05_BATTLE_SYSTEM` / `09_ENEMIES_AND_ENCOUNTERS`; Card mechanics live in `07_CARDS`; progression lives in `10_PROGRESSION_AND_EXP`.


Exact Chapter-0 spoken text originally existed directly in validated Godot `.tres` Resources rather than a dedicated Markdown transcript directory.

This migration converts:
- S001–S006
- C01–C02

into readable Markdown while preserving every spoken `speaker_id` + `text` pair.

Current compatibility:
- the green/gold Chapter-0 phenomenon is an **incomplete protective response**;
- it is not a Prime activation;
- it is not Last Sentinel activation/confirmation;
- the old internal `Broken Champion's Ward` label is retired from current-facing authoring;
- legacy technical IDs are not reproduced as current canon terminology.
