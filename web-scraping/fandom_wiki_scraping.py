import cloudscraper
from bs4 import BeautifulSoup
import time
import requests

scraper = cloudscraper.create_scraper()

# Aang page
# url = "https://avatar.fandom.com/wiki/Aang"
# start = time.time()
# response = scraper.get("https://avatar.fandom.com/wiki/Aang",timeout=5)
# end = time.time()
# print(end - start)

# soup = BeautifulSoup(response.text, "html.parser")

start = time.time()
# Use action=parse to get rendered HTML for article pages via the MediaWiki API
response = requests.get(
    "https://avatar.fandom.com/api.php",
    params={"action": "parse", "page": "Aang", "prop": "text", "format": "json"},
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=5
)
end = time.time()
print(end - start)
soup = BeautifulSoup(response.json()["parse"]["text"]["*"], "html.parser")
name = soup.title
paragraph = soup.find("p").text

print("name:", name)
print("about:", paragraph)

import json

data = {
    "name": name,
    "about": paragraph
}

with open("aang.json", "w") as f:
    json.dump(data, f, indent=4)

print("Save to aang.json")
