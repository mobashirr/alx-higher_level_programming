#!/usr/bin/python3

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the file exists
if path.exists(filename):
    # Load existing items from file
    items = load_from_json_file(filename)
else:
    items = []

# Add arguments to the list
items.extend(sys.argv[1:])

# Save the list to the file
save_to_json_file(items, filename)
