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


class genView(View):

    def get(self, request, type):
        modular_templates = {
            'about': 'about.html',
            'formsub': 'forsub.html',
        }
        return render(request, modular_templates[type], context)


def home(request):
    return render(request, 'home.html', context)


def allview(request):
    return render(request, 'allview.html', context)


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
        form = buyform(request.POST)
        if form.is_valid():
            # Grabs all the form data
            form_dict = {
                # Type Forms
                'type_rarity': form.cleaned_data['type_rarity'],
                'type_category': form.cleaned_data['type_category'],
                # Weapon Forms
                'weapon_damage_max': form.cleaned_data['weapon_damage_max'],
                'weapon_damage_min': form.cleaned_data['weapon_damage_min'],
                'weapon_aps_max': form.cleaned_data['weapon_aps_max'],
                'weapon_aps_min': form.cleaned_data['weapon_aps_min'],
                'weapon_crit_max': form.cleaned_data['weapon_crit_max'],
                'weapon_crit_min': form.cleaned_data['weapon_crit_min'],
                'weapon_dps_max': form.cleaned_data['weapon_dps_max'],
                'weapon_dps_min': form.cleaned_data['weapon_dps_min'],
                'weapon_pdps_max': form.cleaned_data['weapon_pdps_max'],
                'weapon_pdps_min': form.cleaned_data['weapon_pdps_min'],
                'weapon_edps_max': form.cleaned_data['weapon_edps_max'],
                'weapon_edps_min': form.cleaned_data['weapon_edps_min'],
                # Armour Forms
                'armour_max': form.cleaned_data['armour_max'],
                'armour_min': form.cleaned_data['armour_min'],
                'armour_evasion_max': form.cleaned_data['armour_evasion_max'],
                'armour_evasion_min': form.cleaned_data['armour_evasion_min'],
                'armour_es_max': form.cleaned_data['armour_es_max'],
                'armour_es_min': form.cleaned_data['armour_es_min'],
                'armour_ward_max': form.cleaned_data['armour_ward_max'],
                'armour_ward_min': form.cleaned_data['armour_ward_min'],
                'armour_block_max': form.cleaned_data['armour_block_max'],
                'armour_block_min': form.cleaned_data['armour_block_min'],
                # Sockets Forms
                'Item_sockets': form.cleaned_data['Item_sockets'],
                # Requirements Forms
                'Item_req_Lvl': form.cleaned_data['Item_req_Lvl'],
                'Item_req_Strength': form.cleaned_data['Item_req_Strength'],
                'Item_req_Intelligence': form.cleaned_data['Item_req_Intelligence'],
                'Item_req_Dexterity': form.cleaned_data['Item_req_Dexterity'],
                # Map Forms
                'map_tier': form.cleaned_data['map_tier'],
                'map_area_level': form.cleaned_data['map_area_level'],
                'map_region': form.cleaned_data['map_region'],
                'map_blight': form.cleaned_data['map_blight'],
                # Misc Forms
                'Item_level': form.cleaned_data['Item_level'],
                'Is_identified': form.cleaned_data['Is_identified'],
                'misc_fractured': form.cleaned_data['misc_fractured'],
                'misc_corrupted': form.cleaned_data['misc_corrupted'],
                # Trade
                'accountname': form.cleaned_data['accountname'],
                'Item_price_currency': form.cleaned_data['Item_price_currency'],
                'Item_price_quantity': form.cleaned_data['Item_price_quantity'],
                # Mods
                'mods_implicit_1': form.cleaned_data['mods_implicit_1'],
                'mods_implicit_2': form.cleaned_data['mods_implicit_2'],
                'mods_implicit_3': form.cleaned_data['mods_implicit_3'],
                #
                'mods_prefix_1': form.cleaned_data['mods_prefix_1'],
                'mods_prefix_2': form.cleaned_data['mods_prefix_2'],
                'mods_prefix_3': form.cleaned_data['mods_prefix_3'],
                'mods_prefix_4': form.cleaned_data['mods_prefix_4'],
                #
                'mods_suffix_1': form.cleaned_data['mods_suffix_1'],
                'mods_suffix_2': form.cleaned_data['mods_suffix_2'],
                'mods_suffix_3': form.cleaned_data['mods_suffix_3'],
                'mods_suffix_4': form.cleaned_data['mods_suffix_4'],


            }
            # TODO
            # modifiy api_index caclulate dps and add another key for dps
            # Need to make a query for mongo db with all the above form data correlating to how it its in the database
            # inorder to determin if an item is rare modifiy api_index to count number of explicit mods and add a key for rarity
            # OUTLINE
            #            base form dict test very form to see if has a valid imput if it has an imput create another dict with only imputs that need to be searched for
            #            next take that dict and convert it into another dict with keys converted to mongo search query then its as simple as
            #            taking the keys and putting them in the query

            # for x in mycol.find({}, {"_id": 0}):
            #     print(x)
            # ({'qty': {$gt : 50 , $lt : 60}})
            def form_validation(form_dict):
                valid_form_dict = {}
                for key in form_dict:
                    if key == ''

                    elif key == any

                    else:
                        pass
                form_dict
                return
            return render(request, 'search_results.html', {'form': form})
    else:
        form = buyform()
    return render(request, 'search.html', {'form': form})


def formsub(request):
    return render(request, 'forsub.html', context)


main_view_template = []


def main_view(request, type, collection):
    if type == 'sview':
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
