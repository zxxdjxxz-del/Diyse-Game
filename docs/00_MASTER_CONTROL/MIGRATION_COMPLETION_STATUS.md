# Diyse — Migration Completion Status

> **SUBJECT-FOLDER REORGANIZATION COMPLETE**

All major domains 01–16 have been migrated.

Migration-only planning/history files have been moved out of active `00_MASTER_CONTROL` into `99_ARCHIVE`.

`90_WORKING` now contains only unresolved/reopened work.

## What remains
Remaining work is game-development work, not folder-migration work:
- CEXP recalibration — **CLOSED v91**
- later dialogue authoring
- unresolved rewards
- production implementation
- asset production
- music redevelopment
- full playtest/QA

## Workflow from here
1. start in `00_MASTER_CONTROL`;
2. edit the owning numbered domain;
3. use `90_WORKING` only for unresolved drafts;
4. archive superseded snapshots/history under `99_ARCHIVE`;
5. avoid recreating a giant cumulative canon tracker.
