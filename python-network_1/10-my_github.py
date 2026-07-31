#!/usr/bin/python3
"""Module that displays a GitHub user's id using Basic Authentication."""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get(
        "https://api.github.com/user", auth=(username, password))
    print(r.json().get("id"))
