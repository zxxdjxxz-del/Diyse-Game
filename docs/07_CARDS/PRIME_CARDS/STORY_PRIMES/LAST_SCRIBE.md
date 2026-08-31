# Diyse — Prime: Last Scribe
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary Card/Prime authority:** compatible **Audit116**, superseded where applicable by **Audit119**, **Audit122**, later current v85 working closures, and newer explicit Face correction.  
**Current written whole-project authority:** **v2.20 / Audit135** plus newer approved corrections.

**Face:** Memory  
**Narrative bearer:** Nimera  
**Progression:** Recovered → Awakened

## Command package
| Command | Target | Formula | Power | Base Hit | Effect |
|---|---|---|---:|---:|---|
| **Recovered — Redraft** | one enemy | Magical / Colorless | 320 | — | 35% Spirit penetration; reverse sign of every eligible ordinary temporary stat change while preserving magnitude and remaining duration. |
| **Awakened — Redraft** | one enemy | Magical / Colorless | 270 | — | 30% Spirit penetration; same eligible temporary stat-sign reversal. |
| **Awakened — Index Shift** | one enemy | State rewrite | — | — | Temporarily swap that target's eligible **Weak ↔ Resistant** standard-element relationships **through the end of the next Prime round, or until dismissal if dismissal occurs first**. Neutral, Strongly Resistant, and Immune relationships are protected and unchanged. Unavailable Round 3. |
| **Awakened — Transcribe Affliction** | one enemy | Status rewrite | — | — | Choose one existing eligible canonical harmful status and rewrite it into a **different** legal canonical harmful status. Remove the original instance, then create a fresh instance of the chosen replacement under the target's current ordinary/high-rank status rules. No application or Status-Resistance roll is made; explicit immunity/protection still forbids that replacement. No extra action or copied damage. |
| **Legacy/final — Final Revision** | Prime Round 3 only; all enemies | Magical / Colorless | 245 each | — | 30% Spirit penetration; eligible positive ordinary temporary stat changes become corresponding negative values under protection rules. |

Last Scribe's Memory identity treats existing recorded conditions as material that can remain relevant, be preserved, or be rewritten into the present. This Face does not create a universal replay/copy command.

## Index Shift exact resolver
Index Shift rewrites only the four standard-element affinity relationships that are actually eligible to flip:
- **Weak 125% → Resistant 80%**;
- **Resistant 80% → Weak 125%**;
- Neutral 100% remains Neutral;
- Strongly Resistant 60% remains Strongly Resistant;
- Immune 0% remains Immune.

While Index Shift is active:
- direct elemental damage uses the temporarily rewritten Weak/Resistant relationship;
- a linked elemental harmful-status application uses the rewritten Weak/Resistant affinity modifier where relevant;
- raw Status Resistance, explicit status immunity, Ruin affinity, Colorless typing, and protected/scripted relationships are unchanged.

Index Shift requires at least one eligible Weak or Resistant standard-element relationship on the target. It does not transfer to a replacement/fresh enemy body.

## Transcribe Affliction exact resolver
Legal source/replacement identities are exactly the five canonical harmful statuses:
- Burn;
- Freeze;
- Stun;
- Staggered;
- Bleed.

Resolution:
1. choose one existing eligible status on the target;
2. choose a **different** canonical replacement the target is not explicitly immune/protected against;
3. remove the original status instance;
4. create the replacement as a **fresh instance**, with no ordinary application-chance, elemental-affinity, application-reliability, or Status-Resistance roll;
5. from that point onward, the replacement follows its normal current lifecycle and any Regional-Hunt / Major-Hunt / mandatory-boss conversion for that target.

Therefore a fresh rewritten status begins at its normal current starting state:
- Burn begins a new legal Burn duration and its current Defense/Spirit rider;
- Freeze begins at its first affected-round stage, subject to the target's legal Freeze maximum;
- Stun begins at its first affected turn with the target-rank action-loss rate;
- Staggered begins its full legal target-rank duration;
- Bleed begins at its initial legal magnitude with uncleared-turn age **0**, then escalates normally only if it remains uncleared through three affected turns.

Transcription intentionally **does not preserve or refresh the original status's remaining duration/progress**; the original instance is replaced by a new legal status identity.

## Global Prime references
- `../PRIME_SYSTEM_RULES.md`
- `../PRIME_SCALING.md`
- `../PRIME_STATUS_CONTROL.md`
- `../../../05_BATTLE_SYSTEM/PRIME_ROUND_SEQUENCING.md`

## Ruin formula scope
If this Prime contains Ruin damage, use the command's explicitly authored Prime formula.
Do **not** force the character-Ability 75/25 Ruin rule onto a Prime command.
