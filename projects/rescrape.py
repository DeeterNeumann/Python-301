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
ingredient_list = [ingredient.strip().lower() for ingredient in ingredients.split(",")]

print("Gathering recipes...")

URL = "https://codingnomads.github.io/recipes"
get_recipes = requests.get(URL)

with open('recipe_collection.json', "r") as fin:
    recipe_collection_data = json.load(fin)

recipe_collection_soup = BeautifulSoup(recipe_collection_data, features="html.parser")
recipe_links = recipe_collection_soup.find_all('a', href=True)

search_string = "recipes/"

links_list = [link['href'] for link in recipe_links if search_string in link['href']]

matching_recipes = []

for link in links_list:
    recipe_url = f"https://codingnomads.github.io/recipes/{link}"
    try:
        print(f"Searching...{link}")
        recipe_response = requests.get(recipe_url)
        recipe_data = recipe_response.text
        
        # ingredients_section = recipe_soup.find(class_="ingredients")

        # if ingredients_section:
        #     recipe_text = ingredients_section.get_text().lower()
        # else:
        recipe_text = recipe_data.lower()

        if all(ingredient in recipe_text for ingredient in ingredient_list):
            matching_recipes.append(recipe_url)
    except Exception as e:
        print(f"Error scraping {recipe_url}: {e}")

if matching_recipes:
    print(f"\nWe found {len(matching_recipes)} recipes that include your ingredients!:")
    pprint(matching_recipes)
else:
    print("There were no recipes that included all the ingredients you entered!")