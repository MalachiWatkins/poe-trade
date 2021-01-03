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
import pdb
# pdb.set_trace()
# use wirte mode and load the json bedore hand
# check if the new name is in the json if it is pass if not append and overwrite json with the new dict


def name(list_items, item_length):
    name_list = []
    x = 0
    while x < item_length:
        items_in_index = list_items[x]
        item_base = items_in_index['typeLine']
        item_name = items_in_index['name']
        name_list.append(item_base)

        x += 1

    res = not bool(name_list)
    if res == False:
        dictionary = {'Names': name_list}
        json_object = json.dumps(dictionary, indent=4)
        with open('data.json', 'a') as outfile:
            outfile.write(json_object)
    return


while True:  # loops infinitely
    # stops for 600 milleseconds so app doest get rate limited
    time.sleep(.600)
    # opens txt file and reads change id
    with open("next_change_id.txt") as file:
        change_id = file.read()
        # api response with the change id
        response = requests.get(
            "http://www.pathofexile.com/api/public-stash-tabs?id=" + change_id)
        file.close()
        # reads the response and formats as json
        json_response = response.json()
        # gets the next change id
        next_change_id = json_response['next_change_id']
        # if the next change id is the same as the current if moves on so the app doesnt process the same data
        if next_change_id == change_id:
            continue
        # gets all the stash tab data from api response
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
            # grabs all the item data form the stashes in that what ever filter you set
            acc_name = list_index['accountName']
            list_items = list_index['items']
            stash_id = list_index['id']
            stash_name = list_index['stash']
            # gets length of the item data list
            item_length = len(list_items)
            # loops through the item list
            name(list_items=list_items, item_length=item_length)
            x += 1
        # writes next change id to the file so it can be on the current shard
        with open('next_change_id.txt', 'w') as file:
            file.write(next_change_id)
