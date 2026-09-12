# Diyse — Dialogue Master Index

**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicit user corrections/current domain migrations.  
**Dialogue production root:** `docs/03_DIALOGUE/PRODUCTION/`

## Dialogue Engine hard rules

Current production dialogue uses the rehearsal-first Agent Brain pipeline:

> **scene/world state → independent Person Agent Brain rehearsals → Dialogue Editor → invisible Canon/Knowledge Checker → spoken-dialogue vs narration audit → economical HD-2D staging/implementation**

Owning pipeline lock:
- `AGENT_SYSTEM/CHAPTER_0_1_PIPELINE_CONTINUITY_LOCK.md`

Story-beat guardrail lock:
- `AGENT_SYSTEM/STORY_BEAT_AS_GUARDRAIL_LOCK.md`

Natural-turn / floor-holding lock:
- `AGENT_SYSTEM/NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md`

Spoken-dialogue vs narration lock:
- `AGENT_SYSTEM/SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md`

Character-Life numbering lock:
- `PRODUCTION/CHARACTER_LIFE_NUMBERING_LOCK.md`

Hard rhythm rule:
> **Concision is not a one-sentence limit. A character yields the floor because the interaction changes, not because the script reached a period.**

Hard spoken-dialogue rule:
> **The environment shows. Evidence owners interpret. Authority figures decide. Characters react. Nobody recites the scene back to the player.**

A conversational turn may be a fragment, one sentence, several connected sentences, an interrupted thought, or silence. Dialogue-box pagination is a presentation unit and does not define the end of a speaker turn.

New-listener briefings must be compressed to what the listener actually needs; the listener should pull further detail through character-driven questions rather than causing the previous scene to be replayed for the player.

Retroactive rhythm audit tracker:
- `CHAPTER_0_3_NATURAL_TURN_RHYTHM_AUDIT_TRACKER.md`

**Retroactive Chapters 0–3 natural-turn rhythm audit status: COMPLETE.**  
**Retroactive Chapters 0–3 spoken-dialogue / narration audit status: COMPLETE.**

Walking-dialogue lock:
- `AGENT_SYSTEM/WALKING_DIALOGUE_LOCK.md`

Ordinary traversal does not receive walking dialogue unless someone is genuinely guiding the route.

---

# Canonical Character-Life Sequence — Current Through Chapter 3

> **C01 → C02 → C03 → C04 → C05 → C06 → C07, with no live gaps.**

- **C01 — Six Minutes** — Chapter 0
- **C02 — Torren's Version of Dinner** — Chapter 1
- **C03 — What the Map Says** — Chapter 1
- **C04 — Not Professionally** — Chapter 1
- **C05 — Still Burns** — Chapter 2
- **C06 — Nimera Takes Over a Table** — Chapter 3
- **C07 — Ilyra and Nimera** — Chapter 3

Retired/superseded development IDs do not reserve numbers. Some atomic filenames still carry legacy source prefixes until they and their synchronized manuscripts are regenerated together; `PRODUCTION/CHARACTER_LIFE_NUMBERING_LOCK.md` controls canonical live IDs.

---

# Canonical Chapter Dialogue Locations — Chapters 0–3

| Chapter | Current status | Chapter-level dialogue authority |
|---|---|---|
| Ch0 | **COMPLETE CURRENT WORKING PRODUCTION; NATURAL-TURN + SPOKEN-VS-NARRATION AUDITS COMPLETE** — P01–P07 + optional C01; atomic files current, combined read-through stale for revised scenes | `PRODUCTION/CHAPTER_00/CHAPTER_00_DIALOGUE_AUTHORITY_INDEX.md` |
| Ch1 | **COMPLETE CURRENT WORKING PRODUCTION; NATURAL-TURN + SPOKEN-VS-NARRATION AUDITS COMPLETE** — Beats 1–15 + C02/C03/C04; atomic files current, combined read-through stale where flagged | `PRODUCTION/CHAPTER_01/CHAPTER_01_DIALOGUE_AUTHORITY_INDEX.md` |
| Ch2 | **COMPLETE CURRENT WORKING PRODUCTION; NATURAL-TURN + SPOKEN-VS-NARRATION AUDITS COMPLETE** — Beats 1–16 + C05; atomic files current, combined read-through stale where flagged | `PRODUCTION/CHAPTER_02/CHAPTER_02_DIALOGUE_AUTHORITY_INDEX.md` |
| Ch3 | **COMPLETE CURRENT WORKING PRODUCTION; CLOSING INTEGRATION + NATURAL-TURN + SPOKEN-VS-NARRATION AUDITS COMPLETE** — Beats 1–15 + C06/C07; atomic files current, combined read-through stale where flagged | `PRODUCTION/CHAPTER_03/CHAPTER_03_DIALOGUE_AUTHORITY_INDEX.md` |

These four chapter folders are the correct live production locations. Where a combined manuscript's embedded SHA differs from the current atomic source, the atomic source is the exact wording authority.

---

# Chapter 0

Folder:
- `PRODUCTION/CHAPTER_00/`

Authority index:
- `CHAPTER_00_DIALOGUE_AUTHORITY_INDEX.md`

Current sequence:
> **P01 → P02 → P03 → P04 → P05 → P06 → P07 → optional C01 `Six Minutes` → explicit departure to Brackenwall**

Natural-turn audit: **COMPLETE.**  
Spoken-dialogue / narration audit: **COMPLETE.**

Spoken-vs-narration material revisions:
- **P03** — the north-cut suspicion is not re-explained to the same officer; Cyanis answers what changed operationally.
- **P07** — Ilyra states the decision to stay once and supplies the reason only when Cyanis challenges it.

Audited and intentionally retained:
- P01, P02, P04–P06, C01.

Combined read-through:
- `CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — **stale for P03/P07 after this audit.**

---

# Chapter 1

Folder:
- `PRODUCTION/CHAPTER_01/`

Authority index:
- `CHAPTER_01_DIALOGUE_AUTHORITY_INDEX.md`

Canonical Character-Life scenes:
- **C02 — Torren's Version of Dinner**;
- **C03 — What the Map Says**;
- **C04 — Not Professionally**.

Natural-turn audit: **COMPLETE.**  
Spoken-dialogue / narration audit: **COMPLETE.**

Spoken-vs-narration material revisions:
- Beats **1, 3, 5, 6, 7, 10, 11**.

Key result:
- new-listener Card briefings are consequence-first rather than replayed chronologically;
- Hollow Watch occupation/excavation staging carries information the environment can show;
- the six-channel relief and mural stay visual-first instead of being read aloud as checklists;
- the Hollow Watch resolution reports what Greenhollow needs, not the chapter back to the people who lived it.

Audited and intentionally retained:
- Beats 2, 4, 8–9, 12–15 and canonical C02/C03/C04.

Protected **C03** anchor remains exact:
- Cyanis: `Old slut?`
- Torren: `Bitch.`

Known Beat-14 Face-list wording remains source-controlled and is not silently changed by this dialogue audit.

Combined read-through:
- `CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — **requires resynchronization after atomic dialogue and prior numbering revisions.**

---

# Chapter 2

Folder:
- `PRODUCTION/CHAPTER_02/`

Authority index:
- `CHAPTER_02_DIALOGUE_AUTHORITY_INDEX.md`

Current state:
- all sixteen mainline beats have one standalone exact current dialogue authority;
- **C05 — Still Burns** is current cleanup Character-Life dialogue.

Natural-turn audit: **COMPLETE.**  
Spoken-dialogue / narration audit: **COMPLETE.**

Spoken-vs-narration material revisions:
- Beats **5, 6, 10, 13, 16**.

Key result:
- Archive staging carries visible organization/forcing evidence while Ilyra and Torren supply only distinct interpretation;
- prisoner testimony is not paraphrased three times after the witnesses establish the facts;
- Rhazek no longer narrates the player's dungeon progress back to the party;
- Dunmere's final debrief is consequence-first rather than a beat-by-beat Chapter-2 recap;
- the elder's thematic summary is reduced to the character-appropriate `Both matter.`

Audited and intentionally retained:
- Beats 1–4, 7–9, 11–12, 14–15 and C05.

Core outcomes remain unchanged: current prisoners rescued, Rhazek loses the Old Bastion locally but survives a credible withdrawal, earlier transferred captives remain unresolved, Greenhollow ↔ Dunmere travel reopens, and Chapter 3 begins only through explicit player confirmation.

Combined read-through:
- `CHAPTER_02_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — **requires resynchronization after atomic dialogue and prior numbering revisions.**

---

# Chapter 3

Folder:
- `PRODUCTION/CHAPTER_03/`

Authority index:
- `CHAPTER_03_DIALOGUE_AUTHORITY_INDEX.md`

Combined read-through:
- `CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` — **currently stale for revised atomic scenes identified by the authority index.**

Prior closing integration audit:
- `CHAPTER_03_DIALOGUE_CLOSING_INTEGRATION_AUDIT_2026-09-12.md`

Current state:
- Beats 1–15 current in standalone atomic authority;
- **C06 — Nimera Takes Over a Table** current;
- **C07 — Ilyra and Nimera** current;
- closing integration audit complete;
- natural-turn / floor-holding rhythm audit complete;
- spoken-dialogue / narration audit complete.

Spoken-vs-narration material revisions:
- Beats 2, 3, 4, 6, 9, 10, 12, 13, 15.

Key result:
- Lysara tests certainty, judges, sets boundaries, and orders rather than repeating information already established;
- Mirena converts evidence into investigation choices rather than narrating clue stacks;
- visible evidence progression remains in staging when dialogue would only repeat it;
- Nimera retains real evidentiary explanations when only she can responsibly establish the distinction;
- repeated new-listener briefings are compressed rather than replayed chronologically.

Protected **C06** exact anchors:
- Cyanis: `I bet you use that cape to sneak up on the goats you fuck.`
- Torren: `You look like a walking dick in armor.`

Beat 11 exact Warden messages remain:
- `PREVIOUS ERROR`
- `LAST SENTINEL CONFIRMED`

---

# Later Chapters

| Chapter | Dialogue status |
|---|---|
| Ch4 | pending current Dialogue Engine production under current restructured story authority **with natural-turn/floor-holding and spoken-vs-narration rules active from the first rehearsal** |
| Ch5 | beat rewrite required before dialogue generation |
| Ch6 | macro/beat authority; dialogue pending |
| Ch7 | macro authority; dialogue pending |
| Ch8 | macro authority; dialogue pending |
| Ch9 | macro/beat authority; dialogue pending |
| Ch10 | detailed story architecture; dialogue pending |
| Ch11 | macro authority; dialogue pending |
| Ch12 | macro authority; dialogue pending |
| Ch13 | macro authority; dialogue pending |

All later chapter dialogue uses the locked rehearsal-first Agent Brain pipeline plus all later workflow corrections, including `NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md` and `SPOKEN_DIALOGUE_VS_NARRATION_LOCK.md` from the first production pass onward.

---

# Source-cleanup rule

Current production dialogue belongs in:
> `docs/03_DIALOGUE/PRODUCTION/CHAPTER_##/`

Each chapter's authority index / assembly tells production where the exact current dialogue lives.

When a scene receives a targeted revision, update its standalone current production file first. Do not retain an unsynchronized duplicate transcript as competing live authority; either deliberately reassemble it or keep the chapter-level file as an explicit assembly/status map.

For Character-Life, use the canonical ID from `PRODUCTION/CHARACTER_LIFE_NUMBERING_LOCK.md`. Legacy file prefixes are implementation provenance only and must not create holes in the live numbering sequence.

Use Git history for superseded copies.
