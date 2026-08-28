# Diyse — AI Engineering Rules

`AGENTS.md` is the root agent contract. This file expands the working method and must be interpreted through the latest canon.

## Authority order for implementation work

1. New explicit user instruction for the current task.
2. **Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.20 / Audit135** and any later explicit authority.
3. `docs/ACTIVE_CANON.md`.
4. The relevant current chapter operational file under `docs/chapters/`.
5. The latest controlling canon audit/overlay for the subsystem.
6. `docs/IMPLEMENTATION_STATUS.md`, `docs/PRESENTATION_RULES.md`, and relevant production records.
7. Compatible subsystem specifications and working models, interpreted through current overlays.
8. Existing production code and regression tests, interpreted through current authority.
9. Historical prototype/recovery material only when explicitly requested or explicitly inherited.

Do not use an older implementation, proof fixture, stale chapter number, retired region name, legacy identifier, or superseded numeric table to override newer authority.

## Current chapter-number rule

Chapter 10 — The Last Blank was inserted after Chapter 9.

Current late-game structure:
- **Chapter 10 — The Last Blank**.
- **Chapter 11 — Crown Engine / Calder / Custodian / Truth**.
- **Chapter 12 — The Reforged March**.
- **Chapter 13 — The Last Command**.

Historical translation:
- old Ch10 → current Ch11;
- old Ch11 → current Ch12;
- old Ch12 → current Ch13.

Never implement the old late-game folder meaning.

Read:
`docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`

Current operational files:
- `docs/chapters/chapter_10/CHAPTER_10_THE_LAST_BLANK_STORY_STRUCTURE_LOCK.md`
- `docs/chapters/chapter_11/CHAPTER_11_CURRENT_SCOPE.md`
- `docs/chapters/chapter_12/CHAPTER_12_REFORGED_MARCH_FORWARD_HUB_AND_CLEANUP_LOCK.md`
- `docs/chapters/chapter_13/CHAPTER_13_MACRO_STORY_STRUCTURE_LOCK.md`

## Current phase rule

- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapters 0–4 HD-2D Conversion Audit Pass 1 remains COMPLETE / APPROVED.
- Cross-chapter HD-2D consistency/cost consolidation remains PASS / GREEN.
- Current late-game macro story structure is chapter-correct through Audit113 and later overlays.
- Detailed scene production for Chapters 10–13 remains separate work unless a later scene pass explicitly locks it.
- Current class MP, CEXP, Mastery, player-level progression, mandatory EXP/CEXP allocation, named/story EXP+CEXP placement, and progression-dependent mandatory/Elite/Regional-Hunt/Major-Hunt raw-stat recertification are all closed under Audits123–135.
- Do not assume Chapter 5 is the universal “next task”; follow the user's current requested workstream.

## HD-2D authority

Diyse's active presentation target is **HD-2D**.

Older active `2.5D` and `3D` language is superseded. Historical proof documents may remain as provenance but must not drive current visual implementation.

Current production targets:
- ~80 px field characters;
- ~200–220 px battle characters;
- large high-resolution dialogue portraits;
- authored layered field environments;
- bounded cameras and restrained parallax;
- four active party members staggered left / enemies right / open center action lane;
- reusable battle-background families derived from field geography;
- exact visual masters control derivatives.

## Current world terminology

Use current-facing:
- **Black Host Territory**
- **The Westways**
- **The Greyspires**
- **Yahtrenhold**
- **The Blackspine**
- **Westguard**
- **Vhalmarch**
- **Vorathen**
- **The Veiled Citadel**

Do not restore `Blackstone` as the formal region label, `The Crownhold`, `Black Mountains`, `Westreach`, or `Yahtrens Stand` in authored current-facing content.

Stable technical identifiers may retain historical strings only until a reference-safe engineering migration is performed.

## Current point of no return

Starting Chapter 13 is deliberate but is **not** itself the irreversible point of no return.

The true irreversible threshold is:

**Last Shelter → Reactor Galleries**

Any runtime gating that permanently disables world return at Chapter-13 launch is stale and must not be implemented.

## New-authoring workflow

For new scene work:
- begin from current chapter macro authority;
- use the chapter-level process in `docs/SCENE_AUTHORING_STANDARD.md`;
- preserve knowledge firewalls, geography, roster state, approved causal structure, and locked outcomes;
- distinguish proposal text from locked text;
- only promote exact dialogue after explicit approval.

For Chapters 0–4, use exact source/Resource sets rather than reconstructing dialogue from summaries.

## No-invention policy

When implementation detail is missing, use a clearly labeled placeholder only when the milestone permits it, isolate it in data/configuration, document the assumption, and do not present it as canon.

Never invent permanent mechanics, dialogue, lore, characters, relationships, Card identities, Prime rules, story outcomes, chapter rewards, or progression numbers merely to unblock coding.

## Current system facts that override older proof docs

- Player level cap = **70**.
- Base class cap = **CL13**.
- Subclass cap = **CL13**.
- Exactly **24 Standard Cards** and **12 Prime Cards**.
- Standard Cards are unlimited-use.
- Current Faces: Might / Elements / Grace / **Acuity** / Change / Ruin.
- Current Acuity Story Prime = **Last Cartographer**.
- `Resource / Last Measure` is retired current-facing final-act terminology.
- No Prime had ever been successfully activated before the modern story.
- Sixfold event = **The Sixfold Volition**, not Sixfold Accord.
- No permanent character uses a Subclass before the Volition.
- **Synthesis is removed.**
- Class Ability MP certification is closed under Audit123.
- CL13 cumulative CEXP = **6,000**.
- Exactly 8 automatic Mastery Points: Lv5 / 10 / 15 / 20 / Sixfold Volition / 40 / 50 / 60.
- Normal route reaches approximately Ch12 Lv57 / Last Shelter Lv60 / ending Lv62.
- Status Resistance uses 0 / 5 / 10 / 15 general bands; explicit immunity remains separate.
- Barrier and Brace do not exist. No global Break/Stagger meter exists. Guard remains valid; Staggered is an ordinary harmful status.
- Hunt tuning is fixed authored tuning; recommended level is a preparedness target, not an access gate.

## Proven-architecture protection

Do not casually replace accepted behavior:
- authored dialogue with no player response system;
- stable-ID Resource-backed dialogue with portrait-registry indirection and structural validation;
- discrete round-based combat;
- deterministic automatic hostile retargeting;
- unlimited data-driven Standard Cards;
- compatible Prime summon presentation/runtime architecture;
- versioned plain-data persistence separate from scene nodes;
- Android as a first-class build/test target;
- random encounters as normal hostile-exploration grammar where approved.

Do not protect retired presentation assumptions merely because they existed in old proof files.

## HD-2D cost discipline

Prefer reusable authored composition over simulation.

Use:
- regional environment kits;
- small battle-background families;
- reusable body-animation families;
- portrait acting;
- prop/environment state swaps;
- selective background loops;
- audio to imply offscreen scale;
- modular Face/Card/Prime and elemental VFX;
- one evolving Cresthaven master hub;
- one common transition architecture;
- reusable nonlethal battle-resolution patterns.

Avoid by default:
- fully modeled cities;
- giant seamless dungeons solely to imply scale;
- free-camera field navigation;
- fluid/crowd/destruction/chain/cloth/hair simulation;
- one bespoke battle arena per formation;
- one bespoke actor animation per Ability;
- unnecessary full boss bodies for same-body/same-HP escalations.

## Boss/form discipline

Before implementing a boss transition, classify it as:

1. same-body / same-HP escalation;
2. genuine new form with fresh HP where explicitly locked;
3. Prime-scale manifestation using the reusable Prime pipeline.

Do not add extra forms, health bars, adds, threshold systems, or bespoke meters that canon does not require.

Current hard examples:
- Registry Warden: one HP bar, no adds, no transformation.
- Regulation Crucible → The Seventh Reaction: genuine fresh form; no third form.
- Crownless Siege Marshal → Crownless War Engine: genuine fresh form; Prime refreshes at War Engine.
- Concordance Guardian: Six Faces → Open Concordance on one continuous HP bar.
- Worldscar Leviathan: Prismatic Confluence on one continuous HP bar.
- Final Archive Arbiter: one continuous HP bar.
- The Unfinished World: WORLDFRAME → WORLDHEART EXPOSED → FINAL CONSTRUCTION on one continuous **78,000 HP** bar.
- Vaelkor: two genuine forms.
- Last Weapon Archon: one HP bar.
- Reconstituted Entity → The Last Command: exactly two genuine full-health final-boss forms, no third form.

## Dialogue workflow

Production dialogue uses stable-ID `DiyseDialogueSceneDefinition` Resources. Never embed canon scene text or final portrait paths in generic engine code.

For completed Chapters 0–4:
- start from exact Markdown source and validated Resources;
- preserve approved wording, protected lines, scene purpose, character voice, geography, knowledge state, and outcomes;
- use bounded corrections for later terminology/canon overlays;
- rerun source-parity/continuity validators after changes.

A missing map, trigger, portrait, battle background, or presentation consumer is not evidence that dialogue/canon is missing.

## Legacy timing after chapter insertion

Synthesis is removed and must not be used as a gate.

Current timing:
- mandatory reciprocal-pair resolution beats = **late Chapter 12**;
- secured Cresthaven native-Legacy completion/release remains available through the **Chapter-13 pre-Last-Shelter returnable period**;
- final cutoff = **Last Shelter → Reactor Galleries**.

Historical Synthesis-era timing files are provenance only where they conflict with Audit121+.

## Progression / reward state — CLOSED NUMERICAL SPINE

The old post-insertion progression timing hold is superseded by Audits123–128.

Current normal-route anchors:
- Ch1 5
- Ch2 9
- Ch3 13
- Ch4 17
- Ch5 22
- Ch6 27
- Ch7 32
- Ch8 37
- Ch9 42
- Ch10 47
- Ch11 52
- Ch12 57
- Last Shelter 60
- End Ch13 62
- cap 70

Current progression authority:
- Audit123 — Ability MP certification, CL13 CEXP curve, Mastery schedule, player-level spine;
- Audit124 — optional EXP / Lv70 cap proof;
- Audit125 — formation EXP/CEXP allocation;
- Audits126–128 — exact mandatory named/story EXP+CEXP placement.

Do not use the historical `POST_INSERTION_PROGRESSION_TIMING_HOLD_2026-08-23.md` as an active numerical hold.

## Raw-stat state — CLOSED THROUGH MAJOR HUNTS

- mandatory named/story bodies — Audits129–132;
- numbered-chapter optional Elites — Audit133;
- 11 Regional Hunts — Audit134;
- 6 Major Hunts — Audit135.

Current challenge hierarchy:

> **Ordinary < Elite < mandatory story boss < Regional Hunt < Major Hunt**

Do not add dynamic Hunt scaling. Do not fabricate unresolved support-object/component HP to make tables look complete.

## Current implementation frontier

The current concrete implementation/content frontier is:

**Kessara Relic-copy service implementation**

Preserve the closed rule:
- Relic already obtained;
- one matching copy component required;
- maximum one forged duplicate per Relic;
- maximum quantity = 2;
- duplicate mechanically identical;
- Legacies cannot be copied.

Remaining work may determine fee, menu timing, and original-vs-copy UI presentation without reopening the core rule.

## Engineering behavior

- Fresh Godot/GDScript implementation; do not copy/port historical prototype code unless explicitly authorized for named reuse.
- Dialogue is one authored continuity; no response wheels, morality/affinity responses, or romance routes.
- Implement one bounded milestone at a time.
- Preserve deterministic behavior where combat rules require it.
- Add deterministic validation for pure logic/content contracts where practical.
- Keep exploration, dialogue, combat, save/state, UI, and content loading separable.
- Prefer simple readable GDScript over clever abstractions.
- Keep authored content data-driven where practical.
- Do not change canon/specification documents as accidental side effects of code work.
- After any implementation change, run the smallest relevant deterministic validator first, then broader regression as needed.

## Historical audit interpretation

Historical Audit84/Audit89 remain provenance and must not be used with their original chapter numbers as current implementation guidance.

Use:
- `docs/canon/AUDIT89_CURRENT_REINDEX_AND_TERMINOLOGY_OVERLAY_2026-08-23.md`
- `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`

Historical Audit106 item identities/counts remain compatible, but its late chapter labels are corrected by:
`docs/canon/AUDIT106_POST_INSERTION_CHAPTER_LABEL_OVERLAY_2026-08-23.md`
