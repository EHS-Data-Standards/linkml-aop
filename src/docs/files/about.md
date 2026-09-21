# linkml-aop

A LinkML schema for Adverse Outcome Pathways, with EMOD (Evidence Model) expansions.

## Purpose

The schema serves two purposes at once.

**Validating content already in the AOP-Wiki.** AOP-Wiki content is curated by people, in
free text as much as in structured fields. Expressing the data model as a LinkML schema
makes it possible to check that content against stated expectations - that a referenced
Key Event exists, that a controlled vocabulary is used where one applies, that an
assertion carries the evidence it claims.

**Providing a basis for AOPs derived by automated approaches.** Adverse Outcome Pathways
can be assembled from analysis of multimodal data and from text mining. Such a pathway is
only as useful as the record of where each of its parts came from, so the schema has to
be able to carry that record: which observation was made, by what method, and what was
inferred from it.

Both purposes rest on the same requirement - what evidence supports must be
distinguishable from what has been inferred - which is why `Assay`, `Observation`, and
`Evidence` are separate classes rather than fields on an Event, and why the definition of
`Event` is explicit that a Key Event is an abstraction rather than something that happened.

## Source of the schema

The schema is generated from the MySQL database behind
[AOP-Wiki EMOD 3.0](https://emod.aopwiki.org) and then curated. See the repository README
for the generation and curation workflow, and
[`src/docs/dev/definition_rationale.md`](https://github.com/EHS-Data-Standards/linkml-aop/blob/main/src/docs/dev/definition_rationale.md)
for the reasoning behind individual class definitions.
