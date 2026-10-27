# AOP-EMOD Schema Elements

The six core classes of the AOP-Wiki data model with EMOD, as a tree: the pathway (`Aop`), its parts (`Event`, `KeRelationship`), and the evidence model that supports them (`Assay`, `Observation`, `Evidence`). Only the slots that link the classes, plus the few that define each one, are shown. The full schema is [aop_emod_linkml.yaml](https://github.com/EHS-Data-Standards/linkml-aop/blob/main/src/linkml_aop/schema/aop_emod_linkml.yaml).

An Assay can link to Events and to Key Event Relationships. `KeRelationship.assays` holds assays that measure both the upstream and the downstream Event of the relationship in the same test system, so that one assay can inform the relationship as a single module. The EMOD database has no table for this link; the curation script adds it.

```text
Aop
├── id, title                                              integer, string
├── events: [AopToEvent]                                   the Events in this pathway
│   ├── event_id ──────────────────────────────┐           Event
│   ├── type                                   │           string; the Event's role in THIS pathway
│   │                                          │           (MIE, KE or AO); one Event can differ per AOP
│   └── essentiality_id                        │           ConfidenceLevel: high | moderate | low | not specified
├── ke_relationships: [AopToKeRelationship]    │
│   ├── relationship_id ───────────────────────┼──┐        KeRelationship
│   ├── confidence_id                          │  │        ConfidenceLevel
│   └── directness_id                          │  │        Directness: adjacent | non-adjacent
└── assays: [Assay]                            │  │
                                               │  │
Event ◄────────────────────────────────────────┤  │        a measurable biological change, in the abstract
├── id, title                                  │  │        integer, string
├── biological_organization_id                 │  │        LevelOfBiologicalOrganization
├── assays: [Assay]                            │  │        methods that can measure it
└── observations: [Observation]                │  │        measurements that have been made of it
                                               │  │
KeRelationship ◄───────────────────────────────┼──┤        a causal, predictive link between two Events
├── id                                         │  │        integer
├── upstream_event_id ─────────────────────────┤  │        Event
├── downstream_event_id ───────────────────────┤  │        Event
├── weight_of_evidence                         │  │        string (prose)
└── assays: [Assay] ───────────────────────────┼──┼──┐     assays that measure both Events in the same
                                               │  │  │     test system, so one assay informs the KER as a module
                                               │  │  │
Assay ◄────────────────────────────────────────┼──┼──┤     a defined method for measuring a change;
├── id, title                                  │  │  │     how NAMs connect to AOPs
├── detection_technology                       │  │  │     string
├── biological_action_id                       │  │  │     BiologicalAction
├── objects / processes                        │  │  │     [BiologicalObject] / [BiologicalProcess]
├── events: [Event] ───────────────────────────┤  │  │     the Events it can inform
├── ke_relationships: [KeRelationship] ────────┼──┤  │     inverse of KeRelationship.assays
└── aops: [Aop]                                │  │  │
                                               │  │  │
Observation ◄──────────────────────────────────┼──┼──┼──┐  one measured result
├── id                                         │  │  │  │  integer
├── assay_id ──────────────────────────────────┼──┼──┘  │  Assay; the method that produced it
├── stressor_id                                │  │     │  Stressor
├── biological_action / process / object       │  │     │  what changed, and how
├── events: [Event] ───────────────────────────┘  │     │  the Events it is a measurement of
└── citations: [Citation]                         │     │
                                                  │     │
Evidence                                          │     │  a pair of Observations bearing on one KER
├── id                                            │     │  integer
├── relationship_id ──────────────────────────────┘     │  KeRelationship
├── upstream_observation_id ────────────────────────────┤  Observation
├── downstream_observation_id ──────────────────────────┘  Observation
└── citation_id                                            Citation
```
