# Current Chapter 0 Enemy Visual Masters

This folder is the canonical repository destination for the seven exact approved Chapter 0 enemy visual masters.

Exact fingerprints are registered in [`APPROVED_SOURCE_MANIFEST.json`](APPROVED_SOURCE_MANIFEST.json). A repository binary is authoritative only when its SHA-256 matches the manifest exactly.

Approved destinations:
- `black_host_raider.png`
- `black_host_crossbowman.png`
- `ruin_shieldbearer.png`
- `war_hound.png`
- `ruin_vanguard_pursuer_concealed_seyrik.jpg`
- `convoy_war_sorcerer.png`
- `riftmaw.png`

Reference packet destination:
- `chapter_00_locked_enemy_visuals.pdf`

Human-readable authority:
- [Chapter 0 Enemy Visual Authority](../../../../docs/14_ART_AND_VISUALS/ENEMIES/CHAPTER_00_ENEMY_VISUAL_AUTHORITY.md)

## Exact-source rule

Do not re-encode, resize, crop, retouch, recolor, optimize, or resave a master merely to make repository sync easier.

Until a destination binary hashes exactly to the manifest, the registered approved source fingerprint outranks any older or substitute binary at that path under the repository's exact-binary sync exception.

## Binary-sync state

**EXACT ENEMY MASTER SYNC: COMPLETE — 7/7.**

All seven repository master binaries match the approved source byte identities registered in the manifest. The concealed-Seyrik master is stored as `.jpg` because its native approved byte stream is JPEG/JFIF despite the original uploaded filename ending in `.png`; no conversion was performed.

**Reference PDF sync:** PENDING. The PDF is a convenience/reference packet and does not control the seven individual exact visual masters.
