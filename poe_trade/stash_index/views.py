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
from django.http import HttpResponse


cluster = MongoClient(Atlas_Connect)
Itemdb = cluster["POE_DOCS"]
buyorderCollection = Itemdb["buyorder"]
currencyCollection = Itemdb["Currency"]
cardsCollection = Itemdb["Cards"]
accessoriesCollection = Itemdb["Accessories"]
gemsCollection = Itemdb["Gems"]
jewelsCollection = Itemdb["Jewels"]
mapsCollection = Itemdb["Maps"]
weaponsCollection = Itemdb["Weapons"]
armourCollection = Itemdb["Armour"]
flaskCollection = Itemdb["Flasks"]
context = {}
# get home paage working similar to the offical poe trade site


def data_processing(type):
    global context
    data_list = ['stashid', 'stashid', 'accountName', 'icon', 'name', 'stackSize', 'identified', 'descrT`ext', 'ilvl',
                 'explicitMods', 'implicitMods', 'note', 'baseType', 'typeLine', 'flavourText', 'x', 'y', 'corrupted', 'properties', 'sockets', 'influences', 'requirements']
    link = ['group', 'sColour']
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


def home(request):
    return render(request, 'home.html', context)


def allview(request):
    return render(request, 'allview.html', context)


def about(request):

    return render(request, 'about.html', context)


@ ensure_csrf_cookie
def buyorder(request):
    if request.method == 'POST':
        form = buyform(request.POST)
        if form.is_valid():
            post = {'custom_id': form.cleaned_data['custom_id'],
                    'collection_type': form.cleaned_data['collection_type'], 'item_name': form.cleaned_data['item_name'], 'item_price': form.cleaned_data['Item_price'], }
            buyorderCollection.insert_one(post)
            print('incert one')
            return HttpResponseRedirect('/formsub')
    else:
        form = buyform()
    return render(request, 'buy_order.html', {'form': form})


@ ensure_csrf_cookie
def search(request):
    if request.method == 'POST':
        url = str(request.get_full_path())
        print(url)
        form = buyform(request.POST)
        if form.is_valid():
            accname = form.cleaned_data['accountname']
            print(accname)
            return HttpResponseRedirect('/tanks/')
    else:
        form = buyform()
    return render(request, 'search.html', {'form': form})


def formsub(request):
    return render(request, 'forsub.html', context)


main_view_template = []


def main_view(request, type, collection):
    if type == 'yeet':
        main_view_template.append('view.html')
        all_view_list = ['currency', 'cards', 'jewel', 'map',
                         'accessories', 'armour', 'flask', 'gems', 'weapons']
        for key in all_view_list:
            if collection == key:
                # get all of the urls working /view/map/yeet/ /view/cards/yeet/ etcs
                index_collection_dict = {  # feel like there is a better way to do this but i did this in 30 min and i have to go to work
                    'currency': currencyCollection,
                    'cards': cardsCollection,
                    'jewel': jewelsCollection,
                    'map': mapsCollection,
                    'accessories': accessoriesCollection,
                    'armour': armourCollection,
                    'flask': flaskCollection,
                    'gems': gemsCollection,
                    'weapons': weaponsCollection,
                }
                data_processing(type=index_collection_dict[key])
    return render(request, main_view_template[0], context)
