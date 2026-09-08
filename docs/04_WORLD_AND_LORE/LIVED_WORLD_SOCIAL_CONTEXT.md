# Diyse — Lived-World Social Context

**Status:** ACTIVE WORLD-LIFE AUTHORITY  
**Domain:** `04_WORLD_AND_LORE`  
**Purpose:** preserve the ordinary lived-world pressure that characters, NPCs, and Dialogue Engine agents should perceive between plot beats without inventing new geography, politics, prices, or hidden lore.

This file restores the compatible lived-world layer from the completed Diyse dialogue-development work under the current organized canon. It does **not** override newer story, geography, economy, or character authority.

## Core world-life rule

> **The characters are allowed to forget the war for a few minutes. The world is not.**

Diyse is not a sequence of story rooms populated only when the party arrives. People continue working, sleeping, eating, repairing, traveling, grieving, arguing, gossiping, waiting, recovering, caring for family, and making plans outside the protagonist's camera.

Ordinary life remains legitimate even during crisis. A scene may be about food, weather, a bad chair, wet boots, a damaged buckle, a route marker, a blanket, a stupid argument, boredom, or somebody wanting five minutes of quiet without becoming narratively empty.

## Persistent wartime pressure

When compatible with the current chapter and location state, the world may be shaped by:
- fatigue and interrupted sleep;
- casualty awareness;
- food and supply shortages;
- watches and guard rotations;
- wounds and recovery limitations;
- route closures, damaged roads, dangerous crossings, and changing travel time;
- evacuation and temporary shelter;
- displaced civilians;
- missing people and family tracing;
- alarms and sudden interruptions;
- practical preparation and repair work;
- transport constraints;
- professional shorthand developed under pressure;
- bounded gallows humor among people who have earned that familiarity;
- routines continuing imperfectly around danger.

These are **world pressures, not mandatory dialogue topics**. An agent should not mention them mechanically in every scene. They influence what people notice, what is difficult, what gets postponed, and why ordinary comforts matter.

## People have lives outside the party

NPCs are not quest terminals.

A believable Diyse NPC may have:
- a job or craft;
- family or household obligations;
- friends and coworkers;
- hobbies and ordinary pleasures;
- complaints;
- wrong rumors;
- local priorities;
- professional pride;
- grudges unrelated to the main plot;
- limited information;
- plans that do not involve the permanent six;
- reasons to be absent when the party returns.

A recurring NPC may be working elsewhere, asleep, traveling, meeting suppliers, repairing infrastructure, helping family, on watch, receiving treatment, or simply unavailable. Popularity does not require omnipresence.

The same rule applies to supporting characters: their relationships should not form only as radial links to Cyanis or to the active party.

## Knowledge is local and uneven

People do not possess writer-level world knowledge.

What someone plausibly knows depends on:
- where they live;
- where they have traveled;
- profession and training;
- institutional access;
- personal history;
- what has happened by the current story position;
- what they directly observed;
- what another person legitimately told them;
- rumor, misunderstanding, and incomplete evidence.

Wrong but reasonable beliefs are allowed. Uncertainty is allowed. "I don't know," "maybe," and conflicting local accounts are part of the world rather than failures of exposition.

All ancient-history and reveal restrictions remain subordinate to `MODERN_KNOWLEDGE_FIREWALL.md`, current `02_STORY` reveal timing, and character-specific knowledge boundaries in `01_CHARACTERS`.

## Professional reality

Expertise changes what a person notices; it does not merely change vocabulary.

Current permanent-six broad expertise routing is:
- **Cyanis** — command, fortification/Crest practice, practical logistics, group exposure and risk;
- **Ilyra** — medicine, recovery, consent in care, physical condition, preservation;
- **Torren** — terrain, routes, tracking/field evidence, travel, maintenance, practical logistics;
- **Nimera** — Cards, records, provenance, classification, contradictory evidence;
- **Vaelira** — elemental systems, regulation, instability, calibrated technical observation;
- **Seyrik** — Black Host doctrine, Ruin practice, institutional procedure, military operational logic.

Those boundaries are descriptive routing, not permission to invent mechanics or future knowledge. Exact character authority remains in `01_CHARACTERS`; exact class mechanics remain in `06_CLASSES_AND_ABILITIES`.

## Ordinary-life continuity

Character and NPC continuity should remember mundane facts when they have actually been established:
- who cooks badly or well;
- who forgets to eat;
- who complains about wet boots;
- who keeps fixing something before being asked;
- who prefers silence on watch;
- who borrows tools and forgets to return them;
- who sleeps lightly;
- who always notices the bad chair;
- who knows the local baker, clerk, quartermaster, medic, ferryman, or stable worker;
- who told a story before and now tells it differently.

Do **not** invent a permanent preference merely because a scene needs texture. New mundane facts become durable character continuity only when they are compatible with the owning character authority and are intentionally authored/approved.

## Social texture under pressure

War does not erase humor, attraction, irritation, pettiness, hobbies, gossip, appetite, boredom, curiosity, or stupid opinions.

Likewise, comedy does not erase danger. Characters should not become incompetent because a scene is funny. Victims of atrocities are never the joke; absurd circumstances, interpersonal timing, professional frustration, and familiar people irritating one another may be.

People may stop talking because there is nothing else worth saying. Comfortable silence is part of lived life.

## Location-state rule

The Dialogue Engine should receive the current location and chapter/story position and infer only consequences that are supported by current canon or observable scene context.

Do not globally assume:
- every settlement is short on food;
- every road is blocked;
- every civilian is displaced;
- every market is functioning normally;
- every character knows the latest military development.

Local conditions come from the owning story/world files and the scene payload.

## Economy boundary

Everyday economic pressure is real, but exact currency/prices/commerce rules belong in `12_ECONOMY_AND_REWARDS`.

This file establishes only the world-life principle that supplies, repairs, transport, food, shelter, medical needs, trade access, and disrupted routes can matter to ordinary people.

See:
- `../12_ECONOMY_AND_REWARDS/ECONOMY_MASTER.md`
- `../12_ECONOMY_AND_REWARDS/LIVED_ECONOMY_CONTEXT.md`

## Agent-authoring rule

A character agent should ask, implicitly or explicitly:
1. What is physically happening here?
2. What would this person notice because of their life and expertise?
3. What ordinary need or interruption exists around the plot?
4. What do they actually know at this story position?
5. Is saying nothing more natural than commenting?

The answer should make Diyse feel inhabited, not make every scene busier.