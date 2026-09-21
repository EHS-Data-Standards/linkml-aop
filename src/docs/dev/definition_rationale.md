# Definition rationale

Background, sources, and reasoning for the class and attribute definitions in
[`aop_definitions_and_enums.py`](../../linkml_aop/curation_helpers/aop_definitions_and_enums.py). The Python file holds the
text that goes into the schema; this file records why that text says what it says.

## Aop, KeRelationship, and Stressor

These descriptions came with the `join-classes` work and are quoted, not written here.
Checked against the
[AOP Developers' Handbook 2.8](https://aopwiki.org/handbooks/6) (released 2026-03-12) on
2026-09-21:

- **Aop:** verbatim from the handbook's introduction to AOPs, three sentences. The first
  sentence had been paraphrased ("starting with initial interaction(s) between a stressor
  and a biomolecule"); it now matches the handbook ("commencing with initial
  interaction(s) of a stressor with a biomolecule").
- **KeRelationship:** verbatim from the handbook's Table 1 definition of a Key Event
  Relationship.
- **Stressor:** *source not found.* The handbook has no formal stressor definition, and
  the text ("An external or internal factor that induces a perturbation...") does not
  appear in it. Its nearest statement is about prototypical stressors: "stressors for
  which responses at multiple KEs in addition to the MIE have been well documented."

## Event

**Definition** (`CLASS_DESCRIPTIONS["events"]`, revised 2026-09-21):

> An Event is a measurable biological change at a defined level of biological
> organization, described in the abstract so that it can be measured and supported by
> evidence. An Event may be described in the AOP-Wiki before it is used anywhere, and
> becomes a Key Event when it is incorporated into an Adverse Outcome Pathway. The AOP-Wiki
> defines a Key Event as "a change in biological or physiological state that is both
> measurable and essential to the progression of a defined biological perturbation leading
> to a specific adverse outcome." Within a pathway, the Key Events at the starting and ending positions are Molecular Initiating
> Events and Adverse Outcomes, and those between them are intermediate Key Events. These
> positions are recorded per pathway and rest on the mechanistic evidence available to the
> authors of that pathway, so one Event may serve as a Molecular Initiating Event in one
> Adverse Outcome Pathway and as an intermediate Key Event in another.
>
> Whether an Event's change can be measured experimentally depends on factors such as the
> level of biological organization and the species. Molecular and cellular changes can be
> tested and measured in model organisms in a laboratory context. Changes up to the
> population level can be observed in model organisms in a lab and in ecological indicator
> species. Changes at the individual or population level in humans are observed through
> epidemiological and clinical studies rather than tested.
>
> An Event is a type of change rather than a particular occurrence of one, and is
> therefore not an exposure event in an open system: the exposure of a population to a
> pollutant in air or water is not an Event. Such real-world exposures can rarely be
> observed at the molecular level, so the Molecular Initiating Event that follows one is
> not usually observable at the time of the exposure event. Describing Events in the
> abstract keeps supporting evidence separate from what is inferred.

**Rationale:**

- *The class is Event, not Key Event.* An Event can be described in the AOP-Wiki before it
  is used in any pathway, so defining the class as a Key Event would be false for every
  such record. The definition names when the transition happens instead: incorporation
  into an AOP.
- *Event > Key Event > MIE and AO is a real hierarchy, but not an inheritance one.* Each
  level is conferred by a relationship rather than by the Event itself:

  | Level | What confers it | Where it is recorded |
  |---|---|---|
  | Event | nothing - this is the class | `events` |
  | Key Event | membership in an AOP | an `aop_events` row exists |
  | MIE / intermediate KE / AO | position within that AOP | `aop_events.type` |

  `aop_events.type` takes `MolecularInitiatingEvent`, `KeyEvent`, or `AdverseOutcome`
  (see `EVENT_GROUP_BY_DB_TYPE` in the web app's `EventsTableForAopPage.tsx`;
  `main.py` defaults the column to `KeyEvent`). Because the value sits on the membership
  row, the same Event can be a Molecular Initiating Event in one AOP and an intermediate
  Key Event in another. LinkML `is_a` subclasses would fix the role to the Event
  permanently and could not express that, so the schema keeps one `Event` class and the
  definition states where each distinction lives. Nothing is lost: the hierarchy remains
  queryable through `aop_events`.
- *The AOP-Wiki's Key Event definition is quoted, not replaced.* It was the class
  description in the `join-classes` work, and it adds a criterion the rest of the
  definition does not state: a Key Event is *essential to the progression* toward an
  adverse outcome. It is quoted and attributed at the point where an Event becomes a Key
  Event, since that is what it defines.
- *Type, not occurrence.* A Key Event is an abstract, generalized description of a kind of
  biological change, not an individual happening. Without this, consumers of the schema
  can read `Event` in the everyday sense and conflate it with an exposure event occurring
  in an open system.
- *Exposure events are excluded explicitly.* Population-level exposure to a pollutant in
  air or water is the case most likely to be mistaken for an `Event`, so it is named
  outright rather than left to inference. Exposure is modelled elsewhere: `Stressor`, and
  `ExperimentSetup.causal_agent` for the controlled case.
- *Why the abstraction matters.* A Molecular Initiating Event triggered by a real-world
  exposure usually cannot be observed at the time of exposure. Describing Events in the
  abstract is what makes them measurable, and keeps evidence-supported claims distinct
  from inferred ones. The definition states this reason rather than only asserting the
  rule.
- *Measurable, but not necessarily in a laboratory.* An earlier draft said an Event is
  described so that it "can be tested in a laboratory", which is wrong at the upper levels
  of `BiologicalOrganizationEnum`. Lab testability is not a property of the level alone: a
  population-level change is measurable in the laboratory for a model organism or an
  ecological indicator species, and not for humans, where the same level is reached
  through epidemiological and clinical observation. The definition therefore names the
  level *and* the species as the factors, and keeps observational evidence inside the
  definition rather than treating it as an exception.
- *Three paragraphs.* Identity and hierarchy, then measurability, then what an Event is
  not. The definition is too long to read as one block. `description_lines` writes these
  as a folded block scalar with two blank lines between paragraphs, which YAML folds into
  the single blank line that keeps the paragraph break in the parsed value.

## Assay

**Definition** (`CLASS_DESCRIPTIONS["assays"]`, adopted 2026-09-20):

> A defined experimental method for measuring a biological change, structured so that its
> elements - the biological object measured, the process it takes part in, the detection
> technology, and the taxa and biological target families it applies to - can be matched
> against the Key Events the assay can inform. Assays are how New Approach Methodologies
> (NAMs) connect to Adverse Outcome Pathways, and an assay may be specified by one or more
> test guidelines. Some assays have an inherent directionality, meaning they are designed
> to detect change in a specific direction, such as an agonist or an antagonist effect on
> a specific molecular target.

**Rationale:**

- *"Structured so that its elements … can be matched."* The EMOD 3.0 feature list describes
  the Assay class as one that "structures method elements for more computable integration
  between AOPs & NAMs". The elements named in the definition are the class's own
  attributes: `objects`, `processes`, `detection_technology`, `taxon_terms`, and
  `bio_target_families`. Naming them ties the definition to what the class actually holds.
- *"Key Events the assay can inform."* An assay measures a biological change that bears on
  a Key Event; it does not measure the Key Event itself, which is an abstraction (see the
  Event rationale above).
- *"One or more test guidelines."* The mouse local lymph node assay is covered by OECD TG
  429, 442A, and 442B, so the relationship is many-to-many in both directions.
- *Directionality.* Some assays detect change in one direction only, so a negative result
  means "no change in that direction" rather than "no effect". An agonist assay and an
  antagonist assay against the same target are different assays, and matching an assay to
  a Key Event has to respect that. The direction itself is carried by
  `Assay.biological_action_id`, whose enum includes `increased` and `decreased`; the
  definition says why that attribute matters rather than restating its values.

## TestGuideline

**Definition** (`CLASS_DESCRIPTIONS["test_guidelines"]`, adopted 2026-09-18):

> A standardized test method published by a regulatory or intergovernmental body, such as
> an OECD Test Guideline or an EPA OCSPP test guideline, that specifies how to carry out
> one or more assays so that the resulting data are accepted for regulatory hazard
> assessment of chemicals. In EMOD, a test guideline is linked to the Assays it covers and
> to the Key Events those Assays measure.

**Rationale:**

- *"Standardized test method … accepted for regulatory hazard assessment."* OECD
  describes its Guidelines for the Testing of Chemicals as a collection of internationally
  agreed testing methods used by government, industry, and independent laboratories to
  identify and characterise potential hazards of chemicals. Under the OECD Mutual
  Acceptance of Data (MAD) system, member countries accept studies performed to these
  guidelines in another member country. EPA states that its Endocrine Disruptor Screening
  Program test guidelines are "generally intended to meet testing requirements under
  TSCA, FIFRA and FFDCA". Regulatory acceptance is the feature common to both sources, and
  it is what separates a test guideline from an ordinary published assay protocol.
- *"Specifies how to carry out one or more assays."* Test guidelines and assays are
  many-to-many in EMOD data. In the skin-sensitisation use case,
  `OECD TG 442C` covers three assays (DPRA, ADRA, kDPRA), while the single mouse local
  lymph node assay (LLNA) is covered by `OECD TG 429`, `442A`, and `442B`. This is why
  `test_guideline_assays` is modelled as a bidirectional reference.
- *"Linked to … the Key Events those assays measure."* Describes the
  `test_guideline_events` relationship. OECD TGs 442C, 442D, and 442E are each titled
  after the skin-sensitisation AOP Key Event they address (covalent binding to proteins,
  keratinocyte activation via ARE-Nrf2, dendritic cell activation).
- *"such as" OECD or EPA.* The issuing bodies are examples, not a closed list, so
  guidelines from other bodies (e.g. ISO, ICH) fit without redefining the class.

**Attribute descriptions** (`test_guideline_definitions`):

- `short_title` is the uploader's lookup key for linking guidelines to assays and events,
  so the description states that it is unique and gives both the OECD and EPA number forms.
- `full_title` says "as published by the issuing body" because the source data is
  inconsistent: in `aleksic.json`, TG 442C and 442E use OECD's own `Test No. 442C: ...`
  form while 442D, 429, 442A, and 442B repeat the short title instead. The description
  states the intent; correcting the data is a separate change in the web app.
- `citation_id` points at the guideline document itself (e.g. OECD Guidelines for the
  Testing of Chemicals, Section 4, with a DOI), not at a paper that uses the guideline.

**Identifier conventions seen in the sources:**

- OECD: `Test No. <number><letter>`, grouped into five sections (1 Physical Chemical
  Properties; 2 Effects on Biotic Systems; 3 Environmental Fate and Behaviour; 4 Health
  Effects; 5 Other Test Guidelines). EMOD `short_title` values use the form `OECD TG 442C`.
- EPA OCSPP: series number and title, e.g. `890.1250 – Estrogen Receptor Binding`
  (series 890 is the EDSP).

**Sources:**

- [OECD Guidelines for the Testing of Chemicals](https://www.oecd.org/en/topics/sub-issues/testing-of-chemicals/test-guidelines.html)
  (returned HTTP 403 to automated fetches on 2026-09-18; OECD wording above was taken
  from OECD's section pages and search summaries of this page)
- [OECD Guidelines for the Testing of Chemicals, Section 4](https://www.oecd.org/en/publications/serials/oecd-guidelines-for-the-testing-of-chemicals-section-4_g1gha298.html)
- [EPA EDSP Test Guidelines and Guidance Document](https://www.epa.gov/test-guidelines-pesticides-and-toxic-substances/edsp-test-guidelines-and-guidance-document)
- EMOD example data: `aopwiki_emod_web_app/inputs/skin_sensitization/aleksic.json`
