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

    return render(request, 'stash_index.html', context)


def test(request):
    context = {}
    a = 'a'

    return render(request, 'test.html', context)

# setup another function as a test
