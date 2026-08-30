# Diyse — Status Balance Tests
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


Universal harmful statuses exactly:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

## Application resolver
Verify:
`Final = Base + affinity + legal specialist bonuses - Status Resistance`

Ordinary clamp:
> 5%–95%

Explicit immunity/guarantee/script may override.

## Burn
- 3 rounds
- 3% MaxHP end of each affected round
- refresh duration
- can KO
- no Crit
- ignores Defense/Spirit
- Regional Hunt damage = 75% ordinary
- Major Hunt/mandatory boss damage = 50% ordinary.

## Freeze
- no action
- rounds1–2 guaranteed
- separate 80% persistence into r3 and r4
- max4
- first successful direct Physical hit removes after hit
- no refresh
- Regional Hunt max2
- Major Hunt/mandatory boss max1.

## Stun
- 3 affected turns
- 40% action-loss ordinary
- no refresh
- Regional Hunt 25%
- Major Hunt/mandatory boss 20%.

## Staggered
- 3 rounds
- Speed −20%
- Base Hit −20%
- Evasion −20%
- refreshes
- no stack.

## Bleed
- 3% MaxHP per qualifying proc
- each round
- again whenever affected character acts
- indirect/no Crit/ignore Defense/Spirit/can KO
- clear only full HP / valid status clear / valid item
- Regional Hunt magnitude 75%
- Major Hunt/mandatory boss 50%.

Test all boundaries, including full-heal Bleed removal after exact full HP.
