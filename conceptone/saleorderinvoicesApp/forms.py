from django import forms
from baseApp.models import Company
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
                'sale_order':forms.Select(attrs={'class':'form-control', 'disabled':'True'}),
                'invoice_number':forms.TextInput(attrs={'class':'form-control', 'disabled':'True'}),
                'invoice_date':forms.DateInput(attrs={'class':'form-control', 'type':'date','disabled':'True'}),
        }
