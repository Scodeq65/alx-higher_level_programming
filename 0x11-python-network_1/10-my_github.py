#!/usr/bin/python3
"""
Python script that takes your GitHub credentials and
uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


def get_github_id(username, token):
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(username, token))
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("None")


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_id(username, token)
