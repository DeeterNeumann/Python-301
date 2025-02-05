
import requests
import json
from pprint import pprint

BASE_URL = "https://pokeapi.co/api/v2/"
response = requests.get(BASE_URL)
poke_data = response.json()

with open('pokeman.json', 'w') as fout:
    json.dump(poke_data, fout)