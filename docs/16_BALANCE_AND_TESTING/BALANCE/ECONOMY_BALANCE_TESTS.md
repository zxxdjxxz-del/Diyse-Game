# Diyse — Economy Balance Tests

**Status:** ACTIVE ECONOMY QA FRAMEWORK / NUMERIC RECALIBRATION OPEN  
**Economy authority:** `../../12_ECONOMY_AND_REWARDS/`

Economy authority:
`12_ECONOMY_AND_REWARDS`

## Current currency
> **G**

## Test goals
- normal-route income can support ordinary consumable/equipment use without trivializing purchases;
- ordinary equipment registration/repurchase works;
- selling cannot create infinite profit loops;
- protected project materials cannot be sold;
- reward-only exceptional consumables remain scarce;
- Vhalmarch is not a duplicate full superstore;
- Cresthaven Quartermaster backfill works as authored.

## Numeric-authority boundary
The current economy is explicitly **rebuild/recalibration pending** in `12_ECONOMY_AND_REWARDS`.

Do not test provisional G prices, payouts, fees, liquidity totals, or completionist-cash totals as final target oracles. Preserve structural exploit/flow tests now; rerun numeric affordability and sink calibration after the rebuilt economy is authored.

Current open examples include:
- Chapter-3 Memory Construct G payout;
- final formation-level G remap where still open;
- future recertification of quest/Hunt cash and Kessara service pricing.

## Exploit tests
Check:
- buy → sell loop;
- forged Relic duplication → sell or copy exploit;
- project-material resale;
- repeated first-clear reward;
- save/load duplication around service/reward commits.
