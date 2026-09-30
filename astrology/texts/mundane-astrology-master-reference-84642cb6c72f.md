---
title: Mundane Astrology — Master Reference
type: reference
status: living document — update as the astrology layer develops
created: 2026-06-05
house_system: Whole Sign (primary) · Placidus (secondary reference only)
locale: Washington, D.C. (mundane charts)
---

# Mundane Astrology — Master Reference

> **Purpose.** The **dictionary** — source shelf, locked US natal table, Katie's keywords, synods, Greer pairs. It is **not** the how-to. How to read: [[Reading the Charts — START HERE]]. Atoms (orbs, Sabians, families, cycles, houses): `Mundane Astrology Reference — Katie's Method.xlsx` (tab map: `_Grok/How Katie reads — the full shelf.md`).
>
> **Ground rules:** Whole Sign (Placidus nuance only) · mundane charts for **Washington, D.C.** · natal/founding stay at birthplace (US = Philadelphia) · her vocabulary over textbook. Live counts and tab lists do **not** live here — see the Primer / the shell.

---

## 0. The sources

- **Baigent, Campion & Harvey — *Mundane Astrology*** (Aquarian, 1984). The modern academic text; thinks in **cycles** (André Barbault's lineage). *Uses quadrant houses — see §7.*
- **C. C. Zain (Elbert Benjamine) — *Mundane Astrology*** (Church of Light). Older American Hermetic tradition; thinks in **national birthcharts + secondary progressions** and his own declination "Cycle" charts.
- **John Michael Greer — *The Astrology of Nations*** (2021). The modern practical cookbook; complete planet-in-house and planet-in-aspect delineations **written entirely in mundane language**. Adds: the binary planet pairs framework (Sun/Moon, Venus/Mars, Jupiter/Saturn, Uranus/Neptune), the ingress validity rule, eclipse timing by duration, Moon = the political class (not "the people"). Uses Goldstein-Jacobson dignities for the outers. *Uses Placidus — see §7.* Full digest: [[Greer — Astrology of Nations Study Notes]].
- **Katie's own Astrology Notes vault** (`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Astrology Notes/`) — her interpretive dictionary, an atomic/Zettelkasten system. **Her lineage = archetypal (Tarnas–Grof–Rudhyar) + Bill Tierney aspect-dynamics + an evolutionary/lived phrasing.** This is the voice to write in.
- **Ellynor Barz — *Gods and Planets: The Archetypes of Astrology*** (Chiron, trans. Matthews). Jungian/mythological: the planets as gods, myths as images of powers in the soul; full god-stories per planet, mythic readings of all 12 signs, the old Latin house names. Digested 2026-06-12 → [[Barz — Gods and Planets Study Notes]]; feeds the interpretation panel's "The god" layer (interp_blocks.json myth fields).
- **Bruno & Louise Huber — *Aspect Pattern Astrology*** (HopeWell, 2005). API school (Zurich). The aspect pattern as a "diagram of consciousness" — not isolated aspects but unified energy fields. Seven aspects as a plant-growth cycle (seed→sprout→flower→fruit→harvest→autumn→winter). Three colors = three motivations (red=achievement, blue=talent, green=awareness). Four developmental levels per aspect. 50+ named aspect figures as psychological building blocks (Learning Triangles, Yod, Kite, Dominant Triangle, etc.). Hard/soft planet interactions with aspect colors. Full digest: [[Huber — Aspect Pattern Astrology Study Notes]]; feeds the interpretation engine's narrative synthesis layer.
- **Marc Edmund Jones — *The Sabian Symbols* lineage / planetary-nodes work** (digested 2026-06-12). The planetary nodes as standing trigger-degrees; the trinity/elevation thesis and war-rule flags. Full digest: [[Jones — Planetary Nodes Study Notes]] (+ 3 Book Digest parts). Feeds Katie's Sky, the Characters node-elevations, and the Almanac's "Planetary Nodes today" card.
- **Michael Munkasey — *Midpoints*** (digested 2026-06-12). The 78 mundane midpoint pairs (mod-45 dial), Crisis Axes, and Midpoint Strikes. Full digest: [[Munkasey — Midpoints Study Notes]]; meanings in `midpoint_meanings.json`. Feeds Ingress Charts, Katie's Sky, and Characters.
- **Celeste Teal — *Identifying Planetary Triggers*** (digested 2026-06-12). The timing hierarchy — Rule of Three, transit-to-progressed precedence, returns, eclipse re-fires. Full digest: [[Teal — Identifying Planetary Triggers Study Notes]]. Feeds Katie's Sky's Trigger Stack and the Characters trigger panels.
- **Steven Forrest — *The Night Speaks*** (1993/2016; digested 2026-06-13). The project's **theory-of-synthesis** source — *how* astrology works (matter + meaning) and how symbols *blend* rather than stack (the Argument of Color; "the smallest unit of significance is the whole chart"). Full digest: [[Forrest — The Night Speaks Study Notes]]; it carries Katie's own captured synthesis method (planet=motivation, aspect=wiring, sign=toolshed, house=location; condition first) and the color-mixing model for the interpretation engine. (Forrest's step-by-step *delineation* method lives in *The Inner Sky* / *The Changing Sky* — not yet in the library.)
- **Noel Tyl — *Guide to Astrological Consultation*** (2007; digested 2026-06-13). The project's **whole-chart-synthesis** source — how to organize an entire chart into one developmental-need story (Developmental Tension; Psychological Need Theory; the Moon = the "reigning need"; the synthesis sequence; Tension Networks among houses). The antidote to siloed placement-reading. Full digest: [[Tyl — Astrological Consultation Study Notes]]; pairs with Forrest for the engine's synthesis spec.
- **Nicholas Campion — *The Practical Astrologer*** (1987; digested 2026-06-13). Campion's solo illustrated handbook of *all* branches. Carries a clean **three-stage interpretation method ending in synthesis** (analyze factors → find dominants & **contradictions** → weave one narrative around the central choice) — a third independent witness, with Tyl and Katie, to the whole-chart/central-tension method — plus explicit **weighting rules** (tighter orb stronger, applying > separating, luminary aspects amplified) and a compact **mundane toolkit** (planets/houses/signs in mundane; ingress + eclipse-by-modality + national charts; outer-planets-as-era, incl. Uranus in Gemini = "new humanitarian ideals; crises in thought and ideology"). Full digest: [[Campion — The Practical Astrologer Study Notes]]. (Note the Moon divergence flagged in §2b.)
- **Richard Tarnas — *Cosmos and Psyche*** (2006; **INTERIM digest 2026-06-16**). The project's **philosophical keystone** and the source of the *archetypal outer-planet world-transit method* underneath everything — the deep-cycle "tide" beneath the ingress/lunation "weather." Supplies the participatory/re-enchanted worldview, **archetypal multivalence** ("archetypally predictive, not concretely predictive"), the mythic reframes (Uranus = Prometheus, Pluto = Dionysus/evolutionary will), and the major cycles (Saturn–Pluto, Uranus–Pluto, Uranus–Neptune, **Saturn–Neptune** = the 2026 signature, Neptune–Pluto). Full digest: [[Tarnas — Cosmos and Psyche Study Notes]]. ⚠ **INTERIM** — drafted from Claude's knowledge (Apple Books copy not machine-readable); to be verified against captured pages. This is the named root of Katie's lineage (*archetypal: Tarnas–Grof–Rudhyar*).
- **Robert P. Blaschke — *Astrology: The Language of Life, Vol. I — Progressions*** (1998; digested 2026-07-09). The project's **progression-timing** source: three progression systems at a fixed **1:13:27** speed ratio — **secondary** (day/year, structural), **tertiary** (day/lunar-month, mood), **minor** (lunar-month/year, doctrine) — disciplined by **Carter's Natal Rule** ("no direction brings anything not in the natal") and **Law of Excitation** (a transit by one of the same pair fires a progressed "sensitive degree"). Written in a personal/esoteric register; the **mundane translation** (the three lenses as the nation's institutional/mood/ideological layers, applied to the locked US chart) is the load-bearing part for us. Full digest: [[Blaschke — Progressions Study Notes]]; adaptation: [[Progressions — Mundane Adaptation]]. *(Finding: the US secondary progressed New Moon seeded 19°26′ Pisces in 03-2026 — a fresh ~30-yr national chapter on "A table set for an evening meal / ingathering after the ordeal," dead on the re-founding thesis.)*
- **Generational astrology** (the **cohort layer**; concept distilled from Edwin Rose, *Generational Patterns Using Astrology*, 2010, digested 2026-06-26). The missing layer that groups the *populace* into datable birth-generations: the outer planets as the generational planets (Pluto = a generation's Sun, Neptune = its Moon, Uranus = its Ascendant), ten outer-planet **pair meanings**, and — its real prize — **Strauss & Howe's four-turning saeculum fused with astrology**: a US **84-yr** cycle (ignited by Uranus in early Gemini + Neptune on the Aries/Libra cusp: 1692→1776→1861→1941→**2025**) and a European **108-yr** cycle (ignited by a Saturn–Neptune conjunction in a fire sign → **1° Aries 2026**), fire/earth/air/water = Prophet/Nomad/Hero/Artist. Rose (in 2010) pre-registers a **2025–26 INTERNAL US structural convulsion** at the rare US–Europe re-sync — landing squarely on the chronicle's Saturn–Neptune-in-Aries spine (Forecast Ledger candidate). Full digest: [[Rose — Generational Patterns Using Astrology Study Notes]] (the concept only; a popular synthesis built on Strauss & Howe — hold at Tarnas's "archetypally, not concretely, predictive" discipline).

A future session can re-load the full long-form book digest from the standalone file **"Mundane Astrology — Study Notes.md"** (kept on Katie's computer); this Master Reference is the condensed, always-available version.

---

## 1. What mundane astrology is

The astrology of the **collective** — nations, cities, peoples, organizations, civilizations — rather than the individual. The oldest form (Babylon "divined for the State"). Two load-bearing ideas:

- **Subsumption** — the individual is contained within the mass; the natal chart sits *inside* the mundane chart.
- **The "body politic"** — the nation is an organic whole that can be healthy or "sick," which is *why* natal interpretive rules transfer to a nation.

---

## 2. Katie's method (how we actually work a chart)

From her own mundane practice (e.g. her *2025 Aries Solar Ingress* analysis):

1. **Cast the Aries Solar Ingress** for the year, set for **Washington, D.C.**, in **Whole Sign** (Placidus noted as secondary "for the nuance").
2. **Find the chart ruler** (ruler of the rising sign) and **trace the dispositor chain** — e.g. "chart ruler Uranus in the 3rd; ruler of Uranus in the 2nd conjunct Sun/Mercury, under the Sun's beams; ruler of Venus = Mars in the 6th…"
3. **Judge each planet by traditional condition** — sign dignity (rulership, exaltation, **detriment, fall**), **combustion / under the Sun's beams**, house debility (e.g. Mars weakened in the 6th), and **aspects weighed by orb**. Ask: is this planet *happy* or not?
4. **Speak at the right level (DR-013).** Symbolic reading is bold. Mundane translation names actors and **both poles**. A literal event in a literal window is a **separate** Forecast Ledger call. The old line “commit to a concrete mundane verdict” is level-1/2 speech, not a licence to smuggle a headline into the chart. How-to: [[Reading the Charts — START HERE]] §6–§7.

**Voice:** in mundane work, decisive and concrete; in natal work, lyrical, second-person, deeply empathetic.

---

## 2b. The binary planet pairs (Greer) — who in the nation

Greer organizes the planets as **four binary pairs plus Mercury:**

- **Sun / Moon** = the ruler and the ruled (executive power vs. the political class)
- **Venus / Mars** = women and men (women's vote/issues vs. men's vote/corporate-military)
- **Jupiter / Saturn** = corporate expansion and bureaucratic inertia (hierarchy that grows vs. hierarchy that endures)
- **Uranus / Neptune** = the individual and the mass (democracy/counterculture vs. collective movements/unity)

**Mercury** is the "elusive androgyne" floating between all pairs — press, transport, treaties, the national conversation.

This framework answers the question natal astrology never asks: **who in the nation** is affected by each planet? Every mundane interpretation should name a *mundane actor* (the government, the political class, the laboring classes, the military, corporations, etc.), not an abstract psychological principle.

**Key Greer distinction on the Moon:** The Moon = the **political class** (the ~20% with a political voice) and public mood; women. The **1st house ruler** = the ordinary people / the nation’s body. **DR-009:** she may say “the people (Moon)” — that Campion sense is sanctioned; do not “correct” it. The gauge still stands: Moon in harmony with the 1st-house ruler → voiced class and populace aligned; hostile → the political class has lost the plot.

---

## 3. The cycles framework (Baigent / Barbault) — the long arc

History unfolds through a **nested hierarchy of cycles**, longest → shortest, read together like telescopes of rising magnification. Outer-planet synods set the era's theme; shorter cycles and the annual ingress only *time and locate* it.

- **The conjunction is the seed; the opposition is the harvest.** Treat each planetary *pair* as one idea unfolding conjunction → opposition → back to seed; the hard sub-phases are crisis points.
- **Shorter cycles trigger the longer ones** into manifestation.
- **Barbault's Cyclical Index** = the summed angular separations of all ten pairs of the five outer planets. **Low = clustered = global tension/crisis; high = dispersed/relaxed.** A single "temperature" reading of the age.

### The synods and their meanings (the interpretive backbone)

- **Neptune–Pluto (~492 yr)** — whole epochs of civilization; the era's deep spiritual *ideals and aspirations*. Conjunctions seed great cultural ages.
- **Uranus–Neptune (~172 yr)** — civilization's unfoldment via **capital (Uranus) vs. labour (Neptune)**, conservatism vs. liberalism, capitalism vs. communism, industrialization.
- **Uranus–Pluto (~127 yr)** — **radical restructuring of peoples/nations**; "building again on the ruins of the old." (1965/66 = the computer/AI generation.)
- **Saturn–Uranus (~45 yr)** — conservative/**authoritarian**, the "politics of Order," imperialism, heavy capital. Strong Middle-East signature.
- **Saturn–Neptune (~36 yr)** — Barbault's paramount cycle of **socialism/idealism**; *"the dissolution (Neptune) of whatever has become negatively crystallized (Saturn)"* and the descent of new collective images.
- **Saturn–Pluto (~33 yr)** — **emerging nations, deep purgation, "resurrections"**; "back to basics," black-and-white thinking, the imposition of compulsive collective power; the square = a "crisis of authority."
- **Jupiter–Saturn (~20 yr)** — the **"Great Chronocrators"**: the ground-base of social structures and national identity. The **"Great Mutation"** (change of element) marks a civilizational reorientation — 1603 Fire → America; 1842 Earth → materialism; the current shift into **Air** (~2020 → 2060).

---

## 4. The annual engine — ingresses, lunations, eclipses

The **fine-grain timers and locators** that bring the big cycles down to a *time and place*. Use *with* the larger cycles and the national chart — never alone.

- **Cardinal Ingress chart** = the Sun's entry into 0° **Aries** (and Cancer/Libra/Capricorn), set for the capital (D.C.). It reveals the year's themes there. *Year-start debate:* Aries/spring equinox (most common) vs. Capricorn/winter solstice (Witte, Carter) vs. Libra/autumn (Troinski). Treat each as the whole year from a different vantage; the other cardinals mark sub-stages.
- **Ingress validity rule (Greer):** The Aries ingress chart's duration depends on the **modality of the rising sign:** **Fixed rising = full year; Cardinal rising = six months; Mutable rising = three months.** When the Aries chart expires, the next cardinal ingress takes over, subject to the same rule. This determines how many charts you need to cast per year.
- **Timing:** ingress charts act **~2–3 weeks before** the astronomical event ("events cast their shadow before them"); lunations **~3 days before**.
- **Reading one:** assess the outer-planet background first, then **give pride of place to the angles** — angular planets and close aspects to the angles show "what can be released into the world"; then the Sun; then midpoints to the angles.
- **Lunation-to-ingress comparison (Greer):** When casting a New/Full Moon chart for the capital, **always compare its positions to the current ingress chart.** If the lunation's Sun-Moon hits ingress positions (conjunct, opposite, square), it **times the events shown in the ingress chart.** A lunation that doesn't hit ingress positions = a quiet month. Greer's metaphor: ingresses are the hour hand, lunations are the minute hand.
- **Eclipses.** *Baigent:* a charged New Moon for the place of visibility. *Zain's empirical rule:* **a solar eclipse over a populated region brings a disaster to that region within a few months (more often after), near the central path; the eclipse chart shows the *nature* of it by house.** *Greer's timing rule:* **a solar eclipse is effective for as many years as it lasts in hours; a lunar eclipse is effective for as many months as it lasts in hours.**

## 4b. The lunar gestation cycle & Moon Families (Pessin) — CANONICAL DEFINITION

*(Moved here 2026-07-10 so the definition has a live home. Full method depth: [[Pessin — Lunar Shadows III Study Notes]] + [[Greer — Astrology of Nations Study Notes]] §Pessin.)*

- **The cycle:** every storyline is **seeded at a New Moon** and develops through a ~9-month gestation. The seed degree returns as its own **First Quarter (+273 days), Full Moon (+546 days), Last Quarter (+819 days)** — at the *same sign and degree* — a ~2¼-year seed→harvest arc. Seed (New Moon) vs. harvest (Full Moon) is the fundamental rhythm.
- **Moon Families** group lunations by shared degree band across these chains. The chronicle names four (see the Moon Families tab; two are **Nodal Families** — their seeds are nodal New Moons, not eclipses). "The Lineages" (Almanac/Moon Families) computes the true chains: same sign+degree at 273/546/819-day spacing.
- **Why New Moons matter here:** the working finding that the Money Machine's filings overwhelmingly seed in "The Eclipse Storm" degree band (→ a 2027 harvest), and the **Cancer Eclipse Spine** (dollar-order events on 24–30° Cancer eclipses striking the US Moon–Pluto, 19-year Metonic backbone; next strike 2028-07-22).
- **Use with §4's minute-hand rule:** a lunation times the ingress; its *family* tells you which running story the timing belongs to. The forward test of any family claim is the Forecast Ledger — a family preference is a tendency, never a proof.
- **Do not collapse eclipse genealogies:** a Pessin Moon Family is the
  273/546/819-day seed-phase clock; a Saros is the 223-lunation shadow series;
  a Metonic echo is the 235-lunation same-phase return near the same calendar
  date and degree. A Metonic echo may change Saros or may not be an eclipse.
  See [[The Shadow Has More Than One Ancestor — Saros, Metonic and Moon-Family
  Time]].

---

## 5. Zain's distinctive toolkit (hold separately)

- **The "Cycle" chart** — a chart for a locality at the moment a planet crosses the equator **south→north in declination**; each planet's Cycle governs its own affairs (Moon's Cycle = the lunation). Declination-based, *not* the synodic conjunction.
- **Major conjunctions** — a locality chart at the moment two planets conjoin = the meaning of that convergence there.
- **National/city birthcharts advanced by secondary progression** — his core doctrine: *"Major Events are attracted only when a Major Progressed Aspect within 1° relates by house to the department of life affected."* Read through **house rulership**.
- His US chart = **July 4 1776, 2:13 a.m., Philadelphia** (Gemini rising; he rules the US by **Gemini**). Baigent uses the **Sibley** chart (~5:10 p.m., Cancer Sun, Sagittarius rising). *Which US chart we trust used to be an open choice — **now settled, see §5b.***

---

## 5b. The United States natal chart — SETTLED (2026-06-15)

After casting every serious candidate and testing them against 17 American turning-points (Yorktown → today) in **The American Charts** (`04 - Synthesis/Cross-cuts/The American Charts.html`, builder `99 - Templates/build_us_charts.py`), the project's canonical US chart is:

> **July 2, 1776 · ~5:10 PM LMT · Philadelphia · Sagittarius 10°44′ rising · MC Virgo 28°54′.**

**Why July 2, not July 4:** July 2 is when the Continental Congress *voted* for independence, and it gives a live **Capricorn Moon** (28°20′, conjunct Pluto, on the Cancer–Capricorn people-vs-government axis) instead of Sibley's July-4 **void Aquarius Moon**. ("We are NOT a void-moon nation.")

**Why Sagittarius rising:** the rectification favored the Sagittarian (8th-house) architecture for the *systemic and foreign* turns that are this chronicle's spine (1913 Fed, 1944 Bretton Woods, 9/11, the Pluto-return war), while the Gemini-rising alternate owns the *domestic*-money events (1929, 1933 gold seizure, 1971 gold window). The Gemini chart is kept as a true secondary reading of the nation's own body and money.

**Gemini-rising overlay clock:** **July 2, 1776 · ~2:13 AM LMT · Philadelphia** — same vote-day as the locked chart, different hour (`build_us_charts.py` candidate `gem`). This is **not** Zain’s US chart in §5 (July 4, 1776, 2:13 a.m.). Do not mix the two clocks.

**Profection (birthday-strict):** annual profection flips on **2 July**, the locked chart’s birthday. Through 1 July 2026 the nation is still age **249 / 10th house (Virgo / Mercury)**. From 2 July 2026 it is age **250 / 11th (Libra / Venus)**. The workbook Profections tab’s 2026 row is the 11th-house year — do not apply that row to a June ingress.

**The chart, Whole Sign:**

| Body | Position | House | Note |
|---|---|---|---|
| Ascendant | Sagittarius 10°44′ | — | ruler **Jupiter** |
| Sun | Cancer 11°25′ | 8th | the debt/reserve-currency identity |
| Moon | Capricorn 28°20′ | 2nd | **detriment**, conjunct Pluto — the people fused to wealth/power |
| Mercury ℞ | Cancer 24°59′ | 8th | retrograde national voice |
| Venus | Cancer 0°39′ | 8th | |
| **Jupiter** | **Cancer 5°29′** | **8th** | **EXALTED — chart ruler at its finest** |
| Mars | Gemini 20°01′ | 7th | born from war with Britain |
| **Saturn** | **Libra 14°45′** | **11th** | **EXALTED** — both societal planets dignified |
| Uranus | Gemini 8°49′ | 7th | |
| Neptune | Virgo 22°23′ | 10th | the government's idealistic/propagandistic image |
| Pluto | Capricorn 27°36′ | 2nd | Pluto-return completed 2022 |
| N. Node | Leo 6°35′ | 9th | |

**Signature:** chart ruler **Jupiter exalted in Cancer in the 8th**, with **Saturn also exalted** — a nation whose institutions of faith/abundance and law/structure are both at their best tools, governing through the world's money (the 8th-house faith-and-finance empire). This is now THE chart for all US-chart work — profections, progressions, solar returns, transits-to-angles, and the mundane node/midpoint layers.

---

## 6. The mundane lexicon — in Katie's vocabulary

> Each planet/sign carries (a) its **mundane civic meaning** and (b) **Katie's archetypal keyword ties** (from her vault — the words to actually write with).

### Planets — essence, mundane role, Katie's keywords

| Planet | Essence ("Nature =") | Mundane role | Katie's keywords |
|---|---|---|---|
| **Sun** | to **Build** | the leader / head of state / supreme authority; national self-image | Authority · Illumination · "Everything revolves around the Sun" · Internal Constitution · Perception of the Soul |
| **Moon** | to **Nourish** | the **political class** (~20% with a voice) & public mood; women. 1st-house ruler = ordinary people. “People (Moon)” is sanctioned (DR-009) — do not correct it. | The reflecting one · Your Average Mood · Impulse to Gestate & Bring Forth |
| **Mercury** | **Communication** | press, transport, trade, treaties-as-documents | To Perceive & Reason · Endlessly Curious · Critical Thinking · "Speed of Thought Itself" · Data in, Data out |
| **Venus** | to **Magnetize** | the arts, diplomacy, social harmony, currency | Value · Harmony · Beauty of Form · Aphrodite |
| **Mars** | to **Energize** | the military, war, aggression, strife | Ares (God of War) · Conflict · Action · Capacity to Assert |
| **Jupiter** | to **Expand & Affirm** | law, religion, courts, expansion, wealth, alliances | Zeus (King of the Gods) · Faith · Courage to Hope · Saying "Yes" · Knowledge · Alliances |
| **Saturn** | to **Endure** | the state's structure, authority, the establishment, restriction, loss | Kronos (Stern Father) · Structure · Limits · Self-Respect · Dignity · "Nature = to Endure" · "ability to do what we don't feel like doing" |
| **Uranus** | (rebel/awaken) | revolution, disruption, technology, sudden reform | **Prometheus** (rebelled against the gods) · Awakener · Breakthroughs · Liberation · Innovation · Individualist · Absolute Truth |
| **Neptune** | (dissolve/idealize) | ideals & dissolution, socialism, the sea/oil, propaganda, scandal, glamour | Dissolution · the Ideal · Delusion · Mysticism · Utopian Social Ideologies · Transcendent · Oceanic Depths of the Unconscious · Non-ordinary States of Consciousness · Window Beyond the Ego |
| **Pluto** | (transform/purge) | collective power, the masses-as-force, transformation, destruction/rebirth | Resurrection · Power Struggles · Overwhelming & Catastrophic Extremes · Repression · Transformative · Ever-Evolving · Intensity · God of the Underworld |

### Signs — Katie's keyword ties

- **Aries** — Primal · Raw Strength · Survival Instinct · Initiative · Spontaneous · Competitiveness · Playing to Win · "Life Choosing Existence Over Surrender and Extinction"
- **Taurus** — Quality · the 5 Senses · Natural Habitat · Sticking with the Familiar · Wisdom of Simplicity · Silence · Consistent
- **Gemini** — Endless Learning · Eternal Quest for Information · Duality · Versatile · Mental Energy · Openness to the Unexpected · Insight
- **Cancer** — The Great Mother · Nurturing · Protective · Sensitivity · a Safe & Restorative Home · Raw Direct Emotion · Acceptance of Human Frailty
- **Leo** — Urge to be Seen & Celebrated · "Attention is a life-giver" · Spontaneous Self-expression · Creativity · Loyalty · Emotional Risk of Authentic Self-expression
- **Virgo** — Breaking Things Into Components · Editing · Processes · Details · the Comparison of the Ideal to the Actual · wanting to be seen as Competent
- **Libra** — Balance · Diplomatic · Perfect Equilibrium · Making Peace with Paradox · Perceptual Intelligence
- **Scorpio** — Focused Mars · Detective · Unflinching Insight · Psychological Truth · Raw Reality of Life · facing charged truths courageously
- **Sagittarius** — Philosopher · Scholar · Voyager · Natural Law · "Truth is More Important Than Facts" · Stretching Our Boundaries · Spirit
- **Capricorn** — Aim of Becoming an Elder · Self-discipline · Absolute Mastery · "If You Cut Corners, the Corners Will Cut You" · cold clear eye on reality · Integrity
- **Aquarius** — Paradigm Shifter · A New Type of Human Being · Process of Individuation · Free-thinking · Independence · On the Outside Looking In · Utopian & Dystopian · Alienation
- **Pisces** — Ocean of Consciousness · Primal Oneness with the Universe · Visionary Imagination · Realm of Archetypal Patterns · Enlightenment · Escapism · Ambient Psychic Energies

### Aspects — Katie's developmental (Tierney) dynamics

- **Conjunction** — "Direct Blending Initiates Pure Activity" · Co-Presence (two principles fused into one).
- **Opposition** — externalizes through **relationship & projection**; "face-to-face awareness"; tests self-determinism; well-integrated = the two enhance each other.
- **Square** — **crisis-oriented**, "purposeful turning-points in consciousness"; internalized tension, cardinal, relieved by decisive action; self-blocking only if its challenge is denied.
- **Trine** — line of **least** resistance; relaxation, harmony, pleasurable reception (can be passive).
- **Sextile** — opportunity through active, willing cooperation.
- **Quincunx** — the **nagging, almost-fated** adjustment; re-assemble & correct; analyze and dissect.
- **Texture layers:** applying vs. separating · lower vs. upper (which half of the cycle) · **dissociate / out-of-sign** aspects.

### Mundane houses — Katie's significations (Whole Sign; classic, in her words)

- **1st** — the **ordinary people of the nation**; general condition, prosperity, health and attitudes of the masses. (Sign on the 1st = the national myth/character.)
- **2nd** — the economy, money, banks, financial & material resources; national values.
- **3rd** — communications, the press, transport, schools, neighbouring countries.
- **4th** — the **party OUT of power (opposition)**; the **land**, real estate & its value, agriculture/mining/resource industries, the rural population; the nation's foundations.
- **5th** — entertainment, sport, speculation, children/birth rate, high society.
- **6th** — workers, unions, the civil service, the **armed forces** as service, public health.
- **7th** — **foreign affairs & policy**; **political treaties (explicitly NOT trade treaties)**; international incidents; peace, war, power politics; open enemies.
- **8th** — international finance, foreign investment, public mortality; national death/rebirth.
- **9th** — long-distance travel/shipping, religion & belief, higher education, the courts/law, publishing.
- **10th** — the **government / party IN power** when the chart takes effect; the **Executive Branch**; the power & authority of the gov't and the nation as a whole; national prestige.
- **11th** — the legislature, local government, allied nations; collective hopes & ideals.
- **12th** — the hidden: prisons, hospitals, asylums; subversion, secret societies; self-undoing.

*(She also works a **decan + dwad** layer on a 0° Aries dial — harmonic subdivisions, e.g. "the Libra Dwad in the Libra Decan.")*

---

## 7. ⚠️ House systems — the standing correction

**We use Whole Sign. Both books lean quadrant**, so their house-specific techniques get translated:

- **Houses = whole signs counted from the rising sign.** The **10th house = the whole sign in tenth place, NOT wherever the MC degree falls.**
- **The MC stays a sensitive *point*** (public standing, what's culminating) and its tight aspects matter — but in Whole Sign the MC can sit in the 9th, 10th, or 11th whole-sign house, and *that* placement is the house story.
- **Angles still lead** (rising sign + its ruler; the sign/planets at the MC) — read by **sign**, not by quadrant cusp.
- Techniques that *only* work with intermediate cusps (some astrocartography/local-space) **don't port** — say so rather than fudge.
- Everything **house-system-independent** — the cycles, synod meanings, planet/sign symbolism, eclipse & ingress logic — ports cleanly.

---

## 8. Sign-rulership of nations & cities (classic reference, via Zain)

Abbreviated; "commonly used," not gospel. **Aries** — England, Germany (older), Japan, Palestine. **Taurus** — Ireland, Persia, Poland, Austria. **Gemini** — **United States (7°)**, Belgium, Wales, Lower Egypt. **Cancer** — Scotland, Holland, Germany; *New York.* **Leo** — France, Italy, Sicily; *Rome, Philadelphia, Chicago.* **Virgo** — Brazil, Turkey, Switzerland, Virginia. **Libra** — China, Tibet, Argentina, Upper Egypt; *Los Angeles.* **Scorpio** — Norway, Morocco, Algeria, Bavaria, Judea; *Washington, D.C.* **Sagittarius** — Spain, Australia, Arabia, Hungary. **Capricorn** — India, Mexico, Greece, Afghanistan; *Boston.* **Aquarius** — **Russia**, Prussia, Sweden, Abyssinia. **Pisces** — Portugal, Normandy, the Sahara.

---

## 9. The Freedom 250 configuration, in Katie's words

The project's premise: the 2025–26 outer-planet sky echoes the American Revolution's (≈1776). Letting Katie's own keywords assemble across the current signatures — now fully integrated into the chronicle via the transit notes, interpretation notes, subplot astrological signatures, and the three overlay artifacts:

- **Pluto in Aquarius** → *Resurrection / Power Struggles / Overwhelming & Catastrophic Extremes* in *Paradigm Shifter / A New Type of Human Being / Process of Individuation* → **a catastrophic, underworld power-struggle over what the new human being will be.**
- **Saturn–Neptune in Aries** → *Structure / Limits / Endure* meeting *Dissolution / the Ideal / Utopian Social Ideologies* in *Primal / Survival Instinct / "Life Choosing Existence Over Surrender and Extinction"* → **enduring structure dissolved into a raw, survival-driven new ideal.** (Note: Saturn–Neptune is Barbault's idealism/"dissolution of the crystallized" synod — §3.)
- **Uranus in Gemini** → *Prometheus / Awakener / Breakthroughs / Liberation* in *Endless Learning / Eternal Quest for Information / Duality* → **the Promethean awakening — and doubling — of information itself.**
- **Jupiter in Leo** → *Expand & Affirm / Faith / Courage to Hope* in *Urge to be Seen / "Attention is a life-giver" / Spontaneous Self-expression* → **faith in spectacle; affirmation of the sovereign, seen self.**

---

## 9b. The most dangerous and most fortunate mundane aspects (Greer)

**Most dangerous (in order):**
1. Sun–Neptune hostile — "far and away the most unfortunate." Downfall, collapse, scandal.
2. Sun–Saturn hostile — loss of power, obstacles, economic stagnation.
3. Sun–Mars hostile — conflict, partisan hatred, violence against officials.
4. Mars–Saturn hostile — public discontent, rioting, crimes against authority.
5. Moon–Saturn hostile — misfortune to political class and country, government may collapse.

**Most fortunate (in order):**
1. Sun–Jupiter helpful — "the most favorable aspect in mundane astrology." Peace, prosperity, good luck.
2. Venus–Jupiter helpful — "one of the best aspects in any mundane chart." Peace, goodwill, prosperity.
3. Moon–Jupiter helpful — peace and prosperity, economy expands.
4. Sun–Moon helpful — harmony between government and political class.
5. Uranus–Neptune helpful — harmony between political class and people, constructive reform.

**Neptune caution:** Neptune is almost always malefic in mundane charts (Greer's most surprising finding). Only when completely unafflicted does Neptune favor democratic causes and peace. In any other condition: chaos, mass movements, speculative bubbles, deception, collapse.

---

## 10. Maintenance

This file is the **dictionary**. Do not park live counts, tab lists, or “how to read a chart” here — those rot. Method: [[Reading the Charts — START HERE]]. Drawer: the xlsx. US natal lock: §5b / DR-002.

Dated snapshot (2026-06-07/08, not live state): eight cardinal ingresses were first cast; 36 pair notes exist in `03 - Astrology/Interpretations/`; subplot signatures regenerate with `subplot_signatures.py`. For current Observatory tabs and counts, read the Primer / the shell.

## The 36 interpretation notes

The planet-pair dictionary behind every subplot signature — one note per pair, each with the mundane read, the trigger speed, and the chronicle arcs it drives (in `03 - Astrology/Interpretations/`):

[[Jupiter–Neptune]] · [[Jupiter–Pluto]] · [[Jupiter–Saturn]] · [[Jupiter–Uranus]] · [[Mars–Jupiter]] · [[Mars–Neptune]] · [[Mars–Pluto]] · [[Mars–Saturn]] · [[Mars–Uranus]] · [[Mercury–Jupiter]] · [[Mercury–Mars]] · [[Mercury–Neptune]] · [[Mercury–Pluto]] · [[Mercury–Saturn]] · [[Mercury–Uranus]] · [[Mercury–Venus]] · [[Neptune–Pluto]] · [[Saturn–Neptune]] · [[Saturn–Pluto]] · [[Saturn–Uranus]] · [[Sun–Jupiter]] · [[Sun–Mars]] · [[Sun–Mercury]] · [[Sun–Neptune]] · [[Sun–Pluto]] · [[Sun–Saturn]] · [[Sun–Uranus]] · [[Sun–Venus]] · [[Uranus–Neptune]] · [[Uranus–Pluto]] · [[Venus–Jupiter]] · [[Venus–Mars]] · [[Venus–Neptune]] · [[Venus–Pluto]] · [[Venus–Saturn]] · [[Venus–Uranus]]
