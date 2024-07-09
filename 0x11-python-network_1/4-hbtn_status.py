#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status using requests.
"""
import requests


def fetch_status():
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")


if __name__ == "__main__":
    fetch_status()
