#!/usr/bin/python3
"""Module that sends a POST request with an email parameter."""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={"email": email})
    print(r.text)
