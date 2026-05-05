# Zootopia - Codio Git Aufgabe
# Alexander Bormann

import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")
#print(animals_data)

for animal in animals_data:
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    locations = animal.get("locations", [])
    location = locations[0] if locations else None
    animal_type = characteristics.get("type")

    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if location:
        print(f"Location: {location}")
    if animal_type:
        print(f"Type: {animal_type}")
    print()