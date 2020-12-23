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
currencyCollection = Itemdb["Currency"]
cardsCollection = Itemdb["Cards"]
accessoriesCollection = Itemdb["accessories"]
gemsCollection = Itemdb["gems"]
jewelsCollection = Itemdb["Jewels"]
mapsCollection = Itemdb["Maps"]
weaponsCollection = Itemdb["weapons"]
armourCollection = Itemdb["armour"]
flaskCollection = Itemdb["flasks"]
context = {}
# TODO: finish other functions (dont worrie about the html just create them)
# get home paage working similar to the offical poe trade site


def data_processing(type, data_list):
    global processed_data
    global context
    raw_post = []
    processed_data = []
    for doc in type.find():
        raw_post.append(doc)
    x = 0
    while x < len(raw_post):
        single_post = raw_post[x]
        post_data = {}
        for key in data_list:
            try:
                post_data[key] = single_post[key]
            except KeyError:
                pass
        processed_data.append(post_data)
        x += 1
    context['data'] = processed_data
    return


def bootstrap4_index(request):
    return render(request, 'base.html', {})


def home(request):
    context = {}
    return render(request, 'home.html', context)


def currencyView(request):  # Gets all currency data from the db and sends it to frontend
    currency_datalist = ['icon', 'accountName', 'typeLine',
                         'stackSize', 'note', 'ilvl', 'stashname', 'stashid', 'x', 'y']
    data_processing(type=currencyCollection, data_list=currency_datalist)
    return render(request, 'currency_view.html', context)


def cardView(request):
    card_datalist = ['icon', 'accountName', 'typeLine',
                     'stackSize', 'note', 'ilvl', 'stashname', 'stashid', 'x', 'y']
    data_processing(type=cardsCollection, data_list=card_datalist)
    return render(request, 'card_view.html', context)
