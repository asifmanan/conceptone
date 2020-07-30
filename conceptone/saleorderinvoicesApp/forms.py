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

class SaleOrderInvoiceSearchForm(forms.Form):
    invoice_number = forms.CharField(label='Invoice Number', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control search_field'}))
    sale_order_no = forms.CharField(label='Sale Order No.', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control search_field'}))
    buyer_po_number = forms.CharField(label='Buyer PO No.', max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control search_field'}))
    buyer_po_date = forms.DateField(label='Buyer PO Date', widget=forms.DateInput(attrs={'type':'date','class':'form-control form-control search_field'}))

class SupplierSelectForm(forms.Form):
    class Meta:
        model = SaleOrderInvoice
        fields = (
                'supplier',
                'sale_order',
        )
        widgets={
                'supplier':forms.Select(attrs={'class':'form-control'}),
                'sale_order':forms.Select(attrs={'class':'form-control', 'disabled':'True'}),
        }
