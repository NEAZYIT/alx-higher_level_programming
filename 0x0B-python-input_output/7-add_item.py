#!/usr/bin/python3
""" Load, add, save  """
from sys import argv
from 6-load_from_json_file import load_from_json_file
from 5-save_to_json_file import save_to_json_file

""" Script that adds all arguments to a Python list,
and then save them to a file """
try:
    add_items = load_from_json_file('add_item.json')
    save_to_json_file(add_items + argv[1:], 'add_item.json')
except Exception:
    save_to_json_file(argv[1:], 'add_item.json')
