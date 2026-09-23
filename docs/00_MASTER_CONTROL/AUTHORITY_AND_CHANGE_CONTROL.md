# Diyse — Authority & Change Control

## Current authority precedence

When two active claims conflict:

1. newest explicit approved user correction;
2. current file in the owning numbered domain;
3. cross-domain authority in `00_MASTER_CONTROL`;
4. clearly marked current working item in `90_WORKING` when intentionally unresolved;
5. historical/archived material for provenance only.

## Character visual authority

Exact current character appearance is owned by `14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`.

Within that art authority:
1. newest explicit approved replacement image;
2. exact approved source fingerprint registered by the active production authority;
3. repository master binary when it matches the fingerprint;
4. matching current visual-lock document;
5. shared current visual-style rules;
6. older prose/renders/hashes for provenance only.

A detailed older text description never outranks the current approved image.

### Exact-binary sync exception

When an approved replacement image cannot be promoted into Git in the same operation, the art domain may register its SHA-256, dimensions, native format, and intended path as temporary exact-source authority. During that state the registered source outranks any older binary at the path. Promotion completes only when the repository binary hashes exactly to the registered source. The source must not be altered merely to make sync easier.

## No silent resurrection

An old audit, runtime proof, image filename, archived document, or stale binary does not regain authority because a newer source has not yet been byte-synced.
