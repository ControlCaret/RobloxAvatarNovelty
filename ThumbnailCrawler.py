import os
import json
import requests

apiName: str = "avatar-headshot"
#userList: list[int] = []
imageSize: str = "48x48"
imageFormat: str = "Png"
isCircular: str = "false"
folderName: str = "Thumbnails"

if not os.path.exists(folderName):
    os.makedirs(folderName)

for i in range(0, 10):
    userList: list[int] = [j for j in range(i * 100, (i + 1) * 100)]
    userIds: str = ','.join(str(i) for i in userList)

    requestData = requests.get("https://thumbnails.roblox.com/v1/users/" + apiName
                               + "?userIds=" + userIds
                               + "&size=" + imageSize
                               + "&format=" + imageFormat
                               + "&isCircular=" + isCircular)

    if requestData.status_code == 200:
        jsonData = json.loads(requestData.text)
        for user in jsonData["data"]:
            print(user["targetId"])
            print(user["state"])
            print(user["imageUrl"])
            if(user["state"] == "Blocked"):
                continue
            with open(folderName + "/" + str(user["targetId"]) + "." + imageFormat.lower(), "wb") as f:
                f.write(requests.get(user["imageUrl"]).content)

# TODO: Add delay for API limits
