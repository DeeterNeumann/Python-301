import requests
import json

nfl_stats_url = "https://www.nfl.com/stats/player-stats/"

response = requests.get(nfl_stats_url)
nfl_data = response.text

with open('nfl_stats.json', 'w') as fout:
    json.dump(nfl_data, fout)