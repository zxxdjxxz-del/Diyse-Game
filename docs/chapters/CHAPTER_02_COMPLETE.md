# Chapter 2 — The Drowned Oath — COMPLETE

**Whole-project authority:** Diyse Clean Active Complete Master Canon **v1.64 / Audit79**  
**Chapter line-complete checkpoint:** **Audit78**, inherited into v1.64  
**Closed set:** S012–S016 + C06–C07  
**Runtime status:** Story/dialogue/continuity/relationship/affordable-2.5D authority CLOSED; Godot Resource conversion/validation still pending.

The exact approved Chapter 2 dialogue now lives in `docs/chapters/dialogue/chapter_02/`. Do not reconstruct it from older summary notes when the line-complete scene source exists.

## Controlling scene files

- [S012 — Dunmere / Poisoned Waterworks](dialogue/chapter_02/S012.md)
- [S013 — Sunken Archive / Archive Leviathan](dialogue/chapter_02/S013.md)
- [S014 — Prisoner Galleries](dialogue/chapter_02/S014.md)
- [S015 — Red Transfer Bastion / Commander Rhazek](dialogue/chapter_02/S015.md)
- [S016 — Extraction Causeway](dialogue/chapter_02/S016.md)
- [C06 — Three People Who Know Each Other Now](dialogue/chapter_02/C06.md)
- [C07 — Bad Dreams, No Questions](dialogue/chapter_02/C07.md)

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

## Runtime conversion rule

Convert the closed scenes into the existing stable-ID `DiyseDialogueSceneDefinition` Resource schema. Implementation may normalize IDs/cues/portrait references and make bounded technical staging adjustments, but must preserve exact approved dialogue, prisoner agency, encounter counts/handoffs, Rhazek's same-bar limit, the relationship-address firewall, and C06/C07 availability.
