#!/usr/bin/python3
"""Module that sends a POST request with an email parameter."""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    with urllib.request.urlopen(url, data) as r:
        print(r.read().decode("utf-8"))
