#!/bin/bash
# Bash script that takes a URL, sends a POST request to the passed URL, and displays the response body
curl -sLX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
