# Diyse — Character Portrait Derivative Pipeline

**Status:** ACTIVE PRODUCTION PIPELINE  
**Identity authority:** `README.md` in this folder + `asset_sources/characters/current/`  
**Runtime ID architecture:** `game/dialogue/dialogue_portrait_registry.gd`  
**Dialogue presentation authority:** `docs/13_UI_AND_IMPLEMENTATION/DIALOGUE_UI.md`

## Purpose

This pipeline defines how approved B00/current character masters become downstream dialogue and UI portrait assets without creating a second visual identity source.

The current repository master image is never a disposable input and is never overwritten by a crop, repaint, expression edit, resize, transparency pass, runtime export, or UI treatment.

## Authority chain

For every portrait derivative:

1. latest explicitly approved character revision;
2. current source master in `asset_sources/characters/current/`;
3. matching `*_CURRENT_VISUAL_LOCK.md`;
4. `DIYSE_VISUAL_STYLE_CANON.md`;
5. this derivative pipeline;
6. purpose-specific derivative/export metadata.

A derivative may vary expression, pose/framing, crop, and production simplification only as needed for its approved purpose. It does not gain authority over the source master.

## Current source set

Stable character IDs used by production data:
- `cyanis`
- `ilyra`
- `torren`
- `nimera`
- `vaelira`
- `seyrik`
- `maevra`
- `kessara`

Current source masters:
- `asset_sources/characters/current/cyanis.jpg`
- `asset_sources/characters/current/ilyra.jpg`
- `asset_sources/characters/current/torren.jpg`
- `asset_sources/characters/current/nimera.jpg`
- `asset_sources/characters/current/vaelira.jpg`
- `asset_sources/characters/current/seyrik.jpg`
- `asset_sources/characters/current/maevra.jpg`
- `asset_sources/characters/current/kessara.png`

## Derivative lanes

### Dialogue portrait / bust
Primary acting asset for story dialogue.

Requirements:
- preserve exact facial identity, age read, eye color, hair silhouette, costume identity, and signature upper-body equipment visible in the source design;
- expressions may change without changing facial structure or redesigning the character;
- composition must remain readable when displayed as a large portrait at approximately 35–45% of screen height where practical;
- support left/right presentation without silently mirroring identity-critical equipment placement;
- transparent-background export is preferred for final production presentation when the approved composition and runtime test support it;
- preserve the mature seinen / chaotic-variable-line / graphic cel-informed style at portrait scale.

Production scene data must continue to reference **character ID + expression ID**, not an image path.

### Menu / status / party UI portrait
Recognition-first derivative for menus and character information surfaces.

Requirements:
- preserve face and hair read first;
- retain enough costume/silhouette information to distinguish the character immediately;
- crop must not remove the visual anchor needed to identify the character;
- simplify microdetail where the actual UI size cannot resolve it;
- no alternate redesign simply to fit a frame.

Exact UI crop, pixel dimensions, and frame treatment remain downstream of the approved UI layout and should not be invented in this file.

### Later field / battle derivatives
Diyse's active B00 runtime direction uses rigged 3D field/battle characters. Any future 2D field/battle derivative is optional and subordinate to the same current master.

Do not treat dialogue/UI derivative production as permission to create or lock a second battle/field identity.

## Expression IDs and filenames

The existing proof architecture already uses stable semantic expression IDs such as `neutral`, `amused`, and `dry`, while its placeholder files follow `<character_id>_<expression_id>.<ext>`.

Production rule:
- preserve semantic expression IDs in dialogue data;
- use lowercase stable IDs;
- prefer `<character_id>_<expression_id>.png` for approved raster portrait exports unless a later asset-pipeline requirement needs a different container;
- filenames are implementation locators, not identity authority;
- do not rename an expression merely to describe a particular drawing more poetically.

New expression IDs should be added only when authored dialogue actually needs a distinct acting state. Do not create a large speculative expression library before scene demand exists.

## Left/right handling

Do not solve left/right portrait presentation by destructively flipping the authoritative master.

If a portrait is mirrored at runtime or exported as a side-specific variant:
- confirm that asymmetric armor, props, scars, hair details, weapon placement, insignia, or other identity-critical details are not made canonically wrong;
- use an authored side-specific derivative when mirroring would break identity;
- record the orientation in derivative metadata.

## Derivative metadata

Every approved derivative should be traceable to:
- `character_id`;
- `expression_id` or UI variant ID;
- derivative purpose;
- source master path;
- source fingerprint available at production time;
- output filename/path;
- output dimensions;
- crop/framing description;
- transparency/background treatment;
- orientation or side-specific requirement;
- approval/status note.

For the seven masters with verified SHA-256 fingerprints, use those fingerprints. For Kessara, use the current Git blob identity until a SHA-256 and exact dimensions are independently verified; do not fabricate them.

## Source-master safety

Never:
- overwrite or resave `asset_sources/characters/current/*` as part of derivative production;
- destructively crop a master in place;
- patch an obsolete character render and call it a derivative of the current master;
- let a derivative become the source for a later identity redraw when the current master exists;
- use another character's generated image as subject/identity reference;
- promote proof SVG placeholders to production art;
- hardcode final dialogue scene files directly to portrait image paths when registry indirection exists.

## Review gate

A portrait derivative passes only when:
- the character is immediately recognizable as the exact current master;
- expression reads without facial-identity drift;
- age and body/face maturity remain correct;
- eye color, hair, costume and visible equipment are correct;
- line/value/material treatment remains in Diyse style;
- no patch artifacts, random dots, accidental symbols or anatomy errors are present;
- the crop works at the actual target UI scale;
- orientation does not corrupt asymmetric identity details;
- provenance metadata points back to the current master.

## Runtime handoff

The production dialogue registry should eventually map stable `character_id` + `expression_id` pairs to approved derivative textures. Until those textures exist, the current proof registry and `game/characters/placeholders/portraits/` remain proof-only stand-ins.

Do not point the dialogue runtime directly at the full B00 master JPEG/PNG as a shortcut. The final portrait should be an approved derivative with its own framing, transparency and runtime validation.
