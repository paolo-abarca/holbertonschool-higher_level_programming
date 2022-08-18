#!/bin/bash
# Bash script that takes a URL and displays all the HTTP methods the server will accept
curl -sLI "$1" | grep -i Allow | cut -d " " -f2-
