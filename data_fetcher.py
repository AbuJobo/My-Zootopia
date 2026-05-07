import os
from dotenv import load_dotenv
import requests
load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_NINJAS_KEY")


def fetch_data(animal_name):

    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()