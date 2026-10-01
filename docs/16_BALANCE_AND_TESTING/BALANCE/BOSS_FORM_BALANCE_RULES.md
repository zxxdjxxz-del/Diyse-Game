# Diyse — Boss Form Balance Rules

**Status:** ACTIVE BOSS-FORM BALANCE BOUNDARY  
**Boss-form mechanics authority:** `../../05_BATTLE_SYSTEM/BOSS_FORM_RULES.md`  
**Prime authority:** `../../07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`

This file defines balance/QA expectations only. Exact encounter form architecture belongs to the current enemy/boss owners.

## Same-bar state change

- one continuing HP bar/body;
- no intermediate victory/reward;
- no automatic Prime availability restoration;
- no HP refill unless the owning mechanic explicitly says otherwise;
- state mechanics may change.

## Genuine fresh form

- a new full-HP body/form where the owning encounter says so;
- no intermediate final-victory reward;
- **does not restore spent Prime identities merely because a fresh body begins**;
- does not cancel or shorten an active post-dismissal Prime-spacing gate.

Prime spent/Ready state follows the Prime owner, not enemy-body boundaries.

## Test failures

Fail if implementation:
- refills HP on a same-bar transition without an authored rule;
- restores a spent Prime merely because a boss changes state/body/form;
- pays final EXP/G/rewards before the full encounter is complete;
- creates an extra boss form not present in the current encounter owner;
- lets a historical balance report override current boss-form or Prime rules.
