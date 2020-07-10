from django import forms
from simpleinvoiceApp.models import StandardInvoice, StandardInvoiceItem

class StandardInvoiceForm(forms.ModelForm):
    class Meta:
        model = StandardInvoice
        fields = (
            'invoice_number','invoice_date',
            'customer','project',
        )
        widgets = {
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
