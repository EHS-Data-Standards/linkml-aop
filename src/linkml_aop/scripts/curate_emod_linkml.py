"""
Build a curated emod_linkml.yml from a raw schemauto-generated file that is generated
from the AOP-Wiki EMOD 3.0 MySQL database.

Usage:
    uv run python -m linkml_aop.scripts.curate_emod_linkml <sql_based_file> <output_file>

    sql_based_file  Raw output from `schemauto import-sql` (e.g. aop_emod_linkml.yml)
    output_file     Destination file for the curated schema

What this script does:
  1. Writes the SCHEMA_HEADER constant as the output header, replacing the raw
     header from sql_based_file.
  2. Removes wiki-specific tables (WIKI_TABLES_TO_DROP) from the input before processing.
  3. Handles join tables in four ways depending on their type:
       - PURE_PIVOT_UNIDIRECTIONAL: join table is removed from output as a class; the
         parent class gains a multivalued attribute pointing directly to the target class.
       - BIDIRECTIONAL_INVERSE: join table is removed from output; both referenced
         classes gain a multivalued attribute pointing to each other.
       - JOIN_TABLES_TO_BIDIRECTIONAL_RELS: join table stays as a top-level class;
         both referenced classes gain a multivalued attribute pointing to the join table.
       - JOIN_TABLES_TO_UNIDIRECTIONAL_RELS: join table stays as a top-level class;
         only class_a gains a multivalued attribute pointing to the join table.
  4. For each remaining class:
       - CURATED_RANGES attribute-level range: references are grafted onto the
         generated attributes, then the slots pattern conversion is applied
         (shared slots → slots: list, id range → integer, bare range: string stripped).
  5. CLASS_RENAMES substitutions are applied to class headers and range: values
     throughout the output. All rename definitions live in CLASS_RENAMES as the
     single source of truth.
  6. Classes are written in CLASS_ORDER priority first, then alphabetically.
  7. All class names are converted to PascalCase in the output.
"""

import re
import sys
from pathlib import Path

from linkml_aop.curation_helpers.aop_definitions_and_enums import (
    ATTRIBUTE_DESCRIPTIONS,
    ENUM_DEFINITIONS,
    CLASS_DESCRIPTIONS,
    CLASS_TO_ENUM,
)
from linkml_aop.curation_helpers.sql_to_linkml_helpers import *

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


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def extract_class_names_from_input_schema(text: str) -> set[str]:
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


def remove_wiki_classes(text: str, class_names: set[str]) -> tuple[str, list[str]]:
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

# Merge enum ranges from curation_helpers/aop_definitions_and_enums.py into CURATED_RANGES.
# CLASS_TO_ENUM maps PascalCase class name -> (attr, PascalCaseEnumName).
# Both are converted to snake_case for lookup; apply_pascal_case_to_classes handles output.
for _pascal_class, (_attr, _pascal_enum) in CLASS_TO_ENUM.items():
    CURATED_RANGES.setdefault(to_snake_case(_pascal_class), {})[_attr] = to_snake_case(_pascal_enum)
    
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
    attr_name: str, range_name: str
) -> list[str]:
    """Return attribute lines for a multivalued reference.

    Note: inverse: is intentionally omitted. Class-level attributes cannot be referenced
    by inverse: in LinkML (only top-level slots can); including it causes schema validation
    errors in linkml-run-examples.
    """
    return [
        f"      {attr_name}:\n",
        f"        multivalued: true\n",
        f"        range: {range_name}\n",
    ]


def convert_class_block(
    lines: list[str],
    curated_ranges: dict[str, str],
    dropped_attrs: list[str] | None = None,
    descriptions: dict[str, str] | None = None,
    class_description: str | None = None,
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

    # Inject class-level description after the class header line (first line).
    if class_description and lines:
        result: list[str] = [lines[0], f"    description: >-\n      {class_description}\n"]
        i = 1
    else:
        result = []
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
# Pipeline steps
# ---------------------------------------------------------------------------

def report_class_breakdown(
    sql_based_classes: set[str],
    removed: set[str],
    pure_pivot: dict,
    bidirectional_inv: dict,
    bidir_rels: dict,
    unidir_rels: dict,
) -> None:
    """Print a breakdown of all input classes by how they are handled in the output."""
    all_join_tables = set(pure_pivot) | set(bidirectional_inv) | set(bidir_rels) | set(unidir_rels)
    entity_classes  = sql_based_classes - all_join_tables

    if removed:
        print(f"Tables from Wiki that are being skipped/removed:")
        for table in sorted(removed):
            print(f"  {table}")
        print("")

    print(f"Input classes: {len(sql_based_classes)}")
    print(f"  Entity classes — written as top-level classes ({len(entity_classes)}):")
    for c in sorted(entity_classes):
        print(f"    {c}")
    print("")

    print(f"  Bidirectional rel join tables — top-level + refs on both parent classes ({len(bidir_rels)}):")
    for jt in sorted(bidir_rels):
        print(f"    {jt}")
    print("")

    print(f"  Unidirectional rel join tables — top-level + ref on parent only ({len(unidir_rels)}):")
    for jt in sorted(unidir_rels):
        print(f"    {jt}")
    print("")

    print(f"  Pure pivot join tables — collapsed as attributes on parent class ({len(pure_pivot)}):")
    for jt in sorted(pure_pivot):
        print(f"    {jt}")
    print("")

    print(f"  Bidirectional inverse join tables — collapsed into both parent classes as attributes ({len(bidirectional_inv)}):")
    for jt in sorted(bidirectional_inv):
        print(f"    {jt}")
    print("")


def build_extra_attrs(
    pure_pivot: dict,
    bidirectional_inv: dict,
    bidir_rels: dict,
    unidir_rels: dict,
) -> dict[str, list[str]]:
    """Build extra multivalued attrs to inject into parent class blocks from all join table types."""
    extra_attrs: dict[str, list[str]] = {}
    for jt, (parent, attr_name, target_range) in pure_pivot.items():
        extra_attrs.setdefault(parent, []).extend(
            make_multivalued_attr_lines(attr_name, target_range)
        )
    for jt, (parent, parent_attr, inv_class, inv_attr) in bidirectional_inv.items():
        extra_attrs.setdefault(parent, []).extend(
            make_multivalued_attr_lines(parent_attr, inv_class)
        )
        extra_attrs.setdefault(inv_class, []).extend(
            make_multivalued_attr_lines(inv_attr, parent)
        )
    for jt, (class_a, class_a_attr, class_b) in bidir_rels.items():
        extra_attrs.setdefault(class_a, []).extend(
            make_multivalued_attr_lines(class_a_attr, jt)
        )
        extra_attrs.setdefault(class_b, []).extend(
            make_multivalued_attr_lines(class_a, jt)
        )
    for jt, (class_a, class_a_attr, class_b) in unidir_rels.items():
        extra_attrs.setdefault(class_a, []).extend(
            make_multivalued_attr_lines(class_a_attr, jt)
        )
    return extra_attrs


def resolve_class_order(sql_based_classes: set[str], nested_join_tables: set[str]) -> list[str]:
    """
    Return active classes (SQL-based names) in CLASS_ORDER priority first, then alphabetically.
    TODO: move all classes based on join tables to the end of the ordering
    """
    active_classes = sql_based_classes - nested_join_tables
    priority = [n for n in CLASS_ORDER if n in active_classes]
    return priority + sorted(active_classes - set(priority))


def build_classes_yaml(
    ordered_classes: list[str],
    sql_based_blocks: dict[str, list[str]],
    extra_attrs: dict[str, list[str]],
) -> str:
    """Convert and assemble all class blocks into the classes: YAML body string.

    All dicts are keyed by SQL-based names. CLASS_RENAMES is applied here as the single rename step.
    """
    lines = []
    for sql_name in ordered_classes:
        raw_lines = sql_based_blocks.get(sql_name)
        if raw_lines is None:
            continue
        converted = convert_class_block(
            raw_lines, CURATED_RANGES.get(sql_name, {}), DROPPED_ATTRS.get(sql_name),
            ATTRIBUTE_DESCRIPTIONS.get(sql_name), CLASS_DESCRIPTIONS.get(sql_name),
        )
        converted = apply_class_renames(converted, CLASS_RENAMES)
        if sql_name in extra_attrs:
            converted.extend(apply_class_renames(extra_attrs[sql_name], CLASS_RENAMES))
        lines.append("".join(converted))
    return "".join(lines)


def filter_join_groupings(join_groupings: dict[str, tuple], sql_based_classes: set[str]) -> dict[str, tuple]:
    """Filter join table groupings to only those present in the input schema."""
    return {k: v for k, v in join_groupings.items() if k in sql_based_classes}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2]) 
    else:
        print(f"ERROR: No output path specified")
        sys.exit(1)

    sql_based_path = Path(sys.argv[1])
    if not sql_based_path.exists():
        print(f"ERROR: file not found: {sql_based_path}")
        sys.exit(1)

    sql_based_linkml = sql_based_path.read_text()

    # Strip wiki-specific classes from the in-memory text before processing.
    sql_based_linkml, removed = remove_wiki_classes(sql_based_linkml, set(WIKI_TABLES_TO_DROP))
    sql_based_classes = extract_class_names_from_input_schema(sql_based_linkml)

    # Filter all join table dicts to only those present in the input schema.
    pure_pivot    = filter_join_groupings(PURE_PIVOT_UNIDIRECTIONAL, sql_based_classes)
    bidir_inv     = filter_join_groupings(BIDIRECTIONAL_INVERSE, sql_based_classes)
    bidir_rels    = filter_join_groupings(JOIN_TABLES_TO_BIDIRECTIONAL_RELS, sql_based_classes)
    unidir_rels   = filter_join_groupings(JOIN_TABLES_TO_UNIDIRECTIONAL_RELS, sql_based_classes)
    collapsed_join_tables = set(pure_pivot) | set(bidir_inv)

    report_class_breakdown(sql_based_classes, removed, pure_pivot, bidir_inv, bidir_rels, unidir_rels)

    sql_based_blocks = extract_class_blocks(sql_based_linkml, sql_based_classes)
    extra_attrs = build_extra_attrs(pure_pivot, bidir_inv, bidir_rels, unidir_rels)
    ordered_classes = resolve_class_order(sql_based_classes, collapsed_join_tables)
    classes_yaml = build_classes_yaml(ordered_classes, sql_based_blocks, extra_attrs)

    output = apply_pascal_case_to_classes(SCHEMA_HEADER + "classes:\n" + classes_yaml)
    output += build_enums_yaml(ENUM_DEFINITIONS)
    output_path.write_text(output)
    print(f"Written to {output_path}")


if __name__ == "__main__":
    main()
