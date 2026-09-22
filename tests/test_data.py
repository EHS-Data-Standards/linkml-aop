"""Load the example data through the generated datamodel.

Each file in src/data/examples/valid is named <Class>-<n>.yaml and must load as
that class; each file in src/data/examples/invalid must not. This is the same
convention linkml-run-examples uses in `just test`, checked here against the
Python datamodel rather than the schema.
"""
import glob
import os

import pytest
from linkml_runtime.loaders import yaml_loader

from linkml_aop import datamodel

ROOT = os.path.join(os.path.dirname(__file__), "..")
EXAMPLES_DIR = os.path.join(ROOT, "src", "data", "examples")
VALID_FILES = sorted(glob.glob(os.path.join(EXAMPLES_DIR, "valid", "*.yaml")))
INVALID_FILES = sorted(glob.glob(os.path.join(EXAMPLES_DIR, "invalid", "*.yaml")))


def target_class(path: str):
    """Resolve the datamodel class named by an example file's <Class>-<n>.yaml stem."""
    class_name = os.path.basename(path).rsplit(".", 1)[0].split("-", 1)[0]
    cls = getattr(datamodel, class_name, None)
    assert cls is not None, (
        f"{os.path.basename(path)}: no class named {class_name!r} in the datamodel; "
        "example files must be named <Class>-<n>.yaml"
    )
    return cls


def test_examples_exist():
    assert VALID_FILES, "no valid example files found"
    assert INVALID_FILES, "no invalid example files found"


@pytest.mark.parametrize("path", VALID_FILES, ids=os.path.basename)
def test_valid_example_loads(path):
    obj = yaml_loader.load(path, target_class=target_class(path))
    assert obj is not None
    assert obj.id is not None


@pytest.mark.parametrize("path", INVALID_FILES, ids=os.path.basename)
def test_invalid_example_is_rejected(path):
    # Resolve the class first so that only a loader rejection can satisfy the raise.
    cls = target_class(path)
    with pytest.raises((ValueError, TypeError)):
        yaml_loader.load(path, target_class=cls)
