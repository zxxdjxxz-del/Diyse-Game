# Chapters 0–4 — HD-2D Conversion Audit, Pass 1

**Status:** APPROVED / CANONICAL PRODUCTION AUTHORITY  
**Date:** August 19, 2026  
**Parent authority:** v1.72 / Audit87  
**Promotion:** v1.73 / Audit88

This document records the approved HD-2D presentation/implementation conversion for completed Chapters 0–4. It does **not** rewrite their approved story, dialogue, combat logic, progression, geography, relationship timing, knowledge firewalls or exact visual masters.

## Cross-chapter master rules

- HD-2D is the sole active presentation target.
- Field characters target approximately **80 px**.
- Battle characters target approximately **200 px**.
- Dialogue uses large high-resolution portraits for facial acting.
- Standard battle frame: active party staggered on the **left**, enemies on the **right**, open center lane for attacks/VFX.
- Undersized early parties use legal positions within the same permanent four-slot left-side grammar; they are not recentered.
- Reserve characters do not stand decoratively at the edge of normal battles.
- Normal exploration generally displays the controlled field character; story-required companions appear through authored staging rather than permanent follower trains.
- Field depth uses authored background/midground/playable/foreground/atmosphere layers, parallax and selective depth geometry.
- Battle backgrounds derive from the field sub-area and reuse small approved composition families rather than one arena per formation.
- Random encounters remain random encounters. HD-2D conversion does not replace them with roaming visible enemies.
- Chapter 0 remains the exception: seven authored tutorial encounters and no normal random-encounter table.
- Fixed authored encounters use the same underlying battle-loader grammar with stronger field setup where appropriate.
- Bosses and Primes may exceed ordinary ~200 px battle scale through layered artwork and temporary authored camera treatment.
- Exact visual masters remain controlling over every derivative sprite, portrait, cut-in and battle asset.
- Exact Yahtrea world-map geography remains untouched.

## Common transition architecture

Use one technical transition family across the early game:

1. **Field/interior transition:** short cut, fade or authored directional transition.
2. **Random battle:** very fast reusable field-to-battle transition with no implied free enemy action.
3. **Fixed encounter:** same loader with authored threat setup.
4. **Boss/Hunt:** bespoke entrance allowed, but still resolves into the standard combat frame.
5. **Prime:** combat remains mechanically active; Prime presentation temporarily changes camera/light/composition, resolves one legal action and returns to the normal battle frame.
6. **Postbattle:** restore the valid exploration state and authored environmental changes.

## Common production-cost rules

Prefer:

- reusable regional environment kits;
- camera-specific environment art;
- prop and environment state swaps;
- lightweight looped particles;
- reusable NPC bases;
- audio to imply offscreen population/machinery/scale;
- selective geometry only where traversal/occlusion needs it;
- modular VFX payloads over shared animation/runtime systems;
- same-body boss escalation through components, overlays and lighting when the boss does not truly become a new body.

Avoid by default:

- fully physically modeled cities;
- seamless giant dungeons merely to imply scale;
- free-camera exploration;
- fluid, crowd, cloth, hair, chain or destruction simulation;
- one unique battle background per encounter formation;
- one bespoke body animation for every Ability;
- giant bespoke cinematics for ordinary scene movement;
- combinatorial art multiplication for six-element content.

## Reusable production-tier vocabulary

- **C0 — Conversational**
- **C1 — Staged**
- **C2 — Dramatic**
- **C3 — Spectacle**
- **V1 — Common**
- **V2 — Face/class identity**
- **V3 — Named signature**
- **V4 — Prime/boss spectacle**

The early-game spectacle ceiling is intentionally controlled. Nothing in Chapters 0–3 reaches the V4 Prime ceiling. Chapter 4's first Last Sentinel manifestation is the first approved V4 event.

---

# Chapter 0 — The Broken Convoy

## Environment families

1. Convoy Road
2. Wreck Field
3. Evacuation / Recovery Line
4. Triage / Safe Camp

These are authored composition families with before/after, intact/damaged, safe/dangerous and lighting/prop-state variants rather than one seamless simulated convoy disaster.

## Battle-background family

- Convoy Road
- Wreck Field
- Recovery Line / Riftmaw boss variant

Seven authored tutorial encounters remain fixed. No Chapter 0 random-encounter table is added.

## Scene presentation locks

### S001 — Opening
- Reuse Convoy Road composition.
- Ordinary pre-ambush atmosphere; do not pre-seed conspicuous green magical light around the sealed object.
- Ambush uses sound, dust, shake and before/after states rather than realtime destruction physics.
- Raider transition gives no illegal opening action.
- **C1 / V1.**

### S002 — Wreck Field
- Two or three connected compositions from one Wreck Field kit.
- Evidence such as moved wagon, impact pattern, north route and retreat tracks uses inspect pose/camera crops/prop overlays rather than bespoke cinematics.
- Four fixed tutorial fights reuse local battle compositions.
- **C0–C1 / V1.**

### S003 — Evacuation Relay Decision
- Reuse Wreck/Recovery assets.
- Preserve the authored 60–90 second stabilization interval before the Pursuer.
- Locked intent remains battle information, not a QTE/realtime reaction mechanic.
- **C1 / V1.**

### S004 — Field Triage Camp Revelation
- Busy triage is sold through layered NPC loops and props.
- Ilyra's first identifiable appearance is functional/professional, not a hero entrance.
- Incomplete green-and-gold response braces existing weak points/routes; it does not heal, attack, speak, manifest or identify itself.
- Implement through projected geometric lines, state swaps, local light, particles and settling debris rather than dynamic magical architecture.
- **C2 / V2.**

### S005 — Riftmaw
- Cyanis/Ilyra occupy normal left formation positions.
- Riftmaw + two Handlers remain one continuous fight; Restrained → Unbound is same HP bar and between-round state change; Cornered is low-HP behavior, not another bar/form.
- Chains use authored sprite/layer states, not physics.
- Green-and-gold Card remains inert during combat.
- **C2 / V2.**

### S006 — Aftermath
- Reuse Wreck/Recovery maps with postboss state overlays.
- Survivor sweep remains player-controlled.
- Recruitment/closing travel use restrained portrait-led staging and short transition.
- **C0–C1 / V1.**

### C01 / C02
- Safe-camp kit, fire/lamplight, ordinary props, portraits, reusable sitting/reach/reaction motions.
- No expensive eating or micro-action animation.
- **C0 / V1.**

---

# Chapter 1 — Brackenwall and the Wayfinder

## Environment families

1. Edgelands Settlement — Brackenwall / Greenhollow shared regional materials, distinct compositions
2. Edgelands Wooded Route — Hollow Watch Approach / Lower Woods / Briar Passage
3. Hollow Watch — later Yahtrean fortification over older Diysean substrate
4. Ancient Route / Wayfinder

## Battle-background family

- Wooded Edgelands Road
- Hollow Watch Outer
- Hollow Watch Lower Defense
- Lower Woods
- Briar Passage
- Castellan Chamber
- optional Cistern Waterworks return/Hunt support

## Core implementation locks

- Leaving Brackenwall's east gate begins the campaign-standard normal random-encounter presentation.
- Random encounter transition is fast, reusable and never implies a free enemy action.
- Safe dialogue/story windows suppress encounter triggering.

### Brackenwall
- Dense authored town compositions rather than a physically complete city.
- Hollow Watch can appear as camera-specific authored distant landmark states.
- Maevra enters without hero-orbit staging.
- Artifact-yard casing response is a thin green/gold floor pattern and local light only.
- **C1 / V1.**

### Hollow Watch
- Connected authored compositions, not one seamless fortress.
- Layer newer Yahtrean fort material over older Ancient substrate.
- Bridge/door/control changes are authored environment states.
- Two principal random-battle backgrounds cover most dungeon formations.

### Hollow Watch Castellan
- Integrated-wall Fortress state and Walking state share one HP bar.
- Reuse layered body/support assets; threshold uses short break-free sequence, state swap and lighting rather than second boss/model.
- Support pieces stay destroyed.
- **C2 / V2.**

### Greenhollow / Lower Woods
- Compact route community using regional materials but a distinct working-route composition.
- Torren's introduction avoids romantic camera implication with Maevra.
- Before permanent recruitment Torren is absent from battle presentation entirely and performs no decorative hidden attacks.
- Wrong marker is a simple prop-state swap.

### Briarhide Stalker
- Wounded/frightened animal; embedded Black Host component is the legal target.
- No villainous boss title/roar montage.
- On resolution the animal retreats; no victory pose.
- **C1 / V1.**

### Briar Passage
- First sustained natural use of the full four-character standard battle frame after Torren joins.
- False-trail hole uses leaf/prop state rather than physics/QTE.
- Civilian crossing uses authored walking path, no balance mechanic.

### Wayfinder Junction
- One bespoke hero exterior; no building.
- Environmental peak comes from composition and ancient road relationships, not heavy VFX.
- Establish one master Ancient cartographic graphic grammar for Wayfinder, route panels and later related maps.
- **C2 / V1.**

### C03–C05
- Portrait-led, prop-led, safe-area scenes using ordinary reusable poses.
- **C0 / V1.**

---

# Chapter 2 — The Drowned Oath

## Environment families

1. Dunmere Waterworks
2. Sunken Archive
3. Prisoner Galleries / Transfer Service
4. Red Transfer Bastion
5. Extraction Causeway

## Battle-background family

- Sunken Archive Walkway
- Flooded Preservation Hall
- Archive Basin / Leviathan
- Prisoner/Transfer Service
- Red Bastion Exterior
- Red Bastion Interior / Control
- Rhazek Command Arena
- Extraction Causeway

### Dunmere
- Two or three dense compositions imply the functioning town.
- Pumps/valves/gates use state changes and authored water/audio changes, not hydraulic simulation.
- Descent visually transitions modern civic construction into older infrastructure.

### Sunken Archive
- Water uses reusable animated textures, tint, reflection masks, ripple/wake/splash overlays and local distortion rather than fluid simulation.
- Large scale is implied through inaccessible layered depth.
- Archive reveal is **C2 / V1**.

### Memory Scribe
- Recording occurs only after an eligible completed action resolves.
- Enemy reproduces weaker function through its own animation language, not body-copy choreography.
- **V2 maximum.**

### Archive Leviathan
- One HP bar; authored same-bar state change.
- Oversized layered HD-2D boss using water occlusion/wakes/background body segments to imply size efficiently.
- No second title/bar/threshold free action.
- **C2 / V2.**

### Prisoner Galleries
- Prisoners retain agency and can accept/refuse care.
- Population scale uses a limited visible sprite set, offscreen audio, silhouettes and prop occupation.
- Safe pocket visually shows prisoners controlling the protective interior door.

### Bastion reveal / Red Transfer Bastion
- Bastion is frightening because it functions: logistics, medical routing, guards, supplies and controlled traffic.
- Build a permanent Black Host environment language from black/crimson/purple segmented biomechanical materials and selective motion.
- Bastion reveal is **C2 / V1.**

### Rhazek — Bastion Master
- Chapter-2 exact visual state only; do not import later Rhazek forms.
- One HP bar with same-body Ruin/armor escalation through layered state swap + short cut-in.
- **C2 / V2.**
- Withdrawal immediately shifts emphasis to opening the evacuation route rather than victory celebration.

### Extraction Causeway
- Evacuation scale comes from a few principal sprites, silhouettes, offscreen footsteps/voices and authored door/route states.
- No crowd AI or escort simulation.
- Hold the Junction is the only mandatory combat in S016.
- Final extraction threshold ends mandatory combat.
- Final Dunmere image centers evacuee consequence rather than protagonist victory tableau.

### C06 / C07
- Small safe/rest compositions, portraits, ordinary gear, ember/smoke/dawn-light loops.
- No dream visualization.
- **C0 / V1.**

---

# Chapter 3 — The Old City and Last Sentinel

## Environment families

1. Caelora Civic / Judicial
2. Old City / Suppressed Archives
3. Deep Command Station
4. Cresthaven Establishment State 1

## Battle-background family

- Judicial Causeway
- Central Adjudication
- Suppressed Archive Outer/Deep
- Command Station
- First Command Warden Chamber

### Caelora / S017–S018
- Dense civic compositions imply capital scale; no ominous villain grading that would rewrite legitimate Crown procedure as evil.
- Writs/records/seals use high-resolution inserts and ordinary paper poses.
- Exactly two authored nonlethal authority encounters.
- Nonlethal battle resolution suppresses death dissolves, generic victory posing and loot-show presentation.
- **C1 / V1.**

### Old City / Suppressed Archives
- Modern Crown records occupy far older Diysean structure.
- Layer inaccessible vertical depth to imply enormous Archive scale rather than physically building every tier.
- Nimera's first field/battle derivatives must follow exact visual authority.
- Living Index Tablet remains separate from the manifested airborne Conduit weapon-form.
- Knowledge firewall forbids Ruby/Last Sentinel/Prime/network visuals before their approved discovery point.

### Nimera recruitment
- Permanent roster/field-story presence and active battle formation are separate systems.
- After recruitment choose-four becomes immediately meaningful; reserves disappear from normal battle frame.

### Deep Command Station
- Cleaner/more intact than Archives; deterministic prepared gate/authority states, not a sentient procedural maze.
- Active four combatants are assessed dynamically; do not hardcode a particular lineup.

### First Command Warden
- Replace old “large 3D chamber” implementation language with a bespoke layered HD-2D hero composition.
- One HP bar, two behavior states.
- Copy function, not character choreography.
- Command Ring is a separate targetable component.
- Defeat is shutdown/dormant support posture, not explosion.
- **C2 / V3.**

### Last Sentinel identification / Ruby response
- Post-Warden output shows `/PREVIOUS ERROR/` then `/LAST SENTINEL CONFIRMED/`.
- Ruby response occurs only after Warden defeat and remains contained/still.
- No figure, voice, warrior silhouette or Prime manifestation in Chapter 3.
- S021 identifies/unlocks Last Sentinel but **does not manifest it**.
- First verified modern manifestation remains S022 in Chapter 4.

### Cresthaven State 1
- Build the permanent hub skeleton once and evolve it through state changes rather than replacing the hub per chapter.
- Chapter 3 immediate safe loop: Rest/Save, Formation, Archive/Records, Medical/Recovery, Departure.
- Workers/staff/establishment scale uses limited loops, audio and temporary props rather than construction simulation.

### H01–H04
- Reuse Cresthaven interiors/common room.
- Table clutter, paperwork, treatment and Card-case chair gag use prop states and portraits.
- Last Sentinel case remains visually inert in H04.
- **C0 / V1.**

---

# Chapter 4 — The Seventh Reaction

## Environment families

1. Cresthaven State 1 + Lower Grounds
2. Ivorybridge
3. Annex Approach / Regulation Terraces
4. Sixfold Annex / Experimental Galleries
5. Regulation Core

### S022 map work / Lower Cresthaven Grounds
- Reuse Chapter 3 Cresthaven state; do not prematurely advance to Chapter 5 Workshop Expansion.
- Map-table comedy uses map-position state swaps and portrait timing.
- Elder Briarhide reuses established Briarhide language as an older/larger/scarred natural-animal derivative; no corruption/Ancient/Black Host visual coding.

### First Last Sentinel manifestation
- Rounds 1–3 remain normal battle rounds.
- Round 4 restricts to Last Sentinel; player confirms.
- Prime manifestation remains legal combat resolution, not a detached prerendered movie.
- Exact Last Sentinel visual master controls the derivative.
- Prime may exceed ordinary battle-sprite scale through layered high-resolution art and temporary camera/light changes while the real battlefield remains visible.
- Manifest → one legal Prime action → dismiss same round → Elder Briarhide retreats alive.
- This establishes the reusable technical Prime pipeline for later Primes.
- **C3 / V4.**

### Ivorybridge / Vaelira
- Compact persistent Southhold hub; share compatible regional materials but preserve distinct local identity.
- Vaelira receives a full permanent-character HD-2D package at recruitment.
- Five permanent roster members may appear in story fields; only selected four appear in normal battle.

### Annex Approach / S023
- Area-driven traversal with encounter-enabled and authored safe pockets; do not pre-author expected random-battle counts.
- Build one exterior regulation kit with modular elemental effect layers.
- Prepared discharge uses authored channel state + VFX rather than simulation.
- Out-of-loop pulse must not be assigned a seventh-element color/iconography.

### Six-element modular library

Use one shared runtime system with six payload families:

- Fire — heat/embers/scorch
- Ice — frost/cold mist
- Lightning — arcs/static
- Wind — air/debris motion
- Earth — cracks/dust/material shift
- Water — wetness/condensation/flow

The same library supports Vaelira, Annex hazards, Hexarch, Crucible and later compatible content.

### Elemental Hexarch
- A harmed living researcher, not a monster.
- One underlying human/researcher battle asset with modular elemental overlays, not six bodies.
- Current state must be readable through art plus UI, not color alone.
- Defeat is nonlethal stabilization; no death dissolve/loot burst/victory pose.
- **C2 / V3.**

### Regulation Core
- Larger interconnected system is implied through layered inaccessible machinery and selective geometry.
- Do not visually reveal the later Underground Crest Network truth.

### Sixfold Crucible
- Form I: central core + six chamber identities; only active three receive full target/readability treatment.
- Preserve standard party-left/enemy-right/open-center battle frame; chamber components live in right/back architecture.
- Form I → Form II is a **genuine** new form: Form I hits zero, HUD withdraws, surviving chamber energy feeds inward, new silhouette/body resolves, Form II begins with fresh full HP and authored MP. Damage does not spill; Prime availability does not refresh.
- Build one Form-II base body plus six independent inherited-trait modules instead of bespoke art for every survivor combination.
- **C3 / V3.**
- Last Sentinel remains the chapter's unique V4 presentation ceiling.

### S025 / S026
- Reuse Annex/Ivorybridge postcrisis states; institutional safeguards become visible through warning placards, closed access, moved instruments and revised work practices.
- Accountability scenes are portrait/paperwork-led, not expensive cinematics.
- Vaelira's place at Cresthaven remains practical/ordinary; no premature hub-phase upgrade.

### C08 / C09 / H05
- Reuse generic roadside camp, Ivorybridge lodging and Cresthaven.
- Torren smoking remains ordinary background behavior lit from existing coals; no modern lighter or dramatic closeup.
- Night conversation and apology scene remain portrait-led.
- Small prop movements use authored sprite/tween/state changes, not physics.
- **C0 / V1.**

### Hunt #4 — Crown Prototype
- Reuse Annex return route and battle-background family.
- One body / one HP bar / no transformation.
- Target reticle/recalibration/low-HP acceleration use overlays and cadence changes.
- Prototype powers down; previously inaccessible storage opens to reveal pre-existing Relentless Flurry.
- **C1 / V2.**

---

# Cross-Chapter Consolidation Lock

## Regional/environment reuse

### Edgelands kit
Seeded in Chapter 0 and reused through Brackenwall, Hollow Watch approach, Greenhollow, Lower Woods, Briar Passage and Dunmere approaches.

### Wet/water library
Developed in Chapter 2 and reused for Ivorybridge/Sixfold Annex where compatible.

### Southhold civic family
Caelora seeds compatible architectural/material pieces for Ivorybridge without making the two locations visually interchangeable.

### Ancient Diysean grammar
All Ancient environments share a civilization-level material/structural language but remain functionally distinct:

- Route infrastructure — Wayfinder / old route systems
- Archive/preservation — Sunken Archive / Suppressed Archives
- Command/authority — Deep Command Station
- Regulation/research — Sixfold Annex substrate / Regulation Core

### Ancient cartographic master
One high-resolution map/route graphic standard controls Wayfinder, Old Waystone, post-Warden route panels, Chapter 3/4 map comparisons and later compatible Ancient cartography.

### Black Host family
Chapter 2 establishes permanent ribbed/segmented black/crimson/purple architecture, chains/restraints, transfer/logistics/medical systems and selective biomechanical motion for later Black Host reuse.

### Cresthaven master hub
Build one connected master environment and advance through authored state changes:

- Chapter 3 Establishment
- Chapter 4 remains Establishment-era with practical local changes
- Chapter 5 Workshop Expansion
- later Accord habitation / political pressure / final preparation / aftermath states as separately locked

## NPC/crowd library

Use a small modular civilian/work/soldier/researcher/prisoner body library with region/uniform/injury/prop variants. Named recurring characters receive exact individual identity; background populations reuse bases aggressively.

## Prop-state standard

Field compositions should support authored persistent states such as `BASE`, `DAMAGED`, `CLEARED`, `OPEN`, `CLOSED`, `ACTIVE`, `INACTIVE`, `POST_BOSS` and `POST_STORY` where relevant. This is the preferred low-cost method for doors, bridges, maps, clutter, machinery, medical props, warning signs, environmental damage and hub evolution.

## Nonlethal-resolution library

Provide reusable battle-resolution behavior that suppresses generic death dissolve/victory/loot presentation and returns to the authored field outcome for retreats, restraint, stabilization and lawful confrontations.

## Face / Card / Prime VFX architecture

One modular Face/VFX runtime supports the six locked Face colors:

- Might — Ruby
- Elements — Emerald
- Grace — Blue
- Resource — Gold
- Change — Fuchsia
- Ruin — Purple

Shared primitives include trails, projected symbols, impacts, particles, light pools, auras and battlefield lighting response. Individual abilities/Cards/Primes vary shape, timing, payload, sound and intensity rather than requiring separate render systems.

## Boss implementation categories

1. **Same-body / same-HP escalation:** components, overlay, idle, lighting and behavior change; no unnecessary new body.
2. **Genuine new form:** substantial new art only when the encounter truly becomes a new body/combat problem, as with Sixfold Crucible Form II.
3. **Prime-scale entity:** uses the reusable Prime manifestation pipeline rather than boss state logic.

## Android scaling

Quality options may reduce decorative particle density, distortion, reflection resolution, secondary background animation, weather density, decorative parallax layers and noncritical dynamic lights.

They must not reduce playable-space readability, character identity, important target readability, critical story effects, combat timing or UI clarity.

## Final Pass-1 result

**Chapters 0–4 HD-2D Conversion Audit, Pass 1: PASS.**  
**Cross-Chapter HD-2D Consistency & Cost-Consolidation: PASS / GREEN.**

No completed chapter requires story/dialogue/gameplay reopening. The approved result is one coherent early-game HD-2D implementation plan and is promoted into Audit88 authority.