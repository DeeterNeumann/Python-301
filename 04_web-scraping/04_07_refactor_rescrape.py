# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

from bs4 import BeautifulSoup, NavigableString
import requests
import json


nfl_url = "https://nfl.com"

# scrape table headers into list
# stat_headers = 

# create dictionary of stat table headers
# player_stats = dict.fromkeys(stat_headers)


### create dictionary filled in with target row stat, return from function, and use dictionary at the end. Don't forget to take in target row and spit out dictionary

def leading_passer():
    with open('nfl_stats.json', "r") as fin:
        nfl_data = json.load(fin)

    nfl_soup = BeautifulSoup(nfl_data, features="html.parser")
    nfl_links = nfl_soup.find_all('a', href=True)
    
    search_string = "/players/"

    links_list = [link['href'] for link in nfl_links if search_string in link['href']]

    leading_passer = next((link for link in links_list if "/players/" in link))

    name = leading_passer.split("/")[2]

    return name.split("-")

def wiki_lookup_leading_passer(first_name, last_name):
    leading_passer_wiki_url = f"https://en.wikipedia.org/wiki/{first_name.capitalize()}_{last_name.capitalize()}"
    passer_response = requests.get(leading_passer_wiki_url)
    return passer_response.text

def get_value(stat):
    # print(type(stat))
    while type(stat.contents[0]) != NavigableString:
        stat = stat.contents[0]
        # print(type(stat))
    return stat.contents[0]

def stat_dict():
    player_stats = {"games_played": None, "games_started": None, "record": None, "completions": None, "attempts": None, "pass_percentage": None, "yards": None, "yards_per_attempt": None, "longest_pass": None, "touchdowns": None, "interceptions": None, "rating": None }
    n = 2
    while n < 14:
        for key in player_stats:
            player_stats[key] = get_value(target_row[n])
            n += 1
    return player_stats

# print(type(""))
# print(str)

# print(passer_response_data)

first_name, last_name = leading_passer()

passer_response_data = wiki_lookup_leading_passer(first_name, last_name)

leading_passer_soup = BeautifulSoup(passer_response_data.replace("\n",""), features="html.parser")

interception_data = leading_passer_soup.select("h3#Regular_season")[0]

regular_season_table = interception_data.find_next("table")

links = regular_season_table.find_all("tr")

# print(len(links))

target_row = links[-2].contents

# print(target_row)

# print(target_row[2].contents[0].contents[0])

# print(target_row[3].contents[0].contents[0])

# games_played = get_value(target_row[2])

# games_started = get_value(target_row[3])

# record = get_value(target_row[4])


# print(games_played)
# print(games_started)
# print(record)


# completions = record.findNext('b').contents[0]

# attempts = completions.findNext('b').contents[0]

# pass_percentage = attempts.findNext('b').contents[0]

# yards = pass_percentage.findNext('b').contents[0]

# yards_per_attempt = yards.findNext('td').contents[0]

# longest_pass = yards_per_attempt.findNext('td').contents[0]

# touchdowns = longest_pass.findNext('b').contents[0]

# interceptions = touchdowns.findNext('td').contents[0]

# rating = interceptions.findNext('b').contents[0]

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


# rows 2-13

player_stats = stat_dict()

print(f"The NFL's leading passer, {first_name.capitalize()} {last_name.capitalize()}, threw for {player_stats["yards"]} yards and {player_stats["interceptions"]} interceptions in the 2024 season.")