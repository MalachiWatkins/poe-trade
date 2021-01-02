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


def name(list_items, item_length):
    cached_results = []
    x = 0
    while x < item_length:
        items_in_index = list_items[x]
        item_name = items_in_index['typeLine']

        x += 1
    return


# i have a headace and wanna die
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
    x = 0
    while x < list_length:
        # loops trough the stash data list
        list_index = json_data[x]
        # filters out anything but the league you are wanting data from
        # this can be anything before items in the json data or nothing at all it just makes the data alot smaller
        # if list_index['league'] == 'Heist':
        stashname = list_index['stash']
        list_items = list_index['items']
        item_length = len(list_items)
        name(list_items=list_items, item_length=item_length)
