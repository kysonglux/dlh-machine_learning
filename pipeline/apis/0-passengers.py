#!/usr/bin/env python3
"""returns the list of ships that can hold a given number of passengers"""
import requests


def availableShips(passengerCount):
    """returns the list of ships"""
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data.get("results", []):
            passengers = ship.get("passengers", "0")

            passengers = passengers.replace(",", "")
            if passengers.isdigit():
                if int(passengers) >= passengerCount:
                    ships.append(ship["name"])

        url = data.get("next")
    return ships
