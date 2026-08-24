# Diyse — Active Engineering Canon Guardrails

This is an implementation-facing summary. It does **not** replace the authoritative canon audits or newer explicit user corrections. If this summary omits a compatible older lock, that lock remains active. If this summary conflicts with a later audit or explicit correction, the later authority wins.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v1.99 / Audit114 — Prime, Combat Element / Status, and Base-Class Normalization Lock**  
**Date:** August 24, 2026

Immediate forward chain:
- **v1.84 / Audit99** — Random-Encounter Runtime Implementation and Production-Readiness Closure.
- **v1.85 / Audit100** — Enemy Asset Reuse and Palette-Swap Production Efficiency Lock.
- **v1.86 / Audit101** — Major Hunt Architecture and Unlock Closure.
- **v1.87 / Audit102** — Major Hunt Difficulty and Progression Balance Closure.
- **v1.88 / Audit103** — Quest Architecture, Character Quest and Ordinary Side-Quest Closure.
- **v1.89 / Audit104** — Reciprocal Class, Synthesis, Legacy, and Legacy-Component Integration Lock.
- **v1.90 / Audit105** — Acuity Face, Story Prime, and Resource Reconciliation Lock.
- **v1.91 / Audit106** — Item, Equipment, Catalog, Economy, and Audit104/105 Reconciliation Lock.
- **v1.92 / Audit107** — Sixfold Volition, Cartographic Mystery, Calder Archive, and Chapter-Structure Reconciliation Lock.
- **v1.93 / Audit108** — Exact World Map, Location Geography, Cerythvale, and The Last Blank Closure.
- **v1.94 / Audit109** — World Map Road, Travel, and Last Shelter Point-of-No-Return Closure.
- **v1.95 / Audit110** — Exact 3D World Map Visual / Spatial Authority Lock.
- **v1.96 / Audit111** — Final World Map, Region Terminology, and Visual Authority Closure.
- **v1.97 / Audit112** — Chapter 10: The Last Blank — Mirena, Eastern Wayfinder, Calder, and Buried Registry Closure.
- **v1.98 / Audit113** — Post-Insertion Chapter Reindex and Late-Game Operational File Reconciliation Lock.
- **v1.99 / Audit114** — Prime, Combat Element / Status, and Base-Class Normalization Lock.

Current combat / Prime / element / status authority:
`docs/canon/AUDIT114_PRIME_COMBAT_ELEMENT_STATUS_AND_BASE_CLASS_NORMALIZATION_LOCK.md`

Current reindex authority:
`docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`

Current Chapter-10 story authority:
`docs/canon/AUDIT112_CHAPTER_10_THE_LAST_BLANK_MIRENA_EASTERN_WAYFINDER_CALDER_AND_BURIED_REGISTRY_CLOSURE.md`

Current final surface-map / region authority:
`docs/canon/AUDIT111_FINAL_WORLD_MAP_REGION_TERMINOLOGY_AND_VISUAL_AUTHORITY_CLOSURE.md`

Current travel / point-of-no-return authority:
`docs/canon/AUDIT109_WORLD_MAP_ROAD_TRAVEL_AND_LAST_SHELTER_POINT_OF_NO_RETURN_CLOSURE.md`

---

# Audit114 combat / Prime firewall — controlling

## Prime progression

Exactly **12 Prime Cards** remain: 6 Story Primes + 6 Major-Hunt Primes.

Prime progression is exactly:

> **Recovered → Awakened**

**Awakened is final. Concordant is removed entirely.**

- Recovered: one strong manifestation action in the current ordinary round, then the manifestation ends.
- Awakened: direct control for exactly **3 Prime rounds**.
- After a Prime ends: **3 full normal-round cooldown** for that Prime identity.
- Each Prime identity may be used once per battle **per genuine boss form**.
- A genuine fresh-HP boss form refreshes Prime use/cooldown state.
- Story Primes are acquired Recovered and later Awaken through mandatory story milestones.
- Major-Hunt Primes are obtained already Awakened.
- No Prime XP, levels, duplicates, upgrade materials, third state, Concordant harmonization, or Concordant duration/HP model remains.
- Old Concordant-gated commands remain in the final Awakened kit where otherwise compatible.

Story Prime progression:
- Last Sentinel / Might / Cyanis — acquired Ch4; Awakens Ch5 Deepforge sovereign chamber.
- Last Cartographer / Acuity / Torren — acquired Ch5; Awakens Ch8 Horizon Vault / western-survey culmination.
- Last Convergence / Elements / Vaelira — acquired Ch6; Awakens end Ch7 Sixfold Volition culmination.
- Last Scribe / Change / Nimera — acquired Ch7; Awakens current Ch11 Custodian / truth archive.
- Last Erasure / Ruin / Seyrik — acquired Ch8; Awakens current Ch12 Reforged March.
- Last Sanctuary / Grace / Ilyra — acquired Ch9; Awakens Ch9 Mercy Is Not Surrender.

Major-Hunt Prime rewards:
- Ashen Whitehorn → Dawn Shepherd / Grace.
- Crownless Siege Marshal → Crownless War Engine → Oathbound Colossus / Might.
- Concordance Guardian → Living Revision / Change.
- Worldscar Leviathan → Prismatic Leviathan / Elements.
- Final Archive Arbiter → Parallax Host / Acuity.
- The Unfinished World / Worldheart → Starfall Engine / Ruin.

## Fixed damage type

Every damaging Ability is authored as exactly one of **Physical / Magical / Hybrid**.

- Do not give ordinary Abilities selectable Physical/Magical expressions.
- Equipment does not decide an Ability's damage formula.
- Hybrid is only for deliberately authored dual-axis actions.
- Element is separate from damage type.
- Weapon-independent Ability legality remains intact.

## Elements

Exactly four standard elements:
- **Fire**
- **Ice**
- **Lightning**
- **Earth**

Water and Wind are removed from the current standard element system.

Linked harmful statuses:
- Fire → Burn
- Ice → Freeze
- Lightning → Stun
- Earth → Staggered

An elemental attack does not automatically inflict its linked status; the action must explicitly carry the rider.

Bleed is non-elemental. Regen is a positive recurring-heal effect.

Exact Weak/Resist damage multipliers, Absorb existence, and standard enemy affinity-profile counts remain open.

## Current universal harmful statuses

Exactly:
- **Burn**
- **Freeze**
- **Stun**
- **Staggered**
- **Bleed**

Removed as universal current statuses/systems include Poison, Confusion, Taunt, Sleep, Silence, Blind, Charm, Fear, separate Shock, Banishment, Instant Defeat, Disable, Jam, Overload, and Corrosion.

There is **no global Break/Stagger meter/system**. `Staggered` means only the Earth-linked harmful status. Older Break/Stagger-contribution language is stale and must be replaced in the relevant later Card/Prime/Ability/equipment pass without recreating the meter under another name.

### Burn
- 3 rounds.
- Ordinary: 3% target Max HP at end of each affected round.
- Reapplication refreshes to 3 rounds.
- No crit; ignores Defense/Spirit; can KO; normal cleanse removes it.

### Freeze
- Target cannot act while Frozen.
- First 2 rounds guaranteed.
- 80% chance to persist into round 3; 80% chance to persist into round 4; max 4 rounds.
- First successful direct Physical hit removes Freeze after that hit.
- Magical/non-Physical damage does not break it merely by dealing damage.
- Cannot refresh while active.

### Stun
- 3 affected turns.
- 40% chance to lose the action on each affected turn.
- Failed roll acts normally.
- Cannot refresh while active.

### Staggered
- 3 rounds.
- Speed −20%.
- Accuracy/Base Hit −20%.
- Evasion −20%.
- Target still acts.
- Reapplication refreshes; does not stack.

### Bleed
- Ordinary: 2% target Max HP when the affected unit successfully takes an action.
- Max one Bleed proc per round.
- Freeze/Stun-lost actions do not trigger Bleed.
- Any successful HP heal of at least 1 removes Bleed after the heal resolves.
- Regen restoring at least 1 HP removes Bleed.
- No stack; no crit; ignores Defense/Spirit; can KO.

### Regen / lifecycle
- Regen potency/duration are source-specific.
- KO clears Burn / Freeze / Stun / Staggered / Bleed / Regen.
- Battle end clears ordinary temporary combat statuses/effects.
- A genuine fresh-HP boss form clears ordinary temporary statuses unless explicit carryover is authored.

## Status application

Base authored bands:
- 10% minor rider
- 20% standard rider
- 35% dedicated status/control
- 50% premium/setup-dependent
- above 50% uncommon and explicitly justified

Matching element/status affinity modifier:
- Weak: +10 percentage points
- Neutral: 0
- Resist: −10 percentage points
- Immune: linked status cannot apply from that elemental hit

Vaelira herself receives +5 percentage points on qualifying Ability applications when her Ability element matches the linked status. This does not automatically apply to Cards, Primes, Items, other characters, or mismatched pairs.

Status Resistance scale:
- Normal 0
- Resistant 5
- Highly Resistant 10
- Exceptional 15
- Immune explicit

Ordinary chance formula:

> Base + element modifier + Vaelira bonus − Status Resistance

Clamp legal ordinary chance applications to 5%–95% except explicit immunity/guarantee/script.

High-rank effect conversion:
- Ordinary: full.
- Elite: full by default absent explicit thematic immunity.
- Regional Hunt: Freeze max 2 rounds; Stun 25% action-loss chance; Staggered full where legal; Burn/Bleed at 75% ordinary damage.
- Major Hunt / mandatory boss: Freeze max 1 round; Stun 20% action-loss chance; Staggered full where legal; Burn/Bleed at 50% ordinary damage.

High-rank effect scaling is separate from application chance; do not blanket-immune bosses just to reduce status power.

Remedy grouping:
- Injury group = Burn + Bleed.
- Control group = Freeze + Stun + Staggered.
- final display names remain open.
- remedies do not remove stat changes, Fields, Guard/Barrier, Hunter's Measure, Imprints, Prepared, or protected/scripted states.

---

# Cyanis / Ilyra Base normalization — controlling

## Cyanis — Crest Knight

Current Base Ability map for the formula / element / status pass:
- CL1 **Crest Strike** — Physical / Neutral / one enemy / no status.
- CL1 **Crest Reprisal** — replaces Guardian Sigil; self-Prepared automatic intercept of the next eligible single-target hostile attack aimed at another active party member, then powerful Physical / Neutral counter; no ally target selection; no status.
- CL1 **Resonant Pulse** — replaces Harmonizing Ward; Magical / Colorless / one enemy / no status.
- CL3 **Sweeping Edge** — replaces Resolute Counter; Physical / Neutral / all enemies / **10% Bleed per target**.
- CL6 **Twin Advance** — replaces Crest Rush; Physical / Neutral / one enemy / exactly 2 hits / no status; no defensive rider or alternate magical route.
- CL9 **Crest Rend** — Hybrid / Neutral / one enemy / **35% Bleed**; old Vulnerability rider removed; exact Hybrid weighting / penetration resolution deferred.
- CL13 **Crest of Companions** — Magical / Colorless enemy damage / no harmful-status rider; preserve compatible established party cleanse/support component.

**Harmonized Crest Trait is not redesigned by Audit114.**

## Ilyra — Blue Warden

- **Mend** — healing only; no element; healing uses Magic, not Spirit.
- **Clear Warding** — no element; removes one eligible ordinary harmful status; current cleanse set Burn / Freeze / Stun / Staggered / Bleed; Status Resistance Up remains a stat change.
- **Renewal** — party healing; no element; healing uses Magic; no automatic Regen added.
- **Warden's Valor** — supersedes the old ally basic-Attack two-strike modification; now Magical / Colorless / one enemy / Magic-scaled / no heal rider / no status rider.
- **Revive** — no element; redundant explicit Bleed-clear text removed because KO already clears temporary ordinary statuses.
- **Lifeline** — Prepared survival effect; no element; recovery uses Magic; Prepared is not an ordinary status ailment.
- **Gentle Continuance** — excess-healing Regen is now **4% Max HP per round for 4 rounds**; compatible established other Trait behavior remains.
- **Dawn Without End** — Magical / Colorless enemy damage; healing uses Magic; cleanses all eligible ordinary harmful statuses; Poison wording removed; applies **5% Max HP Regen for 3 rounds**; preserve compatible established revive/heal/AoE structure.

---

# Current chapter-number firewall — controlling

Chapter 10 — The Last Blank was inserted after Chapter 9.

Therefore:
- former Chapter 10 → **current Chapter 11**;
- former Chapter 11 → **current Chapter 12**;
- former Chapter 12 → **current Chapter 13**.

Current late spine:
- **Ch9** — Larkspire / Crownfall / Rhazek.
- **Ch10 — The Last Blank** — Mirena records lead → Cerythvale → eastern forest → discover Eastern Wayfinder → complete physical map → old Crown excavation → Calder provenance → Registry Warden → Buried Registry → Mirena verification.
- **Ch11** — Crown Engine / Othmar Calder / Custodian / Truth.
- **Ch12 — The Reforged March** — final Black Host campaign / Varkesh / Vhalmarch Forward Hub / Vorathen / Vaelkor / cleanup.
- **Ch13 — The Last Command** — final Ancient domain / Last Weapon Archive / Last Shelter / Reconstituted Entity / Final Severance / ending.

Current operational chapter sources:
- `docs/chapters/chapter_10/CHAPTER_10_THE_LAST_BLANK_STORY_STRUCTURE_LOCK.md`
- `docs/chapters/chapter_11/CHAPTER_11_CURRENT_SCOPE.md`
- `docs/chapters/chapter_12/CHAPTER_12_REFORGED_MARCH_FORWARD_HUB_AND_CLEANUP_LOCK.md`
- `docs/chapters/chapter_13/CHAPTER_13_MACRO_STORY_STRUCTURE_LOCK.md`

Do not use pre-insertion `chapter_11 = Vaelkor campaign` or `chapter_12 = final domain` wording as current implementation authority.

---

# Chapter 10 — The Last Blank — controlling summary

- Target first-clear runtime: approximately **55–65 minutes**.
- Mirena has been auditing strange Crown orders since Chapter 3.
- She finds an old authentic eastern research order and a later `research completed` entry, with the meaningful middle missing.
- Mirena and the party do **not** know Eastern Wayfinder exists when the chapter begins.
- The party travels through Cerythvale and the eastern forest to investigate the old research area.
- They discover **Eastern Wayfinder unexpectedly**.
- Eastern Wayfinder supplies the final eastern cartographic evidence and completes the physical/geographic Ancient map **before** the excavation/boss sequence.
- The party then discovers a substantial old Crown excavation beneath the site that the accessible record chain never describes.
- Calder's Prime research predates the game and predates **any successful Prime activation**.
- Calder's lawful standing recovery order is why the recovered Card was transported to Caelora and therefore why Cyanis's Chapter-0 convoy existed.
- Calder did not choose Cyanis, cause the ambush, or know the Card would activate.
- Nimera reconstructs Calder's connection to the two genuine authorities later combined into the Chapter-3 composite seizure order.
- Mirena verifies the final provenance on return: **Calder was behind the Chapter-3 composite seizure architecture**.
- Calder's old excavation stopped at a protected lower threshold; he approved personnel withdrawal rather than sacrificing the research crew.
- The party goes farther than Calder did.
- Mandatory boss = **Registry Warden**: one HP bar, no adds, no transformation, no boss-only subsystem.
- Beyond is the **Buried Registry**, physically linking geography with custody / authority / jurisdiction / responsibility / transfer.
- Prime classifications appear but no earlier Prime activation or Prime-power explanation is revealed.
- Caelora / Yahtrenhold is disproportionately central to both geographic and administrative patterns.
- Full Crown Engine / Underground Crest Network / Custodian / Entity truth remains for Chapter 11 and later.
- Item rewards, treasure, EXP/CEXP, equipment, economy, and any Chapter-10 Standard-Card reward remain deferred to the item/progression pass.

---

# Current point of no return — controlling

Vaelkor is defeated in **Chapter 12**. His defeat opens the broad final cleanup/preparation state and does not automatically begin Chapter 13.

The player deliberately begins Chapter 13 from the final-operation briefing state, but **Chapter-13 launch is not the irreversible point of no return**.

Audit109 controls:

**Last Shelter → Reactor Galleries = true irreversible threshold.**

Before crossing it, the player may still return to eligible unfinished world content through the approved return-access implementation.

---

# Current Chapter 12 campaign guardrails

- Chapter 12 = **The Reforged March**.
- Current route: **Westguard → The Blackspine crossing → Draevensreach → Vhalmarch → Vorathen → The Veiled Citadel**.
- Varkesh is defeated/captured alive before Vhalmarch becomes the Forward Hub.
- **Cresthaven ↔ Vhalmarch** two-way travel opens after that capture and remains through the post-Vaelkor cleanup state.
- Cresthaven remains the full-service HQ; Vhalmarch is essential-services field staging.
- Regional Hunt #11 — **Throne of Emperor Vaelkor** belongs to Chapter 12; Hunt number remains 11.
- Vaelkor remains **Emperor of the Reforged Host → Sovereign Panoply Unbound**, consciously himself and morally responsible.
- Late Chapter-12 Synthesis-resolution beats:
  - Cyanis ⇄ Vaelira — What Holds, What Changes — Cresthaven.
  - Ilyra ⇄ Seyrik — Keep Them Alive — Vhalmarch recovery area.
  - Torren ⇄ Nimera — Enough to Move — Vhalmarch operations/map area.

---

# Current Chapter 13 finale guardrails

- Chapter 13 = **The Last Command**.
- Surface access: Cresthaven briefing → captured Black Host Territory → Vorathen → Veiled Citadel → excavation descent → Deepest City.
- Final Archive is **not** the mandatory finale entrance.
- Chapter 13 Regional Hunt: **none**.
- Chapter 13 Elite: **Devourer of Names**.
- Mandatory guardian: **Last Weapon Archon**, one HP bar, physical Ancient Diysean guardian.
- Final macro progression: **Deepest City → Deep City → Last Weapon Archive → Last Weapon Archon → Last Shelter → Reactor Galleries → Reactor–Crest Interface → Reconstituted Entity → Crest Integration → The Last Command → Final Severance → ending**.
- Last Weapon Archive reveals exactly one mangled Entity portion survived the ancient convergence/compression/discharge firing.
- Reconstituted Entity is the same sole surviving continuity, not a copy/child/second fragment.
- Final boss = exactly **Reconstituted Entity → The Last Command**, two genuine full-health forms, no third form.
- Final Severance is invented by the modern six during The Last Command, not recovered as an Ancient plan.
- Current Story Prime order uses **Acuity / Last Cartographer**, not Resource / Last Measure:
  1. Last Sentinel / Might — HOLD
  2. Last Convergence / Elements — DISTINGUISH
  3. Last Cartographer / Acuity — MAP
  4. Last Sanctuary / Grace — PRESERVE
  5. Last Scribe / Change — CONTAIN
  6. Last Erasure / Ruin — END
- Final Severance permanently ends all Entity continuity/rebuild paths.
- All six permanent party members survive.

---

# Current world / map terminology

Audit111 controls:
- **BLACK HOST TERRITORY** — Black Host-controlled homeland/territory.
- **THE WESTWAYS** — western Yahtrea.
- **THE GREYSPIRES** — northern Yahtrean mountain region.
- **YAHTRENHOLD** — central/southern royal/historic core. Do not use `The Yahtrenhold`.
- **The Blackspine** — canonical frontier mountain range; not printed on the final map by design.
- **Westguard** — current proper name of the settlement formerly Westreach / Yahtrens Stand.
- **Vhalmarch** — current proper name of the Chapter-12 Forward Hub.

Surface-world macro geography is closed unless explicitly reopened.

---

# Sixfold Volition / class architecture

Formal term: **The Sixfold Volition**. `Sixfold Accord` is deprecated.

- Chapter 6 ends with Seyrik's conditional permanent recruitment.
- Chapter 7 — The Prison of Names — is the first full-six integration chapter.
- Sixfold Volition occurs at end of Chapter 7 / Cresthaven return.
- No permanent character uses a Subclass before the Volition.
- All six Subclasses unlock at the Volition.
- Chapter 8 is the first full mandatory post-Volition Subclass chapter.

Reciprocal pairs:
- Cyanis ⇄ Vaelira
- Ilyra ⇄ Seyrik
- Torren ⇄ Nimera

Current Base/Subclass identities:
- Cyanis — Crest Knight / Crest Arcanist
- Vaelira — Green Arcanist / Axiomblade
- Ilyra — Blue Warden / Vowblade
- Seyrik — Ruin Vanguard / Ruin Warden
- Torren — War Archer / Routeweaver
- Nimera — Cardweaver / Truthshot

Player level cap = **70**. Base and Subclass caps = **CL13**.

No Ability or Ultimate requires a particular equipped weapon.

---

# Faces / Cards / Primes

Current Faces:
- Might
- Elements
- Grace
- **Acuity**
- Change
- Ruin

Exactly **24 Standard Cards**, four per Face. Standard Cards are unlimited-use.

Post-insertion acquisition labels:
- Ch1 2
- Ch2 2
- Ch3 3
- Ch4 3
- Ch5 2
- Ch6 4
- Ch7 1
- Ch8 1
- Ch9 2
- Ch10 **0 currently locked new sources**
- Ch11 3 — Devouring Singularity; Worldsplitter; Decisive Interval
- Ch12 1 — Zero Hour

Story Primes:
- Might — Last Sentinel
- Elements — Last Convergence
- Grace — Last Sanctuary
- Acuity — Last Cartographer
- Change — Last Scribe
- Ruin — Last Erasure

No Prime had ever been successfully activated before the modern story.

---

# Quest / Legacy timing after reindex

Exactly six standalone Character Quests remain optional.

Character Quests and eligible secured Legacy completion remain available while world return remains available, including the Chapter-13 pre-Last-Shelter period.

Secured Legacy release occurs through Cresthaven before the **Last Shelter → Reactor Galleries** irreversible threshold, not at a stale `Chapter-12 point of no return`.

The interaction remains authored restoration/completion, not crafting.

---

# Equipment / item architecture

Audit106 remains controlling where later audits do not alter chapter labels or Audit114 status/remedy rules.

Current practical counts:
- Consumables: **20**
- Ordinary Equipment: **48**
- Relics: **64**
- Legacies: **6**
- Exceptional Equipment: **70**
- Total Equipment: **118**
- Standard Cards: **24**
- Prime Cards: **12**
- General Accessories: **0**

Final raw equipment stats / Level-70 balance remain pending the separate progression/item pass.

---

# Random encounters / combat foundation

Compatible Audit99 rules remain active, including:
- random encounters driven by eligible movement-distance pressure;
- menus/cutscenes/dialogue pause encounter pressure;
- maximum **8 simultaneously active enemies**;
- immediate exact formation repeats suppressed where alternatives exist;
- up to four active party members;
- discrete round-based command combat;
- standard battle frame: party left, enemies right, open center action/VFX lane.

Diyse remains an **HD-2D JRPG** targeting approximately 80 px field sprites and approximately 200–220 px battle sprites, with large high-resolution dialogue portraits.

Target full-game runtime remains approximately **25 hours**, subject to revalidation after the added Chapter 10.

---

# Open work after Audit114

1. Continue the Base-class formula / element / status pass with **Torren → Nimera → Vaelira → Seyrik**.
2. Run the same normalization across all six Subclasses.
3. Normalize all **24 Standard Cards** against the four-element / current-status / no-global-Break model.
4. Normalize all **12 Prime Cards** against the same element/status model and Recovered→Awakened progression.
5. Reconcile enemy, Regional Hunt, Major Hunt, and mandatory-boss Ability/status references.
6. Lock exact elemental Weak/Resist damage multipliers and decide whether Absorb exists.
7. Lock enemy affinity-profile construction rules.
8. Complete exact Ability MP/Power, Hybrid weighting/defense resolution, Level-70 curve placement, enemy stats, equipment stats, and economy/drop work in their dedicated passes.
9. Sweep implementation-facing combat/class/Card/Prime files and tests for Audit114-invalid terminology/assumptions.
10. Detailed Chapter-11 Crown Engine scene production when explicitly resumed.
11. Exact Chapter-10 dialogue / final scene IDs if moving from macro structure into line production.
12. Reference-safe runtime/dialogue stale-term cleanup where implementation identifiers or authored text still use retired geography terms.
13. Exact Chapter-5 Deepforge survey scene and Chapter-8 Westguard survey scene where not yet physically staged.
14. Exact chronology/age span of Calder's older source decrees/custody precedents where still open.
15. Exact Sixfold Volition dialogue scene at end of Chapter 7 if not yet line-produced.
16. Late-game detailed scene numbering and HD-2D production for Chapters 11–13.
17. Full implementation/data regression after the post-insertion chapter-path reindex and Audit114 combat cleanup.

Omission from this summary does not erase compatible older canon. **Audit114, Audit113, Audit112, Audit111, Audit109, Audit107, Audit106, Audit105, Audit104, Audit103, compatible prior canon, exact visual authorities, and newer explicit user corrections control conflicts.**
