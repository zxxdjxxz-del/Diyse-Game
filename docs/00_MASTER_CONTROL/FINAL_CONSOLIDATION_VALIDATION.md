# Diyse — Consolidation Validation

This file records the repository-facing validation rules for the subject-folder authority. Historical package-count audits are preserved in Git history and are not repeated here.

## Structure
Required active domains:
- `00_MASTER_CONTROL`
- numbered domains `01` through `16`
- `90_WORKING`

Historical recovery is provided by Git history and `archive/pre-v98-reorganization`; active documentation must not depend on archived material for current rules.

## Authority
- One owning subject domain per current rule — REQUIRED.
- Newest explicit approved correction outranks older text — REQUIRED.
- `90_WORKING` does not become canon until promoted into the owning domain — REQUIRED.
- Historical audits/trackers never silently override current domain files — REQUIRED.
- Root `README.md` and `AGENTS.md` route engineering work; they are not duplicate master-canon files — REQUIRED.

## Current high-risk firewalls
- `Blackstone`, Crownhold, Southhold, Edgelands, Diysereach and other retired regional labels are not current-facing geography.
- Acuity is the current Face; Resource/Last Measure are retired.
- Standard elements are Fire / Ice / Lightning / Earth only.
- Spirit is the magic-resistance stat.
- There is no natural Accuracy stat.
- Barrier does not exist.
- Brace does not exist.
- There is no global Break/Stagger meter; Staggered is an ordinary harmful status.
- Mastery Point currency is removed.
- Synthesis progression is removed.
- Concordant Prime progression is removed.

## Current progression/balance checkpoint
- Player level cap: 70.
- Normal campaign ending: about Lv62.
- Last Shelter: about Lv60.
- CL13: 6,000 cumulative CEXP.
- Recruitment-aware normal-route Base + Subclass completion: approximately Lv55–60.
- Enemy direct-damage Power audit: CLOSED.
- Mandatory-vs-completionist campaign paper validation: COMPLETE through Chapters 0–13.
- Enemy static design: CLOSED.
- Hollow Watch Castellan representative true battle: CERTIFIED v93.
- Archive Leviathan representative true battle: CERTIFIED v97 / RETAIN.

## Current Bleed authority
`05_BATTLE_SYSTEM/STATUS_EFFECTS.md` owns Bleed:
- 3% Max HP per qualifying proc initially;
- after 3 affected-unit turns uncleared, 4% per qualifying proc;
- round tick + actual-action tick;
- removal only by full-HP restoration, eligible harmful-status clear, or eligible item.

## Repository migration acceptance
Before the migration PR may become reviewable:
1. all required subject domains exist under `docs/`;
2. old root-level legacy documentation authority is removed from active `docs/`;
3. runtime/build/test surfaces are unchanged except intentional routing/test-reference updates;
4. stale root Mastery/retired-system guidance is absent;
5. Godot Smoke Validation passes on the exact final head;
6. Android APK Proof passes on the exact final head.

No gameplay value is changed merely to make this repository transition pass.
