# Diyse — Dialogue Master Index

**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicit user corrections/current domain migrations.  
**Dialogue production root:** `docs/03_DIALOGUE/PRODUCTION/`

## Dialogue Engine hard rules

Current production dialogue uses the rehearsal-first Agent Brain pipeline:

> **scene/world state → independent Person Agent Brain rehearsals → Dialogue Editor → invisible Canon/Knowledge Checker → economical HD-2D staging/implementation**

Owning pipeline lock:
- `AGENT_SYSTEM/CHAPTER_0_1_PIPELINE_CONTINUITY_LOCK.md`

Story-beat guardrail lock:
- `AGENT_SYSTEM/STORY_BEAT_AS_GUARDRAIL_LOCK.md`

Story structure controls situation, hard outcomes, reveal boundaries, and gameplay state. It does **not** pre-write speaker order, required jokes, motivation speeches, or conversational checkpoints.

Natural-turn / floor-holding lock:
- `AGENT_SYSTEM/NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md`

Hard rhythm rule:
> **Concision is not a one-sentence limit. A character yields the floor because the interaction changes, not because the script reached a period.**

A conversational turn may be a fragment, one sentence, several connected sentences, an interrupted thought, or silence. Dialogue-box pagination is a presentation unit and does not define the end of a speaker turn.

The recurring one-sentence ping-pong artifact is tracked in:
- `CHAPTER_0_3_NATURAL_TURN_RHYTHM_AUDIT_TRACKER.md`

Walking-dialogue lock:
- `AGENT_SYSTEM/WALKING_DIALOGUE_LOCK.md`

Ordinary traversal does not receive walking dialogue unless someone is genuinely guiding the route.

---

# Canonical Chapter Dialogue Locations — Chapters 0–3

| Chapter | Current status | Chapter-level dialogue authority |
|---|---|---|
| Ch0 | **COMPLETE CURRENT WORKING PRODUCTION; NATURAL-TURN RHYTHM AUDIT COMPLETE** — P01–P07 + optional C01 | `PRODUCTION/CHAPTER_00/CHAPTER_00_DIALOGUE_AUTHORITY_INDEX.md` → `CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` |
| Ch1 | **COMPLETE CURRENT WORKING PRODUCTION; NATURAL-TURN RHYTHM AUDIT NEXT/PENDING** — Beats 1–15 + C03/C04/C05 | `PRODUCTION/CHAPTER_01/CHAPTER_01_DIALOGUE_AUTHORITY_INDEX.md` → `CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` |
| Ch2 | **COMPLETE CURRENT WORKING MAINLINE PRODUCTION; NATURAL-TURN RHYTHM AUDIT PENDING** — Beats 1–16; C06 current | `PRODUCTION/CHAPTER_02/CHAPTER_02_DIALOGUE_AUTHORITY_INDEX.md` |
| Ch3 | **COMPLETE CURRENT WORKING PRODUCTION; NATURAL-TURN RHYTHM AUDIT PENDING** — Beats 1–15 + H01/H03; prior closing integration audit complete | `PRODUCTION/CHAPTER_03/CHAPTER_03_DIALOGUE_AUTHORITY_INDEX.md` → `CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` |

These four chapter folders are the correct live production locations. Do not recover dialogue from old chats, historical files, removed `LINE_COMPLETE` sets, or superseded manuscripts when a current chapter authority/index points elsewhere.

---

# Chapter 0

Folder:
- `PRODUCTION/CHAPTER_00/`

Primary chapter file:
- `CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`

Authority index:
- `CHAPTER_00_DIALOGUE_AUTHORITY_INDEX.md`

Current sequence:
> **P01 → P02 → P03 → P04 → P05 → P06 → P07 → optional C01 `Six Minutes` → explicit departure to Brackenwall**

Key continuity:
- Cyanis begins alone;
- Ilyra enters during P04 and independently joins the defense;
- first incomplete Card flare occurs in P04 and ends before P05;
- P05 is the concealed Ruin Vanguard Pursuer;
- P06 is the combined Riftmaw + Convoy War-Sorcerer boss;
- the recovery casing breaks during P06;
- the Card survives intact and is carried directly afterward;
- P07 closes through survivor recovery rather than celebration.

Current polish state:
- **natural-turn / floor-holding rhythm audit complete**;
- P01–P02 were audited and intentionally preserved because crisis shorthand is appropriate;
- P03–P07 received selective floor-time corrections;
- C01 received the strongest quiet-scene rhythm correction;
- chapter manuscript and standalone authorities are synchronized.

---

# Chapter 1

Folder:
- `PRODUCTION/CHAPTER_01/`

Primary chapter file:
- `CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`

Authority index:
- `CHAPTER_01_DIALOGUE_AUTHORITY_INDEX.md`

Current coverage:
- Beats 1–15 mainline;
- C03 — `Torren's Version of Dinner`;
- C04 — `What the Map Says`;
- C05 — `Not Professionally`.

Standalone scene drafts/specs remain in the same folder as detailed scene-level production authority.

Obsolete Chapter-1 `LINE_COMPLETE` material is not current authority.

Current polish state:
- **natural-turn / floor-holding rhythm audit is the next live target.**

---

# Chapter 2

Folder:
- `PRODUCTION/CHAPTER_02/`

Authority index:
- `CHAPTER_02_DIALOGUE_AUTHORITY_INDEX.md`

Current state:
- all sixteen mainline beats have current rehearsal-first working dialogue;
- Beats 1–11 are contained in `CHAPTER_02_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`;
- Beats 12–16 are current standalone rehearsal-first working dialogue files in the same Chapter-2 folder;
- C06 — `Still Burns` — is current cleanup Character-Life dialogue;
- the older manuscript header/storage split does **not** mean Beats 12–16 are missing.

Chapter-2 mainline dialogue production is complete. It is in revision/playtest territory, not pending initial Dialogue Engine production.

Current polish state:
- natural-turn / floor-holding rhythm audit pending.

---

# Chapter 3

Folder:
- `PRODUCTION/CHAPTER_03/`

Authority index:
- `CHAPTER_03_DIALOGUE_AUTHORITY_INDEX.md`

Complete readable chapter manuscript:
- `CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`

Closing integration audit:
- `CHAPTER_03_DIALOGUE_CLOSING_INTEGRATION_AUDIT_2026-09-12.md`

Current state:
- Beats 1–15 have current working dialogue;
- H01 — `Nimera Takes Over a Table` — current working dialogue complete;
- H03 — `Ilyra and Nimera` — current working dialogue complete;
- the chapter-wide closing integration audit is complete;
- the cumulative manuscript has been rebuilt from the post-audit scene authorities and contains Beats 1–15 + H01 + H03;
- standalone Beat / Character-Life files remain the detailed scene-level authority if a later targeted revision has not yet been reassembled into the manuscript.

Closing-audit changes included:
- Beat 4 — fresh guardrail-first Agent-Brain rerun to remove remaining checklist-driven conversation;
- Beats 6/7 — minor integration trims;
- Beat 11 — Warden/Card timing remains strongly meaningful but no longer reads as proven causation;
- Beat 12 — repeated mark-vs-authority-copy explanation reduced to one clean distinction;
- Beat 13 — debrief trimmed so it reports consequences instead of re-explaining Beat 12;
- H03 — repeated Chapter-2 comedy cadence removed;
- full manuscript rebuilt afterward.

Current Beat-11 lock:
> Warden assessment → battle → `PREVIOUS ERROR` → `LAST SENTINEL CONFIRMED` → Warden inert → Card stable deep Ruby.

Current Beat-12 lock:
- visible Crest copying is distinct from reproducing genuine royal magical authority;
- no new map/route relief is introduced.

Current Beat-13/14/15 continuity:
- Mirena asks the party to investigate directly with her;
- Cresthaven is identified from the existing Chapter-2 Ancient map evidence;
- the party rests in Caelora before departure;
- Cresthaven becomes the working base;
- Mirena and Maevra return to Caelora after the handoff;
- Chapter-3 cleanup becomes active.

Chapter 3 is not missing any initial dialogue production, but still requires the natural-turn / floor-holding rhythm audit before dialogue is treated as fully polished for implementation.

---

# Later Chapters

| Chapter | Dialogue status |
|---|---|
| Ch4 | pending current Dialogue Engine production under current restructured story authority **and the natural-turn/floor-holding lock from the first rehearsal** |
| Ch5 | beat rewrite required before dialogue generation |
| Ch6 | macro/beat authority; dialogue pending |
| Ch7 | macro authority; dialogue pending |
| Ch8 | macro authority; dialogue pending |
| Ch9 | macro/beat authority; dialogue pending |
| Ch10 | detailed story architecture; dialogue pending |
| Ch11 | macro authority; dialogue pending |
| Ch12 | macro authority; dialogue pending |
| Ch13 | macro authority; dialogue pending |

All later chapter dialogue uses the same locked rehearsal-first Agent Brain pipeline plus all later explicit workflow corrections, including `NATURAL_TURN_LENGTH_AND_FLOOR_HOLDING_LOCK.md`, unless explicitly revised by the user.

---

# Exact dialogue anchors

Current examples:
- Ch1 C04: `old slut` remains preserved in the current joke exchange.
- Ch3 H01:
  - Cyanis: `I bet you use that cape to sneak up on the goats you fuck.`
  - Torren: `You look like a walking dick in armor.`

Those exact anchors remain protected during the rhythm audit. A cadence correction around an exact anchor must not alter the locked wording itself.

---

# Source-cleanup rule

Current production dialogue belongs in:
> `docs/03_DIALOGUE/PRODUCTION/CHAPTER_##/`

Each chapter's dialogue authority index/manuscript tells production where the current exact dialogue lives.

When a scene receives a later targeted revision, update its standalone current production file first. Then deliberately synchronize/reassemble any cumulative manuscript that contains it rather than leaving ambiguous competing versions.

Use Git history for superseded copies. Do not leave older duplicate transcripts presented as competing current authority.
