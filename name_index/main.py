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


def index(name_list, stored_name_list):
    no_dupe_list = []
    res = not bool(name_list)
    if res == False:  # if the new name list is empty
        # loop through both list and check if a name from name list is in there
        x = 0
        while x < len(name_list):
            if name_list[x] not in stored_name_list:
                no_dupe_list.append(name_list[x])
            x += 1
    whole_list = stored_name_list + no_dupe_list
    complete_list = []
    for i in whole_list:
        if i not in complete_list:
            complete_list.append(i)
    if res == False:
        dictionary = {'Names': complete_list}
        json_object = json.dumps(dictionary, indent=4)
        with open('data.json', 'w') as outfile:
            outfile.write(json_object)
            print('wrote')
            time.sleep(.5)
    return


def name(list_items, item_length):
    name_list = []
    stored_name_list = []
    x = 0
    while x < item_length:
        items_in_index = list_items[x]
        item_base = items_in_index['typeLine']
        item_name = items_in_index['name']
        name_list.append(item_base)
        x += 1
    with open('data.json') as json_file:
        data = json.load(json_file)
        for name in data['Names']:
            stored_name_list.append(name)
    index(name_list=name_list, stored_name_list=stored_name_list)
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
            list_items = list_index['items']
            # gets length of the item data list
            item_length = len(list_items)
            # print(item_length)
            # loops through the item list
            name(list_items=list_items, item_length=item_length)
            x += 1
        # writes next change id to the file so it can be on the current shard
        with open('next_change_id.txt', 'w') as file:
            file.write(next_change_id)
