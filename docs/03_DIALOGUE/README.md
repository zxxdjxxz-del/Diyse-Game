# 03_DIALOGUE
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicit user corrections/current domain migrations.  
**Repository source checkpoint used for historical exact-dialogue extraction:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  

This is the canonical home for **spoken dialogue and dialogue-scene authoring**.

## Current Dialogue Engine authority
Story function, scene order, required events, knowledge, recruitment, reveal timing, mandatory outcomes, and canon-safe staging requirements live in `02_STORY`. Combat mechanics live in `05_BATTLE_SYSTEM` / `09_ENEMIES_AND_ENCOUNTERS`; Card mechanics live in `07_CARDS`; progression lives in `10_PROGRESSION_AND_EXP`.

Dialogue Engine architecture:
> `AGENT_SYSTEM/README.md`

Unified dialogue / character / map / gameplay / HD-2D scene-construction stack:
> `AGENT_SYSTEM/SCENE_CONSTRUCTION_STACK.md`

Dialogue-facing map/traversal interface:
> `../13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`

### Full-stack authoring rule
Dialogue is never authored as isolated prose and fitted into the game afterward.

Every current scene must be built with the simultaneous inputs that are relevant to that scene:
- story/canon/reveal state;
- persistent character brains;
- relationship progression and personal memory;
- mature-adult naturalism;
- cinematic subtext and selective participation;
- anime expressiveness and tonal elasticity;
- comedy timing when appropriate;
- lived-world and lived-economy context;
- actual location/sub-area/cell and visible environment;
- recent combat/traversal pressure and recovery;
- dialogue-safe traversal rules;
- current HD-2D/B00 staging grammar and production cost;
- dialogue UI/runtime capabilities.

Historical shorthand remains useful:

> **Talk like people. React like anime characters. Time jokes like a comedy. Structure important scenes like a great RPG. Remember they are living through a war. And occasionally let them argue about absolutely nothing.**

That sentence is a mnemonic for the full craft study, not a replacement for it.

### GLOBAL ALL-DIALOGUE REGENERATION RULE — LOCKED
**Every spoken dialogue scene in Diyse is to be written / rewritten by the new Diyse Dialogue Engine.** This is not limited to Character-Life material. It applies to:
- mandatory story scenes (`S##` and later equivalents);
- Character-Life / camp / hub-life scenes (`C##`, `H##`, and later equivalents);
- boss-intro / post-boss spoken material;
- travel dialogue and party exchanges;
- hub / investigation / recruitment conversations;
- any other authored spoken scene across Chapters 0–13.

Historical line-complete files are **reference material, not current final spoken-dialogue authority**, even when they carry historical labels such as `APPROVED / LOCKED`, `closed`, `line-complete`, or similar.

For all dialogue generation:
- the Dialogue Engine writes the current scene fresh using active character-agent voices, relationship state, chapter state, participants, location, canon, reveal timing, and knowledge firewall;
- the Director also receives the actual map/traversal/gameplay context so a scene's length and form fit what the player is doing;
- current HD-2D staging and production constraints are considered during writing, not retrofitted afterward;
- historical transcripts may inform scene purpose, relationship function, participant chemistry, staging ideas, joke structures, performance ideas, continuity clues, and voice/tone examples where compatible;
- historical wording is **not automatically preserved, paraphrased, or reused** simply because it was once accepted;
- current story authority controls what happens, in what order, who is present, what each character knows, what must be revealed, and what must remain unknown;
- retired story structures, obsolete party states, stale locations, retired terminology, obsolete knowledge, and superseded plot causality must never return through historical transcript reuse;
- this global rule supersedes older dialogue notes that distinguish between `reopened` and `not reopened` scenes or imply that mandatory-story wording may remain exact by default.

### Explicit exact-line anchors
The only historical or previously authored wording that must survive regeneration verbatim is wording the user has **explicitly selected / locked as an exact line or joke anchor**.

An explicit line anchor constrains that line only unless the user separately locks surrounding staging or dialogue. The Dialogue Engine remains free to regenerate the rest of the scene around it.

Current examples:
- Ch1 C04: `old slut` remains an exact joke anchor if that exchange survives regeneration.
- Ch3 H01:
  - Cyanis: `I bet you use that cape to sneak up on the goats you fuck.`
  - Torren: `You look like a walking dick in armor.`

Those anchors do not lock the surrounding dialogue.

## Current status
- **Chapter 0:** lean story beats are current structural authority; **all mandatory and Character-Life dialogue is regenerated by the Dialogue Engine** from those beats and current character/canon state.
- **Chapters 1–3:** current lean story structures are the authority; **all spoken dialogue is regenerated by the Dialogue Engine**, with historical files used only as compatible reference.
- **Chapter 4:** current story/overlay authority controls the upcoming restructure; all spoken dialogue is Dialogue Engine output rather than inherited exact transcript authority.
- **Chapters 5–13:** their current authoring status is recorded under `AUTHORING_STATUS/`; when authored, all spoken dialogue is generated through the same Dialogue Engine authority.

## Historical line-complete set
Exactly **41 historical dialogue/scene sources** are preserved from the migrated closed set:
- Ch0: S001–S006 + C01–C02 = 8
- Ch1: S007–S011 + C03–C05 = 8
- Ch2: S012–S016 + C06–C07 = 7
- Ch3: S017–S021 + H01–H04 = 9
- Ch4: S022–S026 + C08/C09/H05 + Crown Prototype = 9

This count describes preserved source material; it does **not** mean any of those files automatically control current exact spoken wording.

## What this folder owns
- current spoken dialogue generated / approved through the Dialogue Engine;
- dialogue-scene staging that materially controls delivery;
- mandatory-story and Character-Life dialogue authoring inputs and outputs;
- dialogue-specific identity / continuity overlays;
- explicitly preserved exact-line anchors;
- the scene-construction interface that combines dialogue craft with current gameplay/map/presentation context.

## What this folder does not own
Embedded old source notes may mention mechanics or story structure for context, but those are **not editable authority here**. Current mechanics and story structure must be read from their canonical system/story folders.

The ongoing area-design study remains research/design guidance until individual rules/numbers are explicitly locked by their owning domain. Dialogue may use its structural concepts without inventing canonical map sizes, chapter runtimes, encounter counts, or level bands.

## Current bounded dialogue corrections / examples
1. Current Face list is **Might / Elements / Grace / Perception / Memory / Ruin**; stale Resource/Acuity/Change Face naming must not return.
2. Ch0 old internal `Broken Champion's Ward` wording is not current-facing authority; use the current incomplete protective-response story state.
3. Ch0 negative old `First Champion` terminology is retired in favor of current Last Sentinel authority where appropriate.
4. Current region/place corrections already present in the repository source are preserved: **Yahtrenhold**, **Reaction Annex**, etc.
5. Ch1 C04's explicitly approved `old slut` wording remains an exact joke anchor if that exchange survives regeneration.
6. Ch3 H01's explicitly selected Cyanis/Torren opening insults remain exact anchors; all surrounding dialogue is regenerated.
