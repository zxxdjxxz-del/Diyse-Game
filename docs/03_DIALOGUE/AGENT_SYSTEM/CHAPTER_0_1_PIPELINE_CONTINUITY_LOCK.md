# Diyse — Chapter 0–1 Dialogue Pipeline Continuity Lock

**Status:** LOCKED PRODUCTION WORKFLOW  
**Effective:** 2026-09-10  
**Domain:** dialogue generation / editing workflow  
**Scope:** Chapters 0–13 and all future story / Character-Life dialogue unless explicitly revised by the user.

## Core lock

> **The rehearsal-first Agent Brain system used to create the current completed Chapter 0 and Chapter 1 production dialogue is the mandatory dialogue-production method for Chapter 2 through Chapter 13 and all future Diyse dialogue.**

Do not revert later chapters to the older simplified dialogue-agent method, a generic single-pass cast-writing method, or direct production-script generation from canon constraints.

## Mandatory production sequence

1. **Scene / world state** — establish the playable situation, current continuity, physical/gameplay pressure, reveal boundaries, and who is present.
2. **Independent Person Agent Brain rehearsals** — each participating character responds from that character's current full brain profile rather than from an omniscient shared cast voice. A Person Agent completes the natural behavioral turn rather than automatically yielding after one sentence.
3. **Dialogue Editor** — aggressively cut, reconcile, and shape the rehearsal while preserving selective participation, interruptions, silence, pair-specific rhythm, disagreement, mundane behavior, natural floor-holding, sentence-length variation, and other human irregularity. `Cut aggressively` means remove repetition and weak material; it does **not** mean force one sentence per speaker turn.
4. **Invisible Canon / Knowledge Checker** — verify lore, chronology, reveal timing, personal knowledge boundaries, relationship state, gameplay legality, map/traversal legality, terminology, and current production constraints without making characters verbalize the firewall.
5. **Economical HD-2D staging / implementation pass** — translate the surviving dialogue into the established field, portrait, dialogue-box, battle, and traversal presentation without inventing unnecessary cinematic choreography. Dialogue-box pagination does not define when a conversational turn ends.

`REHEARSAL_FIRST_AUTHORING_LOCK.md`, `NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md`, `KNOWLEDGE_FIREWALL_INVISIBILITY_RULE.md`, `AUTHORITY_PACKET_COMPILER.md`, `SCENE_CONSTRUCTION_STACK.md`, and other current Agent System locks remain binding parts of this workflow.

## Natural-turn correction

The following interpretation is now explicit and mandatory:

> **Concision is a density trait, not a one-sentence limit. A character yields the floor because the interaction changes, not because the script reached a period.**

Character-brain language such as `concise`, `short practical question`, `conclusion first`, `shorter answers`, or `lower verbal density` must never be treated as a maximum sentence count.

A natural turn may be a fragment, one sentence, several connected sentences, an unfinished thought, or silence. If the UI needs multiple boxes for one turn, consecutive boxes from the same speaker are allowed and preferred over inventing an unnecessary reply.

Owning detailed rule:
- `NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md`

Chapters 0–3 require a retroactive rhythm audit under that lock before dialogue is treated as fully polished for implementation. Preserve strong lines and only repair artificial one-sentence ping-pong where it actually occurs.

## Agent Brain requirement

Every participating permanent-character agent must use the **current full character brain/profile** available at authoring time, including relevant:
- life history and lived experience;
- world and cultural knowledge;
- personal knowledge boundaries and provenance;
- relationship history and current pair/group state;
- memories and accumulated continuity;
- motives, wants, fears, habits, blind spots, and expertise boundaries;
- current physical/emotional/contextual state;
- individual speaking and conversational behavior.

The character brain shapes behavior. It does not authorize self-expository dialogue about the character sheet itself.

## Deployment/runtime distinction

Railway / Render character-agent services are deployment/runtime implementations of the same Agent Brain architecture/profile lineage. They are **not** the production-workflow authority by themselves.

The authoring authority is the current Agent Brain architecture and current brain data. Dialogue may be rehearsed through an available runtime/deployment or instantiated within the authoring workflow, but the required behavioral and knowledge model must remain the same.

## Chapter 0–1 precedent

The current Chapter 0 and Chapter 1 rehearsal-first production manuscripts are the reference implementation for this method:

- `../PRODUCTION/CHAPTER_00/CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- `../PRODUCTION/CHAPTER_01/CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`

Their production method, not every individual line or cadence artifact, is the locked precedent.

Later explicit workflow corrections—including the natural-turn/floor-holding lock—supersede any accidental rhythm pattern present in those manuscripts.

## Forward rule

> **New Ch.0–1 workflow = mandatory Ch.2–13 workflow, with all later explicit workflow corrections applied.**

A later chapter may require different characters, stakes, pacing, or scene types, but it must not silently change the dialogue-generation architecture.

Any future change to this pipeline requires an explicit user revision and a corresponding update to this lock and the dialogue master index.
