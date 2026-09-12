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

Walking-dialogue lock:
- `AGENT_SYSTEM/WALKING_DIALOGUE_LOCK.md`

Ordinary traversal does not receive walking dialogue unless someone is genuinely guiding the route.

---

# Canonical Chapter Dialogue Locations — Chapters 0–3

| Chapter | Current status | Chapter-level dialogue authority |
|---|---|---|
| Ch0 | **COMPLETE CURRENT WORKING PRODUCTION** — P01–P07 + optional C01 | `PRODUCTION/CHAPTER_00/CHAPTER_00_DIALOGUE_AUTHORITY_INDEX.md` → `CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` |
| Ch1 | **COMPLETE CURRENT WORKING PRODUCTION** — Beats 1–15 + C03/C04/C05 | `PRODUCTION/CHAPTER_01/CHAPTER_01_DIALOGUE_AUTHORITY_INDEX.md` → `CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` |
| Ch2 | **COMPLETE CURRENT WORKING MAINLINE PRODUCTION** — Beats 1–16; C06 current | `PRODUCTION/CHAPTER_02/CHAPTER_02_DIALOGUE_AUTHORITY_INDEX.md` |
| Ch3 | **MAINLINE BEATS 1–15 COMPLETE CURRENT WORKING PRODUCTION**; cleanup H01/H03 pending dialogue pass | `PRODUCTION/CHAPTER_03/CHAPTER_03_DIALOGUE_AUTHORITY_INDEX.md` |

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

---

# Chapter 3

Folder:
- `PRODUCTION/CHAPTER_03/`

Authority index:
- `CHAPTER_03_DIALOGUE_AUTHORITY_INDEX.md`

Current state:
- Beats 1–15 have current working dialogue;
- Beats 6–8 were rerun after the checkpoint-driven scripting correction;
- Beats 9–15 were authored from the start under `STORY_BEAT_AS_GUARDRAIL_LOCK.md`;
- Beat 8 permanently recruits Nimera;
- Beat 15 establishes Cresthaven as the operational headquarters and opens cleanup;
- H01 and H03 remain pending cleanup dialogue passes.

Important storage note:
- `CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md` is currently only a partial assembled reading copy through Beat 5;
- it is **not** the authority for deciding whether Beats 6–15 exist;
- the exact current mainline dialogue for Beats 1–15 is mapped in `CHAPTER_03_DIALOGUE_AUTHORITY_INDEX.md` to the standalone Beat files.

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

---

# Later Chapters

| Chapter | Dialogue status |
|---|---|
| Ch4 | pending current Dialogue Engine production under current restructured story authority |
| Ch5 | beat rewrite required before dialogue generation |
| Ch6 | macro/beat authority; dialogue pending |
| Ch7 | macro authority; dialogue pending |
| Ch8 | macro authority; dialogue pending |
| Ch9 | macro/beat authority; dialogue pending |
| Ch10 | detailed story architecture; dialogue pending |
| Ch11 | macro authority; dialogue pending |
| Ch12 | macro authority; dialogue pending |
| Ch13 | macro authority; dialogue pending |

All later chapter dialogue uses the same locked rehearsal-first Agent Brain pipeline unless explicitly revised by the user.

---

# Exact dialogue anchors outside completed current scenes

Current examples:
- Ch1 C04: `old slut` remains preserved in the current joke exchange.
- Ch3 H01:
  - Cyanis: `I bet you use that cape to sneak up on the goats you fuck.`
  - Torren: `You look like a walking dick in armor.`

Those anchors do not lock the rest of their scenes.

---

# Source-cleanup rule

Current production dialogue belongs in:
> `docs/03_DIALOGUE/PRODUCTION/CHAPTER_##/`

Each chapter's dialogue authority index/manuscript tells production where the current exact dialogue lives.

When an assembled chapter manuscript is intentionally incomplete but current standalone scenes exist, the chapter authority index must explicitly map those scenes rather than allowing the partial manuscript to imply missing dialogue.

Use Git history for superseded copies. Do not leave older duplicate transcripts presented as competing current authority.
