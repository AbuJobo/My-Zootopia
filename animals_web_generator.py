# Zootopia - Codio Git Aufgabe
# Alexander Bormann
import data_fetcher


def render_card(animal):
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    locations = animal.get("locations", [])
    location = locations[0] if locations else None
    animal_type = characteristics.get("type")

    card = '<li class="cards__item">\n'

    if name:
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


def create_output(animals_data):
    if not animals_data:
        return (
            '<li class="cards__item">\n'
            '  <div class="card__title">No animals found</div>\n'
            '  <p class="card__text">The API did not return any matching animals.</p>\n'
            '</li>\n'
        )

    output = ""
    for animal in animals_data:
        output += render_card(animal)
    return output


def main():
    animal_name = input("Please enter an animal: ").strip()
    data = data_fetcher.fetch_data(animal_name)
    output = create_output(data)

    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_template = file.read()

    html = html_template.replace("{{ANIMAL_CARDS}}", output)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
