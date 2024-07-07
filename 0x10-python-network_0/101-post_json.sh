#!/bin/bash
# A bash script that sends a JSON POST request to a URL and display response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
