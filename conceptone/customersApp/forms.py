from django import forms
from customersApp.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_code','customer_name','customer_address',
                    'customer_city','customer_phone','customer_fax',
                    'customer_email','customer_ntn_number',)
        widgets = {
                'customer_code':forms.TextInput(attrs={'class':'form-control'}),
                'customer_name':forms.TextInput(attrs={'class':'form-control'}),
                'customer_address':forms.TextInput(attrs={'class':'form-control'}),
                'customer_city':forms.TextInput(attrs={'class':'form-control'}),
                'customer_phone':forms.TextInput(attrs={'class':'form-control'}),
                'customer_fax':forms.TextInput(attrs={'class':'form-control'}),
                'customer_email':forms.TextInput(attrs={'class':'form-control'}),
                'customer_ntn_number':forms.TextInput(attrs={'class':'form-control'}),
        }

class CustomerSearchForm(forms.Form):
    customer_name = forms.CharField(label='Customer name', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    customer_code = forms.CharField(label='Customer code', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    customer_ntn_number = forms.CharField(label='NTN number', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control search_field'}))
    customer_phone = forms.CharField(label='Phone number', max_length=60, required=False, widget=forms.TextInput(attrs={'class':'form-control search_field'}))
