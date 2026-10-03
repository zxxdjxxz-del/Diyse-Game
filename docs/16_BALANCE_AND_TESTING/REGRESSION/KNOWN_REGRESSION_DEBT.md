# Diyse — Known Regression/Test Debt

**Status:** ACTIVE REGRESSION-DEBT REGISTER  
**Balance/QA authority:** `../README.md`

## HIGH — Prime proof runtime migration
The executable combat proof still implements:
- `first_champion`;
- Cyanis bearer lock;
- non-bearers unable to use it;
- older proof manifestation behavior.

These runtime assumptions conflict with current Prime authority.

The obsolete mechanics regression that asserted those behaviors has already been retired, and current smoke/combat validation deliberately does not certify them. Production runtime migration plus current Prime-specific regression coverage are still required.

## MEDIUM — currency balance / final economy coverage

Runtime/save reward storage now uses `rewards.g`, and schema-v1 `rewards.gold` compatibility is regression-tested.

Still missing from final production coverage:
- authoritative prices/payouts/balances after the economy rebuild;
- complete shop/service UI behavior;
- end-to-end player-facing rejection of retired Auren terminology across final content surfaces.

## HIGH — content fixtures
Proof:
- Potion
- Proof Sword / armor
- four-character proof party
- placeholder Card/Prime

must not become production balance tests.

## MEDIUM — Chapter 13 runtime coverage
Current campaign authority includes `chapter_13`, but the generic random-encounter implementation is not whole-campaign complete:
- executable formation pools currently stop at Chapter 4;
- `encounter_balance.gd` profiles stop at Chapter 12;
- `area_encounter_tuning.gd` currently rejects enabled Chapter-13 random-encounter contexts.

Current Chapter-13 repeatable formations therefore still require a deliberate runtime migration from the owning encounter data.

## MEDIUM — no full production CEXP test
Exact campaign CEXP placement remains rebuild-pending. The retained class-completion target is Lv55–60.

Do not write a regression that freezes superseded pre-rebuild completion timing.

## MEDIUM — audio/UI final QA absent
No production audio bank/final UI yet, so release tests cannot be complete.
