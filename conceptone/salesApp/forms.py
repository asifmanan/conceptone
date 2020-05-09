from django import forms
from datetime import datetime
from salesApp.models import (SaleOrder,
                                SaleOrderItem,
                                SaleInvoice,
                                SaleInvoiceItem,
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

class SaleInvoiceSoForm(forms.ModelForm):
    class Meta:
        model = SaleInvoice
        fields = ('si_sonumber',)
        widgets = {
                    'si_sonumber':forms.Select(attrs={'class':'form-control'}),
                    # 'si_date':forms.DateInput(attrs={'class':'form-control','type':'date','id':'si_date'}),
                    }

class SaleInvoiceNewForm(forms.ModelForm):
    class Meta:
        model = SaleInvoice
        fields = ('si_date','si_customer','si_project',)
        widgets = {
                    'si_customer':forms.Select(attrs={'class':'form-control'}),
                    'si_project':forms.Select(attrs={'class':'form-control'}),
                    'si_date':forms.DateInput(attrs={'class':'form-control','type':'date','id':'si_date'}),
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

class SaleInvoiceItemForm(forms.ModelForm):
    class Meta:
        model = SaleInvoiceItem
        fields = ('si_item','si_item_bill_quantity','si_item_tax_rate')
        widgets = {
                    'si_item':forms.Select(attrs={'class':'form-control'}),
                    'si_item_bill_quantity':forms.TextInput(attrs={'class':'form-control'}),
                    'si_item_tax_rate':forms.Select(attrs={'class':'form-control'}),
        }

class SelectItemFromSo(forms.Form):
    selected_item = forms.BooleanField(widget=forms.CheckboxInput(attrs={'value':'{{item.id}}'}))

    # class Meta:
    #     model = SaleOrderItem
    #     soipk = SaleOrderItem.pk
    #     fields = ('id',)
    #     widgets = {
    #                 'id':forms.CheckboxInput(attrs={'class':'form-control'})
    #     }

class InputInvoiceItemQuantity(forms.ModelForm):
    class Meta:
        model = SaleInvoiceItem
        fields = ('si_item_bill_quantity',)
        widgets = {
            'si_item_bill_quantity':forms.TextInput(attrs={'class':'form-control'})
        }
