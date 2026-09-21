from pathlib import Path
from .aop_emod_linkml import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "aop_emod_linkml.yaml"
