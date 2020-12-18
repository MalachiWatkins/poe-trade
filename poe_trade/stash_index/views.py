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


def bootstrap4_index(request):
    return render(request, 'index.html', {})


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
    currency_len = len(currency_list)
    x = 0
    icon_list = []

    while x < currency_len:
        currency_post = currency_list[x]
        currency_icon = currency_post['icon']
        icon_list.append(currency_icon)

        x += 1
    context['currency_icon'] = icon_list
    return render(request, 'stash_index.html', context)
