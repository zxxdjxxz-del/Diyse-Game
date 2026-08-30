# Diyse — Trait Register
**v93 true-battle recovery normalization**  
**Rank milestones:** Rank I — CL1 / Rank II — CL6 / Rank III — CL12  
**Selection rule:** exactly one selected-class Trait package is active: Base Trait while Base class is selected, Subclass Trait while that Subclass is selected.

This file is the controlling current Trait-effect register. It restores the latest accepted Trait mechanics that survived in the working trackers but were reduced to names during the folder migration.

## Base Traits

### Cyanis — Crest Knight — Harmonized Crest
- **Rank I — CL1:** after a damaging **Physical** Crest Knight Ability, prime Cyanis's next damaging **Magical or Hybrid** Crest Knight Ability; after a damaging **Magical** Crest Knight Ability, prime his next damaging **Physical or Hybrid** Crest Knight Ability. The next qualifying opposite-side action consumes the prime for **+10% final damage**.
- **Rank II — CL6:** consumed-prime bonus becomes **+15% final damage**.
- **Rank III — CL12:** consumed-prime bonus becomes **+20% final damage**.
- A Hybrid Ability may consume either primed state but does not itself establish a new prime. One prime maximum; refresh rather than stack; no gauge or extra action.

### Ilyra — Blue Warden — Gentle Continuance
- **Rank I — CL1:** the first direct-healing Ability Ilyra resolves each round restores an additional **5% target Max HP** if that target began the action below 50% HP.
- **Rank II — CL6:** eligible excess direct healing creates **Regen: 4% Max HP per round for 4 rounds**, once per target per action. Regen remains a positive recurring heal; a tick that restores the target to full HP clears Bleed under the global Bleed rule.
- **Rank III — CL12:** Ilyra's cleansing Abilities gain **+10% healing potency**.

### Torren — War Archer — Veteran's Measure
- **Rank I — CL1:** Torren gains **+10 Base Hit** against enemies whose major defensive data or observed behavior is known.
- **Rank II — CL6:** the first direct-damage War Archer Ability each round against **Hunter's Measure** gains **+5 percentage points Critical Chance**.
- **Rank III — CL12:** that Hunter's Measure Critical bonus becomes **+10 percentage points**.
- Hunter's Measure remains an authored tactical state, not a universal harmful status.

### Nimera — Cardweaver — Living Archive
- **Rank I — CL1:** Nimera's first Standard Card each round gains **+10% eligible primary-action potency**. The interface also exposes only encounter-permitted known Face/effect/targeting/Prime-consequence information; no removed Card-Seal subsystem is restored.
- **Rank II — CL6:** that first Standard Card each round additionally gains **+10 Base Hit / application reliability**, where relevant.
- **Rank III — CL12:** after a legal Prime activation begins initial resolution while Nimera is conscious and active, restore **5% Max MP**, at most once per ordinary party round before Prime suspension.

### Vaelira — Green Arcanist — Prismatic Flow
- **Rank I — CL1:** the first damaging action each round whose standard element differs from Vaelira's previous damaging action gains **+10% final damage**. Colorless resets the remembered element without receiving the bonus.
- **Rank II — CL6:** that qualifying different-element action also gains **+10 Base Hit / application reliability**, where relevant.
- **Rank III — CL12:** that qualifying action additionally gains **+15% Magic Defense penetration** on its Magical-derived portion.
- Vaelira's separately authored matching-element status-specialist bonuses remain separate.

### Seyrik — Ruin Vanguard — Severed Command
- **Rank I — CL1:** Ruin Vanguard Abilities that already carry an authored Bleed rider gain **+5 percentage points Bleed application chance**. This never invents Bleed on a move that lacks it and does not modify Basic Attack, Cards, Items, Primes, equipment riders, or Shardfang autonomous attacks.
- **Rank II — CL6:** while Seyrik remains conscious, **Shardfang +10 Base Hit**.
- **Rank III — CL12:** while Seyrik remains conscious, Shardfang additionally deals **+10% final damage**.

## Subclass Traits

### Cyanis — Crest Arcanist — Crest Resonance
- **Rank I — CL1:** all MP-costing Crest Arcanist Abilities cost **2 less MP**, minimum 1 MP.
- **Rank II — CL6:** damaging **Magical / Colorless** Crest Arcanist Abilities gain **+15% Magic Defense penetration**.
- **Rank III — CL12:** when **Crest Attunement** is consumed, the empowered Ability additionally deals **+10% final damage**.
- **Crest Attunement:** Arcane Lance establishes it through the end of the following round; Cyanis's next **different** Crest Arcanist Ability consumes it for **+15 Base Hit / application reliability**. One state maximum; refresh, not stack; Arcane Lance cannot consume the state it just created.

### Ilyra — Vowblade — Mercy in Steel
- **Rank I — CL1:** when a Vowblade Ability restores HP to a conscious ally other than Ilyra, she gains **Tempered Mercy** through the end of the following round. Her next damaging Vowblade Ability consumes it for **+10% final damage**.
- **Rank II — CL6:** the consuming Ability also gains **+10 Base Hit**, **+10% Defense penetration** on Attack-derived portions, and **+10% Magic Defense penetration** on Magic-derived portions.
- **Rank III — CL12:** if that empowered Ability hits a target already **Bleeding**, that target takes an additional **+10% final damage**. Evaluate per target for AoE.
- One Tempered Mercy state maximum; qualifying heals refresh rather than stack.

### Torren — Routeweaver — Route Weaving
- **Rank I — CL1:** after Torren uses a Standard Card, his next damaging Routeweaver Ability before the end of the following round gains **+10% final damage**.
- **Rank II — CL6:** after Torren uses any Routeweaver Ability, his next Standard Card before the end of the following round gains **+10 Base Hit / application reliability**, where relevant.
- **Rank III — CL12:** **Open the Way** initial duration increases **3 → 4 rounds**.
- Stored sequencing benefits refresh rather than stack and never create an extra action.

### Nimera — Proofhunter — Applied Evidence
- **Rank I — CL1:** damaging Proofhunter Abilities gain **+10 Base Hit** against targets with Hunter's Measure.
- **Rank II — CL6:** those Abilities additionally gain **+10 percentage points Critical Chance** against measured targets.
- **Rank III — CL12:** those Abilities additionally gain **15% applicable defensive-axis penetration** against measured targets: Defense for Physical, Spirit for Magical, split appropriately for Hybrid.
- These bonuses stack with explicitly authored same-axis penetration on the Ability.

### Vaelira — Axiomblade — Formal Equivalence
- **Rank I — CL1:** when Vaelira deals damage with a single-element **Fire / Ice / Lightning / Earth** Ability, that element becomes her current expression through the end of the following round. Her next **Neutral damaging Axiomblade Ability** adopts that stored element and consumes the expression. Authored elemental Axiomblade Abilities are never overwritten; multi-element actions do not establish an expression; one expression maximum.
- **Rank II — CL6:** a Neutral Axiomblade Ability that consumes the expression gains **+10% final damage**.
- **Rank III — CL12:** that consuming Ability also gains **+15% Defense penetration** on Physical-derived portions and **+15% Magic Defense penetration** on Magical-derived portions.

### Seyrik — Ruin Warden — Ruin's Mercy
- **Rank I — CL1:** whenever Seyrik actually restores HP to himself from an authored **Drain**, also restore HP equal to **15% of the actual HP restored to Seyrik** to the conscious other ally with the lowest HP%. Cannot revive; ties use stable party-slot order.
- **Rank II — CL6:** shared recovery increases **15% → 25%**.
- **Rank III — CL12:** whenever a Ruin Warden Ability restores HP to a conscious ally, that ally gains **+10 Status Resistance through the end of the following round**. Reapplications refresh rather than stack.

## Firewall
- These are Trait effects, not separate commands.
- Do not reintroduce retired Card Seals, Imprints-as-global-resource, Break/Stagger meters, Brace, or any historical trait text superseded by these later accepted packages.
