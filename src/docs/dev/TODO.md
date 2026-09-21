# To do: schema update for new EMOD tables

Branch: `update-schema-new-emod-tables` (no upstream set). Nothing committed yet.
Full work record: `/Users/ginniehench/Developer/ehmech/docs/linkml_aop_schema_update_plan.md`.

## Done

- [x] **Step 1: migrate the EMOD DB.** Empty DB brought to alembic head `e426e452227d`
      (17 migrations); `alembic check` shows no drift from `models.py`. The `mysql` and
      `api` containers are left running in `aopwiki_emod_web_app`.
- [x] **Step 2: generate the base schema.** `outputs/linkml_schemas/aop_wiki_emod_linkml.yml`
      in the web app (81 classes).
- [x] **Step 3: copy into linkml-aop.** `inputs/schemauto_generated_emod_linkml_09-18-2026.yml`.
- [x] **Step 4: update curation constants** in `curate_emod_linkml.py`:
  - [x] dropped `aop_batch_imports`, `batch_imports`, `can_event_merge_groups`,
        `can_event_merge_group_members`
  - [x] `batch_import_id` dropped from every class (`DROPPED_ATTRS_ALL_CLASSES`)
  - [x] eight FK-only join tables reclassified to `BIDIRECTIONAL_INVERSE`;
        `experiment_setup_cell_terms` to `PURE_PIVOT_UNIDIRECTIONAL`
  - [x] curated ranges for new FKs, `Observation.stressor_id` and `Evidence.citation_id`
  - [x] stale keys fixed: `evidence_id` → `confidence_id` (11 tables),
        `evidences.reference_id` → `citation_id`
- [x] **Step 5 (partly done): definitions.**
  - [x] class definitions: `TestGuideline`, `Event`, `Assay`
  - [x] `TestGuideline` attribute descriptions: `short_title`, `full_title`, `citation_id`
  - [x] support for multi-paragraph and colon-containing descriptions (`description_lines`)
  - [x] schema-level purpose statement in `SCHEMA_HEADER`
  - [x] About page (`src/docs/files/about.md`)
  - [x] rationale recorded in `src/docs/dev/definition_rationale.md`
- [x] **Dev docs location.** `src/docs/dev/` holds tracked, unpublished maintainer docs
      (this list and `definition_rationale.md`); only `src/docs/files/` is published.

- [x] **Generated artifacts renamed to `aop_emod_linkml`.** The cookiecutter `linkml_aop.*`
      artifacts (11 in `project/`, plus `datamodel/linkml_aop.py`) are deleted;
      `datamodel/__init__.py` imports `aop_emod_linkml`; the justfile's OWL/Java/TypeScript
      steps now check their args correctly and name output after the schema file.
      `src/linkml_aop/` stays as the Python package name.

- [x] **`src/linkml_aop/schema/linkml_aop.yaml` archived in place.** The original
      hand-written AOP schema is kept for reference, marked by a header comment and the
      LinkML `deprecated:` field. (It already failed `gen-python` before archiving:
      `string` range without importing `linkml:types`.)

## Open

- [ ] **`tests/test_data.py`** is skipped and still targets the old `AOPathwayCollection`
      class, which the EMOD schema does not have.
- [ ] **`ExperimentSetup` class definition**, the last new class without one. Deferred
      until after this work is committed.
- [ ] **Step 6: regenerate and verify.**
  - [x] `just curate`
        (rewrites the input file in place; the web-app copy is the clean original)
  - [x] `just test` (0 lint errors; example data validates)
  - [x] `just site`
  - [ ] review the schema diff
  - [ ] commit

## Noted, not scheduled

- About page: once EnviroHealthMech is further along, add a short "Used by" line pointing
  to it. (A section comparing linkml-aop with dismech was removed: dismech does not use
  this schema.)
- Leftover config with no effect: `CURATED_RANGES["assays"]` keys `reference_id` and
  `taxon_term_id`; `CURATED_RANGES["statuses"]`; three `CLASS_RENAMES` entries for join
  tables that are no longer classes.
- Web app source data: `full_title` in `inputs/skin_sensitization/aleksic.json` is
  inconsistent (some entries repeat the short title instead of OECD's `Test No. ...` form).
- README gaps: the output filename rename between repos; that table drops, join-table
  handling, and FK ranges live in `curate_emod_linkml.py`; that uncurated FKs lose their
  range; `generate_linkml_schema.sh` does not create `outputs/linkml_schemas/`.
