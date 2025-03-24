import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_html(file_path):
    with open(file_path, "r") as handle:
        return handle.read()


def create_animal_data_html(animal_data):
    animal_data_string = ""

    for animal in animal_data:
        animal_data_string += "<li class='cards__item'>"
        animal_data_string += f"<div class='card__title'>Name: {animal['name']}</div>"
        animal_data_string += "<p class='card__text'>"

        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            animal_data_string += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>"

        animal_data_string += f"<strong>Locations:</strong> {animal['locations'][0]}<br/>"

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            animal_data_string += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>"

        animal_data_string += "</p></li>\n"

    return animal_data_string


def write_html(html):
    with open('animal.html', "w") as handle:
        handle.write(html)


def main():
    animal_data = load_data('animals_data.json')
    html = load_html('animals_template.html')
    animal_data_string = create_animal_data_html(animal_data)

    html = str(html).replace("__REPLACE_ANIMALS_INFO__", animal_data_string)
    write_html(html)

    print(animal_data_string)
    print(html)


if __name__ == '__main__':
    main()