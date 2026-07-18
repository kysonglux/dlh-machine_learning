#!/usr/bin/env python3
"""write a script that prints the location of a specific user"""

import requests
import sys
from datetime import datetime


def user_location(url):
    """write a script that prints the location of a specific user"""
    try:
        response = requests.get(url)
        if response.status_code == 403:
            reset_ts = int(response.headers.get("X-RateLimit-Reset", 0))
            now_ts = int(datetime.now().timestamp())
            minutes = (reset_ts - now_ts) // 60
            print(f"Reset in {minutes} min")
            return
        if response.status_code == 404:
            print("Not found")
            return

        data = response.json()
        location = data.get("location")

        if location:
            print(location)
        else:
            print("Not found")

    except Exception:
        print("Not found")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not found")
    else:
        user_location(sys.argv[1])
