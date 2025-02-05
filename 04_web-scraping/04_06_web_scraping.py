# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

from bs4 import BeautifulSoup
import requests
import json

with open('nfl_stats.json', "r") as fin:
    nfl_data = json.load(fin)

nfl_url = "https://nfl.com"

nfl_soup = BeautifulSoup(nfl_data)

nfl_links = nfl_soup.find_all('a', href=True)

search_string = "/players/"

links_list = [link['href'] for link in nfl_links if search_string in link['href']]

leading_passer = next((link for link in links_list if "/players/" in link))

leading_passer_stats_url = nfl_url + leading_passer + "stats/"

leading_passer_soup = BeautifulSoup(leading_passer_stats_url)

interception_data = leading_passer_soup.find_all('td', class_="nfl-t-stats_col-14 selected")

interception_values = [float(td.text.strip()) for td in interception_data]

total_interceptions = sum(interception_values)

print(f"The NFL's leading passer has thrown {total_interceptions} interceptions")


# print(type(nfl_data)) Output: <class 'str'>

# links = nfl_soup.find_all("a")

# links_list = [link['href'] for link in links]

# print(links_list)

# print(nfl_soup.prettify())

# player_link = next((link for link in links_list if))

# for link in links:
#     if http_search in link["href"]:
#         links_list.append(link)

# player = input("Enter last name of an NFL player: ")

# player = player.lower()

# player_link = next((link for link in links_list if player in link), None)

# print(player_link)
# player_url = nfl_url + player_link

# print(player_url)

# if player_link:
#     print("Player: ", player_url)


#     player_page = requests.get(player_url)
#     scraped_page = player_page.text

#     with open('player_scrape.json', 'w') as fout:
#         json.dump(scraped_page, fout)

#     print("Scraped NFL player page saved to 'player_scrape.json'")
# else:
#     print("No player link found.")