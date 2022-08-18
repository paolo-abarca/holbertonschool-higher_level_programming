#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument and returns the response body
curl -sLX "DELETE" "$1"
