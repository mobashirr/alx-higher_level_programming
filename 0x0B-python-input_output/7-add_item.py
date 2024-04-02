#!/usr/bin/python3

import sys
from os import path
import importlib


# Import the modules
module_name = "5-save_to_json_file"
module2_name = "6-load_from_json_file"
module = importlib.import_module(module_name)
module2 = importlib.import_module(module2_name)
filename = "add_item.json"

# Check if the file exists
if path.exists(filename):
    # Load existing items from file
    items = module2.load_from_json_file(filename)
else:
    items = []

# Add arguments to the list
items.extend(sys.argv[1:])

# Save the list to the file
module.save_to_json_file(items, filename)
