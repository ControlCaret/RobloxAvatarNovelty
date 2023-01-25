import os
import json
import requests

# Change this to the type of thumbnail you want to get
# Options: avatar, avatar-bust, avatar-headshot
apiName: str = "avatar-headshot"

# Change this to the user IDs you want to get the thumbnail of
# Max 100 IDs
userList: list[int] = [i for i in range(1, 101)]

# Change this to the size of the thumbnail you want to get
# Options: 48x48, 50x50, 60x60, 75x75, 100x100, 110x110, 150x150, 180x180, 352x352, 420x420, 720x720
imageSize: str = "48x48"

# Change this to the format of the thumbnail you want to get
# Options: Png, Jpeg
imageFormat:str = "Png"

# Change this to whether or not you want the thumbnail to be circular
# Options: true, false
isCircular: str = "false"

# Change this to the folder name you want to save the thumbnails in
folderName: str = "Thumbnails"

# Do not change anything below this line
userIds: str = ','.join(str(i) for i in userList)

# Create the folder if it doesn't exist
if not os.path.exists(folderName):
    os.makedirs(folderName)

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
        with open(folderName + "/" + str(user["targetId"]) + "." + imageFormat.lower(), "wb") as f:
            f.write(requests.get(user["imageUrl"]).content)
