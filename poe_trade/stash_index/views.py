from django.shortcuts import render
from configparser import ConfigParser
import pymongo
from pymongo import MongoClient
import pprint
import requests
import json
import time
import random
import re
from Atlas_Connection import Atlas_Connect
# Create your views here.


def stash_index(request):
    context = {}
    cluster = MongoClient(Atlas_Connect)
    Itemdb = cluster["POE_DOCS"]
    currencyCollection = Itemdb["Currency"]
    cardsCollection = Itemdb["Cards"]
    accessoriesCollection = Itemdb["accessories"]
    gemsCollection = Itemdb["gems"]
    jewelsCollection = Itemdb["Jewels"]
    mapsCollection = Itemdb["Maps"]
    weaponsCollection = Itemdb["weapons"]
    armourCollection = Itemdb["armour"]
    flaskCollection = Itemdb["flasks"]

    collectionList = ['cardsCollection', 'currencyCollection', 'jewelsCollection',
                      'accessoriesCollection', 'armourCollection', 'gemsCollection', 'weaponsCollection', 'mapsCollection', 'flaskCollection']
    listLen = len(collectionList)
    currency_list = []
    cards_list = []
    jewels_list = []
    accessories_list = []
    armour_list = []
    gems_list = []
    weapons_list = []
    maps_list = []
    flask_list = []
    for doc in currencyCollection.find():
        currency_list.append(doc)
        # x = 0
        # while x < listLen:
        #     collection_1 = collectionList[x]
        #     for document in collection_1.find():
        #         collection_1.append(document)
        #     x += 1
    context['test'] = "this is a test"
    context['currency'] = currency_list
    context['cards'] = cardsCollection
    context['jewels'] = jewelsCollection
    context['accessories'] = accessoriesCollection
    context['armour'] = armourCollection
    context['gems'] = gemsCollection
    context['weapons'] = weaponsCollection
    context['maps'] = mapsCollection
    context['flasks'] = flaskCollection
    return render(request, 'stash_index.html', context)
