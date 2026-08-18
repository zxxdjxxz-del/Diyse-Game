# Diyse — Active Engineering Canon Guardrails

This is an implementation-facing summary. It does **not** replace the authoritative Complete Master Canon or newer explicit user corrections. If this summary conflicts with newer authority, the newer authority wins and this file must be updated deliberately.

## Current written authority

- **Whole-project root:** Diyse Clean Active Complete Master Canon **v1.64 / Audit79** — Chapter 1 Full Production Dialogue Lock, inheriting the Chapter 2 Audit78 line-complete lock and corrected Chapter 3 Audit77 line-complete lock.
- **Date:** August 18, 2026.
- Chapters **0–3 are COMPLETE/CLOSED** at story/dialogue/continuity/relationship/affordable-2.5D production-authority level.
- Chapter 4 — **The Seventh Reaction** — is the next exact scene-level authoring frontier.
- Completed early-chapter repository packages: `docs/chapters/`.
- Chapters 1–3 exact line-complete repository source: `docs/chapters/dialogue/`.
- Chapter 0 exact line/cue authority remains the merged Godot Resource set at `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` where compatible with later canon.
- **Chapter 1 S007–S011 + C03–C05 are now converted into production `.tres` dialogue Resources and validated for exact source parity plus whole-chapter continuity.**
- Chapters 2–3 still require Resource conversion/implementation validation; that does not reopen their approved dialogue.

## Project foundation

- Game: DIYSE — mature-fantasy 2.5D party-command JRPG.
- Target platform: Android / APK.
- Target runtime: approximately **25 hours**, with final timing validation still implementation work.
- Critical story: Chapters 0–12 exactly, plus Sixfold Accord interlude and cleared-save `WORLD_AFTER` free roam.
- Permanent roster: exactly six.
- Maximum active battle party: four; two reserve when roster-complete.
- Absolute character level cap: **60**.
- Chapters 0–10 broadly occupy progression through Level 50; Chapters 11–12 extend through the 50s toward 60.
- No Level 61+, prestige levels, separate postgame progression campaign, or new equipment tier above Legacy.
- Worldframe Depths remains a specifically **Level-50 optional-major challenge**, not the absolute character-level cap.
- Dialogue: one authored continuity; no response wheel, morality route, affinity response, selectable protagonist personality, or romance route/system.
- Cleared-save aftermath exists; no hidden true-ending route.

## World geography

The Three Realms of modern Yahtrea are:

- **Edgelands** — west.
- **Diysereach** — north. “The Highlands” may be descriptive terrain language, not the formal Realm name.
- **Southhold** — south/east and includes Caelora.

The Black Mountains lie west outside Yahtrea and are Black Host territory.

`Heartlands`, `Crown Heartlands`, and `Crown Region` are not active formal Realm names.

Broad campaign movement: **Edgelands → Southhold → Diysereach → Southhold → Black Mountains → Ancient subterranean Diyse**.

### Chapter 3 geography hard lock

**Caelora → Old City / Suppressed Archives → separate Cresthaven.**

Caelora is the national capital/seat of the Crown within Southhold. Cresthaven is a separate hub/site and is not a room, district, wing, or chamber inside Caelora's Old City.

The controlling S020→S021 transition is explicit: after the First Command Warden, the cleared command state opens a command-record room that proves the false order was assembled from separate authentic judicial/custody inputs; Torren recognizes and copies a map-like routing display; the party returns to Mirena; Mirena identifies the destination as **Cresthaven, an abandoned Crown outpost in Southhold**. The party stops for the night. S021 begins the next morning with Mirena already at Cresthaven with workers, records staff, medical support, supplies, and security establishing it as the party's working headquarters while the investigation continues.

## Chapter spine

| State | Title | Current status |
|---|---|---|
| Ch0 | The Broken Convoy | COMPLETE/CLOSED; exact Resources merged, later compatibility overlays apply |
| Ch1 | Brackenwall and the Wayfinder | COMPLETE/CLOSED; **production dialogue Resources converted; exact source-parity + continuity validated** |
| Ch2 | The Drowned Oath | COMPLETE/CLOSED; line-complete repo source; Resource conversion pending |
| Ch3 | The Old City and Last Sentinel | COMPLETE/CLOSED; line-complete corrected repo source; Resource conversion pending |
| Ch4 | The Seventh Reaction | next exact scene-production frontier |
| Ch5 | The Mountain Engine | inherited architecture |
| Ch6 | Broken Sky and Crimson Work | inherited architecture |
| Accord | Sixfold Accord | locked interlude architecture |
| Ch7 | The Prison of Names | inherited architecture |
| Ch8 | Westreach and the Marshal | inherited architecture |
| Ch9 | Equal Mercy and Continuity | inherited architecture |
| Ch10 | Crown Engine and Sixfold Truth | inherited architecture |
| Ch11 | The Reforged March | Black Mountains; progression beyond 50 begins |
| Ch12 | The Last Command | Ancient subterranean Diyse; progression culminates at 60 |
| After | WORLD_AFTER — Cresthaven Reconstruction | cleared-save free roam / aftermath |

## Permanent cast / class / Face / Story Prime

| Character | Age | Base → Subclass | Face | Story Prime |
|---|---:|---|---|---|
| Cyanis Dovaren | 29 | Crest Knight → Crest Magus | Might / Ruby | Last Sentinel |
| Ilyra Amarin | 28 | Blue Warden → Vowblade | Grace / Blue | Last Sanctuary |
| Torren Harth | 42 | War Archer → Routeweaver | Resource / Gold | Last Measure |
| Nimera Pellan | 23 | Cardweaver → Sixfold Knight | Change / Fuchsia | Last Scribe |
| Vaelira Serren | 27 | Green Arcanist → Prism Archer | Elements / Emerald | Last Convergence |
| Seyrik Rell | 29 | Ruin Vanguard → Ruin Reclaimer | Ruin / Purple | Last Erasure |

All Subclasses are first learned at the Sixfold Accord. No permanent character has meaningful pre-Accord Subclass training.

Maevra Solmar is a recurring temporary/guest playable ally, not a seventh permanent. Kessara Durnan is a recurring technical ally, not permanent.

## Combat architecture

- Discrete round-based command combat.
- Permanent commands: Attack / Ability / Card / Item / Defend.
- Speed determines action order only; it does not grant extra ordinary actions.
- MP is the universal ordinary Ability resource.
- No grid, lanes, facing system, real-time meter, stagger gauge, overwatch, or character-specific combat resource.
- Maximum four active.
- Traditional random battles are the ordinary hostile-exploration layer where fiction supports them. Authored safe/story pockets suppress encounter triggering while preserving local pressure rather than resetting it.
- Automatic hostile retargeting remains the accepted implementation behavior when an original hostile target dies before resolution, unless an authored effect explicitly overrides it.

## Class EXP / Focus

Class/Subclass EXP goes **only to the selected class**:

- Base Focus → selected Base Class receives all CEXP; Subclass receives 0.
- Subclass Focus → selected Subclass receives all CEXP; Base receives 0.
- No passive split, donor share, catch-up share, or “base always gains” exception.

Open equipment/persistent ability authority remains: once an equipment/ability access is legally unlocked, changing Focus does not hide or revoke it. Focus controls the selected class stat package/Trait and class-only behavior.

## Cards

- **42 Cards total:** 30 Standard + 12 Prime.
- 30 Standard = five per Face.
- 12 Prime = six Story Primes + six optional-major Primes.
- Standard Cards are unlimited-use, data-driven; no charges, Essence, Card ranks, refresh counters, or duplicate farming.
- Cards and Conduits are separate systems.
- Bosses/constructs do not create Cards; victory/access may gate recovery of pre-existing Ancient Cards.

## Conduits

Conduit is the equipment category used by Nimera's Cardweaver tradition and later by Torren's inherited Routeweaver access. A Conduit can be a tome, talisman, seal, codex, charm, crystal, medallion, token, or relic. The object does not become a melee weapon: it manifests an airborne weapon-form for ordinary Attack while the bearer uses reusable casting/command presentation.

## Prime fiction / implementation separation

- Story Prime acquisition order: Last Sentinel (Ch3), Last Measure (Ch5), Last Convergence (Ch6), Last Scribe (Ch7), Last Sanctuary (Ch9), Last Erasure (Ch10).
- Prime activation uses the bearer's selected Card action and the accepted directly controlled replacement/suspension architecture.
- No living modern person has witnessed a verified Prime Manifestation before the first successful post-S021 battle use of Last Sentinel.
- S021 identifies/unlocks Last Sentinel **without manifesting it**. The player's first later real-battle use is the first verified modern Prime activation/sighting.
- Gameplay UI can explain technical battle rules after unlock. Characters do not acquire those empirical formulas/durations as in-world knowledge merely because the UI exists.

## Modern knowledge / Ancient Diysean firewall

Modern people broadly know:

- Ancient Diyseans were advanced humans.
- Their civilization ended in a great catastrophe.
- Ancient ruins/subterranean sites exist.
- Cards come from Ancient Diyse.
- Some fragments of names/history survive.

Modern people do **not** begin with the full truth of:

- the Entity;
- the true Ancient War / Last Weapon operation;
- the unified physical Underground Crest Network;
- the enormous buried Crest beneath Yahtrea and beyond;
- the six original Story-Prime sacrifice warriors and final inheritance purpose.

Ancient machinery may recognize signatures/Cards/Faces, follow instructions, assess claims, redirect routes, and change tactics. Do not infer broad conscious AI from those behaviors.

## Underground Crest Network

Later-story authority: the Network is a physical underground civilization of bunkers, stockpiles, transit, cities, defenses, and reactor infrastructure built as catastrophe-survival architecture. It is not a consciousness network or one-person-anchor system. Multiple reactors inject magic into one enormous regional buried Crest; the land/Crest is the medium. This truth is not an early-chapter exposition shortcut.

## Cresthaven

Cresthaven is an abandoned Crown outpost in Southhold that Mirena recognizes from Torren's copied post-Warden routing map. By the time the party arrives the next morning in S021, Mirena has already begun reactivating it with Crown workers/staff so it can serve as a **working headquarters while the party investigates what is going on**.

Cresthaven becomes one connected master hub with Command, Common, Archive, Medical, Workshop, Lodging, Training, Overlook, and Departure Court sublocations. Chapter 3 establishes only the immediate safe loop: Rest/Save, Formation, Archive/Records, Medical/Recovery, Departure. Later services unlock through later hub phases.

Preferred optional-content rhythm: **chapter exploration → home/Cresthaven → optional revisit/Hunt → home → onward**.

## Regional Hunt return grammar

Eligible chapter-dungeon Regional Hunts use a visible but unavailable first-pass branch. The chapter climax changes local state so the branch opens afterward and generally remains available. Return through a shortcut/cleared route rather than replaying the full dungeon.

Early locks:
- Hunt #1 Cistern Devourer: post-S011 route spur toward Dunmere; standalone route exception, not fake dungeon replay.
- Hunt #2 Transfer Executioner: Bastion/prisoner transfer branch opens after Rhazek defeat + secured S016 extraction.
- Hunt #3 Archive Judgment Engine: S019 judgment branch denied first pass; S020/S021 authorization-state change opens it after Cresthaven establishment; return to Old City/Archive separately.

## Optional-major unlock windows

1. After Ch3 — Ashfrost Expanse / Ashen Whitehorn → Dawn Shepherd.
2. After Ch5 — Crownfall Redoubt / Crownless Siege Marshal → Oathbound Colossus.
3. After Sixfold Accord — Concordance Vault / Concordance Guardian → Living Revision.
4. After Ch8 — Worldscar Basin / Worldscar Leviathan → Prismatic Leviathan.
5. After Ch10 — Final Archive / Final Archive Arbiter → Sheltering Host.
6. After Final Archive first clear — Worldframe Depths / The Unfinished World → Starfall Engine.

## Dialogue / characterization guardrails

Dialogue has one authored continuity. Natural conversation may use contractions, interruptions, false starts, repetition, partial answers, topic shifts, failed jokes, profanity, boredom, misunderstanding, and silence. Do not write party roll-call dialogue.

Core early voices:
- Cyanis: social/playful/practical wit; not stoic; self-neglect shows when attention turns to him.
- Ilyra: warm/dry, excellent listener not therapist; precise/formal anger.
- Torren: practical/social, talkative about roads/terrain/weather/bows; not permanent terse quips.
- Nimera: engages, challenges wording, self-revises, swears frequently/cleverly; true fury becomes formal and stops swearing.
- Maevra: energetic/social/decisive/argumentative/mischievous/warm; stress can push Commander Solmar mode.
- Mirena: witty/observant/mischievous/politically impatient; public cleaner, private warmer/more profane.
- Lysara: patient/observant/dry funny/affectionate/stubborn/practical; continuity without stagnation and restraint of sovereign ownership.

Protected relationship progression and exact early-chapter wording are recorded in the line-complete scene files under `docs/chapters/dialogue/`, with implementation-facing locks in `CHAPTER_01_COMPLETE.md` through `CHAPTER_03_COMPLETE.md`. Chapter 1 Resource text is additionally protected by exact source-parity validation.

## Affordable 2.5D production baseline

3D owns world scale, spatial continuity, towns, ruins, elevation, traversal, lighting, weather, machinery, crowds, arenas, destruction states, and spatial reveals. 2D/2.5D character presentation and portraits own close performance.

Use reusable poses/portraits/props/camera inserts and authored environment states. Destruction = before/after + VFX, not physics simulation. Water = authored state, not fluid simulation. Crowds = layered groups, not crowd AI. “Checks/tests/aligns/examines” normally use a reusable interaction pose + insert. Warden copied actions use its own mechanical strike/emitter. Character-Life scenes favor tables/maps/food/bandages/reports/cups/chairs/tools/lighting/silence over bespoke animation.

## Finale outcome guardrails

The final antagonist sequence remains Reconstituted Entity → Last Command. Final Severance is the modern six-person solution; all six survive. The Entity and every surviving Entity trace are permanently destroyed. No party member becomes infrastructure or a permanent living anchor. The giant Crest survives damaged/low/stable. Story Primes survive. Vaelkor remains responsible for his own choices and is not retroactively reduced to possession.

## Historical repository rule

The older `zxxdjxxz-del/Diyse` repository is historical prototype material only. Do not use its code or obsolete story/system assumptions as implementation authority.
