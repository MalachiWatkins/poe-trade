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
accessoriesCollection = Itemdb["Accessories"]
gemsCollection = Itemdb["Gems"]
jewelsCollection = Itemdb["Jewels"]
mapsCollection = Itemdb["Maps"]
weaponsCollection = Itemdb["Weapons"]
armourCollection = Itemdb["Armour"]
flaskCollection = Itemdb["Flasks"]
context = {}
link_list_parsed = []
properies_list = []
requirements_list = []
# get home paage working similar to the offical poe trade site


def socket_parsing(key, single_post):
    # gets socket data and removes the attr field
    raw_socket_data = []
    single_socket_post = single_post[key]
    for socket_group in single_socket_post:
        single_socket_post = [socket_group['group'],
                              socket_group['sColour']]
        raw_socket_data.append(single_socket_post)
    # socket link list
    link_0 = []
    link_1 = []
    link_2 = []
    link_3 = []
    link_4 = []
    link_5 = []
    x = 0
    while x < len(raw_socket_data):
        single_socket_data = raw_socket_data[x]
        socket_groups = single_socket_data[0]
        socket_colour = single_socket_data[1]
        dict = {
            0: link_0,
            1: link_1,
            2: link_2,
            3: link_3,
            4: link_4,
            5: link_5
        }
        for link_key in dict:
            if link_key == socket_groups:
                dict[link_key].append(socket_colour)
        global link_list_parsed
        link_list_parsed = [link_0, link_1, link_2, link_3, link_4, link_5]
        x += 1

    return


def properties_parsing(key, single_post):
    single_property_post = single_post[key]
    raw_prop_data = []
    master_list = []
    x = 0
    while x < len(single_property_post):
        single_prop = single_property_post[x]
        name = single_prop['name']
        values = single_prop['values']
        if values:
            values = values[0]
            values = values[0]
            parsed_data = name + ': ' + values
            print(parsed_data)
            master_list.append(parsed_data)

        x += 1
        global properies_list
        properies_list = master_list
    return


def requirements_parsing(key, single_post):
    single_requirements_post = single_post[key]
    raw_requirements_data = []
    master_list = []
    x = 0
    while x < len(single_requirements_post):
        single_requirements = single_requirements_post[x]
        name = single_requirements['name']
        values = single_requirements['values']
        if values:
            values = values[0]
            values = values[0]
            parsed_data = name + ': ' + values
            master_list.append(parsed_data)

        x += 1
        global requirements_list
        requirements_list = master_list
    return


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
                if key == 'properties':
                    properties_parsing(key=key, single_post=single_post)
                    post_data[key] = properies_list

                elif key == 'sockets':
                    socket_parsing(key=key, single_post=single_post)
                    post_data[key] = link_list_parsed
                    # print(link_list_parsed)
                elif key == 'requirements':
                    requirements_parsing(key=key, single_post=single_post)
                    post_data[key] = requirements_list

                else:
                    post_data[key] = single_post[key]
            except KeyError:
                pass
        processed_data.append(post_data)
        x += 1
    context['data'] = processed_data
    return


def main_view(request):
    url = str(request.get_full_path())
    index_collection_dict = {  # feel like there is a better way to do this but i did this in 30 min and i have to go to work
        '/currency': currencyCollection,
        '/cards': cardsCollection,
        '/jewel': jewelsCollection,
        '/map': mapsCollection,
        '/accessories': accessoriesCollection,
        '/armour': armourCollection,
        '/flask': flaskCollection,
        '/gems': gemsCollection,
        '/weapons': weaponsCollection,
    }
    data_processing(type=index_collection_dict[url])
    return render(request, 'view.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)


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


def search(request):

    return render(request, 'save.html', context)


def formsub(request):
    return render(request, 'forsub.html', context)
