import requests
import json

RIOT_API_KEY = "********************"
region = "na1"

riot_url = f"https://{region}.api.riotgames.com/lol/platform/v3/champion-rotations"

headers = {
    "X-Riot-Token": RIOT_API_KEY,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com"
}

response = requests.get(riot_url, headers=headers)

riot_data = response.json()
print(json.dumps(riot_data, indent=2))

with open("riot_summoner.json", "w") as f:
    json.dump(riot_data, f, indent=2)


ddragon_url = "https://ddragon.leagueoflegends.com/cdn/13.17.1/data/en_US/champion.json"
champ_data = requests.get(ddragon_url).json()

id_to_name = {int(info["key"]): info["name"] for info in champ_data["data"].values()}

free_champ_ids = riot_data["freeChampionIds"]
free_champ_names = [id_to_name[i] for i in free_champ_ids]

print("Free Champion Rotation:", free_champ_names)

EUROPEANA_API_KEY = "******"
search_item = "fallen angel"

url = f"https://api.europeana.eu/record/v2/search.json?query={search_item}&wskey={EUROPEANA_API_KEY}"

response = requests.get(url)
data = response.json()

print(f"\nEuropeana search results for '{search_item}':")

with open(f"europeana_{search_item}.json", "w") as f:
    json.dump(data['items'], f, indent=2)

print(f"\nAll Europeana items saved to 'europeana_{search_item}.json'")

print("Champion: Aatrox")
print(f"Related Europeana items for 'fallen angel':")
for item in data.get('items', [])[:4]:
    title = item.get('title', [''])[0].strip()
    year = item.get('year', ['N/A'])[0]
    link = item.get('edmIsShownAt', [''])[0]
    print(f"{title} ({year}) -> {link}")
