import requests
import json

user_id = 80254
request_data = requests.get("https://avatar.roblox.com/v1/users/%d/currently-wearing" % user_id)
json_data = None
outfits_list = []
if request_data.status_code == 200:
    json_data = json.loads(request_data.text)
    outfits_list.append(json_data["assetIds"])
print(outfits_list)
