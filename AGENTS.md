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

- Whole-project written authority: **Diyse v2.05 / Audit120**.
- Current Critical/direct-damage authority: `docs/canon/AUDIT120_CRITICAL_HIT_AND_DIRECT_DAMAGE_FORMULA_LOCK.md`.
- Compatible combat/resource/Prime/progression reconciliation: `docs/canon/AUDIT119_POST_AUDIT116_COMBAT_RESOURCE_PRIME_AND_PROGRESSION_RECONCILIATION_LOCK.md`.
- Exact ordinary/Relic/Legacy-Trait/Forge numerical catalog: `docs/canon/AUDIT118_COMPLETE_EQUIPMENT_TRACKER_DELTA_PROMOTION_AND_NUMERICAL_CATALOG_LOCK.md`.
- Equipment/Legacy/class-access structure: `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md`.
- Compatible Card/Prime command authority: `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`.
- Compatible global status/element/Ruin/class-Ability authority: `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`.
- Current chapter-number reconciliation: `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`.
- Current Chapter-10 story authority: `docs/canon/AUDIT112_CHAPTER_10_THE_LAST_BLANK_MIRENA_EASTERN_WAYFINDER_CALDER_AND_BURIED_REGISTRY_CLOSURE.md`.
- Current world-map / region authority: `docs/canon/AUDIT111_FINAL_WORLD_MAP_REGION_TERMINOLOGY_AND_VISUAL_AUTHORITY_CLOSURE.md`.
- Current travel / point-of-no-return authority: `docs/canon/AUDIT109_WORLD_MAP_ROAD_TRAVEL_AND_LAST_SHELTER_POINT_OF_NO_RETURN_CLOSURE.md`.
- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level.
- HD-2D is the sole active presentation target.

Historical audit filenames and trackers remain provenance, not automatic current authority.

---

## Current system firewall — Audit120 / Audit119

### Direct damage / Critical Hits

Physical direct damage:

> **BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

> **EffectiveDefense = CurrentDefense × (1 - EffectiveDefensePenetration)**

Magical direct damage:

> **BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

> **EffectiveSpirit = CurrentSpirit × (1 - EffectiveSpiritPenetration)**

- Physical = Attack vs Defense.
- Magical = Magic vs Spirit.
- Character-Ability Ruin remains 75% Attack / 25% Magic where Audit115 applies.
- Same-axis penetration adds in percentage points and caps at **75%**.
- No cross-axis penetration transfer.
- No hidden universal AoE penalty.
- No universal random damage variance.
- Basic Attack = 100 Power / Physical / Neutral unless equipment explicitly changes affinity.

Critical rules:
- base Critical Chance = **5%**;
- Critical bonuses are flat percentage-point additions;
- ordinary random Critical Chance cap = **50%**;
- eligible Critical multiplier = **1.5×**;
- resolve Base Hit/Evasion before Critical Chance;
- a miss gets no Critical roll;
- each authored direct hit in a multihit action rolls independently by default;
- one authored Hybrid hit uses one Critical roll on its combined eligible direct damage;
- eligible Magical direct hits use the same 1.5× multiplier;
- Critical does not bypass Defense/Spirit;
- Critical does not automatically improve harmful-status application;
- Burn, Bleed, explicitly no-Crit copied/echo damage, indirect Max-HP damage unless explicitly authored otherwise, and healing cannot Crit.

Do not implement the superseded Audit119 `Offense × 1.50 × 150/(150+Defense)` resolver.

Use **Base Hit**, never `Accuracy`, as the current hit-stat term.

### Standard Cards

Exactly 24 Standard Cards, maximum 3 equipped per character.

Current Card MP range is **18–48 MP**, not Audit116's older 12–36 range. Exact current costs are in Audit119 / ACTIVE_CANON.

Cards are reusable and MP-consuming. Do not implement a charge/deck/draw/discard/duplicate/rank system.

### Primes

Current progression:

> **Recovered → Awakened**

Do not implement the temporary tracker label `Reactive`.

Current Invocation MP:
- Recovered Story — **50 MP**
- Awakened Story — **80 MP**
- Awakened Major Hunt — **90 MP**
- manifested commands — 0 additional MP

Do not use Audit116's old 60/75/75 ladder.

Awakened Primes replace/suspend the party for exactly 3 Prime rounds, then trigger the shared 3-full-normal-round cooldown. Prime use remains once per identity per battle / genuine fresh-HP form.

Default Prime harmful-status susceptibility = 80%. Freeze/Stun together may deny at most one selected Prime command per manifestation; after that the Prime is Freeze/Stun immune for the remainder of that manifestation.

Prime manifestation uses the Audit119 Reference-Level scaling architecture. Do not invent Prime levels or Prime XP.

### Consumables

Current Consumable count = **21**.

MP recovery:
- Flow Tonic 50 MP
- Deepflow Tonic 80 MP
- Highflow Tonic 120 MP
- Reservoir Tonic 75% Max MP
- Emergency Kit 60% Max MP as its MP component

Do not use the old 20-consumable count. Exact HP-restorative values remain open.

---

## Current class / Mastery architecture

Permanent six:
- Cyanis — **Crest Knight / Crest Magus**
- Ilyra — **Blue Warden / Vowblade**
- Torren — **War Archer / Routeweaver**
- Nimera — **Cardweaver / Sixfold Knight**
- Vaelira — **Prism Archer / Green Arcanist**
- Seyrik — **Ruin Vanguard / Ruin Healer**

Base and Subclass caps are both **CL13**.

No permanent character uses a Subclass before the Sixfold Volition at the end of Chapter 7.

Current Subclass equipment progression:
- CL1 — donor Primary
- CL3 — donor Armor + Mastery 1 eligible
- CL5 — donor Secondary + Mastery 2 eligible
- CL7 — Mastery 3 / Equipment Mastery eligible; **purchase grants donor Relic access**
- CL11 — Mastery 4 / Legacy Mastery eligible; **purchase grants donor Legacy access**

Do not grant donor Relic/Legacy permission merely for reaching CL7/CL11 if the relevant Mastery purchase has not occurred.

**Synthesis is removed.** Never implement:
- Synthesis Mastery node;
- Synthesis MP cost;
- Synthesis passive/integration effect;
- Base-CL13 + Subclass-CL13 Synthesis gate;
- separate shared-Legacy items.

Only eight active Mastery nodes remain. The exact Mastery Point grant schedule must be reconciled; do not invent a ninth node merely to consume the old ninth point.

Current exact Base/Subclass Ability MP costs after the latest class-kit changes are still open. Preserve the higher-MP direction and modest Subclass premium, but do not treat retired-name tracker tables or older low Audit115 costs as final implementation values.

---

## Equipment / Relic / Legacy firewall

Current active catalog:
- 38 ordinary
- 36 Relics
- 17 native Legacies
- **91 total**

All 12 Subclass Relics are removed.

Exact ordinary/Relic data is in Audit118 and is implementation-ready unless a newer audit changes it.

Slot rules:
- Ilyra — Wardrod Primary; Shield or Focus Secondary.
- Torren Great Bow — Weapon + Secondary.
- Vaelira Arcane Staff — one-slot Primary; Focus legal.
- Seyrik Two-Handed Sword — Weapon + Secondary.
- Nimera ordinary / surviving Relic Conduits — one-slot.
- Nimera native Legacy Conduit — Weapon + Secondary.

Native Legacy completion requires:
- Base CL13;
- four Core Masteries;
- Character Quest / resolution;
- unique Character Quest Legacy Component;
- unique Legacy precursor;
- Gate A material;
- Gate B material;
- Kessara project availability.

Gate A releases the Legacy weapon. Gate B releases the rest of the package.

Linked donor access uses the donor's **existing obtained item**. No separate shared Relic/Legacy artifact is created.

Forge economy:
- 30 components total;
- 2 Legacy-gate-specific per Face;
- 3 Relic-copy-specific per Face;
- categories are non-interchangeable.

Relic copies:
- original must already be obtained;
- one matching-Face copy material;
- maximum one forged duplicate / max quantity 2;
- Legacies remain unique.

Equipment hierarchy:

> **Ordinary < Relic < Legacy**

Exact Legacy raw stats / HP-MP-Base-Hit-Evasion assignments remain pending approval. Do not implement the working v600 numbers as canon yet.

Final Relic / Legacy / Legacy-Component / Forge-variant names remain deferred.

---

## Progression / enemy balance firewall

- Player level cap = 70.
- Chapter 0 grants no character levels.
- Chapters 1–7 intentionally sit somewhat below a near-linear curve.
- Faster level gain begins after Chapter 7.
- Expected Chapter-12 campaign-only clear target = **Lv60**.
- Spread the needed late EXP backward through Chapter 9 onward.
- Enemy strength and kill EXP should rise within a chapter from start to end.
- Old/weak enemies should award much less kill EXP to overlevelled parties.

Do **not** implement the old v494–v503 exact chapter-level/enemy/encounter tables. Detailed current Ch1–13 player bands, enemy bands, encounter counts, formation EXP, and diminishing-return percentages remain deferred to the dedicated progression pass.

Boss/Hunt/Elite resistance should be higher than ordinary-enemy resistance without blanket immunity. Use Audit119's 125/100/80/60/0 elemental framework and 100/80/60/0 status-susceptibility framework.

---

## Post-insertion chapter-number firewall

The game has Chapter 0 plus Chapters 1–13.

Current late-game numbering:
- Chapter 10 — **The Last Blank**
- Chapter 11 — **Crown Engine**
- Chapter 12 — **The Reforged March**
- Chapter 13 — **The Last Command**

Historical translation:
- old Ch10 → current Ch11
- old Ch11 → current Ch12
- old Ch12 → current Ch13

Never implement the old `chapter_11 = Forward Hub/Vaelkor` or `chapter_12 = final domain` arrangement.

Current operational chapter files:
- `docs/chapters/chapter_10/CHAPTER_10_THE_LAST_BLANK_STORY_STRUCTURE_LOCK.md`
- `docs/chapters/chapter_11/CHAPTER_11_CURRENT_SCOPE.md`
- `docs/chapters/chapter_12/CHAPTER_12_REFORGED_MARCH_FORWARD_HUB_AND_CLEANUP_LOCK.md`
- `docs/chapters/chapter_13/CHAPTER_13_MACRO_STORY_STRUCTURE_LOCK.md`

---

## Current point of no return

Starting Chapter 13 is deliberate but not itself irreversible.

True irreversible threshold:

> **Last Shelter → Reactor Galleries**

Before that threshold, preserve supported return to eligible unfinished world content.

---

## Current ordinary Side-Quest correction

Do not use the stale v480–v493 cumulative-tracker reduction branch as current roster authority.

Current retained ordinary quests include:
- Edda Harth — **The Marks We Leave** — Ch1 after Torren joins / Greenhollow / low-zero required combat.
- Edda Harth — **When the Roads Open** — post-Vaelkor cleanup / current Ch12.
- Talia Rell — **The Third Caravan** — after Ch8 / Greenhollow → Ashford.
- Talia Rell — **The Living List** — after Ch10 / Ashford anchor.

Dialogue and exact final rewards remain deferred.

---

## Current world terminology

Use current-facing terminology:
- BLACK HOST TERRITORY / Black Host Territory
- THE WESTWAYS / The Westways
- THE GREYSPIRES / The Greyspires
- YAHTRENHOLD / Yahtrenhold
- The Blackspine
- Westguard
- Vhalmarch
- Vorathen
- The Veiled Citadel

Do not restore retired current-facing labels such as Blackstone, Westreach, Black Mountains, or The Crownhold.

Legacy stable technical IDs may retain old strings until a reference-safe cleanup; technical IDs are not authored geography authority.

---

## Chapter 10 knowledge firewall

For Chapter 10 — The Last Blank:
- Mirena begins from the old eastern research-authorization gap, not prior knowledge of Eastern Wayfinder.
- Eastern Wayfinder is discovered during the investigation and completes the physical Ancient map.
- Calder's Prime research predates any successful Prime activation.
- Calder's lawful recovery directive explains why the recovered Card travelled to Caelora; he did not choose Cyanis or cause the ambush.
- Registry Warden has one HP bar, no adds, no transformation, no boss-only subsystem.
- Buried Registry does not reveal the full Crown Engine/Custodian/Entity truth.

Do not invent Chapter-10 reward allocation during story implementation.

---

## Chapter 12 / 13 hard boundaries

Chapter 12:
- Varkesh controls the defensive withdrawal and is defeated/captured before Vhalmarch becomes the Forward Hub.
- Cresthaven ↔ Vhalmarch two-way travel remains through Chapter 12 and post-Vaelkor cleanup.
- Regional Hunt #11 remains separate from the conventional Elite.
- Vaelkor remains **Emperor of the Reforged Host → Sovereign Panoply Unbound**, consciously himself, no third form.
- Vaelkor defeat opens cleanup and does not auto-start Chapter 13.

Chapter 13:
- Surface entry uses the Vorathen / Veiled Citadel excavation route.
- Regional Hunt: none.
- Elite: Devourer of Names.
- mandatory guardian: Last Weapon Archon.
- final boss: exactly **Reconstituted Entity → The Last Command**, two genuine full-health forms.
- no third form / hidden copy / escape fragment.
- all six permanent party members survive.

---

## HD-2D presentation contract

Diyse is **HD-2D**.

Current production targets:
- field characters approximately 80 px;
- battle characters approximately 200–220 px;
- large dialogue portraits;
- authored layered environments;
- bounded cameras and restrained parallax;
- party left / enemies right / open center combat frame;
- reusable battle-background families derived from geography;
- exact visual masters control derivatives.

Prefer reusable animation/staging families, portrait swaps, bounded camera work, state-swapped props/environments, layered loops, modular Face/Card/Prime/element VFX, and reusable battle backgrounds.

Avoid by default: physics destruction, fluid simulation, crowd simulation, free-camera exploration, chain/cloth/hair simulation, bespoke body animation for every Ability, or a unique arena for every formation.

---

## Boss/form implementation categories

1. Same-body / same-HP escalation — behavior/presentation changes without unnecessary HP reset.
2. Genuine new form — fresh HP only where canon explicitly defines it.
3. Prime-scale entity — use the reusable Prime presentation pipeline.

Do not add health bars, transformations, threshold attacks, or Prime refreshes not present in canon.

---

## Completed Chapters 0–4 rule

Do not recover, re-author, or re-audit Chapters 0–4 as though approved story/dialogue were missing.

Use exact source/validated Resources listed by `docs/chapters/README.md` and `docs/IMPLEMENTATION_STATUS.md`.

Later terminology/canon overlays may require bounded reference-safe updates without reopening scene logic or dialogue voice.

---

## Engineering behavior

- Fresh Godot/GDScript implementation; do not copy/port code from historical `zxxdjxxz-del/Diyse` unless explicitly authorized.
- Dialogue is one authored continuity; no response wheels, morality routes, affinity routes, persuasion trees, or romance branches.
- Production dialogue uses stable-ID `DiyseDialogueSceneDefinition` Resources; do not embed final canon dialogue in generic engine code.
- Implement one bounded milestone at a time.
- Preserve deterministic behavior where combat rules require it.
- Add deterministic validation for pure logic/content contracts where practical.
- Keep exploration, dialogue, combat, save/state, UI, and content loading separable.
- Prefer simple readable GDScript over clever abstractions.
- Keep authored content data-driven where practical.
- Do not invent mechanics, terminology, characters, Cards, classes, resources, story outcomes, or missing dialogue merely to fill gaps.
- Do not optimize around placeholders in a way that blocks final exact assets.
- Do not change canon/specification documents as accidental side effects of code work.

The active working tracker is consolidated. Do not treat the frozen 165,000-line cumulative tracker as an implementation authority; use master audits and the compact current tracker instead.
