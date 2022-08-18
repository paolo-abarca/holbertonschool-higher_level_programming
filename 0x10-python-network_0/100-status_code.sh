#!/bin/bash
# Bash script that sends a request to a URL passed as an argument and displays only the response status code
curl -o /dev/null --silent --head --write-out '%{http_code}' "$1"
