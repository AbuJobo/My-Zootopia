# Zootopia - Codio Git Aufgabe
# Alexander Bormann

import json

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")
#print(animals_data)

# HTML-String für die Tierkarten aufbauen
output = ""
for animal in animals_data:
    name             = animal.get("name")
    characteristics  = animal.get("characteristics", {})
    diet             = characteristics.get("diet")
    locations        = animal.get("locations", [])
    location         = locations[0] if locations else None
    animal_type      = characteristics.get("type")

    output += '          <li class="cards__item">\n'
    if name:
        output += f'            <div class="card__title">{name}</div>\n'
    output += '            <p class="card__text">\n'
    if diet:
        output += f"                <strong>Diet:</strong> {diet}<br/>\n"
    if location:
        output += f"                <strong>Location:</strong> {location}<br/>\n"
    if animal_type:
        output += f"                <strong>Type:</strong> {animal_type}<br/>\n"
    output += "            </p>\n"
    output += "          </li>\n"

print(output)