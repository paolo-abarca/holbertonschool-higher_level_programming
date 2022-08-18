#!/bin/bash
# Bash script that takes a URL, sends a request to that URL, and returns the size of the response body
curl -sI 0.0.0.0:5000 | grep -i Content-Length | cut -d " " -f2
