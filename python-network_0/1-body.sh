#!/usr/bin/env bash
# Send a GET request to a URL and display the body only if status is 200

url="$1"

response=$(curl -s -w "\n%{http_code}" "$url")
status_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$d')

if [ "$status_code" -eq 200 ]; then
    echo "$body"
fi
