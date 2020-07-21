from django import forms
from saleordersApp.models import (
                                SaleOrder,
                                SaleOrderItem
                                )
class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = (
                'so_number','supplier','so_date',
                'buyer','buyer_po_number','buyer_po_date',
                'project',
                )
        widgets = {
                'so_number':forms.TextInput(attrs={'class':'form-control'}),
                'supplier':forms.Select(attrs={'class':'form-control'}),
                'so_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                'buyer':forms.Select(attrs={'class':'form-control'}),
                'buyer_po_number':forms.TextInput(attrs={'class':'form-control'}),
                'buyer_po_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                'project':forms.Select(attrs={'class':'form-control'}),
        }

class SaleOrderItemForm(forms.ModelForm):
    class Meta:
        model = SaleOrderItem
        fields = (
                'item',
                'tax',
                'order_quantity',
                'sale_price',
        )
        widgets = {
                'item':forms.Select(attrs={'class':'form-control'}),
                'tax':forms.Select(attrs={'class':'form-control'}),
                'order_quantity':forms.TextInput(attrs={'class':'form-control'}),
                'sale_price':forms.TextInput(attrs={'class':'form-control'}),
        }
