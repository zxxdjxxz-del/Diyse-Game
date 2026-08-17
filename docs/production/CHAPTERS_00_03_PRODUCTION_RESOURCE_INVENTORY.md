# DIYSE — Chapters 0–3 Production Resource Inventory

**Authority basis:** Complete Master Canon v1.60 / Audit75  
**Scope:** Chapter 0 through Chapter 3, including their closed Character-Life / hub scenes and the immediately associated post-chapter return-loop content.  
**Purpose:** define the reusable visual/game-production resources needed to build the closed early game without reopening dialogue or turning written micro-actions into bespoke animation requirements.

## 1. Production rule

This is an **asset/resource inventory**, not dialogue re-authoring and not Godot dialogue `.tres` conversion.

The early game should be produced from:

- a small reusable character acting vocabulary;
- illustrated portrait expression packs;
- modular 3D environment kits assembled into authored locations;
- authored before/after environment states instead of systemic simulation;
- modular NPC/outfit sets instead of unique crowd characters;
- reusable prop families;
- reusable VFX families;
- a small camera-composition library;
- reusable enemy chassis where visual identity permits;
- unique production budget concentrated on named bosses, exact character identities, major reveals, and important machines.

Written staging communicates **what the player must understand**. It does not automatically demand a unique animation asset for every verb.

## 2. Named character production set required through Chapter 3

### Full named-character presentation packs

1. Cyanis Dovaren
2. Ilyra Amarin
3. Torren Harth
4. Maevra Solmar
5. Nimera Pellan
6. Crown Princess Mirena Ceryth
7. Queen Lysara Ceryth

Maevra remains guest/recurring rather than permanent. Mirena and Lysara require story presentation resources but no permanent-party battle package in Chapters 0–3.

### Shared world-acting vocabulary — working target

Build once and retarget/adapt by character silhouette where legal:

1. neutral idle
2. alert/work idle
3. walk
4. brisk walk / short run
5. stop / settle
6. turn / reorient
7. look / attention shift
8. inspect small object
9. interact with wall/plate/table
10. point / indicate direction
11. open-hand explanation gesture
12. short dismissive/negative gesture
13. nod
14. head shake
15. sit
16. stand from seat
17. crouch / kneel
18. reach / take small prop
19. hold / read paper, map, or Card-sized prop
20. eat / drink simple loop
21. brace / shield from impact
22. hurt / stagger
23. recover / steady
24. quiet/resting idle

Do not create unique authored-body animation for every written action such as checking a line, rereading a page, comparing two documents, examining a mark, tightening a strap, or looking between two objects. Use the closest reusable action plus camera/prop state.

### Shared combat presentation vocabulary

Every combat-capable character needs the common state set:

- battle idle
- advance/return
- hit reaction
- heavy hit/stagger
- Defend
- Item use
- Card command gesture
- KO/down
- recovery/revive
- victory/relax transition where used

Weapon/class action families required through Chapter 3:

- Cyanis — sword + shield / Crest Knight
- Ilyra — Blue Warden staff/ward casting
- Torren — bow / War Archer
- Maevra — spear/glaive command-fighter guest set
- Nimera — Conduit/caster set; ordinary Attack uses a manifested airborne spear-form rather than Nimera physically wielding it

Abilities should preferentially reuse one of a few strong action silhouettes plus different VFX/timing rather than receiving one bespoke full-body animation per ability.

## 3. Portrait production set

Portraits carry the expensive close acting so world animation can stay economical.

### Core expression family for named cast

Working baseline per major named character:

- neutral / listening
- focused / professional
- amused / small smile
- irritated / skeptical
- concerned / worried
- surprised / caught off guard
- tired / worn down
- angry / hard
- soft / private, only where characterization requires it

Not every character needs every expression immediately. Build only the expressions actually used in Chapters 0–3, then expand later.

Character-specific priorities:

- Cyanis: neutral, focused, amused, irritated, concerned, tired
- Ilyra: neutral, focused, dry-amused, concerned, irritated, tired, precise anger
- Torren: neutral, focused, dry-amused, annoyed, concerned, tired
- Maevra: command-focused, neutral, amused, irritated, strained/Commander-Solmar, concerned, tired
- Nimera: neutral, engaged, delighted/curious, irritated, skeptical, alarmed, tired, unusually-simple/vulnerable
- Mirena: public neutral, sharp/focused, amused, irritated, concerned
- Lysara: neutral, observant, dry-amused, concerned, formal/angry

Generic NPCs should not receive full portrait packs. Use no portrait or one/two role portraits where a scene genuinely benefits.

## 4. Modular environment kits

The early game does **not** need a unique asset library for every named location. Build seven modular environment kits and combine them into authored maps.

### ENV-KIT-01 — Road / wilderness / convoy

Use for:

- Chapter 0 convoy/wreck approaches
- Hollow Watch approach
- Greenhollow routes
- Briar Passage
- travel connectors and Hunt-return roads

Core pieces:

- road/path splines or modular segments
- dirt/mud/grass/rock ground materials
- embankments, slopes, ledges, low cliffs
- woodland trunks/branches/brush
- route markers/signs
- small bridge/crossing pieces
- wagon tracks / mud decals
- authored blocked/open path variants

### ENV-KIT-02 — Yahtrean settlement / working town

Use for:

- Brackenwall
- Greenhollow
- Dunmere
- ordinary support areas adjoining larger sites

Core pieces:

- modular walls, houses, sheds, workshops
- gates/fences
- repair scaffolds
- market/supply awnings
- barrels, crates, carts
- medical/service corners
- civilian work stations
- route boards / notices
- reusable interior room shell

Regional dressing/material swaps should distinguish settlements without rebuilding the structural kit.

### ENV-KIT-03 — Ancient Diysean infrastructure

Use for:

- Hollow Watch buried levels
- Wayfinder Junction
- Sunken Archive
- Old City / Suppressed Archives
- command-station architecture
- parts of Cresthaven

Core language:

- fitted stone/metal architecture
- clean mechanical tolerances where preserved
- recessed rings/plates
- Card receptacles
- rotating parts
- reader surfaces
- articulated doors/gates
- compact integrated machinery
- Crest-like geometry
- archive shelves/storage modules
- maintenance passages
- modular bridge/platform components

The visual escalation comes from **state, scale, preservation, and density of functioning systems**, not by creating an unrelated art style in every chapter.

### ENV-KIT-04 — Black Host retrofit / Bastion

Use for:

- Black Host excavation intrusions at Hollow Watch
- prisoner retrofit elements
- Red Transfer Bastion
- Black Host machinery layered over older Diysean infrastructure

Core pieces:

- black/dark-charcoal ribbed structural modules
- crimson inner-channel accents
- dark-purple Ruin-energy nodes
- cages/restraint frames
- military barricades
- transfer apparatus
- field command fixtures
- chains/cables/reservoir assemblies
- black-metal tool and reinforcement pieces

This kit must read as a contemporary Black Host imposition when placed over Ancient Diysean architecture.

### ENV-KIT-05 — Waterworks / flooded-state kit

Use for:

- Poisoned Waterworks
- Sunken Archive flooded sections
- Dunmere water-system investigation

Core pieces:

- channels/troughs
- sluice/gate mechanisms
- pipes/intakes
- drains/grates
- wet-surface material variants
- static shallow/deep water planes
- contaminated-water material/VFX state
- lowered-water state
- blocked/open feed state

Use authored water levels and swaps. No fluid simulation requirement.

### ENV-KIT-06 — Caelora civic / royal administration

Use for:

- S017 containment
- S018 authority/procedure spaces
- Judicial Causeway / administrative approaches

Core pieces:

- civic stone modules
- formal gates/arches
- offices/counters
- queue/barrier furniture
- records desks
- document storage
- seal stations
- guard posts
- court/administrative signage
- covered passages / causeway modules

Crowd life comes from layered loops and background groups, not systemic bureaucracy simulation.

### ENV-KIT-07 — Cresthaven establishment / lived-in overlay

Use at the **separate Cresthaven site** after the Old City sequence.

This is primarily an overlay kit applied to Cresthaven's own Ancient architecture:

- temporary tables
- lamps
- bedrolls
- archive boxes
- medical supplies
- route markings
- portable storage
- simple food setup
- chairs/stools
- temporary partitions
- work notices

Chapter 3 Cresthaven exposes only the immediate safe loop: Rest/Save, Formation, Archive/Records, Medical/Recovery, Departure.

Cresthaven must remain a separate map/site from Caelora's Old City / Suppressed Archives even though both reuse Ancient-Diysean asset families.

## 5. Authored location build matrix

### Chapter 0 — The Broken Convoy

Location builds:

- Convoy Wreck Field — ENV-KIT-01 + wreck-state props
- Evacuation Relay — ENV-KIT-01 + relay stone/mechanism pieces
- Field Triage Camp — ENV-KIT-01/02 + temporary medical/camp overlay

Required authored states:

- damaged wagon/wreck states
- blocked/cleared survivor routes
- intact/damaged cover
- triage active / post-fight settling state
- incomplete green/gold Card-response overlay

### Chapter 1 — Brackenwall and the Wayfinder

Location builds:

- Brackenwall — ENV-KIT-02
- Hollow Watch — ENV-KIT-02/03/04
- Greenhollow — ENV-KIT-02 + ENV-KIT-01
- Briar Passage — ENV-KIT-01
- Wayfinder Junction — ENV-KIT-03

Required authored states:

- Brackenwall repair activity
- Hollow Watch bridge/door states
- Black Host excavation evidence
- Castellan fortress/walking arena-state changes
- Greenhollow damaged civilian route/flood crossing
- Briar Passage blocked/usable route states
- Wayfinder Face-ring / route-map interface states

### Chapter 2 — The Drowned Oath

Location builds:

- Dunmere — ENV-KIT-02/05
- Poisoned Waterworks — ENV-KIT-05
- Sunken Archive — ENV-KIT-03/05
- Prisoner Galleries — ENV-KIT-03/04
- Red Transfer Bastion — ENV-KIT-04 over ENV-KIT-03 substrate where appropriate
- Extraction Causeway — ENV-KIT-04/03

Required authored states:

- contaminated / isolated / shut lower feed
- damaged/flooded versus protected Archive areas
- prisoner safe-pocket door states
- sealed future Hunt branch
- Bastion active / defeated / extraction-safe states
- extraction crowd layers
- opened post-chapter Transfer Executioner branch

### Chapter 3 — The Old City and Last Sentinel

Location builds:

- Caelora civic/containment spaces — ENV-KIT-06
- Old City / Suppressed Archives — ENV-KIT-03 + limited modern records overlay
- deeper command-station route — ENV-KIT-03, higher preservation/function density
- **separate Cresthaven** — ENV-KIT-03 + ENV-KIT-07

Required authored states:

- queue/access/restricted civic states
- paper/seal/authorization states
- Suppressed Archive secure/open/denied doors
- denied judgment branch on first pass
- command-route redirect/gate states
- Warden arena command-ring states
- post-Warden stable Ruby Card state
- post-S021 judgment-branch-open state for return Hunt
- Cresthaven establishment before/after occupancy states

## 6. Reusable prop library

### PROP-FAM-01 — Travel / field

- wagons and cart variants
- wheels/axles
- crates/barrels/sacks
- rope/cord
- tarps
- lanterns
- bedrolls
- water containers
- route signs/markers

### PROP-FAM-02 — Medical

- medical pouch
- bandages/wraps
- treatment cloths
- water basin
- simple bottles/containers
- stretcher/carrier
- blankets
- temporary treatment mat

### PROP-FAM-03 — Food / ordinary life

- cooking pot
- ladle
- bowls
- cups
- bread
- simple meal plate
- camp/table food states

This family carries C02, C03, C05 and later H04 cheaply.

### PROP-FAM-04 — Maps / records / authority

- route map
- official map
- charcoal/writing tool
- map weights
- reports
- writs
- ledgers
- folders
- wax/seal set
- evidence tags
- record boxes

This family is heavily reused from C04 through Chapter 3.

### PROP-FAM-05 — Furniture / work surfaces

- table small/medium
- desk
- chair/stool
- bench
- shelf
- cabinet
- work stand

### PROP-FAM-06 — Ancient interface objects

- reader plate
- Card receptacle
- ring interface
- archive tablet/media
- control lever/mechanical switch
- gate control
- protected repository slot

### PROP-FAM-07 — Black Host retrofit

- cage sections
- restraint fixtures
- transfer frame
- chains
- red/purple reservoir/node
- military tool chest
- command marker

### PROP-FAM-08 — Card / Conduit story objects

- sealed recovered Card case
- generic Standard Card physical presentation
- Last Sentinel static Ruby presentation state
- Glassform Rupture comparison Card
- Nimera Living Index Tablet

## 7. Character-Life / hub prop bundles

These scenes should be cheap because their emotional performance is mostly dialogue, portraits, props and timing.

### C01 — The Fire Is Too Close

Reuse: campfire, gloves, seat/stone, basic camp kit.

### C02 — Food After Triage

Reuse: two bowls, bread/potatoes/simple food, table/ground seating.

### C03 — Torren's Version of Dinner

Reuse: fire, pot, bowls, bread, ladle, sit/eat/stir states.

### C04 — What the Map Says

Reuse: route table, two maps, charcoal, map weights, cup, Torren's bow; sit/stand/point/write states. No custom handwriting animation.

### C05 — Two Professionals Complaining About Cyanis

Reuse: medical pouch, reports, work table, chair; sit/sort/read/stand states.

### C06 — Three People Who Know Each Other Now

Use existing field/camp furniture and small repair/rope/cord props. The scene should remain mundane and socially readable rather than cinematic.

### C07 — Bad Dreams, No Questions

Use lodging/camp seat, blanket/bedroll, boot/lace, low-light state. No dream-flashback asset is required.

### H01 — Nimera Takes Over a Table

Use Cresthaven table plus paper/book/tablet clutter states. Physical comedy comes from clutter swaps/tweens, not bespoke animation.

### H02 — Torren and Maevra, Unsupervised

Use reports/maps/weather-record props, table/seat, quiet Cresthaven work state.

### H03 — Ilyra and Nimera

Use medical wrap/bandage, seat/table, terrible bread/food prop. Treatment uses reusable medical interaction states.

### H04 — Last Sentinel Is Not Invited

Use dinner table, chairs, ordinary food, static protected Ruby Card case. The chair gag is a prop/position change, not a custom cinematic. No Card autonomy or activation VFX.

## 8. NPC / crowd production set

Build modular people rather than unique background characters.

### Base civilian presentation

- adult masculine base
- adult feminine base
- several face/hair/skin variants
- workwear / travel / town / injured overlays

### Reusable role outfits

- Yahtrean soldier / convoy escort
- Blue Warden / medical support
- Brackenwall/route worker
- settlement worker/civilian
- Crown clerk / administrative worker
- Ivory Watch / royal security
- prisoner / evacuee
- Black Host soldier/support

Crowd scenes should use 3–6 foreground readable people plus lower-detail repeated background groups with offset timing/placement.

## 9. Enemy production strategy through Chapter 3

Do not build every combat identity as a completely unrelated rig if a shared chassis preserves readability.

### ENEMY-CHASSIS-A — Humanoid military

Shared skeleton/body base can support modular equipment/FX variants such as:

- early hostile soldier/reaver roles
- crossbow/ranged soldier roles
- shield/guard roles
- War-Sorcerer / Ward-Sorcerer caster roles
- Bastion Shield Guard
- Bastion Crossbow Guard
- Transfer Adept
- later Way-Fort/Rift support identities where still used by final encounter tables

Faction silhouette, armor modules, weapon, stance and VFX create identity without rebuilding locomotion/hit/KO sets.

### ENEMY-CHASSIS-B — Medium Ancient humanoid construct

Reusable mechanical rig family for roles such as:

- Hollow Watch Sentry
- Memory Scribe
- Vault Sentinel
- Archive Scribe Engine
- Judgment Frame
- Command-Station Sentry

Use different heads/sensors/arm modules/emitters and behavior VFX.

### ENEMY-CHASSIS-C — Turret / fixed mechanical

- Hollow Watch Ballista
- Authority Lens / reader-emitter style threats
- fixed support hardware and command components

### ENEMY-CHASSIS-D — Orb / drone / magical-machine emitter

- Archive Current-style threats
- Erasure Wisp-style output
- Command Ring Drone
- other small machine/magic support units

### ENEMY-CHASSIS-E — Natural quadruped

Reuse locomotion/hit base where anatomy permits for Greenhollow/Briar wildlife identities. Briarhide remains a displaced/territorial animal, not a corrupted monster.

### Unique or near-unique early-game enemy assets

Reserve bespoke production work for identities whose silhouette/mechanics justify it:

- Briar Boar / plant-controller families if retained in final formation tables
- Cistern Leech / Bogshell / Drowned Archive Maw families where final Chapter-2 encounter tables retain them
- large Archive Leviathan

Exact ordinary formation counts/weights remain Phase-29B implementation work; this inventory defines asset reuse families rather than freezing proposed encounter-table numbers.

## 10. Named boss / elite production budget

### Chapter 0

- Convoy War-Sorcerer: reuse humanoid military/caster base with authored boss presentation and encounter VFX
- injured Iron Cohort Soldier: reuse humanoid military base

### Chapter 1

- Briarhide Stalker: authored large-predator presentation; nonlethal state/readability required
- Hollow Watch Castellan: unique major Ancient construct; fortress state and walking state share one HP bar and one core asset with authored mechanical-state changes
- Watch Captain Frame, if retained as optional elite: derive from Ancient construct chassis rather than unique boss-grade rig

### Chapter 2

- Archive Leviathan: unique large machine/beast boss asset, one HP bar with authored state progression
- Commander Rhazek — Bastion Master: exact named-character/boss asset; finite support; same-HP-bar escalation only in Chapter 2
- Archive Duplicant, if retained: derive from medium Ancient construct family

### Chapter 3

- Ivory Adjudicator: derive from premium Ivory Watch humanoid package with authored nonlethal boss/miniboss presentation
- First Command Warden: unique major Ancient machine; one HP bar, two behavior states, targetable Command Ring
- Archive Judgment Engine Regional Hunt: build from judgment/command mechanical language with enough unique silhouette/readability for Hunt status; return branch reuses Old City environment

## 11. VFX library

### VFX-FAM-01 — Modern Crest / protection

- modern Crest geometry
- green/gold incomplete Card response
- defensive stabilization lines
- Blue Warden protection/medical magic

### VFX-FAM-02 — Standard Card presentation

- Card select/read activation layer
- Face-color accent layer
- hit/heal/protection payload hooks

Do not build Prime-manifestation spectacle into Chapters 0–3 scenes. Last Sentinel does not manifest during S021.

### VFX-FAM-03 — Ancient machine/interface

- scan line / sensor focus
- ring rotation/glow
- reader accept/deny
- door/gate authorization state
- route redirect indicator
- archive data/projection

### VFX-FAM-04 — Black Host / Ruin

- crimson/dark-purple energy
- transfer-system pulse
- ward/caster projectile
- Rhazek Bastion escalation layer

### VFX-FAM-05 — Water / contamination

- clean-water surface state
- contaminated-water tint/particles
- wet drip/mist ambience
- authored drain/lower-state transition

### VFX-FAM-06 — Command authority

- target-specific Command Seal
- Command Ring targetable state
- weakened recorded-action machine response
- authority accept/deny result

### VFX-FAM-07 — Last Sentinel identification

- stable Ruby Card state
- machine text/output presentation for `/PREVIOUS ERROR/` and `/LAST SENTINEL CONFIRMED/`
- Recovered UI accent

No warrior, silhouette, voice, autonomous motion, or manifestation is included in this Chapter-3 resource family.

## 12. Camera composition library

Build a small number of reusable camera behaviors:

1. exploration follow / readable 2.5D depth
2. wide environment reveal
3. functional two-character world-space composition
4. three/four-person group composition
5. prop/document/interface insert
6. threat/boss reveal
7. post-battle consequence wide
8. quiet Character-Life locked composition
9. crowd/settlement establishing pass
10. transition from world-space acting into portrait dialogue and back

Do not create bespoke camera rails for every conversation unless the geography/reveal truly requires one.

## 13. Audio production resources

Music composition remains its own regional/music workstream. This inventory covers reusable **SFX/ambience** only.

### Shared ambience families

- wilderness/road
- town/worksite
- rain/wet/flooded interior
- Ancient machinery low bed
- Black Host machinery/Ruin bed
- civic/administrative crowd
- Cresthaven early lived-in hub

### Reusable SFX families

- footsteps by surface family
- cloth/armor movement
- weapon draw/ready
- paper/map/page handling
- wax/seal/document stamp
- chair/bench/table movement
- bowl/cup/food handling
- gate/door/lock
- Ancient ring/reader/mechanical movement
- water gate/drain/splash
- chain/cage/transfer machinery
- Card case open/close
- Card/interface activation accents

## 14. Optional-return resources attached to Chapters 0–3

The chapter-completion pass should account for the Regional Hunts that become reasons to revisit earlier spaces.

### Hunt #1 — Cistern Devourer

- reuse road/wilderness kit
- small cistern sub-kit derived from stone/waterworks pieces
- one Hunt-grade creature asset
- post-S011 route-open state

### Hunt #2 — Transfer Executioner

- reuse Red Transfer Bastion / prisoner safe-pocket assets
- post-S016 opened transfer-branch state
- one Hunt-grade executioner asset or boss-grade modular Black Host construct/humanoid package according to final visual authority

### Hunt #3 — Archive Judgment Engine

- reuse Old City / Suppressed Archive kit
- post-S021 authorization/open-door state
- Hunt-grade Judgment Engine asset

These returns should use shortcuts/checkpoints and changed state, not full dungeon rebuilds.

### Post-Chapter-3 Major unlock

Ashfrost Expanse / Ashen Whitehorn is a separate world-map optional-major destination unlocked after Chapter 3. Treat it as an **extension package**, not a reason to inflate the core Caelora/Old City/Cresthaven kit.

## 15. Priority build order

### P0 — proves the whole Ch0–3 production language

- core named-character world presentation for Cyanis/Ilyra/Torren/Maevra/Nimera
- shared 24-state acting vocabulary
- core combat states + five weapon/class action families
- initial portrait packs
- ENV-KIT-01 road/wilderness
- ENV-KIT-02 settlement
- ENV-KIT-03 Ancient Diysean
- ENV-KIT-04 Black Host retrofit
- core props 01–08
- VFX families 01–04
- camera library
- generic civilian/soldier modular NPC package

### P1 — required to finish Chapters 2–3

- ENV-KIT-05 waterworks/flood
- ENV-KIT-06 Caelora civic
- ENV-KIT-07 Cresthaven establishment
- Nimera Conduit/spear-manifestation presentation
- Archive Leviathan
- Rhazek Bastion Master
- Ivory Watch role package
- First Command Warden + Command Ring
- VFX families 05–07
- Mirena and Lysara portrait/story presentation packs

### P2 — optional/revisit completion

- Cistern Devourer Hunt package
- Transfer Executioner Hunt package
- Archive Judgment Engine Hunt package
- post-Chapter-3 Ashfrost Expanse optional-major extension

## 16. Explicitly do not build for Chapters 0–3

Do not budget:

- full 3D cinematic acting for every dialogue line;
- unique animation for each physical verb in prose;
- physics-driven wreck destruction;
- simulated fluid systems;
- crowd AI;
- a systemic bureaucracy/queue simulation;
- procedural Ancient facility logic;
- actor-body mimic animation for Memory Scribe or First Command Warden;
- a Prime warrior model/manifestation for S021;
- separate bespoke environment art families for every named map when modular kits can distinguish them through layout, materials, dressing, lighting and authored states;
- a unique full character model for every civilian, prisoner, clerk or soldier.

## 17. Production target

The working target for Chapters 0–3 is therefore:

- **7 modular environment kits** assembled into the chapter locations;
- **7 named story-character presentation packs**, with full battle production required for the five combat-capable characters present by Chapter 3;
- **1 shared world-acting vocabulary** rather than scene-specific motion libraries;
- **5 weapon/class combat action families** through Chapter 3;
- **8 reusable prop families**;
- **7 VFX families**;
- **10 reusable camera compositions/behaviors**;
- a modular NPC/crowd package;
- a small set of reusable enemy chassis plus unique boss-grade assets only where silhouette/mechanics justify them;
- separate optional Hunt/major-destination extensions that reuse the main chapter kits wherever possible.

This is the resource ceiling to design toward. If a scene can be staged with these resources and a prepared environment state, do that before authorizing a new bespoke asset.