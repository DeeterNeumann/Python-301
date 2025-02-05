# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

import requests
from pprint import pprint
import json

BASE_URL = "https://pokeapi.co/api/v2/"
response = requests.get(BASE_URL)
poke_data = response.json()

poke_URL = BASE_URL + "pokemon/"

# pprint(poke_data)

poke_list = ["bulbasaur", "charizard", "squirtle", "weedle", "beedrill", "pidgeot"]

for pokemon in poke_list:
    response = requests.get(poke_URL + pokemon)
    poke_data = response.json()
    poke_num = poke_data['game_indices'][-1]['game_index']
    poke_types = poke_data['types']
    poke_types_list = []
    for type in poke_types:
        poke_types_list.append(type['type']['name'])
    print(f"Name: {pokemon}, Number: {poke_num}, Types: {'; '.join(poke_types_list)}")

# combine the list into one string with this "joining" them