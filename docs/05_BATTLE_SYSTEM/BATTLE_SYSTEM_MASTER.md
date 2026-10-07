# Diyse — Battle System Master

**Status:** ACTIVE BATTLE-SYSTEM AUTHORITY  
**Authority:** current battle-system owner plus later explicit approved corrections.  
**Purpose:** single consolidated specification for current global battle rules.

This file is the canonical owner for global battle-system behavior. Supporting files in this folder are routing/index surfaces only and must not define parallel combat rules.

## 1. Structural foundation

Diyse uses an ordered **TURN / EXECUTION** timeline.

- **TURN** = a combatant receives a command opportunity.
- **EXECUTION** = a previously selected queued action resolves.
- Time pauses for player command selection when a player TURN arrives.
- A selected action either resolves immediately or creates a future EXECUTION marker.
- Other TURNs and EXECUTIONs may occur before a queued action resolves.
- A combatant's next TURN is scheduled when the command is selected, not when the queued action executes.
- A combatant cannot receive another command TURN while one of its own selected actions is still pending. If necessary, its calculated next TURN is clamped to after its queued EXECUTION.

Core sequence:

`TURN → choose command → EXECUTION if queued → next TURN`

The primary structural influences are Final Fantasy X's ordered-turn clarity and party swapping plus Grandia's queued execution, timing pressure, Delay, and Interrupt. There is no universal Octopath-style Break loop.

## 2. Action timing

Execution categories:

- **Immediate:** 0 timeline units
- **Fast:** 25
- **Standard:** 50
- **Slow:** 75

Return categories:

- **Fast:** ×0.75 personal TURN spacing
- **Normal:** ×1.00
- **Heavy:** ×1.25

Execution and Return are separate balance axes. Default native Ability timing is **Standard Execution / Normal Return** unless explicitly authored otherwise.

The timeline preview should show both the selected action's projected EXECUTION and the user's projected next TURN before confirmation.

### Speed-to-TURN-spacing formula

Speed controls TURN frequency, not Execution delay.

`Personal Normal TURN Spacing = 50 + (100 × R / (R + Speed))`

Current design constant:

- **R = 200**

Representative spacing:

- Speed 50 → 130
- 100 → 116.7
- 200 → 100
- 300 → 90
- 400 → 83.3
- 600 → 75
- 999 → ~66.7

After normal spacing is calculated:

1. apply the action's Return multiplier;
2. apply Quick/Slow to the new TURN spacing;
3. schedule the next TURN.

An already-placed queued EXECUTION marker is not retroactively moved by later Speed, Quick, Slow, stat, elemental, Ward, or similar ordinary state changes. Only explicit timeline mechanics such as Delay, Stuck, authored acceleration, or Interrupt can alter/cancel it.

## 3. Universal commands

Every active permanent has:

- **Attack**
- **Abilities**
- **Cards**
- **Item**
- **Defend**
- **Swap**

Prime manifestation is a separate special access path.

### Attack

- Immediate Execution
- Normal Return
- 0 MP
- 1.00 Potency baseline
- uses the character's physical offensive rules/final equipped stats
- can crit by default
- no inherent Delay or Interrupt

### Defend

- Immediate Execution
- Fast Return
- 0 MP
- begins immediately and lasts until that character's next TURN begins
- reduces incoming direct physical and magical damage by **40%**
- does not reduce indirect fixed/percentage damage such as Poison, Wounded self-damage, or Doomed
- does not inherently prevent status
- stacks multiplicatively with Ward

Defend + Ward: `0.60 × 0.75 = 0.45`, so the user takes 45% of normal direct physical/magical damage.

### Item

Default Item timing is **Immediate / Normal**. Specific exceptional items may explicitly override it.

## 4. Party, swapping, reserves, and KO replacement

Diyse has **6 permanent party members**, with **4 active** and **2 reserves**.

### Voluntary Swap

- only the active TURN owner may initiate Swap;
- the target reserve must be conscious;
- the incoming reserve inherits the exact current TURN and may act immediately;
- the incoming reserve's former hidden reserve TURN marker is canceled;
- the outgoing character keeps HP, MP, equipped Cards, buffs/debuffs/statuses and other persistent battle state;
- the outgoing character begins a hidden reserve cycle from the exact swap point;
- a character with an unresolved queued action cannot receive another command TURN and therefore cannot initiate Swap before that action resolves;
- a KO'd active cannot initiate a normal Swap.

### Hidden reserve cycle

Reserve characters remain on a hidden personal timing cycle. Hidden reserve TURNs:

- process TURN-triggered effects such as Poison and Regen;
- decrement affected-TURN durations;
- advance Doomed;
- grant no command opportunity.

The first hidden reserve TURN after a voluntary swap-out is scheduled from the exact swap point using current Personal Normal TURN Spacing with normal Quick/Slow rules.

### Emergency replacement after active KO

If an active character is KO'd and a conscious reserve exists:

- finish the current authored action/reaction sequence first;
- then the player chooses a conscious reserve if more than one is available;
- that reserve takes the vacated active slot;
- the KO'd member moves to reserve;
- this is not a normal Swap;
- the incoming reserve does **not** inherit the KO'd character's lost TURN/timeline position;
- the incoming reserve keeps only its already-scheduled hidden reserve TURN and waits for it before receiving a command.

A reserve is never inserted into the middle of a multi-hit or mixed-effect action. Remaining hits do not transfer to the incoming reserve unless the action is explicitly authored to retarget across separate targets.

The party is defeated only when no active or reserve party member can continue.

## 5. Delay and Interrupt

Ordinary damage does not automatically interfere with queued actions.

Queued actions are authored as:

- **Interruptible** — eligible for Delay and Interrupt;
- **Delay-only** — eligible for Delay but not Interrupt;
- **Uninterruptible** — immune to ordinary Delay/Interrupt.

### Delay

Standard Delay displacement is **25% of the affected unit's normal TURN spacing**. An effect specifies whether it targets a TURN marker, an EXECUTION marker, or either.

A single TURN or EXECUTION marker may receive at most **2 standard Delays**. A newly created marker receives a fresh count. Stuck's own execution push is separate and does not consume the standard two-Delay cap unless an effect explicitly says otherwise.

Boss baseline standard Delay displacement is **50% of the ordinary standard displacement**, i.e. 12.5% of normal TURN spacing, unless the phase is authored Normal/Resistant/Immune differently.

### Interrupt

Interrupt cancels an eligible queued EXECUTION. The user's already-scheduled next TURN does not move earlier.

There is no universal Interrupt meter.

Queued MP actions commit their full cost at selection. If a queued MP action is canceled **before EXECUTION**, its final cost is **50% of listed MP**, rounded up for odd costs. This includes formal Interrupt, actor KO, or another explicit pre-execution cancellation unless an owning effect says otherwise.

If an action reaches EXECUTION, it pays 100% even if an authored execution-time failure occurs. Delay does not refund MP because the action remains pending.

## 6. Core combat stats

Core stats:

- **HP**
- **MP**
- **Strength** — native physical offense
- **Magic** — native magical offense
- **Intelligence** — all scalable Standard Card numerical output
- **Defense** — physical mitigation
- **Spirit** — magical mitigation and native healing potency
- **Speed** — TURN spacing

There are no core Accuracy, Evasion, Critical Chance, Luck, Status Potency, or Status Resistance stats.

Source stat and output/mitigation type are separate concepts. A physical-type Card may scale from Intelligence and still resolve against Defense.

Technical non-HP stat ceiling: **999**.  
Player HP technical ceiling: **9,999**.  
Player MP technical ceiling: **999**.

Practical non-HP progression targets:

- early ~20–80
- mid ~70–180
- late ~150–350
- specialized ~350–500+

The final player level cap is **not fixed by the battle system**.

## 7. Equipment

Weapons/equipment raise the character's visible combat stats directly and may grant explicit passives. There is no separate hidden Weapon Power term layered onto the damage formula.

## 8. Damage, healing, potency, variance, and caps

### Direct scalable damage

`Base Damage = Potency × Offensive Stat × (K / (K + Defensive Stat))`

Current design constant:

- **K = 300**

Typical mapping:

- native physical: Strength vs Defense
- native magical: Magic vs Spirit
- scalable Standard Card output: Intelligence as source; the Card defines physical/magical/other output type

Modifier order:

1. final equipped offensive stat including buffs/debuffs;
2. Potency;
3. Defense/Spirit curve;
4. elemental affinity;
5. Ward/direct mitigation;
6. critical multiplier if eligible;
7. explicit late modifiers;
8. variance;
9. final rounding.

Direct scalable damage uses **95%–105%** variance. Fixed/percentage/status effects are exact unless explicitly authored otherwise.

A successful direct damaging hit deals at least **1 HP** unless Null, explicit immunity, full prevention/negation, or an explicit zero-damage rule applies.

There is no arbitrary 9,999 damage-number cap. Damage may exceed 9,999 if formulas produce it; HP simply cannot fall below 0.

### Potency scale

- 0.50–0.74 light
- 0.75–0.99 below-standard
- 1.00 standard single-target baseline
- 1.01–1.49 above-standard
- 1.50–1.99 heavy
- 2.00–2.99 very heavy / major commitment
- 3.00+ exceptional / finisher / Prime / boss-signature / heavily conditioned

The scale is open-ended rather than capped at 3.00.

Routine all-enemy guidance: ~0.60–0.85.  
Strong all-enemy guidance: ~0.90–1.20.

### Healing

Native scalable healing uses **Spirit**. Scalable healing Standard Cards use **Intelligence**.

`Healing = Potency × Source Stat`

- normal scalable healing uses 95%–105% variance;
- no Defense/Spirit mitigation;
- no crit by default;
- no elemental modifier by default;
- Regen is exact;
- normal healing cannot exceed Max HP;
- excess healing is lost;
- overhealing does not create a hidden barrier/temp-HP layer.

### Multi-hit and mixed effects

Each hit resolves independently:

1. hit validity;
2. damage/crit/element/modifiers;
3. immediate HP loss;
4. on-hit effects;
5. KO check before the next hit.

If a target reaches 0 HP, it is KO'd immediately and remaining hits against that target stop unless the action explicitly continues against KO'd targets. Other valid targets continue.

Mixed-effect actions resolve in explicit authored order. If no order is specified, default:

1. damage;
2. target status/debuff;
3. user/self effect;
4. field/global effect.

### Drain / lifesteal

Drain heals from **actual HP removed**, not theoretical overkill damage. A hit that calculates 1,000 damage against a target with 300 HP remaining deals 300 actual HP damage for drain purposes. Ordinary drain cannot revive a KO'd user unless explicitly authored to do so.

## 9. Critical hits and hit rules

### Critical

- base chance: **5%**
- multiplier: **×1.5**
- no permanent Critical Chance stat
- Attack can crit by default
- Abilities/Cards define crit eligibility explicitly
- healing does not crit by default
- crit has no automatic timeline effect

### Hit / miss / evade

There is no universal Accuracy-vs-Evasion roll. A legal valid action hits by default.

Miss/Evade only occur through explicit authored effects. Sure Hit may override an eligible Evade effect when authored to do so.

## 10. Elements

Standard elements:

- Fire
- Ice
- Lightning
- Earth

No Water element.

Affinity multipliers:

- Weak ×1.5
- Neutral ×1.0
- Resist ×0.5
- Null ×0

There is no universal elemental wheel. Affinities are authored per target/encounter. Elements and statuses are separate; Fire does not automatically apply a burn status, etc.

## 11. Status system

Timed status duration is normally based on the **affected unit's own TURNs**, including hidden reserve TURNs.

Same-status reapplication refreshes to full duration without stacking potency/copies unless explicitly authored otherwise. Opposing paired states cancel to neutral where defined.

A timed effect only decrements at TURN end if it was already active when that TURN began. A timed effect newly applied or refreshed during that unit's own current TURN does not immediately lose one count.

Ordinary temporary buffs/debuffs/statuses clear on KO. Revival does not restore them.

Status application uses:

`final application chance = action base chance × target susceptibility`

Susceptibility:

- Vulnerable ×1.5
- Normal ×1.0
- Resistant ×0.5
- Immune ×0

Final chance caps at 100%. There is no hidden Status Potency/Resistance stat.

### Quick

- TURN spacing ×0.75
- 4 affected TURNs
- no Execution-delay change
- does not move an already queued EXECUTION
- mutually exclusive with Slow

### Slow

- TURN spacing ×1.25
- 4 affected TURNs
- no Execution-delay change
- mutually exclusive with Quick

### Stuck

- 4 affected TURNs
- unit still commands normally
- when one of its queued EXECUTIONs arrives, 40% internal trigger chance
- trigger pushes that EXECUTION later by 25% of normal TURN spacing
- does not cancel
- Immediate actions are unaffected
- at most one Stuck push per queued action
- if Stuck expires before EXECUTION, there is no Stuck check

### Asleep

- 3 affected TURNs
- denies command TURNs
- a queued action already pending remains pending
- if the unit wakes before EXECUTION, the action resolves normally
- if still Asleep at EXECUTION, the action fails
- direct damage wakes after damage resolves
- passive DoT does not wake by default
- healing does not wake

### Poison

- 6% Max HP at each afflicted TURN
- 5 affected TURNs
- total 30% if uninterrupted
- ignores Defense/Spirit/Ward
- no crit
- may KO
- processes in reserve

### Wounded

- 4% Max HP self-damage whenever the afflicted unit successfully resolves an action
- canceled queued action produces no Wounded proc
- afflicted unit takes +10% physical damage
- no magical-damage increase
- self-damage ignores Defense/Spirit/Ward, cannot crit, and may KO
- no fixed duration; persists until cured or battle end

When inflicted, record the target's HP immediately after the inflicting effect fully resolves. Wounded clears only when healing later brings current HP to at least that recorded threshold. Regen contributes. Reapplication does not stack the 4%/+10%; threshold becomes `max(existing threshold, HP after new Wounded effect resolves)`.

### Sealed

- 3 affected TURNs
- blocks future selection of all native Abilities
- does not block Attack, Cards, Item, Defend, Swap, or Prime
- does not cancel an already queued Ability

### Ward

- incoming direct physical and magical damage ×0.75
- 3 affected TURNs
- separate mitigation layer
- refreshes; does not stack

### Regen

- heals 6% Max HP per affected TURN
- 5 affected TURNs
- total 30%
- exact; no crit
- unaffected by Defense/Spirit/Ward/elements
- processes in reserve
- contributes toward Wounded's healing threshold

### Doomed

- visible 5-TURN countdown
- decrements on afflicted TURN
- 0 → KO
- no direct queued-EXECUTION effect

### Stat Up / Down

Applicable axes:

- Strength
- Magic
- Intelligence
- Defense
- Spirit

Up = **+25%**. Down = **−25%**. Duration = **4 affected TURNs**.

There is no generic Speed Up/Down; Quick and Slow own TURN-frequency changes. Same-state reapplication refreshes. Opposing Up/Down cancels the existing state to neutral.

## 12. TURN-start and TURN-completion order

When a TURN arrives:

1. KO/absolute-state validity check;
2. positive TURN-start healing such as Regen;
3. passive TURN-start damage such as Poison;
4. countdown/lethal checks such as Doomed;
5. TURN-denial checks such as Asleep;
6. other TURN-start triggers;
7. command selection if conscious/allowed;
8. TURN completion and duration decrement.

If the unit reaches 0 HP during TURN-start processing, stop remaining TURN-start processing unless an effect explicitly resolves simultaneously.

A TURN is complete when that TURN's command opportunity is fully processed, not when a queued action later executes. A denied TURN still counts as an affected TURN and schedules the next TURN normally. Hidden reserve TURNs use the same duration rules without opening command selection.

## 13. Battle start and exact timeline ties

Normal battle start:

1. calculate each active combatant's Personal Normal TURN Spacing;
2. use those values as provisional first-TURN positions;
3. find the earliest provisional first TURN;
4. shift the entire opening timeline left so the earliest begins at 0;
5. preserve relative spacing.

Exact TURN-position ties:

1. party side before enemy side;
2. party ties use stable active-slot order;
3. enemy ties use stable encounter slot order.

If an EXECUTION and TURN share the same exact timeline position, **EXECUTION resolves first**. Multiple EXECUTIONs at the same position resolve in stable order of scheduling.

Ambushes, preemptive strikes, scripted openings, or encounter-specific rules may explicitly override normal initialization.

## 14. Targeting and automatic retargeting

Core target patterns include:

- Self
- Single Ally
- All Active Allies
- Single Enemy
- All Enemies
- Any Single Combatant
- All Combatants
- Random Enemy / Ally / Combatant
- Single Reserve Ally where legal
- All Party Members when explicitly authored

Reserves are normally off-field and invalid targets for hostile attacks/effects and ordinary buffs. Healing and cleansing may target conscious reserves by default. Revival/special recovery may target KO'd reserves when the action explicitly supports it.

At EXECUTION, a single-enemy action rechecks the original target. If invalid, it automatically selects the next valid enemy in stable encounter target order, wrapping once if needed. Ally-targeting and other non-enemy actions do not auto-retarget unless explicitly authored.

All-target actions affect the valid group that exists at EXECUTION.

## 15. Queued-action evaluation

Queued actions do **not** snapshot combat stats or defenses at selection.

At EXECUTION use current:

- acting offensive stat;
- target Defense/Spirit;
- buffs/debuffs;
- Ward/Defend;
- elemental affinity;
- target validity.

What is fixed at selection:

- action identity;
- listed MP cost;
- chosen initial target/group;
- authored Execution category;
- authored Return category;
- any action-specific mode/branch chosen at command selection.

## 16. Items

- shared inventory;
- only an active TURN owner uses an item;
- default timing Immediate / Normal;
- healing/cleansing items may target conscious reserves;
- revival items may target KO'd party members including reserves when supported;
- offensive items target active enemies only by default;
- ordinary Immediate items are consumed on resolution;
- exceptional queued items canceled before EXECUTION are not consumed;
- if a queued item reaches EXECUTION but has no valid target under its rules, it is consumed unless explicitly authored otherwise;
- ordinary item magnitudes are fixed/percentage-based unless the item explicitly names a scaling stat;
- no universal per-battle item limit/cooldown.

## 17. MP economy

One normal MP pool per character powers native Abilities and Standard Cards.

- HP/MP persist between battles;
- no universal automatic MP restore on victory;
- full rest restores HP/MP;
- items/Abilities/Cards/equipment/passives may restore MP;
- Attack, Defend, and Swap cost 0 MP;
- ordinary costs are fixed values rather than percentages of Max MP;
- native Abilities generally cost less than comparable Standard Cards;
- no baseline MP gain from attacking, defending, taking damage, or waiting.

Practical MP bands:

- early 50–110
- mid 100–200
- late 180–330
- high-MP specialists 330–500

Native Ability cost guidance:

- low 4–10
- moderate 11–24
- high 25–45
- exceptional 46+

Standard Card guidance:

- low 8–16
- moderate 17–32
- high 33–55
- exceptional 56+

## 18. Battle victory, defeat, escape, revival, and simultaneous outcomes

### Battle start/end

HP/MP and equipment/Card loadouts carry into battle. KO does not automatically clear before battle. Ordinary temporary battle buffs/debuffs/statuses do not carry between battles unless an effect is explicitly persistent.

Victory:

- clear ordinary temporary battle buffs/debuffs/statuses;
- discard queued actions/timeline markers;
- preserve post-battle HP/MP;
- KO remains KO unless a specific victory rule revives;
- rewards belong to the progression/reward domains.

### Defeat

Defeat occurs when no active or reserve party member can continue, unless the encounter defines a special failure state.

### Revival

Revival restores the authored HP amount but grants no free immediate TURN.

- revived active: schedule next TURN from the exact revival point using current Personal Normal TURN Spacing / Normal Return;
- revived reserve: restart its hidden reserve cycle from the exact revival point;
- lost queued actions/old TURNs are not reclaimed;
- temporary states cleared by KO do not return.

### Simultaneous resolution

Battle outcome is checked after the current atomic authored action/effect/reaction sequence finishes, not in the middle of it.

- party can continue / enemies cannot → Victory
- enemies can continue / party cannot → Defeat
- neither side can continue after the same completed sequence → Mutual KO, default **Defeat** unless encounter-specific story rules say otherwise.

### Escape

Eligible battles allow Escape from a character TURN.

Failed Escape:

- Immediate
- Heavy Return

Base chance:

`60% + 40% × ((Party Avg Speed - Enemy Avg Speed) / (Party Avg Speed + Enemy Avg Speed))`

Clamp base chance to 30%–90%. Each failure adds +15 percentage points; final chance caps at 95%. Only conscious combatants count in average Speed.

Successful Escape ends battle, clears ordinary temporary battle states, preserves HP/MP, and grants no normal victory rewards. Boss/locked encounters may disable Escape.

## 19. Reactions, counters, Reflect, and redirection

Automatic counters/reactions do not normally interrupt the middle of the triggering action.

- record eligible reactions while the action resolves;
- finish all hits/linked effects first;
- then resolve pending reactions before the next normal timeline marker;
- multiple reactions resolve in trigger order;
- reactor must still be conscious/eligible;
- reaction does not create a normal TURN or change an already-scheduled next TURN unless explicitly authored;
- prevent recursive infinite reaction loops by default.

### Reflect

- checked when the relevant hit/effect would resolve;
- reflected single-target hostile effect normally returns to original source;
- recalculate against the new recipient's Defense/Spirit, affinities, Ward, Defend, etc.;
- preserve original offensive source stat, Potency, element, and crit eligibility;
- no new TURN/EXECUTION marker;
- one reflection maximum by default;
- self/ally/healing/field effects and explicitly Unreflectable effects ignore Reflect;
- multi-hit normally checks Reflect per hit.

### Damage redirection

- resolves before mitigation;
- receiving target uses its own defenses/affinities/states;
- redirected recipient is the actual target for on-hit and damage-triggered reactions;
- one redirection maximum per hit/effect by default;
- no protector loops.

Priority:

`target/retarget → redirection → Reflect → damage/effect resolution`

## 20. Enemy and boss timing

Enemies use the same TURN/EXECUTION framework, Speed scheduling, Execution categories, Return categories, queued-action limits, Delay/Interrupt classes, and marker visibility rules as players unless an explicit encounter exception applies.

Queued enemy intent is normally visible, including target/group when logical. Concealed/deceptive actions must be explicitly authored.

Bosses do not receive blanket immunity to Delay/Interrupt. Ordinary queued boss actions may be Interruptible; stronger/signature actions may be Delay-only or Uninterruptible. Current eligibility is shown on the timeline.

## 21. Interactive timeline inspection

Visible timeline markers are interactive planning surfaces.

Queued EXECUTION inspection should show at minimum:

- actor;
- action name/intent if not intentionally concealed;
- target/group when not concealed;
- Execution category;
- current Interruptible / Delay-only / Uninterruptible state;
- whether standard Delay applications remain under the two-Delay cap;
- visible timing/special conditions.

TURN inspection may show projected TURN, Quick/Slow, Delay eligibility, and remaining Delay applications.

Inspection costs no TURN/time. When selecting Delay or Interrupt, legal markers should be directly selectable.

## 22. Faces and Standard Cards — system-level rules

Current Faces:

- Might
- Elements
- Grace
- Perception
- Memory
- Ruin

Combat lanes:

- **Might:** physical force, impact, aggression, vitality
- **Elements:** elemental offense/affinity interaction
- **Grace:** healing, protection, recovery, stability
- **Perception:** Rogue/Assassin/Hunter space; precision, criticals, opportunistic timing, especially Interrupt
- **Memory:** Time Mage/Blue Mage/Copy space; Quick, Slow, Delay, Stuck, duration manipulation, delayed/echo effects, controlled recall/copy
- **Ruin:** destructive, degrading, dangerous/high-risk effects

Perception has the strongest association with canceling eligible queued actions. Memory has the strongest association with manipulating when actions happen and how long effects persist.

Each permanent character has exactly **4 Standard Card slots** unlocked at:

- Base CL1
- Base CL4
- Base CL8
- Base CL12

Standard Cards:

- are unique named Cards; no duplicate ownership/equipping;
- one Card may be assigned to only one character at a time;
- assignment happens outside battle;
- loadouts cannot change mid-battle;
- every equipped Standard Card grants at least a stat bonus, passive, or both;
- equipped stat bonuses remain part of the character's stats in reserve;
- character-bound passives do not affect the active party from reserve unless explicitly authored;
- use MP and generally cost more than comparable native Abilities;
- use Intelligence for all scalable numerical output where scaling applies;
- use the normal TURN/EXECUTION framework unless explicitly overridden.

Exact Standard Card content is intentionally parked for the dedicated Card-content pass.

## 23. Native Ability architecture — system-level rules

Native Abilities use MP. There is no default class-specific combat resource.

Target kit sizes:

- Base class: **6–8 active Abilities**
- Subclass: **4–6 active Abilities**
- fully developed native toolkit: roughly **10–14 actives**
- Base class: **4 passives**
- Subclass: **3 passives**
- fully developed total: **7 passives**

Starting characters begin with **3 base active Abilities + 1 base passive**. Subclass access immediately grants **2 subclass active Abilities + 1 subclass passive**. Later joiners may enter with more already unlocked according to campaign progression.

Base/subclass Abilities share one top-level **Abilities** command with visible origin tags rather than separate submenus.

Every native Ability must explicitly define MP cost, Execution, Return, targeting, Potency/fixed magnitude, physical/magical/other output, element, crit eligibility, queued-action interaction class, status chance, timeline effects, and conditions/special rules.

Existing Ability/passive content is source material, not a constraint. It may be kept, reworked, renamed, merged, moved, or replaced during the dedicated character-kit rebuild. Exact CL unlock thresholds remain parked.

## 24. Prime system — stable battle foundation

Exact internal Prime manifestation TURN sequencing is **parked** and is not current authority yet.

Stable rules:

- exactly 12 Primes: 6 Story + 6 Major-Hunt;
- Story progression: Recovered → Awakened only;
- Major-Hunt Primes are acquired Awakened;
- no Prime XP, levels, duplicates, or material progression;
- Chapter 4 Prime battle-loadout access: 1 Prime slot per permanent;
- after Sixfold Volition at end of Chapter 7: 2 Prime slots per permanent;
- Story bearer association is narrative/thematic, not battle-use owner-lock;
- Major-Hunt Primes are not owner-locked;
- invocation costs 0 MP;
- Prime commands cost 0 MP unless a specific Prime explicitly defines another internal restriction;
- each Prime identity has 1 use until restored;
- spent/Ready persists across battles;
- battle end/new battle do not restore spent Primes;
- valid full rest or checkpoint-area restoration restores eligible spent Primes;
- explicit restoration effects may restore spent Primes;
- Emergency Kit restores every acquired Story and Major-Hunt Prime to Ready without changing progression state;
- same-bar phases and fresh-HP enemy bodies/forms do not automatically restore Prime uses.

Manifestation temporarily replaces the normal active party; party HP/MP/persistent state are preserved while manifested. Exact party hidden-cycle behavior and Recovered/Awakened sequence timing are part of the parked Prime pass.

Every Prime has an automatic signature effect when manifestation ends; exact finisher timing and Delay/Interrupt interaction remain part of that parked sequencing pass.

After demanifestation, Prime invocation enters a **party-wide lockout measured by the invoking character's next 3 personal TURNs**.

- invoking character is cooldown owner;
- nobody may manifest any Prime during the lockout;
- each owner TURN reduces it by 1;
- hidden reserve TURNs belonging to the owner count;
- queued EXECUTIONs do not count;
- swapping itself does not add a count;
- a denied owner TURN counts if that TURN occurred;
- after the third owner TURN is processed, the lockout ends;
- restoring a spent Prime does not bypass the active lockout.

No placeholder three-Prime-round or three-normal-round sequencing rule is authoritative until the dedicated Prime pass is completed.

## 25. Current numerical design targets

Player HP practical bands:

- early 300–700
- mid 800–1,600
- late 1,600–3,000
- high-HP/defensive builds 3,000–4,500

Current formula constants **R = 200** and **K = 300** are locked design targets subject to later simulation certification; numerical certification may tune them without reopening the system architecture.

## 26. Remaining work

The global battle-rule foundation is closed. Remaining work is deliberately limited to:

- exact Standard Card roster/content;
- dedicated Prime manifestation/TURN sequencing and exact Prime kits/finishers;
- exact character native Ability/passive rebuild and CL unlock thresholds;
- item catalog and exceptional item-specific effects;
- numerical certification of stat curves, R/K, Potencies, MP costs, HP/MP growth, and encounter pacing;
- presentation polish and encounter-specific authored exceptions.
