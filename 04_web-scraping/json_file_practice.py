import json
from pprint import pprint

with open('films.json', "r") as fin:
    movie_data = json.load(fin)

print(len(movie_data))
print(type(movie_data))

film_data = movie_data['data']['films']

# pprint(film_data)

# pprint(film_data)

for i in film_data:
    pprint(f"{i['title']} was directed by {i['director']}.")
    
longest_film = max(film_data, key=lambda x: int(x['running_time']))
# check lambda types

print(f"The longest film at a run time of {longest_film['running_time']} minutes is {longest_film['title']}. It was released in {longest_film['release_date']} with the original title {longest_film['original_title']}.")