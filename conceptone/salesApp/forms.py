from django import forms
from datetime import datetime
from salesApp.models import (SaleOrder,
                                SaleOrderItem,
                                SaleInvoice,
                                SaleInvoiceItems,
)

class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = ('so_number','so_ponumber','so_date','so_customer','so_amount',
                    'so_tax_amount')

class SaleInvoiceForm(forms.ModelForm):
    class Meta:
        model = SaleInvoice
        fields = ('so_number','si_number','si_date','si_customer','si_project',)
        widgets = {
                    'so_number':forms.Select(attrs={'class':'form-control'}),
                    'si_number':forms.TextInput(attrs={'class':'form-control'}),
                    'si_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                    'si_customer':forms.Select(attrs={'class':'form-control'}),
                    'si_project':forms.Select(attrs={'class':'form-control'}),
                    }
