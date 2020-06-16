from django import forms
from django.forms import (formset_factory, modelformset_factory)
from datetime import datetime
from purchaseApp.models import (PurchaseOrder,
                                PurchaseOrderItem,
                                )


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ('project','supplier','tax_rate', 'po_date',)
        widgets = {
                'project':forms.Select(attrs={'class':'form-control'}),
                'supplier':forms.Select(attrs={'class':'form-control'}),
                'po_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                'tax_rate':forms.Select(attrs={'class':'form-control'}),
                }

class PurchaseOrderItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderItem
        fields = ('item','order_quantity','purchase_price')
        widgets = {
                'item':forms.Select(attrs={'class':'form-control form-control', 'type':'date','id':'itemselect'}),
                'order_quantity':forms.TextInput(attrs={'class':'form-control form-control','id':'order_quantity','onchange':'auto_complete()'}),
                'purchase_price':forms.TextInput(attrs={'class':'form-control form-control','id':'purchase_price'}),
                }
