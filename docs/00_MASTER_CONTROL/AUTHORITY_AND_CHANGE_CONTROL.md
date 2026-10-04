# Diyse — Authority & Change Control

## Current authority precedence

When two active claims conflict:

1. newest explicit approved user correction;
2. current file in the owning numbered domain;
3. cross-domain authority in `00_MASTER_CONTROL`;
4. clearly marked current working item in `90_WORKING` when intentionally unresolved.

Proof/runtime behavior is implementation evidence only and never overrides the current owner.

Git history is recovery infrastructure, not an authority layer.

## Repository retention

`main` should contain current authority and active production dependencies.

Identifiers, fixtures, source records, or compatibility data may remain only when a current production requirement depends on them, such as:
- save/data compatibility;
- active regression validation;
- licensing or exact-source provenance;
- a still-used proof/runtime dependency explicitly tracked for migration.

Those exceptions remain implementation/provenance data and do not gain design authority.

## Character visual authority

Exact current character appearance is owned by `../14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`.

Within that art authority:
1. newest explicit approved replacement image;
2. exact approved source fingerprint registered by the active production authority;
3. repository master binary when it matches the fingerprint;
4. matching current visual-lock document;
5. shared current visual-style rules.

### Exact-binary sync exception

When an approved replacement image cannot be promoted into Git in the same operation, the art domain may register its SHA-256, dimensions, native format, and intended path as temporary exact-source authority. During that state the registered source controls until the repository binary hashes exactly to it.

The source must not be altered merely to make synchronization easier.

## Current-source rule

Proof runtime, unmatched binaries, and Git recovery data do not outrank current approved owner-domain authority.
