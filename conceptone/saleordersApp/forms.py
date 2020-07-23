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
                'item':forms.Select(attrs={'class':'form-control item-input'}),
                'tax':forms.Select(attrs={'class':'form-control tax-input'}),
                'order_quantity':forms.TextInput(attrs={'class':'form-control order-quantity-input'}),
                'sale_price':forms.TextInput(attrs={'class':'form-control sale-price-input'}),
        }

class SaleOrderSearchForm(forms.Form):
    so_number = forms.CharField(label='SO Number', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control search_field'}))
    buyer = forms.CharField(label='Buyer', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control search_field'}))
    buyer_po_number = forms.CharField(label='Buyer PO No.', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control search_field'}))
    buyer_po_date = forms.DateField(label='Buyer PO Date', widget=forms.DateInput(attrs={'type':'date','class':'form-control form-control search_field'}))
