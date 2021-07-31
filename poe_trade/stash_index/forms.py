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


class buyform(forms.Form):
    custom_id = forms.CharField(label='Custom ID', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Custom Id'}))

    collection_type = forms.CharField(label='What kind of item is this?',
                                      widget=forms.Select(choices=COLLECTION_CHOICES))

    item_name = forms.CharField(label='Item name', widget=forms.TextInput(
        attrs={'placeholder': 'Name of item'}))

    Item_price_currency = forms.CharField(label='Item Price',
                                          widget=forms.Select(choices=Currency_choice))

    Item_price_quantity = forms.CharField(label='Item name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': '#'}))
    Item_price_quantity.widget.attrs.update(size='2')
    accountname = forms.CharField(label='account name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Account Name'}))

    Is_Identified = forms.CharField(label='', max_length=100, widget=forms.CheckboxInput(
        attrs={'placeholder': 'Is Item Identified'}))

    Item_level = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': '#'}))
    Item_level.widget.attrs.update(size='2')
    # accountname = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    Item_name = forms.CharField(label='iname', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Item Name'}))

    Item_base = forms.CharField(label='ibase', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Item Base'}))
    Item_sockets = forms.CharField(label='isockets', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'EX: B-B-B R-R'}))
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
 # 1
  # 1
   # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1

    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    rarity_choices = (
        ('Rare', 'Rare'),
        ('Rare', 'Rare'),
        ('Rare', 'Rare'),
        ('Rare', 'Rare'),
        ('Rare', 'Rare'),
    )
    Item_category = (
        ('Rare', 'Rare'),
        ('Rare', 'Rare'),
        ('Rare', 'Rare'),
        ('Rare', 'Rare'),
        ('Rare', 'Rare'),
    )
    type_filter = forms.CharField(label='', max_length=100, widget=forms.CheckboxInput(
        attrs={'placeholder': 'Is Item Identified'}))
    Item_rarity = forms.CharField(
        widget=forms.Select(choices=rarity_choices))
    Item_category = forms.CharField(
        widget=forms.Select(choices=Item_category))
