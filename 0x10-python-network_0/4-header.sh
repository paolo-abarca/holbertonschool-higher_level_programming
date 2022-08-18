#!/bin/bash
# Bash script that takes a URL as an argument, sends a GET request to the URL, and displays the response body
curl -sLH "X-HolbertonSchool-User-Id: 98" "$1"
