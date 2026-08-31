# Implementation Notes — Current Face Terminology

**Status:** ACTIVE IMPLEMENTATION TERMINOLOGY HANDOFF  
**Owning Face authority:** `../../07_CARDS/SIX_FACES.md`

Current player-facing Face names are exactly:
> **Might / Elements / Grace / Perception / Memory / Ruin**

Required replacements:
- `Acuity` → **Perception**
- Face-name `Change` → **Memory**
- older `Resource` Face → **Perception**

## Runtime / data migration rule
Legacy technical IDs may remain temporarily where changing them would break proof fixtures, saves, or migration code, but they must be treated as internal compatibility identifiers only.

Production-facing UI, Card lists, Prime lists, tutorials, glossary text, dialogue, combat rewards, save display names, and inspect/debug text intended for players must use **Perception** and **Memory**.

If stable internal IDs currently encode `acuity`, `change`, or older `resource` Face names:
- do not silently repurpose unrelated ordinary-use `change` identifiers;
- map the Face identity explicitly to the current display label;
- preserve save compatibility when migrating serialized values;
- do not create a new natural Accuracy character stat for Perception.

## Current semantic mapping
Perception:
- Base Hit/application reliability where authored;
- Evasion;
- Critical Hits;
- Fields;
- battlefield reading, position, timing, openings, space control/exploitation.

Memory:
- recall;
- repetition;
- preservation;
- reuse of prior actions/states;
- prior battle state remaining available to influence current resolution where explicitly authored.

This rename does not alter Card count, Prime count, class kits, equipment legality, damage formulas, or save-slot architecture by itself.
