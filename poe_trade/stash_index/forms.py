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


class buyform(forms.Form):
    custom_id = forms.CharField(label='Custom ID', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Custom Id'}))

    collection_type = forms.CharField(label='What kind of item is this?',
                                      widget=forms.Select(choices=COLLECTION_CHOICES))

    item_name = forms.CharField(label='Item name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Name of item'}))

    Item_price = forms.CharField(label='Item name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Price of the item'}))

# class searchform(form.Forms):
#     Account Name = forms.CharField(label='Custom ID', max_length=100, widget=forms.TextInput(
#         attrs={'placeholder': 'Custom Id'}))
