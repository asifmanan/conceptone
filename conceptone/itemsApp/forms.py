from django import forms
from datetime import datetime
from itemsApp.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_code',
                    'item_description',
                    'item_uom',
                    'item_price',
                    'item_type',
                    'item_sub_type',)
        widgets = {
                'item_code':forms.TextInput(attrs={'class':'form-control'}),
                'item_description':forms.TextInput(attrs={'class':'form-control'}),
                'item_uom':forms.TextInput(attrs={'class':'form-control'}),
                'item_price':forms.TextInput(attrs={'class':'form-control'}),
                'item_type':forms.Select(attrs={'class':'form-control'}),
                'item_sub_type':forms.Select(attrs={'class':'form-control'}),
        }

class ItemSearchForm(forms.Form):
    item_code = forms.CharField(label='Item code', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    item_description = forms.CharField(label='Item description', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    item_type = forms.CharField(label='Item type', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    item_sub_type = forms.CharField(label='Item sub type', max_length=60, required=False, widget=forms.TextInput(attrs={'class':'form-control search_field'}))
