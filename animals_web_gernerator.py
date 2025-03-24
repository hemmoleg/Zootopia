import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_html(file_path):
    with open(file_path, "r") as handle:
        return handle.read()


def create_animal_data_html(animal_data):
    animal_data_string = "<ul class='cards'>"

    for animal in animal_data:
        animal_data_string += "<li class='cards__item'>"
        animal_data_string += f"Name: {animal['name']}<br/>\n"

        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            animal_data_string += f"Diet: {animal['characteristics']['diet']}<br/>\n"

        animal_data_string += f"Locations {animal['locations'][0]}<br/>\n"

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            animal_data_string += f"Type: {animal['characteristics']['type']}<br/>\n"

        animal_data_string += "</li>\n"

    animal_data_string += "</ul>"

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


if __name__ == '__main__':
    main()