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
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    locations = animal.get("locations", [])
    location = locations[0] if locations else None
    animal_type = characteristics.get("type")

    if name:
        output += f"Name: {name}\n"
    if diet:
        output += f"Diet: {diet}\n"
    if location:
        output += f"Location: {location}\n"
    if animal_type:
        output += f"Type: {animal_type}\n"
    output += "\n"

print(output)