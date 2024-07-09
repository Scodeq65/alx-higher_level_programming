#!/usr/bin/python3
"""
Python script that send a post request to a URL with email as it parameter.
"""

import sys
import urllib.parse
import urllib.request


def post_email(url, email):
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    try:
        with urllib.request.urlopen(url, data) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
