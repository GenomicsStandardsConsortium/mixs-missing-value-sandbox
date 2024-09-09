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

checklist_slots = schema_view.get_class(current_checklist).slots

extension_slots = schema_view.get_class(current_extension).slots

checklist_extension_slots = set(checklist_slots).intersection(set(extension_slots))
checklist_extension_slots = list(checklist_extension_slots)
checklist_extension_slots.sort()

checklist_usages = schema_view.get_class(current_checklist).slot_usage
extension_usages = schema_view.get_class(current_extension).slot_usage
for slot in checklist_extension_slots:
    global_definition = schema_view.get_slot(slot)
    checklist_modifies = slot in checklist_usages
    extension_modifies = slot in extension_usages
    if checklist_modifies or extension_modifies:
        if checklist_modifies:
            print(f"{slot} slot's usage in {current_checklist}:")
            print(yaml_dumper.dumps(checklist_usages[slot]))
        else:
            print(f"{current_checklist} uses the global definition for {slot}")
            # print(yaml_dumper.dumps(global_definition))
        if extension_modifies:
            print(f"{slot} slot's usage in {current_extension}:")
            print(yaml_dumper.dumps(extension_usages[slot]))
        else:
            print(f"{current_extension} uses the global definition for {slot}")
            # print(yaml_dumper.dumps(global_definition))
        print(f"Induced slot {slot} in {current_checklist}{current_extension}\n")
        print(yaml_dumper.dumps(schema_view.induced_slot(slot, f"{current_checklist}{current_extension}")))
    else:
        print(f"{slot} not modified by {current_checklist} or {current_extension}\n")
        print("----")
