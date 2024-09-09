import pprint
from pathlib import Path

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

# from ..mixs_missing_value_sandbox import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "mixs_missing_value_sandbox" / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "mixs_missing_value_sandbox.yaml"

schema_view = SchemaView(MAIN_SCHEMA_PATH)

current_checklist = "Mims"
current_extension = "Soil"

combination_class_name = f"{current_checklist}{current_extension}"

combination_class = schema_view.induced_class(combination_class_name)

combination_class_attributes = combination_class.attributes

for ak, av in combination_class_attributes.items():
    if av.required:
        print(f"Slot {ak} is required in {combination_class_name}")
        print(f"{av.range}")
        if av.structured_pattern:
            print(f"{av.structured_pattern.syntax}")
        if av.pattern:
            print(f"{av.pattern}")
        print("----")
