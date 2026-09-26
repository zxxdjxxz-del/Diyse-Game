# DIYSE Runtime Dialogue Resources

## Current authority

For Chapters 0–3, the only live runtime dialogue Resources are generated under:

```text
game/content/dialogue/current/
```

The manifest at `current/manifest.json` is the runtime routing/index layer. It records canonical slot IDs, source identities, source hashes, spoken-sequence hashes, and line counts.

Exact spoken wording remains owned by `docs/03_DIALOGUE/PRODUCTION/`; runtime Resources are derived artifacts.

## Retired legacy trees

The former `chapter_00/` through `chapter_03/` S/H resource trees were retired after the B/C migration. They encoded superseded structures and numbering and must not be restored beside `current/`.

Git history preserves those historical generated Resources and their old regression tests.

## Chapter 4

`chapter_04/` remains a legacy/pre-current implementation layer for now because Chapter 4 exact dialogue is not yet fully approved/compiled. Do not infer exact Chapter-4 wording authority from those Resources.

When Chapter 4 exact dialogue is approved, compile it into `current/chapter_04/` and retire the legacy Chapter-4 tree in the same migration.
