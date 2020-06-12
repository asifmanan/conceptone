from django import forms
from django.forms import (formset_factory, modelformset_factory)
from datetime import datetime
from purchaseApp.models import (PurchaseOrder,
                                OrderItem,
                                )


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ('project','po_number','supplier','tax_rate', 'po_date',)
        widgets = {
                'project':forms.Select(attrs={'class':'form-control'}),
                'supplier':forms.Select(attrs={'class':'form-control'}),
                'po_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                'po_number':forms.TextInput(attrs={'class':'form-control'}),
                'po_tax':forms.Select(attrs={'class':'form-control'}),
                }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('item','order_quantity','purchase_price')
        widgets = {
                'order_item':forms.Select(attrs={'class':'form-control form-control-sm', 'type':'date','id':'itemselect'}),
                'order_quantity':forms.TextInput(attrs={'class':'form-control form-control-sm','id':'order_quantity','onchange':'auto_complete()'}),
                'purchase_price':forms.TextInput(attrs={'class':'form-control form-control-sm','id':'purchase_price'}),
                }
