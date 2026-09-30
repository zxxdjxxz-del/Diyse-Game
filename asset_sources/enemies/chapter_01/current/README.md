# Current Chapter 1 Enemy Visual Masters

Canonical destination for exact approved Chapter-1 enemy visual masters.

**Current visual state:** **9 / 9 Chapter-1 masters locked and exact-binary synced.**

The three reused Black Host enemies remain sourced from Chapter 0:
- Black Host Raider → `asset_sources/enemies/chapter_00/current/black_host_raider.png`
- Black Host Crossbowman → `asset_sources/enemies/chapter_00/current/black_host_crossbowman.png`
- Black Host Shieldbearer → `asset_sources/enemies/chapter_00/current/black_host_shieldbearer.png`

Do not duplicate those carryover masters into this folder. Their exact source paths are also recorded in `APPROVED_SOURCE_MANIFEST.json`.

## Locked exact masters

- [thicket_stalker.png](thicket_stalker.png) — Thicket Stalker
- [vine_creeper.png](vine_creeper.png) — Vine Creeper
- [bullhog.jpg](bullhog.jpg) — Bullhog (original upload is JPEG/JFIF data; preserve bytes exactly)
- [needlewing.png](needlewing.png) — Needlewing
- [burrowclaw.png](burrowclaw.png) — Burrowclaw
- [barkling.png](barkling.png) — Barkling
- [construct.png](construct.png) — Construct
- [shield_construct.png](shield_construct.png) — Shield Construct
- [thornhide.png](thornhide.png) — Thornhide

Exact dimensions, source/generation identity, byte size, SHA-256, and binary-sync state are recorded in `APPROVED_SOURCE_MANIFEST.json`. All nine binaries match their approved SHA-256 fingerprints; `SHA256SUMS.txt` provides a local verification list.

## Chapter 1 roster changes reflected by this lane

- Briar Boar → **Bullhog**
- Rootmaw → **Burrowclaw**
- Rubbleback → **Barkling**

These are **asset-source reconciliation mappings only**. They do not mean the current enemies inherit retired encounter roles. Watch Captain Frame is retired from Chapter 1 and has no Chapter-1 rename/successor mapping; Construct is its own current ordinary underground identity. Watch Castellan is likewise retired with no successor mapping; Shield Construct is its own separately locked fixed/authored encounter and is explicitly **not a miniboss**. **Thornhide** is the current Chapter-1 boss identity and species name. **Thornhide Stalker → Thornhide** is a true retired-name → current-name mapping.
- **Watch Sentry** removed
- **Watch Ballista** removed
- **Cistern Devourer** removed
- **Regional Hunt #1** removed

## Exact-source rule

Do not re-encode, crop, resize, recolor, retouch, optimize, or resave an approved master during repository promotion. A repository binary becomes authoritative only when its SHA-256 matches the value in `APPROVED_SOURCE_MANIFEST.json` exactly.
