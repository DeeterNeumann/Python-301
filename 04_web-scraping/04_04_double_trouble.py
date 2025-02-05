# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests
import json
from pprint import pprint

chuck_url = "https://api.chucknorris.io/jokes/random"

chuck_response = requests.get(chuck_url)
chuck_fact = chuck_response.json()
# print(chuck_fact['value'])

num_url = "http://numbersapi.com/random/trivia"

num_response = requests.get(num_url)
num_fact = num_response.text

print(f"Welcome to your random Chuck and Number facts.\n Here is your Chuck fact: {chuck_fact['value']}\n Here is your Number fact: {num_fact}")


