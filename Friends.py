import requests
import json

user_id = 80254
request_data = requests.get("https://friends.roblox.com/v1/users/%d/friends/count" % user_id)
json_data = None
friends_list = []
tmp_list = []
if request_data.status_code == 200:
    json_data = json.loads(request_data.text)
    tmp_list.append(json_data["count"])
else:
    tmp_list.append(None)
request_data = requests.get("https://friends.roblox.com/v1/users/%d/followers/count" % user_id)
if request_data.status_code == 200:
    json_data = json.loads(request_data.text)
    tmp_list.append(json_data["count"])
else:
    tmp_list.append(None)
request_data = requests.get("https://friends.roblox.com/v1/users/%d/followings/count" % user_id)
if request_data.status_code == 200:
    json_data = json.loads(request_data.text)
    tmp_list.append(json_data["count"])
else:
    tmp_list.append(None)
friends_list.append(tmp_list)
print(friends_list)
