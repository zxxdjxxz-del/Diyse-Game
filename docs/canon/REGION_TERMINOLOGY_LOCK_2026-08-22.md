# Diyse — Current Region Terminology Lock

**Original lock date:** August 22, 2026  
**Current reconciliation:** August 23, 2026 — Audit111 / Audit112

This file now reflects the current final macro-region terminology. It supersedes its earlier `The Crownhold` / `Blackstone` wording while preserving all compatible geography, settlements, landmarks, roads, regional identities, story routing, and exact map placement.

## Locked current macro-region names

- **THE GREYSPIRES / The Greyspires** — northern Yahtrean mountain region. Replaces **Diysereach** and older Highlands regional usage.
- **THE WESTWAYS / The Westways** — western Yahtrea. Replaces **Edgelands**.
- **YAHTRENHOLD / Yahtrenhold** — central/southern royal and historic core region, including Caelora and Cerythvale. Replaces **The Crownhold / Crownhold** and earlier **Southhold**.
- **BLACK HOST TERRITORY / Black Host Territory** — Black Host-controlled homeland/territory beyond The Blackspine. Replaces **Blackstone** as the region/place designation.

## The Blackspine

**The Blackspine** is the canonical mountain-range/frontier-barrier name between Yahtrea and Black Host Territory.

- `Black Mountains` is deprecated as the formal mountain-range name.
- Audit111 intentionally omits a printed Blackspine label from the final map artwork; that is a presentation choice only and does not remove the name from canon.

## Preservation rule

These terminology corrections do not move or otherwise rewrite geography unless a separate later audit explicitly says so.

- Existing settlement and landmark positions remain unchanged.
- Existing roads and connections remain unchanged.
- Existing rivers, coastlines, mountains, forests, and exact approved map placement remain unchanged.
- Existing regional cultural, musical, traversal, environmental, and story identities remain inherited where compatible.
- Audit111's exact final world-map image remains the visual/spatial authority.

## Usage rule

Use **The Greyspires**, **The Westways**, **Yahtrenhold**, and **Black Host Territory** as the current authoritative region names in new canon, scripts, dialogue, quest text, UI, codex text, map labels, and implementation-facing documentation.

Interpret older regional references as follows when they refer to the same places:

- `Diysereach` / regional `Highlands` → **The Greyspires**.
- `Edgelands` / `Borderlands` as the old western-region name → **The Westways**.
- `Southhold` / `The Crownhold` / `Crownhold` → **Yahtrenhold**.
- `Blackstone` as the Black Host homeland/region → **Black Host Territory**.

Do not use **The Yahtrenhold** as the formal region name. The correct prose form is **Yahtrenhold**.

## Westguard location-name reconciliation

**Westguard** is the current proper name of the western settlement/location formerly called **Westreach** and briefly **Yahtrens Stand**.

This is a location rename, not a new settlement. Preserve its locked map position, terrain, roads, and Crownfall relationship.

Older `Westreach` / `Yahtrens Stand` references should be interpreted as **Westguard** when they refer to this same location until a reference-safe stale-term cleanup is completed.

## Chapters 0–4 dialogue terminology status

The earlier August-22 terminology pass changed several old regional words while preserving locked dialogue voice and scene logic. Audit111 now supersedes the intermediate `Crownhold` wording with **Yahtrenhold**.

Final intended authored terminology for the previously affected beats is therefore:

- **Chapter 0 — S001 staging:** `Westways road` remains correct.
- **Chapter 3 — S019_B016 spoken dialogue:** `Westways reports` remains correct.
- **Chapter 3 — S020_B044 spoken dialogue:** current region term should be **Yahtrenhold**, not `Southhold` or `the Crownhold`.
- **Chapter 3 — S021_B001 staging:** current region term should be **Yahtrenhold**, not `Southhold` or `Crownhold`.
- **Chapter 4 — S022_B001 staging/reference:** current region term should be **Yahtrenhold**, not `Southhold` or `the Crownhold`.

The terminology correction does not reopen character voice, scene beats, delivery, narrative logic, quest logic, combat logic, or unrelated staging. Source/runtime text propagation should be performed through a reference-safe dialogue/implementation cleanup if those files still contain the superseded intermediate terms.

### Technical-identifier boundary

Legacy implementation identifiers and filenames are not authored regional prose and must not be blindly renamed merely because they contain deprecated terms. Migrate technical identifiers only through a dedicated reference-safe engineering cleanup.

Current controlling higher authority:
- Audit111 — final surface map / region terminology.
- Audit112 — Chapter-10 story / Eastern Wayfinder discovery logic.
