# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

from bs4 import BeautifulSoup
import requests
import json

URL = "https://en.wikipedia.org/wiki/Web_scraping"

page = requests.get(URL)
# print(page.text)

wiki_soup = BeautifulSoup(page.text, "html.parser")

links = wiki_soup.find_all('a', href=True)

# for link in links:
#     print(link["href"])

http_search = "http"
# wiki_search = "/wiki/"

links_list = [link['href'] for link in links if http_search in link['href']]

# for link in links:
#     if http_search in link["href"]:
#         links_list.append(link)

wikipedia_link = next((link for link in links_list if "wikipedia.org/wiki/" in link), None)

if wikipedia_link:
    print("First Wikipedia link:", wikipedia_link)


    wiki_page = requests.get(wikipedia_link)
    scraped_page = wiki_page.text

    with open('wiki_scrape.json', 'w') as fout:
        json.dump(scraped_page, fout)

    print("Scraped Wikipedia page saved to 'wiki_scrape.json'")
else:
    print("No Wikipedia link found.")
