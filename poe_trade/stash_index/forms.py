from django import forms


class buyform(forms.Form):
    custom_id = forms.CharField(label='Custom ID', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Custom Id'}))

    item_type = forms.CharField(label='Item name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Type of item'}))

    item_name = forms.CharField(label='Item name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Type of item'}))

    Item_price = forms.CharField(label='Item name', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Price of the item'}))
