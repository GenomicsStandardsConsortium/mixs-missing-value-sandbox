from pathlib import Path
from .mixs_missing_value_sandbox import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "mixs_missing_value_sandbox.yaml"
