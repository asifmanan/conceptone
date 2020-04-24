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
        fields = (
                    'so_number','so_podate','so_ponumber','so_customer',
                    'so_project',)
        widgets = {
                    'so_number':forms.TextInput(attrs={'class':'form-control'}),
                    'so_podate':forms.DateInput(attrs={'class':'form-control','type':'date','id':'so_podate'}),
                    'so_ponumber':forms.TextInput(attrs={'class':'form-control'}),
                    'so_customer':forms.Select(attrs={'class':'form-control'}),
                    'so_project':forms.Select(attrs={'class':'form-control'}),
                    }

class SaleInvoiceForm(forms.ModelForm):
    class Meta:
        model = SaleInvoice
        fields = ('si_sonumber','si_number','si_date','si_customer','si_project',)
        widgets = {
                    'si_sonumber':forms.Select(attrs={'class':'form-control'}),
                    'si_number':forms.TextInput(attrs={'class':'form-control'}),
                    'si_date':forms.DateInput(attrs={'class':'form-control','type':'date','id':'si_date'}),
                    'si_customer':forms.Select(attrs={'class':'form-control'}),
                    'si_project':forms.Select(attrs={'class':'form-control'}),
                    }

class SaleOrderItemForm(forms.ModelForm):
    class Meta:
        model = SaleOrderItem
        fields = (
                    'sale_order_item','so_quantity','sale_price',
                    'so_tax_rate',
                    )
        widgets = {
                    'sale_order_item':forms.Select(attrs={'class':'form-control'}),
                    'so_quantity':forms.TextInput(attrs={'class':'form-control'}),
                    'sale_price':forms.TextInput(attrs={'class':'form-control'}),
                    'so_tax_rate':forms.Select(attrs={'class':'form-control'}),
        }
