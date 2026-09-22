# Diyse — Mandatory Route G Budget

**Status:** EXACT MANDATORY-ROUTE G CALIBRATION AUTHORITY

This file defines the mandatory-route G envelope used to tune ordinary formations, story encounters, authored currency rewards, and direct-G caches.

## Currency
All current-facing mandatory income uses:
> **G**

## Mandatory-route direct-G composition
| Source | Direct G |
|---|---:|
| Starting wallet | **2,500 G** |
| Ordinary Chapter 1–13 formations | **~135,600 G** |
| Mandatory story bosses / named encounters | **92,700 G** |
| Fixed authored combat/event payouts | **5,300 G** |
| Mandatory non-battle reward map | **80,800 G** |
| **Mandatory-route total** | **~316,900 G** |

The ordinary-formation total is a route expectation across the 225-encounter planning spine, so the final wallet can vary with encounter RNG, escapes, backtracking, and spending.

## Ordinary encounter share
Ordinary formations contribute approximately:
> **42.8%**

of the calibrated mandatory-route direct G.

This satisfies the retained design target that ordinary random encounters contribute roughly:
> **40–50% of routine mandatory-route spendable currency**

without becoming the only meaningful source of money.

## Protected/nonlethal contribution
Protected/nonlethal story-boss resolutions contribute **7,800 G** inside the 92,700-G story-boss layer.

Additional protected/nonlethal authored-event payouts are represented in the fixed event layer where applicable.

Do not restore a blanket `nonlethal = 0 G` rule.

## Exact owner files
- ordinary formations → `ENCOUNTER_G_REWARDS.md`
- mandatory story bosses/named encounters → `STORY_BOSS_G_REWARDS.md`
- fixed authored combat/event payouts → `ENEMY_REWARD_HANDOFF.md`
- mandatory non-battle map → `MANDATORY_NONBATTLE_G_BUDGET.md`
- starting wallet → `CHAPTER_00_FIELD_ISSUE.md`

## Sources excluded from baseline solvency
Do **not** rely on:
- ordinary Side Quests;
- Regional Hunts;
- Major Hunts;
- Character Quests;
- resale;
- repeat farming/backtracking;
- optional late-game cleanup.

Those sources create surplus and build flexibility.

## Checkpoint pressure rule
At a normal meaningful commerce checkpoint:
> **one meaningful ordinary equipment purchase + routine Consumable restock should usually be affordable without exhausting all funds.**

The mandatory route does not promise enough G to buy every newly available ordinary item immediately.

## Anti-grind guardrail
If future playtest simulation shows a normal campaign repeatedly falls below intended purchase/restock pressure, fix authored mandatory G distribution rather than requiring optional farming.

If the mandatory route routinely buys everything with little sacrifice, reduce or redistribute authored G before globally inflating prices.


## Strong normal-pool former-Elite rule
Former optional-Elite identities are now part of normal encounter pools. They do **not** add a separate fixed bounty to the mandatory-route budget.

Their current G is subsumed by the normal formation-level reward selected from `ENCOUNTER_G_REWARDS.md`. This keeps the existing ordinary-formation route expectation structurally intact unless later encounter-frequency/G validation changes the formation-level budget itself.
