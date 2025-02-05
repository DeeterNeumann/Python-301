# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi-iansedano.vercel.app/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests
import json
from pprint import pprint

response = requests.get("https://ghibliapi-iansedano.vercel.app/api/species")
species_data = response.json()['data']['species']

# pprint(species_data)

search_string = "Cat"

for species in species_data:
    if species['name'] == search_string:
        for person_url in species['people']:
            person_response = requests.get(person_url)
            person_data = person_response.json()['data']
            for person in person_data:
                print(f"{person['name']}, {person['gender']}")
            
    
# {"data":[{"id":"7151abc6-1a9e-4e6a-9711-ddb50ea572ec","name":"Jiji","gender":"Male","age":"NA","eye_color":"Black","hair_color":"Black","films":["https://ghibliapi-iansedano.vercel.app/api/films/ea660b10-85c4-4ae3-8a5f-41cea3648e3e"],"species":"https://ghibliapi-iansedano.vercel.app/api/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3","url":"https://ghibliapi-iansedano.vercel.app/api/people/7151abc6-1a9e-4e6a-9711-ddb50ea572ec"}]}

