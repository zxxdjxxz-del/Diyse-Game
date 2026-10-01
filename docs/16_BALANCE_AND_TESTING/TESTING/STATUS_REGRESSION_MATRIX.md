# Diyse — Status Regression Matrix

**Status:** ACTIVE STATUS QA OWNER  
**Status-system authority:** `../../05_BATTLE_SYSTEM/STATUS_EFFECTS.md`

Automate where practical:

## Burn
- apply
- tick1/2/3
- refresh
- KO
- boss magnitude conversion
- no Crit.

## Freeze
- action denial
- guaranteed first2
- persistence r3/r4
- max4
- direct Physical hit removes **after** damage
- no refresh
- Regional max2
- Major/mandatory max1.

## Stun
- affected-turn counter
- 40% ordinary roll
- 25% Regional
- 20% Major/mandatory
- no refresh.

## Staggered
- Speed/Base Hit/Evasion −20%
- refresh
- no stack
- expiry restoration
- no Break meter.

## Bleed
- starts at **3% Max HP per qualifying proc**
- after the affected unit completes **3 turns uncleared**, escalates to **4% Max HP per qualifying proc**
- third-turn action proc still uses 3%; escalation applies after that turn resolves
- reapplication while active does not reset the age/escalation; full removal followed by reapplication starts a fresh 3% Bleed
- round tick
- action tick
- multiple actual actions each qualify
- can KO
- no Crit
- ignores defenses
- partial heal does not clear
- Regen only clears if full HP achieved
- exact full HP clears
- valid status clear/item clears
- Regional Hunt conversion: 2.25% → 3% after escalation
- Major Hunt / mandatory boss conversion: 1.5% → 2% after escalation.

## Application
- hit-attached rider never applies on miss
- ordinary chance clamps 5–95
- explicit immunity blocks
- SR is raw 0/5/10/15, not percentage multiplier.
