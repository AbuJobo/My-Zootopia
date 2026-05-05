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
    output += '            <div class="card__text">\n'
    if name:
        output += f'              <div class="card__title">{name}</div>\n'
    if diet:
        output += f"              <p>Diet: {diet}</p>\n"
    if location:
        output += f"              <p>Location: {location}</p>\n"
    if animal_type:
        output += f"              <p>Type: {animal_type}</p>\n"
    output += "            </div>\n"
    output += "          </li>\n"

print(output)