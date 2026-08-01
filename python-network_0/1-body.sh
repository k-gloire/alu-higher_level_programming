#!/bin/bash
# Send a GET request and display only the body if status is 200
[ "$(curl -s -o /tmp/curl_body -w '%{http_code}' "$1")" = "200" ] && cat /tmp/curl_body
