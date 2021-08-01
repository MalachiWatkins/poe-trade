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
    ('Rare', 'Rare'),
    ('Rare', 'Rare'),
    ('Rare', 'Rare'),
    ('Rare', 'Rare'),
    ('Rare', 'Rare'),
)
item_category = (
    ('Rare', 'Any'),
    ('Rare', 'Rare'),
    ('Rare', 'Rare'),
    ('Rare', 'Rare'),
    ('Rare', 'Rare'),
)
identified = (
    ('any', 'any'),
    ('ture', 'ture'),
    ('False', 'False'),
)


class buyform(forms.Form):
    custom_id = forms.CharField(label='Custom ID', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Custom Id'}))

    collection_type = forms.CharField(label='What kind of item is this?',
                                      widget=forms.Select(choices=COLLECTION_CHOICES))

    ############################################
    ################Type Filter###################
    ############################################

    Item_rarity = forms.CharField(
        widget=forms.Select(choices=rarity_choices))
    Item_category = forms.CharField(
        widget=forms.Select(choices=item_category))
    ############################################
    ############# Weapon Filter ##################
    ############################################

    ############################################
    ############### Armour #####################
    ############################################

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

    ############################################
    ############## MISC #######################
    ############################################
    Item_level = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': '#'}))
    Item_level.widget.attrs.update(size='2')

    Is_identified = forms.CharField(
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
