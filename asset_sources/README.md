# Diyse Asset Source Storage

**Purpose:** repository-side routing for original source archives used by the Diyse visual-production asset library.

This directory is intentionally separate from runtime-ready Godot assets. The tracked `.gdignore` keeps archival packages out of Godot import scanning.

## Public-repository safety split

`Diyse-Game` is currently a **public** repository.

### `private_reference/`

For the license-unverified extracted Map001–Map116 source archives and any directly derived extracted textures.

- This path is ignored by `.gitignore`.
- Do **not** commit this material to the public repository.
- Keep a private/off-repository copy and verify it against the authoritative checksum manifest before treating it as the source archive.
- If rights are later confirmed or repository/storage visibility changes, revise this policy explicitly rather than silently committing the material.

### `third_party_cc0/`

For source archives whose included license has been verified as redistributable.

The current verified set is Quaternius CC0 1.0 / Public Domain Dedication:

- `Fantasy Props MegaKit[Standard].zip`
- `Universal Animation Library[Standard].zip`
- `Universal Animation Library 2[Standard].zip`

ZIPs under this path are routed through Git LFS by the repository `.gitattributes` file.

## Authority and verification

Authoritative inventory and provenance documentation:

`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/README.md`

Authoritative source archive hashes:

`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/SOURCE_ARCHIVE_MANIFEST.md`

Use:

`python tools/verify_asset_archives.py`

to compare locally staged archives against that manifest. Use `--present-only` when checking a partial staging set.

## Runtime boundary

These source ZIPs are archival inputs, not production runtime resources. Extracted or adapted assets intended for the game should be organized separately according to current visual-production and provenance rules. License-unverified source material must remain segregated from verified-open and Diyse-original production assets.
