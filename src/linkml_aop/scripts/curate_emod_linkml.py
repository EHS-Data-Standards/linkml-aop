"""
Build a curated emod_linkml.yml from a raw schemauto-generated file that is generated
from the AOP-Wiki EMOD 3.0 MySQL database.

Usage:
    uv run python -m linkml_aop.scripts.curate_emod_linkml <sql_based_file> [<output_file>]

    sql_based_file  Raw output from `schemauto import-sql` (e.g. aop_emod_linkml.yml)
    output_file     Destination file (defaults to sql_based_file, i.e. in-place)

What this script does:
  1. Writes the SCHEMA_HEADER constant as the output header, replacing the raw
     header from sql_based_file.
  2. Removes admin/internal classes (WIKI_TABLES_TO_DROP) from the
     generated file in-place before processing.
  3. Handles join tables in three ways depending on their type:
       - PURE_PIVOT_UNIDIRECTIONAL: join table is removed from output as a class; the
         owner class gains a multivalued attribute pointing directly to the target class.
       - BIDIRECTIONAL_INVERSE: join table is removed from output; both referenced
         classes gain a multivalued attribute with inverse: pointing to each other.
       - SEMANTIC_JOIN_TABLES: join table stays as a top-level class (it carries
         extra semantic attributes); both referenced classes gain a multivalued
         attribute pointing to the join table class.
  4. For each remaining class:
       - CURATED_RANGES attribute-level range: references are grafted onto the
         generated attributes, then the slots pattern conversion is applied
         (shared slots → slots: list, id range → integer, bare range: string stripped).
  5. CLASS_RENAMES substitutions are applied to class headers and range: values
     throughout the output.
  6. Classes are written in CLASS_ORDER priority first, then alphabetically.
  7. All class names are converted to PascalCase in the output.
"""

import re
import sys
from pathlib import Path

from linkml_aop.curation.aop_definitions_and_enums import (
    biological_action_enum_list,
    biological_object_source_enum_list,
    biological_organization_enum_list,
    biological_process_source_enum_list,
    class_to_enum,
    confidence_levels_enum_list,
    directnesses_enum_list,
    event_definitions,
    life_stage_terms_enum_list,
    oecd_status_enum_list,
    sex_terms_enum_list,
    taxon_term_classes_enum_list,
)

def to_pascal_case(name: str) -> str:
    return "".join(word.capitalize() for word in name.split("_"))


def to_snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def singularize_word(word: str) -> str:
    """Return the singular form of a single English word (no underscores)."""
    if word.endswith("ies"):
        return word[:-3] + "y"
    if word.endswith("xes"):          # sexes → sex, boxes → box
        return word[:-2]
    if word.endswith("sses"):         # processes → process, directnesses → directness
        return word[:-2]
    if word.endswith("uses"):         # statuses → status
        return word[:-2]
    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def to_singular(name: str) -> str:
    """Singularize the last underscore-separated segment of a snake_case name.

    Examples: bio_target_families → bio_target_family, aops → aop,
    oecd_statuses → oecd_status, directnesses → directness.
    Enum names (ending in _enum) are left unchanged since 'enum' has no trailing 's'.
    """
    if "_" in name:
        prefix, last = name.rsplit("_", 1)
        return f"{prefix}_{singularize_word(last)}"
    return singularize_word(name)


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
]

# Classes that appear first in the output, in this order. All other classes follow alphabetically.
# Use final output names (i.e. post-CLASS_RENAMES) here.
CLASS_ORDER = [
    "aops",
    "events",
    "relationships",
    "stressors",
    "bio_target_families",
    "observations",
    "citations",
]

# Class name substitutions applied to headers and range: references in the output.
# Also governs attribute names wherever the old class name appears as an attr name.
CLASS_RENAMES = {
    "biological_target_families":           "bio_target_families",
    "assay_target_families":                "assay_bio_target_families",
    "citation_biological_target_families":  "citation_bio_target_families",
    "event_target_families":                "event_bio_target_families",
    "sub_events":                           "event_components",
}


# Attributes to drop from specific classes. Keys are sql-based class names.
DROPPED_ATTRS: dict[str, list[str]] = {
    "aops": ["status_id"],
}


# Join tables that collapse to a unidirectional multivalued reference on the owner.
# Format: join_table -> (owner_class, attr_name, target_range)
PURE_PIVOT_UNIDIRECTIONAL: dict[str, tuple[str, str, str]] = {
    "assay_objects": ("assays", "objects", "biological_objects"),
    "assay_processes": ("assays", "processes", "biological_processes"),
    "assay_taxon_terms": ("assays", "taxon_terms", "taxon_terms"),
    "aop_url_links": ("aops", "url_links", "url_links"),
    "event_sub_events": ("events", "event_components", "sub_events")
}

# Join tables that collapse to bidirectional inverse multivalued refs.
# Format: join_table -> (owner_class, owner_attr, inverse_class, inverse_attr)
BIDIRECTIONAL_INVERSE: dict[str, tuple[str, str, str, str]] = {
    "aop_coaches": ("aops", "coaches", "users", "coached_aops"),
    "aop_contributors": ("aops", "contributors", "users", "contributed_aops"),
    "event_assays": ("events", "assays", "assays", "events"),
    "observation_events": ("observations", "events", "events", "observations"),
}

# Join tables with extra semantic attributes: stay as top-level classes; both referenced
# classes get a multivalued attr pointing to the join table.
# Format: join_table -> (class_a, class_a_attr, class_b, class_b_attr)
# Where the attr name may strip the owner prefix for readability (e.g. event_life_stages
# becomes life_stages on events), while the range always points to the join table class.
SEMANTIC_JOIN_TABLES: dict[str, tuple[str, str, str, str]] = {
    # Format: join_table -> (class_a, class_a_attr, class_b, class_b_attr)
    # class_a_attr: strip the owner prefix from the join table name
    # class_b_attr: use the owner (class_a) name
    "aop_life_stages":                     ("aops",         "life_stages",               "life_stage_terms",          "aops"),
    "aop_sexes":                           ("aops",         "sexes",                     "sex_terms",                 "aops"),
    "aop_taxons":                          ("aops",         "taxons",                    "taxon_terms",               "aops"),
    "aop_stressors":                       ("aops",         "prototypical_stressor",     "stressors",                 "aops"),
    "aop_events":                          ("aops",         "events",                    "events",                    "aops"),
    "aop_relationships":                   ("aops",         "relationships",             "relationships",             "aops"),
    "event_life_stages":                   ("events",       "life_stages",               "life_stage_terms",          "events"),
    "event_sexes":                         ("events",       "sexes",                     "sex_terms",                 "events"),
    "event_target_families":               ("events",       "bio_target_families",       "biological_target_families","events"),
    "event_taxons":                        ("events",       "taxons",                    "taxon_terms",               "events"),
    "assay_target_families":               ("assays",       "bio_target_families",       "biological_target_families","assays"),
    "citation_biological_target_families": ("citations",    "bio_target_families",       "biological_target_families","citations"),
    "observation_citations":               ("observations", "citations",                 "citations",                 "observations"),
    "relationship_taxons":                 ("relationships","taxons",                    "taxon_terms",               "relationships"),
    "relationship_sexes":                  ("relationships","sexes",                     "sex_terms",                 "relationships"),
    "relationship_life_stages":            ("relationships","life_stages",               "life_stage_terms",          "relationships"),
}

# Schema header written verbatim at the top of the output file.
# Sourced from aop_wiki_linkml.yml; inlined here to make the script self-contained.
SCHEMA_HEADER = """\
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

# Merge enum ranges from inputs/aop_definitions_and_enums.py into CURATED_RANGES.
# class_to_enum maps PascalCase class name -> (attr, PascalCaseEnumName).
# Both are converted to snake_case for lookup; apply_pascal_case_to_classes handles output.
for _pascal_class, (_attr, _pascal_enum) in class_to_enum.items():
    CURATED_RANGES.setdefault(to_snake_case(_pascal_class), {})[_attr] = to_snake_case(_pascal_enum)

# Attribute descriptions keyed by sql-based class name -> attr name -> description string.
DESCRIPTIONS: dict[str, dict[str, str]] = {
    "events": event_definitions,
}

# Enum definitions used to generate the enums: section of the output YAML.
# Keys are snake_case enum names (converted to PascalCase in output).
# Values are either a list (no descriptions) or a dict {value: description}.
ENUM_DEFINITIONS: dict[str, list | dict] = {
    "biological_action_enum":        biological_action_enum_list,
    "biological_organization_enum":  biological_organization_enum_list,
    "biological_object_source_enum": biological_object_source_enum_list,
    "biological_process_source_enum":biological_process_source_enum_list,
    "sex_terms_enum":                sex_terms_enum_list,
    "life_stage_terms_enum":         life_stage_terms_enum_list,
    "taxon_term_classes_enum":       taxon_term_classes_enum_list,
    "confidence_levels_enum":        confidence_levels_enum_list,
    "directnesses_enum":             directnesses_enum_list,
    "oecd_status_enum":              oecd_status_enum_list,
}


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def extract_class_names(text: str) -> set[str]:
    """Return all class names defined under the top-level 'classes:' section."""
    in_classes = False
    names: set[str] = set()
    for line in text.splitlines():
        if line.startswith("classes:"):
            in_classes = True
            continue
        if in_classes:
            if line and not line[0].isspace() and not line.startswith("#"):
                break
            m = re.match(r"^  ([a-z][a-z_0-9]*):\s*$", line)
            if m:
                names.add(m.group(1))
    return names


def extract_class_blocks(text: str, class_names: set[str]) -> dict[str, list[str]]:
    """Return the raw lines for each named class from the 'classes:' section.

    Each value is the list of lines from the class header down to (but not
    including) the next class header or end of section.
    """
    blocks: dict[str, list[str]] = {}
    lines = text.splitlines(keepends=True)

    in_classes = False
    current_name: str | None = None
    current_lines: list[str] = []

    def flush():
        if current_name and current_name in class_names:
            blocks[current_name] = current_lines[:]

    for line in lines:
        if line.startswith("classes:"):
            in_classes = True
            continue
        if in_classes:
            if line and not line[0].isspace() and not line.startswith("#"):
                flush()
                break
            m = re.match(r"^  ([a-z][a-z_0-9]*):\s*$", line)
            if m:
                flush()
                current_name = m.group(1)
                current_lines = [line]
            elif current_name is not None:
                current_lines.append(line)

    flush()
    return blocks


def remove_admin_classes(text: str, class_names: set[str]) -> tuple[str, list[str]]:
    """Remove named class blocks from the 'classes:' section of a YAML text.

    Returns (updated_text, removed_names).
    """
    lines = text.splitlines(keepends=True)
    result: list[str] = []
    removed: list[str] = []
    in_classes = False
    skip_current = False

    for line in lines:
        if line.startswith("classes:"):
            in_classes = True
            result.append(line)
            continue
        if in_classes:
            m = re.match(r"^  ([a-z][a-z_0-9]*):\s*$", line)
            if m:
                skip_current = m.group(1) in class_names
                if skip_current:
                    removed.append(m.group(1))
            elif not line[0:1].isspace() and line.strip() and not line.startswith("#"):
                in_classes = False
                skip_current = False
        if not skip_current:
            result.append(line)

    return "".join(result), removed


# ---------------------------------------------------------------------------
# Conversion
# ---------------------------------------------------------------------------

def apply_class_renames(lines: list[str], renames: dict[str, str]) -> list[str]:
    """Apply class name substitutions to a block of YAML lines.

    Replaces class header lines (2-space indent) and range: values.
    """
    result = []
    for line in lines:
        for old, new in renames.items():
            line = re.sub(rf'^(  ){re.escape(old)}(:\s*)$', rf'\g<1>{new}\g<2>', line)
            line = re.sub(rf'^( +range: ){re.escape(old)}(\s*)$', rf'\g<1>{new}\g<2>', line)
        result.append(line)
    return result


def apply_pascal_case_to_classes(text: str) -> str:
    """Convert class names to PascalCase in the classes: section only.

    Applies to class header lines (2-space indent) and range: values,
    skipping LinkML built-in scalar types.
    """
    marker = "\nclasses:\n"
    idx = text.find(marker)
    if idx == -1:
        return text
    header = text[:idx + len(marker)]
    body = text[idx + len(marker):]

    body = re.sub(
        r'^(  )([a-z][a-z_0-9]*)(:\s*)$',
        lambda m: m.group(1) + to_pascal_case(to_singular(m.group(2))) + m.group(3),
        body,
        flags=re.MULTILINE,
    )
    body = re.sub(
        r'^( +range: )([a-z][a-z_0-9]*)(\s*)$',
        lambda m: (
            m.group(1) + to_pascal_case(to_singular(m.group(2))) + m.group(3)
            if m.group(2) not in LINKML_BUILTIN_TYPES
            else m.group(0)
        ),
        body,
        flags=re.MULTILINE,
    )
    return header + body


def make_multivalued_attr_lines(
    attr_name: str, range_name: str, inverse: str | None = None
) -> list[str]:
    """Return attribute lines for a multivalued reference, optionally with inverse:."""
    lines = [
        f"      {attr_name}:\n",
        f"        multivalued: true\n",
        f"        range: {range_name}\n",
    ]
    if inverse:
        lines.append(f"        inverse: {inverse}\n")
    return lines


def convert_class_block(
    lines: list[str],
    curated_ranges: dict[str, str],
    dropped_attrs: list[str] | None = None,
    descriptions: dict[str, str] | None = None,
) -> list[str]:
    """Convert a schemauto-generated class block to the hand-curated style.

    Pass 1 — processes each attribute:
      - dropped_attrs fields are removed entirely
      - SHARED_SLOTS fields are removed from attributes: and recorded for
        the slots: list
      - id range is normalised to integer
      - range: string is stripped (covered by default_range: string)
      - curated_ranges values are applied where available, overriding any
        generated range: string for that attribute
      - descriptions values are injected as description: lines

    Pass 2 — inserts the slots: block immediately before attributes:.
    """
    dropped_attrs = dropped_attrs or []
    descriptions = descriptions or {}
    found_slots: list[str] = []
    result: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]

        attr_match = re.match(r"^      ([a-z][a-z_0-9]*):\s*$", line)
        if attr_match:
            attr_name = attr_match.group(1)

            # Collect sub-lines for this attribute (8-space indent)
            attr_block = [line]
            j = i + 1
            while j < len(lines) and re.match(r"^        ", lines[j]):
                attr_block.append(lines[j])
                j += 1

            if attr_name in dropped_attrs:
                i = j
                continue

            if attr_name in SHARED_SLOTS:
                found_slots.append(attr_name)
                i = j
                continue

            if attr_name == "id":
                new_block = []
                has_range = False
                for al in attr_block:
                    if re.match(r"^        range:\s+\S+\s*$", al):
                        new_block.append("        range: integer\n")
                        has_range = True
                    else:
                        new_block.append(al)
                if not has_range:
                    new_block.append("        range: integer\n")
                result.extend(new_block)
                i = j
                continue

            # Apply curated range if available, otherwise strip range: string
            curated = curated_ranges.get(attr_name)
            new_block = []
            replaced = False
            for al in attr_block:
                if re.match(r"^        range:\s+\S+\s*$", al):
                    if curated:
                        new_block.append(f"        range: {curated}\n")
                        replaced = True
                    # else: drop range: string (it's the default)
                else:
                    new_block.append(al)
            if curated and not replaced:
                new_block.append(f"        range: {curated}\n")
            desc = descriptions.get(attr_name)
            if desc and not any("description:" in al for al in new_block):
                new_block.insert(1, f"        description: {desc}\n")
            result.extend(new_block)
            i = j
            continue

        result.append(line)
        i += 1

    # Pass 2: insert slots: block before attributes:
    if not found_slots:
        return result

    slots_block = ["    slots:\n"] + [f"      - {s}\n" for s in sorted(found_slots)]
    final: list[str] = []
    for line in result:
        if line.strip() == "attributes:":
            final.extend(slots_block)
        final.append(line)
    return final


def build_enums_yaml(enum_definitions: dict) -> str:
    """Generate the enums: YAML section from ENUM_DEFINITIONS."""
    lines = ["\nenums:\n"]
    for snake_name, values in enum_definitions.items():
        lines.append(f"  {to_pascal_case(snake_name)}:\n")
        lines.append("    permissible_values:\n")
        if isinstance(values, dict):
            for k, v in values.items():
                lines.append(f"      {k}:\n")
                lines.append(f"        description: {v}\n")
        else:
            for v in values:
                lines.append(f"      {v}:\n")
    return "".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    sql_based_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else sql_based_path

    if not sql_based_path.exists():
        print(f"ERROR: file not found: {sql_based_path}")
        sys.exit(1)

    sql_based_text = sql_based_path.read_text()

    admin_classes = set(WIKI_TABLES_TO_DROP)

    # Remove admin classes from the sql-based file in-place
    sql_based_text, removed = remove_admin_classes(sql_based_text, admin_classes)
    if removed:
        sql_based_path.write_text(sql_based_text)
        print(f"Removed admin classes from {sql_based_path}: {sorted(removed)}")

    sql_based_classes = extract_class_names(sql_based_text)

    join_tables_present = sql_based_classes & (
        set(PURE_PIVOT_UNIDIRECTIONAL) | set(BIDIRECTIONAL_INVERSE) | set(SEMANTIC_JOIN_TABLES)
    )
    nested_join_tables = (
        (sql_based_classes & set(PURE_PIVOT_UNIDIRECTIONAL))
        | (sql_based_classes & set(BIDIRECTIONAL_INVERSE))
    )
    semantic_join_tables_present = sql_based_classes & set(SEMANTIC_JOIN_TABLES)

    print(f"Active classes: {len(sql_based_classes - nested_join_tables)}")
    print(f"Join tables identified ({len(join_tables_present)}): {sorted(join_tables_present)}")
    print(f"Join tables nested ({len(nested_join_tables)}): {sorted(nested_join_tables)}")
    print(f"Join tables with extra attrs — refs added to both owners ({len(semantic_join_tables_present)}): {sorted(semantic_join_tables_present)}")

    sql_based_blocks = extract_class_blocks(sql_based_text, sql_based_classes)

    # Build extra multivalued attrs to inject into owner class blocks
    extra_attrs: dict[str, list[str]] = {}
    for jt, (owner, attr_name, target_range) in PURE_PIVOT_UNIDIRECTIONAL.items():
        if jt in sql_based_classes:
            extra_attrs.setdefault(owner, []).extend(
                make_multivalued_attr_lines(attr_name, target_range)
            )
    for jt, (owner, owner_attr, inv_class, inv_attr) in BIDIRECTIONAL_INVERSE.items():
        if jt in sql_based_classes:
            extra_attrs.setdefault(owner, []).extend(
                make_multivalued_attr_lines(owner_attr, inv_class, inverse=inv_attr)
            )
            extra_attrs.setdefault(inv_class, []).extend(
                make_multivalued_attr_lines(inv_attr, owner, inverse=owner_attr)
            )
    for jt, (class_a, class_a_attr, class_b, class_b_attr) in SEMANTIC_JOIN_TABLES.items():
        if jt in sql_based_classes:
            extra_attrs.setdefault(class_a, []).extend(
                make_multivalued_attr_lines(class_a_attr, jt)
            )
            extra_attrs.setdefault(class_b, []).extend(
                make_multivalued_attr_lines(class_b_attr, jt)
            )

    # Build output: schema header + classes: + converted class blocks
    lines = [SCHEMA_HEADER, "classes:\n"]

    # CLASS_ORDER uses output names; resolve back to sql-based names for lookup.
    reverse_renames = {v: k for k, v in CLASS_RENAMES.items()}
    active_classes = sql_based_classes - nested_join_tables
    priority = [
        reverse_renames.get(n, n)
        for n in CLASS_ORDER
        if reverse_renames.get(n, n) in active_classes
    ]
    remaining = sorted(active_classes - set(priority))

    for name in priority + remaining:
        raw_lines = sql_based_blocks.get(name)
        if raw_lines is None:
            continue
        curated_ranges = CURATED_RANGES.get(name, {})
        converted = convert_class_block(
            raw_lines, curated_ranges, DROPPED_ATTRS.get(name), DESCRIPTIONS.get(name)
        )
        converted = apply_class_renames(converted, CLASS_RENAMES)
        if name in extra_attrs:
            converted.extend(apply_class_renames(extra_attrs[name], CLASS_RENAMES))
        lines.append("".join(converted))

    output = apply_pascal_case_to_classes("".join(lines))
    output += build_enums_yaml(ENUM_DEFINITIONS)
    output_path.write_text(output)
    print(f"Written to {output_path}")


if __name__ == "__main__":
    main()
