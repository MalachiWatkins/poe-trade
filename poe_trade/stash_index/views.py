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
# get home paage working similar to the offical poe trade site


def data_processing(type):
    global context
    data_list = ['stashid', 'stashid', 'accountName', 'icon', 'name', 'stackSize', 'identified', 'descrText', 'ilvl',
                 'explicitMods', 'implicitMods', 'note', 'baseType', 'typeLine', 'flavourText', 'x', 'y', 'corrupted', 'properties', 'sockets', 'influences', 'requirements']
    Socket_list = ['group', 'sColour']
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
                if key == 'sockets':
                    item_socket_list = []
                    s_post = single_post[key]
                    for socket_group in s_post:
                        s_list = [socket_group['group'],
                                  socket_group['sColour']]
                        item_socket_list.append(s_list)
                    # item socket list
                    socket_list_0 = []
                    socket_list_1 = []
                    socket_list_2 = []
                    socket_list_3 = []
                    socket_list_4 = []
                    socket_list_5 = []
                    y = 0
                    while y < len(item_socket_list):
                        socket = item_socket_list[y]
                        socket_groups = socket[0]
                        socket_colour = socket[1]
                        if socket_groups == 0:
                            socket_list_0.append(socket_colour)
                        elif socket_groups == 1:
                            socket_list_1.append(socket_colour)
                        elif socket_groups == 2:
                            socket_list_2.append(socket_colour)
                        elif socket_groups == 3:
                            socket_list_3.append(socket_colour)
                        elif socket_groups == 4:
                            socket_list_4.append(socket_colour)
                        elif socket_groups == 5:
                            socket_list_5.append(socket_colour)
                        else:
                            pass
                        y += 1
                    socket_list_partial = [
                        socket_list_0, socket_list_1, socket_list_2, socket_list_3, socket_list_4, socket_list_5]
                    # socket_list_parsed = [len(socket_list_0), len(socket_list_1), len(
                    #     socket_list_2), len(socket_list_3), len(socket_list_4), len(socket_list_5)]
                    # print(socket_list_partial[0] + '~~~~~' + socket_list_partial[1] + socket_list_partial[2] +
                    #       socket_list_partial[3] + socket_list_partial[4] + socket_list_partial[5])
                    # print('~~~~~~~~~~~~~~~~~~~~~')

                    post_data[key] = socket_list_partial
                else:
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
