import os
import json

if not os.path.exists("Photos"):
    os.mkdir("Photos")
if not os.path.exists("data/Photos"):
    os.mkdir("data/Photos")

if not os.path.isfile('data/bank.json'):
    #open("data/bank.json", "w").close()
    with open('data/bank.json',"w") as f:
        f.write("{\n}")
        f.write("{\n}")

if not os.path.isfile('data/settings.json'):
    with open('data/settings.json',"w") as f:
        with open("data/global_settings.json","r") as g:
            json.dump(json.load(g), f)