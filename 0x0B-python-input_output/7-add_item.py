#!/usr/bin/python3
""" Adds argument to a python list."""


import sys
import json


def save_to_json_file(data, filename):
    """Save data to JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_from_json_file(filename):
    """Load data from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python3 script.py <argv1> <argv2> ...")
        sys.exit(1)

    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    for arg in sys.argv[1:]:
        data.append(arg)

    save_to_json_file(data, "add_item.json")
