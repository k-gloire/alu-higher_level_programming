#!/usr/bin/python3
"""Module that searches for a user by letter via a POST request."""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})

    try:
        result = r.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
