from django import forms
from django.forms import formset_factory, modelformset_factory
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import DecimalValidator
from salesApp.models import (SaleOrder,
                                SaleOrderItem,
                                SaleInvoice,
                                SaleInvoiceItem,
)

class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = (
                    'so_number','customer_po_date','customer_po_number','customer',
                    'project',)
        widgets = {
                    'so_number':forms.TextInput(attrs={'class':'form-control'}),
                    'customer_po_date':forms.DateInput(attrs={'class':'form-control','type':'date','id':'so_podate'}),
                    'customer_po_number':forms.TextInput(attrs={'class':'form-control'}),
                    'customer':forms.Select(attrs={'class':'form-control'}),
                    'project':forms.Select(attrs={'class':'form-control'}),
                    }

class SaleInvoiceSoForm(forms.ModelForm):
    class Meta:
        model = SaleInvoice
        fields = ('sale_order',)
        widgets = {
                    'sale_order':forms.Select(attrs={'class':'form-control'}),
                    # 'si_date':forms.DateInput(attrs={'class':'form-control','type':'date','id':'si_date'}),
                    }

class SaleInvoiceNewForm(forms.ModelForm):
    class Meta:
        model = SaleInvoice
        fields = ('si_date','customer','project',)
        widgets = {
                    'customer':forms.Select(attrs={'class':'form-control'}),
                    'project':forms.Select(attrs={'class':'form-control'}),
                    'si_date':forms.DateInput(attrs={'class':'form-control','type':'date','id':'si_date'}),
                    }

class SaleOrderItemForm(forms.ModelForm):
    class Meta:
        model = SaleOrderItem
        fields = (
                    'item','order_quantity','unit_price',
                    'tax_rate',
                    )
        widgets = {
                    'item':forms.Select(attrs={'class':'form-control'}),
                    'order_quantity':forms.TextInput(attrs={'class':'form-control'}),
                    'unit_price':forms.TextInput(attrs={'class':'form-control'}),
                    'tax_rate':forms.Select(attrs={'class':'form-control'}),
        }

class SaleInvoiceItemForm(forms.ModelForm):
    class Meta:
        model = SaleInvoiceItem
        fields = ('sale_order_item','bill_quantity','tax_rate')
        widgets = {
                    'sale_order_item':forms.Select(attrs={'class':'form-control'}),
                    'bill_quantity':forms.TextInput(attrs={'class':'form-control'}),
                    'tax_rate':forms.Select(attrs={'class':'form-control'}),
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

# class InputInvoiceItemQuantity(forms.ModelForm):
#     class Meta:
#         model = SaleInvoiceItem
#         fields = ('si_item_bill_quantity',)
#         widgets = {
#             'si_item_bill_quantity':forms.TextInput(attrs={'class':'form-control inv-qty-input border-0 rounded-0',
#                                                             'label':''})
#         }
# invoice_item_formset = modelformset_factory(InputInvoiceItemQuantity,extra=10)

invoice_item_formset = modelformset_factory(
    SaleInvoiceItem,
    fields=('bill_quantity', ),
    extra=0,
    widgets={'bill_quantity': forms.TextInput(attrs={
            'class': 'form-control',
            'required':'required',
            'placeholder': '<Invoice Quantity>'
        })
    }
    # widgets={'si_item_bill_quantity': forms.DecimalField(validators=[DecimalValidator(max_digits=14, decimal_places=2)],attrs={
    #         'class': 'form-control',
    #         'required':'required',
    #         'placeholder': '<Invoice Quantity>'
    #     })
    # }
)
