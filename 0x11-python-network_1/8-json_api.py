#!/usr/bin/python3
"""
Python script that sends Post request to URL with a letter as parameter.
"""

import sys
import requests


def check_usr(letter):
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    respo = requests.post(url, data=data)
    try:
        json_response = respo.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    check_usr(letter)
