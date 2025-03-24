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

    for animal_obj in animal_data:
        animal_data_string += serialize_animal(animal_obj)

    return animal_data_string


def serialize_animal(animal_obj):
    animal_data_string=""
    animal_data_string += "<li class='cards__item'>"
    animal_data_string += f"<div class='card__title'>Name: {animal_obj['name']}</div>"
    animal_data_string += "<div class='card__text'><ul>"

    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        animal_data_string += f"<li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>"

    animal_data_string += f"<li><strong>Locations:</strong> {animal_obj['locations'][0]}</li>"

    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        animal_data_string += f"<li><strong>Type:</strong> {animal_obj['characteristics']['type']}</li>"

    if 'characteristics' in animal_obj and 'group_behavior' in animal_obj['characteristics']:
        animal_data_string += f"<li><strong>Group behavior:</strong> {animal_obj['characteristics']['group_behavior']}</li>"

    if 'characteristics' in animal_obj and 'top_speed' in animal_obj['characteristics']:
        animal_data_string += f"<li><strong>Top speed:</strong> {animal_obj['characteristics']['top_speed']}</li>"

    animal_data_string += "</ul></div></li>\n"
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