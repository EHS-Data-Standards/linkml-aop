## Add your own just recipes here. This is imported by the main justfile.

# Curate the EMOD LinkML schema from a raw schemauto SQL-based input file.
# Runs via the venv Python directly to avoid uv rebuild on schema file changes.
# Usage: just curate [date] [output]
# date format: MM-DD-YYYY (e.g. 04-02-2026)
curate date="04-02-2026" output="src/linkml_aop/schema/aop_emod_linkml.yaml":
    .venv/bin/python -m linkml_aop.scripts.curate_emod_linkml inputs/schemauto_generated_emod_linkml_{{date}}.yml {{output}}
