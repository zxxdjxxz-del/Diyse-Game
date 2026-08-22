# Chapter 1 — Audit105 Acuity Bounded Correction

**Authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.90 / Audit105**  
**Date:** August 22, 2026  
**Status:** **LOCKED / CONTROLLING OVERLAY** for the bounded Chapter 1 corrections below.

This file exists to keep the line-complete Audit79 Chapter 1 transcript locally reconciled with Audit105 without reopening unrelated approved dialogue or staging.

## S008 — Hollow Watch / What Woke Up

Only the first-clear reward block is changed:

- `BASTION RESERVE acquired.` → **`FAULTLINE SIGHT acquired.`**
- `No character suddenly explains Resource.` → **`No character suddenly explains Acuity.`**

All other S008 dialogue, staging, encounter architecture, knowledge firewall, and scene outcome remain inherited and closed.

## S011 — Wayfinder Junction / Six Ways Through

Only the Face terminology/production wording is changed:

- `TORREN: Resource here.` → **`TORREN: Acuity here.`**
- `Resource appears around route branches...` → **`Acuity appears around route branches...`**
- wording that assumes dedicated `Face symbols` is superseded by neutral **Face markings / Face notation** language;
- the formal Six Faces are **Might, Elements, Grace, Acuity, Change, Ruin**.

All other S011 dialogue, staging, Wayfinder discovery logic, Hunt #1 unlock, physical-map-copy continuity, and knowledge firewall remain inherited and closed.

## Runtime Resource reconciliation

The generated Godot dialogue Resources:

- `game/content/dialogue/chapter_01/S008.tres`
- `game/content/dialogue/chapter_01/S011.tres`

were produced before Audit105 and may still contain the superseded strings above in staging metadata. They must be regenerated or synchronously patched from the controlling Markdown + this overlay before the next Chapter 1 source-parity/runtime closure pass.

This is a terminology/reward reconciliation only. It does **not** authorize unrelated dialogue rewrites.
