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


cluster = MongoClient(Atlas_Connect)
Itemdb = cluster["POE_DOCS"]
cardsCollection = Itemdb["Cards"]
accessoriesCollection = Itemdb["accessories"]
gemsCollection = Itemdb["gems"]
jewelsCollection = Itemdb["Jewels"]
mapsCollection = Itemdb["Maps"]
weaponsCollection = Itemdb["weapons"]
armourCollection = Itemdb["armour"]
flaskCollection = Itemdb["flasks"]


def bootstrap4_index(request):
    return render(request, 'base.html', {})


def home(request):
    context = {}
    return render(request, 'home.html', context)


def currencyView(request):
    context = {}
    currencyCollection = Itemdb["Currency"]

    currency_post_list = []
    for doc in currencyCollection.find():
        currency_post_list.append(doc)
    currency_len = len(currency_post_list)
    currency_post = []
    x = 0
    while x < currency_len:
        currencypost = currency_post_list[x]
        currency_post.append(currencypost)
        x += 1
    context['currencyPost'] = currency_post

    return render(request, 'currency_view.html', context)
