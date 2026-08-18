# Chapter 1 — Brackenwall and the Wayfinder — COMPLETE

**Whole-project authority:** Diyse Clean Active Complete Master Canon **v1.64 / Audit79**  
**Chapter line-complete checkpoint:** **Audit79**  
**Closed set:** S007–S011 + C03–C05  
**Runtime status:** Story/dialogue/continuity/relationship/affordable-2.5D authority CLOSED; **production dialogue Resource conversion is COMPLETE and exact source-parity + whole-chapter continuity validated.**

The exact approved Chapter 1 dialogue lives in `docs/chapters/dialogue/chapter_01/`. Its production `DiyseDialogueSceneDefinition` Resource set lives in `game/content/dialogue/chapter_01/`. Do not reconstruct or rewrite the chapter from older summaries or recovered fragments.

## Controlling scene files

- [S007 — Brackenwall / Protocol](dialogue/chapter_01/S007.md)
- [S008 — Hollow Watch / What Woke Up](dialogue/chapter_01/S008.md)
- [S009 — Greenhollow / What the Map Has Wrong](dialogue/chapter_01/S009.md)
- [S010 — Briar Passage / The Route I Would Take](dialogue/chapter_01/S010.md)
- [S011 — Wayfinder Junction / Six Ways Through](dialogue/chapter_01/S011.md)
- [C03 — Torren's Version of Dinner](dialogue/chapter_01/C03.md)
- [C04 — What the Map Says](dialogue/chapter_01/C04.md)
- [C05 — Two Professionals Complaining About Cyanis](dialogue/chapter_01/C05.md)

## Production Resource checkpoint

Live Chapter 1 Resource set:
- `game/content/dialogue/chapter_01/S007.tres`
- `S008.tres`
- `S009.tres`
- `S010.tres`
- `S011.tres`
- `C03.tres`
- `C04.tres`
- `C05.tres`
- `chapter_01_dialogue_registry.tres`

Validation authority:
- `tests/dialogue/validate_chapter_01_resources.gd` checks schema, metadata, expected beat counts, and **every spoken speaker/text pair against the controlling Markdown source in exact order**.
- `tests/dialogue/validate_chapter_01_continuity.gd` checks party handoffs, optional-scene gates, knowledge firewall, C04 Audit79 final wording, C03 smoke/fire staging, and Torren/Maevra address progression.
- These gates are part of the permanent Godot Smoke workflow.

## Hard continuity / implementation locks

- Chapter opens with Cyanis + Ilyra. Maevra becomes a **temporary guest** in S007.
- Torren accompanies the Greenhollow rescue first as a non-commandable route specialist and becomes a **permanent War Archer only after the local problem is resolved in S009**.
- Torren/Maevra remain **Harth / Solmar** throughout Chapter 1. Edda may naturally call Maevra **Mae**; this does not advance Torren/Maevra address progression.
- S010 preserves Cyanis's authored refusal to destroy the civilian flood crossing. Maevra records the refusal and the group owns the harder tactical problem together.
- Wayfinder Junction is an **outdoor physical Ancient Diysean cartographic monument/crossroads**, not a station, terminal, hidden Network interface, or control building.
- The Six Faces are common Yahtrean knowledge. Chapter 1 reveals only that Ancient Diyseans used familiar Face symbols inside a technical cartographic grammar the party does not yet understand.
- The party leaves S011 with practical physical copies/rubbings of the Wayfinder material. Those copies persist for later comparison.
- The mystery Card remains unidentified as a Prime. No Last Sentinel, Ruby-response, giant buried Crest, or integrated Underground Crest Network reveal occurs here.
- Hunt #1 — **Cistern Devourer** becomes accessible from knowledge of the old cistern branch after S011 and remains optional/returnable.

## Character-Life locks

C03, C04, and C05 unlock after S011 and are independently available.

- **C03:** ordinary dinner; terrible bread is not Torren's; Cyanis eats two bowls; Torren's `Hot / Enough / Safe / Cheap` road-food logic; comfortable silence; Torren may smoke from existing coals as ordinary background behavior.
- **C04:** Audit79's line-complete version is controlling. The misunderstanding is **Cyanis: “Old whore.” / Torren: “Bitch.”** The older `Whore/Shore` recovery reconstruction is superseded and must not be restored.
- **C05:** Ilyra/Maevra friendship grows through reciprocal self-neglect, dry humor, and work. Cyanis catches their hypocrisy; all three ultimately stop working and go eat.

## Combat / affordable-2.5D locks

- Hollow Watch Castellan: one HP bar, Fortress→Walking same-bar state change, finite supports stay destroyed.
- Briarhide Stalker: nonlethal authored encounter; remove/disable the Black Host irritant and allow the frightened animal to retreat.
- Traversal spaces are moderate in size and support several likely random encounters where appropriate, with safe authored pockets suppressing interruption.
- Prefer reusable environment kits, portraits, poses, prop states, lighting, simple route/door changes, and short authored buffers over bespoke cinematic animation.

## Runtime rule going forward

The Chapter 1 Resource conversion is now an accepted implementation baseline. Future work may wire approved portrait assets, trigger/world-state consumers, encounter handoffs, and presentation executors, but it may not rewrite approved dialogue, move relationship milestones, leak future knowledge, change party-state transitions, or alter scene outcomes. Exact wording remains protected by the source-parity validator.
