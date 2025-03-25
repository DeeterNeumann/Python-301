# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

from bs4 import BeautifulSoup
import requests
import json


nfl_url = "https://nfl.com"

with open('nfl_stats.json', "r") as fin:
    nfl_data = json.load(fin)

nfl_soup = BeautifulSoup(nfl_data, features="html.parser")
nfl_links = nfl_soup.find_all('a', href=True)

search_string = "/players/"

links_list = [link['href'] for link in nfl_links if search_string in link['href']]

leading_passer = next((link for link in links_list if "/players/" in link))

name = leading_passer.split("/")[2]

first_name, last_name = name.split("-")

leading_passer_wiki_url = f"https://en.wikipedia.org/wiki/{first_name.capitalize()}_{last_name.capitalize()}"

# print(leading_passer_wiki_url)

passer_response = requests.get(leading_passer_wiki_url)
passer_response_data = passer_response.text

# print(passer_response_data)

leading_passer_soup = BeautifulSoup(passer_response_data, features="html.parser")


interception_data = leading_passer_soup.select("h3#Regular_season")[0]

regular_season_table = interception_data.find_next("table")

links = regular_season_table.find_all("a", href=True)

# print(links)

http_search = "/wiki/2024_NFL_season"
# # wiki_search = "/wiki/"

links_list = [link for link in links if http_search in link['href']]

target_link = links_list[0]

# print(target_link)

games_played = target_link.find_next('b').contents[0]

games_started = games_played.find_next('b').contents[0]

record = games_started.find_next('td').contents[0]

completions = record.find_next('b').contents[0]

attempts = completions.find_next('b').contents[0]

pass_percentage = attempts.find_next('b').contents[0]

yards = pass_percentage.find_next('b').contents[0]

yards_per_attempt = yards.find_next('td').contents[0]

longest_pass = yards_per_attempt.find_next('td').contents[0]

touchdowns = longest_pass.find_next('b').contents[0]

interceptions = touchdowns.find_next('td').contents[0]

rating = interceptions.find_next('b').contents[0]

# print(games_played)
# print(games_started)
# print(record)
# print(completions)
# print(attempts)
# print(pass_percentage)
# print(yards)
# print(yards_per_attempt)
# print(longest_pass)
# print(touchdowns)
# print(interceptions)
# print(rating)

print(f"The NFL's leading passer, {first_name.capitalize()} {last_name.capitalize()}, threw for {yards} yards and {interceptions} interceptions in the 2024 season.")

# selenium