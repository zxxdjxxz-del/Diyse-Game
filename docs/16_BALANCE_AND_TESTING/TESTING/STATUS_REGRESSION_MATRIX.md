# Diyse — Status Regression Matrix

**Status:** ACTIVE STATUS QA OWNER  
**Status-system authority:** `../../05_BATTLE_SYSTEM/STATUS_EFFECTS.md`

Automate where practical. If this file conflicts with `../../05_BATTLE_SYSTEM/STATUS_EFFECTS.md`, the battle-system owner wins and this matrix must be synchronized.

## Burn

Verify:
- 4-round duration;
- 6% Max HP end-of-round damage per affected round;
- application round can count as round 1 when Burn remains active through round end;
- Defense −10% and Spirit −10% while active;
- reapplication refreshes duration;
- Burn does not stack with itself;
- damage cannot Crit;
- damage ignores Defense/Spirit;
- damage can KO;
- Regional Hunt damage conversion = 4.5% Max HP/round;
- Major Hunt / mandatory boss damage conversion = 3% Max HP/round;
- high-rank conversion changes damage magnitude only, not the Defense/Spirit rider.

## Freeze

Verify:
- target cannot act;
- first 2 affected rounds guaranteed;
- separate 80% persistence checks into affected rounds 3 and 4;
- ordinary maximum 4 affected rounds;
- first successful direct Physical hit removes Freeze after that hit;
- no refresh while active;
- Regional Hunt maximum 2 affected rounds;
- Major Hunt / mandatory boss maximum 1 affected round;
- application timing correctly distinguishes before-turn vs after-turn application.

## Stun

Verify:
- 4 affected turns;
- 40% action-loss chance on each ordinary affected turn;
- cannot refresh while active;
- Regional Hunt action-loss chance = 25%;
- Major Hunt / mandatory boss action-loss chance = 20%;
- each affected turn opportunity consumes one duration count whether the action-loss roll succeeds or fails.

## Staggered

Verify:
- 5-round ordinary duration;
- Attack −20%;
- Magic −20%;
- Speed −20%;
- application round counts as round 1;
- mid-round application does not reorder the already-fixed current-round initiative;
- Speed penalty affects later beginning-of-round ordering while active;
- reapplication refreshes duration;
- no self-stacking;
- remains a normal harmful status, not a Break/Stagger meter;
- Regional Hunt duration = 4 rounds;
- Major Hunt / mandatory boss duration = 3 rounds.

## Bleed

Verify:
- starts at 3% Max HP per qualifying proc;
- end-of-round proc while active;
- additional proc after each actual action by the affected unit;
- lost/no-action turns can advance Bleed age but do not create an action proc;
- third completed affected turn's action proc still uses 3%;
- after that third completed turn, same uncleared Bleed escalates to 4%;
- reapplication while active does not reset age/escalation;
- full removal + later reapplication starts a fresh 3% Bleed;
- can KO;
- cannot Crit;
- ignores Defense/Spirit;
- full HP clears;
- valid harmful-status clear/item clears;
- partial heal does not clear;
- Regen clears only if full HP is actually reached or an explicit clear is included;
- Regional Hunt magnitude = 2.25% initially → 3% escalated;
- Major Hunt / mandatory boss magnitude = 1.5% initially → 2% escalated.

## Application resolver

Verify:
- hit-attached status rider never applies on miss;
- ordinary status chance clamps to 5%–95%;
- explicit immunity/guarantee/script may override the ordinary clamp;
- Status Resistance uses raw 0/5/10/15 values;
- application-reliability bonuses add percentage points where legal;
- retired percentage-based Status Resistance tables do not reappear.
