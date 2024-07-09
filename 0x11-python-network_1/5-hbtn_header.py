#!/usr/bin/python3
"""
Python script that sends a request to a URL and displays the value
of X-Request-Id.
"""

import sys
import requests


def fetch_res_id(url):
    respo = requests.get(url)
    request_id = respo.headers.get('X-Request-Id')
    print(request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_res_id(url)
