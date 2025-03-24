import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_html(file_path):
    with open(file_path, "r") as handle:
        return handle.read()


def create_animal_data_string(animal_data):
    animal_data_string = ""

    for animal in animal_data:
        animal_data_string += f"Name: {animal['name']}\n"

        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            animal_data_string += f"Diet: {animal['characteristics']['diet']}\n"

        animal_data_string += f"Locations {animal['locations'][0]}\n"

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            animal_data_string += f"Type: {animal['characteristics']['type']}\n"

        animal_data_string += "\n"

    return animal_data_string


def write_html(html):
    with open('animal.html', "w") as handle:
        handle.write(html)


def main():
    animal_data = load_data('animals_data.json')
    html = load_html('animals_template.html')
    animal_data_string = create_animal_data_string(animal_data)

    html = str(html).replace("__REPLACE_ANIMALS_INFO__", animal_data_string)
    write_html(html)


if __name__ == '__main__':
    main()