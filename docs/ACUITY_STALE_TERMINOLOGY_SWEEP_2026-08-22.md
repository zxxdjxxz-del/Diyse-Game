# Diyse — Audit105 Acuity Stale-Terminology Sweep

**Date:** August 22, 2026  
**Authority:** `docs/canon/AUDIT105_ACUITY_FACE_STORY_PRIME_AND_RESOURCE_RECONCILIATION_LOCK.md`  
**Purpose:** Track physical cleanup of current-facing source/runtime files after the Resource → Acuity canon promotion.

## Sweep rule

Do **not** rewrite historical canon snapshots merely because they preserve superseded terminology. Older Audit files are archival authority records and remain valid as history; Audit105 controls conflicts.

Only current-facing authoring, runtime, tracker, and implementation files should be physically reconciled.

Ordinary lowercase English/Godot uses of `resource` / `Resource` are not Face terminology and must not be blanket-replaced.

## Confirmed current-facing stale references

### Chapter 1 source — S008
Path: `docs/chapters/dialogue/chapter_01/S008.md`

Required bounded replacements:
- `BASTION RESERVE acquired.` → `FAULTLINE SIGHT acquired.`
- `No character suddenly explains Resource.` → `No character suddenly explains Acuity.`

No other S008 wording is reopened.

### Chapter 1 source — S011
Path: `docs/chapters/dialogue/chapter_01/S011.md`

Required bounded replacements:
- spoken `TORREN: Resource here.` → `TORREN: Acuity here.`
- `Resource appears around route branches...` → `Acuity appears around route branches...`
- `Face symbols` / equivalent dedicated-symbol wording → neutral `Face markings` / `Face notation` wording.

No other S011 wording is reopened.

### Chapter 1 runtime — S008
Path: `game/content/dialogue/chapter_01/S008.tres`

Generated staging metadata still carries the superseded Bastion Reserve / Resource wording. Regenerate or synchronously patch from the controlling Markdown/Audit105 overlay.

### Chapter 1 runtime — S011
Path: `game/content/dialogue/chapter_01/S011.tres`

Generated runtime data still carries:
- spoken `Resource here.`;
- staging references to `Face symbols`;
- the old Resource route-branch wording.

Because the spoken line changes, the production Resource and any spoken-sequence hash/source-parity expectations must be regenerated/revalidated together rather than hand-diverging source and runtime.

### Routeweaver current working spec
Path: `docs/TORREN_NIMERA_SUBCLASS_WORKING_SPEC.md`

Current visual wording says `Torren's Resource-gold / amber route lines remain dominant.`

Audit105 correction:
- use **Torren's gold / amber route lines** as personal visual language without assigning Routeweaver to the retired Resource Face;
- preserve **Change-fuchsia** at junctions, Card-linked nodes, and Conduit routing points;
- Routeweaver remains a **Change Face class**, not an Acuity class.

## Already reconciled during this sweep

`docs/chapters/CHAPTER_01_COMPLETE.md` now:
- points to v1.90 / Audit105 as whole-project authority;
- records the Audit105 bounded Chapter 1 correction;
- uses `Face markings` rather than `Face symbols` in the Chapter 1 continuity summary.

Local Chapter 1 correction overlay added:
- `docs/chapters/dialogue/chapter_01/AUDIT105_ACUITY_BOUNDED_CORRECTION.md`

## Runtime/data status

No production implementation for the Chapter 5 Chosen Course / Last Cartographer correction, Mercyfallen Behemoth → Predicted Impact reward, or Final Archive Arbiter → Parallax Host + Decisive Interval reward is currently treated as complete merely because Audit105 canonized those assignments.

Those future runtime data entries must be authored directly with Acuity terminology and must not first reproduce the retired Resource versions.

## Remaining sweep work

- physically synchronize S008 Markdown and runtime staging metadata;
- physically synchronize S011 Markdown and runtime Resource together, then rerun Chapter 1 source-parity/continuity validation;
- remove the `Resource-gold` Face attribution from the Routeweaver working spec while preserving Torren's gold/amber personal visual language and Change-fuchsia subclass signal;
- inspect any later-added Hunt/Card/Prime implementation data for retired IDs/names before production promotion;
- do not edit archival Audit snapshots solely to erase historical terminology.
