import requests
import json

# Fetch all elements
response = requests.get('https://api.periodictableofelements.org/elements/export/json/').json()

#
def load_all_elements_as_json():
    with open('periodic_table_data.json', encoding="utf-8", mode='w') as elements_file:
        json.dump(response, elements_file, indent=2)




