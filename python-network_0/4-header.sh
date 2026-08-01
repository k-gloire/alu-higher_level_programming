#!/bin/bash
# Send a GET request with a custom header and display the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
