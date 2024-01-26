import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!, we are live'

@app.route('/dota')
def hello_dota():
    return 'this is the dota route'

@app.route('/search')
def fetch_item_data():
    url = "https://steamcommunity.com/market/search/render/?query=appid%3A570&start=0&count=100&norender=1&category_570_Rarity[]=tag_Rarity_Immortal&category_570_Hero[]=tag_npc_dota_hero_alchemist"

    response = requests.get(url)

    data = response.json()

    item_list = []

    for item in data["results"]:
        asset_description = item.get("asset_description", {})
        icon_url = asset_description.get("icon_url", "")

        item_details = {
            "name": item.get("name", ""),
            "sell_listings": item.get("sell_listings", ""),
            "sell_price_text": item.get("sell_price_text", ""),
            "icon_url": icon_url
        }
        item_list.append(item_details)

    # Writing item details to a text file
    with open("items.txt", "w") as file:
        for item in item_list:
            file.write(f"Name: {item['name']}\n")
            file.write(f"Sell Listings: {item['sell_listings']}\n")
            file.write(f"Sell Price Text: {item['sell_price_text']}\n")
            file.write(f"Icon Url: {item['icon_url']}\n")
            file.write("\n")

    return "Item data fetched and written to items.txt"




if __name__ == '__main__':
    app.run(debug=True)

#     general link here:
#   https://steamcommunity.com/market/search/render/?query=appid%3A570&start=0&count=100&norender=1&category_570_Rarity%5B%5D=tag_Rarity_Immortal&category_570_Hero%5B%5D=tag_npc_dota_hero_axe
#  tested with changing params on hero tag, so its uniform, rarity is the same
#   just pass hero input data, probably with a map of heros from a dropdown,
#   and rarity of items needed, probably key by price data low < high
#   let the user sort by either one
#
#   item icons are structured with this link:
#   https://community.cloudflare.steamstatic.com/economy/image/{data}
#   with data being pulled directly from {asset_description} and then the child {icon_url}
#
#
#
#
#
