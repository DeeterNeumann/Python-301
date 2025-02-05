# In three lines of code, fetch the HTML text from CodingNomads'
# main page and print it to your console.
#
# If you run into encoding/decoding errors, you're experiencing something
# very common. head over to StackOverflow and find a solution!

import requests

coding_nomads = "https://codingnomads.com/"
page = requests.get(coding_nomads)
print(page.text)