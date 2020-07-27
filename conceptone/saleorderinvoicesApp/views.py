from django.shortcuts import render, get_object_or_404, render_to_response
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django import forms
from django.views.generic import (
                                CreateView,
                                DeleteView,
                                FormView,
                                )
from saleordersApp.models import SaleOrder
from saleorderinvoicesApp.models import (
                                        SaleOrderInvoice,
                                        SaleOrderInvoiceItem,
                                        )
from saleorderinvoicesApp.forms import (
                                        SaleOrderInvoiceForm,
                                        )
# Create view for SaleOrderInvoice.
class CreateSaleOrderInvoice(CreateView):
    model = SaleOrderInvoice
    form_class = SaleOrderInvoiceForm
    template_name = 'saleorderinvoicesapp/create_saleorderinvoice.html'
    def form_valid(self,form):
        print("In form Valid")
        sale_order_invoice = form.save(commit=False)
        sale_order_invoice.supplier = sale_order_invoice.sale_order.supplier
        sale_order_invoice.save()
        return super().form_valid(form)

# AJAX CALL
def GetFormData(request):
    if request.GET.get('company') == "":
        data = 0
        # return
    company_id = request.GET.get('company')
    sale_order_list = SaleOrder.objects.filter(supplier__id=company_id)
    # form = SaleOrderInvoiceForm(initial={'supplier':'company_id'})
    form = SaleOrderInvoiceForm()
    # form.fields['supplier'].widget = forms.Select(attrs={'class':'form-control','readonly':'readonly'})
    form.fields['sale_order'].queryset = sale_order_list
    form.fields['supplier'].initial = company_id
    # form.fields['supplier'].widget.attrs.update({'readonly':'readonly'})
    form.fields['supplier'].disabled = True
    # form.fields['supplier'].widget.attrs.pop('required')
    form.fields['sale_order'].widget.attrs.pop('disabled')
    form.fields['invoice_number'].widget.attrs.pop('disabled')
    form.fields['invoice_date'].widget.attrs.pop('disabled')
    # print(form)
    return render(request,'saleorderinvoicesapp/_form_saleorderinvoice.html',{'form':form})
    # return HttpResponse(form)
