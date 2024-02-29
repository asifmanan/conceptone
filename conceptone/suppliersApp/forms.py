from django import forms
from suppliersApp.models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('supplier_code','supplier_name', 'supplier_address',
                    'supplier_city','supplier_phone', 'supplier_fax',
                    'supplier_email', 'supplier_ntn_number',)
        widgets = {
            'supplier_code':forms.TextInput(attrs={'class':'form-control'}),
            'supplier_name':forms.TextInput(attrs={'class':'form-control'}),
            'supplier_address':forms.TextInput(attrs={'class':'form-control'}),
            'supplier_city':forms.TextInput(attrs={'class':'form-control'}),
            'supplier_phone':forms.TextInput(attrs={'class':'form-control'}),
            'supplier_fax':forms.TextInput(attrs={'class':'form-control'}),
            'supplier_email':forms.TextInput(attrs={'class':'form-control'}),
            'supplier_ntn_number':forms.TextInput(attrs={'class':'form-control'}),
        }

class SupplierSearchForm(forms.Form):
    supplier_name = forms.CharField(label='Supplier name', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    supplier_code = forms.CharField(label='Supplier code', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    supplier_ntn_number = forms.CharField(label='NTN number', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    supplier_phone = forms.CharField(label='Phone number', max_length=60, required=False, widget=forms.TextInput(attrs={'class':'form-control search_field'}))
