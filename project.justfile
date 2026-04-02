## Add your own just recipes here. This is imported by the main justfile.

# Curate the EMOD LinkML schema from a raw schemauto SQL-based input file.
# Runs via the venv Python directly to avoid uv rebuild on schema file changes.
# Usage: just curate [input] [output]
curate input="inputs/aop_wiki_emod_3_0_4-2-26.yml" output="src/linkml_aop/schema/aop_emod_linkml.yaml":
    .venv/bin/python -m linkml_aop.scripts.curate_emod_linkml {{input}} {{output}}
