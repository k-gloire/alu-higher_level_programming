#!/usr/bin/python3
"""Module that fetches a URL and reports its HTTP error code, if any."""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            print(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
