# linkml-aop

A LinkML schema for Adverse Outcome Pathways, with EMOD - Evidence Model - expansions.

## Website

*Coming soon...*

## Repository Structure

* [examples/](examples/) - example data
* [inputs/](inputs/) - raw input files (e.g. schemauto-generated YAML)
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [linkml_aop](src/linkml_aop)
    * [schema](src/linkml_aop/schema) -- LinkML schemas
    * [datamodel](src/linkml_aop/datamodel) -- generated Python datamodel
    * [scripts](src/linkml_aop/scripts) -- curation and utility scripts
    * [curation](src/linkml_aop/curation) -- domain constants, definitions, and enums used by scripts
* [tests/](tests/) - Python tests

## Curation Workflow

The `schemauto` generated schema, `inputs/emod_3-26-26_linkml.yml`, is based on the AOP-Wiki EMOD 3.0
application MySQL DB schema that is under development for prototyping purposes. It serves as the basis for
the `src/linkml_aop/schema/aop_emod_linkml.yaml`, that was generated from the `schemauto` file by applying
the transformations in `src/linkml_aop/scripts/curate_emod_linkml.py`.

To add or revise schema definitions and enumerations:

*Optional first step* - generate a new EMOD input schema by pointing to the EMOD 3.0 MySQL instance (permissions needed)

1. Edit [`src/linkml_aop/curation/aop_definitions_and_enums.py`](src/linkml_aop/curation/aop_definitions_and_enums.py) with
  new or updated definitions/enums.
2. Run the curation script to regenerate the schema:

   ```bash
   uv run python -m linkml_aop.scripts.curate_emod_linkml inputs/<input_file>.yml src/linkml_aop/schema/aop_emod_linkml.yaml
   ```

3. Review the changes in [`src/linkml_aop/schema/aop_emod_linkml.yaml`](src/linkml_aop/schema/aop_emod_linkml.yaml).

## Developer Documentation

<details>
<summary>Commands</summary>

This LinkML project uses the command runner [just](https://github.com/casey/just/) which is a better choice than `make` on Windows.
To generate project artefacts, run:

* `just --list`: list all pre-defined tasks
* `just all`: make everything
* `just deploy`: deploys site

</details>

## Credits

This project was started from:
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
****