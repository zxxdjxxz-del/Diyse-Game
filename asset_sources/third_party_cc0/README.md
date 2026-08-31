# Verified CC0 Source Archives

This directory is reserved for redistributable third-party source archives whose included license has been verified before import.

## Current approved source ZIPs

Quaternius / @Quaternius — CC0 1.0 Universal / Public Domain Dedication:

| Archive | Expected bytes | Expected SHA-256 |
|---|---:|---|
| `Fantasy Props MegaKit[Standard].zip` | 150213360 | `8b6f7e806d222e585478f0e1bdc6b271bbc7bc6f84dd6af8ca703a7c64f0cb1e` |
| `Universal Animation Library[Standard].zip` | 15904933 | `cc73fc4e495b82958207316596317a3f40b9fa38065bde1027937452da537724` |
| `Universal Animation Library 2[Standard].zip` | 18735003 | `4008ea208a604773a2b2177d965f0f5d3195498b5bf838c3f5785d68e95f2a68` |

These ZIPs are configured for Git LFS by the root `.gitattributes` file.

Before committing any binary, verify it with:

`python tools/verify_asset_archives.py --present-only`

The complete authoritative archive manifest remains:

`docs/14_ART_AND_VISUALS/PRODUCTION/ASSET_LIBRARY/SOURCE_ARCHIVE_MANIFEST.md`
