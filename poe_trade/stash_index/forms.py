from django import forms
COLLECTION_CHOICES = (
    ('Currency', 'Currency'),
    ('Cards', 'Cards'),
    ('Accessories', 'Accessories'),
    ('Gems', 'Gems'),
    ('Jewels', 'Jewels'),
    ('Maps', 'Maps'),
    ('Weapons', 'Weapons'),
    ('Armour ', 'Armour'),
)
Currency_choice = (
    ('Alteration', 'Alteration'),
    ('Fusing', 'Fusing'),
    ('Alchemy', 'Alchemy'),
    ('Chaos', 'Chaos'),
    ('GCP', "Gemcutter's Prism"),
    ('Exalted', 'Exalted'),
    ('Chromatic', 'Chromatic'),
    ('Jeweller', ' Jeweller'),
    ('Engineer', 'Engineer'),
    ('Chance', 'Chance'),
    ('Cartographer_Chisel', 'Cartographer Chisel'),
    ('Scouring', 'Scouring'),
    ('Blessed', 'Blessed'),
    ('Regret', 'Regret'),
    ('Regal', 'Regal'),
    ('Divine', 'Divine'),
    ('Vaal', 'Vaal'),
    ('Annulment', 'Annulment'),
    ('Binding', 'Binding'),
    ('Ancient Orb', 'Ancient'),
    ('Horizons Orb', 'Horizons'),
    ('Harbingers_orb', 'Harbingers Orb'),
    ('Wisdom', 'Wisdom'),
    ('Portal Scroll', 'Portal'),
    ('Armour_scraps', 'Armour Scraps'),
    ('Blacksmiths_whetstone', 'Blacksmiths Whetstone'),
    ('Glassblowers_baulble', 'Glassblowers Bauble'),
    ('Transmutation', 'Transmutation'),
    ('Augmentation', 'Augmentation'),
    ('Mirror of Kalandra', 'Mirror'),
    ('Perandus_coin', ' Perandus Coin'),
    ('Rogue_marker', 'Rogue Marker'),
    ('silver_coin', 'Silver Coin'),
)
rarity_choices = (
    ('any', 'Any'),
    ('normal', 'Normal'),
    ('rare', 'Rare'),
    ('unique', 'Unique'),
    ('anynonunique', 'Any Non-Unique'),
)
item_category = (
    ('any', 'Any'),
    ('anyweapon ', 'Any Weapon'),
    ('one_handed_weapon', 'One Handed Weapon'),
    ('one_handed_melee_weapon', 'One Handed Melee Weapon'),
    ('two_handed_melee_weapon', 'Two Handed Melee Weapon'),
    ('bow', 'Bow'),
    ('claw', 'Claw'),
    ('any_dagger', 'Any Dagger'),
    ('base_dagger', ' Base Dagger'),
    ('rune_dagger', 'Rune Dagger'),
    ('one_handed_axe', 'One Handed Axe'),
    ('one_handed_mace', 'One Handed Mace'),
    ('one_handed_sword', 'One Handed Sword'),
    ('scepter', 'Scepter'),
    ('any_staff', 'Any Staff'),
    ('base_staff', 'Base Staff'),
    ('warstaff', 'Warstaff'),
    ('two_handed_axe', 'Two Handed Axe'),
    ('two_handed_mace', 'Two Handed Mace'),
    ('two_handed_sword', 'Two Handed Sword'),
    ('wand', 'Wand'),
    ('any_armour', 'Any Armour'),
    ('body_armour', 'Body Armour'),
    ('boots', 'Boots'),
    ('gloves', 'Gloves'),
    ('helmet', 'Helmet'),
    ('shield', 'Shield'),
    ('quiver', 'Quiver'),
    ('any_accesory', 'Any Accessories'),
    ('amulet', 'Amulet'),
    ('belt', 'Belt'),
    ('ring', 'Ring'),
    ('any_gem', 'Any Gem'),
    ('skill_gem', 'Skill Gem'),
    ('support_gems', 'Support Gems'),
    ('awakened_support_gem', 'Awakened Support Gem'),
    ('any_jewel', 'Any Jewel'),
    ('base_jewel', 'Base Jewel'),
    ('abyss_jewel', 'Abyss Jewel'),
    ('cluster_jewel', 'Cluster Jewel'),
    ('flask', 'Flask'),
    ('map', 'Map'),
    ('map_fragment', 'Map Fragment'),
    ('scarab', 'Scarab'),
    ('watchstone', 'Watchstone'),
    ('prophecy', 'Prophecy'),
    ('divination_card', 'Divination Card'),
    ('any_expedition_logbook', 'Any Expedition Log Book'),
    ('any_currency', 'Any Currency'),
    ('resonator', 'Resonator'),
    ('fossil', 'Fossil'),
    ('incubator', 'Incubator'),
)
identified = (
    ('any', 'any'),
    ('ture', 'ture'),
    ('False', 'False'),
)
map_region_choice = (
    ('any', 'any'),
    ('haewak_hamlset', 'Haewak Hamlet'),
    ('tirns_end', "Tirn's End"),
    ('lex_proxima', 'Lex Proxima'),
    ('lex_ejoris', 'Lex Ejoris'),
    ('new_vastir', 'New Vastir'),
    ('glennach_cairins', 'Glennach Cairins'),
    ('valdos_rest', 'Valdos Rest'),
    ('lira_arthain', 'Lira Arthain'),
)


class buyform(forms.Form):
    custom_id = forms.CharField(label='Custom ID', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Custom Id'}))

    collection_type = forms.CharField(label='What kind of item is this?',
                                      widget=forms.Select(choices=COLLECTION_CHOICES))

    ############################################
    ############### Type Filter ##################
    ############################################
    type_rarity = forms.CharField(
        widget=forms.Select(choices=rarity_choices))
    type_category = forms.CharField(
        widget=forms.Select(choices=item_category))

    ############################################
    ############# Weapon Filter ##################
    ############################################
    # there is prob a bettter way but django forms are confsing
    weapon_damage_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))
    weapon_damage_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    #
    weapon_aps_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    weapon_aps_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))
    #
    weapon_crit_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    weapon_crit_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))
    #
    weapon_dps_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    weapon_dps_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))
    #
    weapon_pdps_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    weapon_pdps_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))
    #
    weapon_edps_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    weapon_edps_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))

    ############################################
    ############### Armour #####################
    ############################################
    armour_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    armour_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))
    #
    armour_evasion_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    armour_evasion_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))
    #
    armour_es_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    armour_es_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))
    #
    armour_ward_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    armour_ward_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))
    #
    armour_block_max = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MAX', 'size': '4'}))
    armour_block_min = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'MIN', 'size': '4'}))

    ############################################
    ############### Sockets #####################
    ############################################
    Item_sockets = forms.CharField(label='isockets', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'EX: B-B-B R-R'}))

    ############################################
    ############# Requirements ###################
    ############################################
    Item_req_Lvl = forms.CharField(label='ireq', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'LVL'}))
    Item_req_Lvl.widget.attrs.update(size='3')
    Item_req_Strength = forms.CharField(label='ireqstr', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'STR'}))
    Item_req_Strength.widget.attrs.update(size='3')
    Item_req_Intelligence = forms.CharField(label='ireqint', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'INT'}))
    Item_req_Intelligence.widget.attrs.update(size='3')
    Item_req_Dexterity = forms.CharField(label='ireqdex', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'DEX'}))
    Item_req_Dexterity.widget.attrs.update(size='3')

    ############################################
    ################ Map ######################
    ############################################
    map_tier = forms.CharField(label='ireqdex', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': ''}))
    map_tier.widget.attrs.update(size='3')
    map_area_level = forms.CharField(label='ireqdex', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': ''}))
    map_area_level.widget.attrs.update(size='3')
    map_region = forms.CharField(
        widget=forms.Select(choices=map_region_choice))
    map_blight = forms.CharField(
        widget=forms.Select(choices=identified))

    ############################################
    ############## MISC #######################
    ############################################
    Item_level = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': '#'}))
    Item_level.widget.attrs.update(size='2')
    Is_identified = forms.CharField(
        widget=forms.Select(choices=identified))
    misc_fractured = forms.CharField(
        widget=forms.Select(choices=identified))
    misc_corrupted = forms.CharField(
        widget=forms.Select(choices=identified))
    ############################################
    ################ Trade ######################
    ############################################
    accountname = forms.CharField(label='account name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Account Name'}))
    Item_price_currency = forms.CharField(label='Item Price',
                                          widget=forms.Select(choices=Currency_choice))

    Item_price_quantity = forms.CharField(label='Item name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': '#'}))
    Item_price_quantity.widget.attrs.update(size='2')
    ############################################
    ################## Mods ####################
    ############################################
    # 4 prefix 4 suffix 3 implicits
 # add when i get home
