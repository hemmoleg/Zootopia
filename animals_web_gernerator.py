import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def main():
    animal_data = load_data('animals_data.json')

    for animal in animal_data:
        print(f"Name: {animal['name']}")
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            print(f"Diet: {animal['characteristics']['diet']}")
        print(f"Locations {animal['locations'][0]}")
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")
        print()

if __name__ == '__main__':
    main()