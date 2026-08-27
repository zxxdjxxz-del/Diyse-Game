# AGENTS.md — Diyse Engineering Contract

This file governs AI-assisted engineering work in this repository.

## Read first

Before changing gameplay code or production content, read:

1. `docs/ACTIVE_CANON.md`
2. `docs/IMPLEMENTATION_STATUS.md`
3. `docs/chapters/README.md`
4. the relevant current chapter file under `docs/chapters/`
5. the latest controlling canon audit for the subject
6. `docs/PRESENTATION_RULES.md`
7. the relevant subsystem document
8. `docs/DIALOGUE_AUTHORING_SCHEMA.md` and `docs/STEP_7C_AUTHORING_TEMPLATE.md` before dialogue Resource work
9. `docs/TECHNICAL_PROOF.md` only as compatible historical engineering evidence

If a task conflicts with these files or a newer explicit user instruction, stop and surface the conflict. Do not silently reinterpret canon.

## Current authority state

- Whole-project written authority: **Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.03 / Audit118**.
- Current exact ordinary-equipment / Relic / Legacy-Trait / Forge-source authority: `docs/canon/AUDIT118_COMPLETE_EQUIPMENT_TRACKER_DELTA_PROMOTION_AND_NUMERICAL_CATALOG_LOCK.md`.
- Compatible equipment structure / Synthesis-removal / donor-access authority: `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md`.
- Current Card / Prime resource + command authority: `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`.
- Current global combat / Ruin / status / class-Ability authority: `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`.
- Current chapter-number reconciliation: `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`.
- Current Chapter-10 story authority: `docs/canon/AUDIT112_CHAPTER_10_THE_LAST_BLANK_MIRENA_EASTERN_WAYFINDER_CALDER_AND_BURIED_REGISTRY_CLOSURE.md`.
- Current world-map / region authority: `docs/canon/AUDIT111_FINAL_WORLD_MAP_REGION_TERMINOLOGY_AND_VISUAL_AUTHORITY_CLOSURE.md`.
- Current travel / point-of-no-return authority: `docs/canon/AUDIT109_WORLD_MAP_ROAD_TRAVEL_AND_LAST_SHELTER_POINT_OF_NO_RETURN_CLOSURE.md`.
- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level.
- HD-2D is the sole active presentation target.

Historical audit filenames and acceptance IDs remain provenance. Current chapter folders and later overlays control implementation.

## Post-insertion chapter-number firewall

Chapter 10 — The Last Blank was inserted after Chapter 9.

Current late-game numbering:

- **Chapter 10 — The Last Blank** — Mirena records lead / Cerythvale / eastern forest / discovery of Eastern Wayfinder / physical-map completion / old Crown excavation / Calder provenance / Registry Warden / Buried Registry.
- **Chapter 11** — Crown Engine / Othmar Calder / Custodian / Truth.
- **Chapter 12 — The Reforged March** — final Black Host campaign / Varkesh / Vhalmarch Forward Hub / Vorathen / Vaelkor / cleanup.
- **Chapter 13 — The Last Command** — final Ancient domain / Last Weapon Archive / Last Shelter / Reconstituted Entity / Final Severance / ending.

Historical translation:
- old Ch10 → current Ch11;
- old Ch11 → current Ch12;
- old Ch12 → current Ch13.

Never implement the old `chapter_11 = Forward Hub/Vaelkor` or `chapter_12 = final domain` arrangement.

Current operational sources:
- `docs/chapters/chapter_10/CHAPTER_10_THE_LAST_BLANK_STORY_STRUCTURE_LOCK.md`
- `docs/chapters/chapter_11/CHAPTER_11_CURRENT_SCOPE.md`
- `docs/chapters/chapter_12/CHAPTER_12_REFORGED_MARCH_FORWARD_HUB_AND_CLEANUP_LOCK.md`
- `docs/chapters/chapter_13/CHAPTER_13_MACRO_STORY_STRUCTURE_LOCK.md`

## Current point of no return

Starting Chapter 13 is deliberate but **not** itself irreversible.

The true irreversible threshold is:

**Last Shelter → Reactor Galleries**

Before that threshold, the runtime must preserve a supported way to return to eligible unfinished world content.

Do not implement any old rule that disables all world access at Chapter-13 launch.

## Current world terminology

Use current names in authored prose/UI/codex/implementation-facing docs:

- **BLACK HOST TERRITORY / Black Host Territory**
- **THE WESTWAYS / The Westways**
- **THE GREYSPIRES / The Greyspires**
- **YAHTRENHOLD / Yahtrenhold** — never `The Yahtrenhold`
- **The Blackspine**
- **Westguard**
- **Vhalmarch**
- **Vorathen**
- **The Veiled Citadel**

Retired current-facing names include:
- Blackstone as the formal region label;
- The Crownhold / Southhold;
- Black Mountains;
- Westreach / Yahtrens Stand.

Legacy stable technical IDs may retain retired strings until a reference-safe engineering cleanup. Stable IDs are not authored geography authority.

## Chapter 10 knowledge firewall

For Chapter 10 — The Last Blank:

- Mirena has been reviewing strange Crown orders since Chapter 3.
- She finds an old eastern research authorization plus a later `research completed` notation, with the meaningful middle absent.
- Mirena and the party do **not** know Eastern Wayfinder exists at chapter start.
- The party discovers Eastern Wayfinder while investigating the old research area beyond Cerythvale.
- Eastern Wayfinder completes the physical Ancient map before the excavation/boss sequence.
- Calder's Prime research predates the game and predates any successful Prime activation.
- Calder's lawful standing recovery directive is why the recovered Card was transported to Caelora and therefore why Cyanis's Chapter-0 convoy existed.
- Calder did not choose Cyanis, cause the ambush, or know the Card would activate.
- Mirena's final provenance verification establishes Calder as the source behind the Chapter-3 composite seizure architecture.
- Registry Warden = one HP bar, no adds, no transformation, no boss-only subsystem.
- Buried Registry links geography with custody/authority/jurisdiction/responsibility/transfer but does not reveal the full Underground Crest Network / Crown Engine / Custodian / Entity truth.

Target first-clear runtime is approximately 55–65 minutes.

Do not invent Chapter-10 item/EXP/CEXP/Card rewards in story implementation; those are deferred to the item/progression pass.

## Current Chapter 12 campaign hard boundaries

- Current Chapter 12 = **The Reforged March**.
- Varkesh controls the defensive withdrawal and is defeated/captured alive before Vhalmarch becomes the Forward Hub.
- Once Vhalmarch is secured, **Cresthaven ↔ Vhalmarch** two-way travel remains available through the rest of Chapter 12 and the post-Vaelkor cleanup state.
- Cresthaven is the primary full-service HQ; Vhalmarch is essential-services field staging.
- Chapter-12 conventional Elite remains separate from Hunts.
- **Regional Hunt #11 — Throne of Emperor Vaelkor** belongs to current Chapter 12 and remains separate from the Elite.
- Vaelkor boss remains **Emperor of the Reforged Host → Sovereign Panoply Unbound**. He remains consciously himself and morally responsible; no possession and no third Vaelkor form.
- Vaelkor's defeat opens cleanup/preparation and does not automatically start Chapter 13.
- Native Legacy completion may occur during the late-Ch12 / early-Ch13 returnable window when its individual requirements are satisfied. There is **no mandatory Synthesis-resolution scene gate**.

## Current Chapter 13 final-act hard boundaries

- Chapter 13 = **The Last Command**.
- Surface access uses the Vorathen / Veiled Citadel excavation route; Final Archive is not the mandatory finale entrance.
- Regional Hunt: none.
- Elite: **Devourer of Names**.
- Calamity Memory remains enemy/special-enemy ecosystem material, not the Elite.
- Mandatory guardian: **Last Weapon Archon**, one HP bar, physical Ancient Diysean guardian.
- Locked macro progression: **Deepest City → Deep City → Last Weapon Archive → Last Weapon Archon → Last Shelter → Reactor Galleries → Reactor–Crest Interface → Reconstituted Entity → Crest Integration → The Last Command → Final Severance → ending**.
- Last Weapon Archive is where the modern party first discovers exactly one mangled Entity portion survived the ancient convergence/compression/discharge firing.
- Custodian's record was incomplete, not deceptive.
- Final Severance is not an Ancient procedure and is invented by the modern six during The Last Command.
- Reconstituted Entity is the same sole surviving continuity, not a copy/child/second fragment.
- Final boss has exactly two genuine full-health forms: **Reconstituted Entity → The Last Command**. No third form.
- Entity ends permanently; no hidden copy/branch/escape fragment.
- Giant Crest/viable reactors survive damaged/stable.
- All six permanent party members survive.

## Current Faces / Story Primes

Faces:
- Might
- Elements
- Grace
- **Acuity**
- Change
- Ruin

Story Primes:
- Might — Last Sentinel
- Elements — Last Convergence
- Grace — Last Sanctuary
- Acuity — **Last Cartographer**
- Change — Last Scribe
- Ruin — Last Erasure

No Prime had ever been successfully activated before the modern story.

Do not restore `Resource / Last Measure` as current final-act terminology.

Current Final Severance order:
1. Last Sentinel / Might — HOLD
2. Last Convergence / Elements — DISTINGUISH
3. Last Cartographer / Acuity — MAP
4. Last Sanctuary / Grace — PRESERVE
5. Last Scribe / Change — CONTAIN
6. Last Erasure / Ruin — END

## Current system baselines

- Player level cap: **70**.
- Base class cap: **CL13**.
- Subclass cap: **CL13**.
- Maximum active party: four.
- Maximum simultaneously active enemies: eight.
- Permanent battle commands: **Attack / Ability / Card / Item / Defend**.
- MP is the universal ordinary Ability resource; no character-specific combat gauges.
- No Ability or Ultimate requires a specific equipped weapon once learned.
- Exactly **24 Standard Cards** and **12 Prime Cards**.
- Standard Cards are reusable and MP-consuming; they are data-driven and remain outside ordinary inventory.
- Persistent game state remains versioned plain data separate from scene nodes.
- Random encounters remain normal hostile-exploration grammar where approved; do not replace them with visible roaming enemies without explicit canon revision.

Current Base/Subclass identities:
- Cyanis — **Crest Knight / Crest Magus**
- Ilyra — **Blue Warden / Vowblade**
- Torren — **War Archer / Routeweaver**
- Nimera — **Cardweaver / Sixfold Knight**
- Vaelira — **Prism Archer / Green Arcanist**
- Seyrik — **Ruin Vanguard / Ruin Healer**

## Sixfold Volition

Formal term: **The Sixfold Volition**. `Sixfold Accord` is deprecated.

- Chapter 6 ends with Seyrik's conditional permanent recruitment.
- Chapter 7 — The Prison of Names — is the first full-six integration chapter.
- Sixfold Volition occurs at the end of Chapter 7 / Cresthaven return.
- No permanent character uses a Subclass before the Volition.
- All six Subclasses unlock there.
- Chapter 8 is the first full mandatory post-Volition Subclass chapter.

Reciprocal pairs:
- Cyanis ⇄ Vaelira
- Ilyra ⇄ Seyrik
- Torren ⇄ Nimera

## Subclass donor equipment access — Audit117/118

Current progression milestones:

- **CL1** — linked donor Primary access
- **CL3** — linked donor Armor access
- **CL5** — linked donor Secondary access where applicable
- **CL7** — Subclass Mastery 3 becomes eligible; purchasing it grants linked donor Relic access
- **CL11** — Subclass Mastery 4 becomes eligible; purchasing it grants linked donor Legacy access

The receiver equips the donor's **existing obtained item**. No separate shared Relic/Legacy artifact is created.

**Synthesis is removed.** Never implement a Synthesis Mastery node, Synthesis MP cost, Synthesis passive, or Base-CL13/Subclass-CL13 Synthesis gate.

## Legacy project / Kessara baseline — Audit117/118

There are exactly **17 native Legacy equipment pieces** and **no separate shared-Legacy artifact catalog**.

Native Legacy completion requires:
- Base CL13;
- all four Core Masteries;
- that character's Character Quest / resolution;
- the Character Quest's unique Legacy Component;
- the character's unique Legacy precursor;
- dedicated Legacy Gate A and Gate B materials;
- Kessara project availability.

Gate A releases the Legacy weapon. Gate B releases all remaining pieces in that native package.

Forge economy:
- 5 Face components per Face / 30 total;
- 2 Legacy-gate-specific per Face;
- 3 Relic-copy-specific per Face;
- Legacy-gate and Relic-copy materials are not interchangeable;
- mandatory Gate materials do not require Hunts or sidequests;
- Audit118 contains the exact 30-slot chapter/source-role matrix.

Relic-copy forging may create one identical extra copy of an already-obtained Relic. Max quantity per Relic = 2; the finite pool allows at most three duplicated Relics per Face. Legacies remain unique.

Character Quests remain optional while world return remains available, but a character's own Legacy cannot be completed until that character's Character Quest and unique Legacy Component are complete/registered.

Secured Legacy completion remains available through the **Chapter-13 pre-Last-Shelter returnable period**. Final cutoff is the Last Shelter → Reactor Galleries commitment.

Exact post-insertion CEXP timing remains pending the dedicated progression pass. Do not preserve old 12-chapter CEXP milestones by assumption.

## Equipment-count / slot firewall — Audit118

Current active catalog:
- **38 ordinary equipment pieces**
- **36 Relics**
- **17 Legacies**
- **91 total**

All 12 Subclass Relics are removed.

Slot rules that must not regress:
- Ilyra — Wardrod Primary; Shield or Focus Secondary.
- Torren Great Bow — Weapon + Secondary.
- Vaelira Arcane Staff — one-slot Primary; Focus legal.
- Seyrik Two-Handed Sword — Weapon + Secondary.
- Nimera ordinary / surviving Relic Conduits — one-slot.
- Nimera native Legacy Conduit — **Weapon + Secondary**.

Audit118 is the exact implementation authority for:
- all 38 ordinary raw-stat lines and Ch2–8 source map;
- all 36 surviving Relic raw-stat/Trait packages;
- all 36 current Relic Ch6–12 first-acquisition homes;
- current native Legacy Trait definitions;
- Cresthaven ordinary relative-value/backfill rules;
- the exact 30 Forge Component source-role matrix.

Equipment tier identity:

> **Ordinary < Relic < Legacy**

Legacies may carry capstone Max HP / Max MP / Accuracy / Evasion perks. **Exact 17-piece Legacy raw-stat/perk numbers remain pending approval; do not implement the working v600 numbers as canon yet.**

Final Relic / Legacy / Legacy-Component / Forge-variant names remain deferred until dialogue is substantially more complete.

## Critical presentation rule

Diyse is **HD-2D**.

Current production targets:
- field characters approximately 80 px;
- battle characters approximately 200–220 px;
- large high-resolution dialogue portraits;
- authored layered environments;
- bounded authored cameras and restrained parallax;
- party left / enemies right / open center combat frame;
- reusable battle-background families derived from field geography;
- exact visual masters control derivatives.

Do not revive retired 2.5D/3D presentation direction from historical proof documents.

## Affordable HD-2D behavior

Prefer reusable animation and staging families, portrait/expression swaps, bounded camera work, state-swapped props/environments, layered background loops, modular Face/Card/Prime/elemental VFX, and reusable battle-background families.

Avoid by default: physics destruction, fluid simulation, crowd simulation, free-camera exploration, chain/cloth/hair simulation, bespoke body animation for every Ability, or one unique arena per formation.

## Boss/form implementation categories

Classify encounter transitions correctly:

1. **Same-body / same-HP escalation:** presentation/behavior changes without unnecessary new body/HP reset.
2. **Genuine new form:** new combat state/body with fresh HP only where canon explicitly defines it.
3. **Prime-scale entity:** use the reusable Prime presentation pipeline.

Do not add health bars, transformations, threshold attacks, or Prime refreshes not present in canon.

## Prime presentation

S021 identifies/unlocks Last Sentinel without manifesting it. S022's Elder Briarhide fight remains the first verified modern Prime manifestation under compatible early-game authority.

Reusable Prime presentation remains:

command accepted → battlefield yields through authored camera/light → exact Prime manifestation → one legal action → impact → dismissal → normal battle presentation returns.

Do not convert Prime use into a detached movie that bypasses combat rules.

## Completed Chapters 0–4 rule

Do not recover, re-author, or re-audit Chapters 0–4 as though their approved story/dialogue were missing.

Use exact source and validated Resources listed by `docs/chapters/README.md` and `docs/IMPLEMENTATION_STATUS.md`.

Later terminology/canon overlays may require bounded reference-safe updates without reopening dialogue voice or scene logic.

## Engineering behavior

- Fresh Godot/GDScript implementation; do not copy/port code from historical `zxxdjxxz-del/Diyse` unless explicitly authorized for named reuse.
- Dialogue is one authored continuity; no response wheels, tone selection, morality/affinity responses, persuasion trees, or romance routes.
- Production dialogue uses stable-ID `DiyseDialogueSceneDefinition` Resources; never embed canon scene text or final portrait paths in generic engine code.
- Implement one bounded milestone at a time.
- Preserve deterministic behavior where combat rules require it.
- Add deterministic validation for pure logic/content contracts where practical.
- Keep exploration, dialogue, combat, save/state, UI, and content loading separable.
- Prefer simple readable GDScript over clever abstractions.
- Keep authored content data-driven where practical.
- Do not invent mechanics, terminology, characters, Cards, classes, resources, story outcomes, or missing dialogue merely to fill gaps.
- Do not optimize around placeholders in a way that blocks final exact assets.
- Do not change canon/specification documents as accidental side effects of code work.

## Progression/reward reindex boundary

The added Chapter 10 requires a dedicated balance pass. Historical exact late-game EXP/CEXP/economy timing written for the 12-chapter spine is non-controlling where it depends on that old timing.

Use:
`docs/canon/POST_INSERTION_PROGRESSION_TIMING_HOLD_2026-08-23.md`

Do not silently invent replacement progression numbers during unrelated implementation work.

## Historical audit interpretation

Historical Audit84/Audit89 remain useful decision provenance but do not carry current chapter numbers.

Use:
- `docs/canon/AUDIT89_CURRENT_REINDEX_AND_TERMINOLOGY_OVERLAY_2026-08-23.md`
- `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`

Current operational chapter files always outrank historical folder/number assumptions.
