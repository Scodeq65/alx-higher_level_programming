#!/usr/bin/python3
"""This is a python script  that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


def fetch_status():
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    fetch_status()
