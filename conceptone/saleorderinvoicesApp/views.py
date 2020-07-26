from django.shortcuts import render, get_object_or_404, render_to_response
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
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

# AJAX CALL
def GetFormData(request):
    if request.GET.get('company') == "":
        data = 0
        # return
    company_id = request.GET.get('company')
    sale_order_list = SaleOrder.objects.filter(supplier__id=company_id)
    # form = SaleOrderInvoiceForm(initial={'supplier':'company_id'})
    form = SaleOrderInvoiceForm()
    form.fields['sale_order'].queryset = sale_order_list
    form.fields['supplier'].initial = company_id
    form.fields['supplier'].disabled = 'disabled'
    form.fields['sale_order'].widget.attrs.pop('disabled')
    form.fields['invoice_number'].widget.attrs.pop('disabled')
    form.fields['invoice_date'].widget.attrs.pop('disabled')
    # print(form)
    return render(request,'saleorderinvoicesapp/_form_saleorderinvoice.html',{'form':form})
    # return HttpResponse(form)
