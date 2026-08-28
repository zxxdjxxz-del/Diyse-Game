# Chapters 0–4 — Current HD-2D Production Reconciliation Overlay

**Date:** 2026-08-28  
**Status:** **CURRENT PRODUCTION OVERLAY**  
**Whole-project authority:** **Diyse v2.20 / Audit135**, with later explicit corrections controlling over older production wording  
**Historical parent:** `docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md` / Audit88

This overlay preserves Audit88 as historical production provenance while superseding the portions of that document that conflict with current canon, current Chapter 4 authoring, or the validated runtime.

Audit88 remains useful for stable HD-2D production grammar such as field/battle scale, composition, reusable environment kits, authored state swaps, portrait-led dialogue, random-encounter presentation, cost control, Prime-scale presentation, and Android-conscious production choices. It is **not** current authority for retired element counts, retired Chapter 4 entity names, retired regional terminology, or obsolete Prime-refresh rules.

---

## 1. Current Chapter 4 elemental production rule

Chapter 4 uses exactly four active canonical elements:

- **Fire**
- **Ice**
- **Lightning**
- **Earth**

The reusable elemental presentation runtime therefore exposes exactly four elemental payload families.

**Wind and Water are not active elements.** Do not implement Wind or Water elemental channels, chamber identities, inherited boss traits, enemy states, or player-facing elemental presentation for Chapter 4.

Ordinary physical water, rainfall, wet surfaces, condensation, mist, flowing water, air movement, dust movement, and similar environmental effects remain valid environmental presentation. They do not become Water- or Wind-element channels merely because those visual phenomena exist.

The **Seventh Reaction** is an emergent consequence of the full four-element regulation system. It is **not a seventh element**, does not receive a seventh-element icon/color/channel, and does not expand the elemental runtime beyond four elements.

---

## 2. Current Reaction Annex production terminology

Use these current-facing names:

- **Reaction Annex** — not `Sixfold Annex`
- **Reaction Node** — not `Sixfold Node`
- **Reaction Conduit** — not `Elemental Hexarch`
- **Regulation Crucible** — not `Sixfold Crucible`

Current ordinary Chapter 4 Reaction Annex encounter ecology includes:

- Reaction Node
- Reaction Hound
- Composite Elemental
- Element Mirror
- Annex Crucible Guard

The **Reaction Conduit** remains a harmed living researcher resolved through nonlethal stabilization. Its elemental expression is restricted to the four current elements and their current harmful-status relationships:

- Fire → Burn
- Ice → Freeze
- Lightning → Stun
- Earth → Staggered

Retired Wind tempo and Water Barrier/restoration expressions are removed and are not reassigned to another element.

---

## 3. Current Regulation Crucible production rule

**Form I — Regulation Crucible** uses exactly four elemental chambers:

- Fire
- Ice
- Lightning
- Earth

Exactly **two** chambers are active/targetable at once.

Current intact rotation:

1. Fire / Ice
2. Lightning / Earth
3. Fire / Lightning
4. Ice / Earth

Destroyed chambers remain destroyed. A destroyed scheduled slot stays empty; if both chambers scheduled for a rotation are destroyed, that rotation is core-only.

Form I has no Wind chamber, no Water chamber, no six-chamber architecture, and no three-active-chamber state.

**Form II — The Seventh Reaction** is a genuine fresh-HP/fresh-MP form. It inherits only surviving Fire/Ice/Lightning/Earth traits from Form I. It has no third form.

Because Form II is a genuine fresh-HP boss form, **Prime availability refreshes** at the transition. The retired Audit88 instruction that Prime availability does not refresh is superseded.

Production should continue to use the standard party-left / enemy-right / open-center combat frame and efficient component/state-swap construction where compatible with the current four-chamber design.

---

## 4. Current regional production terminology

Current-facing production prose must use current region names:

- **The Westways** — not `Edgelands`
- **Yahtrenhold** — not `Southhold`, `Crownhold`, or `The Crownhold`
- **The Greyspires** — not `Diysereach` or formal regional `Highlands`
- **Black Host Territory** — not `Blackstone`
- **The Blackspine** — not formal `Black Mountains`
- **Westguard** — not `Westreach` or `Yahtrens Stand`

Accordingly, historical Audit88 headings such as `Edgelands kit` and `Southhold civic family`, and Chapter 4 prose describing Ivorybridge as a Southhold hub, are historical terminology only and must not be reused as current-facing production instructions.

---

## 5. Legacy implementation IDs are not prose authority

Some existing filenames, resource IDs, environment IDs, and implementation keys still contain historical terminology. These may remain temporarily when changing them would require a reference-safe engineering migration.

Examples include, but are not limited to:

- `environment_edgelands_settlement.tres`
- `environment_sixfold_annex.tres`
- `environment_southhold_roadside.tres`
- `CH04_SIXFOLD_ANNEX`
- `CH04_SOUTHHOLD_ROADSIDE`
- `LOC_SIXFOLD_*`
- `LOC_BORDERLANDS_*`

These strings are **legacy technical identifiers**, not current-facing geography or entity names. Do not infer current canon from them, and do not rename them casually as a prose cleanup. Any identifier migration must be reference-safe and validated across all dependent Resources/tests.

---

## 6. Current validated implementation baseline

The current runtime already reflects the four-element conversion:

- `game/presentation/elemental_presentation_runtime.gd` exposes exactly Fire / Ice / Lightning / Earth.
- Wind and Water are rejected as active elemental presentation IDs.
- Seventh Reaction is rejected as an element.
- Chapter 4 presentation validation requires Reaction Conduit / Regulation Crucible current terminology and the fresh-HP Form-II Prime refresh.
- Chapter 4 ordinary encounter formations use the current Reaction Annex enemy names.

The full Godot smoke-validation workflow passed at commit:

`419d41dc2c6acf79eb5c6826d3aeadf1e78fa6cb`

Workflow run:

`33144308306`

That green baseline includes Chapters 0–4 HD-2D validation, encounter/runtime checks, combat/Card/Prime validation, dialogue source/resource parity and continuity through Chapter 3, rendered field proof, and artifact upload.

---

## 7. Authority resolution

For current implementation, read the following in this order when older wording conflicts:

1. `README.md`
2. `docs/ACTIVE_CANON.md`
3. `docs/IMPLEMENTATION_STATUS.md`
4. latest controlling canon audits, including Audit121 and compatible later audits through Audit135
5. `docs/chapters/dialogue/chapter_04/FOUR_ELEMENT_REWORK_2026-08-27.md`
6. this current production overlay
7. historical Audit88 production document for compatible non-superseded HD-2D guidance only

**Result:** Audit88 remains historical provenance; its six-element Chapter 4 model, retired Chapter 4 names, retired regional names, six-chamber/three-active Crucible instructions, and no-Prime-refresh Form-II rule are superseded and must not be implemented.