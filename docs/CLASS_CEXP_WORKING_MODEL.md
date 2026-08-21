# Diyse — CL13 Class EXP Working Model

**Status:** ACTIVE WORKING DESIGN — NOT MASTER CANON  
**Parent tracker:** `docs/CLASS_REWORK_MASTER_TRACKER.md`  
**Parent whole-project authority:** v1.84 / Audit99 plus newer explicit class-rework decisions.

## 1. Purpose

This file models Class EXP pacing for the proposed **Base CL1–13 / Subclass CL1–13** architecture. It is intended to keep class progression meaningful through the campaign-only Level ~55 finish while leaving optional Level 56–60 play useful for players who split Focus or want to finish both class lines.

Class EXP remains separate from Character EXP. The currently selected class receives CEXP; the unselected class receives none. Before the Sixfold Accord only Base Focus exists.

The chapter encounter counts used below are the current Audit98/Audit99 expected mandatory-route random-encounter references. They are **not fixed quotas**. The model uses them only to prove pacing mathematically.

## 2. Proposed shared CL13 threshold curve

Use the same cumulative threshold curve for Base and Subclass unless later testing demonstrates a need to separate them.

| Class Level | Cumulative CEXP | CEXP to next |
|---:|---:|---:|
| CL1 | 0 | 150 |
| CL2 | 150 | 200 |
| CL3 | 350 | 250 |
| CL4 | 600 | 350 |
| CL5 | 950 | 400 |
| CL6 | 1,350 | 450 |
| CL7 | 1,800 | 500 |
| CL8 | 2,300 | 550 |
| CL9 | 2,850 | 600 |
| CL10 | 3,450 | 700 |
| CL11 | 4,150 | 800 |
| CL12 | 4,950 | 1,050 |
| CL13 | **6,000** | — |

Design reasons:
- 6,000 is long enough to spread a fresh Subclass across the post-Accord campaign.
- Early levels are deliberately less compressed than the retired 4,800-CEXP CL12 implementation table, so donor equipment learned by CL5 does not all arrive after only a handful of fights.
- Late levels deliberately lengthen so Trait III and the Ultimate remain meaningful late-campaign goals.

## 3. Base learning schedule paired to the curve

| Base CL | Major class result | Cumulative CEXP |
|---:|---|---:|
| 1 | Trait I + Base Abilities 1–3 + starting equipment | 0 |
| 3 | Base Ability 4 | 350 |
| 5 | Native advanced equipment permission where one exists | 950 |
| 6 | Base Ability 5 + Trait II | 1,350 |
| 9 | Base Ability 6 | 2,850 |
| 12 | Trait III | 4,950 |
| 13 | Base Ultimate | 6,000 |

Base CL5 remains class-specific: Cyanis second Sword, Ilyra Shield, Nimera two-handed Conduits; Vaelira Focus remains the leading candidate; Torren and Seyrik must not receive fabricated equipment permissions merely for symmetry.

## 4. Subclass learning schedule paired to the curve

| Subclass CL | Major class result | Cumulative CEXP |
|---:|---|---:|
| 1 | Donor Primary + Trait I + Ability 1 | 0 |
| 3 | Donor Armor | 350 |
| 4 | Ability 2 | 600 |
| 5 | Donor advanced equipment permission / Secondary package where applicable | 950 |
| 6 | Trait II | 1,350 |
| 7 | Ability 3 | 1,800 |
| 9 | Ability 4 | 2,850 |
| **10** | **Equipment Mastery gate — Subclass Mastery Node 4 becomes available; acquiring it unlocks donor Relic access** | **3,450** |
| 11 | Ability 5 | 4,150 |
| 12 | Trait III | 4,950 |
| 13 | Subclass Ultimate | 6,000 |

**Equipment Mastery is a CL10 milestone.** It remains the fourth Subclass Mastery node rather than becoming an automatic ordinary class ability. Reaching Subclass CL10 opens that node; once the node is acquired through the Mastery system, the character gains the donor tradition's Relic access.

## 5. Recruitment starting Base CL values

When a character joins above CL1, begin them exactly at the threshold for their authored starting Base CL unless a later balance pass intentionally gives partial progress.

| Character | Recruitment | Starting Base CL | Starting cumulative CEXP |
|---|---|---:|---:|
| Cyanis | Chapter 0 | CL1 | 0 |
| Ilyra | Chapter 0 | CL1 | 0 |
| Torren | Chapter 1 | CL4 working | 600 |
| Nimera | Chapter 3 | CL4 working | 600 |
| Vaelira | Chapter 4 | CL7 working | 1,800 |
| Seyrik | Chapter 6 | **CL8** | **2,300** |

Seyrik CL8 is an explicit current design decision. He therefore reaches CL9 / Call Shardfang through player-controlled growth after recruitment rather than arriving with it.

## 6. Ordinary random-encounter CEXP target by chapter

The following values are **expected average CEXP per ordinary random-encounter victory** for a character whose currently selected class receives CEXP.

They are not intended to make every Light / Standard / Heavy formation award exactly the same number. Implementation may split each chapter target into Light / Standard / Heavy rewards, provided the weighted average stays close to the chapter target.

| Chapter | Expected ordinary random encounters | Target average CEXP / victory | Expected ordinary CEXP |
|---:|---:|---:|---:|
| Ch1 | 18 | 20 | 360 |
| Ch2 | 19 | 24 | 456 |
| Ch3 | 19 | 28 | 532 |
| Ch4 | 19 | 32 | 608 |
| Ch5 | 20 | 36 | 720 |
| Ch6 | 19 | 40 | 760 |
| Ch7 | 19 | 42 | 798 |
| Ch8 | 18 | 45 | 810 |
| Ch9 | 16 | 48 | 768 |
| Ch10 | 17 | 52 | 884 |
| Ch11 | 18 | 56 | 1,008 |
| Ch12 | 8 | 60 | 480 |

Expected ordinary-random totals under the current encounter-count reference:
- **Ch1–6:** 3,436 CEXP;
- **Ch7–12:** 4,748 CEXP;
- **Ch1–12:** 8,184 CEXP.

This is intentionally not enough by itself to take a fresh post-Accord Subclass from CL1 to CL13. Significant authored combat supplies the remaining campaign CEXP, so bosses and major story battles matter to class growth without ordinary encounters becoming trivial.

## 7. Mandatory authored-combat CEXP budget by chapter

For pacing proof, use the following **chapter-level authored-combat budgets**. These are not one mandatory lump-sum reward and are not a hard count of bosses. The chapter's actual Elites, minibosses, story bosses, and other authored victories should divide the budget among themselves.

| Chapter | Authored-combat CEXP budget |
|---:|---:|
| Ch1 | 90 |
| Ch2 | 100 |
| Ch3 | 110 |
| Ch4 | 120 |
| Ch5 | 140 |
| Ch6 | 160 |
| Ch7 | 180 |
| Ch8 | 190 |
| Ch9 | 200 |
| Ch10 | 220 |
| Ch11 | 250 |
| Ch12 | 220 |

Suggested per-victory hierarchy inside a chapter budget:
- authored tough battle / named formation: lowest share;
- Elite / miniboss: medium share;
- story boss: high share;
- chapter climax / major mandatory boss: highest share.

Exact individual fight values wait for the chapter-by-chapter combat audit. The chapter total is what matters for this pacing model.

## 8. Base-line pacing proof for an early recruit

Assume an early recruit begins Base CL1 and keeps Base Focus throughout Chapters 1–6. Combining expected ordinary random CEXP with the authored-combat budget gives:

| End of chapter | Chapter CEXP | Cumulative Base CEXP | Resulting neighborhood |
|---:|---:|---:|---|
| Ch1 | 450 | 450 | CL3 |
| Ch2 | 556 | 1,006 | CL5 |
| Ch3 | 642 | 1,648 | CL6 |
| Ch4 | 728 | 2,376 | CL8 |
| Ch5 | 860 | 3,236 | CL9 |
| Ch6 | 920 | **4,156** | **CL11** |

This is the intended pre-Accord result: an early recruit is highly developed but **not finished** when Subclasses arrive.

If that character ignores the new Subclass and continues Base Focus:
- Ch7 expected gain = 978 → total 5,134 → CL12;
- only 866 more CEXP is needed for Base CL13;
- Base Ultimate therefore lands naturally during Ch8 rather than before the Accord.

## 9. Fresh post-Accord Subclass pacing proof

Assume a fresh Subclass begins at CL1 at the start of Ch7 and the character keeps Subclass Focus for essentially all mandatory-route combat.

| End of chapter | Chapter CEXP | Cumulative Subclass CEXP | Resulting class level / milestone |
|---:|---:|---:|---|
| Ch7 | 978 | **978** | **CL5** — donor advanced-equipment milestone reached |
| Ch8 | 1,000 | **1,978** | **CL7** — Ability 3 online |
| Ch9 | 968 | **2,946** | **CL9** — Ability 4 online |
| Ch10 | 1,104 | **4,050** | **CL10** — Equipment Mastery becomes available |
| Ch11 | 1,258 | **5,308** | **CL12** — Trait III online |
| Ch12 | 700 | **6,008** | **CL13** — Subclass Ultimate |

This is the strongest current proof that **CL13 is enough to last to approximately character Level 55**:
- the donor equipment package becomes usable during Ch7 rather than instantly;
- Ability 3 arrives in Ch8;
- Ability 4 arrives in Ch9;
- **Equipment Mastery / donor Relic access becomes available at CL10 around the end of Ch10**;
- Ability 5 arrives early in Ch11;
- Trait III arrives by late Ch11;
- the Subclass Ultimate lands naturally in Ch12 around the campaign-only Level ~55 finish.

The 8-CEXP overrun is intentional rounding noise and does not justify changing the 6,000 threshold.

## 10. Light / Standard / Heavy implementation rule — provisional

Do **not** hardcode the chapter target in Section 6 as the reward for every formation.

Preferred implementation principle:
- Light formations award below the chapter target;
- Standard formations sit near the chapter target;
- Heavy formations award above the chapter target;
- the actual local formation weights should be normalized so expected CEXP per random victory remains close to the chapter target.

Exact Light / Standard / Heavy values should be derived only after the final formation weights are inspected. This avoids accidentally inflating CEXP because a chapter happens to use more Heavy formations.

## 11. Elite / boss / Hunt reward bands — provisional direction

Individual authored rewards should remain compact. Do not copy Character EXP values into CEXP.

Working qualitative hierarchy:
- named/tough authored encounter < Elite/miniboss < story boss < chapter climax;
- Regional Hunt should be a meaningful optional CEXP injection but should not trivialize several Class Levels by itself;
- Major Hunt should award more than a Regional Hunt and can accelerate completion for optional-heavy players;
- optional route combat to a Hunt also contributes normal selected-class CEXP.

Exact numeric Hunt and boss tables remain pending because they should be fit to the actual number of authored fights and optional battle routes rather than invented in isolation.

## 12. Split-Focus behavior

Because only the selected class receives CEXP, the model intentionally creates different outcomes:

- **Base-focused after Accord:** finishes Base CL13 during Ch8, then can begin Subclass afterward.
- **Subclass-focused after Accord:** reaches Subclass CL13 around the Ch12 / Level ~55 campaign finish.
- **50/50 Base/Subclass split:** neither line is expected to finish as early; optional combat and Levels 56–60 become useful completion space.
- **Optional/Hunt-heavy:** may complete one line earlier and has enough additional combat to make finishing both lines realistic without requiring a separate postgame leveling campaign.

Class completion is therefore a player-priority result rather than an automatic consequence of character level.

## 13. Reserve-party CEXP — current working decision

**All recruited permanent party members receive 100% of awarded CEXP for their own currently selected class, whether active or in reserve.**

This rule is separate from which class receives the CEXP:
- the character's **selected Base or Subclass Focus** receives the full CEXP reward;
- the unselected class receives **0 CEXP**;
- being one of the four active combatants is **not** required for CEXP;
- being benched does not reduce the reward;
- unrecruited characters do not accumulate CEXP offscreen and instead join at their authored starting Base CL / threshold;
- temporary/guest allies do not enter the permanent class-progression economy unless separately authored.

Design reasons:
- the permanent roster has six characters but only four active battle slots;
- reduced reserve CEXP would punish normal rotation and encourage keeping the same four characters active merely to protect class progression;
- reciprocal training is meant to create build choice, not a benching tax;
- full reserve CEXP keeps the meaningful decision on **which class each character is training**, rather than whether the character happened to be active for a specific battle.

This does **not** make both class lines advance together. A reserve character still trains only the class currently selected for that character.

## 14. Mastery / Relic interaction — current working decision

**Equipment Mastery is gated at Subclass CL10.**

- Equipment Mastery remains **Subclass Mastery Node 4**.
- Reaching **Subclass CL10** makes Equipment Mastery available on that character's Mastery board.
- The character must still acquire the node through the Mastery system; CL10 itself does not silently grant the node for free.
- Once Equipment Mastery is acquired, the character gains access to the **donor Base tradition's Relic equipment**.
- Ordinary donor equipment remains the earlier CL1–5 progression and is not delayed to CL10.
- Legacy access remains later and separate from Equipment Mastery.

The old Synthesis prerequisite of both classes at CL12 must still be reconsidered for the new CL13 cap. Do not automatically convert that requirement without the dedicated Synthesis/Legacy pass.

## 15. Next numerical / mastery pass

1. inspect final Light / Standard / Heavy formation weights and turn the chapter averages into exact tier rewards;
2. assign exact CEXP to mandatory authored battles while preserving each chapter budget;
3. assign Regional Hunt and Major Hunt CEXP;
4. simulate Base-focused, Subclass-focused, 50/50, and optional-heavy paths with exact encounter data;
5. reconcile the remaining Mastery-node gates plus Synthesis / Legacy progression against CL13;
6. only then promote the CEXP model into master canon.
