#!/usr/bin/python3
"""A Python script that takes in a URL,then sends
a request to the URL which would display the value of
the variable X-Request-Id in the response header."""

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
