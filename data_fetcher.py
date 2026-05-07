import os
import sys
import requests

API_URL = "https://api.api-ninjas.com/v1/animals"


def load_api_key():
    file_path = "apikey.txt"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            api_key = file.read().strip()
            if api_key:
                return api_key

    api_key = input("Please enter your API key: ").strip()

    if not api_key:
        print("No API key provided. Program will exit.")
        sys.exit(1)

    return api_key


def fetch_data(animal_name):
    api_key = load_api_key()

    response = requests.get(
        API_URL,
        headers={"X-Api-Key": api_key},
        params={"name": animal_name},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()