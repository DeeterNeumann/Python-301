# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.

import webbrowser
import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

# Input to gather ingredients from user
ingredients = input("Enter the ingredients you want to use in a recipe, each separated by a comma (Example: milk, eggs, flour): ")
ingredient_list = ingredients.split(", ")

URL = "https://codingnomads.github.io/recipes"
get_recipes = requests.get(URL)

with open('recipe_collection.json', "r") as fin:
    recipe_collection_data = json.load(fin)

recipe_collection_soup = BeautifulSoup(recipe_collection_data, features="html.parser")
recipe_links = recipe_collection_soup.find_all('a', href=True)

search_string = "recipes/"

links_list = [link['href'] for link in recipe_links if search_string in link['href']]

recipe_list = []

for link in links_list:
    recipe_url = f"https://codingnomads.github.io/recipes/{link}"
    recipe_response = requests.get(recipe_url)
    recipe_data = recipe_response.text
    recipe_soup = BeautifulSoup(recipe_data, features="html.parser")
    ingredient_data = recipe_soup.find_all("md")
    for ingredients in ingredient_data:
        recipe_list.append(link)
    print(recipe_list)
    

# search each URL for included ingredients

# Fetch recipe from CodingNomads recipe collection

# Search recipes to find ones including provided ingredients