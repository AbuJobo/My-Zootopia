# Zootopia - Codio Git Aufgabe
# Alexander Bormann
#

import json

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

def render_card(animal):
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    locations = animal.get("locations", [])
    location = locations[0] if locations else None
    animal_type = characteristics.get("type")

    card = '<li class="cards__item">\n'
    if name:
        card += f'<div class="card__title">{name}</div>\n'
    card += '<p class="card__text">\n'
    if diet:
        card += f'<strong>Diet:</strong> {diet}<br/>\n'
    if location:
        card += f'<strong>Location:</strong> {location}<br/>\n'
    if animal_type:
        card += f'<strong>Type:</strong> {animal_type}<br/>\n'
    card += '</p></li>\n'
    return card

# HTML-String für die Tierkarten aufbauen

output = ""
for animal in animals_data:
    output += render_card(animal)

with open("animals_template.html", "r", encoding="utf-8") as f:
    template = f.read()

updated_html = template.replace("{{ANIMAL_CARDS}}", output)

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(updated_html)