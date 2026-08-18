# Chapter 2 — The Drowned Oath — COMPLETE

**Whole-project authority:** Diyse Clean Active Complete Master Canon **v1.64 / Audit79**  
**Chapter line-complete checkpoint:** **Audit78**, inherited into v1.64  
**Closed set:** S012–S016 + C06–C07  
**Runtime dialogue Resource status:** **IMPLEMENTED / source-parity and chapter-continuity validation locked**.

The exact approved Chapter 2 dialogue lives in `docs/chapters/dialogue/chapter_02/`. The production translation lives in `game/content/dialogue/chapter_02/`. Do not reconstruct it from older summary notes or rewrite it during follow-on implementation.

## Controlling scene files

- [S012 — Dunmere / Poisoned Waterworks](dialogue/chapter_02/S012.md)
- [S013 — Sunken Archive / Archive Leviathan](dialogue/chapter_02/S013.md)
- [S014 — Prisoner Galleries](dialogue/chapter_02/S014.md)
- [S015 — Red Transfer Bastion / Commander Rhazek](dialogue/chapter_02/S015.md)
- [S016 — Extraction Causeway](dialogue/chapter_02/S016.md)
- [C06 — Three People Who Know Each Other Now](dialogue/chapter_02/C06.md)
- [C07 — Bad Dreams, No Questions](dialogue/chapter_02/C07.md)

## Production Resource set

- `game/content/dialogue/chapter_02/S012.tres`
- `game/content/dialogue/chapter_02/S013.tres`
- `game/content/dialogue/chapter_02/S014.tres`
- `game/content/dialogue/chapter_02/S015.tres`
- `game/content/dialogue/chapter_02/S016.tres`
- `game/content/dialogue/chapter_02/C06.tres`
- `game/content/dialogue/chapter_02/C07.tres`
- `game/content/dialogue/chapter_02/chapter_02_dialogue_registry.tres`

Deterministic translation/validation authority:
- `tools/dialogue/compile_chapter_02.py` reproduces the `.tres` translation from the locked Markdown source without rewriting spoken text.
- `tests/dialogue/validate_chapter_02_resources.gd` enforces exact source-to-Resource speaker/text order and schema/metadata validity.
- `tests/dialogue/validate_chapter_02_continuity.gd` enforces the Chapter 2 continuity, prisoner-agency, Rhazek-limit, encounter-count, relationship, knowledge-firewall, Character-Life, and durable-handoff locks below.
- The unusual source forms remain explicit implementation metadata rather than rewritten prose: `PRISONER WOMAN — THROUGH DOOR` remains an offscreen/through-door delivery, and C06's `ILYRA / TORREN: No.` remains a simultaneous two-speaker line.

## Hard continuity / implementation locks

- Dunmere remains a functioning community under pressure. S012 establishes deliberate contamination and shuts only the unsafe lower feed without falsely declaring all remaining water safe.
- S013's **thirty-one transfers** are transfer records, not a prisoner headcount. Do not equate the number with the people later found in the galleries.
- Memory Scribe behavior keys off an **eligible action after it actually completes**. It does not read unexecuted menu selections or copy actor body choreography.
- Archive Leviathan uses one HP bar with its authored same-bar state change. The `Same one? / Yes.` exchange is conditional on a Recorded Pattern actually persisting through that transition.
- Prisoners in S014 are differentiated adults with agency. Ilyra asks before care; people may accept or refuse. The prisoners themselves retain control of the defensible safe-room bar.
- The only Chapter 2 Torren/Maevra address breach is Maevra's involuntary **“Torren!”**, immediately corrected to **“Harth.”** Nobody comments on it. The first deliberate `Maevra` remains Chapter 3 H02.
- Commander Rhazek is competent, accountable, non-possessed, ideologically intact, and owns the transfer operation and his choices.
- Rhazek's Chapter 2 boss state is **Bastion Master**, one HP bar with finite support and a same-bar Ruin/armor escalation. He survives and withdraws. Later Rhazek forms are not imported backward.
- S016 contains exactly **one mandatory authored combat encounter: Hold the Junction**. There is no second mandatory rearguard battle and no combat after the final extraction threshold.
- The missing-brother thread remains unresolved.
- Hunt #2 — **Transfer Executioner** becomes accessible after the Bastion/branch state change and remains optional/returnable.

## Character-Life locks

C06 and C07 unlock after S016 and are order-independent.

- **C06:** saved seat, ordinary gear repair, shorthand, teasing, mutual work-stopping care, and comfortable silence. No lore/Prime payload or relationship speech.
- **C07:** Audit78 Rewrite Draft 2 controls. The earlier protected C07 line set is retired. The approved callback is **wet sleeves**. Torren sometimes smokes weed late at night to relax/focus; the scene does not frame this as impairment or vice. He lights the blunt from existing low coals—**no modern lighter**. No dream visualization, confession, forced disclosure, or therapy conversation.

## Knowledge / production locks

- No Chapter 3 Prime, Last Sentinel, Nimera-party, Old City/Suppressed Archive, Sixfold Accord, giant buried Crest, integrated Underground Crest Network, or later relationship knowledge leaks backward into Chapter 2.
- Bosses/constructs do not create Cards; victory/access may gate recovery of pre-existing Ancient Cards.
- Use authored water states rather than fluid simulation, prepared machinery/gate changes rather than physics destruction, layered/limited evacuee sprites rather than crowd AI, and reusable treatment/escort/interaction poses.

## Follow-on implementation rule

Treat the validated Chapter 2 Resource set as the dialogue baseline. Follow-on work may wire world triggers, encounter consumers, state changes, portraits, animation/pose cues, maps, and other production systems, but it may not rewrite approved dialogue, alter prisoner agency, change encounter counts/handoffs, advance Rhazek beyond his Chapter 2 same-bar limit, move the Torren/Maevra address milestone, or change C06/C07 availability.
