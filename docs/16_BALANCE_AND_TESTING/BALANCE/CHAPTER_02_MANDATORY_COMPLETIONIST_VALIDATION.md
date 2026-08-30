# Diyse — Chapter 2 Mandatory-vs-Completionist Validation

**Chapter:** 2 — The Drowned Oath  
**Status:** **PAPER VALIDATED v78 / TRUE-BATTLE CERTIFIED v97**  
**Power audit:** **CLOSED — ZERO DIRECT-DAMAGE POWER VALUES CHANGED**

## Validation rule — actual chapter progression
Chapter 2 is validated from its real campaign curve:
> **Lv5 chapter start → Lv9 chapter end / 6,400 cumulative EXP**

Do not test the whole chapter as a flat Lv9 package.

| Route point | Mandatory reference | Completionist / high-side reference | Active party |
|---|---|---|---|
| S012 — Dunmere / lower feed | **Lv5** | Lv5–6 | Cyanis + Ilyra + Torren + Maevra guest |
| S013 — Sunken Archive / Archive Duplicant / Leviathan | **~Lv6** | **~Lv7** | same four |
| S014 — Prisoner Galleries | **~Lv7** | **~Lv8** | same four |
| S015 — Red Transfer Bastion / Rhazek | **~Lv7** | **~Lv8**, high-side ~Lv9 | same four |
| S016 — Hold the Junction | **~Lv8** | **~Lv9** | same four |
| Chapter clear | **Lv9** | Lv9+ authored-content high-side | same four |
| Regional Hunt #2 recommendation | **Lv11 recommended** | prepared completionist may challenge earlier | Maevra remains available in the early recommended window |

### Completionist entry advantage
Mandatory Chapter 1 ends at exactly **1,600 EXP / Lv5**.

Before Chapter 2, optional authored content can include:
- The Marks We Leave — +500 EXP;
- Cistern Devourer — +1,000 EXP;
- optional encounter/Elite rewards and extra ordinary combat where earned.

A completionist can therefore enter Chapter 2 around Lv5–6 and reach the Archive Leviathan around Lv7 without any dynamic enemy scaling.

## Mandatory equipment boundary
Mandatory testing does not assume optional shop purchases.

Guaranteed baseline remains the already-owned Chapter-1 loadout.

Completionist/high-side testing may legitimately use Chapter-2 equipment that is actually obtained, including the first Chapter-2 weapon tier such as:
- Dunmere Steel;
- Blue Wardrod.

Optional equipment is an earned advantage and is not used to inflate mandatory enemy tuning.

## Reproducible Lv6 mandatory bodies
Using the active natural-stat formula, selected Base classes, and guaranteed carried equipment:
- Cyanis: **417 HP / 68 ATK / 71 DEF / 56 Spirit**;
- Ilyra: **397 HP / 54 ATK / 70 MAG / 42 DEF / 68 Spirit**;
- Torren: **377 HP / 81 ATK / 46 DEF / 40 Spirit**;
- Maevra: use the recovered early-guest combat profile already embedded in the boss recertification, approximately **50 ATK / 36 DEF / 34 Spirit** at this route point.

Maevra is not flavor-only support. She occupies the fourth active battle slot throughout Chapter 2.

## Ordinary enemy validation

### S012 — Lv5 opening ecology
Checked:
- Redwater Initiate;
- Bogshell;
- Cistern Leech.

The strongest ordinary direct hits remain low-to-moderate pressure against the Lv5 four-person party. Burn is introduced here through explicit authored riders rather than raw burst damage.

Result:
> **PASS — RETAIN RAW STATS AND POWER**

### S013 — Lv6 Archive ecology
Checked:
- Archive Current;
- Memory Scribe;
- Vault Sentinel;
- Drowned Archive Maw.

Representative pressure at the mandatory Lv6 floor remains safe but meaningful:
- Drowned Archive Maw's 180-Power physical hit is roughly **46 damage** into Ilyra's lower physical defense, about **12% Max HP**;
- Archive Current / Memory Scribe magical pressure remains below burst territory;
- copied/echoed damage is bounded by the already-closed 65% / clamp80–180 rule;
- Drowned Archive Maw's Ice presentation does not introduce Freeze early.

Result:
> **PASS**

### S014–S016 — Lv7→8 Bastion ecology
Checked:
- Bastion Shield Guard;
- Bastion Crossbow Guard;
- Transfer Adept;
- Black Host Raider carryover;
- Beast Handler;
- Rift Hound.

At the actual Lv7–8 party state, their strongest ordinary direct actions generally land in the high-single-digit to low-teens percentage of Max HP before Burn/Bleed. Formation synergy, not one oversized coefficient, supplies the pressure.

Result:
> **PASS**

## Optional Elite — Archive Duplicant
Actual access:
> **~Lv6 mandatory-route vicinity / ~Lv7 completionist high-side**

Current body:
> Lv9 / **1,000 HP** / ATK43 / MAG46 / DEF32 / Spirit33 / SPD27 / EVA5 / SR10

At Lv6, a serious four-person round using already-legal early actions is approximately:
- Cyanis Crest Strike ≈ **64.7**;
- Ilyra Warden's Valor ≈ **80.9**;
- Torren Cinder Shot ≈ **90.0**;
- Maevra Linebreaker ≈ **44.2**;
- total ≈ **279.8**.

That puts the 1,000-HP body at about **3.6 serious rounds** before Duplicant Guard, squarely inside the intended ~2–4 serious-round Elite role once its defensive turn is considered.

Deep Duplicate remains bounded at 80% of source total Power, clamp110–240, and does not copy riders.

Result:
> **PASS — RETAIN 1,000 HP AND CURRENT POWERS**

## Mandatory boss — Archive Leviathan
Existing mandatory/completionist recertification already uses the correct four-person party including Maevra:
- mandatory central: **~Lv6**;
- completionist/high-side: **~Lv7**;
- current body: Lv9 / **1,900 HP** / ATK50 / MAG52 / DEF31 / Spirit33.

Existing pacing remains valid:
- mandatory aggressive ~8–9;
- mandatory normal ~9–10;
- completionist ~8–9;
- safety ~10–11.

### v97 Recorded Pattern deterministic closure
The v78 effect/duration/threshold remain unchanged, but v97 closes the formation trigger required for reproducible true-battle testing.

**Eligibility**
Basic Attack, direct-damage Ability, and direct-damage Standard Card actions are eligible. Items, healing/support-only actions, unresolved reactions/counters, and Prime actions are not.

**Trigger**
- Track each actor's immediately previous completed eligible direct-damage action.
- Repeating the **same exact actor-qualified action** on that actor's next offensive action creates a repeat candidate.
- A non-eligible action breaks that actor's repetition chain.
- The triggering repeat deals full damage.
- At end of the party round, the last repeat candidate to have resolved becomes the single visible Recorded Pattern.
- Later qualifying repeats may replace/refresh; Patterns never stack.

**Effect**
Later use of the exact recorded actor-qualified action while active deals:
> **20% less final direct damage**

No status, penetration, healing, resource, or support component is copied or altered.

**Duration**
- State A: **2 full party rounds**;
- State B / Emergent: newly recorded patterns last **1 full party round**.

**Same-bar threshold**
> **45% HP**

No HP refill, transition damage, fresh body, or Prime refresh occurs. An already-active Pattern keeps its remaining duration through the threshold.

### v97 true-battle result
20,000 prepared simulations per route using the actual Lv6 mandatory and Lv7 high-side party states produced:
- mandatory: **100% wins / 10-round median / 10.05 mean / 0.05% any-KO**;
- completionist/high-side: **100% wins / 9-round median / 8.58 mean / 0% any-KO**.

The fight therefore lands directly in its existing ~9–10 mandatory / ~8–9 completionist target windows. HP, raw stats, action Powers, status chances, and threshold remain unchanged.

Full certification: `../TRUE_BATTLES/ARCHIVE_LEVIATHAN_TRUE_BATTLE_v97.md`

Result:
> **TRUE-BATTLE PASS / RETAIN — RAW BODY AND POWERS UNCHANGED**

## Mandatory boss — Commander Rhazek / Bastion Master
Existing recertification already includes Maevra and the real route state:
- mandatory: **~Lv7**;
- completionist: **~Lv8**;
- high-side: ~Lv9.

Current body:
> Lv10 / **2,050 HP** / ATK58 / MAG44 / DEF36 / Spirit32 / SPD27 / EVA5 / SR5

The finite Shield Detachment and Ranged Position provide action-economy tax without respawn loops. The 45% same-bar Ruin Escalation remains appropriate.

Expected pacing remains:
- mandatory normal ~10–11;
- completionist ~8–9;
- high-side ~7–8.

Result:
> **PASS — RETAIN CURRENT BODY, SUPPORTS, AND POWERS**

## Authored encounter — Hold the Junction
Actual route point:
> **~Lv8 mandatory / ~Lv9 completionist**

Fixed formation:
1. Bastion Shield Guard
2. Bastion Crossbow Guard
3. Transfer Adept
4. Rift Hound

Combined raw HP:
> **995**

All four enter together, but there is no second wave, respawn, or hidden miniboss. At the real late-Chapter-2 party level, this is a short high-action-economy rearguard fight rather than a boss-length endurance check. Completionists resolve it faster, which is intended.

Result:
> **PASS — RETAIN FIXED FOUR-BODY FORMATION**

## Regional Hunt #2 — Transfer Executioner
Unlock:
> Chapter 2 — Red Transfer Bastion branch state change

Recommendation:
> **Lv11**

Current fixed body:
> Lv11 / **3,760 HP** / ATK54 / MAG36 / DEF38 / Spirit35 / SPD28 / EVA0 / SR10

### Immediate-access check
The party can reach the Hunt while still around Lv8–9. That is intentionally below recommendation; the Hunt is not scaled down to story-route strength.

### Recommended Lv11 check
With ordinary mandatory-equipment bodies at Lv11, representative direct pressure is still recoverable:
- Executioner Blade: roughly **50–64 damage** on the permanent trio;
- Crosscut total: roughly **56–72**;
- Transfer Sweep: roughly **35–44 per target**;
- Transfer Scorch is lighter direct magic plus its 25% Burn rider.

The 3,760-HP body supplies the endurance burden. Four-person basic throughput remains far below a short-Elite clear, while legal premium abilities and stronger completionist equipment make the recommended fight meaningfully faster.

Result:
> **PASS — RETAIN FIXED Lv11 / 3,760-HP PACKAGE**

## Chapter 2 certification
### Mandatory route
> **PASS**

### Completionist route
> **PASS — ADVANTAGE PRESERVED**

### Power status
> **POWER AUDIT REMAINS CLOSED**

Zero direct-damage Power values changed in v78.

## Changes made in v78
1. Corrected Chapter 1 documentation so Maevra is explicitly included before and after Torren's recruitment.
2. Reconfirmed Watch Captain Frame at 500 HP with Maevra included.
3. Reconfirmed Cistern Devourer with the real four-person post-Torren party.
4. Validated Chapter 2 at **Lv5 start → Lv9 end**, not a flat end-level reference.
5. Explicitly counted Maevra as the fourth active combatant throughout Chapter 2.
6. Retained all Chapter-2 ordinary/Elite/Hunt raw stats and direct-damage Powers.
7. Closed Archive Leviathan's remaining Recorded Pattern duration/effect and **45%** same-bar emergence threshold.
8. Changed **zero direct-damage Power values**.

## Next validation frontier
Proceed to:
> **Chapter 3**, using its actual chapter-start, intermediate, and chapter-end levels and the correct Maevra/Nimera party-state changes.
