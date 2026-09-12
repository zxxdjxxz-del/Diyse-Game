# Diyse — Dialogue Master Index

**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicit user corrections/current domain migrations.  
**Dialogue production root:** `docs/03_DIALOGUE/PRODUCTION/`

## Dialogue Engine rule

The Diyse Dialogue Engine is the production authoring method for current spoken dialogue across the game. It combines current story authority, character brains, relationship state, lived-world/economy context, map/traversal state, gameplay pressure, naturalistic/cinematic/comedic craft, anime expressiveness, and economical HD-2D staging.

Current production dialogue lives under `PRODUCTION/CHAPTER_##/`. Story function and chapter structure remain owned by `docs/02_STORY/CHAPTERS/`.

Historical pre-rehearsal / pre-Dialogue-Engine material does **not** control current spoken wording. For Chapters 0 and 1, the obsolete `LINE_COMPLETE/CHAPTER_00` and `LINE_COMPLETE/CHAPTER_01` sets have been removed from the live repository tree. Their history remains recoverable through Git if provenance is ever needed.

### Production-pipeline continuity hard lock

> **The rehearsal-first Agent Brain system used to create the current completed Chapter 0 and Chapter 1 production dialogue is the mandatory dialogue-production method for Chapter 2 through Chapter 13 and all future Diyse dialogue unless explicitly revised by the user.**

Required sequence:

> **scene/world state → independent Person Agent Brain rehearsals → Dialogue Editor → invisible Canon/Knowledge Checker → economical HD-2D staging/implementation**

Each participating character must use the current full Agent Brain/profile available at authoring time, including relevant life history, world knowledge, personal knowledge boundaries, relationship state, memories, motives, current context, expertise limits, and individual speaking behavior. Do not revert to the older simplified dialogue-agent method, a generic whole-cast single pass, or direct production-script generation from canon constraints.

Owning lock: `AGENT_SYSTEM/CHAPTER_0_1_PIPELINE_CONTINUITY_LOCK.md`.

### Story-beat guardrail hard lock

> **Story structure controls the situation, hard outcomes, reveal boundaries, and gameplay state. It does not pre-write the conversational path.**

Owning lock: `AGENT_SYSTEM/STORY_BEAT_AS_GUARDRAIL_LOCK.md`.

Production specs must not assign speaker order, required conversational checkpoints, required jokes, motivation speeches, firewall dialogue, or one required verbal contribution to every present character. The Person Agents discover the route through the scene; the Editor shapes what survives; the Canon Checker remains invisible.

This rule was added after Chapter-3 Beats 6–8 drifted too far toward checkpoint-driven scripting. Beats 6–8 have now been rerun under the corrected method, and Beat 9 onward begins under it from the start.

The Railway/Render services are deployment/runtime implementations of the Agent Brain architecture/profile lineage; they do not supersede the current Agent Brain data or this authoring-workflow lock.

### Walking-dialogue hard lock

> **Do not use walking dialogue scenes during ordinary traversal unless the party is actively being led somewhere by another person.**

Owning detailed lock: `AGENT_SYSTEM/WALKING_DIALOGUE_LOCK.md`.

## Current chapter status

| Chapter | Current dialogue status |
|---|---|
| Ch0 | **COMPLETE CURRENT WORKING PRODUCTION** — `PRODUCTION/CHAPTER_00/CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` |
| Ch1 | **COMPLETE CURRENT WORKING PRODUCTION** — `PRODUCTION/CHAPTER_01/CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` |
| Ch2 | pending current Dialogue Engine production **under the locked Ch0–1 Agent Brain pipeline** |
| Ch3 | **ACTIVE REHEARSAL-FIRST PRODUCTION** — standalone Beats 1–10 Draft A complete; **Beats 6–8 rerun under the story-beat-as-guardrail correction; Beats 9–10 created under that method from the start**; cumulative readable manuscript currently assembled through Beat 5 at `PRODUCTION/CHAPTER_03/CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` |
| Ch4 | pending current Dialogue Engine production under the locked Ch0–1 Agent Brain pipeline and current restructured story authority |
| Ch5 | beat rewrite required before dialogue generation; subsequent dialogue uses the locked Ch0–1 Agent Brain pipeline |
| Ch6 | macro/beat authority; dialogue pending under the locked Ch0–1 Agent Brain pipeline |
| Ch7 | macro authority; dialogue pending under the locked Ch0–1 Agent Brain pipeline |
| Ch8 | macro authority; dialogue pending under the locked Ch0–1 Agent Brain pipeline |
| Ch9 | macro/beat authority; dialogue pending under the locked Ch0–1 Agent Brain pipeline |
| Ch10 | detailed story architecture; dialogue pending under the locked Ch0–1 Agent Brain pipeline |
| Ch11 | macro authority; dialogue pending under the locked Ch0–1 Agent Brain pipeline |
| Ch12 | macro authority; dialogue pending under the locked Ch0–1 Agent Brain pipeline |
| Ch13 | macro authority; dialogue pending under the locked Ch0–1 Agent Brain pipeline |

`COMPLETE CURRENT WORKING PRODUCTION` means the chapter is assembled end-to-end and is the version to use going forward. It is still editable during implementation/playtesting; it is not a claim that every line is permanently immutable.

## Chapter 0 current production

Current sequence:

> **P01 → P02 → P03 → P04 → P05 → P06 → P07 → optional C01 `Six Minutes` → explicit departure to Brackenwall**

Current production manuscript:
`PRODUCTION/CHAPTER_00/CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`

Current standalone scene drafts are stored beside it under `PRODUCTION/CHAPTER_00/`.

Key current facts:
- Cyanis begins alone; Ilyra enters during P04 and independently joins the defense;
- first incomplete Card flare occurs in P04 and fully ends before P05;
- P05 is the concealed Ruin Vanguard Pursuer only; the Card remains inert;
- P06 is the combined **Riftmaw + Convoy War-Sorcerer** final boss;
- the recovery casing breaks during P06 after the second flare begins;
- the Card survives intact and is carried directly from then onward;
- P07 closes through survivor recovery rather than celebration;
- C01 `Six Minutes` is the current optional Character-Life scene;
- Chapter 0 ends only when the player explicitly departs for Brackenwall.

The old locked Chapter-0 transcript set and the temporary casing-overlay manuscript are no longer live dialogue authority and have been removed from the current tree.

## Chapter 1 current production

Current production manuscript:
`PRODUCTION/CHAPTER_01/CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`

Current structure is Beats 1–15 plus optional Character-Life C03–C05 during the Junction camp cleanup window.

Current Character-Life drafts:
- C03 — `C03_TORRENS_VERSION_OF_DINNER_REHEARSAL_FIRST_DRAFT_C.md`
- C04 — `C04_WHAT_THE_MAP_SAYS_REHEARSAL_FIRST_DRAFT_A.md`
- C05 — `C05_NOT_PROFESSIONALLY_REHEARSAL_FIRST_DRAFT_D.md`

The obsolete Chapter-1 `LINE_COMPLETE` S007–S011/C03–C05 set and the superseded pre-rehearsal cumulative manuscript have been removed from the current tree.

## Chapter 3 current production

Current cumulative readable manuscript:
`PRODUCTION/CHAPTER_03/CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`

Current cumulative assembly coverage:
- Beats 1–5 are assembled in the cumulative manuscript.
- Beats 6–10 are current as standalone production drafts and remain authoritative before the next cumulative assembly pass.
- Beats 6–8 were fully rerun after the Agent-Brain freedom correction; Git history contains their retired checkpoint-driven versions.
- Beats 9–10 were authored from the start under `STORY_BEAT_AS_GUARDRAIL_LOCK.md`.

Current production status:
- Beat 1 — **Caelora Gate / Arrival — Draft A**;
- Beat 2 — **Royal Audience / The Chapter-2 Report — Draft A**;
- Beat 3 — **The Impossible Orders — Draft A**;
- Beat 4 — **The Seal That Wasn't Used — Draft A**;
- Beat 5 — **Old City Access / Archive Descent — Draft A**;
- Beat 6 — **Scholar in Redacted Stacks — Draft A, AGENT-DRIVEN RERUN COMPLETE**;
- Beat 7 — **Ancient Barrier / First Cooperation — Draft A, AGENT-DRIVEN RERUN COMPLETE**;
- Beat 8 — **Archive Scribe Engine / Nimera Joins — Draft A, AGENT-DRIVEN RERUN COMPLETE**; Nimera permanently joins here and the active permanent combat party becomes Cyanis + Ilyra + Torren + Nimera;
- Beat 9 — **Buried Collections / Dormant Card Research — Draft A, GUARDRAIL-FIRST AGENT-BRAIN PASS COMPLETE**;
- Beat 10 — **The Recent Reader / Hall of Seals — Draft A, GUARDRAIL-FIRST AGENT-BRAIN PASS COMPLETE**;
- Beat 11 — **NEXT LIVE TARGET — First Command Warden**;
- Beats 12–15 — pending sequential rehearsal-first passes;
- H01 — pending later cleanup pass with the two explicitly preserved Cyanis/Torren opening anchors;
- H03 — pending fully agent-driven Ilyra/Nimera scene discovery during its rehearsal pass.

Current Chapter-3 standalone files:
- `PRODUCTION/CHAPTER_03/BEAT_01_CAELORA_GATE_ARRIVAL_SPEC.json`
- `PRODUCTION/CHAPTER_03/BEAT_01_CAELORA_GATE_ARRIVAL_DRAFT_A.md`
- `PRODUCTION/CHAPTER_03/BEAT_02_ROYAL_AUDIENCE_CH2_REPORT_SPEC.json`
- `PRODUCTION/CHAPTER_03/BEAT_02_ROYAL_AUDIENCE_CH2_REPORT_DRAFT_A.md`
- `PRODUCTION/CHAPTER_03/BEAT_03_IMPOSSIBLE_ORDERS_SPEC.json`
- `PRODUCTION/CHAPTER_03/BEAT_03_IMPOSSIBLE_ORDERS_DRAFT_A.md`
- `PRODUCTION/CHAPTER_03/BEAT_04_SEAL_NOT_USED_SPEC.json`
- `PRODUCTION/CHAPTER_03/BEAT_04_SEAL_NOT_USED_DRAFT_A.md`
- `PRODUCTION/CHAPTER_03/BEAT_05_OLD_CITY_ACCESS_ARCHIVE_DESCENT_SPEC.json`
- `PRODUCTION/CHAPTER_03/BEAT_05_OLD_CITY_ACCESS_ARCHIVE_DESCENT_DRAFT_A.md`
- `PRODUCTION/CHAPTER_03/BEAT_06_SCHOLAR_IN_REDACTED_STACKS_SPEC.json`
- `PRODUCTION/CHAPTER_03/BEAT_06_SCHOLAR_IN_REDACTED_STACKS_DRAFT_A.md`
- `PRODUCTION/CHAPTER_03/BEAT_07_ANCIENT_BARRIER_FIRST_COOPERATION_SPEC.json`
- `PRODUCTION/CHAPTER_03/BEAT_07_ANCIENT_BARRIER_FIRST_COOPERATION_DRAFT_A.md`
- `PRODUCTION/CHAPTER_03/BEAT_08_ARCHIVE_SCRIBE_ENGINE_NIMERA_JOINS_SPEC.json`
- `PRODUCTION/CHAPTER_03/BEAT_08_ARCHIVE_SCRIBE_ENGINE_NIMERA_JOINS_DRAFT_A.md`
- `PRODUCTION/CHAPTER_03/BEAT_09_BURIED_COLLECTIONS_DORMANT_CARD_RESEARCH_SPEC.json`
- `PRODUCTION/CHAPTER_03/BEAT_09_BURIED_COLLECTIONS_DORMANT_CARD_RESEARCH_DRAFT_A.md`
- `PRODUCTION/CHAPTER_03/BEAT_10_RECENT_READER_HALL_OF_SEALS_SPEC.json`
- `PRODUCTION/CHAPTER_03/BEAT_10_RECENT_READER_HALL_OF_SEALS_DRAFT_A.md`

Chapter 3 uses the current consolidated 15-beat story authority in `docs/02_STORY/CHAPTERS/CHAPTER_03.md`.

## Exact line anchors outside completed current scenes

Current examples:
- Ch1 C04: `old slut` remains preserved in the current joke exchange.
- Ch3 H01:
  - Cyanis: `I bet you use that cape to sneak up on the goats you fuck.`
  - Torren: `You look like a walking dick in armor.`

These anchors do not lock the rest of their scenes.

## Source-cleanup rule

Once a chapter has a complete current rehearsal-first production manuscript, an older duplicate chapter transcript must not remain beside it as a competing `locked`, `line-complete`, or generic `working` authority. Keep current production material in `PRODUCTION/CHAPTER_##/`; rely on Git history for removed superseded copies.

No later chapter receives fabricated dialogue merely to make the folder look complete.
