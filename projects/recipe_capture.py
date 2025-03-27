import requests
import json

URL = "https://codingnomads.github.io/recipes"

response = requests.get(URL)
recipe_data = response.text

with open('recipe_collection.json', "w") as fout:
    json.dump(recipe_data, fout)