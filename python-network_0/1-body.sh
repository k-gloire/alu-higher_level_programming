#!/bin/bash
# Send a GET request, follow redirects, and display the body if status is 200
[ "$(curl -sL -o /tmp/curl_body -w '%{http_code}' "$1")" = "200" ] && cat /tmp/curl_body
