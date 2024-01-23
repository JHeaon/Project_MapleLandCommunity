import requests
import pprint
import json

responses = requests.get("https://maplestory.io/api/gms/62/mob/6130101/name")
pprint.pprint(responses.text)
