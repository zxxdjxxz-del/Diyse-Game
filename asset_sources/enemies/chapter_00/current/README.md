# Current Chapter 0 Enemy Visual Masters

This folder is the canonical repository destination for the seven exact approved Chapter 0 enemy visual masters.

Exact fingerprints are registered in [`APPROVED_SOURCE_MANIFEST.json`](APPROVED_SOURCE_MANIFEST.json). A repository binary is authoritative only when its SHA-256 matches the manifest exactly.

Approved exact repository masters:

| Enemy | Repository master | Native format | Dimensions | SHA-256 |
| --- | --- | --- | ---: | --- |
| Black Host Raider | [`black_host_raider.png`](black_host_raider.png) | PNG | 1122 × 1402 | `446ff9e2275fbbd2d44be3b5c61f8cc1136d910e53a760d3a605dfcee8d2687f` |
| Black Host Crossbowman | [`black_host_crossbowman.png`](black_host_crossbowman.png) | PNG | 1122 × 1402 | `845b344ebf8d45b3c078b9ffc3dd094c19407bdfe07819608dfcbd07960c96a5` |
| Black Host Shieldbearer | [`black_host_shieldbearer.png`](black_host_shieldbearer.png) | PNG | 1122 × 1402 | `18d1237f4f933bdf6dbcba7f9b4df90c5090ec413ebe334cb5a4982c221fb2d7` |
| War Hound | [`war_hound.png`](war_hound.png) | PNG | 1155 × 1362 | `2108a1cd66d42512342c96f4cf02787d0a06aee20410145ff20c77bfbeec192a` |
| Ruin Vanguard Pursuer / concealed Seyrik | [`ruin_vanguard_pursuer_concealed_seyrik.jpg`](ruin_vanguard_pursuer_concealed_seyrik.jpg) | JPEG/JFIF | 1287 × 1536 | `c6ea82c58c628679536447fd6a55b00d306651f99a39599fba4124262d7aa011` |
| Battle Sorcerer | [`battle_sorcerer.png`](battle_sorcerer.png) | PNG | 1145 × 1374 | `4090842e2e765cecc83235d1ddf79d0b211872f3abbf2baff0955bd3bfff3573` |
| Riftmaw | [`riftmaw.png`](riftmaw.png) | PNG | 1122 × 1402 | `0d7058da574b838a22ab5a1835278eff0e2ab3e60f13ff62a9df37687f0e3dd1` |

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
