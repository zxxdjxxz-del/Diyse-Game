# Diyse — Audit105 Acuity Stale-Terminology Sweep

**Date:** August 22, 2026  
**Authority:** `docs/canon/AUDIT105_ACUITY_FACE_STORY_PRIME_AND_RESOURCE_RECONCILIATION_LOCK.md`  
**Purpose:** Track physical cleanup of current-facing source/runtime files after the Resource → Acuity canon promotion.

## Sweep rule

Do **not** rewrite historical canon snapshots merely because they preserve superseded terminology. Older Audit files are archival authority records and remain valid as history; Audit105 controls conflicts.

Only current-facing authoring, runtime, tracker, and implementation files should be physically reconciled.

Ordinary lowercase English/Godot uses of `resource` / `Resource` are not Face terminology and must not be blanket-replaced.

## Completed current-facing reconciliation

### Chapter 1 source — S008
Path: `docs/chapters/dialogue/chapter_01/S008.md`

Applied:
- `BASTION RESERVE acquired.` → `FAULTLINE SIGHT acquired.`
- `No character suddenly explains Resource.` → `No character suddenly explains Acuity.`
- whole-project authority header advanced to v1.90 / Audit105 while retaining the Audit79 line-complete chapter checkpoint.

No other S008 wording was reopened.

### Chapter 1 source — S011
Path: `docs/chapters/dialogue/chapter_01/S011.md`

Applied:
- spoken `TORREN: Resource here.` → `TORREN: Acuity here.`
- `Resource appears around route branches...` → `Acuity appears around route branches...`
- dedicated-symbol wording replaced with neutral **Face markings / notation** wording;
- whole-project authority header advanced to v1.90 / Audit105 while retaining the Audit79 line-complete chapter checkpoint.

No other S011 story/dialogue outcome was reopened.

### Chapter 1 runtime — S008
Path: `game/content/dialogue/chapter_01/S008.tres`

Synchronized with the updated source:
- first-clear staging now records **FAULTLINE SIGHT**;
- stale Face-system `Resource` explanation wording is removed;
- runtime authoring notes now identify v1.90 / Audit105 while preserving the Audit79 line-complete checkpoint.

S008 has no changed spoken line, so its spoken-line sequence remains unchanged.

### Chapter 1 runtime — S011
Path: `game/content/dialogue/chapter_01/S011.tres`

Synchronized with the updated source:
- spoken Torren line is now **`Acuity here.`**;
- route-branch staging uses **Acuity**;
- dedicated Face-symbol wording is replaced by **Face markings**;
- generic Wayfinder description uses neutral **markings** language;
- runtime authoring notes now identify v1.90 / Audit105 while preserving the Audit79 line-complete checkpoint.

### Chapter 1 validation
Path: `tests/dialogue/validate_chapter_01_continuity.gd`

Updated to:
- require **`Acuity here.`** in S011;
- explicitly reject regression to **`Resource here.`**;
- preserve all existing knowledge-firewall, party, durable-handoff, and relationship checks.

`tests/dialogue/validate_chapter_01_resources.gd` already derives exact spoken parity from the controlling Markdown sources, so no special Acuity exception was added; source and runtime are expected to match directly.

### Chapter 1 compiler
Path: `tools/dialogue/compile_chapter_01.py`

Updated so future regeneration records **v1.90 / Audit105** and the inherited Audit79 line-complete checkpoint rather than reintroducing the old authority note. The compiler still takes current Markdown as the wording/staging source, so regenerated S008/S011 retain the Acuity correction.

### Chapter 1 completion summary
Path: `docs/chapters/CHAPTER_01_COMPLETE.md`

Now:
- points to v1.90 / Audit105 as whole-project authority;
- records the bounded Chapter 1 Acuity correction;
- uses `Face markings` rather than `Face symbols` in the Chapter 1 continuity summary.

Local correction overlay:
- `docs/chapters/dialogue/chapter_01/AUDIT105_ACUITY_BOUNDED_CORRECTION.md`

### Routeweaver current working spec
Path: `docs/TORREN_NIMERA_SUBCLASS_WORKING_SPEC.md`

Reconciled:
- retired `Resource-gold` Face attribution removed;
- Torren's **gold / amber** route lines are explicitly personal presentation language, not Face assignment;
- **Change-fuchsia** remains the subclass signal at junctions, Card-linked nodes, and Conduit routing points;
- Routeweaver remains a **Change Face class**, not an Acuity class.

## Runtime/data status beyond Chapter 1

No production implementation for the Chapter 5 **Chosen Course / Last Cartographer** correction, **Mercyfallen Behemoth → Predicted Impact** reward, or **Final Archive Arbiter → Parallax Host + Decisive Interval** reward is treated as complete merely because Audit105 canonized those assignments.

Those future runtime data entries must be authored directly with Acuity terminology and must not first reproduce the retired Resource versions.

## Remaining sweep work

- inspect any later-added Chapter 5/Hunt/Card/Prime implementation data for retired IDs/names before production promotion;
- reconcile future equipment/item files through the separate Torren/Acuity equipment audit rather than duplicating that work here;
- keep Last Cartographer visual design deferred until the dedicated Prime visual pass;
- do not edit archival Audit snapshots solely to erase historical terminology.

The immediate Chapter 1 source/runtime/validator/compiler synchronization and Routeweaver visual-label cleanup are **COMPLETE** under Audit105.
