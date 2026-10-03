# Diyse — Authority & Change Control

## Current authority precedence

When two active claims conflict:

1. newest explicit approved user correction;
2. current file in the owning numbered domain;
3. cross-domain authority in `00_MASTER_CONTROL`;
4. clearly marked current working item in `90_WORKING` when intentionally unresolved;
5. Git history for deliberate provenance/recovery only.

## Historical-material policy

Superseded or retired design material does not remain on `main` solely to preserve history. Git history is the project recovery layer.

Historical identifiers, fixtures, data, or source records may remain only when a current production requirement depends on them, such as:
- save/data compatibility;
- active regression validation;
- licensing or exact-source provenance;
- a still-used proof/runtime dependency that is explicitly tracked for migration.

Those exceptions must be documented beside the current owning system and do not regain design authority.

## Character visual authority

Exact current character appearance is owned by `../14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`.

Within that art authority:
1. newest explicit approved replacement image;
2. exact approved source fingerprint registered by the active production authority;
3. repository master binary when it matches the fingerprint;
4. matching current visual-lock document;
5. shared current visual-style rules;
6. older source evidence only when a current provenance requirement explicitly preserves it.

A detailed older text description never outranks the current approved image.

### Exact-binary sync exception

When an approved replacement image cannot be promoted into Git in the same operation, the art domain may register its SHA-256, dimensions, native format, and intended path as temporary exact-source authority. During that state the registered source outranks any older binary at the path. Promotion completes only when the repository binary hashes exactly to the registered source. The source must not be altered merely to make sync easier.

## No silent resurrection

An old audit, runtime proof, historical filename, stale binary, or past commit does not regain authority because a newer source has not yet been byte-synced.
