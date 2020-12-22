from django.shortcuts import render
from django.views import View
from configparser import ConfigParser
import pymongo
from pymongo import MongoClient
import pprint
import requests
import json
import time
import random
import re
from django.http import HttpResponse
from Atlas_Connection import Atlas_Connect
cluster = MongoClient(Atlas_Connect)
Itemdb = cluster["POE_DOCS"]

accessoriesCollection = Itemdb["accessories"]
gemsCollection = Itemdb["gems"]
jewelsCollection = Itemdb["Jewels"]
mapsCollection = Itemdb["Maps"]
weaponsCollection = Itemdb["weapons"]
armourCollection = Itemdb["armour"]
flaskCollection = Itemdb["flasks"]

# TODO: finish other functions (dont worrie about the html just create them)
# get home paage working similar to the offical poe trade site


def bootstrap4_index(request):
    return render(request, 'base.html', {})


def home(request):
    context = {}
    return render(request, 'home.html', context)


def currencyView(request):  # Gets all currency data from the db and sends it to frontend
    context = {}
    currencyCollection = Itemdb["Currency"]
    currency_raw_post = []
    processed_data = []
    for doc in currencyCollection.find():
        currency_raw_post.append(doc)
    data_list = ['icon', 'accountName',
                 'typeLine', 'stackSize', 'note', 'ilvl', 'stashname', 'stashid', 'x', 'y']
    x = 0

    while x < len(currency_raw_post):
        single_post = currency_raw_post[x]
        post_data = {}
        for key in data_list:
            try:
                post_data[key] = single_post[key]
            except KeyError:
                pass
        processed_data.append(post_data)

        x += 1

    context['data'] = processed_data
    return render(request, 'currency_view.html', context)

#
# def cardView(request):
#     context = {}
#     cardsCollection = Itemdb["Cards"]
#     card_post_list = []
#     for doc in cardsCollection.find():
#         card_post_list.append(doc)
#     context['cardPost'] = card_post_list
#     return render(request, 'card_view.html', context)
