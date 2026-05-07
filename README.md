# Zootopia Animal Repository

This project generates a simple animal website based on data from the API Ninjas Animals API.

The user enters the name of an animal, the program fetches matching results from the API, and then creates an `animals.html` page that displays the selected animal information.

## Project Purpose

This project demonstrates how to:

- fetch data from an external API
- separate data fetching from website generation
- use a template-based HTML generator
- store sensitive API keys outside the Python code
- document and structure a small Python project professionally

## Project Structure

- `animals_web_generator.py` – main program, asks the user for an animal name and generates the website
- `data_fetcher.py` – fetches animal data from the API
- `animals_template.html` – HTML template used to build the final page
- `style.css` – external stylesheet for the website
- `requirements.txt` – required Python packages
- `.env` – stores the API key locally (not committed to Git)
- `README.md` – project documentation

## Installation

Install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## API Key Setup

Create a `.env` file in the root folder of the project:

```env
API_NINJAS_KEY=your_api_key_here
```

Make sure `.env` is listed in `.gitignore` so your secret key is not uploaded to GitHub.

## Usage

Run the program with:

```bash
python3 animals_web_generator.py
```

Example:

```bash
Please enter an animal: Fox
Website was successfully generated to the file animals.html.
```

After running the script, the program creates an `animals.html` file containing the matching animal results.

## Data Structure

The API returns a JSON array of animal objects.  
Each animal is represented by a dictionary with this general structure:

```json
[
  {
    "name": "Fox",
    "taxonomy": {
      "kingdom": "Animalia",
      "phylum": "Chordata",
      "class": "Mammalia",
      "order": "Carnivora",
      "family": "Canidae",
      "genus": "Vulpes",
      "scientific_name": "Vulpes vulpes"
    },
    "locations": [
      "Africa",
      "Asia",
      "Europe",
      "North-America"
    ],
    "characteristics": {
      "prey": "Rabbits, Birds, Lizards",
      "habitat": "Woodland areas and urban parks",
      "diet": "Carnivore",
      "lifestyle": "Solitary",
      "type": "Mammal",
      "color": "BrownRedBlackTan",
      "skin_type": "Fur",
      "top_speed": "29 mph",
      "lifespan": "3 - 11 years",
      "weight": "5kg - 11kg (11lbs - 24lbs)",
      "length": "40cm - 83cm (16in - 33in)"
    }
  }
]
```

According to the API documentation, each result can contain these top-level fields:

- `name`
- `taxonomy`
- `locations`
- `characteristics`

### Taxonomy structure

The `taxonomy` object may contain:

- `kingdom`
- `phylum`
- `class`
- `order`
- `family`
- `genus`
- `scientific_name`

### Characteristics structure

The `characteristics` object may contain many fields, for example:

- `prey`
- `name_of_young`
- `group_behavior`
- `estimated_population_size`
- `biggest_threat`
- `most_distinctive_feature`
- `gestation_period`
- `habitat`
- `diet`
- `average_litter_size`
- `lifestyle`
- `common_name`
- `number_of_species`
- `location`
- `slogan`
- `group`
- `color`
- `skin_type`
- `top_speed`
- `lifespan`
- `weight`
- `height`
- `age_of_sexual_maturity`
- `age_of_weaning`

## Currently Used Data Extract

Although the API returns a rich nested data structure, the current version of this project only uses a **small selected extract** of the response.

### Currently displayed fields

```json
{
  "name": "Fox",
  "locations": [
    "Africa",
    "Asia",
    "Europe",
    "North-America"
  ],
  "characteristics": {
    "diet": "Carnivore",
    "type": "Mammal"
  }
}
```

### What is currently rendered on the website

The website currently displays:

- `name`
- `characteristics.diet`
- `characteristics.type`
- the **first item only** from the `locations` array

### Important note about locations

The API returns `locations` as an array of places where the animal can be found.  
At the moment, the project does **not** display all locations. Instead, it only uses:

```python
location = locations if locations else None
```

This means:

- if multiple locations are returned, only the first one is shown
- the remaining locations are currently ignored
- the full API response contains more information than the website currently displays

## Example

If the user enters `Fox`, the API may return several matching animals such as `Fox`, `Red Fox`, `Gray Fox`, or `Fennec Fox`, because the search supports partial matches. The generated website will display one card per returned animal result. [web:5]

If the user enters an animal name that is not found, the program generates a fallback message on the page instead of animal cards.

## Requirements

This project currently needs these external Python packages:

```txt
requests
python-dotenv
```

## Contributing

Contributions are welcome.  
You can improve the project by:

- displaying more fields from the API
- showing all available locations instead of only the first one
- improving the website layout
- adding better error handling

## License

This project was created for educational purposes.