#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response if the status code is 200
curl -sL -w "%{http_code}" "$1" -o temp_body | grep -q "200$" && cat temp_body
