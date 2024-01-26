import requests
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, Flask!, we are live'

@app.route('/test', methods=['POST'])
def handle_request():
    data = request.json
    print('Received data:', data)
    # Process the data as needed
    return 'Data received successfully'

@app.route('/search', methods=['POST'])
@cross_origin()
def fetch_item_data():
    data = request.json
    heroID = data.get('selectedHeroId')
    rarityID = data.get('selectedRarityId')
    print

    url_template = "https://steamcommunity.com/market/search/render/?query=appid%3A570&start=0&count=100&norender=1&category_570_Rarity[]=tag_Rarity_{rarityID}&category_570_Hero[]=tag_npc_dota_hero_{heroID}"
    url = url_template.format(heroID=heroID, rarityID=rarityID)

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

    return item_list




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
