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
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import buyform
from django.http import HttpResponseRedirect

cluster = MongoClient(Atlas_Connect)
Itemdb = cluster["POE_DOCS"]
buyorderCollection = Itemdb["buyorder"]
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
# get home paage working similar to the offical poe trade site
# create a buy order process with an app that alerts you when what you wantis in stock
# create a place where you can downlod the app
# 2345612344 currency Exalted orb 120 chaos
# taking a break for a day need sleep after work


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


@ensure_csrf_cookie
def buyorder(request):
    if request.method == 'POST':
        form = buyform(request.POST)
        if form.is_valid():
            post = {'custom_id': form.cleaned_data['custom_id'],
                    'item_type': form.cleaned_data['item_type'], 'item_name': form.cleaned_data['item_name'], 'item_price': form.cleaned_data['Item_price'], }
            buyorderCollection.insert_one(post)
            print('incert one')
            return HttpResponseRedirect('/formsub')
    else:
        form = buyform()
    return render(request, 'buy_order.html', {'form': form})


def formsub(request):
    return render(request, 'forsub.html', context)
