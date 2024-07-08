#!/usr/bin/python3
"""A python script that takes in a URL, sends a request to the URL
and display the value of the X-Request-Id variable,
"""

import sys
import urllib.request


def fetch_x_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id not found in the response headers.")
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
