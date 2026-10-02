# Diyse — Known Regression/Test Debt

**Status:** ACTIVE REGRESSION-DEBT REGISTER  
**Balance/QA authority:** `../README.md`

## HIGH — Prime proof tests
Current smoke/combat proof still expects:
- `first_champion`;
- Cyanis bearer lock;
- non-bearers unable to use it;
- older proof manifestation behavior.

These expectations conflict with current Prime authority.

Production test update required.

## HIGH — Mastery Point regression
Older repository documentation references 8 automatic Mastery Points.

Current:
> Mastery Point currency removed.

Add regression that no runtime/save/UI field reintroduces it.

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

## MEDIUM — Chapter ID range
Older schema docs may stop at chapter_12/S062.

Current:
- chapter_13
- S073.

## MEDIUM — no full production CEXP test
Exact campaign CEXP placement remains rebuild-pending. The retained class-completion target is Lv55–60.

Do not write a regression that freezes superseded pre-rebuild completion timing.

## MEDIUM — audio/UI final QA absent
No production audio bank/final UI yet, so release tests cannot be complete.
