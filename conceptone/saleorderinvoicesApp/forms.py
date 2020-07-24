from django import forms
from saleorderinvoicesApp.models import (
                                        SaleOrderInvoice,
                                        SaleOrderInvoiceItem,
                                        )
class SaleOrderInvoiceForm(forms.ModelForm):
    class Meta:
        model = SaleOrderInvoice
        fields = (
                'supplier',
                'sale_order',
                'invoice_number',
                'invoice_date',
                )
        widgets={
                'supplier':forms.Select(attrs={'class':'form-control'}),
                'supplier':forms.Select(attrs={'class':'form-control'}),
                'supplier':forms.TextInput(attrs={'class':'form-control'}),
                'invoice_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }
