# Zootopia - Codio Git Aufgabe
# Alexander Bormann
import data_fetcher


def render_info_item(label, value):
    if not value:
        return ""
    return (
        '<div class="info-item">'
        f'<span class="info-label">{label}</span>'
        f'<span class="info-value">{value}</span>'
        '</div>'
    )


def render_card(animal):
    name = animal.get("name")
    taxonomy = animal.get("taxonomy", {})
    characteristics = animal.get("characteristics", {})

    scientific_name = taxonomy.get("scientific_name")
    slogan = characteristics.get("slogan")

    locations = animal.get("locations", [])
    location = locations[0] if locations else None

    animal_type = characteristics.get("type")
    diet = characteristics.get("diet")
    lifespan = characteristics.get("lifespan")
    weight = characteristics.get("weight")
    length = characteristics.get("length")

    left_column = ""
    left_column += render_info_item("Primary Location", location)
    left_column += render_info_item("Type", animal_type)
    left_column += render_info_item("Diet", diet)

    right_column = ""
    right_column += render_info_item("Length", length)
    right_column += render_info_item("Weight", weight)
    right_column += render_info_item("Lifespan", lifespan)

    header = f'<h2 class="card-title">{name}'
    if scientific_name:
        header += f' <span class="scientific-name">({scientific_name})</span>'
    header += '</h2>'

    card = '<div class="animal-card">\n'
    card += '  <div class="card-header">\n'
    card += f'    {header}\n'
    if slogan:
        card += f'    <div class="card-slogan">{slogan}</div>\n'
    card += '  </div>\n'
    card += '  <div class="card-body">\n'
    card += f'    <div class="card-col">{left_column}</div>\n'
    card += f'    <div class="card-col">{right_column}</div>\n'
    card += '  </div>\n'
    card += '</div>\n'
    return card


def create_output(animals_data):
    if not animals_data:
        return (
            '<div class="animal-card">'
            '<div class="card-header">'
            '<h2 class="card-title">No animals found</h2>'
            '</div>'
            '<div class="card-body">'
            '<div class="card-col">'
            '<div class="info-item"><span class="info-value">The API did not return any matching animals.</span></div>'
            '</div>'
            '<div class="card-col"></div>'
            '</div>'
            '</div>'
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