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


def data_processing(type):
    global context
    data_list = ['stashid', 'stashid', 'accountName', 'icon', 'name', 'stackSize', 'identified', 'descrText', 'ilvl',
                 'explicitMods', 'implicitMods', 'note', 'baseType', 'typeLine', 'flavourText', 'x', 'y', 'corrupted', 'properties', 'sockets', 'influences', 'requirements']
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
    data_processing(type=currencyCollection)
    return render(request, 'currency_view.html', context)


def cardView(request):
    data_processing(type=cardsCollection)
    return render(request, 'card_view.html', context)


def jewelsView(request):
    data_processing(type=jewelsCollection)
    return render(request, 'jewels_view.html', context)


def mapsView(request):
    data_processing(type=mapsCollection)
    return render(request, 'map_view.html', context)


def accessoriesView(request):
    data_processing(type=accessoriesCollection)
    return render(request, 'accessories_view.html', context)


def armourView(request):
    data_processing(type=armourCollection)
    return render(request, 'armour_view.html', context)


def flaskView(request):
    data_processing(type=flaskCollection)
    return render(request, 'flask_view.html', context)


def gemsView(request):
    data_processing(type=gemsCollection)
    return render(request, 'gems_view.html', context)


def weaponsView(request):
    data_processing(type=weaponsCollection)
    return render(request, 'weapons_view.html', context)
