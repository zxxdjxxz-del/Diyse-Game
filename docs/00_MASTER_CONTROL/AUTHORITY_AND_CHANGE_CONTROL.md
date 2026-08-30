# Diyse — Authority & Change Control

## Current authority precedence

When two active claims conflict:

1. newest explicit approved user correction;
2. current file in the owning numbered domain;
3. cross-domain authority in `00_MASTER_CONTROL`;
4. a clearly marked current working item in `90_WORKING` when the question is intentionally unresolved;
5. historical source/archived authority only for provenance.

## One canonical home
Every current rule has one owning domain.

Examples:
- exact spoken lines → `03_DIALOGUE`
- combat formula → `05_BATTLE_SYSTEM`
- Ability MP → `06_CLASSES_AND_ABILITIES`
- Prime mechanics → `07_CARDS`
- equipment stats → `08_ITEMS_AND_EQUIPMENT`
- enemy raw stats → `09_ENEMIES_AND_ENCOUNTERS`
- Player EXP/CEXP → `10_PROGRESSION_AND_EXP`
- quest flow → `11_QUESTS`
- item price/shop economy → `12_ECONOMY_AND_REWARDS`

Other domains may reference the rule but should not independently redefine it.

## Working promotion
A draft in `90_WORKING` becomes current only when:
1. approved;
2. written into the owning numbered domain;
3. relevant cross-domain references are updated;
4. the working file is closed/moved to archive as appropriate.

## Closed numeric change
For a closed balance value:
- reproduce the problem;
- determine bug vs data vs UX vs actual balance issue;
- propose explicit replacement;
- identify regressions;
- obtain approval;
- update the owner file and validation references.

## No silent resurrection
An old audit, old tracker, old runtime proof, old image filename or archived document does not regain authority because a newer file is incomplete.

OPEN means:
> unresolved

not:
> use the previous retired answer.
