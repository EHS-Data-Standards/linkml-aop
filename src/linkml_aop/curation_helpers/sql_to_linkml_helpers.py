__all__ = [
    "SCHEMA_HEADER",
    "SHARED_SLOTS",
    "LINKML_BUILTIN_TYPES",
    "WIKI_TABLES_TO_DROP",
    "DROPPED_ATTRS",
    "PURE_PIVOT_UNIDIRECTIONAL",
    "BIDIRECTIONAL_INVERSE",
    "JOIN_TABLES_TO_BIDIRECTIONAL_RELS",
    "JOIN_TABLES_TO_UNIDIRECTIONAL_RELS",
    "CURATED_RANGES",
    "CLASS_ORDER",
    "CLASS_RENAMES",
]

# Schema header written verbatim at the top of the output file.
# Sourced from aop_wiki_linkml.yml; inlined here to make the script self-contained.
SCHEMA_HEADER= """\
name: aopwiki-emod
id: http://example.org/aopwiki-emod
default_prefix: http://example.org/aopwiki-emod/
title: AOP Wiki Data Model with EMOD
description: >-
  This is a LinkML schema for the AOP-Wiki data model,
  extended with EMOD concepts.
prefixes:
  linkml: https://w3id.org/linkml/
  xsd: http://www.w3.org/2001/XMLSchema#
  foaf: http://xmlns.com/foaf/0.1/
  schema: http://schema.org/
  dcterms: http://purl.org/dc/terms/
  prov: http://www.w3.org/ns/prov#
default_range: string

imports:
  - linkml:types

# Slot defintions shared across multiple classes
slots:
  changed_at:
    description: Timestamp of when the record was last changed
    range: datetime
  created_at:
    description: Timestamp of when the record was created
    range: datetime
  updated_at:
    description: Timestamp of when the record was last updated
    range: datetime

# Class definitions
"""


SHARED_SLOTS = {"created_at", "updated_at"}

# LinkML built-in scalar types — excluded from PascalCase conversion.
LINKML_BUILTIN_TYPES = {
    "string", "integer", "float", "double", "decimal",
    "boolean", "date", "datetime", "time", "uri",
    "uriorcurie", "curie", "ncname",
}

# Tables from the aop-wiki DB should not be part of the schema at this stage.
WIKI_TABLES_TO_DROP = [
    "alembic_version",
    "entity_counts",
    "oecd_metrics",
    "roles",
    "assignments",
    "event_stressors",
    "citation_biological_target_families",      # redundant: BioTargetFamily.batch_import_id -> BatchImport -> citation
    "chemical_synonyms",                        # should be handled in future using external references
    "citation_relationships",                   # no content at present so skip
    "profiles",                                 # properties should be combined with User class
    "aop_contributors",                         # should be revised so that all user roles are captured in the same manner
    "aop_coaches",                              # should be revised so that all user roles are captured in the same manner
    "stressor_chemicals",                       # could be handled using external references and more time is needed to set this up
    "chemicals",                                # could be handled using external references and more time is needed to set this up     
    "url_links",                                # could be expanded to serve more entities than just AOPs; needs more time to set this up
    "relationship_logs",
    "aop_logs",
    "event_logs",
    "stressor_logs",
]

# Attributes to drop from specific classes. Keys are sql-based class names.
DROPPED_ATTRS: dict[str, list[str]] = {
    "aops": ["status_id", "saaop_status_id", "user_defined_mie", "user_defined_ao", "references"],
    "stressors": ["chemical_description", "characterization_of_exposure", "references"],
    "observations": ["process_is_phenotype", "other", "notes"]
}


# Join tables that collapse to a unidirectional multivalued reference on the parent.
# Format: join_table -> (parent_class, attr_name, target_range)
PURE_PIVOT_UNIDIRECTIONAL: dict[str, tuple[str, str, str]] = {
    "assay_objects": ("assays", "objects", "biological_objects"),
    "assay_processes": ("assays", "processes", "biological_processes"),
    "assay_taxon_terms": ("assays", "taxon_terms", "taxon_terms"),
    "aop_url_links": ("aops", "url_links", "url_links"),
    "event_sub_events": ("events", "event_components", "sub_events")
}

# Join tables that collapse to bidirectional inverse multivalued refs.
# Format: join_table -> (parent_class, parent_attr, inverse_class, inverse_attr)
BIDIRECTIONAL_INVERSE: dict[str, tuple[str, str, str, str]] = {
    "event_assays": ("events", "assays", "assays", "events"),
    "observation_events": ("observations", "events", "events", "observations"),
}

# Join tables that stay as top-level classes; both class_a and class_b get a
# multivalued attr pointing to the join table.
# Format: join_table -> (class_a, class_a_attr, class_b)
# class_a gets a multivalued attr named class_a_attr pointing to the join table.
# class_b gets a multivalued attr named class_a pointing back to the join table.
# Output class names are defined in CLASS_RENAMES.
JOIN_TABLES_TO_BIDIRECTIONAL_RELS: dict[str, tuple[str, str, str]] = {
    "aop_stressors":         ("aops",   "prototypical_stressors",   "stressors"),
    "aop_events":            ("aops",   "events",                   "events"),
    "aop_relationships":     ("aops",   "ke_relationships",         "relationships"),
    "assay_target_families": ("assays", "bio_target_families",      "biological_target_families"),
}

# Join tables that stay as top-level classes; only class_a gets a multivalued attr
# pointing to the join table. Used where class_b is a lookup or reference class.
# Format: join_table -> (class_a, class_a_attr, class_b)
# Output class names are defined in CLASS_RENAMES.
JOIN_TABLES_TO_UNIDIRECTIONAL_RELS: dict[str, tuple[str, str, str]] = {
    "aop_life_stages":           ("aops",          "life_stages",        "life_stage_terms"),
    "aop_sexes":                 ("aops",          "sexes",              "sex_terms"),
    "aop_taxons":                ("aops",          "taxons",             "taxon_terms"),
    "event_life_stages":         ("events",        "life_stages",        "life_stage_terms"),
    "event_sexes":               ("events",        "sexes",              "sex_terms"),
    "event_taxons":              ("events",        "taxons",             "taxon_terms"),
    "event_target_families":     ("events",        "bio_target_families","biological_target_families"),
    "relationship_taxons":       ("relationships", "taxons",             "taxon_terms"),
    "relationship_sexes":        ("relationships", "sexes",              "sex_terms"),
    "relationship_life_stages":  ("relationships", "life_stages",        "life_stage_terms"),
    "observation_citations":     ("observations",  "citations",          "citations"),
}

# Hand-curated FK and type ranges for class attributes.
# Attribute-level range: string is the default and is omitted from this dict.
# Only non-string, non-id ranges are listed (id is always set to integer by
# convert_class_block regardless).
CURATED_RANGES: dict[str, dict[str, str]] = {
    # aop_coaches and aop_contributors are BIDIRECTIONAL_INVERSE — classes removed from output.
    "aop_events": {
        "aop_id": "aops",
        "event_id": "events",
        "essentiality_id": "confidence_levels",
        "row_order": "integer",
        "sequence": "integer",
    },
    "aop_life_stages": {
        "aop_id": "aops",
        "life_stage_term_id": "life_stage_terms",
        "evidence_id": "confidence_levels",
    },
    "aop_logs": {
        "aop_id": "aops",
        "user_id": "users",
    },
    "aop_relationships": {
        "aop_id": "aops",
        "relationship_id": "relationships",
        "evidence_id": "confidence_levels",
        "quantitative_understanding_id": "confidence_levels",
        "row_order": "integer",
        "directness_id": "directnesses",
    },
    "aop_sexes": {
        "aop_id": "aops",
        "sex_term_id": "sex_terms",
        "evidence_id": "confidence_levels",
    },
    "aop_stressors": {
        "aop_id": "aops",
        "stressor_id": "stressors",
        "evidence_id": "confidence_levels",
    },
    "aop_taxons": {
        "aop_id": "aops",
        "taxon_term_id": "taxon_terms",
        "evidence_id": "confidence_levels",
    },
    "aops": {
        "corresponding_author_id": "users",
        "oecd_status_id": "oecd_statuses",
        "legacy": "integer",
        "assigned_license_id": "assigned_licenses",
        "handbook_id": "handbooks",
    },
    "assay_target_families": {
        "assay_id": "assays",
        "biological_target_family_id": "biological_target_families",
        "batch_import_id": "batch_imports",
    },
    "assays": {
        "reference_id": "citations",
        "taxon_term_id": "taxon_terms",
        "biological_action_id": "biological_actions",
    },
    "assigned_licenses": {
        "license_id": "licenses",
    },
    "batch_imports": {
        "contributor_id": "users",
        "citation_id": "citations",
    },
    "biological_target_families": {
        "batch_import_id": "batch_imports",
    },
    "chemical_synonyms": {
        "chemical_id": "chemicals",
    },
    "citation_biological_target_families": {
        "citation_id": "citations",
        "biological_target_family_id": "biological_target_families",
        "batch_import_id": "batch_imports",
    },
    "citation_relationships": {
        "citation_id": "citations",
        "relationship_id": "relationships",
    },
    "event_life_stages": {
        "event_id": "events",
        "life_stage_term_id": "life_stage_terms",
        "evidence_id": "confidence_levels",
    },
    "event_logs": {
        "event_id": "events",
        "user_id": "users",
    },
    "event_sexes": {
        "event_id": "events",
        "sex_term_id": "sex_terms",
        "evidence_id": "confidence_levels",
    },
    "event_target_families": {
        "event_id": "events",
        "biological_target_family_id": "biological_target_families",
        "batch_import_id": "batch_imports",
    },
    "event_taxons": {
        "event_id": "events",
        "taxon_term_id": "taxon_terms",
        "evidence_id": "confidence_levels",
    },
    "events": {
        "biological_organization_id": "biological_organizations",
        "organ_term_id": "organ_terms",
        "cell_term_id": "cell_terms",
    },
    "evidences": {
        "upstream_observation_id": "observations",
        "downstream_observation_id": "observations",
        "reference_id": "citations",
        "taxon_term_id": "taxon_terms",
        "sex_term_id": "sex_terms",
        "life_stage_term_id": "life_stage_terms",
        "relationship_id": "relationships",
    },
    "handbooks": {
        "version": "float",
    },
    "harmonized_aops": {
        "new_aop_id": "aops",
        "source_aop_id": "aops",
        "batch_import_id": "batch_imports",
    },
    "harmonized_events": {
        "source_event_id": "events",
        "harmonized_event_id": "events",
        "batch_import_id": "batch_imports",
    },
    "observation_citations": {
        "observation_id": "observations",
        "citation_id": "citations",
        "batch_import_id": "batch_imports",
    },
    "observations": {
        "biological_action_id": "biological_actions",
        "biological_process_id": "biological_processes",
        "biological_object_id": "biological_objects",
        "assay_id": "assays",
    },
    "oecd_statuses": {
        "sort": "integer",
    },
    "profiles": {
        "user_id": "users",
    },
    "relationship_life_stages": {
        "relationship_id": "relationships",
        "life_stage_term_id": "life_stage_terms",
        "evidence_id": "confidence_levels",
    },
    "relationship_logs": {
        "relationship_id": "relationships",
        "user_id": "users",
    },
    "relationship_sexes": {
        "relationship_id": "relationships",
        "sex_term_id": "sex_terms",
        "evidence_id": "confidence_levels",
    },
    "relationship_taxons": {
        "relationship_id": "relationships",
        "taxon_term_id": "taxon_terms",
        "evidence_id": "confidence_levels",
    },
    "relationships": {
        "upstream_event_id": "events",
        "downstream_event_id": "events",
    },
    "statuses": {
        "sort": "integer",
    },
    "stressor_chemicals": {
        "chemical_id": "chemicals",
        "stressor_id": "stressors",
    },
    "stressor_logs": {
        "stressor_id": "stressors",
        "user_id": "users",
    },
    "sub_events": {
        "biological_action_id": "biological_actions",
        "biological_object_id": "biological_objects",
        "biological_process_id": "biological_processes",
    }
}

# Classes that appear first in the output, in this order. All other classes follow alphabetically.
# Use SQL-based table names here (pre-CLASS_RENAMES, pre-PascalCase).
CLASS_ORDER = [
    "aops",
    "events",
    "relationships",
    "assays",
    "observations",
    "evidences",
    "stressors",
    "citations",
    "bio_target_families",
    "biological_actions",
    "biological_objects",
    "biological_processes",
    "biological_organizations",
    "batch_imports"
]

# All class name substitutions applied to headers and range: references in the output.
# Use SQL-based table names as keys and desired snake_case output names as values.
CLASS_RENAMES = {
    # Entity class renames
    "biological_target_families":           "bio_target_family",
    "events":                               "event",
    "relationships":                        "ke_relationship",
    "sub_events":                           "event_component",
    "biological_organizations":             "level_of_biological_organization",
    # Join table renames
    "aop_stressors":                        "aop_to_prototypical_stressor",
    "aop_events":                           "aop_to_event",
    "aop_relationships":                    "aop_to_ke_relationship",
    "assay_target_families":                "assay_to_bio_target_family",
    "aop_life_stages":                      "aop_to_life_stage",
    "aop_sexes":                            "aop_to_sex",
    "aop_taxons":                           "aop_to_taxon",
    "citation_biological_target_families":  "citation_to_bio_target_family",
    "event_life_stages":                    "event_to_life_stage",
    "event_sexes":                          "event_to_sex",
    "event_taxons":                         "event_to_taxon",
    "event_target_families":                "event_to_bio_target_family",
    "relationship_taxons":                  "ke_relationship_to_taxon",
    "relationship_sexes":                   "ke_relationship_to_sex",
    "relationship_life_stages":             "ke_relationship_to_life_stage",
    "observation_citations":                "observation_to_citation",
}
