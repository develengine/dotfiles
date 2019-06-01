#!/usr/bin/env python3
import json
from os import system

a = { }

with open("/home/engine/.scripts/lstate.json", "r") as f:
    a = json.load(f)

system("setxkbmap -v " + a["lang"])

if a["lang"] == "us":
    a["lang"] = "sk -variant qwerty"
else:
    a["lang"] = "us"

with open("/home/engine/.scripts/lstate.json", "w") as f:
    json.dump(a, f)

