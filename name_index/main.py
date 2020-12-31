from connect import Atlas_Connect
import time
from configparser import ConfigParser
import pymongo
from pymongo import MongoClient
import pprint
import requests
import json
import time
import random
import re
while True:
    with open("next_change_id.txt") as file:
        change_id = file.read()
    response = requests.get(
        "http://www.pathofexile.com/api/public-stash-tabs?id=" + change_id)
    file.close()
    json_response = response.json()
    # gets the next change id
    next_change_id = json_response['next_change_id']
    # if the next change id is the same as the current if moves on so the app doesnt process the same data
    if next_change_id == change_id:
        continue
    json_data = json_response["stashes"]
    list_length = len(json_data)
    # opens file and writes next change id to the file
    f = open("next_change_id.txt", "w")
    f.write(next_change_id)
    f.close()
