#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL with specified parameters, and displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
