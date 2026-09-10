# Dialogue Authoring Status

**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicit user corrections/current domain migrations.

This folder records chapter-level dialogue readiness. These files are status/gate documents, not substitute scripts and not story authority.

## Current status

- **Chapter 0:** COMPLETE CURRENT WORKING PRODUCTION — see `CHAPTER_00.md`.
- **Chapter 1:** COMPLETE CURRENT WORKING PRODUCTION — see `CHAPTER_01.md`.
- **Chapters 2–4:** historical line-complete material may still exist, but current rehearsal-first replacement work remains pending.
- **Chapters 5–13:** use the chapter-specific status/gate files in this folder; macro-story or beat completion does not by itself mean line-complete current dialogue.

## Authority rule

Current production dialogue belongs under `docs/03_DIALOGUE/PRODUCTION/CHAPTER_##/` and is built through the rehearsal-first Dialogue Engine process.

Once a chapter has a complete current production manuscript, old duplicate `locked`, `line-complete`, or generic working transcripts should not remain live as competing authority. Git history is the archive for superseded versions.

Runtime `.tres` dialogue assets under `game/content/dialogue/` are implementation artifacts. They are current only after they have been regenerated/synchronized from the current production manuscript; their presence does not override current written dialogue authority.
