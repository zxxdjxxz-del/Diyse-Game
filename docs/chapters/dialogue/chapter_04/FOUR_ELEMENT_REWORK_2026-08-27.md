# Chapter 4 — Four-Element Script Reconciliation

**Date:** 2026-08-27  
**Status:** **CURRENT CHAPTER-LOCAL RECONCILIATION AUTHORITY**  
**Whole-project authority:** **v2.20 / Audit135**, with **Audit121** controlling the Chapter 4 four-element conversion and compatible later audits controlling later combat/stat corrections.  
**Approved working source:** `Diyse_Chapter_4_Four_Element_Rework_FULL_HANDOFF_2026-08-27.md` from the accepted design pass.

This note records the synchronization of the approved Chapter 4 four-element rework into the live S022–S026 production-authoring scripts.

Where older Chapter 4 acceptance-log entries, Audit88 production language, or old script revisions contain six-element / six-channel language, this reconciliation plus Audit121 and compatible later authority controls.

## Global Chapter 4 elemental rule

Exactly four standard elements participate in the Chapter 4 research/regulation framework:
- Fire
- Ice
- Lightning
- Earth

Wind and Water are removed from the elemental model. Ordinary physical water, watercourses, rain, condensation, and similar environmental staging remain ordinary geography/weather and are not Water-element channels.

The model has exactly six pairwise relationships among the four elements. The **Seventh Reaction** is emergent full-system behavior when all four interact together; it is not a seventh element or a new player-facing reaction system.

## Script synchronization

### S022 — Brilliant Answer
- `Sixfold Annex` → **Reaction Annex**.
- reduced model uses four elemental inputs and six paired returns.
- B018 prediction uses the approved six-pair sequence.
- B019 confirms six stable pair relationships and a return outside the modeled loop.
- physical watercourse/rain staging remains ordinary environment, not elemental channels.

### S023 — Cost Outside Equation
- location is **Reaction Annex**.
- six stable values are the six pair returns among Fire/Ice/Lightning/Earth.
- ordinary hostile ecology uses **Reaction Node**, not Sixfold Node.
- `Elemental Hexarch` → **Reaction Conduit**.
- Reaction Conduit has four expressions only: Fire/Burn, Ice/Freeze, Lightning/Stun, Earth/Staggered.
- old Wind tempo and Water Barrier/restoration expressions are removed and not reassigned.
- physical condensation remains non-elemental environment.

### S024 — Seventh Reaction
- exactly four elemental chambers.
- model consists of six pairwise relationships.
- `Sixfold Crucible` → **Regulation Crucible**.
- exactly two of four chambers active/targetable at once.
- intact rotation: Fire/Ice → Lightning/Earth → Fire/Lightning → Ice/Earth.
- destroyed chamber slots remain empty; if both scheduled chambers are destroyed, that rotation is core-only.
- Form II is a genuine fresh-HP body and therefore refreshes Prime availability under the current global rule.
- only surviving Fire/Ice/Lightning/Earth chamber traits carry forward.
- no third form.
- no replacement Form-II command list is invented by this conversion.
- Cinder Judgment's mandatory Chapter 4 source is the Reaction Annex/regulation-system protected cache, not a Crucible first-clear reward.

### S025 — Responsibility Without Humiliation
- player-control location is **Reaction Annex**.
- model language is six pairwise predictions / six paired-return figures.
- exposure shutdown applies to **all multi-element exposure**.
- six-pair interaction diagram replaces six-channel diagram wording.

### S026 — A Place Where Being Wrong Is Survivable
- public board preserves the **four-element / six-pair model**.
- `MULTI-ELEMENT EXPOSURE` replaces `MULTI-CHANNEL EXPOSURE`.
- Vaelira's notebook contains a larger four-element / six-pair interaction diagram.
- ordinary time references such as `six months of work` are unchanged.

## Production supersession

The current implementation-facing HD-2D reconciliation is:

`docs/production/HD2D_CHAPTERS_00_04_CURRENT_RECONCILIATION_2026-08-28.md`

That overlay preserves Audit88 as historical provenance while superseding its retired Chapter 4 production instructions, including:

- six-element presentation/runtime requirements;
- Wind and Water elemental payload families;
- Elemental Hexarch / Sixfold Crucible current-facing names;
- six-chamber / three-active Crucible construction;
- the obsolete rule that genuine fresh-HP Form II does not refresh Prime availability;
- retired regional production terminology such as Edgelands and Southhold.

Legacy internal filenames/IDs may retain older strings until a reference-safe engineering migration. They are not current-facing canon or production terminology.

## Preservation rule

Dialogue/staging not explicitly changed by the accepted four-element handoff remains previously accepted text. This was a surgical conversion, not a general rewrite.

## Runtime synchronization

The Markdown files S022–S026 are the current canon/production-authoring sources. Matching Godot dialogue/presentation resources must mirror these revisions; any remaining runtime six-element strings are implementation drift, not canon.

As of the current validated baseline, `game/presentation/elemental_presentation_runtime.gd` exposes exactly Fire/Ice/Lightning/Earth and the Chapter 4 presentation validator enforces the current Reaction Conduit / Regulation Crucible / fresh-HP Prime-refresh rules.