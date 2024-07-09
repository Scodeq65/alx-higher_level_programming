#!/usr/bin/python3
"""
Python script that send a request to URL and display
the body of the request.
"""

import requests
import sys


def show_url(url):
    respo = requests.get(url)
    if respo.status_code >= 400:
        print(f"Error code: {respo.status_code}")
    else:
        print(respo.text)


if __name__ == "__main__":
    url =sys.argv[1]
    show_url(url)
