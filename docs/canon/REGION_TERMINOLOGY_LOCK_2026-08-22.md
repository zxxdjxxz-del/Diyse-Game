# Diyse — Yahtrea Region Terminology Lock

**Date:** August 22, 2026

This file records a newer explicit canon correction to Yahtrea's three modern regional names. It supersedes the prior regional labels wherever they appear in compatible older canon, without changing the underlying geography, settlements, landmarks, roads, regional identities, story routing, or map placement.

## Locked modern regional names

- **The Greyspires** — northern mountain region. Replaces **Diysereach**.
- **The Westways** — western region. Replaces **Edgelands**.
- **The Crownhold** — capital / royal-core region, including Caelora. Replaces **Southhold**.

## Preservation rule

This is a terminology-only regional correction unless a later explicit canon decision states otherwise.

- Existing settlement names remain unchanged.
- Existing landmark names remain unchanged.
- Existing roads and connections remain unchanged.
- Existing geography and exact approved map placement remain unchanged.
- Existing regional cultural, musical, traversal, environmental, and story identities remain inherited.
- The Black Mountains remain west outside Yahtrea in Black Host territory.

## Usage rule

Use **The Greyspires**, **The Westways**, and **The Crownhold** as the authoritative current regional names in new canon, scripts, dialogue, quest text, UI, codex text, map labels, and implementation-facing documentation.

When older canon uses **Diysereach**, **Edgelands**, or **Southhold** as regional names, interpret those references respectively as **The Greyspires**, **The Westways**, and **The Crownhold** unless the text is explicitly discussing historical/deprecated terminology.

## Chapters 0–4 locked-dialogue propagation

A complete terminology audit was performed across the locked Chapter 0–4 authored dialogue sources, including mandatory scenes, optional character/life scenes, Hunt dialogue, and the corresponding runtime dialogue resources where applicable.

The dialogue locks remain fully intact. Only obsolete regional proper nouns and directly attached staging/reference wording were changed; no character voice, scene beat, delivery, narrative logic, quest logic, combat logic, or unrelated staging was reopened.

Exact changes:

- **Chapter 0 — S001 staging:** `Borderlands road` → `Westways road`.
- **Chapter 3 — S019_B016 spoken dialogue:** `Edgelands reports` → `Westways reports`.
- **Chapter 3 — S020_B044 spoken dialogue:** `Old Crown outpost in Southhold.` → `Old Crown outpost in the Crownhold.`
- **Chapter 3 — S021_B001 staging:** `abandoned Southhold outpost` → `abandoned Crownhold outpost`.
- **Chapter 4 — S022_B001 staging/reference:** `current Crown map of Southhold` → `current Crown map of the Crownhold`.

No locked Chapter 1 or Chapter 2 dialogue required a regional-name change. No additional stale regional labels were found in the audited Chapter 3 or Chapter 4 optional/Hunt dialogue.

Chapter 3 runtime Resources were regenerated from their controlling locked Markdown sources so exact source/Resource dialogue parity remains valid. The Chapter 4 S022 runtime staging was synchronized to the same terminology correction.

### Technical-identifier boundary

Legacy implementation identifiers and filenames are not authored regional prose and are **not** to be blindly renamed as part of this terminology correction. Examples include `LOC_BORDERLANDS_*` identifiers and legacy environment-resource filenames containing deprecated regional words. These may be migrated only through a dedicated reference-safe engineering cleanup if needed; their internal names do not restore or preserve the deprecated terms as current canon.
