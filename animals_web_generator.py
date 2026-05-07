# Zootopia - Codio Git Aufgabe
# Alexander Bormann

import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "ciBBT43nMOeo5QDAnJeFo91mLNeReqlVSvtsAblX"


def fetch_animals(animal_name):
    response = requests.get(
        API_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


animals_data = fetch_animals("fox")


def render_card(animal):
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    locations = animal.get("locations", [])
    location = locations[0] if locations else None
    animal_type = characteristics.get("type")

    card = '<li class="cards__item">\n'
    card += f'  <div class="card__title">{name}</div>\n'
    card += '  <p class="card__text">\n'

    if diet:
        card += f'    <strong>Diet:</strong> {diet}<br/>\n'
    if location:
        card += f'    <strong>Location:</strong> {location}<br/>\n'
    if animal_type:
        card += f'    <strong>Type:</strong> {animal_type}<br/>\n'

    card += '  </p>\n'
    card += '</li>\n'
    return card


output = ""
for animal in animals_data:
    output += render_card(animal)

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

html = html_template.replace("{{ANIMAL_CARDS}}", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Website was successfully generated to the file animals.html.")