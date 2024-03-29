from django import forms
from standardinvoiceApp.models import StandardInvoice, StandardInvoiceItem

class StandardInvoiceForm(forms.ModelForm):
    class Meta:
        model = StandardInvoice
        fields = (
            'company','invoice_number','invoice_date',
            'customer','project',
        )
        widgets = {
            'company':forms.Select(attrs={'class':'form-control'}),
            'invoice_number':forms.TextInput(attrs={'class':'form-control'}),
            'invoice_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'customer':forms.Select(attrs={'class':'form-control'}),
            'project':forms.Select(attrs={'class':'form-control'}),
        }

class StandardInvoiceItemForm(forms.ModelForm):
    class Meta:
        model = StandardInvoiceItem
        fields = (
            'item','quantity','sale_price','tax',
        )
        widgets = {
            'item':forms.Select(attrs={'class':'form-control'}),
            'quantity':forms.TextInput(attrs={'class':'form-control'}),
            'sale_price':forms.TextInput(attrs={'class':'form-control'}),
            'tax':forms.Select(attrs={'class':'form-control'}),
        }

class StandardInvoiceSearchForm(forms.Form):
    invoice_number = forms.CharField(label='Invoice Number', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control search_field'}))
    customer = forms.CharField(label='Customer', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control search_field'}))
    project = forms.CharField(label='Project', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control search_field'}))
    date = forms.DateField(label='Invoice Date', widget=forms.DateInput(attrs={'type':'date','class':'form-control form-control search_field'}))
