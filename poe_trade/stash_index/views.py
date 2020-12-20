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


def currencyView(request):  # Gets all currency data from the db and sends it to frontend
    context = {}
    currencyCollection = Itemdb["Currency"]  # gets currency collection
    currency_post_list = []  # a list to store all the currency related posts
    for doc in currencyCollection.find():  # finds all the currency documents and appends them to a list
        currency_post_list.append(doc)
    # sends the post data to frontend
    context['currencyPost'] = currency_post_list
    return render(request, 'currency_view.html', context)


def cardView(request):
    context = {}
    cardsCollection = Itemdb["Cards"]
    card_post_list = []
    for doc in cardsCollection.find():
        card_post_list.append(doc)
    context['cardPost'] = card_post_list
    return render(request, 'card_view.html', context)
