**Avatar the Last Airbender (Aang Wiki Fandom)**
Wiki Site: https://avatar.fandom.com/wiki/Aang
Wiki Site Robots.txt: https://avatar.fandom.com/robots.txt

**Why this Wiki?**
The Avatar: The Last Airbender has been one of my favorite series and is a beloved show loved by many. The premise of the show follows a fictional world where there are different types of elemental benders associated with their respective nations
which include the water, fire, earth, and air nations. These nations had conflicts and power imbalances, which led to the fire nation attack and taking over all other nations, destroying the air nation and their people in effort to destroy the avatar which 
is Aang. Aang was born with all the powers of water, fire, earth, and air, and once one avatar dies, these powers are succeeded by another, and in this case, it's Aang. The series has various cultural references referenicng various martial arts, clothing, traditions,
and social dynamics. Although Avatar the Last Airbender may seen like a light-hearted show, it's animation and storytelling tells a richer story about diverse cultural customs and narritives. 

**Why is this Wiki useful/interesting to researchers?**
This wiki may be interesting to researchers who are investigating how different cartoons or shows represent Asian culture in various of ways. There are many shows and movies out there that represent asian cultures, but some do a better interpretation than others. 
Being able to scrap this data about each Avatar the Last Airbender character can give researchers a better understanding of how these charater reflect their own nation in their character style, background, and fighting style. 

**My Process**
Throughout this scraping process I actaully ran into an issue as fandom wikis implemented a greater anti-bot protection that provented me being able to scrap any data even the name of the charater and their description. After receiving some assistance from professor I was able to scrap information about the main charater Aang on the wikimedia API endpoint instead.

**Code**
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
